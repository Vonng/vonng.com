---
title: 黄金监控指标、PG Load 水位与慢查询微分治理
linkTitle: 黄金指标与慢查询
description: 四大黄金信号、PG Load 负载曲线、压测基线标定与 pg_stat_statements 微分定位。
weight: 220
icon: fa-solid fa-gauge-high
---

三千个裸监控指标堆上大盘只会制造噪音，单看机器 CPU 或笼统 QPS 更抓不住数据库锁争用与连接饥饿。唯有构建归一化的 `PG Load` 饱和度标尺，并对 `pg_stat_statements` 累积计数器做时序微分，才能在毫秒级红线内精准剿灭慢查询。

## 一、黄金监控指标、PG Load 水位与压测基线 {#metrics-load-and-benchmark}

### 三千指标如何做减法，为何 QPS 管不住水位？ {#golden-metrics-hierarchy}

单实例动辄暴露三千多个指标，必须将事后验尸的冷指标与十项盯盘黄金信号严格分离。错误与排队告警优先级最高，但平时恒零只能事后“报丧”；QPS 把 10 微秒点查与 10 秒大查询等权记作 1 次，跨库与纵向对比皆失真；RT 适合划定“OLTP 禁超 1ms”质量红线，唯有归一化到 `0%～100%` 的饱和度指标才能统领瞬时告警与长期扩容。

- [黄金监控指标：错误延迟吞吐饱和 · 核心指标](/pg/golden-metrics/#核心指标)
- [黄金监控指标：错误延迟吞吐饱和 · 错误指标](/pg/golden-metrics/#错误指标)
- [黄金监控指标：错误延迟吞吐饱和 · 流量指标](/pg/golden-metrics/#流量指标)
- [黄金监控指标：错误延迟吞吐饱和 · 饱和度指标](/pg/golden-metrics/#饱和度指标)

### 如何构造跨机型归一化的 PG Load 指标？ {#pg-load-kpi}

主机 CPU 与磁盘指标遇库内锁争用或连接耗尽即失灵。对单位时间内全部后端活跃总秒数求导再除以 CPU 核数，即得数据库本层饱和度 `PG Load`——数学上恒等于 \(\text{TPS} \times \text{RT} / \text{核数}\)。生产上须对 Pgbouncer 单调递增的 `total_xact_time` 求导，把 `Idle in Transaction` 一并罚入水位：慢查询堵池时它会瞬间冲破 `70%` 红线，15 分钟均值达 `30%～50%` 即可指导扩容。

- [PostgreSQL的KPI · 0x02 常用评估指标的问题](/pg/pg-load/#0x02-常用评估指标的问题)
- [PostgreSQL的KPI · 数据库负载（PG Load）](/pg/pg-load/#数据库负载pg-load)
- [PostgreSQL的KPI · 如何获取活跃时长](/pg/pg-load/#如何获取活跃时长)
- [PostgreSQL的KPI · 0x05 PG Load的实际效果](/pg/pg-load/#0x05-pg-load的实际效果)

### 内置统计视图有何滞后，新一代查询遥测怎么做？ {#stats-collector-and-telemetry}

读监控须懂内核语义：PG 缓冲命中率不含 OS Page Cache，检查点后首次改页会触发 `full_page_writes` 整页写洪峰，且 `pg_stat_*` 存在闲置上报、`500ms` 节流与事务内快照冻结三重滞后（长事务轮询须调 `pg_stat_clear_snapshot()`）。要在低于 1% 损耗下抓逐条 SQL 分位数延迟，可用 `pg_stat_ch` 经无背压共享内存环形队列（满则丢弃、p99 仅 5μs）旁路流式写入 ClickHouse。

- [PostgreSQL监控系统概览 · 监控系统的指标](/pg/monitoring-overview/#监控系统的指标)
- [PostgreSQL监控系统概览 · 检查点与 WAL](/pg/monitoring-overview/#检查点与-wal)
- [PostgreSQL监控系统概览 · 统计收集器](/pg/monitoring-overview/#统计收集器)
- [504 个扩展，PG 生态的天花板在哪？ · 7. pg_stat_ch: ClickHouse 官方出品的 PostgreSQL 查询遥测](/pg/extension-504/#7-pg_stat_ch-clickhouse-官方出品的-postgresql-查询遥测)

### 日志怎么配，如何免搭 ELK 用 SQL 查？ {#csvlog-and-file-fdw}

生产库切忌输出纯文本日志，应设 `log_destination = 'csvlog'` 落盘 23 列结构化记录，并全开检查点、锁等待、DDL、慢查询与 `track_io_timing`；同机采集器须按行首时间戳正则合并跨行 SQL 并限死单核 CPU 防反噬算力。其实无需重型 ELK：将日志配为按星期轮转的 `postgresql-%a.log`，用 `file_fdw` 映射为 7 张分区外部表，写标准 SQL 即可零搬运聚合慢查询与报错。

- [PG服务器日志常规配置 · 日志相关配置项](/pg/logging/#日志相关配置项)
- [PG服务器日志常规配置 · 日志收集](/pg/logging/#日志收集)
- [PG服务器日志常规配置 · 映射日志](/pg/logging/#映射日志)

### CPU 不高为何负载爆表，怎样读懂主机指标？ {#linux-cli-diagnostics}

Linux 的 Load Average 统计的是运行态（`R`）与不可中断睡眠态（`D`，多卡在磁盘硬件 I/O）的平均任务数而非 CPU 使用率，飙高时须联看 `D` 态进程、`%wa` 与虚拟化偷取 `%st`。同理，内核会把空闲内存全借作可回收的 `buffers/cache` 加速 PG，只要 Swap 换页 `si/so` 为零即内存充裕；看盘须敲 `iostat -dxk` 穿透请求合并，直击队列 `avgqu-sz` 与读写延迟 `await`。

- [Linux 常用统计 CLI 工具 · 摘要部分](/pg/unix-tool/#摘要部分)
- [Linux 常用统计 CLI 工具 · 输出样例](/pg/unix-tool/#输出样例)
- [Linux 常用统计 CLI 工具 · 输出说明](/pg/unix-tool/#输出说明)

### 存储与异构库 OLTP 压测有哪些口径与红线？ {#fio-and-sysbench-benchmark}

验收存储必须对齐 PG 物理粒度：FIO 加 `-direct=1` 绕过缓存，重点测 8KB 随机读写 IOPS 与模拟 WAL 的 1MB 顺序带宽；严禁对生产裸块设备跑写压测以免覆写超级块毁盘，XFS 挂载必加 `noatime` 消除读致写放大。与 MySQL 横向对比 OLTP 时，`pgbench` 模型偏私有，应编译 `--with-pgsql` 驱动跑标准 `sysbench` 的 `oltp_read_write.lua` 公平对比 TPS 与 P95 延迟。

- [使用FIO测试磁盘性能](/pg/fio/)
- [使用sysbench测试PostgreSQL性能 · 压测](/pg/sysbench/#压测)

## 二、宏观查询优化、慢查询闭环与运维自动化 {#query-tuning-and-automation}

### 裸查统计视图有何盲区，怎样揪出刷日志真凶？ {#pgss-blindspots-and-wal}

`pg_stat_statements`（PGSS）不记录运行中卡死与超时报错的语句，内置均值列无时间窗参考价值，必须高频采集累积值做时序差分。抓算力杀手应对 `total_exec_time` 求导算无量纲“每秒执行时长（`s/s`）”；若无高频写入却爆复制延迟，对 `wal_bytes` 与 `wal_fpi` 求导即可揪出两类隐蔽元凶：大改后 `ROLLBACK` 的废事务，以及只读大查询首扫改提示位（Hint Bit）引爆的全页写风暴。

- [PostgreSQL 宏观查询优化之 pg_stat_statements · 扩展插件：PGSS](/pg/pgss/#扩展插件pgss)
- [PostgreSQL 宏观查询优化之 pg_stat_statements · 每秒执行时长](/pg/pgss/#每秒执行时长)
- [PostgreSQL 宏观查询优化之 pg_stat_statements · WAL 日志量](/pg/pgss/#wal-日志量)

### 上千类 SQL 按何优先级调优，怎样定性慢查询？ {#macro-tuning-workflow}

脱离全局占比（`%M`）死磕偶发慢 SQL 纯属内耗：只占总耗时 3% 的查询不必急动，吃掉全库 50% 耗时或块 I/O 的查询组砍掉一条就能削去半壁负载。调优遵循“先按 `%M` 抓大头，再联看时间导数 `dM/dt` 与单次调用导数 `dM/dc`”：全库各组平均 RT 齐涨指向硬件饱和，单组突刺锁定慢 SQL 或烂发版；单次仅返几行却扫数 MB 缓冲块，必是缺索引或计划翻转。

- [PostgreSQL 宏观查询优化之 pg_stat_statements · 平均延迟/响应时间/RT](/pg/pgss/#平均延迟响应时间rt)
- [PostgreSQL 宏观查询优化之 pg_stat_statements · 百分比指标](/pg/pgss/#百分比指标)

### 高频点查为何严控一毫秒内，慢查询怎样五步止血？ {#one-ms-sla-and-slow-query}

探探核心库将在线高频点查死卡在“99.99% 低于 1ms”，源于硬核容量账：单次 1ms 即单核每秒千次，48 线程（折算 30 有效核）物理机理论上限恰为 \(30 \times 1000 = 3\text{万}\) QPS。高频 SQL 一旦破 1ms 会瞬间打满连接池雪崩并拖挂从库复制。急救遵循“定位 QueryID—猜根因—核对表级顺序扫描激增—在线补索引止血—监控量化收益”五步闭环，实战中单条索引即可将饱和度从 40% 压回 4%。

- [KNN极致优化：从RDS到PostGIS · 实际场景中的表现](/pg/knn-optimize/#实际场景中的表现)
- [PG慢查询诊断方法论 · 慢查询的定义](/pg/slow-query/#慢查询的定义)
- [PG慢查询诊断方法论 · 慢查询：危害](/pg/slow-query/#慢查询危害)
- [PG慢查询诊断方法论 · 慢查询诊断 —— 传统方法](/pg/slow-query/#慢查询诊断--传统方法)
- [PG慢查询诊断方法论 · 慢查询：小结](/pg/slow-query/#慢查询小结)

### 零扫描索引能直接删吗，清理废索引有哪些陷阱？ {#dummy-and-duplicate-indexes}

僵尸索引白占缓存还拖慢写入与 `VACUUM`，但见 `idx_scan = 0` 绝不可盲删——支撑主键与唯一约束的索引哪怕零扫描也肩负判重职责。排查 SQL 须联查 `pg_constraint` 剔除约束索引、过滤 `indkey` 含 `0` 的表达式索引，按体积降序拼出 `DROP INDEX CONCURRENTLY` 无锁清理；按 `(indrelid, indkey)` 分组抓同列重复索引时，落刀前必须核对 `WHERE` 子句以免误删热点部分索引。

- [找出没用过的索引 · 找出没有使用的索引](/pg/find-dummy-index/#找出没有使用的索引)
- [找出没用过的索引 · 找出重复的索引](/pg/find-dummy-index/#找出重复的索引)

### 脚本编排 psql 跑批如何防半提交与锁库？ {#psql-bash-and-batch-ops}

裸跑 `psql -f` 遇错照常往下执行且会读 `.psqlrc` 污染输出，生产 Bash 包装脚本必须开 `set -euo pipefail` 并传 `-X -v ON_ERROR_STOP=1 --single-transaction` 保原子执行。跨库导表用双端 `\copy` 走匿名管道即可免临时文件流式裁剪；而海量数据复杂清洗切忌跑单体大事务锁库，应在库内建带 `done = false` 的状态表，由外部脚本循环 `LIMIT 1` 微事务步进消费。

- [Bash与psql小技巧 · 执行SQL脚本的Bash包装脚本](/pg/psql-and-bash/#执行sql脚本的bash包装脚本)
- [Bash与psql小技巧 · 跨数据库拷贝表](/pg/psql-and-bash/#跨数据库拷贝表)
- [Bash与psql小技巧 · 如何使用状态表来控制多个PG任务](/pg/psql-and-bash/#如何使用状态表来控制多个pg任务)
