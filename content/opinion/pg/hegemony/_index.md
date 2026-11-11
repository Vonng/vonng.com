---
title: PG 盛世、选型与商业版图
linkTitle: PG 盛世与商业版图
description: 为什么 PostgreSQL 吞噬了数据库世界、对 MySQL/Oracle/MSSQL 的全面替代、巨头并购潮与中文社区复兴。
weight: 10
icon: fa-solid fa-crown
---

数据库内核的王座之争已经尘埃落定：PostgreSQL 正像当年的 Linux 一样吞噬整个数据库世界，把关系事务、文档、地理空间、时序、搜索与 AI 向量检索尽数坍缩进单一可扩展底座，只给嵌入式 SQLite 与分析型 DuckDB 留下错位共生的生态位。当社区治理确保没有任何商业巨头能私有化 PG 内核后，下半场的主矛盾已从“选什么数据库内核”全面上移为“发行版战争、控制面锁定与供应链主权”。本篇系统拆解 PostgreSQL 三十年崛起机理、对 MySQL 及商业数据库的全面替代、硅谷十亿美元级并购潮、开源协议定力以及中文社区基础设施复兴的核心论断。

## 一、为什么 PostgreSQL 吞噬了数据库世界 {#why-pg-ate-the-world}

### PG 凭什么从学院原型长成数据库界的 Linux？ {#from-berkeley-to-linux}

PostgreSQL 虽源于图灵奖得主 Stonebraker 1986 年的伯克利 POSTGRES，但真正将其接生到现代世界的，是 1994 年为其换上标准 SQL 并放上互联网的华人研究生 Jolly Chen 与 Andrew Yu；1996 年 7 月 8 日公开 CVS 架设，标志着它脱离单一机构成为全球社区资产。此后已故先驱 Simon Riggs 补齐 PITR、热备可读从库、同步流复制与分区表等企业级基石，而四十年前埋下的“可扩展性”架构种子更让所有新数据范式直接长在 PG 之上。到 PG 17 发布时，官方底气十足地删去“关系型”定语，直称“世界上最先进的开源数据库”并正面叫板顶级商业库。

- [PostgreSQL 三十岁生日快乐 · 为什么是 7 月 8 日？](/pg/happy-30-birthday/#为什么是-7-月-8-日)：考证 1996 年 7 月 8 日公开 CVS 首笔提交 `d31084e` 的历史节点，阐明脱离单一机构开启全球社区共治的里程碑意义。
- [参加 PostgreSQL 30周年开发者大会 · 本文 AI 含量 0%](/pg/pgconfdev-2026/#本文-ai-含量-0)：还原 Jolly Chen 与 Andrew Yu 为伯克利原型换上标准 SQL 并开源上网、交棒社区核心团队的关键转折。
- [PostgreSQL 三十岁生日快乐 · 三十而立](/pg/happy-30-birthday/#三十而立)：论证比 MVCC、流复制与 JSONB 单点特性更深远的核心竞争力，是使 PostGIS、Citus、`pgvector` 原生生长的可扩展基因。
- [PostgreSQL 主要贡献者 Simon Riggs 因坠机去世](/pg/simon-riggs/)：回顾 Simon Riggs 在时间点恢复、热备可读从库、同步流复制与分区表上的奠基贡献如何撑起企业核心生产底盘。
- [PostgreSQL 17 发布：摊牌了，我不装了！ · 关于 PostgreSQL](/pg/pg-17/#关于-postgresql)：解读官方发布注记删去“关系型”限定词、公开宣称比肩超越顶级专有商业数据库的战略宣言。

### 全球开发者调研如何印证 PG 的断层统治力？ {#survey-and-ranking-dominance}

数万样本的 Stack Overflow 调研连续三年记录了王座易主与断层拉开：PostgreSQL 使用率从 2023 年首次反超 MySQL（45.6% 对 41.1%）、2024 年专业开发者首次过半（51.9%），一路飙升至 2025 年的 58.2%，甩开第二名 MySQL 达 18.6 个百分点，连续包揽流行度、喜爱度与需求度三冠王。用“喜爱减厌恶”构造净喜爱指数（NLS）更能看清口碑决定份额导数的铁律：PG 凭全场最高的 44% NLS 兑现每年 460 个基点的份额增长；而在 AI 向量需求拉动下两年内从 19% 暴涨至 47% 的需求度，已提前锁定未来数年的增量江山。

- [PostgreSQL：最成功的数据库 · 过去的积累：流行度](/pg/pg-is-no1/#过去的积累流行度)：基于 2023 年 9 万名开发者样本，记录 PG 总体流行度首次反超 MySQL 并包揽三榜第一的历史拐点。
- [StackOverflow 2024调研：PostgreSQL已经杀疯了 · 流行度](/pg/pg-is-no1-again/#流行度)：剖析 2024 年专业开发者 PG 使用率首次过半（51.9%）并将对 MySQL 领先身位扩大至 12.5 个百分点的八年长牛曲线。
- [StackOverflow 2024调研：PostgreSQL已经杀疯了 · 喜爱度与需求度](/pg/pg-is-no1-again/#喜爱度与需求度)：拆解 74.5% 留存喜爱度与两年翻倍至 47% 的选型需求度，对比 TiDB 口碑断崖下跌与 MySQL 需求度滑落第三。
- [PostgreSQL 已主宰数据库世界 · 流行度](/pg/so2025-pg/#流行度)：展示 2025 年专业开发者 58.2% 使用率的断层统治、DuckDB 与 Supabase 的爆发，以及封闭化 MongoDB 的负增长。
- [为什么PostgreSQL是最成功的数据库？ · 最喜爱](/pg/pg-is-best/#最喜爱)：建立净喜爱指数（NLS）与六年流行度年化增速的定量映射，证实 PG 44% 口碑优势对市场份额增长的先行预测力。

### 为何说可扩展性才是 PG 跨越三波浪潮的撒手锏？ {#extensibility-three-waves}

单论先进 Oracle 不落下风，单论开源 MySQL 亦占一席；真正让 PostgreSQL 在 420 多款竞品中八年五夺 DB-Engines 年度总冠军的独门武器，是作为通用数据管理框架的极致可扩展性。单点特性领先三年就会被抹平，唯有持续进化才是最强护城河——PG 借此完成三级跳：传统软件时代靠 PostGIS 垄断测绘，移动互联网浪潮内置 JSONB 吞下文档库，AI 浪潮又凭 `pgvector` 稳坐头把交椅。正如核心组成员 Jonathan Katz 所划分，内核专攻 SQL 标准与底层路径优化，再由发行版将数百扩展预编译打包消除“扩展蔓延”，便化作了碾压级生产力。

- [PostgreSQL，三十而立 · 四、三十年，三级跳](/pg/pg-turns-30/#四三十年三级跳)：复盘 PostGIS 制霸空间数据、内置 JSONB 消解 NoSQL 冲击与 `pgvector` 承接 AI 浪潮的三次时代跨越。
- [PostgreSQL 2024 社区现状调查报告 · 选择 PG 的原因](/pg/pg-survey-2024/#选择-pg-的原因)：解析 Timescale 社区调研数据，说明“开源 + 可靠”构成信任底盘，而繁荣插件生态才是区别于商业与同类开源库的灵魂。
- [PostgreSQL荣获2024年度数据库之王！（第五次） · PostgreSQL 为什么这么牛逼？](/pg/pg-dbeng-2024/#postgresql-为什么这么牛逼)：阐明可扩展护城河如何叠加 350 余款扩展的 Linux 原生二进制打包工程，让用户免去编译折腾开箱即用。
- [2023年度数据库：PostgreSQL (DB-Engine) · 年度数据库：PostgreSQL](/pg/dbengines-2023/#年度数据库postgresql)：剖析绝对流行度分值增量评选法如何过滤低基数噪音，印证 PG 力压 Databricks 与 BigQuery 四度夺魁的常青统治力。
- [展望 PostgreSQL 的2024 · 扩展](/pg/pg-in-2024/#扩展)：引述 Jonathan Katz 对内核主干（聚焦 `JSON_TABLE`、迁移兼容与向量 TOAST 优化）与外围“扩展蔓延”治理的边界划分。

### 为什么“一切皆用 Postgres”能根治组件泛滥？ {#just-use-postgres}

死于架构过度复杂的团队远多于死于工具太简单的团队。TimescaleDB CEO Ajay Kulkarni 与 CTO 教练 Stephan Schmidt 都点破了专用数据库泛滥的恶果：把关系、缓存、队列与搜索拆成五六个异构组件，只会让研发困死在跨库胶水代码里。百万用户规模内，用 `UNLOGGED TABLE` 平替缓存、`SKIP LOCKED` 平替队列、`JSONB` 平替文档库，叠加上事务性 DDL、并发不锁表变更与万能 FDW 足以一库通吃。我早年在探探的实战就是铁证：零 Redis 缓存、仅靠百余台 PG 硬扛数百万日活、数百 TB 数据与 250 万全局 TPS，反倒是日活近千万后拆微服务把敏捷系统拖进了泥潭。

- [为什么PostgreSQL是未来数据库的事实标准？ · 第四部分：数据库越多，问题越多](/pg/pg-for-everything/#第四部分数据库越多问题越多)：引述 Ajay Kulkarni 对数百种专用数据库拼凑脆弱数据迷宫、吞噬核心产品研发创造力的批判。
- [技术极简主义：一切皆用Postgres · 然而，我们有极致简化的方案](/pg/just-use-pg/#然而我们有极致简化的方案)：梳理 Stephan Schmidt 在百万用户规模内用原生 PG 特性与扩展平替缓存、消息队列、文档库和搜索引擎的极简清单。
- [技术极简主义：一切皆用Postgres · 译者评论](/pg/just-use-pg/#译者评论)：结合探探零缓存靠百余台 PG 硬扛 250 万 TPS 及 100ms 存储过程推荐算法的实战，警示过早微服务化的复杂度灾难。
- [PostgreSQL好处都有啥 · 全栈数据库](/pg/pg-is-good/#全栈数据库)：总结单组件覆盖 OLTP、OLAP、GIS、时序、流处理与文档存储如何砍掉异构胶水代码、大幅推迟架构分拆阈值。
- [PostgreSQL好处都有啥 · 运维友好](/pg/pg-is-good/#运维友好)：详解事务性 DDL、在线并发建索引重整、多维同步复制以及一行 SQL 搞定跨源 ETL 的 FDW 运维利器。

### 在 Agent 时代，多元持久化为何成了诱发幻觉的毒药？ {#ai-agent-zero-glue}

编写 SQL 的头号主体正从人类静默更替为 AI Agent。在上下文注意力最稀缺的 Agent 架构下，微服务时代的“多元持久化”已沦为认知毒药：把数据拆进 MySQL、MongoDB、ES、Redis 和 Milvus，逼迫 Agent 将多套驱动语法与异构 Schema 塞满窗口，再写胶水代码做跨库搬运与应用层 Join，白白烧掉推理 Token 并诱发幻觉飙升。PostgreSQL 借全栈扩展与 FDW 将关系、全文与向量混合检索坍缩进单条 ACID SQL，实现了“零胶水架构”；且主流大模型天生精通 PG 方言，一行连接串进入 `psql` 就是比任何专用 SDK 都确定的 Agent 操作系统。

- [为什么PG将主宰AI时代的数据库 · 多元持久化：碎片化的认知噩梦](/pg/ai-db-king/#多元持久化碎片化的认知噩梦)：剖析多库异构“乒乓架构”如何挤占有限上下文窗口、消耗 Token 预算并在跨库胶水逻辑中放大模型幻觉。
- [为什么PG将主宰AI时代的数据库 · PostgreSQL：零胶水架构](/pg/ai-db-king/#postgresql零胶水架构)：展示单连接单方言内融合关系过滤、全文与向量检索、位置透明 FDW 及节省 Prompt 的多语言存储过程闭环。
- [为什么PG将主宰AI时代的数据库 · 接口标准化：psql 即 IDE](/pg/ai-db-king/#接口标准化psql-即-ide)：论证预训练语料深厚覆盖的 PG SQL 与 `libpq` 协议如何让 `psql` 结合联网与外部表扩展化身为全能 Agent 执行环境。
- [PostgreSQL 三十岁生日快乐 · 下一个三十年](/pg/happy-30-birthday/#下一个三十年)：阐明在智能体接管 SQL 编写与数据主权博弈加剧的未来，不受单一商业巨头控制的开放 PG 是最稀缺的记忆底座。

### 硬件跃迁与 DuckDB 合流如何颠覆数仓与新内核创业？ {#hardware-duckdb-convergence}

当年将 OLAP 数仓从事务库拆分，是用冗余和 ETL 去补单机算力短板；如今单台双路服务器坐拥 512 核 vCPU、数 TB 内存与数十 TB NVMe 闪存，配合 S3 足以吞下 99% 企业的全量数据，“合久必分”正回归单栈超融合。随着实时分析跃居 PG 第四大场景，出自分析圣地 CWI、单文件 MIT 开源的 DuckDB 由原厂下场推出 `pg_duckdb`，逼得 ParadeDB 等玩家纷纷弃轮跟进，重演了 `pgvector` 荡平独立向量库的收敛剧本。这也彻底改写了创业铁律：通用新内核再无生存空间，垂直专用库若无数量级优势，终将被低成本快速迭代的 PG 扩展复刻吞并。

- [PostgreSQL 正在吞噬数据库世界 · 分久必合的数据库领域](/pg/pg-eat-db-world/#分久必合的数据库领域)：算清现代百核 TB 内存硬件与 S3 存储抹平容量瓶颈的账本，宣告 99% 企业告别笨重大数据拆分的超融合拐点。
- [PostgreSQL 正在吞噬数据库世界 · 改变游戏规则的玩家](/pg/pg-eat-db-world/#改变游戏规则的玩家)：剖析新数据库内核面对全副扩展武装 PG 时的生存拷问，揭示扩展生态滚雪球复刻细分赛道的降维打击机制。
- [谁整合好DuckDB，谁赢得OLAP世界 · DuckDB：OLAP的新兴挑战者](/pg/pg-duckdb/#duckdbolap的新兴挑战者)：解析 CWI 出品的 DuckDB 如何凭单文件架构、PG 语法兼容、ClickBench 顶级表现与 MIT 协议实现一年 2.3 倍爆发。
- [谁整合好DuckDB，谁赢得OLAP世界 · 第二届PG扩展竞速比赛](/pg/pg-duckdb/#第二届pg扩展竞速比赛)：复盘原厂 `pg_duckdb` 入局如何以“原厂吊打同人”之势终结扩展混战，并让全量打包插件的 PG 发行版稳摘桃子。
- [PostgreSQL 2024 社区现状调查报告 · 工作](/pg/pg-survey-2024/#工作)：引用 2024 社区调研中“实时分析”跃居第四大应用场景的数据，预判库内 OLAP 扩展取代传统实时数仓的趋势。

### 列存扩展与冷热分层如何打破 PG 的百 TB 大数据瓶颈？ {#in-db-olap-and-tiered-storage}

认为 PostgreSQL 搞不定复杂分析与海量归档早已是老黄历。百 GB 量级内，10 核 M1 Max 笔记本原生跑完 22 条复杂 SQL 的 10GB TPC-H 仅需 56 秒，配合流复制与逻辑复制本身就是丝滑的 HTAP 底座，上探数 TB 还可无缝衔接同源的 Greenplum 或 MatrixDB。而在前沿扩展侧，`pg_mooncake` 将 DuckDB 向量化与 SIMD 引擎嵌入库内并由 PG 直接托管 Parquet 统计信息做文件跳过，首次让“PG + 扩展”杀入 ClickBench 前十媲美 ClickHouse；再叠加 Ajay Kulkarni 展示的本地高速盘加 S3 透明冷热分层“无限存储表”，单栈 PG 已能从容承载百 TB 至 PB 级分析负载。

- [PostgreSQL 生态前沿进展 · pg_mooncake](/pg/pg-frontier/#pg_mooncake)：解析 `pg_mooncake` 嵌入 DuckDB 引擎并由 PG 管理列存元数据杀入 ClickBench 前十的技术路径及与 `pg_duckdb` 的竞合。
- [为什么PostgreSQL是未来数据库的事实标准？ · 大数据则何如？](/pg/pg-for-everything/#大数据则何如)：引述 Ajay Kulkarni 对本地磁盘驻留热数据、S3 透明卸载冷数据的分层存储架构拆解，打破 PG 容量上限偏见。
- [PostgreSQL 到底有多强？ · TPC-H分析性能](/pg/pg-performence/#tpc-h分析性能)：实测 M1 Max 上 1GB（8 秒）与 10GB（56 秒）TPC-H 单核归一化 QPH 表现，给出流复制、逻辑复制至 MPP 的演进阶梯。

## 二、全面压倒 MySQL、跑分真相与黑稿祛魅 {#crush-mysql-and-benchmarks}

### 为什么说 PG 已赢下增量世界，而 MySQL 沦为遗产？ {#pg-vs-mysql-verdict}

超大规模生产选型以 2010 年为分水岭：Meta、GitHub 等 MySQL 案例皆属旧时代产物；此后崛起的 OpenAI（单主库加近 50 个只读副本扛 8 亿用户百万 QPS）、Figma、Notion、探探及超半数新晋 YC 创业项目一致默认选 PG。Docker Hub 周拉取量 3.8:1、AWS 实例比拉开至 3:2 且新一代 Aurora DSQL 独占兼容 PG、Vercel 存储推荐榜 MySQL 挂零，均宣告增量彻底归属 PG。过去六年两者份额涨跌相关系数高达 `r = -0.96`，证明 MySQL 流失存量正直接置换为 PG 增量；错失 AI 向量浪潮的 MySQL，终将退化为数据库界的 PHP。

- [PostgreSQL vs MySQL 2026 · 七、总体判断](/pg/pg-vs-mysql-2026/#七总体判断)：汇总 Stack Overflow、JetBrains 与 Docker Hub 3.8:1 拉取量三大独立口径，论证增量归属 PG 且国内正以翻倍增速追赶。
- [PostgreSQL vs MySQL 2026 · 时代特征](/pg/pg-vs-mysql-2026/#时代特征)：划定 2010 年选型分水岭，对比早期互联网遗留 MySQL 集群与 OpenAI、Figma、Notion 及过半 YC 项目的 PG 默认栈。
- [PostgreSQL取得对MySQL的压倒性优势](/pg/pg-beats-mysql/)：披露 AWS 实例比 3:2、Aurora DSQL 弃用 MySQL 与 Vercel 存储零推荐实况，剖析错失 `pgvector` 向量浪潮如何注定其“PHP 化”宿命。
- [如何看待 MySQL vs PGSQL 直播闹剧 · MySQL 的用户都流失到哪儿去了？](/pg/mysql-pg-live-drama/#mysql-的用户都流失到哪儿去了)：通过六年份额散点回归得出 `r = -0.96` 极强负相关与总量守恒水平线，定量坐实 MySQL 存量向 PG 的单向置换。

### 关系型“三国演义”中，治理与内核基因如何决定胜负？ {#governance-and-trilogy}

主流关系型博弈归根结底是“德才兼备”：Oracle 积淀深厚但授权天价、法务横行，属“有才无德”；MySQL 早年靠互联网简单 CRUD 的“糙猛快”走红，等 PG 补齐快与猛后，手里只剩默认允许报错事务部分提交、违背原子性的“糙”，属“才浅德薄”。制度根源更决定生死：PG 核心提交者分散在多巨头制衡的独立社区，配合类 BSD 协议与教科书级源码孕育繁荣插件生态；而受 GPL 束缚且被 Oracle 独占的 MySQL 在 2025 年裁撤半数研发后近乎停滞，逼得 PlanetScale 掉头上线 PG，连 Percona 联创也联署公开信坦言其沦为遗留技术。

- [PostgreSQL：最成功的数据库 · 但是，为什么呢？](/pg/pg-is-no1/#但是为什么呢)：用“Oracle 有才无德、MySQL 才浅德薄、PG 德才兼备”拆解三大根协议博弈的终局逻辑。
- [为什么PostgreSQL是最成功的数据库？ · vs MySQL](/pg/pg-is-best/#vs-mysql)：剖析互联网草莽期“糙猛快”红利退潮后，MySQL 允许部分事务提交等破坏一致性设计在严肃场景下的溃败。
- [PostgreSQL vs MySQL 2026 · 六、社区治理](/pg/pg-vs-mysql-2026/#六社区治理)：对比多巨头制衡的 PG 独立社区与 Oracle 2025 年裁撤半数 MySQL 团队导致社区版至今缺席原生向量搜索的制度代差。
- [PostgreSQL vs MySQL 2026 · 二、厂商战略动向](/pg/pg-vs-mysql-2026/#二厂商战略动向)：记录 PlanetScale 被客户推着上线 PG、TiDB 探索 PG 兼容层以及 Percona 联创近 250 人联署公开信承认其遗留化的集体倒戈。
- [PostgreSQL好处都有啥 · 生态健康](/pg/pg-is-good/#生态健康)：对比 GPL 传染性枷锁与类 BSD 宽松协议加高质量内核源码，解释 Citus、TimescaleDB 为何能收敛反哺为原生插件。

### 搜索指数与“中国加权”为何推翻不了 PG 第一的结论？ {#rebut-dbengines-and-china-weight}

拿 DB-Engines 总榜或“中国样本偏少”否定 PG 全球第一根本站不住脚。DB-Engines 只是抓取热搜词拼凑的二手指数，既分不清喜爱还是报错踩坑，又让拥有 `pg`、`postgres` 等五种拼写的 PG 天然吃亏，统计效力远逊于 9 万样本一手问卷——何况其十三年曲线同样唯独 PG 与 Snowflake 长牛，编辑部更八年五授其年度冠军。就算按 8% 未参调中国开发者权重与百度指数（`1260:5283`）强行加权，全球流行度仍是 PG（43.46%）压过 MySQL（43.24%）；在云账本上，AWS 全球两者实例早已 1:1 且 PG 营收反超，连阿里云 RDS 营收比也已达约 1:5。

- [驳《MySQL：这个星球最成功的数据库》 · 搜索引擎指数更权威？](/pg/rebut-mysql-best/#搜索引擎指数更权威)：从统计方法论剖析二手热搜指数相比 9 万样本一手抽样问卷的低效力，指出多拼写变体对 PG 搜索词频的稀释效应。
- [PostgreSQL荣获2024年度数据库之王！（第五次） · 让我们来看看更多详细的数据](/pg/pg-dbeng-2024/#让我们来看看更多详细的数据)：对比问卷真实渗透率与榜单横向失真，用十三年对数增长曲线及五度夺冠印证 MySQL 年度最大跌幅与 PG 的统治力。
- [驳《MySQL：这个星球最成功的数据库》 · 中国加权校正后的估算流行度](/pg/rebut-mysql-best/#中国加权校正后的估算流行度)：综合 GitHub 占比与市场体量设定 8% 权重及百度指数折算国内使用率，证明加权后全球仍是 PG（43.46%）领先。
- [驳《MySQL：这个星球最成功的数据库》 · PostgreSQL 营收是 MySQL 0.1%？](/pg/rebut-mysql-best/#postgresql-营收是-mysql-01)：披露 AWS RDS 实例 1:1 且 PG 营收占优、阿里云 RDS 营收比达 1:5 的真实商业账本，击碎“0.1% 营收”谣言。

### 中外数据库演进为何差十年，人群结构如何迁移？ {#ten-year-lag-and-demographics}

拉通 Google Trends、Yandex 与百度指数可见，各国“PG 与 MySQL 热度差”同发达程度相关系数高达 `r = 0.6`，美（69:61）、俄（70:22）早已反超；而中国波形相当于全球曲线右移约 10 年，MySQL 直到 2015 年前后才见顶，这正是国内企业曾感叹 PG 熟手比 MySQL 难招的历史成因。再拆解 9 万名受访者画像：5.6% 的初学者偏爱拿 MySQL 入门（58.4%），94.4% 的专业开发者则显著青睐 PG（49.1%），转移和弦图中唯一显著的主航道就是从 MySQL 单向流向 PG。逆势死守过气技术，无异于当年押注电子管而错失晶体管。

- [如何看待 MySQL vs PGSQL 直播闹剧 · 菜鸟都在哪儿呢？](/pg/mysql-pg-live-drama/#菜鸟都在哪儿呢)：交叉对比 5.6% 初学者与 94.4% 专业开发者的选型偏好及转移和弦图，揭示从 MySQL 入门向 PG 进阶的单向演进路径。
- [如何看待 MySQL vs PGSQL 直播闹剧 · 哪些国家 PostgreSQL 更流行？](/pg/mysql-pg-live-drama/#哪些国家-postgresql-更流行)：量化计算美俄等国搜索热度反超数据，得出数据库选型先进度与发达国家变量 `r = 0.6` 的强正相关及国内十年滞后。
- [驳《MySQL：这个星球最成功的数据库》 · 中国特色](/pg/rebut-mysql-best/#中国特色)：对照全球 2004 年见顶与国内 2015 年见顶的平移曲线，以电子管与晶体管之喻警示逆全球迁移大势重仓旧栈的资源浪费。
- [PostgreSQL好处都有啥 · 问题](/pg/pg-is-good/#问题)：辨析定期 `VACUUM` 等可控技术细节与传统 Java/PHP 路径依赖造成存量熟手偏少这一真实推广痛点。

### 用 PG 的开发者真能比用 MySQL 多赚四成吗？ {#pg-developer-salary-premium}

就业市场早已用真金白银定价。核算 Stack Overflow 全球 44,354 份专业开发者薪酬样本可见，全球 PG 开发者年薪中位数（62.5 万元）比 MySQL（54.3 万元）高 15%，且样本超 600 人的全部 31 个国家无一例外满足“PG > 全体均值 > MySQL”铁律。固定国别基线后，PG 普遍带来 5%～10% 溢价，MySQL 则折价 5%～10%；而在受早期大厂路径依赖影响、PG 采用率仅 27.6% 的中国市场，人才稀缺直接把 PG 中位数（42.1 万元）推至 MySQL（30.8 万元）的 1.37 倍。正如 Go 替代 Java，押注一专多长的 PG 才是跳出 CRUD“数据矿工”内卷的最优杠杆。

- [用PG的开发者，年薪比MySQL多赚四成？ · 太长不看](/pg/pg-dev-salary/#太长不看)：汇总 4.4 万份薪酬样本，验证全球 31 国无一例外的“PG > 中位数 > MySQL”薪资排序及中国市场 1.37 倍（42.1 万对 30.8 万）高溢价。
- [用PG的开发者，年薪比MySQL多赚四成？ · 关键发现](/pg/pg-dev-salary/#关键发现)：固定各国 50 分位薪酬基线，剥离出 PG 上浮 5%～10%（中国上浮 28%）与 MySQL 下浮 5%～10%（中国下浮 25%）的纯技术栈溢价。
- [用PG的开发者，年薪比MySQL多赚四成？ · 关于数据库流行度](/pg/pg-dev-salary/#关于数据库流行度)：剖析中国 27.6% 垫底采用率背后的互联网大厂存量惯性，论证最低渗透率沿着全球轨道均值回归所释放的人才窗口期。
- [为什么PostgreSQL前途无量？ · 弃暗投明？](/pg/pg-is-great/#弃暗投明)：对标 Instagram、探探与 Apple 的“Go + PG”代际替换，阐明掌握多模 PG 如何帮助工程师跳出低附加值 CRUD 内卷。

### 单机 PG 性能极限有多强，对决 MySQL 谁更快？ {#single-node-pg-extreme-perf}

现代多核与 NVMe 硬件早已把单机 PG 武装成吞吐怪兽：亿级行 `pgbench` 实测中，10 核 M1 Max 笔记本即达 24 万点查 QPS，96 核 `c5d.metal` 物理机常规安全配置下跑出 62.6 万点查与 7.2 万读写 TPS，极限调优更飙至 200 万点查 QPS 与 13.7 万读写 TPS——区区几台十万元内的物理机就足以扛下探探全局 40 万 TPS 负载。至于 MySQL 官网炫耀的百万点查，实则是关停 Binlog、`fsync` 与双写刷出的非生产成绩；若对等采用这套 Dirty Hack 卸除落盘约束同台对决，PG 点查峰值直冲 233 万 QPS（同限 48 并发仍超 MySQL 峰值 43%），混合读写亦不分伯仲。

- [PostgreSQL 到底有多强？ · PGBENCH](/pg/pg-performence/#pgbench)：给出 M1 Max 笔记本与 96 核 `c5d.metal` 物理机在亿级数据集上从常规配置（62.6 万 QPS）到极限调优（200 万 QPS / 13.7 万 TPS）的完整压测数据。
- [PostgreSQL 到底有多强？ · Dirty Hack](/pg/pg-performence/#dirty-hack)：拆穿官网关闭落盘安全特性的刷分套路，在对等卸除安全约束条件下实测 PG 233 万点查 QPS 反超 MySQL 峰值的硬核对比。

### “慢 360 倍”黑稿与刷榜 TPC-C 耍了什么把戏？ {#debunk-360x-and-tpcc}

网传“PG 比 MySQL 慢 360 倍”是不敢公开复现脚本的典型钓鱼黑稿：发帖者故意挂起长 Idle 事务锁死快照阻塞回收，再狂刷百万行更新人为制造死元组堆积——无异于手动关掉垃圾回收器再造垃圾来证明语言慢，正常生产环境靠空闲事务超时与 HOT 更新早已杜绝此类反模式。同理，耗资数亿元堆服务器去刷国际上十年无人问津的三十年前 TPC-C 老榜，参考价值还不如 `sysbench`，纯属营销放卫星。严肃评测应以 Mark Callaghan 的《Small Datum》为标杆公开模型与代码，靠黑稿或买榜只会透支信誉。

- [PG被黑慢MySQL 360倍，这次我真忍不了 · PostgreSQL vs MySQL @ 2025](/pg/pg-360x-slower/#postgresql-vs-mysql--2025)：拆穿故意挂起长空闲事务制造死元组膨胀的钓鱼障眼法，并以《Small Datum》为标杆划清严谨可复现评测与口水黑稿的底线。
- [如何看待 MySQL vs PGSQL 直播闹剧 · 更新：关于打榜 SB 行为](/pg/mysql-pg-live-drama/#更新关于打榜-sb-行为)：批判斥巨资堆硬件冲刺三十年前古老 TPC-C 跑分的营销放卫星乱象，点明其脱离现代数据库真实负载的本质。

## 三、替代商业数据库、协议兼容与架构回流 {#replace-commercial-and-newsql}

### PG 如何完成对其余四大主流数据库的协议兼容合围？ {#four-major-db-compatibility}

同时踩中去 IOE 替代、多模复杂处理与国内份额均值回归三重红利后，PostgreSQL 开源生态已完成对 DB-Engines 前五名其余四家的全面兼容合围：AWS 开源的 Babelfish 借轻度内核修改与四个扩展直接在 1433 端口兼容 TDS 线缆协议与 T-SQL，与 5432 原生端口双协议并存，让微软 SQL Server 成了最易被无缝替代的对象；FerretDB 2.0 切换至微软开源的 DocumentDB 扩展后性能跃升超 20 倍，零改代码即可接管 MongoDB 负载；再加上兼容 MySQL 5.7 线缆协议的 OpenHalo 与兼容 Oracle 的 IvorySQL，四大异构生态已在统一 PG 发行版中会师。

- [OpenHalo：MySQL线缆兼容的PostgreSQL来了！ · 还有其他内核花活](/pg/openhalo-mysql/#还有其他内核花活)：盘点 Babelfish、IvorySQL、FerretDB/DocumentDB 与 OpenHalo 集齐前五大主流数据库兼容能力并在统一发行版开箱即用的全景。
- [PostgreSQL可以替代微软SQL Server吗？ · Babelfish](/pg/pg-replace-mssql/#babelfish)：详解 Babelfish 在 1433 端口直接兼容 TDS 线缆协议与 5432 原生端口双协议同库共存的无痛替代机制。
- [PostgreSQL 生态前沿进展 · FerretDB](/pg/pg-frontier/#ferretdb)：剖析 FerretDB 2.0 借力微软 DocumentDB 扩展实现 20 倍性能跃升、零代码修改接管 MongoDB 负载并继承数百 PG 插件的优势。
- [为什么PostgreSQL前途无量？ · 竞争关系](/pg/pg-is-great/#竞争关系)：梳理头部关系库下行周期中，PG 凭开源替代 Oracle、凭多模碾压 MySQL 及国内份额均值回归的三重增长势能。

### 去 O 遇上闭源遗留包，为何绕不开 IvorySQL？ {#oracle-sysdate-and-ivorysql}

开源把每核十余万元商业授权费直接砸到每核每月二十元硬件成本，原生具备 85% Oracle 兼容度的 PG 天然是去 O 主力；但扩展机制唯独改不了 SQL Parser 语法规则。当 500 强企业的无源码闭源 JAR 包写死光秃秃的 `SYSDATE` 标识符（而非函数调用）急需迁移时，应用与扩展双双无解，唯有改解析器的兼容内核能破局。面对法务凶悍的 Oracle，Apache 2.0 开源的 IvorySQL 采取了务实克制的增量路线：避开高风险私有线缆协议，用标准 PG 驱动连 `1521` 端口提供完整 Oracle 语法与 PL/SQL 兼容，从而紧跟 PG 17/18 最新上游。

- [Oracle 兼容的 PG 真的有用吗？ · 为什么 SYSDATE 这么棘手？](/pg/ivorysql/#为什么-sysdate-这么棘手)：通过 500 强企业无源码 JAR 包写死裸 `SYSDATE` 标识符的真实迁移死局，阐明扩展机制无法触碰 Parser 时的内核改造刚需。
- [Oracle 兼容的 PG 真的有用吗？ · IvorySQL：开源的 Oracle 兼容内核](/pg/ivorysql/#ivorysql开源的-oracle-兼容内核)：解析 IvorySQL 规避线缆协议法务雷区、以增量模块实现双端口语法兼容并紧跟 PG 18.1 上游演进的工程权衡。
- [兼容Oracle的开源 PostgreSQL？ · 快速上手](/pg/oracle-compatible-pg/#快速上手)：对比其他数据库的线缆级兼容，说明客户端走标准 PG 协议连 1521 端口即可获得 PL/SQL、`MERGE` 与系统视图兼容的实操路径。
- [PostgreSQL：最成功的数据库 · 开源之德](/pg/pg-is-no1/#开源之德)：算清从每核十余万商业授权费降至百元级硬件成本的颠覆账本，揭示宽松协议如何让 PG 成为去 O 主力与 36% 国产数据库之母。

### 为什么盲目引入分布式 NewSQL 是过早优化？ {#newsql-premature-optimization}

拉通 TiDB、OceanBase、CockroachDB 与 YugabyteDB 官方百核级 `sysbench` 报告，同生产安全配置下的 96 核单机 PG（137 万点查、51.9 万混合读写）公平对比，分布式 NewSQL 单核归一化吞吐全线落后数倍乃至一个数量级，反倒是主从架构的 PolarDB 表现更稳。NewSQL 的本质是“以量换质”——牺牲复杂 SQL 完备性、稳定性与单核吞吐去换水平扩展上限；但单机 PG 轻松承载 15TB 数据与集群 40 万 TPS，99% 的企业终生摸不到这道天花板，没有 Spanner 的数据命却去交分布式性能税纯属当冤大头。

- [PostgreSQL 到底有多强？ · Fair Play](/pg/pg-performence/#fair-play)：横向拉通百核生产安全配置下的官方 `sysbench` 数据，量化单机 PG 对主流分布式 NewSQL 数倍至数量级的同算力性能碾压。
- [为什么PostgreSQL前途无量？ · vs NewSQL](/pg/pg-is-great/#vs-newsql)：剖析分布式架构“以量换质”牺牲 SQL 完备性的商业困局，用 15TB / 40 万 TPS 单机阈值刺破伪规模焦虑。

### 为什么算力过剩与大模型推动 Web 逻辑回流数据库？ {#omnigres-backend-in-db}

早年应用拆成前后端加数据库三层架构，源于数据库硬件算力紧缺且存储过程受限；如今单机算力大幅富余且 PG 支持二十多种过程语言，架构正迎来“分久必合”。Omnigres 创始人 Yurii 依托 33 个扩展在库内构建含 HTTPD、虚拟文件系统与 Python 的“数据库标准库”，把 Web 全栈塞回数据库。我深耕十年存储过程的体会是，这套范式虽不适合几十万 TPS 巨型核心，但在中小型项目难以普及的唯一命门是研发技能门槛太高；如今大模型编写存储过程已达中高级水准，恰好扫清了最后障碍。

- [PostgreSQL 生态前沿进展 · Omnigres](/pg/pg-frontier/#omnigres)：介绍 Omnigres 依托 33 个扩展在库内直接托管 HTTP 服务与 Web 标准库的技术形态及其在初创与中小型项目中的极简优势。
- [第七届PG生态大会：一些感想 · 如何请外国人参会](/pg/pgconf-china-7th/#如何请外国人参会)：结合十年存储过程重度实战经验评估 Omnigres 范式，阐明大模型娴熟生成高质量存储过程如何破解高技能门槛命门。

### 数据库产品为何必须从盯着 DBA 转向赋能开发者？ {#shift-from-dba-to-developer}

在全程无直播无回放、卸下客套包袱真刀真枪交锋的第七届 PG 生态大会上，马工与萧少聪一语道破天机：数据库的真正用户是开发者而非 DBA。可靠性与安全固然是运维底线，但盯着 DBA 只能做存量搏杀；决定未来增量的一线开发者真正买单的是“用最省力的方式干最多的活”——比如一行 PostGIS 查询顶掉上千行 C++/Java 代码。Neon 与 Supabase 的爆发正是赢在了开发者体验，现代 PG 发行版也必须跳出纯 Ops 舒适区，用数百个开箱即用扩展与自托管 BaaS 直接赋能开发者。

- [第七届PG生态大会：一些感想 · 数据库应该更加关注开发者](/pg/pgconf-china-7th/#数据库应该更加关注开发者)：引述马工与萧少聪关于“一行 PostGIS 顶千行代码”的洞见，阐明从纯 Ops 走向开发者体验与自托管 BaaS 的产品转向。
- [第七届PG生态大会：一些感想 · 如何办好一场会？](/pg/pgconf-china-7th/#如何办好一场会)：复盘无直播无回放纯线下会议与 3～5 分钟闪电交锋如何滤掉“念稿彩虹屁”，激发真刀真枪的行业思辨。

## 四、资本热潮、巨头吞噬 PG 公司与发行版战争 {#capital-mna-and-distro-war}

### 全球风投与云巨头财报为何把筹码全押在 PG 上？ {#capital-all-in-on-pg}

即便在资本寒冬中，数据库赛道的聪明钱也已被 PG 生态包揽。硅谷创业标准栈已收敛为“Vercel/Cloudflare 前端 + Neon/Supabase 托管 PG”：Supabase 继 B、C 轮各融 8000 万美元后半年再拿两亿美元，与十亿美元级并购的 Neon 双双冲上十亿至二十亿美元估值；TimescaleDB 连获重金，刚拿 300 万美元种子轮的 PeerDB 也被闪电收购。二级市场同样定调：微软 CEO 纳德拉在重夺全球市值第一的财报会上点名 Azure PG 连续三季加速增长并覆盖近六成《财富》500 强，提前宣告了赛道终局。

- [PG生态赢得资本市场青睐：Databricks收购Neon，Supabase融资两亿美元，微软财报点名PG · 老冯评论](/pg/pg-capital-market/#老冯评论)：串联 Neon 十亿美元级并购、Supabase 两亿美元新融资与纳德拉财报点名 Azure PG 覆盖六成世界 500 强的资本终局信号。
- [PG系创业公司Supabase：`$80M` C轮融资 · Supabase  B 轮/C 轮融资 `80M $`](/pg/supabase-series-c/#supabase--b-轮c-轮融资-80m-)：梳理 Supabase 连续两轮 8000 万美元融资及 Neon、TimescaleDB、PeerDB 密集吸金脉络，印证增量风投全面押注“数据界 Linux”。

### 三大分析巨头为何斥重金吞噬独立 PG 初创公司？ {#why-olap-giants-buy-pg-startups}

AI 时代数据库格局已彻底收敛为“服务端 PG + 嵌入式 SQLite/DuckDB”：单个 Agent 用完即弃的短命小库下沉到嵌入式或秒级分支存储，企业多 Agent 共享状态的唯一事实源依然是 PG。同时“PG + DuckDB”合流正直接威胁云数仓腹地，三大分析巨头遂挥舞支票簿抢占 Agent 入口：Databricks 十亿美元吞下 Neon 后又收 Mooncake Lab，Snowflake 买下 Crunchy Data，ClickHouse 收购 Xata。这也敲响了开源警钟：`pg_mooncake` 被招安后转向 Iceberg 且原版停更八个月，纯正开源 PG HTAP 的希望最终落回了 DuckDB 官方 `pg_duckdb` 肩上。

- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · 尘埃落定](/pg/clickhouse-got-xata/#尘埃落定)：剖析“服务端 PG + 嵌入式 SQLite/DuckDB”的终局分工，揭示 Databricks、Snowflake 与 ClickHouse 争抢多 Agent 事实源入口的动因。
- [月饼好吃：又一家PG扩展公司被Databricks收购](/pg/databricks-buys-again/)：复盘巨头密集收购 Neon、CrunchyData 与 Mooncake Lab 遏制或主导数仓合流的战略卡位，警示独立扩展被收编后转向停更的风险。

### ClickHouse 如何不动内核完成对 PG 的双向合围？ {#clickhouse-pg-symbiosis}

在“PG 扛在线事务 + 列存做实时分析”成为标配后，精明的异构巨头绝不另起炉灶对抗 PG，而是贴着扩展边界深度共生。以 MySQL 兼容起家的 ClickHouse 走出了教科书级连环棋：先收购提供 10 倍传输加速与 TB 级高速 CDC 的 PeerDB 卡住数仓头号数据源入口；再用 `pg_clickhouse` 直查与 `pg_stat_ch` 遥测插件无缝咬合；最后左联 Ubicloud 推托管 PG 吃下长寿命高吞吐生产库，右收具备写时复制与缩容至零能力的 Xata 承接海量短命 Agent 小库，不改一行 PG 内核便拼齐闭环。

- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · ClickHouse 的 PG 布局](/pg/clickhouse-got-xata/#clickhouse-的-pg-布局)：拆解 PeerDB、`pg_clickhouse`、`pg_stat_ch` 外围咬合加上 Ubicloud 长寿生产库与 Xata 短命 Agent 库的双向合围版图。
- [ClickHouse收购PeerDB：这浓眉大眼的也要来搞 PG 了？ · References](/pg/clickhouse-peerdb/#references)：引述双方披露数据，说明 PG 已成企业头号事务后端，以及 PeerDB 10 倍 CDC 同步加速对实时数仓争夺数据源入口的胜负手价值。

### 内核归属社区无法买走，“发行版战争”究竟争什么？ {#linux-kernel-distro-war}

Stack Overflow 全球数据库迁移图呈现“万流归宗单向汇入 PG”的终局，同生态位竞品悉数失势，当代数据库只剩错位避战或封装 PG 两条生路。正如 Linux 内核一统后竞争转向红帽、Ubuntu 与 Debian，社区宪法确保没有任何巨头能私有化 PG 内核；独立 DBaaS 被密集并购后，真正战场已转向核心人才争夺与发行版价值主张之争，商业锁定也上移至目录、治理与云账单层。在这场发行版内战中，不烧美元 VC、靠稳定现金流把 Pigsty 打造成 Supabase 官方推荐三大自建方案之一，单兵照样能稳坐决赛牌桌。

- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · 格局演变：发行版战争](/pg/clickhouse-got-xata/#格局演变发行版战争)：类比 Linux 终局，阐明独立 DBaaS 被并购收敛后核心人才争夺与控制面、目录及账单层锁定的新博弈焦点。
- [PostgreSQL 已主宰数据库世界 · 迁移图](/pg/so2025-pg/#迁移图)：解读 2025 全球数据库单向迁入 PG 的流向图，剖析 RDS、Supabase、EDB、Percona、Crunchy 与 Pigsty 争夺发行版生态位的格局。
- [StackOverflow 2024调研：PostgreSQL已经杀疯了 · 小结](/pg/pg-is-no1-again/#小结)：总结当代数据库仅剩“云数仓/嵌入式错位避战”与“套壳封装 PG”两条增长路径，预判下半场发行版内战主轴。
- [PG生态赢得资本市场青睐：Databricks收购Neon，Supabase融资两亿美元，微软财报点名PG · 老冯评论](/pg/pg-capital-market/#老冯评论)：论证在美元风险基金退潮背景下，靠扎实开源自建体验与稳定自我造血参与全球 PG 发行版竞争的现实路径。

## 五、开源许可证定力、云账单刺客与供应链主权 {#license-cloud-and-supply-chain}

### Redis 等相继改协议，PG 会背弃宽松开源吗？ {#will-pg-change-license}

绝无可能。正如核心组成员 Jonathan Katz 所阐明，PGDG 承诺永久采用极度宽松的类 MIT/BSD 许可证：PG 总部中立设在加拿大，治理权分散在多家相互制衡的机构中，连受制裁的俄罗斯 Postgres Pro 团队都能平等贡献；任何改协议企图在制度上根本无法通过，更会瞬间毁掉三十年全球信任。也正靠这份零门槛定力，PG 拥有全球最庞大的协议兼容与衍生数据库谱系（含 openGauss 等国产主力），而版权攥在商业巨头 Oracle 手里的 MySQL 才真正面临信创出局。

- [PostgreSQL会修改开源许可证吗？ · PostgreSQL会修改开源许可证吗](/pg/pg-license/#postgresql会修改开源许可证吗)：引述 Jonathan Katz 的权威回应，从防单一实体控盘的治理制度与三十年声誉根基论证 PG 永久坚守宽松许可证的必然性。
- [如何看待 MySQL vs PGSQL 直播闹剧 · BSD 是流氓协议？？](/pg/mysql-pg-live-drama/#bsd-是流氓协议)：驳斥对类 BSD 协议的无知抹黑，对比加拿大独立社区中立治理（含俄罗斯团队平等参与）与 Oracle 掌控 MySQL 的信创风险。
- [驳《MySQL：这个星球最成功的数据库》 · BSD 是流氓协议？？](/pg/rebut-mysql-best/#bsd-是流氓协议)：结合全球数据库谱系数据，证实中立治理与友好许可证使 PG 成为全球数据库创业及国产衍生版无可争议的第一母体。

### NoSQL 集体改投 SSPL，协议背刺与自建短板有何代价？ {#sspl-backlash-and-selfhost}

MongoDB、ES 与 Redis 宁背“闭源”骂名也要改投 SSPL，实则是被公有云白嫖吸血再拉分叉贴牌“真开源”逼出的自卫反击，撕开了教条化 OSI 定义沦为云厂商白嫖保护伞的局限——软件自由才是目的，“开源”只是手段。但在开发者市场上，任何协议背刺或自建割裂都会遭口碑反噬：Redis 改协议后，开源分叉 Valkey 首秀即凭 64.7% 喜爱度顶替上位；而 Supabase 喜爱度跌至 47.2%，则是因客户长大下云自建时，其简陋的 Docker Compose 玩具模板暴露了严重的生产运维短板。

- [PostgreSQL会修改开源许可证吗？ · 译者评论](/pg/pg-license/#译者评论)：剖析公有云“白嫖吸血再拉分叉贴牌真开源”与原厂 SSPL 自卫反击的利益博弈，反思僵化 OSI 教条与软件自由的本末关系。
- [PostgreSQL 已主宰数据库世界 · 喜爱度](/pg/so2025-pg/#喜爱度)：用 2025 喜爱度榜单中 Valkey 首秀 64.7% 顶替 Redis、Supabase 因玩具级自建方案跌至 47.2% 的数据验证开发者口碑惩罚机制。

### 为何从 AGPL 切回 Apache，不防白嫖怎么挣钱？ {#agpl-to-apache-stand-tall}

我在许可证上踩过真坑：AGPLv3 在基础软件领域两头不讨好——既触发大厂法务红灯劝退了打算云主机自建的 OpenAI 团队，令增长退化为线性爬坡，又拦不住云架构师替客户在私有云代部署白嫖。当 AI 赋予单兵数十倍研发杠杆后，真开源的最大回报早已不是外部 PR，而是海量极端生产环境的锤炼反馈与口碑连接。软件打磨到 90 分完成态（高于 80 分公有云 RDS）就该用 Apache 2.0 当礼物白送，靠质保契约、闭源故障测试套件以及把系统推向 100 分的稀缺实战兜底“站着挣钱”。

- [从AGPL到Apache：Pigsty 协议变更的思考 · AGPLv3 的糟糕实践](/pg/pigsty-relicense/#agplv3-的糟糕实践)：复盘切换 AGPLv3 后增长失速、劝退 OpenAI 等合规敏感大客户却拦不住私有云代交付白嫖的真实教训。
- [从AGPL到Apache：Pigsty 协议变更的思考 · 商业模式：站着挣钱](/pg/pigsty-relicense/#商业模式站着挣钱)：阐明 90 分开源完成态软件免费赠送、靠质保契约与不在 AI 语料库里的百倍量级实战兜底将服务推向 100 分的盈利闭环。
- [从AGPL到Apache：Pigsty 协议变更的思考 · 那为什么不用 ELv2 / SSPL / BSL？](/pg/pigsty-relicense/#那为什么不用-elv2--sspl--bsl)：剖析 AI 放大单兵研发杠杆后，真开源的核心价值如何从“外部代码贡献”转向“极端生产场景锤炼与行业连接”。

### 公有云专有 PG 与 RDS 藏着多大的溢价与锁定陷阱？ {#cloud-rds-markup-and-lockin}

算一笔硬账：AWS 宁夏区自带 3.6TB NVMe 的 96 核 `c5d.metal` 物理机年租约 11 万～15 万元（自购同配服务器加五年托管不到 10 万），而对标的 `db.m5.24xlarge` 托管 RDS 年费高达 286.7 万元，溢价近 20 倍！Percona 复盘同样警示，云巨头正通过在 PG 外捆绑 AlloyDB 内存计费、Aurora I/O 计费等专有壳层复刻当年围猎 MongoDB 的锁定剧本，某平台迁出 DBaaS 后算上第三方支持费月支出仍砍半。况且 TDE 防不住平台窥探断供，几分钟扩容的小甜头远抵不上丧失主权与团队技术退化的代价。

- [PostgreSQL 到底有多强？ · 关于成本](/pg/pg-performence/#关于成本)：逐项核算 AWS 96 核裸金属（年租十余万）、自购物理机五年托管（不足十万）与对标 RDS（年费 286.7 万）之间近 20 倍的真实差价。
- [为什么PostgreSQL前途无量？ · vs 云数据库](/pg/pg-is-great/#vs-云数据库)：从商业信任底线（TDE 防不住平台窥探卡脖子）与规模化溢价两道硬坎，论证 Aurora 类扩容提速无法替代本地自建原生 PG。
- [PostgreSQL主宰数据库世界，而谁来吞噬PG？ · MongoDB 能告诉我们 PostgreSQL 将走向何方吗？](/pg/proprity-pg/#mongodb-能告诉我们-postgresql-将走向何方吗)：引述 Percona 对 MongoDB 转向封闭引发逃离潮的复盘，警示云巨头捆绑专有扩展与封闭管控层重演供应商锁定的剧本。
- [PostgreSQL主宰数据库世界，而谁来吞噬PG？ · 成本波动难以预测](/pg/proprity-pg/#成本波动难以预测)：拆解 AlloyDB 与 Aurora 的资源及 I/O 计费刺客案例，指出黑盒托管对合规可见性与内部工程团队敏捷度的长期侵蚀。

### PGDG 切断镜像同步引发“断供”暴露了什么供应链命门？ {#pgdg-mirror-supply-chain}

“开源无断供”只对源码成立，烧着日均 10TB 带宽的二进制仓库并无免费兜底义务。2025 年 PGDG 为缓解日均 6600 万次请求迁往海外 CDN 并关停 rsync/FTP 同步，导致国内高校与大厂镜像停更数月、CVE 安全补丁断流。讽刺的是，云大厂反馈无音讯，两三百家平时白嫖公共源的 PG 套壳“国产库”竟无一家站出来兜底，证明花架子内核 Fork 根本防不住供应链卡脖子。最终我用 Claude Code 写 HTTP 同步脚本，花两小时、几十 GB 空间就搭起国内免费 CDN 镜像——供应链里比开源更稀缺的是不推诿的交付信任。

- [从PG“断供”看软件供应链中的信任问题 · 供应链风险](/pg/pg-mirror-pigsty/#供应链风险)：辨析不可撤销的源码授权与烧带宽的二进制分发义务，还原 PGDG 迁入海外 CDN 并关闭同步通道造成的实质性制成品断供。
- [卡脖子：PGDG切断镜像站同步通道](/pg/pg-mirror-break/)：披露源站日均 10TB / 6600 万请求背景下的断流始末，阐明独立跨平台打包与自主二进制仓库比内核 Fork 更关乎供应链命门。
- [从PG“断供”看软件供应链中的信任问题 · 如何解决供应链风险？](/pg/pg-mirror-pigsty/#如何解决供应链风险)：揭露国内各大云厂商镜像长期停更失联及两三百家 PG 套壳厂商平时白嫖、遇事无一担当的生态窘境。
- [从PG“断供”看软件供应链中的信任问题 · 我行我上](/pg/pg-mirror-pigsty/#我行我上)：记录借助 AI 编写 `apt-mirror` 与 `reposync` 脚本走 HTTP 两小时建成国内免费 CDN 镜像源的破局实操。

### 龙芯跑通内核四年后，为何进官方仓库才算真正能用？ {#loong64-official-apt-repo}

龙芯早在 2022 年靠 1 KB 自旋锁补丁就能编通 PG 内核，但生产环境最怕“理论上能自己编译”——后续小版本安全更新与几百个扩展的兼容构建矩阵才是运维无底洞。此前官方原版包缺位，不仅逼一线 DBA 手工折腾依赖，更成了魔改套壳“自研库”浑水摸鱼的温床。靠当天合入的补丁、555 扩展仓库的同行实绩与寄去构建的物理主板攒够信任后，`loong64` 终于进入 Debian 与 PGDG 官方 APT 仓库，与 AMD64/ARM64 共享签名与持续构建流水线，敲两条 `apt install` 即用上干净原版，完成了从“能跑”到“能维护”的跃迁。

- [龙芯，正式进入 PostgreSQL 官方仓库 · 卡住的，不是 PostgreSQL 内核](/pg/pg-apt-loong64/#卡住的不是-postgresql-内核)：剖析从 2022 年 1 KB 自旋锁补丁跑通内核到打通几万个制品持续构建、签名与安全更新链路的四年工程鸿沟。
- [龙芯，正式进入 PostgreSQL 官方仓库 · 从“能跑”，到“能维护”](/pg/pg-apt-loong64/#从能跑到能维护)：阐明官方原版包上架如何终结魔改套壳浑水摸鱼的局面，让政企与一线 DBA 用两条标准 `apt install` 回归主流生态。
- [龙芯，正式进入 PostgreSQL 官方仓库 · 在全球开源生态里发挥影响力](/pg/pg-apt-loong64/#在全球开源生态里发挥影响力)：复盘靠高质量补丁、555 扩展仓库实绩与捐赠构建主板攒够国际社区信任，推动 GB 18030 国标与国产架构写入全球主干的正道。

## 六、全球顶会破冰、套壳祛魅与中文社区复兴 {#global-stage-and-cn-revival}

### 国内有三百款 PG 套壳库，为何对社区贡献曾被评“负分”？ {#china-shell-forks-negative-score}

盘点官方名录与全球前 188 个 PG 生态开源项目可见刺眼倒挂：中国大陆在 Core Team 与 Major Contributor 中双双挂零，主导的头部生态项目仅 `Pigsty`、`duckdb_fdw`、`zhparser` 与 `pg_roaringbitmap` 四席。反观国内三百余款“国产库”中三四成直接拿 PG 换皮魔改却自称“100% 自研”，零回馈上游还搞负优化把水搅浑，难怪资深布道者给出“负分”，连 Robert Haas 探讨亚洲领导层代表性时都只提日印而无视中国。对比遭全面制裁仍坦然靠开源 PG 挑大梁的俄罗斯，继续闭门折腾只会自己拔掉开源输液管。

- [中国对PostgreSQL的贡献约等于零吗？ · 生态开源项目](/pg/china-pg-contribution/#生态开源项目)：统计官方核心贡献者挂零与全球 188 个生态开源项目中大陆仅占 4 席的真实家底，揭示研发体量与开源回馈的严重倒挂。
- [中国对PostgreSQL的贡献约等于零吗？ · 活动与社区发展](/pg/china-pg-contribution/#活动与社区发展)：对比俄罗斯坦然倚重开源 PG 的务实路线，批判上百款套壳魔改库零回馈上游、劣币驱逐良币自断开源输液管的危机。
- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · 让PG社区参与更有包容性](/pg/pgcondev-2024/#让pg社区参与更有包容性)：记录温哥华核心峰会仅五名华人到场且亚洲多元化讨论未提中国的尴尬一幕，反思闭门造车与白嫖心态导致的国际失语。
- [PostgreSQL，三十而立 · 六、负分与旗手](/pg/pg-turns-30/#六负分与旗手)：剖析套壳换皮“负优化”产品成堆拉低中国社区评分的病根，对照一人公司开源项目 Pigsty 国际影响力反超大厂分支的错位现实。

### 本土数据库如何走出“套壳内卷、仅四家盈利”的死胡同？ {#escape-shell-involution}

国内两三百款数据库把人才资金耗在封闭造轮子上，全行业仅四家盈利且在国际圈层隐形；强推贴“100% 自研”标签的换皮分叉无异于“3C 充电宝贴纸”，最终只会伤害本土用户。济南千人 PG 高峰论坛已凝聚清醒共识：既然 PG 已赢下内核终局，就该放弃低水平内卷，像瀚高 IvorySQL 那样坦诚承认基于 PG 构建，或打造面向全球的顶级发行版。只有拿出全球同行都在用的开源硬通货走到国际现场建立信任，才能反向推动上游修复 GB18030、接纳龙芯与 Rust 扩展，赢回真正的话语权。

- [立足中国，面向全球的 PostgreSQL 发行版 · 中国在PG开源生态中并没有多少参与感](/pg/forge-a-pg-distro/#中国在pg开源生态中并没有多少参与感)：对照全球 58.2% 开发者采用率与国内两三百家仅四家盈利的内卷泥潭，提出放弃封闭造轮子、争夺全球 PG 发行版生态位的战略。
- [PostgreSQL高峰论坛：参会小记](/pg/pg-summit-2025/)：用“3C 充电宝贴纸”辛辣讽刺行政一刀切下的伪自研换皮分叉，呼吁坦诚拥抱开源 PG 连接世界。
- [复兴 PostgreSQL 中文社区 · 还是得自己上](/pg/revive-pg-cn-community/#还是得自己上)：总结拿全球通用开源基建换取上游信任，进而推动 GB18030 修复、`loong64` 入库、Rust 扩展打包与中文消息合入的实战路径。

### 无大厂光环的独立开发者，如何三年阶梯式站上全球顶会？ {#three-year-climb-to-pgconfdev}

开源世界不认资本故事与大厂头衔，积累信任的唯一通道是“把有用的事做实，然后一直在场”。打入全球内核黑客殿堂 PGConf.Dev 全靠三年拾级而上：2024 首届全场仅五名华人且零演讲者，我作为“数据库个体户”被拒稿后就在场边 Unconference 混脸熟；2025 次届与瀚高双双拿下超时即轰下台的 5 分钟闪电演讲，借《Postgres is eating the database world》破冰再用 48 页快闪直击生态三方痛点控住全场；到 2026 三十周年大会，终凭百万月下载的 `PGEXT.CLOUD` 与 Pigsty 晋级 25 分钟正式议题，走的正是 PG 三十年不炒概念靠硬交付赢得世界的老路。

- [中国厂商首次站上 PGConf.dev 主题演讲台 · 中国开发者的身影](/pg/pgconfdev-china-keynote/#中国开发者的身影)：回顾从 2024 年零演讲者的“隐形状态”到凭百万月下载扩展仓库首次以中国本土独立厂商身份入选主会场演讲的破冰历程。
- [PGCon.dev闪电演讲，硬控PG大佬5分钟](/pg/pgcondev-lightning/)：拆解用社区现象级共识破冰加 48 页蒙太奇快闪直击生态多方痛点、非英语母语照样硬控全场顶尖黑客的演讲心法。
- [PGConf.Dev 2026 今天在温哥华开幕 · 中国厂商在这个舞台上](/pg/pgcfd2026-intro/#中国厂商在这个舞台上)：梳理 Pigsty 与瀚高 IvorySQL 团队从首届台下参会、次届 5 分钟闪电演讲到第三届同步晋级 25 分钟正式议题的三年阶梯。
- [PostgreSQL，三十而立 · 结语](/pg/pg-turns-30/#结语)：将个人连续三年奔赴顶会站上讲台的经历同 PG 三十年不雇销售、不炒概念靠扎实版本赢得世界的正道相互印证。

### 国际核心社区如何拓宽荣誉体系，本土分享切中了什么？ {#community-mentorship-and-missing-link}

PostgreSQL 核心治理也在主动破壁。Jonathan Katz 曾结合 Melanie Plageman 等人洞见指出，新人适应邮件列表与打磨补丁门槛极高，因此社区借 PGConf.dev 落地结构化导师制并公开治理报告；到 2026 年 30 周年大会，社区更准备将扩展与外围开源项目正式纳入“显著贡献者”徽章体系，我也在现场同 PGDG 维护者当面敲定了龙芯构建主机赞助。当届仅有的两场中国正式议题恰好一硬一软互为表里：`Extensions for Everyone` 攻克生产级扩展打包交付底座，`The Missing Link` 则修补数万中国用户与上游核心组缺失的反馈桥梁。

- [展望 PostgreSQL 的2024 · 社区建设](/pg/pg-in-2024/#社区建设)：引述 Jonathan Katz 对邮件列表陡峭上手门槛与补丁审查难度的剖析，介绍 PGConf.dev 系统化导师计划与透明治理举措。
- [参加 PostgreSQL 30周年开发者大会 · 本文 AI 含量 0%](/pg/pgconfdev-2026/#本文-ai-含量-0)：披露社区将扩展生态维护纳入显著贡献者徽章体系的治理演进，以及线下峰会当面敲定龙芯官方构建主机的协作效率。
- [PGConf.Dev 2026 今天在温哥华开幕 · 两场来自中国的正式分享](/pg/pgcfd2026-intro/#两场来自中国的正式分享)：解读 `Extensions for Everyone`（生产级扩展打包基建）与 `The Missing Link`（双向社区治理连接）两场中国议题的互补格局。

### 中文社区为何一度空心化，真正的复兴该以谁为根？ {#revive-cn-community-user-root}

全球 PG 蒸蒸日上之际中文社区却陷入沉寂，病根在于套壳运动分流了公共建设力量，又把大会办成了厂商轮番吹牛打广告的聚餐会。借用 Peter Zaitsev 的社区三圈层视角，脱离真实用户空转的厂商行会注定散摊子，覆盖大陆、港澳台与新马的“泛中文世界用户组”才是真正的根——围绕开箱即用的发行版，老实配齐同步中文手册、国内镜像源、简繁本地化与无广告门户。如今一人率领 Agent 舰队即可跑通全史汉化与 600 扩展跨平台打包；当工程能力不再是瓶颈，摒弃收赞助办展销会的算计，纯粹让人用好 PG 的“愿力”才是唯一稀缺品。

- [复兴 PostgreSQL 中文社区 · 复兴隐含着没落](/pg/revive-pg-cn-community/#复兴隐含着没落)：直指套壳换皮分化公共力量与“用户大会沦为厂商广告聚餐会”两大病灶如何掏空了中文社区。
- [复兴 PostgreSQL 中文社区 · 社区的根，在用户](/pg/revive-pg-cn-community/#社区的根在用户)：引入 Peter Zaitsev 三圈层模型确立泛中文世界用户组定位，列出发行版、同步文档、镜像源与简繁汉化的朴素交付清单。
- [复兴 PostgreSQL 中文社区 · 能力不再是瓶颈，愿力才是](/pg/revive-pg-cn-community/#能力不再是瓶颈愿力才是)：对比昔日团队数年愚公移山与如今单兵指挥 Agent 舰队的产能跃迁，点明纯粹热爱与愿力对功利展销模式的替代。
- [一天翻译完 PG 生态三大件文档 · 后面要做什么？](/pg/pg-translate/#后面要做什么)：勾勒以自动化多语种文档资讯流为基座、以高价值开源项目为凝聚核，单枪匹马构建本土社区闭环的蓝图。

### AI 随手可译的时代，为何要把六万条内核报错彻底汉化？ {#why-native-nls-localization}

半夜线上满屏报错分秒必争，母语一目十行的阅读速度绝非切出去问 AI 可比，半吊子汉化更毁开箱印象。翻查 IvorySQL、PolarDB、TBase、昆仑、openHalo 等一众国产衍生库的 `zh_CN.po`，竟全原封躺着 2001 年“臭虫报告至”与“内存溢出”的错译，二十五年无一家国产厂商回馈上游——趁这些谬误被大模型语料焊死前清洗源头刻不容缓。我用七天按“钉死术语表与助动词规约、跨 28 组件 6 版本对齐审校”流水线将 67,487 条消息 100% 合入上游，并逐条订正两岸差异术语（如記憶體、伺服器、交易、執行緒），同步交付地道繁体版。

- [为什么要做 PostgreSQL 汉化？ · AI 都这么强了，为什么还要汉化？](/pg/pg-zh-tw/#ai-都这么强了为什么还要汉化)：从半夜故障现场分秒必争的母语排障速度与默认中文系统的开箱尊严切入，阐明 28 个组件 100% 满配汉化的必要性。
- [PostgreSQL 中文版来了 · 「国产」到底产了什么](/pg/pg-nls/#国产到底产了什么)：晒出各大国产 PG 衍生库原封保留 2001 年“臭虫报告至”错译且上游贡献挂零的铁证，扯下只套壳不顾基础体验的遮羞布。
- [PostgreSQL 中文版来了 · 这七天是怎么过的](/pg/pg-nls/#这七天是怎么过的)：详解先立术语与助动词规矩、跨 6 个版本 28 个组件对齐清洗再人工逐条审校，七天攻克 67,487 条消息并零误差合入上游的全流程。
- [为什么要做 PostgreSQL 汉化？ · 繁体中文，不是简繁转换](/pg/pg-zh-tw/#繁体中文不是简繁转换)：对比两岸截然不同的计算机术语习惯，说明为何必须弃用机械词典转换、基于简体底稿逐条订正出地道台湾技术繁体。
- [PostgreSQL 中文版来了 · 最后](/pg/pg-nls/#最后)：论述上游 `.po` 错译顺工单博客流入大模型训练集的语料污染链条，点明源头清洗跑赢伪共识固化的紧迫性。

### AI 流水线如何终结文档断档，补齐存量与全史 508 版？ {#ai-pipeline-full-version-docs}

母语参考手册能带来两三倍查阅提速，但上千页大版本靠志愿者业余接力动辄磨一两年，终究在 PG 15 后断档，Patroni、PgBouncer、pgBackRest 三大件中文文档更是长期空白。如今先立对标国标的权威术语表（如统一 token 为“词元”）锁死跨版同句强对齐基线，用临期订阅 Token 批量转译再经专家通读纠偏，一天就能交付三大件与活跃版本手册。顾及国内大批未升级的 PG 10～13 存量系统，不仅已 EOL 老版本悉数补齐，借饱和式 Token 投入与 Oink 1.5 工具链，连横跨 31 个大版本、508 个小版本的全史手册也已发起汉化总攻。

- [一天翻译完 PG 生态三大件文档 · 中文文档，到底重不重要？](/pg/pg-translate/#中文文档到底重不重要)：论证母语两三倍查阅提速的认知刚需，剖析志愿者“用爱发电”导致官方手册滞后三年及三大生产组件文档断档的症结。
- [一天翻译完 PG 生态三大件文档 · AI 改变了什么？](/pg/pg-translate/#ai-改变了什么)：拆解“消耗即将过期订阅 Token 批量转译 + 领域专家通读纠偏”如何把数十人协作数月的苦役压缩为近零边际成本的单人一日工程。
- [PG 中文文档发布：11 个大版本，一个不落 · 这个坑为什么空着](/pg/pgsql-cc-online/#这个坑为什么空着)：说明带语境例外清单的多模型核定术语表与 11 个大版本同句强对齐机制，如何实现上游小版本发布即刻滚动跟进。
- [PG 中文文档发布：11 个大版本，一个不落 · 先说这份文档](/pg/pgsql-cc-online/#先说这份文档)：解释为何不局限于维护期内的五个新版，而要专门耗费算力补齐 PG 10～13 等已 EOL 存量版本以服务一线遗留系统。
- [PG 五大版本中文文档已就绪，欢迎查阅！ · 关于这份文档](/pg/pgdoc-cn/#关于这份文档)：记录确立国标数据库术语基线、以 PG 18 精翻本为底本借 Codex 一天交付 PG 14～18 全生命周期文档的工程方法。
- [渡劫期的 PostgreSQL 生态大更新 · 1. 让 PG 说一口地道中国话：内核与 508 个版本文档全史汉化](/pg/eco-update-202611/#1-让-pg-说一口地道中国话内核与-508-个版本文档全史汉化)：展示饱和式 Token 投入下 PG 15–19 内核 100% 汉化、31 个大版本 508 个小版本全史文档总攻及 Oink、Barn、Crib 配套利器。

### 无广告同构门户如何打破“二手博客喂坏模型”死循环？ {#clean-cn-portal-ecosystem}

受语言与网络阻隔，国内许多老手从未逛过英文官网，只能搜残次二手博客或问大模型；而大模型的中文语料恰恰喂自这批二手博客，陷入越传越歪的死循环。破局必须靠干净无“牛皮癣”广告的一手信源矩阵：`pgsql.cc` 与官网改域名直达映射并覆盖 6.3 至 20devel 共 31 版检索；同构复刻官网的 `pg.center` 汉化了 130 余个治理页面、梳理 31 版对象演进百科，并在侧边栏一站式打通高可用、连接池与备份生态且源码全开源；配合收录 2,600+ 扩展双语文档与 600 个二进制包的 `pgext.cloud`，彻底夯实了中文知识底座。

- [PG 中文文档发布：11 个大版本，一个不落 · 最后](/pg/pgsql-cc-online/#最后)：剖析二手博客污染大模型语料的恶性循环，阐明 `pgsql.cc` 零广告、清晰非隶属声明及与官网 URL 一一映射的基建价值。
- [PG 五大版本中文文档已就绪，欢迎查阅！ · 不只是翻译](/pg/pgdoc-cn/#不只是翻译)：介绍文档源码全开源、扩展收录第三方内核与周边工具目录，以及沉淀高质量双语结构化语料反哺专业知识库的运营逻辑。
- [PostgreSQL 官网中文版：pg.center · 为什么要做这件事？](/pg/pg-center/#为什么要做这件事)：直面旧社区站点失修与国内开发者远离英文官网的现状，确立零英文零翻墙门槛同构复刻权威中枢的初衷。
- [PostgreSQL 官网中文版：pg.center · 做了什么？](/pg/pg-center/#做了什么)：盘点 130 余个官网页面汉化及侧边栏一站式打通 Patroni、PgBouncer、pgBackRest、pg_exporter 与 Pigsty 生产生态的版图。
- [为什么要做 PostgreSQL 汉化？ · 顺便说说其他几个站点](/pg/pg-zh-tw/#顺便说说其他几个站点)：串联 `pgsql.cc`（31 大版本手册）、`pg.center`（31 版本对象演进百科）与 `pgext.cloud`（2600+ 扩展双语目录与 600 二进制包）三座门户矩阵。

### 一天精译 30 本专著并安全榨干问题工具链靠什么章法？ {#translate-30-books-and-isolation}

工业级精译与随手机翻的分水岭，在于十年校准的多语种专业术语底座（钉死 `must`/`shall`/`may` 行文规约）加顶级模型“三审三校”流水线，一天即可消化 30 册专著并绕开英语直译俄语 PGPro 讲义与法语 Dalibo 教案——精译一本书烧三四百元 Token，社区集中共享远胜个人零散机翻。公益基建严守不碰商业出版物、只取开放协议或原厂非商业授权并致谢前人译本（如熊灿灿老师）的底线；而对爆出私传仓库隐患的工具链（如 ZCode），将其移出私密代码、专喂 28 年公开历史手册由 Codex 轮番监工核验，便能零泄密榨干套餐余值。

- [工业流水线：一天翻译完 30 本 PG 书籍 · 地表最懂 PG 的翻译底座](/pg/translate-30-books/#地表最懂-pg-的翻译底座)：拆解跨八国语言校准的专业术语表、助动词行文规约与“三审三校”加 Oink 自动化建站如何支撑日产 30 册的高水准吞吐。
- [工业流水线：一天翻译完 30 本 PG 书籍 · 去法语俄语里淘金](/pg/translate-30-books/#去法语俄语里淘金)：展示绕开英语直译俄语 PGPro 讲义与法语 Dalibo 培训教材的跨语种优势，算清每本三四百元 Token 集中精译的社会算力经济账。
- [工业流水线：一天翻译完 30 本 PG 书籍 · 版权规矩与中文社区复兴](/pg/translate-30-books/#版权规矩与中文社区复兴)：确立不接商单、不碰商业出版物、严选 CC BY 4.0 或原厂授权、致谢前人译本并友链成熟译著的公益基建底线。
- [PostgreSQL 19 Beta 4 发布：特性大砍 · 题外话：GLM 的下场](/pg/pg19b4-release/#题外话glm-的下场)：分享对有偷传前科工具链实施职责隔离——剥离私密代码、专喂 28 年公开历史手册并派 Codex 多轮监工把关的安全压榨策略。
