---
title: 生产雪崩复盘：XID 回卷、死锁自救与裸页抢救
linkTitle: 雪崩复盘与绝境抢救
description: 连接池雪崩、20 亿事务年龄回卷、时钟回拨故障及 pg_filedump 底层坏块抢救档案。
weight: 230
icon: fa-solid fa-kit-medical
---

真实的生产雪崩从不按教科书出牌：拆库减负可能引爆连接池饥饿，报错退出的备份工具会毒化全站会话，开机时钟回拨足以令高可用停摆。复盘十起血泪事故与 `pg_filedump` 捞数绝技，方知敬畏运维铁律。

## 一、雪崩复盘：连接池、回卷溢出与时钟回拨 {#outage-postmortems}

### 分库减半负载为何反致崩盘，连接池怎样被吞噬？ {#shard-paradox-and-pool-starvation}

核心集群拆走一半数据与 QPS 后反而晚高峰崩盘：因迁走的全是亚毫秒快查询，留下的重函数调用占比从 `1/6` 升至 `5/9`，并发破 30 后触发剧烈劣化（延迟暴涨 200 倍至 100ms），总吞吐从 40k 断崖跌至 8k QPS。连接池侧平时 10 个连接即可消化快查询，一旦慢查询混入霸占连接，池子迅速撑满至 `max_pool_size=100` 且释放即被新慢查询夺走，彻底挤死快业务。

- [故障档案：快慢不匀雪崩 · 外因：分库迁移](/pg/download-failure/#外因分库迁移)
- [故障档案：快慢不匀雪崩 · 表因：连接打满](/pg/download-failure/#表因连接打满)

### 配了超时为何仍堆慢查询，从库假死怎样秒级回血？ {#cancel-request-and-watch-rescue}

应用配了超时仍拖死数据库，是因为老驱动（如早期 `go-pg`）只断本地 TCP 等待而不发协议层 Cancel Request，慢查询照常在库内空烧算力；必须换 `pgx` 等支持 `Context` 主动取消的现代驱动。当从库被慢查询塞满假死时，切忌调 `pg_terminate_backend` 杀进程引爆重连风暴，直接用 `psql` 配 `\watch 0.5` 每半秒无差别跑 `pg_cancel_backend`，借快慢驻留概率差即可秒级清场回血。

- [故障档案：快慢不匀雪崩 · 副内因：没有超时](/pg/download-failure/#副内因没有超时)
- [故障档案：快慢不匀雪崩 · 修复](/pg/download-failure/#修复)

### 报错退出的备份工具如何毒化连接池，怎样根治？ {#pgbouncer-connection-pollution}

事务池复用连接时残留会话状态会跨事务投毒：低版本 `pg_dump` 误连高版本实例前的 Pgbouncer，首步提交清空 `search_path` 后因版本不匹配退出，留下空路径毒连接引发全站间歇找不到表。急救敲 `RECONNECT` 秒级洗池；根治须同开 `DISCARD ALL` 与 `server_reset_query_always = 1`，并严禁运维工具连业务池。

- [故障档案：pg_dump导致的连接池污染 · 连接污染](/pg/pg-dump-failure/#连接污染)
- [故障档案：pg_dump导致的连接池污染 · Bug复现](/pg/pg-dump-failure/#bug复现)
- [故障档案：pg_dump导致的连接池污染 · 解决方案](/pg/pg-dump-failure/#解决方案)

### 事务号回卷为何逼停生产库，急救冻结要注意什么？ {#xid-wraparound-rescue}

PG 的 32 位事务号靠模 \(2^{32}\) 环切分各 21 亿过去与未来，老元组未冻结且年龄破限就会瞬间隐身；3 万 TPS 下空闲长事务、坏块或 CLOG 缺失卡死 AutoVacuum 一天，便会触发剩一千万号时的强制停写保护。急救忌跑整库 `VACUUM`，须连同附属 TOAST 表按 `relfrozenxid` 年龄降序拉满流控参数逐表精准 `VACUUM FREEZE`，并严防流复制从库同步陷入回卷保护。

- [故障档案：PostgreSQL事务号回卷 · 背景](/pg/xid-wrap-around/#背景)
- [故障档案：PostgreSQL事务号回卷 · 问题](/pg/xid-wrap-around/#问题)
- [故障档案：PostgreSQL事务号回卷 · 注意事项](/pg/xid-wrap-around/#注意事项)

### 表不大为何主键序列会溢出，无法改表时怎样续命？ {#sequence-overflow-rescue}

表里有效行不多但 32 位 `SERIAL` 突然耗尽停写，源于 `SEQUENCE` 发号绝不回滚：冲突报错不退号，高频 `INSERT ... ON CONFLICT DO UPDATE` 哪怕走更新分支每次也照吞一个新号，线上曾有 99.99% 号段被空耗。若受外键牵制无法当场改 `BIGINT`，可用 `generate_series` 对现有主键做 `EXCEPT` 挖出五千万空洞 ID 建号段表，借 `FOR UPDATE` 配 `DELETE ... RETURNING` 队列发号续命十余天。

- [故障档案：序列号消耗过快导致整型溢出 · 外因：不了解Sequence的特性](/pg/sequence-overflow/#外因不了解sequence的特性)
- [故障档案：序列号消耗过快导致整型溢出 · 解决方案](/pg/sequence-overflow/#解决方案)

### 重启时钟回拨为何会让 Patroni 拒绝接管？ {#ntp-stepback-patroni-failure}

宿主机故障重启后 PG 进程明明存活，高可用管家 Patroni 却反复报 `Process is not postmaster` 罢工。根因是开机时钟阶跃回拨：为防 PID 复用误杀，Patroni 严格校验 `postmaster.pid` 记录的启动时间与系统进程真实 `create_time`；若编排不当让 PG 先于 NTP 启动，随后 NTP 将偏快时钟向后回拨超限，两边时间戳失配即拒管。开机必须强制 NTP 同步严先于数据库启动。

- [故障档案：时间回溯导致的Patroni故障](/pg/time-travel/)

## 二、绝境破局：死锁自救、坏块修复与裸页抢救 {#extreme-data-recovery}

### 坏扩展锁死超级用户如何自救，怎样预留逃生通道？ {#broken-extension-global-2964}

用 `ALTER ROLE/DATABASE` 将缺内核符号的损坏 `.so` 挂入 `session_preload_libraries`，会让包括超级用户在内的所有新建连接在派生瞬间 `FATAL` 自杀，根本进不去撤销。因该配置落在 `$PGDATA/global/2964`（`pg_db_role_setting`），唯有停库用十六进制编辑器将坏扩展名原地抹成零字节或截断才能救活。铁律有二：C 扩展必先单会话 `LOAD` 验证；常备无任何预加载钩子的纯净超管逃生号。

- [故障档案：PG安装Extension导致无法连接 · 于是……](/pg/extension/#于是)
- [故障档案：PG安装Extension导致无法连接 · 教训……](/pg/extension/#教训)

### 遇到数据页损坏如何算偏移并从备库无损捞数？ {#invalid-page-ctid-recovery}

报 `invalid page in block N` 说明 `PageIsVerified` 读盘时发现该 8KB 页首部、空闲上下界或校验和损毁。因表文件每满 `1GB` 切段，拿 `N × 8192` 对 `1GB` 整除和取模即可算出段文件号与物理字节偏移。若主库 SSD 坏块已抹零该页，切忌在主库乱动破坏现场，最稳妥无损的打法是去物理隔离的健康流复制从库，直接按 `WHERE ctid = '(N, offset)'` 捞回完好记录修复主表。

- [PostgreSQL数据页面损坏修复 · 最初的问题](/pg/page-corruption/#最初的问题)

### 生产主库为何严禁开启坏页内存抹零参数？ {#zero-damaged-pages-trap}

开启 `zero_damaged_pages` 虽只在内存缓冲池填零跳过坏页且不立即标脏，但在主库长开会引爆双重灾难：一是主库对坏页原有主键失明，重插同主键会放行并复制到从库击穿唯一性；二是后台 `VACUUM` 扫过内存全零页会将其格式化标脏刷盘，把磁盘上尚可抢救的残损字节永久清零毁灭。

- [PostgreSQL数据页面损坏修复 · 苟且的办法](/pg/page-corruption/#苟且的办法)
- [PostgreSQL数据页面损坏修复 · 微妙的问题](/pg/page-corruption/#微妙的问题)

### 实例烤糊无法启动时，如何从裸数据页抢救全库？ {#pg-filedump-bare-metal-rescue}

无备份实例遭误敲 `pg_resetwal` 彻底停摆时，只要底层数据页尚存即可用 `pg_filedump` 批量抢救：先按固定 OID 与 `pg_filenode.map` 优先解出 `pg_class` 等四张系统字典表（过滤 `XMAX != 0` 死元组），再用 SQL 生成全库 `-D` 抽取脚本。两处魔鬼细节在于：`(TOASTED)` 大字段须解出附属 TOAST 表切片按序拼回；不受支持的 `ARRAY` 须加 `-f` 对照内核源码逐字节解析维度、空值位图与对齐头。

- [如何用 pg_filedump 抢救数据？ · 恢复数据字典](/pg/pg-filedump/#恢复数据字典)
- [如何用 pg_filedump 抢救数据？ · 魔鬼在细节中](/pg/pg-filedump/#魔鬼在细节中)
