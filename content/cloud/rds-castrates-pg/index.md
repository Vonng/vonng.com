---
title: "RDS阉掉了PostgreSQL的灵魂"
date: 2024-03-14
authors: [vonng]
summary: >
  RDS 上缺少了许多重要扩展，用户无法在 RDS 上自由加装扩展，而这些强力扩展也注定不会出现在云RDS中。
tags: [PostgreSQL, RDS, 扩展]
---

在上一篇《[**PostgreSQL 正在吞噬数据库世界**](/pg/pg-eat-db-world/)》中，我们提到，尽管 PostgreSQL 是世界上最先进的开源关系型数据库，但其独一无二的特点在于其**极致可扩展性，与繁荣的扩展生态**！

不幸地是，**云上的 RDS 阉割掉了 PostgreSQL 的灵魂** —— 用户无法在 RDS 上自由加装扩展，而一些强力扩展也注定不会出现在 [**RDS**](/cloud/rds/) 中。使用 RDS 无法发挥出 PostgreSQL 真正的实力，而这是一个对云厂商来说无法解决的缺陷。

## RDS 缺失重要扩展

在 PostgreSQL 生态中有着**上千**<sup>[1]</sup>的扩展插件，为 PostgreSQL 在各种方向上添加可选的功能模块。其中不乏一些超级强力的扩展（例如地理空间扩展 PostGIS 有 170 万行代码，而 PostgreSQL 内核只有一百万行）

我们为最新的 PostgreSQL 16 选出了 16 个具有代表性功能的生态扩展 —— 或者是提供某个细分领域的强力特性，或者是对于生产运维必不可少。并观察云厂商 RDS 对其支持的状态，而结果只能用惨不忍睹形容：

![图片](01.webp)

> 本地 RDS / 阿里云 RDS / AWS RDS 对 16 个主流扩展的支持情况

对于 PG 的杀手级特性 PostGIS，两家云厂商都有支持，阿里云海提供了自己的时空扩展 Ganos，把生态里其他一些相关的能力比如 PointCloud 也弄了进去。最近的当红炸子鸡向量数据库扩展 pgvector AWS 有跟进，但阿里云用的还是自家土法手搓的 pase。

作为本土云厂商，阿里云 RDS 提供了中文分词的扩展 `zhparser` 和 `pg_jieba`。最后是运维必不可少的两个扩展：治理膨胀的 pg_repack 和 wal2json AWS RDS 都齐全，但阿里云 RDS 依然没有提供 PG 16 的 wal2json 扩展。

然而，两家云厂商都只提供了 5/16 的重要扩展，其他一些重要的功能，比如时序数据库扩展 TimescaleDB，分布式数据库扩展 Citus，列式存储扩展 Hydra，库内机器学习 PGML，ElasticSearch 全文检索扩展 pg_bm25，图数据库扩展 AGE，库内 GraphQL 查询扩展 PG GraphQL，OLAP 加速扩展 pg_analytics，消息队列 PGQ，嵌入式分析 DuckDB 支持全部缺位了！

![图片](02.webp)

更重要的是，云 RDS 不可能给用户自行加装扩展的能力。而这些缺失的扩展，也基本上不太可能出现在 RDS 中

---

## 为什么 RDS 不提供扩展？

RDS 不提供这些重要扩展的原因，也许与多租户安全策略与开源协议有关。因为这些扩展大多采用了 AGPLv3 开源协议。AGPLv3 协议的特点就是专治云厂商白嫖开源 —— **如果云厂商将这些扩展纳入 RDS 中，他们就必须将 RDS 管控软件开源**。

在《[**DBA 会被云淘汰吗？**](/cloud/dba-vs-rds/)》我们已经深度讨论过云 RDS 的商业模式，沉淀了 DBA 经验的管控软件，是云数据库的核心生产资料与[**摇钱树**](/cloud/rds/)。核·月单位成本 20 块钱的硬件资源，套上管控软件，就能卖出 300～400（Aliyun），甚至 400～ 800（AWS）这样几十倍的天价——云厂商也许会把自己魔改的数据库内核与扩展开源，但是绝不可能把自己的真正核心软件 —— 管控开源的。

AGPLv3 是专门用于遏制云厂商和同业白嫖的开源协议，**对于终端用户来说，AGPLv3 却没有什么影响** —— 终端用户既没有兴趣去魔改软件，也几乎没人会把数据库作为托管服务对外提供。而用户通过客户端、命令行、脚本使用、管理这些 AGPLv3 组件的代码并没有任何开源义务，作者也压根没有对云/同行之外的用户进行追索的兴趣。

不过从另一个角度来说，现在已经出现了开源的 RDS 管控 —— [**Pigsty**](/pigsty/better-rds-alternative/)，那么云厂商开不开源管控其实也不重要了。正好比弹性算力调度有了 K8S 这个标准后，大家已经不在意底下到底是物理机、虚拟机，EC2 还是 ECS 了。

> [范式转移：从云到本地优先](/cloud/paradigm/)

---

## 附录：RDS 提供的扩展

上面我们列了 16 个重要扩展的支持情况，如果我们拉一个完整的扩展清单，这里面缺少的插件还要更多。

Contrib 模块作为 PostgreSQL 本体的一部分，已经包含了 73 个扩展插件，加上 PostgreSQL 官方仓库 PGDG 收录的约 100 个扩展，Pigsty 作为 PG 发行版自身维护打包了 20 个强力扩展插件，在 EL/Deb 平台上总共可用的扩展已经达到了 234 个 —— 覆盖了 PG 生态的主要有生力量。

然而云上的 RDS 却在这一方面存在极大的缺陷。例如，AWS RDS 只提供了 94 个扩展，阿里云 RDS 提供了 104 个扩展。在 PG 自带的 73 个扩展中，阿里云保留了 23 个阉割了 49 个；AWS 保留了 49 个，阉割了 24 个。

进一步刨除 PGDG 仓库里原本就有的扩展，阿里云独有的扩展仅有：ganos，tde，index-adviser，pasee，rds_ccl 等。AWS 独有的扩展稍微多一些：pg_transport，pgactive，pg_tle，log_fdw，flow_control，aws_s3，aws_lambda，aws_commons，rds_tools。

下面是刨除 PostgreSQL 16 自带的 73 个扩展后，开源本地优先的 Pigsty RDS，阿里云 RDS，AWS RDS 提供的扩展列表：

### Pigsty 开源 RDS 提供的扩展清单

完整清单：<https://pigsty.cc/docs/pgsql/ext/>

![图片](03.webp)

### 阿里云 RDS 提供的扩展清单

完整清单：<https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/extensions-supported-by-apsaradb-rds-for-postgresql>

![图片](04.webp)

### AWS RDS 提供的扩展清单

完整清单：<https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-extensions.html>

![图片](05.webp)

### References

- `[1]` 1 千个 PG 扩展列表： <https://gist.github.com/joelonsql/e5aa27f8cc9bd22b8999b7de8aee9d47>

---

发布版本：[微信公众号](https://mp.weixin.qq.com/s/EH7RPB6ImfMHXhOMU7P5Qg)
