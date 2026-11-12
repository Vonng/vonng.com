---
title: 并发隔离异常、八级锁队列与时间编码基石
linkTitle: 并发隔离与锁队列
description: 事务隔离异常谱系、线性一致性边界、PG 八级锁等待阻塞链与时区时间戳铁律。
weight: 210
icon: fa-solid fa-lock
---

并发隔离、锁队列与时空编码是数据库正确性的地基：名实错位的隔离级别会静默制造烂账，未设防的排他锁足以瞬间引爆全站读雪崩。唯有厘清读写依赖、拆解重锁粒度，并死守 `TIMESTAMPTZ` 与 `UTF-8`，方能守住数据底线。

## 一、事务契约、并发异常与分布式共识 {#isolation-and-consensus}

### MySQL 半成功事务错在哪，PG 怎样容错？ {#acid-atomicity-savepoint}

原子性的底线是全成或全败，而 MySQL 默认竟允许同一事务内前句成功、后句报错后照常提交“半成功中间态”，把平账责任甩给开发者纯属设计失职。合格的数据库必须像 PostgreSQL 一样默认在语句报错时立即中止整个事务；若客户端确需交互容错，开启 `psql` 的 `ON_ERROR_ROLLBACK` 借隐式 `SAVEPOINT` 自动回滚单条错句即可体面解决。

- [如何看待 MySQL vs PGSQL 直播闹剧 · 更新：MySQL 事务机制缺陷](/pg/mysql-pg-live-drama/#更新mysql-事务机制缺陷)
- [为什么PostgreSQL前途无量？ · ACID](/pg/pg-is-great/#acid)

### SQL 隔离级别如何名实错位，读已提交有何隐患？ {#isolation-levels-and-read-skew}

SQL-92 标称隔离级别严重名实错位：Oracle 的 `SERIALIZABLE` 与 PG 的 `REPEATABLE READ` 实为快照隔离（SI），而 InnoDB 的 `RR` 连单行丢失更新（P4）都拦不住。默认读已提交仅给语句级快照，并发“先读后写”必丢更新（须改 `SET v = v + 1`），跨行查询还会产生读偏差（A5A）毁掉备份与对账，必须改用事务级快照。

- [并发异常那些事 · 主流关系型数据库的实际隔离等级](/db/concurrent-control/#主流关系型数据库的实际隔离等级)
- [并发异常那些事 · 读偏差 A5A](/db/concurrent-control/#读偏差-a5a)
- [事务隔离等级注意事项 · 更新丢失（P4）](/pg/isolation-level/#更新丢失p4)

### 快照隔离为何漏掉写偏差，如何根治跨行并发异常？ {#write-skew-and-ssi}

快照隔离（SI）靠写冲突回滚根治了同行丢失更新，却对跨行写偏差（A5B / G2-item）失明：如两名值班员同时见两人在岗后各自改自己那行请假，因修改行不重叠便双双提交致空岗。根治跨行与反依赖环（G2）唯有两途：用 `SELECT FOR UPDATE` 悲观锁物化冲突，或开启 PG 的 `SERIALIZABLE`（SSI）追踪读写依赖环并配客户端幂等重试。

- [并发异常那些事 · 写偏差 A5B](/db/concurrent-control/#写偏差-a5b)
- [并发异常那些事 · 解决方案](/db/concurrent-control/#解决方案)
- [事务隔离等级注意事项 · Write Skew (G2-item)](/pg/isolation-level/#write-skew-g2-item)
- [事务隔离等级注意事项 · Anti-Dependency Cycles (G2)](/pg/isolation-level/#anti-dependency-cycles-g2)

### 一致性与 CAP 被误读多久，分布式为何靠共识？ {#consistency-cap-and-consensus}

ACID 的 C 指应用层业务不变量，而 CAP 的 C 是多副本如单副本的“线性一致性”。正如 Kleppmann 所言，CAP 脱离了现实延迟 SLA，当年走红纯属给 NoSQL 弱一致背书，工程更应关注“离线可用性”。分布式事务靠单点 2PC 即可保一致，引入 Raft/Paxos 共识是为了在协调者宕机时无分歧选主以解决可用性死穴。

- [一致性：过载的术语 · 总结一下](/db/consistency/#总结一下)
- [一致性：过载的术语 · 具体来讲](/db/consistency/#具体来讲)
- [重新设计数据密集型应用 · 重新审视 CAP 定理](/db/redesign-data-intensive-app/#重新审视-cap-定理)

### 形式化验证难落地，基础软件靠什么守住质量底线？ {#formal-verification-vs-battle-testing}

Kleppmann 与 Riccomini 道破了真相：TLA+ 九成价值在写规约倒逼暴露隐含假设时已兑现；确定性模拟测试（DST）虽能配合参考预言机校验 AI 代码，却困在“早期不值投、晚期用户报障比补测更快”（如 SlateDB）的悖论里。九成团队连备份切换演练都缺席，海量真实生产负载众测与快速闭环才是终极质量壁垒。

- [重新设计数据密集型应用 · 形式化证明与模型检查](/db/redesign-data-intensive-app/#形式化证明与模型检查)
- [重新设计数据密集型应用 · 三、测试与形式化方法——残酷的现实](/db/redesign-data-intensive-app/#三测试与形式化方法残酷的现实)

### 站在数据库内核视角，如何对区块链与智能合约祛魅？ {#blockchain-byzantine-wal}

剥去炒作外壳，区块链本质是带前序哈希指纹的预写式日志（WAL）：重放全量区块还原状态，“智能合约”即分布式库里的存储过程，“去中心化”是工作量共识的无主复制，“防篡改”靠哈希链算力成本实现拜占庭容错。其吞吐与查询能力远逊生产级数据库，防抵赖刚需又多属公权力地盘，盲目商用必沦为先烈。

- [区块链与分布式数据库](/db/blockchian/)

## 二、八级锁层次、DDL 阻塞链与线缆协议 {#locks-and-wire-protocol}

### 八级表锁如何演化，为何视图里查不到磁盘行锁？ {#table-locks-and-vxid}

PG 八级表锁是四步演化的最小完备集：加 `Access` 前缀解耦 MVCC 读写，加 `RowShare/RowExclusive` 意向锁协调行表冲突，再补 `ShareUpdateExclusive` 自斥锁让 `VACUUM` 与并发建索引既不挡读写又防双开互踩。`pg_locks` 查不到行锁，是因为行锁直接记在数据页元组头上，只读事务仅领本地虚拟号 `vxid` 省下 32 位 `txid`，等行锁表现为对持锁事务号申请 `ShareLock`。

- [PostgreSQL中的锁 · 表级锁的演化](/pg/pg-lock/#表级锁的演化)
- [PostgreSQL中的锁 · 样例数据](/pg/pg-lock/#样例数据)

### 毫秒级加空列为何引发雪崩，大表 DDL 怎么拆？ {#lock-queue-and-online-ddl}

高并发库执行毫秒级 `ADD COLUMN` 空列也足以引爆读雪崩：只要慢查询持 `AccessShare` 未退，申请 `AccessExclusive` 的 DDL 便入队等待，把后续所有普通 `SELECT` 拦死在门外。线上 DDL 必须严守两律：强制前置 `SET lock_timeout` 超时退避；将加默认值列与加主键拆为“长时弱锁回填或并发建索引 + 毫秒级强锁挂载”。

- [PostgreSQL中的锁 · 锁队列](/pg/pg-lock/#锁队列)
- [PostgreSQL中的锁 · 最小化锁阻塞时长](/pg/pg-lock/#最小化锁阻塞时长)

### 线缆协议如何定界，手写七层连接代理要注意什么？ {#wire-protocol-and-proxy}

PG v3 线缆协议边界极其规整：客户端发 `0x30000` 魔数的 `StartupMessage` 启动，认证与参数下发完毕后靠带事务状态的 `ReadyForQuery (Z)` 闭合握手与每次查询结果流。手写七层连接代理最易栽在 SSL 探测上：`psql` 建连常先发特殊探测包而非启动帧，若代理不卸载 TLS，必须先回写单字节 `'N'` 引导客户端降级重发真实启动包，再用 `pgproto3` 透传审计。

- [前后端通信线缆协议 · 启动阶段](/pg/wire-protocol/#启动阶段)
- [前后端通信线缆协议 · 连接代理](/pg/wire-protocol/#连接代理)

### 本地抓包为何不见明文，混杂与监控模式差在哪？ {#wireshark-capture-and-rfmon}

本地敲 `psql` 抓不到明文，是因为省略主机名默认走 Unix Socket 旁路网卡，走 TCP 又默认启用 SSL；须显式传 `-h localhost` 监听 `lo0` 并设 `sslmode=disable`，才能在 Wireshark 看到建连、查询与断连 5 组明文交互。无线抓非本机包则须分清网卡模式：混杂模式只能抓已关联 Wi-Fi 的局域网包，唯有启用射频监控模式（RFMON，如 `tcpdump -I`）外接网卡才能嗅探物理信道原始 802.11 帧。

- [Wireshark抓包分析协议 · 抓包样例](/pg/wireshark-capture/#抓包样例)
- [Wireshark抓包分析协议 · 题外话：使用Mac进行无线网络嗅探](/pg/wireshark-capture/#题外话使用mac进行无线网络嗅探)

## 三、时间纪元暗礁与字符编码基石 {#time-and-character-encoding}

### 闰秒与 2038 大限何来，存时间有哪些暗坑？ {#leap-seconds-2038-timestamptz}

地球自转变慢使天文时慢于原子钟，UTC 插入正闰秒造出 `23:59:60` 常致缺防护程序因时钟回拨崩溃；Unix 时间戳忽略闰秒死守每日 `86400` 秒，但 4 字节有符号整型（如 MySQL `TIMESTAMP`）将在 2038 年溢出。PG 用 8 字节微秒整型实现 `TIMESTAMPTZ` 跨度达 29 万年，但切忌 `::TIMESTAMP` 强转丢时区，更严禁向 `AT TIME ZONE` 传 `'+8'` 等数字串触发 POSIX 符号反转。

- [理解时间：闰年闰秒，时间与时区 · 协调世界时（UTC）](/db/reason-about-time/#协调世界时utc)
- [理解时间：闰年闰秒，时间与时区 · Unix 时间戳](/db/reason-about-time/#unix-时间戳)
- [理解时间：闰年闰秒，时间与时区 · 常见困惑：时区偏移量](/db/reason-about-time/#常见困惑时区偏移量)

### 为何 UTF-16 成包袱而 UTF-8 通吃？ {#utf8-vs-utf16-encoding}

早期 Java 与 Windows 选用的 UTF-16 误判 65536 码位够用，被汉字与 Emoji 撑破后打上“代理对”补丁沦为变长编码——既丢了随机下标访问，又背着大小端 BOM 与截断乱码包袱。反观 UTF-8 以单字节 `uint8` 为码元，根除端序歧义、全兼容 ASCII，且首字节与 `10xxxxxx` 续字节前缀绝不重叠，坏块丢字节后下一字符瞬间自同步，配合 Go 式 `byte/rune` 分离堪称终极通解。

- [理解字符编码原理 · 0x02 模型概览](/db/character-encoding/#0x02-模型概览)
- [理解字符编码原理 · UTF16](/db/character-encoding/#utf16)
- [理解字符编码原理 · 0x05 UTF-8](/db/character-encoding/#0x05-utf-8)
- [理解字符编码原理 · 0x06 编程语言中的字符编码](/db/character-encoding/#0x06-编程语言中的字符编码)
