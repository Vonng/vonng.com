---
title: WAL 日志先行、MVCC 膨胀治理与新硬件演进
linkTitle: WAL 与 MVCC 治胀
description: 脏页与 WAL 刷盘门闩、零 I/O 膨胀率估算、pg_repack 无锁压实与异构内存演进。
weight: 200
icon: fa-solid fa-hard-drive
---

追加写 MVCC 与物理 WAL 契约赋予了 PostgreSQL 极致的无锁并发与流复制吞吐，代价是必须治理表膨胀与长事务。吃透内核刷盘顺序、ABI 边界与排序规则铁律，才能榨干现代大内存单机极限。

## 一、WAL 刷盘契约与 MVCC 膨胀治理 {#wal-and-mvcc-bloat}

### PostgreSQL 先写脏页还是先写 WAL？ {#wal-before-dirty-page}

“日志先行”约束的是刷盘顺序而非内存顺序：内存中先改脏页再写 WAL 缓冲，落盘时先刷 WAL 再刷脏页。进程须在出错即 `PANIC` 的临界区内先改页面才能构造 `XLogRecord`；页头记有 `pd_lsn`，`FlushBuffer` 刷脏前必调 `XLogFlush(pd_lsn)` 锁死日志先行——PG 源码与模块 `README` 是最佳一手教材。

- [PG先写脏页还是先写WAL？ · INSERT 的内存修改](/pg/wal-before-page/#insert-的内存修改)
- [PG先写脏页还是先写WAL？ · 如何强制 WAL 先于脏页刷盘？](/pg/wal-before-page/#如何强制-wal-先于脏页刷盘)
- [PG先写脏页还是先写WAL？ · 关于内核原理](/pg/wal-before-page/#关于内核原理)

### 追加写 MVCC 与新存储引擎该如何权衡？ {#mvcc-tradeoff-and-tam}

工程本质是权衡：追加写 MVCC 虽带来死元组膨胀，却换来了无锁读、低延迟流复制与大事务瞬时回滚，配好空闲事务超时与清理完全可控。OrioleDB 借 UNDO 回滚段消除了膨胀且可与堆表同库共存，但生产切忌盲目尝鲜——TimescaleDB 的 Hypercore 就曾因 GC 漏洞引爆 20 亿年龄全库只读锁死。

- [OpenAI：一套 PG 支持8亿 ChatGPT 用户 · MVCC 膨胀的利弊权衡](/pg/openai-postgres/#mvcc-膨胀的利弊权衡)
- [OrioleDB来了！4x性能，消除顽疾，存算分离 · 消除顽疾，简化运维](/pg/orioledb-is-coming/#消除顽疾简化运维)
- [尝鲜须谨慎：PG新存储引擎故障案例 · 具体案例](/pg/new-storage-engine-risk/#具体案例)

### 表空间该如何核算，怎样零 I/O 测算膨胀率？ {#table-size-and-bloat-estimate}

一张逻辑表在物理上由本体表、大字段表、索引及各自的 `main/fsm/vm/init` 四类分支文件构成复合树；监控必须用囊括分支与大字段树的 `pg_table_size` 加上 `pg_indexes_size`，才能严丝合缝对齐真实总容量。日常巡检膨胀切忌在大表上跑全表扫盘的 `pgstattuple`；结合系统表页数、字段平均宽度与字节对齐公式估算紧实页数，零磁盘读写仅需 50 毫秒即可算完 3TB 全库膨胀率。

- [监控PG中的表大小 · 表的空间布局](/pg/mon-table-size/#表的空间布局)
- [监控PG中的表大小 · 统计函数](/pg/mon-table-size/#统计函数)
- [关系膨胀的监控与治理 · 膨胀率的估算](/pg/bloat/#膨胀率的估算)

### 表体积为何只增不减，pg_repack 有何坑？ {#autovacuum-and-pg-repack}

并发 `VACUUM` 仅标记死元组复用而不缩减文件，`VACUUM FULL` 又全程锁死表，在线压实须靠 `pg_repack` 建影子表、挂触发器追增量后原子换名。执行前须预留双倍空闲磁盘并防范切换期 WAL 洪峰；若中途被异常强杀，务必立即手工清理残留的 `table_<oid>` 临时表与原表增量触发器。

- [关系膨胀的监控与治理 · 关系膨胀概述](/pg/bloat/#关系膨胀概述)
- [关系膨胀的监控与治理 · pg_repack 的原理](/pg/bloat/#pg_repack-的原理)
- [关系膨胀的监控与治理 · pg_repack 的注意事项](/pg/bloat/#pg_repack-的注意事项)

## 二、单机伸缩上限、ABI 契约与本地化铁律 {#kernel-evolution-and-locale}

### 单机 PG 的吞吐上限与新硬件演进方向在哪？ {#scalability-ceiling-and-hardware}

单机百 TB 存储与只读吞吐可随加核挂从库线性扩展，真正的软件上限在于 100～300 MB/s 的 WAL 写入重放（两亿用户的探探全局写仅约 120 MB/s）。PG 17 借 `TidStore` 削减 95% 清理内存并令高并发写入翻倍；Jonathan Katz 指出榨干百核大机需攻克 DIO/AIO 与并行恢复，Margo Seltzer 更点破固态普及后瓶颈已转向 DRAM 速度墙，内核须演进驾驭 HBM 与 CXL 异构内存。

- [令人惊叹的PostgreSQL可伸缩性 · PostgreSQL 的可伸缩性现状](/pg/pg-scalability/#postgresql-的可伸缩性现状)
- [PostgreSQL 17 发布：摊牌了，我不装了！ · 系统性能的全面提升](/pg/pg-17/#系统性能的全面提升)
- [PostgreSQL 17 beta1 发布！ · 查询和写入性能改善](/pg/pg-17-beta1/#查询和写入性能改善)
- [展望 PostgreSQL 的2024 · 性能](/pg/pg-in-2024/#性能)
- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · 临时加场：当数据库遇上新硬件](/pg/pgcondev-2024/#临时加场当数据库遇上新硬件)

### 多线程化为何难落地，C 扩展 ABI 有多脆弱？ {#threading-and-extension-abi}

将 PG 改为多线程除了 Tom Lane 警告丧失进程级故障隔离外，更会迫使数百个依赖进程私有内存假设的 C 扩展彻底重写，短期难落地。C 扩展对 ABI 本就极脆弱——Marco Slot 拆解过 PG 17.1 仅给 `ResultRelInfo` 增加 8 字节，便令按旧步长寻址的 TimescaleDB 段错误崩溃；用覆盖五百余个扩展的打包流水线实测 PG 19 快照（抓出约 50 个失败），正是最佳早期预警。

- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · PostgreSQL 线程模型](/pg/pgcondev-2024/#postgresql-线程模型)
- [不要更新！发布当日叫停：PG也躲不过大翻车 · 附：关于 ABI 的问题的解释](/pg/pg-faint/#附关于-abi-的问题的解释)
- [人人可用的 PG 扩展 · 29. PG 19 兼容性](/pg/extensions-for-everyone/#29-pg-19-兼容性)

### 小版本升级为何会在流复制与 TOAST 上翻车？ {#minor-upgrade-regressions}

只修 Bug 的小版本同样可能引爆底层耦合回归：官方曾废掉 18.5 直发 18.6，紧急修复新备库重放旧小版本主库 WAL 时的自死锁，以及可见性映射漏记 WAL 破坏增量备份的缺陷。而在 PG 18.2 中，`CVE-2026-2006` 补丁将残缺多字节字符改为抛错，却撞上超 2KB 中文 TOAST 列按估算字节切片截半汉字的机制，导致普通 `substring()` 直接报错。

- [井喷：修了 28 个 CVE、110 个 BUG，PG 最新小版本发布 · Bug 修复与改进](/pg/pg-186-cve/#bug-修复与改进)
- [号外：暂缓 PG 最新小版本安装与升级 · BUG 1：substring() 对非 ASCII Toast 文本报错](/pg/pg-out-of-sync-202602/#bug-1substring-对非-ascii-toast-文本报错)

### 初始化为何必守 C.UTF8 而禁设中文排序？ {#locale-c-utf8-and-nls}

生产初始化设 `zh_CN` 排序是严重失误：150 万行排序会从 `C` 逐字节直比的 1.43 秒恶化至 14.85 秒慢十倍，更会废掉 B-Tree 索引的 `LIKE '前缀%'` 扫描；全局守住 `C`、局部按需声明 `COLLATE` 即可。旧版中文消息更失管多年，把 `out of memory` 错译为“内存溢出”、丢 `%m` 且含 `ecpg` 格式化越界缺陷。

- [PG中的本地化排序规则 · 性能损失](/pg/collate/#性能损失)
- [PG中的本地化排序规则 · 为什么？](/pg/collate/#为什么)
- [PG中的本地化排序规则 · 兼容性修改](/pg/collate/#兼容性修改)
- [PostgreSQL 中文版来了 · 错译陈列馆](/pg/pg-nls/#错译陈列馆)
