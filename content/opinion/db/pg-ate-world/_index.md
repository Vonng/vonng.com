---
title: 选型金字塔与 PostgreSQL 吞噬世界
linkTitle: PG 吞噬数据库世界
description: 数据库需求金字塔、PostgreSQL 三十年三级跳、开发者统治力与“一切皆用 Postgres”。
weight: 10
icon: fa-solid fa-crown
---

数据库选型的终点不是拼凑异构组件，而是回归正确性底线与综合 ROI。凭借四十年前种下的可扩展基因与现代多核硬件红利，PostgreSQL 已跨越三代技术浪潮，成为吞噬专用库并统合 AI 时代的事实标准。

## 一、选型第一性原理与需求金字塔 {#principles-and-pyramid}

### 为什么学透数据库原理比死磕算法更能决定上限？ {#why-learn-db-principles}

绝大多数系统都是数据密集型应用，业务代码只是搬运数据的胶水——数据表即数据结构，索引与查询即算法，在数据库面前后端也是前端。范式、关系代数、ACID 与 WAL 绝非空洞教条，而是用 GiST 树把秒级近邻搜索压进 1 毫秒、防并发错账与脑裂丢数的实战武器。先用 PostgreSQL 做出系统踩过慢查询的坑，再结合《DDIA》反刍内核，方能进阶架构师。

- [为什么要学习数据库原理](/db/why-learn-database/)

### 生产数据库的准入底线与高阶比拼维度是什么？ {#db-demand-pyramid}

类比马斯洛模型，ACID 正确性与冷备加 WAL 时间点恢复是不可妥协的生死底线，失守只会令企业破产。多副本高可用与监控仅算及格本分，真正拉开段位的是性能、账单与管理复杂度的综合 ROI，公有云 RDS 正因高溢价在此失分。再往上唯有让全栈可观测性、声明式 IaC 与大模型决策闭环联动，方能迈向自治。

- [数据库需求层次金字塔 · 安全需求](/db/demand-pyramid/#安全需求)
- [数据库需求层次金字塔 · 尊重需求](/db/demand-pyramid/#尊重需求)
- [数据库需求层次金字塔 · 审美需求](/db/demand-pyramid/#审美需求)

### 为什么有硬伤的默认选型能横行，如何打破惯性？ {#mysql-baijiu-obedience-test}

互联网行业的 MySQL 如同酒桌白酒，是借早期惯性与大厂权威塑造成的“服从测试”——随大流踩坑免责，选 PostgreSQL 反要独担风险。嘴上嫌 PG 曲线陡，身体却花三年背诵子查询改 JOIN、中间表替 CTE、外挂工具补锁表 DDL 的擦屁股套路，本质是为逃避认知失调死守舒适区。好数据库应让人舒适，而非逼人给烂设计打补丁。

- [MySQL与白酒：互联网行业的服从测试 · 三、服从测试](/db/mysql-baijiu/#三服从测试)
- [MySQL与白酒：互联网行业的服从测试 · 五、吐真剂](/db/mysql-baijiu/#五吐真剂)
- [MySQL与白酒：互联网行业的服从测试 · 七、选择的勇气](/db/mysql-baijiu/#七选择的勇气)

### 该走专业化还是一体化，主从架构上限有多高？ {#monolith-pg-vs-sharding}

几十 TB 规模内应坚定选择一体化架构：PostgreSQL 就像智能手机，配合 `pgvector` 足以单栈吃下十几 TB 向量与关系负载，免除跨异构系统的一致性与运维税。正如 OpenAI 工程师 Bohan Zhang 披露，ChatGPT 仅凭未分片的“一主四十多从”PG 便扛下五亿月活与百万级 QPS。按 Matt Blewitt 剖析，FoundationDB、TigerBeetle 与 CockroachDB 等专用库，唯有靠严苛自我设限才能在百 TB 强一致或跨洲容灾等窄域立足。

- [AI时代的数据库与DBA将何去何从 · 一体化还是专业化，如何选型？](/db/ai-dba-job/#一体化还是专业化如何选型)
- [OpenAI：将PostgreSQL伸缩至新阶段 · 结果](/db/openai-pg/#结果)
- [七周七数据库（2025年） · 分层数据库](/db/7-week-7-db/#分层数据库)

## 二、为什么 PostgreSQL 吞噬了世界 {#why-pg-ate-the-world}

### PG 凭什么从学院原型长成数据库界的 Linux？ {#from-berkeley-to-linux}

PostgreSQL 源于图灵奖得主 Stonebraker 1986 年的伯克利原型，经华人研究生 Jolly Chen 与 Andrew Yu 换上标准 SQL 放上互联网，并在 1996 年 7 月 8 日架设公开 CVS 成为独立于单一机构的全球社区资产。此后已故先驱 Simon Riggs 补齐时间点恢复、热备可读从库、流复制与分区表等企业基石，可扩展架构更让新范式原生生长；到 PG 17 官方直接删去“关系型”定语，正面叫板顶级商业库。

- [PostgreSQL 三十岁生日快乐 · 为什么是 7 月 8 日？](/pg/happy-30-birthday/#为什么是-7-月-8-日)
- [参加 PostgreSQL 30周年开发者大会 · 本文 AI 含量 0%](/pg/pgconfdev-2026/#本文-ai-含量-0)
- [PostgreSQL 三十岁生日快乐 · 三十而立](/pg/happy-30-birthday/#三十而立)
- [PostgreSQL 主要贡献者 Simon Riggs 因坠机去世](/pg/simon-riggs/)
- [PostgreSQL 17 发布：摊牌了，我不装了！ · 关于 PostgreSQL](/pg/pg-17/#关于-postgresql)

### 全球开发者调研如何印证 PG 的断层统治力？ {#survey-and-ranking-dominance}

数万样本的 Stack Overflow 调研连续三年见证断层统治：PostgreSQL 使用率从 2023 年首超 MySQL（45.6% 对 41.1%）、2024 年专业开发者过半（51.9%），一路飙至 2025 年的 58.2%，甩开次席达 18.6 个百分点并包揽流行、喜爱、需求三冠王。以“喜爱减厌恶”计算的 44% 净喜爱指数（NLS）稳定兑现每年 460 个基点的份额增长，两年翻倍至 47% 的选型需求度更提前锁定未来增量。

- [PostgreSQL：最成功的数据库 · 过去的积累：流行度](/pg/pg-is-no1/#过去的积累流行度)
- [StackOverflow 2024调研：PostgreSQL已经杀疯了 · 流行度](/pg/pg-is-no1-again/#流行度)
- [StackOverflow 2024调研：PostgreSQL已经杀疯了 · 喜爱度与需求度](/pg/pg-is-no1-again/#喜爱度与需求度)
- [PostgreSQL 已主宰数据库世界 · 流行度](/pg/so2025-pg/#流行度)
- [为什么PostgreSQL是最成功的数据库？ · 最喜爱](/pg/pg-is-best/#最喜爱)

### 为何说可扩展性才是 PG 跨越三波浪潮的撒手锏？ {#extensibility-three-waves}

单点特性三年就会被抹平，让 PostgreSQL 在 420 余款竞品中八年五夺 DB-Engines 年度总冠军的撒手锏，是通用框架级的可扩展性。它借此完成三级跳：传统时代靠 PostGIS 垄断测绘，移动浪潮内置 JSONB 消解文档库，AI 时代凭 `pgvector` 稳坐头把交椅。如核心组成员 Jonathan Katz 所言，精简内核加预编译扩展发行版彻底释放了生产力。

- [PostgreSQL，三十而立 · 四、三十年，三级跳](/pg/pg-turns-30/#四三十年三级跳)
- [PostgreSQL 2024 社区现状调查报告 · 选择 PG 的原因](/pg/pg-survey-2024/#选择-pg-的原因)
- [PostgreSQL荣获2024年度数据库之王！（第五次） · PostgreSQL 为什么这么牛逼？](/pg/pg-dbeng-2024/#postgresql-为什么这么牛逼)
- [2023年度数据库：PostgreSQL (DB-Engine) · 年度数据库：PostgreSQL](/pg/dbengines-2023/#年度数据库postgresql)
- [展望 PostgreSQL 的2024 · 扩展](/pg/pg-in-2024/#扩展)

### 为什么“一切皆用 Postgres”能根治组件泛滥？ {#just-use-postgres}

死于架构过度复杂的团队远多于死于工具太简单的团队。如 Ajay Kulkarni 与 Stephan Schmidt 所批判，把关系、缓存、队列和搜索拆进五六个异构库，只会让研发困死在跨库胶水代码里。百万用户规模内，用 `UNLOGGED TABLE` 替缓存、`SKIP LOCKED` 替队列、`JSONB` 替文档库，配合事务性 DDL 与 FDW 足以一库通吃——早年我在探探零 Redis 缓存、仅靠百余台 PG 硬扛数百 TB 数据与 250 万全局 TPS 就是铁证。

- [为什么PostgreSQL是未来数据库的事实标准？ · 第四部分：数据库越多，问题越多](/pg/pg-for-everything/#第四部分数据库越多问题越多)
- [技术极简主义：一切皆用Postgres · 然而，我们有极致简化的方案](/pg/just-use-pg/#然而我们有极致简化的方案)
- [技术极简主义：一切皆用Postgres · 译者评论](/pg/just-use-pg/#译者评论)
- [PostgreSQL好处都有啥 · 全栈数据库](/pg/pg-is-good/#全栈数据库)
- [PostgreSQL好处都有啥 · 运维友好](/pg/pg-is-good/#运维友好)

### 硬件跃迁与 DuckDB 合流如何颠覆数仓与新内核创业？ {#hardware-duckdb-convergence}

单台双路服务器如今坐拥 512 核、数 TB 内存与数十 TB NVMe 闪存，配合 S3 足以装下 99% 企业的全量数据，昔日因单机算力不足拆出的数仓正回归单栈超融合。随着 CWI 出品、MIT 开源的 DuckDB 原厂下场推出 `pg_duckdb`，实时分析扩展迅速收敛，重演了 `pgvector` 荡平独立向量库的剧本。这彻底改写了创业铁律：通用新内核再无生路，垂直专用库若无数量级优势终将被 PG 扩展吞并。

- [PostgreSQL 正在吞噬数据库世界 · 分久必合的数据库领域](/pg/pg-eat-db-world/#分久必合的数据库领域)
- [PostgreSQL 正在吞噬数据库世界 · 改变游戏规则的玩家](/pg/pg-eat-db-world/#改变游戏规则的玩家)
- [谁整合好DuckDB，谁赢得OLAP世界 · DuckDB：OLAP的新兴挑战者](/pg/pg-duckdb/#duckdbolap的新兴挑战者)
- [谁整合好DuckDB，谁赢得OLAP世界 · 第二届PG扩展竞速比赛](/pg/pg-duckdb/#第二届pg扩展竞速比赛)
- [PostgreSQL 2024 社区现状调查报告 · 工作](/pg/pg-survey-2024/#工作)

### 列存扩展与冷热分层如何打破 PG 的百 TB 瓶颈？ {#in-db-olap-and-tiered-storage}

认为 PostgreSQL 搞不定复杂分析与海量存储早已是老黄历。百 GB 量级内，10 核 M1 Max 笔记本原生跑完 10GB TPC-H 全部 22 条复杂查询仅需 56 秒，配合流复制本就是丝滑 HTAP 底座。在前沿扩展侧，`pg_mooncake` 嵌入 DuckDB 向量化引擎并由 PG 直接管理 Parquet 统计信息，首次杀入 ClickBench 前十媲美 ClickHouse；叠加 Ajay Kulkarni 展示的本地盘加 S3 透明冷热分层，单栈即可承载百 TB 至 PB 负载。

- [PostgreSQL 生态前沿进展 · pg_mooncake](/pg/pg-frontier/#pg_mooncake)
- [为什么PostgreSQL是未来数据库的事实标准？ · 大数据则何如？](/pg/pg-for-everything/#大数据则何如)
- [PostgreSQL 到底有多强？ · TPC-H分析性能](/pg/pg-performence/#tpc-h分析性能)

## 三、数据库即架构与超融合扩展实战 {#db-as-architecture}

### 为什么软件架构正向数据库坍缩，库内写逻辑可行吗？ {#db-is-the-arch}

如 Stonebraker 所言“看数据模型便知业务全貌”，现代应用本质只是数据库界面。昔日拆三层源于算力紧缺与手写存储过程门槛高；如今算力富余且大模型精通存储过程，像 Omnigres 用 33 个扩展在库内直跑 HTTP，既省网络往返又将部署化为纯 SQL。随着 PG 吞掉专用库、Supabase 拿下八成 YC 新创，架构正回归 `Agent + Database`。

- [数据库即业务架构 · 数据库是架构的核心](/db/db-is-the-arch/#数据库是架构的核心)
- [数据库即业务架构 · 这会是一个好主意吗？](/db/db-is-the-arch/#这会是一个好主意吗)
- [数据库即业务架构 · 吞噬一切的数据库](/db/db-is-the-arch/#吞噬一切的数据库)

### 在 Agent 时代，多元持久化为何成了诱发幻觉的毒药？ {#ai-agent-zero-glue}

当写 SQL 的主体换作注意力稀缺的 AI Agent，“多元持久化”便沦为认知毒药：数据拆进四五个异构库，逼着 Agent 塞满多套语法再写跨库搬运与应用层 Join 胶水代码，白烧 Token 并放大幻觉。PostgreSQL 借扩展与 FDW 将关系、全文及向量检索坍缩进单条 ACID SQL，且主流模型深谙 PG 方言，一行 `psql` 即是零胶水底座。

- [为什么PG将主宰AI时代的数据库 · 多元持久化：碎片化的认知噩梦](/pg/ai-db-king/#多元持久化碎片化的认知噩梦)
- [为什么PG将主宰AI时代的数据库 · PostgreSQL：零胶水架构](/pg/ai-db-king/#postgresql零胶水架构)
- [为什么PG将主宰AI时代的数据库 · 接口标准化：psql 即 IDE](/pg/ai-db-king/#接口标准化psql-即-ide)
- [PostgreSQL 三十岁生日快乐 · 下一个三十年](/pg/happy-30-birthday/#下一个三十年)

### 为什么自然语言写 SQL 频失灵，Agent 最缺什么？ {#text-to-sql-and-agent-acid}

刷榜高分的 Text-to-SQL 一进真实企业数仓就露怯：Stonebraker 在 MIT 等七座企业数仓实测主流模型，初始准确率 0%，加 RAG 与拆解也仅 20%～30%，内部黑话与重叠视图令裸调模型失灵。更关键的是，当 Agent 迈向锁库存、扣款等跨系统读写编排，绝不能遇错盲目重头重试，状态入库并靠日志与 ACID 事务兜底才是核心基建。

- [2025 年度数据库世界总结：石破天 vs Andy Pavlo 对谈录 · 1. 对 LLM 做 Text-to-SQL 持悲观态度](/db/db-year-review-2025/#1-对-llm-做-text-to-sql-持悲观态度)
- [2025 年度数据库世界总结：石破天 vs Andy Pavlo 对谈录 · 2. Agentic AI 需要 ACID，数据库技术将大放异彩](/db/db-year-review-2025/#2-agentic-ai-需要-acid数据库技术将大放异彩)

### 如何靠 PG 扩展纯 SQL 检索 PDF 并开箱交付？ {#pg-extensions-pdf-and-pig}

构建企业知识库根本不必在库外搭脆弱的下载与解析流水线。正如开发者 Florents Tselai 所示范，组合 `pgpdf` 与 `pgsql-http` 等网络扩展，一条纯 SQL 就能在 PostgreSQL 内直接拉取远程 PDF 抽取文本，并无缝衔接全文分词或 `pgvector` 向量检索。针对 C/Rust 扩展手工编译门槛高的痛点，我通过 Pigsty 与 `pig` 包管理器将 400 余款扩展预编译为十余种主流 Linux 原生安装包，一行配置即可开箱交付。

- [如何在数据库中直接检索PDF · pgpdf + pgsql-http 的强大功能](/db/pdf-in-db/#pgpdf--pgsql-http-的强大功能)
- [如何在数据库中直接检索PDF · 如何获取这些扩展？](/db/pdf-in-db/#如何获取这些扩展)

### 如何一条 SQL 亚秒算完百万行扑克 24 点？ {#sql-poker-24-and-extension}

在禁用自定义函数的前提下用一条 SQL 算扑克 24 点，实时暴力穷举纯属算力灾难。利用算术基本定理将牌面 1～10 映射为前 10 个质数（2 至 29）求积，即可消除顺序生成唯一整数键，降维成与 566 条有解字典 CTE 的单次 Merge Join，M1 单核扫完 100 万行仅需 0.58 秒。面对 10 KB 代码上限，坚守精简内核的 PG 将压缩交由 `pgsql-gzip` 扩展压至 7796 字节——禁扩展测 PG 无异于自缚手脚。

- [使用一条 SQL 计算扑克24点 · 解法](/db/poker-24/#解法)
- [使用一条 SQL 计算扑克24点 · 压缩优化](/db/poker-24/#压缩优化)

### 既然多进程怕高并发，为什么 PG 不内置连接池？ {#why-no-builtin-pool}

PostgreSQL 恪守“一事一程序”的 Unix 哲学：内核专心做好可靠“发动机”，把突发连接缓冲、故障切换与读写分离交给外置“变速箱”（连接池）。裸内核直怼高并发如同发动机硬绑车轮，但强塞内置池或硬改多线程又会破坏内核简洁与弹性。正道是用 Pigsty 这类发行版预装内核、pgBouncer 与高可用，实现无感“整车交付”。

- [你为什么不用连接池？ · PG 应该内置一个连接池吗？](/db/why-no-connection-pool/#pg-应该内置一个连接池吗)
