---
title: "Catalog Bullshit：把数据库拆开，再租给你一张 PostgreSQL 表"
date: 2026-08-28
authors: [vonng]
summary: >
  Snowflake 将湖仓治理裂缝归因于多引擎，并把 Catalog 推上新的收费层。但 Iceberg Catalog 的核心只是一笔元数据指针 CAS；真正的治理缺口，来自控制面与数据路径的分离。
tags: [PostgreSQL, OLAP, 对象存储, 技术评论]
---

## 从 Snowflake 的治理清单说起

前几天，Snowflake 在[一条官方推文](https://x.com/Snowflake/status/2093073608851542204)里发了张黑底蓝字的海报，标题叫 **THE ARCHITECT’S GOVERNANCE CHECKLIST**，架构师治理清单。海报列了九个问题：

- 撤权缺口
- 策略漂移
- 静默损坏
- 分类盲区
- “谁”的问题
- 端到端血缘
- 身份标准化
- 被遗忘权
- 逻辑一致性

配文只有三句话：

> 多引擎湖仓不只是在数据层失败。\
> 它们在治理和安全无法跨所有引擎一致落地时失败。\
> 数据互操作性 ≠ 治理互操作性。

第三句是真的，也是这篇文章的起点：数据格式开放，不等于治理机制可以跨引擎互操作。Snowflake 在配套的[治理互操作性长文](https://www.snowflake.com/en/blog/engineering/lakehouse-data-governance-interoperability/)里列出的很多问题也确实存在。

问题在于，它顺手把这个技术判断推导成了一个商业结论：多引擎必然产生治理裂缝，所以不要多引擎，最好全部收进同一个引擎。翻译成中文，就是“标准还不完备，所以不要用标准”。

这一步值得拆开看。与其停在厂商口水战上，不如继续往 Catalog 下面挖：它到底解决了什么问题，又为什么会在技术必要性逐渐下降的时候，反而变成新的控制点。

## Catalog 的本职：替对象存储保管一个指针

先看 Iceberg 如何提交一次写入。按照 [Iceberg 规范对乐观并发的定义](https://iceberg.apache.org/spec/#optimistic-concurrency)，一次更新大致经历四步：

1. 写新的 Parquet 数据文件；
2. 写新的 manifest；
3. 写新的 `metadata.json`；
4. 让 Catalog 把表的当前指针，从旧 `metadata.json` 换成新的。

Catalog 只有在当前指针仍然等于引擎预期的旧值时才会更新。换指针的那一刻，就是事务提交：此前的读者看到旧快照，此后的读者看到新快照，中间没有第三种状态。

把它翻译成 SQL，无非是一次单行 compare-and-swap：

```sql
UPDATE tables SET ptr = $new WHERE name = $t AND ptr = $old;
```

这次原子换指针，是 Catalog 唯一不可替代的职责，其他能力都建立在它之上。问题也由此变得具体：为了完成一次单行 CAS，是否真的需要一个独立部署、独立授权、独立打补丁、独立计费的分布式服务？

再看这些 Catalog 自己如何持久化元数据：

- [Hive Metastore](https://hive.apache.org/docs/latest/admin/adminmanual-metastore-3-0-administration/) 通常把状态放在 MySQL 等关系数据库里，再暴露 Thrift 接口；
- [Project Nessie](https://projectnessie.org/) 可以使用 JDBC/PostgreSQL 等后端；
- [Apache Polaris](https://polaris.apache.org/) 提供 JDBC 持久化路径；
- [Lakekeeper](https://docs.lakekeeper.io/) 用 Rust 编写、采用 Apache 2.0 许可证，而它的[配置文档](https://docs.lakekeeper.io/docs/nightly/configuration/#persistence-store)明确写着：当前持久化后端只支持 PostgreSQL 15 及以上版本。

所以，“整个 Catalog 行业就是一张套了 REST 壳的 PostgreSQL 表”虽然是一句刻薄的概括，却并没有偏离事实太远。更有意思的是，Snowflake 已经开始按 REST 请求为这层包装收费；从用户视角看，付的确实很像这张表的 `UPDATE` 租金。

## 技术必要性退场，收费站开始上场

独立 Catalog 当年有充分的技术理由。早期 S3 没有原子 rename，也缺少安全的 compare-and-swap；对象存储无法表达“只有旧值仍然等于 X 才写入新值”，于是提交点只能交给一个真正支持线性化 CAS 的外部协调者。

Hive Metastore、Glue、Nessie、Polaris、Unity、Horizon、Gravitino 先后出现。名字换了很多，核心工作没有变：替对象存储保管当前指针。Delta 走了另一条路，直接按序号原子创建日志文件；但早期 S3 不支持 `create-if-not-exists`，因此还要借助 DynamoDB 补上这个原语。

转折发生在 2024 年。[S3 开始支持条件写](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html)，对象存储终于能够直接表达 `create-if-absent` 和基于 ETag 的条件更新。提交原语回到存储层以后，一部分工作负载已经不再需要独立协调者。

这就形成了一条很值得观察的时间线：**独立 Catalog 的技术必要性正在下降，它却恰好在同一时期被做成新的控制点和计费层。**

Snowflake 2024 年发起 Polaris 并将其捐给 Apache；到了 2026 年 4 月，它又以《[Apache Polaris 与数据厂商锁定的终结](https://www.snowflake.com/en/engineering-blog/apache-polaris-iceberg-rest-catalog/)》为题回顾这项工作，强调自己的 Iceberg REST Catalog 没有私有扩展、没有能力阉割、没有小字条款。

与此同时，[Snowflake Open Catalog 已经停止接受首次注册](https://docs.snowflake.com/en/user-guide/opencatalog/overview)，新客户被引导到 Horizon Catalog；而 [Horizon Iceberg REST Catalog API](https://docs.snowflake.com/en/user-guide/tables-iceberg-access-using-external-query-engine-snowflake-horizon) 计划从 2026 年下半年开始按每百万次调用 0.5 credit 计费。

把这几件事放在一起，逻辑就很清楚了：格式开放之后，Catalog 成为新的入口；Catalog 也开放之后，治理又成为更高一层的入口。**Governance is the wedge——治理就是那枚楔子。**开头那张海报，正是这套商业路径最简洁的说明书。

## 控制面根本不在数据路径上

上面说的是 Catalog 为什么会成为生意，下面才是治理为什么难。

数据库里的权限之所以能够成为强制边界，是因为引擎是访问字节的唯一入口。读一行数据必须经过同一扇门，ACL 就挂在门上；所有门都开在同一堵墙里。

湖仓把这堵墙拆开了。数据字节躺在 S3 里，谁拿到桶凭证，谁就能直接读取对象。Catalog 能做的是 credential vending：先识别调用者，再发出一个有时效、权限范围限定到某个前缀的 STS token。可一旦凭证发出，Catalog 就退出了后续的数据路径，也无法再观察引擎究竟读了哪些行、哪些列。

### 行列策略依赖引擎自觉

对象存储 token 的粒度是对象和前缀，Parquet 的行和列却在文件内部。只要 token 允许读取某个文件，持有者就能拿到其中的全部行列。因此，Catalog 层无法直接强制行级安全和列掩码，只能要求各个引擎在扫描时正确执行策略。

这套机制可以工作，但必须把边界说清楚：它不是由存储层强制执行的安全边界，而是一份依赖引擎遵守的协议。

### 撤权只能等 token 过期

同样的限制也解释了所谓“撤权缺口”。如果 Catalog 发出一个有效期一小时的 token，随后管理员在控制面执行 `REVOKE`，已经签发的 token 仍然可以继续使用，直到自然过期。

因此，撤权在这种架构里天然是异步的、最终一致的。把四个引擎缩减为一个并不会消除这个窗口；只要数据面仍然是 S3，只要外部表仍通过短期凭证直读对象，缺口就仍然存在。

### 多引擎替真正的问题背了锅

撤权缺口、策略漂移、“谁”的问题和逻辑一致性，首先是“控制面不在数据路径上”的结果，而不是引擎数量本身的结果。Snowflake 的论证在这里偷换了因果：它把分离式架构的结构性约束，包装成多引擎独有的缺陷，再把单一引擎作为解药。

[Lakekeeper 的产品说明](https://docs.lakekeeper.io/)在这一点上反而更坦率：只描述数据的 Catalog 什么也拦不住，所以它把身份解析、策略评估、短期凭证签发和审计记录都放在元数据请求路径上。这能改善控制面，却仍然改变不了一个事实：它坐在元数据请求路径上，而不是数据路径上。

### “被遗忘权”是一条后台处理链

“被遗忘权”也需要放回实际的数据生命周期里理解。按照 [Iceberg 的行级删除规范](https://iceberg.apache.org/spec/#row-level-deletes)，v2 使用 position delete 或 equality delete，v3 则引入 deletion vector。这些机制首先让查询不再返回目标行，却不会立刻从原始 Parquet 文件中抹掉对应字节。

真正的物理删除还要等待数据重写、快照过期和孤儿文件清理全部完成。换句话说，湖仓里的 GDPR 删除不是一个 `DELETE` 语句，而是一条异步后台处理链。

Snowflake 自己的 micro-partition 同样不可变；在 [Time Travel 和 Fail-safe](https://docs.snowflake.com/en/user-guide/data-time-travel) 的保留窗口内，已删除数据仍然可能存在。把不可变存储的共同约束列进治理清单没有错，问题在于不能据此暗示“换成我就没有这个问题”。

**数据库把所有门开在同一堵墙上。湖仓把墙拆了，然后卖给你一份检查门的清单。**

## 二十年，重新发明数据库

把时间拉长看，过去二十年很像一部不断“重新发明数据库”的连续剧：

- 2004 年，Google 发表 [MapReduce 论文](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)；
- 2008 年初，DeWitt 和 Stonebraker 写下《[MapReduce：一次重大的技术倒退](https://dsf.berkeley.edu/cs286/papers/backwards-vertica2008.pdf)》，批评它没有 schema、没有索引、没有事务，当年被骂成守旧老古董；
- 2010 年前后，Hive 把 SQL 加回来；
- 同期，Hive Metastore 把 system catalog 加回来，底下仍然是一套关系数据库；
- 2017 年起，Delta、Iceberg、Hudi 把 ACID 加回来；
- 后来，[Puffin file](https://iceberg.apache.org/puffin-spec/) 把统计信息文件加回来；
- 2024 年起，Polaris、Unity、Gravitino、Horizon 把 Catalog 服务化；
- 2026 年，又开始往回补 `GRANT`、`REVOKE`、行级安全、列掩码、审计和血缘，也就是海报上的九个问题。

二十年、几百亿美元，行业在对象存储上重新实现了一遍 System R。数据库把这些能力做成一个原子、一致、经过四十年验证的整体，装进同一个进程；`initdb` 之后，事务、权限、目录和统计信息都在里面。

湖仓则把这个整体拆成十几个组件，每个组件背后站着一家公司，需要分别采购、授权、打补丁和运维。Pavlo 与 Stonebraker 2024 年的论文《[What Goes Around Comes Around... And Around](https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf)》讨论的正是这种循环：NoSQL 折腾十年后回到关系模型和 SQL，湖仓只是换了一个舞台重演。

连剧本都很相似。以前说“我们不需要 schema”，现在说“我们不需要数据库”。

## Catalog 本来就该是一张表

如果承认 Catalog 本来就应该是一张数据库表，设计方向就会变得直接：把 Catalog 和元数据一起放回 SQL 数据库，而不是继续把元数据拆成文件撒在对象存储里。

[DuckLake v1.0](https://duckdb.org/2026/04/13/ducklake-10) 采用的就是这条路线。数据仍然是 Parquet，仍然放在用户自己的桶里，仍然使用开放格式；变化的只是元数据的家。v1.0 于 2026 年 4 月发布，宣布达到生产可用状态并承诺向后兼容，元数据模型由 28 张表组成，采用 MIT 许可证。

这个决定带来了两项 Iceberg 很难提供的能力。

### 小文件不必立刻落成 Parquet

DuckLake 支持 [data inlining](https://ducklake.select/docs/stable/duckdb/advanced_features/data_inlining)：低于阈值的插入和删除不立即写 Parquet，而是先进入 Catalog 数据库的内联表，积累到合适规模后再刷成正常大小的文件。v1.0 默认阈值是 10 行。

[MotherDuck 的架构分析](https://motherduck.com/blog/ducklake-architecture-deep-dive/)给出的对比是：传统湖仓每次小事务会产生 JSON、Avro、Parquet 等三四个文件，文件越堆越多，读取和 compaction 的成本也随之上升，实际提交吞吐往往被压在每秒一次左右；使用 inlining 后，DuckLake 可以维持约每秒 100 次事务。

这些数字来自厂商，自然应该打折看；但方向是确定的。元数据位于真正的数据库里，系统才有条件把小变更内联进去。元数据如果本身就是一堆文件，就只能让 compaction 永远追在写入后面。

### 跨表事务变成现成能力

Iceberg 这类表格式通常只能保证单表原子提交；DuckLake 则可以直接使用底层数据库事务，让多张相关表一起 `BEGIN`、一起 `COMMIT`。文件式元数据缺少共同提交点，这件事很难自然实现；放进数据库后，反而成了白送的能力。

Snowflake 开源的 [`pg_lake`](https://pgext.cloud/ext/pg_lake) 也走在同一条路上。它引入新的 Iceberg 表类型，让 PostgreSQL 自己充当 Catalog。Snowflake 的[官方介绍](https://www.snowflake.com/en/blog/engineering/pg-lake-postgres-lakehouse-integration/)对此写得很直白：Postgres 直接管理 Iceberg 表，而不是再把 Catalog 放到另一个系统里。

这不是什么小众异端。只要继续沿着事务一致性和元数据可管理性往下做，很多实现最终都会走到这里。

### 99% 的场景，四级就够

从这个视角出发，路线图其实很短：

1. 直接用 PostgreSQL；
2. 用 DuckDB 做单机分析；
3. DuckDB 加对象存储；
4. DuckDB 加对象存储，再加 PostgreSQL 元数据。

这四级足以覆盖 99% 的场景。剩下 1% 确实需要弹性分布式扫描：100 TB 以上，200 个临时 worker 跑五分钟，然后归零计费，那是 Spark 和 Trino 的地盘。

问题从来不是那 1% 存在，而是为那 1% 设计的架构，被卖给了 100% 的人。

## DuckDB 穿着 PostgreSQL 的马甲

这里还需要正视 PostgreSQL 的真实短板。它的执行器采用逐行的火山模型，没有向量化执行，也没有原生列存；在分析扫描上，比 DuckDB、ClickHouse 慢一到两个数量级并不奇怪。这个短板靠普通扩展补不了，因为扩展无法把整个执行器换掉。

但今天这些“让 PostgreSQL 做分析”的扩展，解决办法都很相似：

- [`pg_lake`](https://pgext.cloud/ext/pg_lake) 让 PostgreSQL 负责规划和事务，另起 `pgduck_server` 进程运行 DuckDB，通过 PostgreSQL wire protocol 通信；
- [`pg_duckdb`](https://pgext.cloud/ext/pg_duckdb) 直接把 DuckDB 的向量化执行器嵌进 PostgreSQL；
- [`pg_mooncake`](https://pgext.cloud/ext/pg_mooncake) 也是同一路线。

所以，“PostgreSQL 吃下数仓”需要换一个主语：

**真正吃下数仓的，是穿着 PostgreSQL 马甲的 DuckDB。**

这不是贬义，而是架构真实的形状：缺失的执行引擎早已存在，现在的问题只是谁来充当外壳。向量化执行这条路，CWI 在 2005 年的 [MonetDB/X100 论文](https://ir.cwi.nl/pub/16497)里就已经论证清楚；DuckDB 也出自同一个实验室。PostgreSQL 二十年没有吸收它，并非不知道，而是执行器实在太难改，社区也不会为了 OLAP 重写整个内核。

与此同时，硬件还在继续进步。一台机器配两条 100 GbE 和一组 NVMe，扫描带宽已经可以达到几十 GB/s。绝大多数公司所谓的“大数据”，一台机器放得下，也往往比八节点集群跑得更快。硬件年年增长，而多数公司的有效数据量并没有同步增长，这个判断只会越来越稳。

## 开放一层，收费站上移一层

把相关公司的动作放在一起看，格局会更清楚：

- [`pg_lake`](https://pgext.cloud/ext/pg_lake) 与 [`pg_parquet`](https://pgext.cloud/ext/pg_parquet) 都来自 Crunchy Data；Snowflake 在 2025 年 6 月完成收购，向 SEC 披露的[现金对价为 1.645 亿美元](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000187/snow-20250731.htm)，并于同年 11 月开源 `pg_lake`；
- [`pg_mooncake`](https://pgext.cloud/ext/pg_mooncake) 背后的 Mooncake Labs 于 2025 年 10 月[被 Databricks 收购](https://www.linkedin.com/posts/databricks_were-excited-to-announce-that-databricks-activity-7379138538652696576-2pbr)；此前 Databricks 已在 5 月[收购 Neon](https://neon.com/blog/neon-and-databricks)，[交易估值约 10 亿美元](https://techcrunch.com/2025/05/14/databricks-to-buy-open-source-database-startup-neon-for-1b/)，两支团队如今都在为 Lakebase 服务；
- [`pg_duckdb`](https://pgext.cloud/ext/pg_duckdb) 是 DuckDB Labs、Hydra 与 MotherDuck 的合作项目；
- DuckDB 和 DuckLake 背后的 DuckLabs 已与 AWS [签署收购协议](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/)；
- [Azure HorizonDB](https://azure.microsoft.com/en-us/blog/from-legacy-to-leadership-how-postgresql-on-azure-powers-enterprise-agility-and-innovation/) 是微软自研的 PostgreSQL 兼容引擎，宣称最高可扩展到 3072 vCore 和 128 TB。

这四级台阶的每一级下面，站着的都是这套架构原本想绕开的公司。它们并没有简单买下项目再将其扼杀；更高明的做法，是买下道路本身。

`pg_lake` 采用 Apache 2.0 许可证，是真开源，代码质量也很高。Snowflake 花 1.645 亿美元买下团队，再把核心能力免费开放，并不矛盾：它不怕 PostgreSQL 吃下数仓，怕的是 PostgreSQL 吃下数仓时完全不经过 Snowflake。

因此，`pg_lake` 让 PostgreSQL 直接管理 Iceberg 表、自己充当 Catalog，确实提供了用户想要的能力；与此同时，它也把 Iceberg 固化成默认落地格式。工具越好用，Iceberg 生态就越稳，而治理入口仍然可以留在更高一层。

这几年最值得研究的商业策略，正是这种收费站上移：

**开放挡不住，就资助开放；然后确保开放的那一层，不是自己收钱的那一层。**

格式开放了，就卖 Catalog；Catalog 开放了，就卖治理；治理继续开放，就再往上找一层。每开放一层，收费站就上移一层。每上移一次，厂商都会告诉你：更高那层太危险，你自己搞不定。

## 拿清单去检查发清单的人

回到最初那九个问题。那张海报值得保存，因为每一条都指向真实风险；但检查清单不该只用来检查竞争对手，也应该用来检查发清单的人：

- **撤权缺口**——外部表是不是通过 credential vending 访问？token 发出去以后，`REVOKE` 何时才真正生效？
- **被遗忘权**——在 Time Travel 和 Fail-safe 的保留期内，客户要求删除的那行数据是否仍然存在？
- **身份标准化**——2024 年针对 Snowflake 客户实例的攻击中，Mandiant 与 Snowflake 通知了[约 165 家可能受影响的组织](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion)；同年，AT&T 又披露攻击者从第三方云平台复制了[近乎全部无线客户的通话与短信交互记录](https://www.sec.gov/Archives/edgar/data/732717/000073271724000046/t-20240506.htm)。在这些事件发生时，组织级强制 MFA 在哪里？

这九条不是多引擎独有的病，而是把数据库拆开以后必然面对的治理成本。解法也不是简单地把引擎从四个减到一个，而是把被拆出去单独出售的能力，一件件搬回它们应该在的位置：

**元数据回到数据库。权限回到唯一入口。剩下的字节留在便宜的对象存储里，用谁都能读的开放格式保存。**

这不是新想法。这就是数据库。

我们花了二十年、几百亿美元绕了一大圈，正在把拆散的能力一件件捡回来。

捡的时候，还得跟人租一张 PostgreSQL 表。
