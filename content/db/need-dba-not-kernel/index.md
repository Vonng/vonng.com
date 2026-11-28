---
title: "不缺好数据库内核，缺能用好数据库的DBA"
date: 2025-05-18
authors: [vonng]
summary: >
  最近知乎上的老问题 “postgresql也很强大，为何在中国大陆，mysql成为主流，postgresql屈
tags: [数据库, 职业, 技术评论]
---
最近知乎上的老问题 “postgresql 也很强大，为何在中国大陆，mysql 成为主流，postgresql 屈居二线呢？” 冒出来几个新答案

> [!SOCIAL] 知乎提问
>
> **postgresql也很强大，为何在中国大陆，mysql成为主流，postgresql屈居二线呢？**
>
> postgresql能否替代mysql?
>
> 我感觉postgresql非常强大，很多地方超过了mysql。
> 举几个例子：
>
> 1. 丰富的数据类，支持数组、字典、json、序列号。
> 2. 强大的审计函数
> 3. 强大的索引，易于sql调优
>
> postgresql在许多地方，有mysql无法比拟的优势。
>
> 但是在中国大陆，许多公司的核心业务库，都是mysql，postgresql则屈居二线，作为审计类的数据库来使用。
>
> 为什么不让postgresql来扛大梁呢，而要用mysql，postgresql不合适么?
{platform="zhihu"}

有朋友转给我，问我怎么看。

> [!SOCIAL] 八舞耶俱矢
>
> 我来给PostgreSQL泼冷水。PG算是好用而非实用。
>
> 著名的“十大问题”：10 Things I Hate About PostgreSQL | by Rick Branson | Medium
>
> 十大问题从上个世纪90年代至今无一彻底解决，PG开发者甚至不承认是问题，将其视作feature。
>
> 因为这十大问题已经是一堆屎山层层叠叠，不是能一点点独立解决的。想要解决，就得要大规模重构才有可能。
>
> ---
>
> PG对于不能运行长事务，已经是一条层层套娃的铁律了。
>
> 1. WAL机制影响范围过大，但是非常脆弱。WAL出问题就是整个PG集群有问题。
> 2. 为了解决页断裂的问题，PG将数据full page write到WAL，导致WAL容易膨胀。
> 3. 32位XID问题，PG永远的长事务无缘。
> 4. MVCC机制问题，PG的堆表tuples，导致必须VACUUM。目前流行的透明页压缩和堆表tuples完全无缘。
> 5. VACUUM又受到最小事务影响。
>
> 如果真的要运行一个长事务呢？PG很容易当场爆炸给你看：
>
> 1. WAL急速膨胀，占用大量磁盘空间
> 2. PG的堆表tuples也急速膨胀，无法VACUUM回收磁盘空间。
> 3. 最后XID回环来一个致命一击。
>
> 因为32位XID不能运行长事务，所以不会解决WAL膨胀问题，也不会解决VACUUM依赖最小事务的问题，所以也没有动力换堆表tuples，所以32位XID还能苟住。
>
> 这是一个feature啊。
>
> ---
>
> 原生的逻辑复制不支持DDL，匪夷所思啊。20s年了竟然还有数据库不支持DDL复制。
>
> ---
>
> 如果要使用pg，一定要严格避讳那几条铁律。
>
> 第一推荐是直接用云数据库RDS就好了，上面的烦恼能免除大半。
>
> 其次要自建的话，就用pigsty这些成体系的postgresql发行版，其完善的插件和监控能尽量避免陷入pg的陷阱。
>
> 第三是用opengauss，polorx这些国产化pg，对pg原有痛点有诸多改进。
>
> 最后是自己编译打包一个简陋版pg，集成自己的必要插件。
>
> 千万不要直接用pg的原生版本自建。
{avatar="avatar-bawuyejushi.webp" platform="zhihu"}

我觉得说的挺好的，老冯的看法是，最狭义上的 PostgreSQL 内核并不是一个 “产品”，而是一个 “项目”。直接裸使用 PostgreSQL 内核本身，其实是有不少问题与坑的。而这些问题与坑，就是 DBA，RDS，发行版，以及商业产品要去解决的。

如果你用 Linux 操作系统就很好理解，没什么人会直接去使用 Linux 裸内核的。大家使用的都是 RedHat，Debian，Ubuntu 这样的操作系统发行版。一个 Linux Kernel 才几 MB，但是一个操作系统发行版的软件包加一块儿可以塞进几张 DVD （十几 GB），你还需要 systemd，定时任务，时间同步，DNS 解析，日志等各种组件才能将这个裸 Linux Kernel 包装成一个实用的操作系统

例如，PostgreSQL 生态里有着 1000+ 扩展插件。像 PostGIS 这样的扩展代码（170 万行）甚至比 PostgreSQL 本身（100 万行）还要多。有着好几本专著和自己的子社区。更别提最近蓬勃发展的向量/DuckDB/Tantivy 扩展缝合大赛了。如果你什么 PG 扩展都没用过，那我可以肯定的判断你错过了 PG 生态的精髓。

![图片](03.webp)

在运维与服务搭建上也同理，如果只是 yum install postgresql systemctl start 这样安装 PG 裸内核，那属实连 门都没有入。一套生产级，企业级的 PostgreSQL 数据库服务一定是成体系的。围绕内核通过架构/扩展来解决各种裸内核的问题。例如：

- 高连接数性能下降，那么就需要 pgbouncer 链接池
- 内核本身不能高可用，但是 patroni 可以提供高可用
- 备份与时间点恢复，需要用到 pgbackrest
- 采集监控指标，需要用到 pg_exporter
- XID 回卷和磁盘写满，那么就一定要有监控告警
- 表有膨胀，那么用于在线治理膨胀的 `pg_repack` 就属于必选扩展

上面的每一个问题，都会有几种不同的备选组件，堪称是 FOSS 展销会大舞台，那么哪一个是最好的？有什么坑没有。

对于一个可靠的 PG 服务而言，这些生态组件的使用经验甚至比 PostgreSQL 内核经验更重要。而这种将开源零件组装为企业级服务的 “最佳实践” 的经验是 **极为极为极为稀缺的**。

---

因此，另一个值得一提的答案来自 @kimmking：“其实国内 PG 没有普及的关键在于严重缺少 DBA。”

> [!SOCIAL] kimmking
>
> 恕我直言，最大的原因可能不是生态、也不是先发优势，而是：国内没有多少资深的PG DBA。
>
> 曾经在多个核心项目里使用PG或其变体，出了底层问题，找来很多所谓的PG大牛，都搞不清楚。
>
> 比如本题下有不少答主提到的vacuum的内存回收问题、数据文件出错后的恢复和处理问题，我们之前也在十万级TPS级别上，遇到内存无法及时回收的问题，找到了很多专家，都没找到几个能真正在内核源码级的理解和排查分析问题的人（包括某些云厂商的数据库技术团队）。
{avatar="avatar-kimmking.webp" platform="zhihu"}

早些年，国内互联网场景用 PostgreSQL 的就是探探和去哪儿，金融领域就是平安银行。能称得上“复杂/规模” 也就这几个，而这样一个公司能有几个 DBA 坑位？而这里的 DBA 又有多少是经过大故障洗礼，或者愿意精益求精深挖研究下去的？高级的 DBA 是甲方用真金白银的故障砸出来的。国内 PG 圈子很小，像这种在内核层面分析问题的 PG DBA 不客气地说两只手就能数出来了。

我认为对于 PostgreSQL 来说，DBA 这个 Title 其实很有误导性，因为 PostgreSQL 只是一个 “发动机” 零件，而不像 Oracle 那种直接买的 “整车”。Oracle DBA  是对照手册进行操作的 “司机”，属于数据库解决方案的一部分。而 PostgreSQL "DBA" 实际上是要自己去设计解决方案，用开源零件攒车的架构师。这也是为什么堪用 PG DBA 如此少的原因 —— 会造车的工程师要比会开车的司机稀缺太多了。

但是有一个办法可以解决这个问题，就是直接用已经经过长期大规模实战考验的体系化攒车方案（甚至是自动驾驶方案），而这也是我做 Pigsty 的原因。让 PostgreSQL 用户跳过 “攒车” 阶段，直接开车即走，甚至连司机都不一定需要了。

- [DBA 会被云淘汰吗？](/cloud/dba-vs-rds/)
- [驳《再论为什么你不应该招 DBA》](/cloud/no-dba-bullshit/)
- [云数据库是不是智商税](/cloud/rds/)
- [DBA 不是数据库的用户，开发者才是！](/cloud/developers-are-db-users/)
- [数据库的“萝卜快跑”时刻已到，DBA 请下车](https://mp.weixin.qq.com/s/vceZUVrVTIEljVDNkuY47w)

---

发布版本：[微信公众号](https://mp.weixin.qq.com/s/lqYYHA45hdqh4sPQWv5t8A)
