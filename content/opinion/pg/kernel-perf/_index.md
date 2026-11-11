---
title: 内核机理、性能调优与故障急救
linkTitle: 内核调优与故障急救
description: WAL 与 MVCC 膨胀治理、锁与隔离级别、黄金监控指标与慢查询方法论、XID 回卷与坏块抢救等生产急救档案。
weight: 40
icon: fa-solid fa-gauge-high
---

平时把数据库当黑盒使唤，线上出事就只能对着报错抓瞎。从 WAL 与脏页的刷盘门闩、追加写 MVCC 的膨胀权衡，到八级表锁队列、黄金监控信号与 `pg_stat_statements` 微分治理，PostgreSQL 的每一条运维铁律背后都有严密的源码契约与血泪账本。本篇汇集内核底层机理、容量监控方法论与极端生产故障的急救档案，只给经受过高压检验的硬核判断。

## 一、日志先行、MVCC 膨胀与内核演进 {#wal-mvcc-and-kernel}

### PostgreSQL 先写脏页还是先写 WAL？ {#wal-before-dirty-page}

“日志先行（WAL）”约束的是磁盘刷盘顺序而非内存顺序：内存中先改脏页再写 WAL 缓冲，落盘时先刷 WAL 再刷脏页。PostgreSQL 默认用物理日志记录页面二进制变化，后端必须先排他锁钉内存页，在出错即 `PANIC` 的不可中断临界区内改好页面，才能构造出 `XLogRecord`。而每个内存页头都记有最后修改位点 `pd_lsn`，任何进程执行 `FlushBuffer` 刷脏前都必须先调 `XLogFlush(pd_lsn)` 确认对应日志已持久化——想彻底吃透这套协同契约，最好的第一手教材永远是高度自解释的 PG 源码及各子系统下的 `README`。

- [PG先写脏页还是先写WAL？ · INSERT 的内存修改](/pg/wal-before-page/#insert-的内存修改)：拆解内存阶段锁钉页面、进入不可中断临界区先改脏页再构造 `XLogRecord` 写入缓冲区的原子流程。
- [PG先写脏页还是先写WAL？ · 如何强制 WAL 先于脏页刷盘？](/pg/wal-before-page/#如何强制-wal-先于脏页刷盘)：剖析页面头部 `pd_lsn` 与 `FlushBuffer` 刷盘前调用 `XLogFlush` 强制日志先落盘的门闩机制。
- [PG先写脏页还是先写WAL？ · 关于内核原理](/pg/wal-before-page/#关于内核原理)：推荐铃木启修、Egor Rogov 内幕专著，并阐明 PostgreSQL 源码与模块 `README` 作为第一手教材的价值。

### 追加写 MVCC 与新存储引擎该如何权衡？ {#mvcc-tradeoff-and-tam}

OpenAI 曾诟病 PostgreSQL 更新单列也要整行复制并带来死元组扫描放大，但工程的本质是权衡：追加写 MVCC 换来了读写无锁高吞吐、极低延迟的物理流复制、大事务瞬时回滚与后台平滑回收 I/O 的能力，配好 `idle_in_transaction_session_timeout` 与定期清理完全可治理。OrioleDB 改用类 Oracle 的 UNDO 回滚段根治了膨胀与回卷（代价是慢回滚），并能通过 `USING orioledb` 与原生堆表同库共存；但生产上切忌盲目尝鲜实验性存储引擎——TimescaleDB 短命的 Hypercore 就曾因垃圾回收缺陷引爆 20 亿年龄只读保护，陷入 `VACUUM` 报错、`DROP TABLE` 被拒的死锁绝境。

- [OpenAI：一套 PG 支持8亿 ChatGPT 用户 · MVCC 膨胀的利弊权衡](/pg/openai-postgres/#mvcc-膨胀的利弊权衡)：评注 OpenAI 生产实践，阐明追加写 MVCC 在流复制延迟与读写并发上的收益及工程化治理手段。
- [OrioleDB来了！4x性能，消除顽疾，存算分离 · 消除顽疾，简化运维](/pg/orioledb-is-coming/#消除顽疾简化运维)：解析 OrioleDB 以 UNDO 回滚段消除表膨胀与回卷，并通过 `USING orioledb` 与原生堆表同库按表共存的设计。
- [尝鲜须谨慎：PG新存储引擎故障案例 · 具体案例](/pg/new-storage-engine-risk/#具体案例)：复盘 TimescaleDB Hypercore 因 GC 漏洞触发全实例 XID 回卷只读保护、被迫新建集群逻辑迁回堆表的真实事故。

### 表空间该如何核算，怎样零 I/O 测算膨胀率？ {#table-size-and-bloat-estimate}

只看堆表主文件会严重低估真实容量：一张逻辑表在物理上是由本体表、TOAST 大字段表、各自索引及每层关系的 `main/fsm/vm/init` 四类分支文件（超 1GB 自动切段）构成的复合树。`pg_relation_size` 默认只算 `main` 分支，监控 SQL 必须用囊括分支与 TOAST 树的 `pg_table_size` 加二级索引 `pg_indexes_size`，才能严丝合缝对齐 `pg_total_relation_size`。巡检膨胀率同样忌讳在 200GB 大表上跑扫盘五分钟的 `pgstattuple`；结合 `pg_class` 页数、`pg_stats` 空值位图与 8 字节对齐公式估算紧实页数，零磁盘 I/O 仅需 50 毫秒即可算完 3TB 全库膨胀率。

- [监控PG中的表大小 · 表的空间布局](/pg/mon-table-size/#表的空间布局)：拆解本体表、TOAST 表、索引及 `main/fsm/vm/init` 四类物理分支文件构成的完整空间复合树。
- [监控PG中的表大小 · 统计函数](/pg/mon-table-size/#统计函数)：厘清 `pg_relation_size`、`pg_table_size` 与 `pg_indexes_size` 的统计口径，给出不重不漏的容量核算公式。
- [关系膨胀的监控与治理 · 膨胀率的估算](/pg/bloat/#膨胀率的估算)：基于元组 23 字节头、空值位图与字段平均宽度的 8 字节对齐公式，实现 3TB 大库 50ms 零 I/O 膨胀巡检。

### 为什么表还会膨胀，pg_repack 在线压实有何雷区？ {#autovacuum-and-pg-repack}

常规并发 `VACUUM` 只标记死元组供后续插入复用，不跨页搬移活元组压实空洞，表文件体积自然只增不减；而 `VACUUM FULL` 全程霸占 `AccessExclusiveLock` 锁表，在线库必须靠 `pg_repack` 无锁重整。它通过建同结构新表、挂行触发器记增量日志并在追平后瞬时换名实现在线压实，宜按表体积分档（如小表膨胀超 40%、1～4GB 超 20%）在低谷自动执行。但执行前必须预留至少一倍原表加索引的空闲磁盘，警惕切换瞬间不可取消的 WAL 洪峰冲高复制延迟；一旦中途异常强杀，务必立即手工清扫残留的 `table_<oid>` 临时表与原表增量触发器。

- [关系膨胀的监控与治理 · 关系膨胀概述](/pg/bloat/#关系膨胀概述)：解释并发 `VACUUM` 不缩减物理文件的原因，对比 `VACUUM FULL` 锁表代价与在线重整必要性。
- [关系膨胀的监控与治理 · pg_repack 的原理](/pg/bloat/#pg_repack-的原理)：剖析快照拷贝、触发器增量日志与原子换名的无锁压实流程，给出按表大小分档的自动化阈值策略。
- [关系膨胀的监控与治理 · pg_repack 的注意事项](/pg/bloat/#pg_repack-的注意事项)：警示双倍磁盘预留、切换期流复制 WAL 洪峰，以及异常中断后残留触发器导致持续写放大的清理要点。

### 单机 PG 的吞吐上限与新硬件演进方向在哪？ {#scalability-ceiling-and-hardware}

得益于 MVCC，PG 只读吞吐随加核与从库线性扩展，单机百 TB 容量毫无压力；真正的单实例软件上限在于 100～300 MB/s 的 WAL 写入重放（两亿用户的探探全局写仅约 120 MB/s）与多进程短连接开销。PG 17 用 `TidStore` 将 `VACUUM` 内存骤降为 1/20、解除 `1GB` 硬上限，并借流式 I/O 与 WAL 锁优化使高并发写入最高翻倍。面对 448 核、24TB 内存的怪兽单机，Jonathan Katz 指出需攻克异步直接 I/O（DIO/AIO）与并行 WAL 崩溃恢复；Margo Seltzer 更点破固态普及后头号瓶颈已移至 DRAM 主存速度墙，下一代内核必须重构缓冲池以驾驭 HBM 与 CXL 异构内存。

- [令人惊叹的PostgreSQL可伸缩性 · PostgreSQL 的可伸缩性现状](/pg/pg-scalability/#postgresql-的可伸缩性现状)：结合探探 120 MB/s 全局写入实测，界定单机在读扩展、百 TB 存储、WAL 重放与连接数四维度的真实边界。
- [PostgreSQL 17 发布：摊牌了，我不装了！ · 系统性能的全面提升](/pg/pg-17/#系统性能的全面提升)：详解 PG 17 引入 `TidStore` 削减 95% 垃圾回收内存及优化 WAL 锁使高并发写入吞吐翻倍的突破。
- [PostgreSQL 17 beta1 发布！ · 查询和写入性能改善](/pg/pg-17-beta1/#查询和写入性能改善)：解析解除 `VACUUM` 历史遗留 `1GB` 内存硬上限、流式顺序扫描与 B-tree `IN` 检索等底层改进。
- [展望 PostgreSQL 的2024 · 性能](/pg/pg-in-2024/#性能)：论证引入 DIO/AIO 与并行 WAL 恢复对于榨干数百核大内存单机算力、消除数小时崩溃恢复窗口的关键意义。
- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · 临时加场：当数据库遇上新硬件](/pg/pgcondev-2024/#临时加场当数据库遇上新硬件)：引述 Margo Seltzer 演讲，点明数据库物理瓶颈从磁盘 I/O 转向主存带宽延迟及适配 HBM/CXL 的挑战。

### 为什么多线程化阻力重重且 C 扩展 ABI 极脆弱？ {#threading-and-extension-abi}

将 PG 从多进程改为多线程虽能带来轻量连接与共享缓存，但社区内部阻力极大：除了 Tom Lane 警告的丧失进程级故障隔离外，更致命的是会迫使数百个依赖进程私有内存假设的 C 扩展彻底重写，短期绝无落地可能。C 扩展对内核 ABI 本就极度脆弱——PG 17.1 仅给 `ResultRelInfo` 增加一个布尔值使其从 376 字节涨至 384 字节，按旧步长做数组指针算术的 TimescaleDB 便当场越界段错误。用覆盖五百多个扩展的打包流水线实测 PG 19 快照（一举抓出约 50 个构建失败），正是量化多线程与 Hook 补丁生态冲击面的最佳早期预警。

- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · PostgreSQL 线程模型](/pg/pgcondev-2024/#postgresql-线程模型)：记录多线程化提案引发的扩展维护者激烈反弹，剖析连接轻量化收益与重写全局状态、破坏生态的巨大冲突。
- [不要更新！发布当日叫停：PG也躲不过大翻车 · 附：关于 ABI 的问题的解释](/pg/pg-faint/#附关于-abi-的问题的解释)：引用 Marco Slot 内存拆解，还原 `ResultRelInfo` 扩容 8 字节击穿 TimescaleDB 结构体数组指针寻址的机理。
- [人人可用的 PG 扩展 · 29. PG 19 兼容性](/pg/extensions-for-everyone/#29-pg-19-兼容性)：展示用 500+ 扩展全量构建流水线实测 PG 19 快照捕获约 50 个失败案例，建立内核变更冲击面早期预警。

### 小版本升级为何会在流复制与 TOAST 上翻车？ {#minor-upgrade-regressions}

哪怕是只修 Bug 的小版本升级也绝不能闭眼滚生产，底层并发恢复与存储切片的微妙耦合随时可能引爆回归事故。官方曾临发版废掉 18.5 直发 18.6，重点修复了上一轮小版本的流复制自死锁回归——升级后的新备库重放旧小版本主库 WAL 时竟会自死锁卡死，同期还修了可见性映射清除位漏记 WAL 破坏增量备份及 `SERIALIZABLE` 空 B-tree 漏检冲突。而在 PG 18.2 中，`CVE-2026-2006` 补丁将不完整多字节字符改为抛错，却忽略了大于 2KB 的中文存于 TOAST 列时 `text_substring()` 按估算字节切片极易截半汉字，导致线上普通 `substring(col, 1, 2)` 直接报错。

- [井喷：修了 28 个 CVE、110 个 BUG，PG 最新小版本发布 · Bug 修复与改进](/pg/pg-186-cve/#bug-修复与改进)：复盘跳过 18.5 直发 18.6 的关键修复，涵盖跨小版本流复制重放自死锁、VM 漏记 WAL 与防回卷缓冲池利用率缺陷。
- [号外：暂缓 PG 最新小版本安装与升级 · BUG 1：substring() 对非 ASCII Toast 文本报错](/pg/pg-out-of-sync-202602/#bug-1substring-对非-ascii-toast-文本报错)：剖析多字节边界安全修复撞上 TOAST 压缩列预估解压切片机制，导致中文表列 `substring()` 异常的根因。

### 初始化为何必须死守 C.UTF8 而禁设 zh_CN？ {#locale-c-utf8-and-nls}

初始化生产库把 `LOCALE`（尤其 `LC_COLLATE`）设为非 `C` 规则是不可原谅的失误。`C` 按码位逐字节直比，`zh_CN` 或 `en_US` 则调系统库做复杂语言学比较：150 万行混合文本排序会从 1.43 秒跌至 14.85 秒慢十倍，更会废掉普通 B-Tree 索引的 `LIKE '前缀%'` 扫描引发全表扫雪崩；其实 `LOCALE=C` 是超集，局部查询显式写 `COLLATE "zh_CN"` 即可无损按拼音排序。服务端消息禁设 `zh_CN` 同样不是玄学——旧版中文目录七年失管跌至 66%，把 `out of memory` 反向错译成“内存溢出”、吞掉系统错误码 `%m`，`ecpg` 甚至把单 `%s` 译成 `%1$s` 与 `%2$s` 触发越界真 Bug。

- [PG中的本地化排序规则 · 性能损失](/pg/collate/#性能损失)：实测 150 万行文本在 `zh_CN` 下内存比较慢 3 倍、全表 `ORDER BY` 外部排序从 1.43 秒恶化至 14.85 秒的十倍损耗。
- [PG中的本地化排序规则 · 为什么？](/pg/collate/#为什么)：解释非 `C` 排序规则因多字符等价规则无法将 `LIKE '前缀%'` 转化为紧致码位区间，导致 B-Tree 主键索引失效的机理。
- [PG中的本地化排序规则 · 兼容性修改](/pg/collate/#兼容性修改)：示范全局坚守 `LOCALE=C` 保住极致性能与索引功能，同时在局部 SQL 按需声明 `COLLATE "zh_CN"` 的最佳实践。
- [PostgreSQL 中文版来了 · 错译陈列馆](/pg/pg-nls/#错译陈列馆)：揭露旧版中文消息目录七年失管埋下的 `out of memory` 反向错译、丢失 `%m` 与 `ecpg` 格式化越界等硬伤。

## 二、事务契约、隔离级别、锁层次与线缆协议 {#tx-lock-and-protocol}

### MySQL 半成功事务错在哪，PG 如何兼顾容错？ {#acid-atomicity-savepoint}

ACID 原子性的底线是“All or Nothing”，而 MySQL/InnoDB 默认竟允许同一事务内首条 DML 成功、次条报错后继续 `COMMIT` 落盘“半成功中间态”，还辩称为 Feature。这种把平账责任甩锅给初级开发者的苟且设计纯属“Stupid by Design”，令所谓“金融级 MySQL”沦为笑谈。合格的数据库必须像 PostgreSQL 一样在服务端默认禁止制造脏账——事务内任一语句报错即进入中止态拒绝提交；若客户端确有交互容错需求，用 `psql` 的 `ON_ERROR_ROLLBACK`（底层借标准隐式 `SAVEPOINT` 自动回滚单条错句），即可在不玷污服务端一致性的前提下体面解决。

- [如何看待 MySQL vs PGSQL 直播闹剧 · 更新：MySQL 事务机制缺陷](/pg/mysql-pg-live-drama/#更新mysql-事务机制缺陷)：批判 MySQL 默认放行含报错语句的事务执行部分提交、违背原子性契约的底层设计缺陷。
- [为什么PostgreSQL前途无量？ · ACID](/pg/pg-is-great/#acid)：对比 MySQL 服务端半提交隐患与 PostgreSQL 严守原子性底线并靠客户端隐式 `SAVEPOINT` 优雅容错的工程高下。

### 三级事务隔离分别防住了什么又会漏掉哪些异常？ {#isolation-levels-anomalies}

默认的 `Read Committed` 只靠语句级快照防脏读脏写，绝不阻止丢失更新（P4）与读偏斜——并发“先 `SELECT` 读回内存加一再写回”必丢数据，必须改写为 `SET v = v + 1` 原地原子更新。升至基于事务级快照的 `Repeatable Read` 后，并发改同一行会直接抛冲突错误回滚，根治丢失更新与标准幻读（PMP）；但若两事务同时读两行校验约束后各自修改不相交的一行，仍会漏网产生写偏斜（G2-item）。唯有启用 `Serializable` 追踪读写依赖环并在成环 `COMMIT` 时主动中止，才能彻底封堵写偏斜与多事务反依赖环（G2），代价是应用端必须内置幂等重试机制。

- [事务隔离等级注意事项 · 更新丢失（P4）](/pg/isolation-level/#更新丢失p4)：演示 `Read Committed` 下“先读后写”并发覆盖导致丢失更新的过程，给出原子更新改写方案。
- [事务隔离等级注意事项 · Write Skew (G2-item)](/pg/isolation-level/#write-skew-g2-item)：解析 `Repeatable Read` 如何靠写冲突回滚拦截丢失更新，却在不相交行并发修改时放行写偏斜的边界。
- [事务隔离等级注意事项 · Anti-Dependency Cycles (G2)](/pg/isolation-level/#anti-dependency-cycles-g2)：阐明 `Serializable` 追踪谓词读写依赖环拦截 G2 异常的乐观并发机制及客户端幂等重试要求。

### 八级表锁如何演化，为何 pg_locks 查不到行锁？ {#table-locks-and-vxid}

看似绕口的八种表锁实为四步演化的最小完备集：从原始读写锁出发，先加 `Access` 前缀解耦 MVCC 读写；再加 `RowShare/RowExclusive` 意向锁防持行锁时整表被抢排他锁；最后补齐 `ShareUpdateExclusive` 等自斥锁，让 `VACUUM` 或并发建索引既不挡业务读写，又禁止同表双开维护进程互踩。`pg_locks` 里查不到磁盘行锁，是因为行锁直接记在数据页元组头上，且只读事务仅分配本地虚拟号 `vxid` 以省下 32 位全局 `txid`；等行锁在视图中表现为对持锁 `txid/vxid` 申请 `ShareLock`，且因视图拼接了进程 `fastpath` 数据，切忌高频轮询争抢锁管理器。

- [PostgreSQL中的锁 · 表级锁的演化](/pg/pg-lock/#表级锁的演化)：沿读写解耦、行表意向协调与维护操作自斥四阶段，推演八级表锁模式的完备设计逻辑。
- [PostgreSQL中的锁 · 样例数据](/pg/pg-lock/#样例数据)：详解只读事务 `vxid` 省号机制、元组头行锁借事务 `ShareLock` 休眠等待的表现及 `fastpath` 视图采样特性。

### 毫秒级加空列为何会引发雪崩，大表 DDL 怎么拆？ {#lock-queue-and-online-ddl}

哪怕是一条不重写表、理论上毫秒级完成的 `ADD COLUMN` 空列变更，在高并发库上也足以引爆全站读雪崩。根源在于锁队列防饥饿机制：只要表上有慢查询拿着 `AccessShare` 未退，申请 `AccessExclusive` 的 DDL 就会进队阻塞，并把后续涌入的所有普通 `SELECT` 统统拦死在门外。因此线上强锁 DDL 必须恪守两条铁律：一是强制前置 `SET lock_timeout`，宁可超时重试绝不当路障；二是将大表维护拆为“长时弱锁 + 瞬时强锁”——加默认值列拆成“秒级加空列 + 分批回填”，加主键拆成“先 `CREATE UNIQUE INDEX CONCURRENTLY` + 后 `USING INDEX` 瞬时挂载”。

- [PostgreSQL中的锁 · 锁队列](/pg/pg-lock/#锁队列)：剖析慢查询与排队中的 `AccessExclusive` 锁联手阻断全表只读请求的链式阻塞机理，确立 `lock_timeout` 保命铁律。
- [PostgreSQL中的锁 · 最小化锁阻塞时长](/pg/pg-lock/#最小化锁阻塞时长)：给出加默认值列与新增主键约束的标准无锁拆解步骤，将排他锁窗口压缩至毫秒级。

### 线缆协议如何定界，写七层连接代理要注意什么？ {#wire-protocol-and-proxy}

PG v3 线缆协议状态机边界极为清晰：客户端发带 `0x30000` 魔数的 `StartupMessage` 启动，服务端依次推认证、会话参数 `ParameterStatus` 与取消密钥 `BackendKeyData`，直至下发 `ReadyForQuery (Z)` 闭合握手；查询阶段同样按表头、行载荷、`CommandComplete` 与携带事务状态的 `ReadyForQuery` 确定性收尾。手写七层连接代理最容易踩中 SSL 握手细节：`psql` 等客户端建连常先发特殊 SSL 探测包而非普通启动帧，若代理不卸载 TLS，必须先回写单字节 `'N'` 引导客户端降级重发真实 `StartupMessage`，随后借 `pgproto3` 数十行 Go 代码即可实现透传或协议审计。

- [前后端通信线缆协议 · 启动阶段](/pg/wire-protocol/#启动阶段)：拆解 v3 线缆协议从 `StartupMessage` 握手认证到查询结果集流转、以 `ReadyForQuery` 定界的完整帧序列。
- [前后端通信线缆协议 · 连接代理](/pg/wire-protocol/#连接代理)：点破建连阶段响应单字节 `'N'` 处理 SSL 探测降级的协议细节，并用 `pgproto3` 实现双向代理原型。

### 本地抓包为何不见明文，混杂与监控模式差在哪？ {#wireshark-capture-and-rfmon}

本地敲 `psql` 抓不到可读报文，是因为省略主机名默认走 Unix Socket 旁路网卡，且走 TCP 默认优先启用 SSL。抓明文包须显式指定 `-h localhost` 监听 `lo0` 并加 `sslmode=disable`，在 Wireshark `pgsql` 解码下可见单条 `SELECT` 历经建连合并回包、简单查询与 `Terminate` 共 5 组交互。若在无线环境下抓非本机包，则须分清网卡“混杂模式”与“射频监控模式（RFMON）”：混杂模式必须先关联特定 Wi-Fi 且只能抓该局域网流量；唯有启用监控模式（如 `tcpdump -I`）才能脱离热点在物理信道层嗅探所有网络的原始 802.11 帧，因该模式会断网，工程上宜外接独立网卡嗅探。

- [Wireshark抓包分析协议 · 抓包样例](/pg/wireshark-capture/#抓包样例)：演示通过 `localhost` 回环接口与 `sslmode=disable` 捕获并解码“建连—查询—断连”五步明文报文的实操流程。
- [Wireshark抓包分析协议 · 题外话：使用Mac进行无线网络嗅探](/pg/wireshark-capture/#题外话使用mac进行无线网络嗅探)：辨析网卡混杂模式与 802.11 射频监控模式（RFMON）的底层差异及外接网卡嗅探实践。

## 三、黄金监控指标、PG Load 水位与压测基线 {#metrics-load-and-benchmark}

### 三千指标如何做减法，为何报错与 QPS 管不住水位？ {#golden-metrics-hierarchy}

单机加 PG 动辄暴露三千多个指标，全堆上主面板只会造成注意力过载。必须把事后验尸的“黑匣子冷指标”与日常盯盘的十项黄金信号（错误、连接排队、PG Load、复制延迟、RT、活跃后端、事务年龄、QPS、CPU）严格分离。四类信号各司其职：错误与排队告警优先级最高，但平时恒为零只能事后“定性报丧”，绝不能拿报错管日常水位；QPS 把 10 微秒点查与 10 秒大查询等权记作 1 次，跨库与历史纵向对比皆失真；RT 适合划定“OLTP 禁超 1ms”质量红线，唯有归一化到 `0%～100%` 的饱和度指标才能统领瞬时告警红线与长期扩容黄线。

- [黄金监控指标：错误延迟吞吐饱和 · 核心指标](/pg/golden-metrics/#核心指标)：提出冷热指标分离原则，浓缩出覆盖错误、延迟、流量与饱和度四维度的十项日常盯盘黄金指标。
- [黄金监控指标：错误延迟吞吐饱和 · 错误指标](/pg/golden-metrics/#错误指标)：阐明错误指标作为头号报警信号却因平时恒零、无法事前量化健康水位的局限性。
- [黄金监控指标：错误延迟吞吐饱和 · 流量指标](/pg/golden-metrics/#流量指标)：剖析数据库 QPS 抹平请求轻重差异、无法跨库对比及划定通用容量红线的根本缺陷。
- [黄金监控指标：错误延迟吞吐饱和 · 饱和度指标](/pg/golden-metrics/#饱和度指标)：对比应用侧 RT 红线与 DBA 侧 `0%～100%` 归一化饱和度标尺在告警与容量规划中的分工。

### 如何构造跨机型归一化的 PG Load 负载指标？ {#pg-load-kpi}

主机 CPU 与磁盘 I/O 只是机器 KPI，遇到库内锁争用或连接耗尽即失灵。将单位时间内所有后端活跃总秒数求导再除以宿主机 CPU 核数，便得到数据库本层饱和度 `PG Load`——数学上恒等于 \(\text{TPS} \times \text{事务 RT} / \text{CPU 核数}\)，天然抹平机型与 SQL 轻重差异。因 `pg_stat_activity` 只是离散快照算不出积分，生产上须对连接池 Pgbouncer 单调递增的 `total_xact_time` 求导，顺带把占着连接空转的 `Idle in Transaction` 罚入水位。慢查询堵死连接池时 TPS 仅微跌，`PG Load` 却瞬间冲破 `70%` 红线乃至飙上 `500%`；15 分钟曲线更滤除了备份与 `VACUUM` 杂音，长期处于 `30%～50%` 即可指导扩容。

- [PostgreSQL的KPI · 0x02 常用评估指标的问题](/pg/pg-load/#0x02-常用评估指标的问题)：论证机器硬件利用率在锁等待与连接耗尽场景下的盲区，确立构建数据库本层饱和度 KPI 的必要性。
- [PostgreSQL的KPI · 数据库负载（PG Load）](/pg/pg-load/#数据库负载pg-load)：推导活跃时长导数除以 CPU 核数的 `PG Load` 定义，揭示其统一吞吐、延迟与硬件算力的数学本质。
- [PostgreSQL的KPI · 如何获取活跃时长](/pg/pg-load/#如何获取活跃时长)：解释为何放弃 `pg_stat_activity` 离散采样，改用 Pgbouncer `total_xact_time` 微分精准积分并纳入空闲长事务惩罚。
- [PostgreSQL的KPI · 0x05 PG Load的实际效果](/pg/pg-load/#0x05-pg-load的实际效果)：展示 `PG Load` 在慢查询雪崩秒级破红线告警及滤除维护杂音指导长期扩容中的实战曲线。

### 内置统计视图有何滞后，新一代查询遥测怎么做？ {#stats-collector-and-telemetry}

搭好 Grafana 只是监控的“面子”，吃透内核语义才是“里子”：PG 缓冲池命中率不含 OS Page Cache；开启 `full_page_writes` 时每次检查点后首次改页都会刷整页镜像激起 WAL 洪峰，若业务 Backend 被迫高频刷脏则说明检查点失调。同时 `pg_stat_*` 存在闲置才上报、`500ms` 节流与事务内快照冻结三重滞后，长事务轮询须调 `pg_stat_clear_snapshot()`。若想在低于 1% 损耗下抓逐条 SQL 分位数延迟，新一代扩展 `pg_stat_ch` 用前端 Hook 写无背压共享内存环形队列（满则丢弃绝不反压主库，p99 仅 5μs）异步流式推入 ClickHouse，再配 `pg_datasentinel` 即可追踪 cgroup 压力与回卷 ETA。

- [PostgreSQL监控系统概览 · 监控系统的指标](/pg/monitoring-overview/#监控系统的指标)：拆解 OS 文件缓存、会话 `idle in transaction` 与表级顺序扫描突增背后的深层故障含义。
- [PostgreSQL监控系统概览 · 检查点与 WAL](/pg/monitoring-overview/#检查点与-wal)：剖析检查点后全页写（FPI）流量波峰成因，以及从 Backend 刷脏比例诊断检查点参数失调的方法。
- [PostgreSQL监控系统概览 · 统计收集器](/pg/monitoring-overview/#统计收集器)：揭示内置统计视图闲置上报、`500ms` 节流与事务内快照冻结三重延迟及 `pg_stat_clear_snapshot()` 用法。
- [504 个扩展，PG 生态的天花板在哪？ · 7. pg_stat_ch: ClickHouse 官方出品的 PostgreSQL 查询遥测](/pg/extension-504/#7-pg_stat_ch-clickhouse-官方出品的-postgresql-查询遥测)：解析无背压共享内存环形队列旁路流式遥测架构，在 36.6K TPS 下以低于 1% 损耗捕获逐条查询明细。

### 服务器日志怎么配，如何不搭 ELK 用 SQL 查日志？ {#csvlog-and-file-fdw}

生产库切忌用难解析的纯文本日志，标准基线是将 `log_destination` 设为 `csvlog` 输出含会话 ID、虚拟事务号与状态码的 23 列结构化记录，并全开检查点、锁等待、DDL、秒级慢查询、慢 Autovacuum 与 `track_io_timing`。同机部署 Filebeat 等采集器必须按行首时间戳正则（`^20\d\d-\d\d-\d\d`）合并跨行 SQL，并强制限制 `max_cpus: 1` 与队列内存，严防报错风暴抢空数据库算力。其实无需搭重型 ELK：将日志配为按星期轮转的 `postgresql-%a.log`，用 `file_fdw` 映射为继承自 `monitor.pg_log` 的 7 张外部子表，写标准 SQL 就能零搬运跨天聚合慢查询与报错分布。

- [PG服务器日志常规配置 · 日志相关配置项](/pg/logging/#日志相关配置项)：给出启用 `csvlog` 结构化输出及锁等待、检查点、Autovacuum 与 I/O 计时全套生产配置基线。
- [PG服务器日志常规配置 · 日志收集](/pg/logging/#日志收集)：指出跨行 SQL 碎片化痛点与同机 Agent 反噬算力风险，确立多行正则归并与单核 CPU 限流规范。
- [PG服务器日志常规配置 · 映射日志](/pg/logging/#映射日志)：示范按星期轮转 CSV 日志配合 `file_fdw` 继承外部表与正则函数，实现自举式 SQL 原地日志分析。

### CPU 不高为何 Load 爆表，怎样读懂主机指标？ {#linux-cli-diagnostics}

排查主机瓶颈最忌望文生义：`top` 的 Load Average 统计的是运行态（`R`）与不可中断睡眠态（`D`，多阻塞在磁盘硬件 I/O 且不响应信号）的平均任务数而非 CPU 利用率，Load 飙升时须联看 `D` 态进程数、`%wa` 与虚拟化偷取时间 `%st`。同理，重度依赖 OS Page Cache 的 PG 主机不能只看 `free` 空闲列，内核会把空闲内存全拿去做可随时回收的 `buffers/cache`，只要 `Swap` 已用与 `vmstat` 换页 `si/so` 为 `0` 即内存充裕。看磁盘则须敲 `iostat -dxk` 穿透请求合并，联看队列 `avgqu-sz`、延迟 `r_await/w_await` 与 `%util`——四大工具本质都是 `/proc` 计数器的采样视图。

- [Linux 常用统计 CLI 工具 · 摘要部分](/pg/unix-tool/#摘要部分)：厘清 Load Average 囊括 `R` 态与 `D` 态不可中断 I/O 睡眠进程的本质，指导结合 `%wa` 与 `%st` 定位卡顿。
- [Linux 常用统计 CLI 工具 · 输出样例](/pg/unix-tool/#输出样例)：解析 `buffers/cache` 对数据库页缓存的加速作用，确立以 Swap 换入换出流量为零判定内存健康的准则。
- [Linux 常用统计 CLI 工具 · 输出说明](/pg/unix-tool/#输出说明)：详解 `iostat -x` 合并率、队列长度与响应延迟指标，点明四大统计工具同源于 `/proc` 伪文件的底层机制。

### FIO 与 sysbench 压测有哪些口径与红线？ {#fio-and-sysbench-benchmark}

压测必须对齐真实物理粒度与公平标尺。PG 数据页默认是 8KB 而非 OS 4KB，验收存储须给 FIO 加 `-direct=1` 绕过 Page Cache，用 `libaio` 重点考察各并发读写比下的 8KB 随机 I/O 及模拟 WAL 的 1MB 顺序吞吐；切记裸块设备写压测会直接覆写分区超级块毁盘，严禁在生产盘执行，且 XFS 挂载须加 `noatime,nodiratime` 消除读致写放大。与 MySQL 等异构数据库横向对比 OLTP 性能时，自带的 `pgbench` 模型偏私有，应编译 `--with-pgsql` 驱动运行标准 `sysbench` 的 `oltp_read_write.lua`，在相同表规模、索引与并发下公平对比 TPS 与 P95 延迟。

- [使用FIO测试磁盘性能](/pg/fio/)：给出 `-direct=1` 绕过缓存、聚焦 PG 8KB 页面随机读写与 1MB 顺序吞吐的 FIO 矩阵，警示裸盘写毁灭文件系统的红线与 XFS `noatime` 挂载规范。
- [使用sysbench测试PostgreSQL性能 · 压测](/pg/sysbench/#压测)：说明编译 `--with-pgsql` 驱动运行 `oltp_read_write.lua` 统一异构数据库 OLTP 压测口径的方法。

## 四、宏观查询优化、慢查询闭环与运维自动化 {#query-tuning-and-automation}

### 裸查 PGSS 有何盲区，怎样揪出暗刷 WAL 的真凶？ {#pgss-blindspots-and-wal}

`pg_stat_statements`（PGSS）按用户、库与归一化 `queryid` 聚合查询，是生产必装基石，但裸查视图有三大盲区：运行中卡死的语句得查 `pg_stat_activity`，超时报错中断的语句不入 PGSS，且内置 `mean/min/max` 列无时间窗参考价值极低，必须高频采集累积 Counter 做差分。抓 CPU 杀手切忌按 QPS 排序，应对 `total_exec_time` 求导算无量纲的“每秒执行时长（`s/s`）”，物理意义等同主机 `load1`。若无高频 DML 却爆复制延迟，对 `wal_bytes` 与 `wal_fpi` 求导即可揪出两类隐蔽元凶：执行大批修改后 `ROLLBACK` 的废事务，以及大吞吐只读 `SELECT` 首扫改 Hint Bit 在检查点后引爆的全页写风暴。

- [PostgreSQL 宏观查询优化之 pg_stat_statements · 扩展插件：PGSS](/pg/pgss/#扩展插件pgss)：界定 PGSS 不记录运行中与超时失败语句的统计边界，阐明抛弃内置均值列、对累积计数器做时序差分的原则。
- [PostgreSQL 宏观查询优化之 pg_stat_statements · 每秒执行时长](/pg/pgss/#每秒执行时长)：定义 `d(exec_time)/dt` 派生指标，用每秒投入的并发执行秒数精准度量各查询组的真实系统负载贡献。
- [PostgreSQL 宏观查询优化之 pg_stat_statements · WAL 日志量](/pg/pgss/#wal-日志量)：利用语句级 `wal_bytes` 与 `wal_fpi` 速率定位回滚废事务及纯只读查询修改提示位引发的全页写日志洪峰。

### 上千类 SQL 按什么优先级调优，如何定性慢查询？ {#macro-tuning-workflow}

脱离全局占比（`%M`）死磕偶发慢 SQL 纯属内耗：某查询哪怕上千 QPS，只占总耗时的 3% 就不急着动；反之吃掉全库 50% 耗时或块 I/O 的查询组，优化它就能削掉半壁负载。宏观治理遵循戴明循环：先按百分比锁定时长、块带宽与 WAL 大头，再联看时间导数 `dM/dt` 与调用导数 `dM/dc`。对调用次数微分的语句组平均 RT 是定性故障的黄金准绳——全库各组 RT 齐涨指向底层硬件饱和，单组 RT 突刺则锁定慢 SQL 与发版回滚点；一旦发现某 OLTP 查询单次仅返回寥寥几行却扫数 MB 缓冲块，便是缺索引或执行计划翻转的铁证。

- [PostgreSQL 宏观查询优化之 pg_stat_statements · 平均延迟/响应时间/RT](/pg/pgss/#平均延迟响应时间rt)：详解用窗口内平均 RT 区分全局硬件瓶颈与单 SQL 劣化，以及对比单次返回行数与缓冲区访问带宽抓缺索引的方法。
- [PostgreSQL 宏观查询优化之 pg_stat_statements · 百分比指标](/pg/pgss/#百分比指标)：建立“先按 `%M` 全局占比抓大头、再联看 `dM/dt` 与 `dM/dc`、最后 `EXPLAIN` 微观手术并监控验证”的闭环工作流。

### 高频查询为何严控 1 毫秒内，慢查询如何五步止血？ {#one-ms-sla-and-slow-query}

慢查询阈值取决于频次：后台低频查询超 `100ms～1s` 才算慢，但探探核心库将在线高频点查死死卡在“99.99% 低于 1 毫秒”。背后是容量硬账：单次 1ms 即单线程每秒 1000 次，24 核 48 线程（折算约 30 有效核）物理机理论吞吐恰为 \(30 \times 1000 = 30,000\) QPS，与线上 1 主 19 从单机 3 万峰值严丝合缝。高频查询破 1ms 会迅速打满连接池雪崩并钉住旧元组拖挂从库复制。结合慢日志抓特例与时序 PGSS 抓拐点，急救应遵循“定位 QueryID—猜想根因—核对表级顺序扫描激增—补索引零侵入止血—监控曲线量化收益”五步法，实战中修一条慢 SQL 就曾把饱和度从 40% 压至 4%。

- [KNN极致优化：从RDS到PostGIS · 实际场景中的表现](/pg/knn-optimize/#实际场景中的表现)：用 48 线程物理机折算 30 有效核乘以 1ms 延迟倒推 3 万 QPS 容量上限，验证线上核心集群真实峰值账本。
- [PG慢查询诊断方法论 · 慢查询的定义](/pg/slow-query/#慢查询的定义)：按业务形态区分偶发查询秒级阈值与高频 OLTP 点查突破 1ms 即拉响警报的生产界定标准。
- [PG慢查询诊断方法论 · 慢查询：危害](/pg/slow-query/#慢查询危害)：剖析慢查询引发连接池打满雪崩、流复制重放挂起与锁踩踏的三重连锁破坏及饱和度从 40% 降至 4% 的实证。
- [PG慢查询诊断方法论 · 慢查询诊断 —— 传统方法](/pg/slow-query/#慢查询诊断--传统方法)：对比慢查询日志抓单次特例与时序化采集 `pg_stat_statements` 突破累计均值盲区的互补分工。
- [PG慢查询诊断方法论 · 慢查询：小结](/pg/slow-query/#慢查询小结)：提炼从指标下钻、表级顺序扫描验证到无侵入补索引止血与成本收益量化的五步标准闭环。

### 零扫描索引能直接删吗，清理废索引有哪些陷阱？ {#dummy-and-duplicate-indexes}

僵尸索引白占缓存与磁盘，还拖慢每次写入与 `VACUUM`，但看到 `idx_scan = 0` 绝不能一股脑全删——支撑主键或唯一约束的底层索引哪怕从未被查询扫描，也肩负唯一性校验职责。排查 SQL 必须联查 `pg_constraint` 剔除约束索引，过滤 `indkey` 含 `0` 的表达式索引，按体积降序统一生成 `DROP INDEX CONCURRENTLY` 在线无锁删除。对于多人迭代堆出的同列重复索引，对 `pg_index` 按 `(indrelid, indkey)` 分组筛 `COUNT(*) > 1` 即可快速揪出，但落刀前须人工核对 `WHERE` 子句，严防误删专为热点子集定制的部分索引（Partial Index）。

- [找出没用过的索引 · 找出没有使用的索引](/pg/find-dummy-index/#找出没有使用的索引)：给出排除唯一约束索引与表达式索引的零扫描废索引排查 SQL，并自动拼接 `DROP INDEX CONCURRENTLY` 语句。
- [找出没用过的索引 · 找出重复的索引](/pg/find-dummy-index/#找出重复的索引)：利用 `(indrelid, indkey)` 分组聚合快速揪出同表同列冗余索引，并提示甄别部分索引过滤条件。

### Bash 编排 psql 跑批如何防半提交与锁库？ {#psql-bash-and-batch-ops}

默认参数跑 `psql -f` 遇错照常往下执行且会加载 `.psqlrc` 污染输出，极易酿成半截入库事故。生产 Bash 包装脚本必须开 `set -euo pipefail` 严格模式，并强制传 `-X --set ON_ERROR_STOP=on --single-transaction` 保证原子变更。跨实例单表迁移与字段裁剪，用双端 `\copy ... to stdout | psql -c "\copy ... from stdin"` 走匿名管道即可零中间文件一行搞定（脚本取值配 `-X -t --no-align`）。而面对海量数据复杂清洗，切忌跑不可中断的单体大事务，应在库内建带 `done = false` 的任务状态表，由外部脚本循环 `LIMIT 1` 步进消费，兼顾最小锁粒度与断点续跑。

- [Bash与psql小技巧 · 执行SQL脚本的Bash包装脚本](/pg/psql-and-bash/#执行sql脚本的bash包装脚本)：给出开启 `set -euo pipefail` 与 `-X`、`ON_ERROR_STOP=on`、`--single-transaction` 的生产变更安全包装模板。
- [Bash与psql小技巧 · 跨数据库拷贝表](/pg/psql-and-bash/#跨数据库拷贝表)：演示利用双端 `\copy` 标准输入输出管道实现免临时文件的跨实例流式表拷贝与字段裁剪。
- [Bash与psql小技巧 · 如何使用状态表来控制多个PG任务](/pg/psql-and-bash/#如何使用状态表来控制多个pg任务)：设计带 `done` 状态列的任务队列配合外部 Bash 步进循环，将危险大事务拆解为可中断续跑的微事务。

## 五、雪崩复盘：连接池、回卷溢出与时钟回拨 {#outage-postmortems}

### 分库减半负载为何反致崩盘，连接池怎样被慢查询吞噬？ {#shard-paradox-and-pool-starvation}

曾有一套核心集群分库迁走一半数据与一半 QPS 后，非但没减负反而在晚高峰雪崩：因为拆走的全是亚毫秒级快查询，原库两个重型函数的调用占比从 `1/6` 升至 `5/9`，并发突破 30 时触发剧烈并行劣化（耗时从 500μs 暴涨 200 倍至 100ms），最大吞吐从 40k QPS 断崖跌至 8k QPS。而在 PgBouncer 侧，48 核机器平时 5～10 个连接即可消化快查询；一旦混入慢查询霸占连接，快查询排队迫使池子撑满至 `max_pool_size=100`，释放的连接瞬间又被新慢查询夺走，最终形成 100 个进程全跑慢 SQL、CPU 飙顶假死的死局。

- [故障档案：快慢不匀雪崩 · 外因：分库迁移](/pg/download-failure/#外因分库迁移)：复盘分库拆走纯快查询推高重查询并发占比、跨越 30 并发劣化拐点导致容量从 40k 跌至 8k QPS 的反直觉事故。
- [故障档案：快慢不匀雪崩 · 表因：连接打满](/pg/download-failure/#表因连接打满)：拆解慢查询逐步蚕食 PgBouncer 100 个后端连接、彻底挤死亚毫秒级快查询的连接池饥饿机理。

### 配了超时为何仍堆慢查询，从库假死怎样秒级回血？ {#cancel-request-and-watch-rescue}

应用层配了超时甚至断路器仍被慢查询拖死，是因为老旧驱动（如早期 `go-pg`）配的只是底层 TCP 超时——客户端单方面弃等并不会向 PG 发取消指令，慢查询仍在后台白烧连接与算力，断路器还会放大抖动；必须换用支持 `Context` 主动发送 Cancel Request 的现代驱动（如 `pgx`）多层协同设防。当从库被慢查询塞满假死、定向查杀失效时，切忌调 `pg_terminate_backend` 杀进程引发重连风暴，而应用 `psql` 配 `\watch 0.5` 每半秒无差别执行 `pg_cancel_backend(pid)`：利用快查询驻留不足 1ms 的概率差精准清场，业务瞬间回血。

- [故障档案：快慢不匀雪崩 · 副内因：没有超时](/pg/download-failure/#副内因没有超时)：揭露客户端弃等不等于数据库取消查询的陷阱，强调选用支持主动发送 Cancel Request 驱动构建端到端超时防线。
- [故障档案：快慢不匀雪崩 · 修复](/pg/download-failure/#修复)：实战演示用 `\watch 0.5` 高频循环调用 `pg_cancel_backend` 无重连冲击秒级清退慢查询、恢复假死集群的急救手法。

### 报错退出的 pg_dump 如何毒化连接池，怎样根治？ {#pgbouncer-connection-pollution}

Pgbouncer 事务池化模式下后端连接被海量前端事务复用，谁改了会话参数归还连接就会毒化后续请求。线上曾有人误拿 10.5 版 `pg_dump` 连向 11.1 实例前的 Pgbouncer `6432` 端口：工具为防同名劫持，建连首步便执行 `set_config('search_path', '', false)` 独立提交清空搜索路径，旋即因服务端版本更高报错退出，向池中留下一条 `search_path=''` 的毒连接，引发全站简写表名的业务间歇性报错。急救登管理端敲 `RECONNECT` 秒级洗池；根治须同时开启 `server_reset_query = DISCARD ALL` 与 `server_reset_query_always = 1`，并严禁运维工具连业务池。

- [故障档案：pg_dump导致的连接池污染 · 连接污染](/pg/pg-dump-failure/#连接污染)：剖析事务级连接池复用机制下，`search_path`、预备语句等会话状态残留引发跨事务污染的原理。
- [故障档案：pg_dump导致的连接池污染 · Bug复现](/pg/pg-dump-failure/#bug复现)：还原低版本 `pg_dump` 先置空 `search_path` 提交、后因版本不匹配退出从而向连接池投毒的完整链路。
- [故障档案：pg_dump导致的连接池污染 · 解决方案](/pg/pg-dump-failure/#解决方案)：给出 `RECONNECT` 秒级止血指令，以及同时开启 `DISCARD ALL` 与 `server_reset_query_always = 1` 的根治配置。

### 事务号回卷为何逼停生产库，急救冻结要注意什么？ {#xid-wraparound-rescue}

PG 的 32 位事务号靠模 \(2^{32}\) 环形比较切分各 21 亿“过去”与“未来”，老元组若未及时 `VACUUM FREEZE` 冻结（`xid=2`）且年龄破 21 亿，已提交数据会瞬间隐身；3 万 TPS 下清理停滞一天便触发剩一千万号时的强制停写。爆发回卷必有前置病灶卡死 AutoVacuum：空闲长事务 `IDLE IN TRANSACTION` 钉死水位、坏块致单表清理中断，或主从切换缺失 CLOG。急救忌跑整库 `VACUUM`，须联查 `pg_class` 及附属 TOAST 表按 `relfrozenxid` 年龄降序逐表精准 `VACUUM FREEZE`（拉满 `vacuum_cost_limit`、清零延迟），并警惕流复制从库共享年龄同样陷入保护态。

- [故障档案：PostgreSQL事务号回卷 · 背景](/pg/xid-wrap-around/#背景)：图解 32 位环形事务空间各 21 亿可见窗口与剩余一千万事务号触发强制停写保护的内核机制。
- [故障档案：PostgreSQL事务号回卷 · 问题](/pg/xid-wrap-around/#问题)：归纳空闲长事务、坏块中断与 CLOG 缺失三大阻断 AutoVacuum 自动冻结的线上典型诱因。
- [故障档案：PostgreSQL事务号回卷 · 注意事项](/pg/xid-wrap-around/#注意事项)：给出包含 TOAST 表按年龄降序定位、解除流控参数精准 `VACUUM FREEZE` 及防范备库同步回卷的抢救手册。

### 表不大为何主键序列会溢出，无法改表时怎样续命？ {#sequence-overflow-rescue}

表里有效行不多，32 位 `SERIAL` 主键却突然溢出停写，源于 `SEQUENCE` 高并发发号绝不回滚：唯一键冲突报错回滚不退号，高频 `INSERT ... ON CONFLICT DO UPDATE` 哪怕走更新分支每次也照样预吞一个新号——真实故障中 99.99% 的序列号都被冲突重试白白吞噬。当主键耗尽又因外键耦合无法当场跑 DDL 改 `BIGINT` 时，可用 `generate_series` 与现有主键做差集 `EXCEPT`，快速挖出 5000 万个未占用的空洞 ID 建号段表，改写插入逻辑用 `SELECT ... FOR UPDATE LIMIT 1` 配 `DELETE ... RETURNING` 队列弹号，稳赢十余天迁移窗口。

- [故障档案：序列号消耗过快导致整型溢出 · 外因：不了解Sequence的特性](/pg/sequence-overflow/#外因不了解sequence的特性)：揭示序列发号不随回滚退回及 `ON CONFLICT DO UPDATE` 每次暗耗序列号导致 99.99% 号段空洞的陷阱。
- [故障档案：序列号消耗过快导致整型溢出 · 解决方案](/pg/sequence-overflow/#解决方案)：实战演示用 `EXCEPT` 挖掘五千万主键空洞建池、配合行锁 `DELETE ... RETURNING` 队列发号紧急恢复写入的巧思。

### 重启后 NTP 回拨为何会让 Patroni 拒绝接管？ {#ntp-stepback-patroni-failure}

宿主机故障重启后，明明 PostgreSQL 进程已正常跑着，高可用管家 Patroni 却反复报 `Process is not postmaster` 拒绝接管并罢工。根因在于开机时钟阶跃回拨：为防操作系统 PID 复用误杀进程，Patroni 会严格比对 `postmaster.pid` 记录的启动时间戳与系统进程真实的 `create_time`。若开机服务编排让 PG 先于 NTP 启动，随后启动的 NTP 将偏快的系统时钟向后阶跃回拨超出阈值，两边时间戳失配即触发防误判保护。保障开机 NTP 时间同步严格先于数据库与 Patroni 启动，是高可用集群不可忽视的底层铁律。

- [故障档案：时间回溯导致的Patroni故障](/pg/time-travel/)：完整复盘宿主机重启后 NTP 晚于 PostgreSQL 启动并阶跃回拨系统时间，导致 `postmaster.pid` 启动时间校验失配使 Patroni 罢工的排障全过程。

## 六、绝境破局：死锁自救、坏块修复与裸页抢救 {#extreme-data-recovery}

### 坏扩展锁死超级用户如何自救，怎样预留逃生通道？ {#broken-extension-global-2964}

用 `ALTER ROLE/DATABASE` 给全局角色与库挂载缺失内核符号的损坏 `.so` 到 `session_preload_libraries`，会让实例瞬间沦为“植物人”：Postmaster 虽存活，但连超级用户在内的任何新建连接都在派生瞬间 `FATAL` 自杀，根本进不去敲 `ALTER` 撤销。因该配置持久化在 `pg_db_role_setting` 对应的 `$PGDATA/global/2964` 文件中，唯有停库拿十六进制编辑器把 `global/2964` 里的坏扩展名原地刷成等长零字节或截断才能救活。铁律有二：C 扩展上线前必须先在单会话 `LOAD` 验证；永远保留一个不挂任何预加载钩子的纯净超级用户逃生通道。

- [故障档案：PG安装Extension导致无法连接 · 于是……](/pg/extension/#于是)：记录损坏扩展写入 `pg_db_role_setting` 锁死全部新建连接后，停库通过十六进制编辑抹除 `$PGDATA/global/2964` 救活实例的极限操作。
- [故障档案：PG安装Extension导致无法连接 · 教训……](/pg/extension/#教训)：提炼单会话先行测试验证动态库符号与常备无钩子纯净超级用户逃生通道的两条保命准则。

### 遇到数据页损坏如何算偏移并从备库捞数？ {#invalid-page-ctid-recovery}

线上报 `invalid page in block N of relation base/db/relfilenode`，说明内核调 `PageIsVerified` 读盘入共享缓冲池时发现该 8KB 页面首部标志位、空闲上下界（`pd_lower <= pd_upper`）或校验和已损毁。因表文件每满 `1GB` 自动切为 `.1`、`.2` 等段文件，拿 `块号 × 8192` 对 `1GB` 做整除和取模，即可精确定位受损段文件与十六进制字节偏移。若底层 SSD 坏块已抹零该页，切忌在主库乱动破坏现场，最稳妥无损的打法是去硬件物理隔离的健康流复制从库上，直接按 `WHERE ctid = '(block, offset)'` 捞回该页全部完好记录再重建主表。

- [PostgreSQL数据页面损坏修复 · 最初的问题](/pg/page-corruption/#最初的问题)：解析 `PageIsVerified` 页面校验逻辑、8KB 块号换算 1GB 段文件物理偏移公式及从流复制备库按 `ctid` 捞回丢失行的标准步骤。

### 主库为何禁开 zero_damaged_pages？ {#zero-damaged-pages-trap}

十余 TB 大库无备机可切又被个别坏块卡死跑批时，临时开 `zero_damaged_pages = on` 会把报错降为 `WARNING` 并在内存缓冲池将该页填零跳过；因未标脏（`isdirty = f`），常规检查点与重启不会覆写磁盘坏页。但在生产主库长开它等于埋下两颗炸弹：一是主库对抹零页原有的主键彻底“失明”，再次插入同主键会顺利放行并复制到从库，造成从库“同一主键查出两条记录”的唯一性崩坏；二是一旦后台 `VACUUM` 扫过内存全零页，会将其当作未初始化新页格式化标脏刷盘，把磁盘上原本还能抢救的残损字节永久清零毁灭。

- [PostgreSQL数据页面损坏修复 · 苟且的办法](/pg/page-corruption/#苟且的办法)：验证 `zero_damaged_pages` 仅在共享缓冲池内存抹零跳过坏块、不主动标脏覆写磁盘原始字节的底层行为。
- [PostgreSQL数据页面损坏修复 · 微妙的问题](/pg/page-corruption/#微妙的问题)：揭露主库开启该参数放行重复主键击穿从库唯一性，以及被后台 `VACUUM` 初始化刷盘彻底毁灭原始坏页现场的双重灾难。

### 实例烤糊停摆时，如何用 pg_filedump 抢救？ {#pg-filedump-bare-metal-rescue}

当无备份实例遭双进程踩踏与误敲 `pg_resetwal` 彻底烤糊无法启动时，只要底层数据页尚存，`pg_filedump` 仍能成批救回上千张表。先按固定 OID 从 `global/1262` 找库目录，优先解出 `pg_class (1259)`、`pg_namespace`、`pg_attribute`、`pg_type` 四张字典表（结合 `pg_filenode.map`，过滤 `XMAX != 0` 死元组），再用 SQL 自动生成全库表路径与 `-D` 类型抽取脚本。真正的魔鬼在两处细节：`(TOASTED)` 大字段须把 `reltoastrelid` 指向的 TOAST 表切片解出按序回填；不受支持的 `ARRAY` 会吐含 `\0` 原始字节，须加 `-f` 对照内核源码逐字节解析维度、空值位图、元素 OID、4 字节长度头移位与对齐填充。

- [如何用 pg_filedump 抢救数据？ · 恢复数据字典](/pg/pg-filedump/#恢复数据字典)：详解利用固定 OID 与 `pg_filenode.map` 优先还原四张系统元数据表，并用 SQL 自动生成上千张业务表批量抽取脚本的方法。
- [如何用 pg_filedump 抢救数据？ · 魔鬼在细节中](/pg/pg-filedump/#魔鬼在细节中)：攻克 TOAST 线外切片回填拼装与对照内核源码逐字节解析 `ARRAY` 十六进制头部、空值位图及内存对齐的硬核难点。
