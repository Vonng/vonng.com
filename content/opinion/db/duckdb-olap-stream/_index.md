---
title: 小数据复兴、DuckDB 合体与时序流计算
linkTitle: DuckDB 与时序流计算
description: 笔记本级小数据革命、DuckDB 接入 PG 内核、TimescaleDB 超表边界与连续视图流处理。
weight: 100
icon: fa-solid fa-bolt
---

生产分析查询中位数仅百兆，单机列存早已揭穿十年分布式大数据的错付。在 PG 内核中挂载 DuckDB、TimescaleDB 超表与连续视图扩展，单库即可免 ETL 通吃分析、时序与实时流计算。

## 一、小数据复兴与分布式 HTAP 祛魅 {#small-data-and-htap}

### 为什么说行业在分布式大数据上白白错付了十年？ {#small-data-lost-decade}

真实企业的分析数据远没厂商吹得那么大。Hannes Mühleisen 援引 Snowflake 生产统计指出查询扫描中位数仅 100MB、99.9 分位不足 300GB：他用 2012 款 16GB 笔记本靠 DuckDB 外存溢出便跑完了 60 亿行 TPC-H SF1000，换 M3 Max 后均耗时更从 218 秒骤降至 12 秒，证明单机列存本可省去十年 Hadoop 弯路。

- [小数据的失落十年：分布式分析的错付 · 基准测试](/db/smalldata-decade/#基准测试)
- [小数据的失落十年：分布式分析的错付 · 讨论](/db/smalldata-decade/#讨论)
- [小数据的失落十年：分布式分析的错付 · 2023 年的改进](/db/smalldata-decade/#2023-年的改进)

### 为何分布式 HTAP 成了无人鼓掌的演出？ {#htap-knork-illusion}

行存点改与列存批扫物理互斥，强捏的分布式 HTAP 只是把“交易库加同步加分析库”捆进一个盒子改叫“刀叉合一”。如瑞典马工剖析，企业交易与数仓团队隔着部门墙，微服务更是多库分立：跨越速运标杆实为 Flink 灌宽表纯跑 OLAP，作业帮样板核心交易仍留 MySQL，还得堆内存防 Full GC 伺候 OMS 同步链路。

- [HTAP数据库，一场无人鼓掌的演出 · 跨越速运](/db/htap-no-applause/#跨越速运)
- [HTAP数据库，一场无人鼓掌的演出 · 作业帮](/db/htap-no-applause/#作业帮)

### 国产分布式库热炒 HTAP 暴露了什么自救焦虑？ {#htap-efficiency-inversion}

扎堆翻炒 HTAP，本质是单机 Scale-Up 证伪分布式交易且大厂不付费后的自救。硬账对比极为荒诞：笔记本用 DuckDB 6 分钟跑完 TPC-H 1000 仓，某国产分布式 HTAP 用 92 核集群跑 50 仓竟只追平 8 核笔记本跑 300 仓——十倍算力干六分之一的活，远不如 PG 加 DuckDB 极简实在。

- [小数据的失落十年：分布式分析的错付 · 老冯评论](/db/smalldata-decade/#老冯评论)
- [HTAP数据库，一场无人鼓掌的演出 · 参考资料](/db/htap-no-applause/#参考资料)
- [分布式数据库是不是伪需求？ · 迷茫下的挣扎](/db/distributive-bullshit/#迷茫下的挣扎)

## 二、PG 与 DuckDB 内核合体及微内核巧思 {#pg-duckdb-fusion}

### 为何 PG 融合列存引擎能补短板并终结双轨制？ {#pg-kiss-duckdb}

PG 与 DuckDB 单机合体一举填平列存短板，宣告“关系库 + 数仓 + ETL”双轨制终结。ClickBench 上原生 PG（x47）曾落后十余倍，接入同源解析器的 DuckDB（x3.2）后直抵塔尖；PG 的高并发 MVCC、权限与高可用恰补齐嵌入式引擎的企业骨架，从 `duckdb_fdw` 到 `pg_duckdb`、`pg_mooncake`，免 ETL 保 ACID 的融合彻底粉碎了套壳迷梦。

- [数据库火星撞地球：当PG爱上DuckDB · 蹭热点引出的好话题](/db/pg-kiss-duckdb/#蹭热点引出的好话题)
- [数据库火星撞地球：当PG爱上DuckDB · 取长补短的黄金组合](/db/pg-kiss-duckdb/#取长补短的黄金组合)
- [数据库火星撞地球：当PG爱上DuckDB · 为什么是 DuckDB+PG？](/db/pg-kiss-duckdb/#为什么是-duckdbpg)
- [数据库火星撞地球：当PG爱上DuckDB · 统一 OLTP 与 OLAP 的梦想](/db/pg-kiss-duckdb/#统一-oltp-与-olap-的梦想)
- [PostgreSQL 正在吞噬数据库世界 · OLAP 领域迎来踢馆者](/pg/pg-eat-db-world/#olap-领域迎来踢馆者)
- [谁整合好DuckDB，谁赢得OLAP世界 · DuckDB的短板与其中的机遇](/pg/pg-duckdb/#duckdb的短板与其中的机遇)
- [duckdb_fdw v1.0.0来了，第13届 PostgreSQL 中国技术大会见 · 引用链接](/pg/duckdb-fdw-1-0/#引用链接)
- [第七届PG生态大会：一些感想 · 扩展很重要，但很多人没意识到](/pg/pgconf-china-7th/#扩展很重要但很多人没意识到)

### 微内核与块级加密如何让嵌入式列存既轻又全能？ {#duckcon-kernel-and-edge}

DuckDB 兼顾零依赖轻量与全能靠四招巧思：将云存储等拆入按需加载的稳定 C API 扩展；在 256KB 块级“先压缩后 AES-GCM 加密”保裁剪率，并动态注入硬件加速 OpenSSL；DuckPL 存储过程用堆上显式栈流式挂起响应 `LIMIT`，直调底层执行器提速 30 倍；Gizmo Edge 借定向广播与 Arrow 零拷贝联动异构边缘节点秒扫万亿行。

- [DuckDB 开发者大会四连击：扩展，加密，存储过程，边缘分析 · 未来方向](/db/duckcon-2026/#未来方向)
- [DuckDB 开发者大会四连击：扩展，加密，存储过程，边缘分析 · 块级加密](/db/duckcon-2026/#块级加密)
- [DuckDB 开发者大会四连击：扩展，加密，存储过程，边缘分析 · 执行引擎设计](/db/duckcon-2026/#执行引擎设计)
- [DuckDB 开发者大会四连击：扩展，加密，存储过程，边缘分析 · 定向广播（Targeted Broadcast）](/db/duckcon-2026/#定向广播targeted-broadcast)

## 三、TimescaleDB 时序超表与库内流计算 {#timeseries-and-stream}

### 时序超表为何坚持宽表，且十亿行写入快二十倍？ {#timescaledb-wide-table-and-hypertable}

专用时序库窄表易引发标签叉积爆炸，TimescaleDB 则用关系宽表存同刻多维指标并关联静态维表。原生 PG 超五千万行后索引溢出内存致写入跌至五千行/秒；超表自动切分物理 Chunk 锁住热索引常驻内存，十亿行仍稳居 11 万行/秒（快 20 倍），过期数据直接 `drop_chunks` 免 `VACUUM`。

- [TimescaleDB 快速上手 · 宽表模型](/pg/timescale-install/#宽表模型)
- [TimescaleDB 快速上手 · 更高的写入速率](/pg/timescale-install/#更高的写入速率)

### 时序超表适用边界在哪，查询为何易爆共享内存锁？ {#timescaledb-boundaries-and-locks}

寄生 PG 虽免去双栈运维，但极简 KV 点查、高度稀疏无模式、极致冷压缩或离线批处理并非其强项。生产上线更有必调暗雷：跨周期查询需同时锁住所有涉及的 Chunk 子表与索引，默认 `max_locks_per_transaction = 64` 极易耗尽并报 `out of shared memory`，必须按 `2 * num_chunks` 预调重启。

- [TimescaleDB 快速上手 · 何时不使用TimescaleDB？](/pg/timescale-install/#何时不使用timescaledb)
- [TimescaleDB 快速上手 · 调参](/pg/timescale-install/#调参)

### 如何免搭重型流引擎，在关系库内跑实时流式聚合？ {#pipelinedb-continuous-views}

面对高频指标与 PV 实时统计，无需复杂窗口编排时根本不必架设 Kafka 加 Flink。PipelineDB 扩展将无界流抽象为 `FOREIGN TABLE` 并定义连续视图：数据经 `COPY` 持续灌入，内存实时完成计数与 P99 分位增量聚合，磁盘仅落结果免存明细；启用时须同步调大 `max_worker_processes` 保障后台进程配额。

- [PipelineDB快速上手 · PipelineDB使用样例 —— 维基PV数据](/pg/pipeline-intro/#pipelinedb使用样例--维基pv数据)
- [PipelineDB快速上手 · PipelineDB安装与配置](/pg/pipeline-intro/#pipelinedb安装与配置)
