---
title: 湖仓 Catalog 税、数仓终局与“本体论”祛魅
linkTitle: 湖仓与本体论祛魅
description: Iceberg/Catalog 复杂度税、Palantir“本体论”包装话术拆穿与现代数仓收敛终局。
weight: 90
icon: fa-solid fa-cubes
---

独立湖仓 Catalog 只是按次收租的 PostgreSQL 表，Palantir 吹嘘的“本体论”也不过是套上哲学外衣的数据建模与驻场咨询。随着 PG 与 DuckDB 融合吞并列存分析，重型大数据栈正沦为期货死人。

## 一、湖仓 Catalog 税与开放数据栈标准 {#lakehouse-catalog-and-standards}

### 独立目录为何沦为收租层，且自带权限裂缝？ {#catalog-rent-and-security-gap}

独立 Iceberg REST Catalog 本质就是一张套壳按次收租的 PostgreSQL 表。Iceberg 提交的核心仅是单行 CAS 更新指针，S3 支持条件写后外部目录必要性已大减；更致命的是控制面不在数据路径上，签发短期 STS 凭证后客户端直读整份 Parquet，行列权限失效且即时撤权只能干等过期。

- [Catalog Bullshit：把数据库拆开，再租给你一张 PostgreSQL 表 · Catalog 的本职：替对象存储保管一个指针](/db/catalog-bullshit/#catalog-的本职替对象存储保管一个指针)
- [Catalog Bullshit：把数据库拆开，再租给你一张 PostgreSQL 表 · 控制面根本不在数据路径上](/db/catalog-bullshit/#控制面根本不在数据路径上)

### 元数据放回关系库，为何单机四级阶梯就够用？ {#metadata-in-db-and-pg-duckdb}

大数据折腾二十年，只是把数据库拆碎在 S3 上重造残缺的 System R。像 DuckLake 或 `pg_lake` 那样将元数据放回 SQL 表、免撒满地 JSON 清单，高频小写入直接内联即可提速百倍并白送跨表 ACID。99% 企业无需伺候 Spark，沿 PG 与 DuckDB 结合 S3 的四级阶梯演进，单机比八节点集群更快。

- [Catalog Bullshit：把数据库拆开，再租给你一张 PostgreSQL 表 · Catalog 本来就该是一张表](/db/catalog-bullshit/#catalog-本来就该是一张表)
- [Catalog Bullshit：把数据库拆开，再租给你一张 PostgreSQL 表 · DuckDB 穿着 PostgreSQL 的马甲](/db/catalog-bullshit/#duckdb-穿着-postgresql-的马甲)

### 开放数据栈收敛向哪三项，PG 与列存边界在哪？ {#open-data-standards-and-f3}

如 Paul Copplestone 归纳，无锁定数据底座正围绕对象存储收敛为三大开放标准：PG 管事务、OTel 管遥测、Iceberg 管分析。中立治理的 PG 足以通吃向量与多模，但重度监控归 VictoriaMetrics、超大规模分析归专用列存；Andy Pavlo 更点破九成四新 Parquet 仍困于旧版，唯有如 F3 随列内嵌解码器才能打破多语言解析割裂。

- [开放数据标准：Postgres，OTel，与Iceberg · 开源的三个信条](/db/open-data-standard/#开源的三个信条)
- [开放数据标准：Postgres，OTel，与Iceberg · 三大开放数据标准](/db/open-data-standard/#三大开放数据标准)
- [开放数据标准：Postgres，OTel，与Iceberg · 关于 Postgres](/db/open-data-standard/#关于-postgres)
- [Andy Pavlo：2025 数据库世界年度总结 · Andy 的看法](/db/db-in-2025/#andy-的看法-3)

## 二、Palantir“本体论”包装话术拆解 {#palantir-ontology-bullshit}

### Palantir 吹嘘的“本体论”到底是什么？ {#what-is-palantir-ontology}

拆开白皮书便知底牌：Object 是表、Property 是列、Link 是外键、Action 是存储过程，几十行 PG SQL 即可等价实现。其美国专利（US7962495B2）明写 Ontology 就是数据库 Schema；纽约警局解约时它更拒交标准格式，把开放“造桥”概念异化成锁客“高墙”，论本体论实践远不如多模 PG。

- [Palantir 的“本体论”骗局 · 二、罗塞塔石碑](/db/ontology-bullshit/#二罗塞塔石碑)
- [一场辩论之后，认真聊聊“本体论” · 一、事实：Ontology 就是数据建模](/db/ontology-again/#一事实ontology-就是数据建模)
- [一场辩论之后，认真聊聊“本体论” · 三、真正的本体论：数据库才是最接近的实践](/db/ontology-again/#三真正的本体论数据库才是最接近的实践)

### 只是数据建模，它凭什么撑起四千亿美元市值？ {#palantir-fde-and-radar}

正像二战英军编造“胡萝卜夜视强”掩护雷达，Ontology 只是掩护华盛顿政商关系与驻场人海的幌子。其 54% 收入源于政府，In-Q-Tel 背书、涉密牌照与政治游说才是拿单引擎；大批驻场工程师（FDE）手写 ETL 干集成苦活，靠将人力塞进研发营销费用才粉饰出百倍 SaaS 估值。

- [一场辩论之后，认真聊聊“本体论” · 二、动机：胡萝卜与雷达](/db/ontology-again/#二动机胡萝卜与雷达)
- [Palantir 的“本体论”骗局 · 四、哲学名词的认知税](/db/ontology-bullshit/#四哲学名词的认知税)
- [Palantir 的“本体论”骗局 · 六、挣了钱自有大儒辩经](/db/ontology-bullshit/#六挣了钱自有大儒辩经)
- [Palantir 的“本体论”骗局 · 七、披着 SaaS 皮的咨询公司](/db/ontology-bullshit/#七披着-saas-皮的咨询公司)

### 谁在买天价本体论，国内跟风为何必蹈中台覆辙？ {#ontology-cargo-cult}

买家多是公款免责型的军方与巨企，业务锁进专有黑盒后便被收割出 134% 净留存率。国内厂商既无国防牌照也无天价大单，跟风炒作纯属搭竹塔等飞机的“货物崇拜”——它本质就是披着哲学皮的“美国版数据中台”，注定重演五年覆灭宿命，技术圈亟需扫除玄学黑话的“概念清洁工”。

- [Palantir 的“本体论”骗局 · 八、Ontology 买家画像](/db/ontology-bullshit/#八ontology-买家画像)
- [一场辩论之后，认真聊聊“本体论” · 四、竹制跑道上的等待](/db/ontology-again/#四竹制跑道上的等待)
- [一场辩论之后，认真聊聊“本体论” · 五、概念清洁工](/db/ontology-again/#五概念清洁工)

## 三、鸭子范式、数仓终局与开源反垄断 {#duck-paradigm-and-warehouse-endgame}

### 鸭子范式凭什么颠覆重型云数仓与湖仓目录栈？ {#duck-paradigm-pg-s3-duckdb}

列存引擎早已沦为同质化大路货，如 Andy Pavlo 剖析 Databricks 砸 20 亿美元买 Tabular 所示，巨头争夺的是表格式目录控制权；但生产分析查询中位数仅扫 100MB，单机绰绰有余。AWS 收购 DuckLabs 押注的“鸭子范式”（关系库管元数据、对象存储放文件、嵌入式引擎无状态计算）直接端掉繁琐目录栈，用 Pigsty 即可零成本全开源平替。

- [AWS 收购 DuckDB：鸭子飞进亚马逊雨林 · 鸭子范式：元数据进 PG，数据放 S3](/db/aws-get-duckdb/#鸭子范式元数据进-pg数据放-s3)
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法：Databricks 与 Snowflake](/db/pavlo-2024-review/#andy-的看法databricks-与-snowflake)
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法：DuckDB 与 PostgreSQL](/db/pavlo-2024-review/#andy-的看法duckdb-与-postgresql)

### 嵌入式双雄如何突围，兼容 MySQL 为何徒劳？ {#duckdb-pg-fusion-and-embedded}

在 PG 稳坐服务端王座的时代，唯有零依赖进程内的 SQLite 与 DuckDB 能绕开运维链路侧翼突围：如 Matt Blewitt 梳理，SQLite 掀起本地优先复兴，DuckDB 通吃文件称霸单机分析（仅超大实时写入让位 ClickHouse）。DuckDB 全面对齐 PG 生态，而强塞 MySQL 语法兼容被拒，证明替退潮生态续命徒劳无功。

- [DuckDB 开发者大会四连击：扩展，加密，存储过程，边缘分析 · 老冯点评](/db/duckcon-2026/#老冯点评)
- [七周七数据库（2025年） · 本地优先数据库](/db/7-week-7-db/#本地优先数据库)

### 传统数仓为何沦为期货死人，巨头并购藏何杀招？ {#big-data-dead-and-tam-veto}

单节点 PG 打通列存分析后即可一库包办九成九企业的事务与数仓需求，直接裁撤繁琐同步链路与大数据团队，传统数仓已成“期货死人”。如 Andy Pavlo 盘点，Databricks 砸 10 亿美元买 Neon 全面合围 PG；Snowflake 豪掷 2.5 亿美元现金收购 CrunchyData，更借核心元老 Tom Lane 对表访问方法接口（TAM）的一票否决权精准牵制对手。

- [别争了，AI时代数据库已经尘埃落定 · 大数据期货死人](/db/db-for-ai/#大数据期货死人)
- [别争了，AI时代数据库已经尘埃落定 · PG 内核的否决权](/db/db-for-ai/#pg-内核的否决权)
- [Andy Pavlo：2025 数据库世界年度总结 · PostgreSQL 持续称霸](/db/db-in-2025/#postgresql-持续称霸)

### 巨头疯抢稀缺内核人才，独立开源发行版如何破局？ {#open-source-distro-anti-monopoly}

全球顶尖独立 PG 团队屈指可数，巨头天价并购本质是争抢稀缺人才的“抢椅子游戏”。面对云寡头借闭源管控筑起的新垄断，不拿风投、独立盈利的“一人公司”开源发行版（如 Pigsty）根本无法被收编：将裸机高可用、连接池、PITR 与数百插件打磨成免费利器，每年直接抹平上亿云 RDS 账单。

- [别争了，AI时代数据库已经尘埃落定 · 人才是最关键的因素](/db/db-for-ai/#人才是最关键的因素)
- [专栏：数据库老司机 · PG 生态篇](/db/guru/#pg-生态篇)
