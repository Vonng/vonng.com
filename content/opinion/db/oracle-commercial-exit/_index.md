---
title: 去 O 实战、商业库平替与协议拟态
linkTitle: 去 O 与商业库平替
description: PostgreSQL 对 Oracle 与 SQL Server 的全面替代、异构协议兼容内核与分布式回流。
weight: 30
icon: fa-solid fa-building-columns
---

PostgreSQL 不仅凭真串行化隔离与十余万分之一授权成本取代商业数据库，更以跨协议拟态内核零代码收编四大异构存量，终结盲目分布式的性能税并推动业务逻辑回流库内。

## 一、PostgreSQL 加冕与多协议拟态合围 {#coronation-and-protocols}

### 治理之外，驱动 PG 吞噬世界的底层引擎是什么？ {#stonebraker-extensibility-seed}

治理优良却无人问津的开源项目比比皆是——Oracle 失误只是推开需求大门，供给侧真正的发动机是图灵奖得主 Stonebraker 在 1986 年种下的“可扩展性”元能力。将自定义类型、操作符与 GiST/GIN 索引做成一等公民，让外部团队免改内核便长出逾千款插件：从 PostGIS、JSONB 到 `pgvector` 与 `VectorChord` 等扩展群，连续三轮吃尽时代红利，镜像下载量拉开 MySQL 四倍，单栈即可平替多套异构库。

- [是 Oracle 的失误让 PostgreSQL 赢了吗？ · 五、但 Stonebraker 也没说错——他种下的那颗种子](/db/thank-oracle/#五但-stonebraker-也没说错他种下的那颗种子)
- [MySQL 9.7：还是那碗冷饭 · 换个方向看看 PG](/db/mysql-97-bye/#换个方向看看-pg)
- [MySQL安魂九霄，PostgreSQL驶向云外 · 日渐落后的功能特性](/db/mysql-is-dead/#日渐落后的功能特性)

### PG 如何成为协议标准并零代码合围四大主流库？ {#pg-wire-protocol-compatibility}

Stonebraker 与 Andy Pavlo 已断言“Postgres 已经赢了”——AWS 分布式旗舰 Aurora DSQL 首发独尊 PG 线缆协议，确立了其“数据库界 Linux”地位。更致命的是双向协议合围：向上成为通用七层标准，向下则在统一发行版内集齐 `Babelfish`（1433 端口直通 MSSQL）、借微软 `DocumentDB` 提速 20 倍的 `FerretDB`（接管 MongoDB）、`OpenHalo`（兼容 MySQL 5.7）与 `IvorySQL`（兼容 Oracle），零改代码即可收编前五大库负载。

- [2025 年度数据库世界总结：石破天 vs Andy Pavlo 对谈录 · 3. Postgres 已经赢了，押注 Postgres 是正确选择](/db/db-year-review-2025/#3-postgres-已经赢了押注-postgres-是正确选择)
- [MySQL vs PostgreSQL @ 2025 · 兼容性](/db/mysql-vs-pgsql/#兼容性)
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法：数据库杂闻](/db/pavlo-2024-review/#andy-的看法数据库杂闻)
- [七周七数据库（2025年） · 老冯评论](/db/7-week-7-db/#老冯评论)
- [OpenHalo：MySQL线缆兼容的PostgreSQL来了！ · 还有其他内核花活](/pg/openhalo-mysql/#还有其他内核花活)
- [PostgreSQL可以替代微软SQL Server吗？ · Babelfish](/pg/pg-replace-mssql/#babelfish)
- [PostgreSQL 生态前沿进展 · FerretDB](/pg/pg-frontier/#ferretdb)
- [为什么PostgreSQL前途无量？ · 竞争关系](/pg/pg-is-great/#竞争关系)

### 开发者调查何时王座易主，选型呈现什么虹吸效应？ {#so2022-turning-point-siphon}

王座更替早在 Stack Overflow 2022 七万开发者调查中便已定局：近五万专业开发者里，PostgreSQL 以 46.5% 首次反超 MySQL（45.7%）夺魁，并以超 70% 喜爱率击败霸榜多年的 Redis，一举包揽流行、喜爱、渴望三冠王。选型流向和弦图更显露残酷的“单向虹吸”：高达 23% 的在用 MySQL 开发者计划次年迁往 PG，反向回流近乎归零，叠加 DB-Engines 传统三强齐跌而 PG 逆势大涨 9.2%，登顶大局已定。

- [StackOverflow 2022数据库年度调查 · 最流行的数据库](/db/so2022-db/#最流行的数据库)
- [StackOverflow 2022数据库年度调查 · 现在用什么以及想用什么？](/db/so2022-db/#现在用什么以及想用什么)
- [StackOverflow 2022数据库年度调查 · DBEngine](/db/so2022-db/#dbengine)

### 从云实例占比到中国市场，PG 逆转到了哪一步？ {#global-and-china-pg-adoption}

云原生、AI 与合规三重浪潮已彻底改写产业版图：三大公有云全面首推 PG，AWS RDS 上 PG 与 MySQL 实例比已达 6:4；Cursor、Dify、Notion 等 AI 独角兽清一色默认选 PG，类 BSD 协议更在合规上完胜 GPL。地缘维度上，受制裁的俄罗斯市场不受单一公司控制的 PG 采用率高达 60.5%（两倍于 MySQL）；即便在传统 MySQL 大本营中国，受去 O 与信创推动存量比也已从 1:5 追至 1:2，增量全面反超。

- [MySQL与白酒：互联网行业的服从测试 · 六、潮水的方向](/db/mysql-baijiu/#六潮水的方向)
- [MySQL vs PostgreSQL @ 2025 · 厂商](/db/mysql-vs-pgsql/#厂商)
- [MySQL安魂九霄，PostgreSQL驶向云外 · 枯萎收缩的生态规模](/db/mysql-is-dead/#枯萎收缩的生态规模)

## 二、去 O 实战：事务差异与兼容内核破局 {#oracle-exit-practice}

### 对比事务正确性，Oracle 可串行化为何输给了 PG？ {#oracle-fake-serializable}

号称顶级商业库的 Oracle 其实虚标了最高隔离级别。如 Cybertec 专家 Laurenz Albe 实测揭露，Oracle 标称的 `SERIALIZABLE` 底层仅是快照隔离（SI）：面对并发“先查计数再按约束插入”场景，它会放行写偏斜（Write Skew）异常致规则失守，甚至莫名抛虚假错误。主流关系库中，唯有 PostgreSQL 凭可串行化快照隔离（SSI）兑现了真串行等价正确性。

- [对比Oracle与PostgreSQL事务系统 · 老冯评论](/db/oracle-pg-xact/#老冯评论)

### 从 Oracle 迁往 PG，事务回滚与 MVCC 有哪些坑？ {#oracle-to-pg-migration-pitfalls}

去 O 迁移必须吃透两大底层差异。按 Laurenz Albe 总结：其一，Oracle 的 DDL 隐式提交而普通报错仅做语句级回滚，PG 支持事务内回滚 DDL 但任一报错即中止整个事务——切忌在长批处理中滥用 `SAVEPOINT` 模拟容错，否则必触发子事务雪崩。其二，Oracle 靠 UNDO 存旧版怕大删改，PG 表内多版本不怕大删改却极怕长事务阻塞 `autovacuum` 致表膨胀；自增更新唯一约束须声明 `DEFERRABLE`，非主键加锁应改用 `FOR NO KEY UPDATE`。

- [对比Oracle与PostgreSQL事务系统 · 语句级回滚](/db/oracle-pg-xact/#语句级回滚)
- [对比Oracle与PostgreSQL事务系统 · 事务的大小和持续时间限制](/db/oracle-pg-xact/#事务的大小和持续时间限制)

### 去 O 遇上闭源遗留包，为何绕不开 IvorySQL？ {#oracle-sysdate-and-ivorysql}

开源把每核十余万元商业授权费直接砸到每月二十元硬件成本，原生具备 85% Oracle 兼容度的 PG 天然是去 O 主力，但扩展机制唯独改不了 SQL 解析器。当 500 强企业的无源码闭源 JAR 包写死裸 `SYSDATE` 标识符时，唯有改解析器的兼容内核能破局。面对法务凶悍的 Oracle，Apache 2.0 开源的 IvorySQL 避开私有线缆协议雷区，走标准 PG 驱动连 `1521` 端口提供完整 PL/SQL 语法兼容，得以紧跟 PG 17/18 上游演进。

- [Oracle 兼容的 PG 真的有用吗？ · 为什么 SYSDATE 这么棘手？](/pg/ivorysql/#为什么-sysdate-这么棘手)
- [Oracle 兼容的 PG 真的有用吗？ · IvorySQL：开源的 Oracle 兼容内核](/pg/ivorysql/#ivorysql开源的-oracle-兼容内核)
- [兼容Oracle的开源 PostgreSQL？ · 快速上手](/pg/oracle-compatible-pg/#快速上手)
- [PostgreSQL：最成功的数据库 · 开源之德](/pg/pg-is-no1/#开源之德)

## 三、分布式祛魅、架构回流与开发者本位 {#architecture-reflow}

### 为什么盲目引入分布式 NewSQL 是过早优化？ {#newsql-premature-optimization}

拉通 TiDB、OceanBase、CockroachDB 与 YugabyteDB 官方百核级 `sysbench` 报告，同生产安全配置下的 96 核单机 PG（137 万点查、51.9 万混合读写）公平对比，分布式 NewSQL 单核归一化吞吐全线落后数倍乃至一个数量级。NewSQL 本质是牺牲复杂 SQL 完备性、稳定性与单核效率去换水平扩展上限；但单机 PG 轻松承载 15TB 数据与集群 40 万 TPS，99% 的企业终生摸不到天花板，盲目上分布式纯属白交性能税。

- [PostgreSQL 到底有多强？ · Fair Play](/pg/pg-performence/#fair-play)
- [为什么PostgreSQL前途无量？ · vs NewSQL](/pg/pg-is-great/#vs-newsql)

### 为什么算力过剩与大模型推动 Web 逻辑回流数据库？ {#omnigres-backend-in-db}

早年拆前后端三层架构源于数据库算力紧缺且存储过程受限；如今单机算力富余且 PG 支持二十多种过程语言，架构迎来“分久必合”。Omnigres 创始人 Yurii 借 33 个扩展在库内构建含 HTTPD 与 Python 的 Web 全栈。我深耕十年存储过程的体会是，这套极简范式普及的唯一命门曾是研发门槛太高，而大模型生成高质量存储过程恰好扫清了障碍。

- [PostgreSQL 生态前沿进展 · Omnigres](/pg/pg-frontier/#omnigres)
- [第七届PG生态大会：一些感想 · 如何请外国人参会](/pg/pgconf-china-7th/#如何请外国人参会)

### 数据库产品为何必须从盯着 DBA 转向赋能开发者？ {#shift-from-dba-to-developer}

在真刀真枪交锋的第七届 PG 生态大会上，马工与萧少聪点破核心：数据库的真正用户是开发者而非 DBA。高可用与安全只守存量底线，决定增量的一线开发者买单的是“用最省力方式干最多的活”——如一行 PostGIS 查询顶掉上千行 C++/Java 代码。Neon 与 Supabase 正赢在开发者体验，现代 PG 发行版必须用丰富扩展与自托管 BaaS 直接赋能开发者。

- [第七届PG生态大会：一些感想 · 数据库应该更加关注开发者](/pg/pgconf-china-7th/#数据库应该更加关注开发者)
- [第七届PG生态大会：一些感想 · 如何办好一场会？](/pg/pgconf-china-7th/#如何办好一场会)
