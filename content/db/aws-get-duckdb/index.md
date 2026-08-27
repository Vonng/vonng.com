---
title: "AWS 收购 DuckDB：鸭子飞进亚马逊雨林"
date: 2026-08-26
authors: [vonng]
summary: >
  AWS 买走了做鸭子的人，把鸭子留给了基金会。
tags: [DuckDB, AWS, 数据库, 开源]
---

> [微信原文](https://mp.weixin.qq.com/s/xaXQvJMFfZ1tpPMd6vFaxA) | 2026 年 8 月 26 日

8 月 26 日，亚马逊官宣：AWS 已与 DuckDB 背后的公司 DuckLabs 签署最终收购协议，预计 9 月初交割，金额未披露。团队留在阿姆斯特丹，DuckDB、DuckLake、Quack 三个项目继续以 MIT 协议开源，挂在独立的 DuckDB 基金会名下。

公告里有一句话写得很讲究：「我们并不是在收购 DuckDB 开源项目」。这话不假，但这笔交易的机关也全在这里：**项目留给基金会，人归我。**

![DuckLabs 加入 AWS 的官方公告](acquisition.webp)

先交代一下背景。DuckLabs 是阿姆斯特丹 CWI（荷兰数学与计算机科学研究中心）的学术 spin-off，Hannes Mühleisen 和 Mark Raasveldt 两位博士 2018 年在 CWI 动手写 DuckDB，之后拉起了公司。

三十来号人，零 VC 融资，股东就是创始人和员工自己，靠支持合同和开发合同养活自己，典型的欧洲小作坊。就是这么一个小作坊，做出了如今每天被下载三百多万次的分析数据库，把一票融了几亿美金的同行按在地上摩擦。现在，它被 AWS 整锅端走了。

## 时间点

这笔收购最有意思的地方在时间线上。8 月 17 日，DuckDB 放出 2.0 前瞻：全新的客户端协议 Quack 登场，外加多进程并发读写。九天之后，8 月 26 日，AWS 官宣收购。

这九天透露出来的信息，比公告本身还多。DuckDB 此前一直是个进程内的嵌入式库，好用，但没法直接拿去卖。有了客户端协议之后，它就不再是一个库，而是一台可以被托管、被计费、被塞进云控制台的服务器。

![DuckDB 2.0 预告](v2-preview.webp)

嵌入式的 DuckDB 是开发者的工具，带协议的 DuckDB 是云厂商的印钞机。AWS 偏偏在鸭子长出翅膀这一刻出手，说是巧合，我反正不信。

Hannes 自己在表态里也把牌摊开了：AWS 带来的规模和触达，能让更多用户用上这项技术，包括那些最终依赖 Duck Stack、但不需要自己运维数据库的人。

最后半句就是产品预告。我在这里立一个可以被打脸的 flag：今年 12 月的 re:Invent 上，大概率会出现基于 DuckDB 的托管服务，形态或许是 S3 的原生查询引擎，或许干脆就叫 Amazon DuckDB 或者 Amazon Quack。

## 出手的不是 Redshift，是 S3

另一个容易被略过的细节是，替 AWS 出面站台的人是 Andy Warfield：AWS 副总裁、Distinguished Engineer，S3 的掌门人。他说双方已经密切合作了两年，联手把 DuckDB 塞进了 S3 Tables 和 SageMaker Lakehouse，还夸 DuckDB 被 S3 客户广泛使用、深受喜爱。

买鸭子的不是 Redshift 团队，是 S3 团队，这个差别很要紧。因为 Amazon 自己的数据仓库产品 Redshift 和 Athena 都实在太拉胯了。AWS 官方的措辞其实已经透露方向：收购 DuckLabs 是为了让 AWS analytics “faster, simpler, and more cost-effective”，比较对象是谁不言而喻。

这几年整个云上数据基础设施都在往对象存储上搬家，各路「XXX over S3」层出不穷。文件系统与数据库这对冤家的恩怨，我在《[DB vs FS：相爱相杀 50 年](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492480&idx=1&sn=0206fb23192ae5f7aff0d24f0a1782b8&scene=21#wechat_redirect)》里聊过。S3 自己也没闲着，先把 Iceberg catalog 直接做进存储服务（S3 Tables），现在又把这颗星球上最擅长读对象存储的查询引擎团队整个买下。对象存储正在长出计算能力，而查询引擎正在沦为存储的配件。

放进牌局里看就更清楚了：Databricks 手握 Delta 与 Unity Catalog，Snowflake 有 Polaris，如今 AWS 凑齐了 S3 Tables + DuckDB + DuckLake。湖仓三国杀，齐活了。

## 买人不买项目

镜头拉远一点，这笔交易只是一个更大序列里的最新一单。

MySQL 当年连人带项目十亿美金卖给 Sun，再被 Oracle 一锅端，那是旧模式，代价是社区至今心有余悸。Citus 2019 年卖给微软，算是中间态。前年 Rockset 卖给 OpenAI，去年 Neon 十亿美金卖给 Databricks、Crunchy Data 卖给 Snowflake。包括最近 pg_mooncake / electricSQL 卖身——数据库引擎的人才，正在被平台公司成建制地收编。

AWS 这次的姿势是其中最精致的一种。还记得当年 Elastic 换协议，指着 AWS 的鼻子骂「strip mining」吗？AWS 被迫 fork 出 OpenSearch，后来干脆捐给了 Linux 基金会。骂挨了，乖也学了。所以这回的话术无懈可击：项目不碰，留在基金会，章程保证 MIT 永续，我们只是雇佣了全部核心开发者而已。既堵住了「吞并开源」的悠悠之口，又实实在在攥住了路线图。上一个十年，云厂商白嫖开源；这一个十年，云厂商直接把上游买成自己的员工。

![DuckDB 关于开源项目不变的承诺](foundation.webp)

平心而论，站在 DuckLabs 的角度，这个归宿不丢人，甚至可以说体面。他们早在 2022 年就坦承过，光靠咨询与支持合同的模式撑不起规模。这次官宣配套的承诺也确实是加分项：扩大基金会的角色，设立商业用户顾问委员会，开放扩展签名让第三方组织也能发布扩展，以及用他们自己的话说，消除把免费用户转化为付费支持客户的商业压力。

说白了，以前得靠卖支持恰饭，现在有亚马逊发工资，反而可以把生态放得更开。这跟 SQLite 靠财团供养的模式神似，区别只在于 SQLite 的金主是一个财团，而 DuckDB 的金主从今往后只有一家。而单一金主，恰恰是真正的问题所在。

## 一个属于世界，一个属于亚马逊

我此前讲过一个判断：数据世界正在收敛出几个默认答案，数据库的默认答案是 PostgreSQL，对象存储的默认答案是 S3，而分析的默认答案会是 DuckDB。这次收购等于 AWS 用真金白银替我确认了第三条。

可惜 DuckDB 本来可以算个「不由单一实体说了算」的案例。从今天起，这个对称性破了一半。DuckDB 项目确实还在基金会，MIT 确实永续，但核心开发者几乎全员领同一家公司的工资，而这家公司是全世界最大的云。

PostgreSQL 的强健，恰恰在于核心贡献者的雇主是散的：EDB、微软、AWS、富士通、NTT、Crunchy Data……谁也不占多数，谁也别想一言堂，哪家想夹带私货，社区里有的是人跟你拍桌子。DuckDB 从今天起暂时失去了这个性质，基金会还在，但基金会里坐着的人，胸牌都印着同一个 logo。

当然，天也没塌。MIT 协议摆在那里，真到了变卦那天，社区手里还有终极武器，那就是 fork。Redis 前脚改协议，Valkey 后脚立地成佛，殷鉴不远。但结构性风险从零变成了非零，这笔账，用 DuckDB 的人心里要有数。

三个默认答案如今的格局是：PG 属于世界，S3 属于亚马逊，DuckDB 悬在半空，基本上也要属于 Amazon。

![亚马逊雨林里的鸭子与鳄鱼](featured.webp)

## 最坐立难安的是 MotherDuck

这笔交易里还有一只当事鸭，处境瞬间变得微妙，那就是 MotherDuck。

给不熟的读者补个背景：MotherDuck 是拿了约一亿美金 VC 的创业公司，创始人 Jordan Tigani 是前 BigQuery 老兵，商业模式就是「云上的 DuckDB」，基础设施跑在 AWS 上。DuckDB 官方 FAQ 里白纸黑字写着两层关系：MotherDuck 与 DuckLabs 签有开发服务合同，DuckLabs 持有 MotherDuck 的股份。

于是 AWS 买下 DuckLabs 之后，AWS 间接成了 MotherDuck 的股东，MotherDuck 核心引擎的外包开发方变成了 AWS 的全资子公司，而 MotherDuck 卖的东西，恰好是 AWS 接下来最可能亲自下场卖的东西。甲方、乙方、股东、房东，如今全是一家人。

更巧的是，就在官宣前一两天，MotherDuck 刚刚收购了 Tower，一家支撑其数据管道功能的基础设施小厂，用来补自己的工程班底。

## 鸭子范式：元数据进 PG，数据放 S3

聊完资本，说回技术。AWS 到底看上了什么？我认为答案有两层。

第一层是范式。DuckLake 的架构说穿了就一句话：元数据进数据库，用 PostgreSQL；数据进对象存储，落成 S3 上的 Parquet；计算则交给无状态、随起随灭的 DuckDB。它不只是又一个表格式，而是把「Iceberg + 各家 Catalog」整个栈端掉的路数。元数据本来就是关系型的，塞回关系型数据库里天经地义，何必用一堆 JSON 文件在对象存储上模拟一个蹩脚的数据库？

进行这项尝试的，还有刚刚被 Snowflake 收购的 Crunchy Data，他们搞的 pg_lake 也是几乎一样的思路，只不过选择在 PG 中做这件事，继承 PG 的权限模型，而不是像 DuckLake 一样让你自己去 DIY。

主数据放对象存储、元数据放 PG，这个套路正在成为新一代数据系统的标准姿势。不用看远，我朋友蒋老板最近攒的四个数据库，图数据库也好、消息队列也好，无一例外全是这个架构。这不是巧合，这是范式。而如今范式的原作者进了 AWS，范式本身只会加速成为行业标准。

第二层是时代。每天三百多万次下载，你以为背后是三百万个数据分析师？相当一部分是 AI agent。零配置、单二进制、进程内、即用即抛，DuckDB 是 agent 干数据活时的本能选择，DeepSeek 的 smallpond 拿它配 3FS 攒分布式分析，就是现成的例子。AWS 买的不只是一个 OLAP 引擎，买的是 agent 时代数据处理的默认心智。

## 尾声

几年前我把 DuckDB 整合进 Pigsty 的时候，它还只是极客圈子里的小众玩具。我很早之前就觉得，除了 PostgreSQL 之外最有前景的数据库就是 DuckDB，话音未落，AWS 用支票投了同一票。

![作者对 PostgreSQL 与 DuckDB 的评价](db-ranking.webp)

![PGCon.Dev 2024 上的数据库可扩展性评价](extensibility.webp)

接下来的剧本不难猜：AWS 会把托管版 Duck Stack 端上货架，广告词 Hannes 已经替它写好了——让用户依赖 Duck Stack，而不必自己运维数据库。

这个故事的镜像，是自建版的 Duck Stack：PostgreSQL 管元数据，MinIO / Silo / RustFS 之类的对象存储放数据，DuckDB 跑计算，全套开源，一分钱订阅费不用交给贝索斯。巧了，这三样东西，Pigsty 里一样不缺。

![Pigsty 数据基础设施全家桶](pigsty.webp)

一行命令，你就可以在自己的 Linux 服务器上，拥有生产级的高可用 PostgreSQL 集群，生产级的 Silo / MinIO（下个版本加入 RustFS 支持）对象存储集群，以及开箱即用的 DuckDB 与 PG DuckDB 全家桶扩展。

市场教育，亚马逊已经替所有人做完了，剩下的是一道选择题：数据的家底，是托付给雨林，还是攥在自己手里。

三十年，数据世界才收敛出三个默认答案。而让其中一个易主，只需要一份签好字的协议。愿鸭子在雨林里飞得高，也愿它落地的时候，还认得基金会的门。

---

**参考链接**

1. [AWS to acquire DuckLabs（亚马逊官方公告）](https://www.aboutamazon.com/news/company-news/aws-ducklabs)
2. [Techzine：Developer DuckDB to be acquired by AWS](https://www.techzine.eu/news/analytics/143855/developer-duckdb-to-be-acquired-by-aws/)
3. [SiliconANGLE：AWS buys DuckLabs](https://siliconangle.com/2026/08/26/aws-buys-ducklabs-to-bring-duckdbs-embeddable-analytics-to-more-enterprises/)
4. [DuckDB FAQ（DuckLabs 与 MotherDuck 的关系）](https://duckdb.org/faq)
5. [DuckLabs 2022 年 MotherDuck 合作公告](https://ducklabs.com/news/2022/11/15/motherduck-partnership)
6. [The New Stack：MotherDuck 收购 Tower](https://thenewstack.io/motherduck-tower-acquisition-python/)
