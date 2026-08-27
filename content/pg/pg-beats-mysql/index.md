---
title: "PostgreSQL取得对MySQL的压倒性优势"
date: 2025-03-01
authors: [vonng]
summary: >
  在全球云厂商中，PostgreSQL的规模与增速远超MySQL，这场纷争已经不再有任何悬念了 —— PostgreSQL 将成为数据库世界的 Linux，而 MySQL 会成为数据…
tags: [PostgreSQL, MySQL, 技术评论]
---

昨天在 X 上看到暴跳发了个帖。暴跳以前是 PolarDB InnoDB 引擎的负责人，现在是阿里云 RDS PG + MySQL 的头儿：

![图片](01.webp)

所以虽然这是个 “我朋友说” 的疑问句式，但我也并不怀疑这个数字的真实性。大概在两年～三年前，AWS 上 PostgreSQL 的实例数量刚好超过 MySQL，而按照这两年 PG 发展的迅猛势头，从 1:1 提升到 3:2 也并不算离谱。

![图片](02.webp)

[StackOverflow 2024调研：PostgreSQL已经超神了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488057&idx=1&sn=6733b62b5cd48c62acd798fc48db1c92&scene=21#wechat_redirect)

------------------------------------------------------------------------

当然，在去年 PGCon.Dev 上我也特意问了 AWS 的人，他们没说具体的比例，但告诉我无论是按实例数量算还是按 CPU 数量算，PostgreSQL 都已经比 MySQL 更多了。特别是 PostgreSQL 实例的平均规格要比 MySQL 大，所以如果按照 CPU 核数来算的话，PostgreSQL 就比 MySQL 多更多了。

其实从 AWS 的产品发布与技术投入路线来看，不难看出全球云计算一哥已经把重注都下在了 PostgreSQL 上，首先整个 RDS （MySQL + PGSQL）的产品经理就是 PostgreSQL 社区核心组成员 Jonathan Katz ，近两年 PG/PGVECTOR 在向量数据库领域嘎嘎乱杀，背后的主要推手和贡献者就是 AWS。

然后最近的 Aurora 新品分布式 DSQL 只有 PostgreSQL 兼容，没搞 MySQL 的，放在以前这种事从来都是 MySQL 先上的。

![图片](03.webp)

------------------------------------------------------------------------

与此同时，其他公司也继续在 PostgreSQL 发力。除了先前持续维护的分布式扩展 Citus 之外，最近微软还开源了 DocumentDB，一款将 PostgreSQL 转换为 MongoDB 的扩展 —— 而且支持与 Citus 深度融合，提供分布式文档数据库的能力。

![图片](04.webp)

当然国内的情况比较特殊，市场会滞后几年。我也特意和阿里云的朋友聊过这个事。作为国内云数据库一哥，目前他们 RDS MySQL 实例数量依然远高于 PostgreSQL。但这两年在增速上，PostgreSQL 显著超过 MySQL 了。而且阿里云用来主推信创国产化市场的 PolarDB 也是 PostgreSQL 路线，PolarDB Oracle 则是 PolarDB PG 的二级衍生分支。

当然，如果我们把目光投向前端开发者使用的 Serverless 云数据库，这个趋势就更明显了。例如在 Vercel 上，推荐的 7 个数据库存储中，四个是直接基于 PostgreSQL，两个 Redis，一个 DuckDB，根本没有 MySQL 什么事。最活跃的数据库用户群体已经系统性的抛弃 MYSQL 了。

![图片](05.webp)

> Neon / Nile / Supabase / Gel (原名 EdgeDB) 都是 PostgreSQL 封装

毫无疑问，[PostgreSQL 正在吞噬数据库世界](/pg/pg-eat-db-world/)， MySQL 作为数据库领域中 PostgreSQL 最大的竞争对手之一（另一个是 Oracle），正在面临严峻的挑战。

我认为 [MySQL 最大的失策就是错过了向量数据库 AI 这一波](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488000&idx=1&sn=7cbc71f4220ef50e967b88771a0fd00a&scene=21#wechat_redirect)巨大的增量。PostgreSQL 凭借内嵌足够好的 pgvector ，几乎碾压了整个专用向量数据库领域，成为 AI 时代的事实数据库标准。成为了最近几年数据库领域的最大赢家。

原因很简单：例如跑 Dify 需要一个PG 和一个向量数据库，如果你用 pgvector，那么你只需要一个 PG 就够了 —— 无需 ETL 与额外组件额外维护！《[专用向量数据库凉了吗？](/db/svdb-is-dead/)》。

基于同样的理由，你并不需要一个专门的 MQ，缓存，全文检索，地理空间，图，文档数据库，所有这些能力都在 PostgreSQL 一个数据库中，通过内核本体或者扩展插件的方式提供。

![图片](06.webp)

而 MySQL 因为 Oracle 的不作为与躺平摆烂，还还将继续错过 OLAP 领域的 [DuckDB 缝合大赛](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488131&idx=1&sn=9dc6a377d0b24fb7b92cac840b229433&scene=21#wechat_redirect)，以及全文检索领域的 Tantivy 缝合大赛，未来与 PostgreSQL 的差距还会越拉越大。

按照现在的发展趋势，我认为大概会在几年内看到 PostgreSQL 正式成为数据库领域的 Linux 内核，而 MySQL 会变为 PHP 现在的状态 —— “PHP 是世界上最好的语言”，然而世界早已被 Javascript 吞噬。

------------------------------------------------------------------------

**\**

[**PostgreSQL正在吞噬数据库世界**](/pg/pg-eat-db-world/)

[**MySQL安魂九霄，PostgreSQL驶向云外**](/db/mysql-is-dead/)

[PostgreSQL is eating the database world](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487156&idx=1&sn=dea8abae114716013dbc4f5fb978064d&scene=21#wechat_redirect "PostgreSQL is eating the database world")

[谁整合好DuckDB，谁赢得OLAP数据库世界](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488131&idx=1&sn=9dc6a377d0b24fb7b92cac840b229433&scene=21#wechat_redirect "谁整合好DuckDB，谁赢得OLAP数据库世界")

[向量数据库凉了吗？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486505&idx=1&sn=a585c9ff22a81a8efe6b87ce9bd66cb1&scene=21#wechat_redirect "向量数据库凉了吗？")

[StackOverflow 2024调研：PostgreSQL已经超神了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486489&idx=1&sn=f2be1be496de46ac5ca816ac39cfdf24&scene=21#wechat_redirect "重新拿回计算机硬件的红利")

[PostgreSQL会修改开源许可证吗？](/pg/pg-license/)

[为什么PostgreSQL是未来数据的基石？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487577&idx=1&sn=e217c7addb57e6f8d45368b969cdf398&scene=21#wechat_redirect "为什么PostgreSQL是未来数据的基石？")

[技术极简主义：一切皆用Postgres](/pg/just-use-pg/)

[2023年度数据库：PostgreSQL (DB-Engine)](/pg/dbengines-2023/)

[PostgreSQL 到底有多强？](/pg/pg-performence/)

[为什么PostgreSQL是最成功的数据库？](/pg/pg-is-best/)

[StackOverflow 2022数据库年度调查](/db/so2022-db/)

[为什么说PostgreSQL前途无量？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247484591&idx=1&sn=a6ab13d93bfa26fca969ba163b01e1d5&scene=21#wechat_redirect "为什么说PostgreSQL前途无量？")

[\
](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247485549&idx=1&sn=7c34439d82431129c57aba211202b5ca&scene=21#wechat_redirect "分布式数据库是伪需求吗？")

[MySQL新版恶性Bug，表太多就崩给你看！](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488014&idx=1&sn=727b1e3e9077af728a243854ea1c2cb3&scene=21#wechat_redirect "MySQL新版恶性Bug，表太多就崩给你看！")

[用PG的开发者，年薪比MySQL多赚四成？](/pg/pg-dev-salary/)

[Oracle最终还是杀死了MySQL！](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487841&idx=1&sn=07ce183e7f5eafb34551438df963fe6d&scene=21#wechat_redirect "Oracle最终还是杀死了MySQL！")

[MySQL性能越来越差，Sakila将何去何从？](/db/sakila-where-are-you-going/)

[MySQL的正确性为何如此拉垮？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486710&idx=1&sn=261e4754df6c85954b50d8f68f277abe&scene=21#wechat_redirect "MySQL的正确性为何如此拉垮？")

[如何看待 MySQL vs PGSQL 直播闹剧](/pg/mysql-pg-live-drama/)

[驳《MySQL：这个星球最成功的数据库》](/pg/rebut-mysql-best/)

### \

[**\**
](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488000&idx=1&sn=7cbc71f4220ef50e967b88771a0fd00a&scene=21#wechat_redirect "MySQL安魂九霄，PostgreSQL驶向云外")
