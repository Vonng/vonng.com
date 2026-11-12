---
title: 物理备份 PITR、瞬间克隆、删库急救与逻辑复制
linkTitle: 备份克隆与逻辑复制
description: pgBackRest 冷备防线、写时复制亚秒克隆、5TB 误删库抢救铁律与逻辑解码槽机理。
weight: 180
icon: fa-solid fa-clock-rotate-left
---

高可用热备只防机器暴毙，唯有异机物理冷备、PITR 与延迟温备才能兜住人为误删。借助现代文件系统的写时复制与逻辑解码流，大库亚秒级克隆与异构数据实时同步皆可原生闭环。

## 一、物理备份 PITR 与 CoW 瞬间克隆 {#backup-pitr-and-clone}

### 逻辑转储与 PITR 边界在哪，时间线有何深意？ {#backup-overview-pitr-timeline}

`pg_dump` 无锁导出单库快照，全局角色与表空间靠 `pg_dumpall` 补齐，恢复须从纯净 `template0` 建库并开 `ON_ERROR_STOP=on`。物理热备本质即持续重放的 `pg_basebackup`，PITR 靠基备加 16MB WAL 重放回拨至任意秒；每次恢复晋升都会递增 24 位 WAL 名首 8 位 Timeline ID 隔离新分支，防覆写历史归档并留足切回原分支的后悔药。

- [备份恢复手段概览 · 1.3 全局转储](/pg/backup-overview/#13-全局转储)
- [备份恢复手段概览 · 使用WAL归档追赶进度](/pg/backup-overview/#使用wal归档追赶进度)
- [备份恢复手段概览 · 3.7 时间线](/pg/backup-overview/#37-时间线)
- [备份恢复手段概览 · 启动从库](/pg/backup-overview/#启动从库)

### 有了高可用热备，为何仍需延迟温备与流式归档？ {#warm-standby-and-pg-receivewal}

一主多从毫秒级同步拦不住一条误敲的 `DROP TABLE` 全军覆没。专配一台不接客的延迟温备，既能在窗口期直接捞回旧数反灌主库，又在持续重放中自动验证备份可恢复性；归档侧用流式 `pg_receivewal` 替代写满 16MB 才触发的 `archive_command`，配同步提交即可实现 `RPO = 0` 归档。

- [温备：使用pg_receivewal · 温备方案](/pg/backup-plan/#温备方案)
- [温备：使用pg_receivewal · 日志归档](/pg/backup-plan/#日志归档)

### pgBackRest 如何跑满吞吐并揪出坏块？ {#pgbackrest-engine-and-stanza}

传统 `tar/rsync` 卡死单核且时间戳增量易漏拷。pgBackRest 凭多核并行流式压缩，实测 40 进程不到 10 分钟便将 341.5GB 库压至 153.6GB 落盘，千兆网跑出每小时 TB 级吞吐；传输同步校验页面 Checksum 揪出磁盘静默坏块，末步才写 `pg_control` 防拉起半成品并支持 `--delta` 差量恢复。高写主库只需开启 `archive-async=y` 异步推 WAL 即可防爆盘。

- [PgBackRest2中文文档 · 0. 特性](/pg/pgbackrest/#0-特性)
- [PgBackRest2中文文档 · 4.7 创建存储单元](/pg/pgbackrest/#47-创建存储单元)

### 备份工具历经停更续命，生产为何切忌慌忙跳车？ {#pgbackrest-supply-chain-and-stay}

备份软件握有全量生产库最高权限，是供应链投毒的头号目标——原作者 David Steele 归档 pgBackRest 时严令 Fork 必须改名，正是倒逼用户重做安全审计。生产切忌盲目跳车：Barman 云块增量尚嫩，WAL-G 缺仓库治理，`pg_probackup` 更有过恢复丢数坏页前科（Issue #474、#249）。如今主线已顺利续命且在 PG 18 上稳如磐石，按兵不动就是最优解。

- [顶级开源备份工具 pgBackRest 停止维护 · 大家在讨论什么](/pg/pgbackrest-archive/#大家在讨论什么)
- [顶级开源备份工具 pgBackRest 停止维护 · 不要着急忙慌的跳车](/pg/pgbackrest-archive/#不要着急忙慌的跳车)
- [pgBackRest 续命战与开源世界的逼定价 · 给用户的建议](/pg/pgbackrest-resume/#给用户的建议)

### 自建环境如何亚秒级零空间克隆 TB 级大库？ {#cow-reflink-instant-clone}

无需绑定专有云存储，只要 Linux 数据盘采用支持 reflink 写时复制的现代文件系统（XFS、Btrfs、ZFS）并开启 PG 18 原生 `file_copy_method = clone`，内核便经 `FICLONE` 仅拷元数据指针——实测克隆 120GB 库仅 200ms、797GB 库仅 569ms 且初始零额外占盘。将模板库闪断压进 200ms 并走纯 SQL 触发，即可让十几个 AI Agent 零成本并发秒拉真实沙盒。

- [Git for Data: 瞬间克隆PG数据库 · 写时复制：为什么能这么快？](/pg/pg-clone/#写时复制为什么能这么快)
- [Git for Data: 瞬间克隆PG数据库 · 关键限制：模板库不能有连接](/pg/pg-clone/#关键限制模板库不能有连接)
- [瞬间克隆 PostgreSQL 数据库，无需黑魔法 · 一些改进](/pg/pg-pig-clone/#一些改进)

### 实例级 Fork 如何零闪断救误删并赋能智能体？ {#instance-fork-pitr-and-agent-cli}

若主库不容忍 200ms 闪断或未升 PG 18，可在 XFS 盘上用 `pg_backup_start/stop` 包裹 `cp --reflink=auto` 执行实例级 `pig pg fork`，零中断秒拉独立影子实例；遇局部误删先在影子实例跑增量 PITR 核验捞数，彻底杜绝盲动主库引发二次事故。面向智能体的运维 CLI 更须内建 `--plan` 风险预演，且全链路输出 JSON/YAML 结构化自描述信息。

- [Git for Data: 瞬间克隆PG数据库 · 实例级克隆：pg-fork](/pg/pg-clone/#实例级克隆pg-fork)
- [瞬间克隆 PostgreSQL 数据库，无需黑魔法 · 实例级 Fork](/pg/pg-pig-clone/#实例级-fork)
- [瞬间克隆 PostgreSQL 数据库，无需黑魔法 · Agent Native CLI](/pg/pg-pig-clone/#agent-native-cli)

### 将 PG 挂载为文件系统适合什么业务场景？ {#pgfs-boundary}

拿数据库充当 POSIX 文件系统挂载（PGFS）是以吞吐折损换跨介质强一致恢复的“穷人工程学”，绝非替代高吞吐文件存储。普通 SSD 单线程实测大文件写约 178.5 MiB/s、读约 31.7 MiB/s，小文件读达 545 files/s——承载 ERP 单据附件等低频中小文件绰绰有余，免去双栈运维即可白嫖 ACID 事务、流复制热备与 PITR 秒级恢复保护。

- [PGFS：将数据库作为文件系统 · 性能表现如何？](/pg/pgfs/#性能表现如何)

## 二、删库急救铁律与主机安全基线 {#disaster-recovery-and-security}

### 为何单盘删光数据库与备份是神仙难救的死局？ {#same-disk-xfs-unrecoverable}

别拿应用内置单机库赌命：当 GitLab 掉电误跑 `pg_resetwal` 或云 RDS 翻车只赔 20% 代金券时，唯有内核老手能用 `pg_filedump` 硬掏残骸。但前提是底层文件尚存——一旦在单机 NVMe + XFS 上把库与本地备份同盘删光，文件系统便渣都不剩，天价块拼图远不如事前搭台异机冷备。

- [这次数据库真爆炸了，但摇人也没用了](/db/database-really-exploded/)
- [数据库爆炸了怎么摇人？](/db/db-emergency-help/)
- [如何用 pg_filedump 抢救数据？ · 后记](/pg/pg-filedump/#后记)

### 为何企业宁花几十万抢救，也不事前搭好备份？ {#bianque-preventive-economics}

单机无备份裸奔没炸只是赌赢了轮盘赌；哪怕跑 PolarDB 分支，用开源 Pigsty 配齐高可用与 PITR 也分文不取。可惜如扁鹊长兄治未病赚不到钱，事前防线毫无戏剧性；其实一次紧急摇人的机票退改签费就够买场事前架构问诊，几千块前置投入性价比碾压事后几十万抢救两个数量级。

- [删库 5 TB · 扁鹊的大哥赚不到钱](/db/drop-5tb-polardb/#扁鹊的大哥赚不到钱)
- [这次数据库真爆炸了，但摇人也没用了](/db/database-really-exploded/)
- [数据库爆炸了怎么摇人？](/db/db-emergency-help/)

### 生产库爆炸的黄金抢救期，管理层最忌讳什么？ {#golden-window-escalation}

无备份误删后的头 48 小时黄金窗口最常死于内部扯皮：管理层应激下忙着讨价还价走流程，却无视停产造成的千万级次生失血。躺在救护车上砍绷带价是致命愚蠢——企业缺的不是几万块抢救费，而是分钟级拍板预算的事故升级预案；更须切记救援专家只是最后止血钳，绝不能代替日常灾备。

- [删库 5 TB · 止血的时候，别跟人砍绷带的价](/db/drop-5tb-polardb/#止血的时候别跟人砍绷带的价)

### 基础软件越新越安全吗，主机高危漏洞怎么修？ {#cve-regression-patch-baseline}

切忌迷信版本越新越安全：`CVE-2024-6387` 信号竞争漏洞因代码回归精准击穿了 Rocky 9.3、Ubuntu 22.04 与 Debian 12 等主流新系统，反倒让 CentOS 7.9 与 Debian 11 等老系统幸免。治理主机漏洞须按精确包版本核查暴露面，直接用系统包管理器升级官方后向移植补丁并平滑重启 `sshd`，同步固化进离线软件源基线即可。

- [CVE-2024-6387 SSH漏洞修复 · 诊断方法](/db/cve-2024-6387/#诊断方法)
- [CVE-2024-6387 SSH漏洞修复 · 处理方法](/db/cve-2024-6387/#处理方法)

## 三、逻辑复制与流式 CDC 机理 {#logical-replication-and-cdc}

### 流式 CDC 为何能收编异构库，靠哪四块基石？ {#cdc-vs-etl-and-four-pillars}

应用双写异构库必陷不一致泥潭，流式 CDC 将 PG 立为唯一写入源，把缓存与数仓收编为按序重放的逻辑从库。PG 靠逻辑解码语义翻译、`pg_export_snapshot` 一致快照、流复制推送与复制槽持久化 LSN 四大基石原生闭环；正因快照与槽同步门槛极高，深耕 PG CDC 的 PeerDB 才获 ClickHouse 并购。

- [CDC 变更数据捕获机理 · CDC与ETL](/pg/logical-decoding/#cdc与etl)
- [CDC 变更数据捕获机理 · 逻辑复制](/pg/logical-decoding/#逻辑复制)
- [ClickHouse收购PeerDB：这浓眉大眼的也要来搞 PG 了？ · References](/pg/clickhouse-peerdb/#references)

### 逻辑解码有何妙用，生产上须兜底哪四大盲区？ {#logical-decoding-plugins-and-pitfalls}

逻辑解码仅输出已提交事务，`decoder_raw` 还能反向生成 SQL 破解迁移切写后无法回滚的死穴。但生产须防四大盲区：不含 DDL、序列与大对象；插件过滤事务边界消息会在清闲库同步提交下卡死主库；崩溃重连“至少一次”投递需消费端幂等；旧版切主丢逻辑槽须备妥迁槽预案。

- [CDC 变更数据捕获机理 · 逻辑解码输出插件](/pg/logical-decoding/#逻辑解码输出插件)
- [CDC 变更数据捕获机理 · 完备性](/pg/logical-decoding/#完备性)
- [CDC 变更数据捕获机理 · 同步提交](/pg/logical-decoding/#同步提交)
- [CDC 变更数据捕获机理 · 故障切换](/pg/logical-decoding/#故障切换)

### 复制标识有何约束，换索引与开 FULL 有何坑？ {#replica-identity-traps}

逻辑复制删改须靠复制标识唯一定位旧行：唯有主键 `DEFAULT` 与全列严格非空的唯一索引配 `USING INDEX` 高效可用，含可空列的普通唯一索引一律因空值无法判等作废。运维严防两颗雷：一是 `USING INDEX` 强绑物理索引对象，建新删旧漏在同一事务重刷会静默退化为 `nothing` 令删改报错（应改用 `REINDEX INDEX CONCURRENTLY`）；二是无主键大表开 `FULL` 会逼订阅端逐行全表扫描将其拖死。

- [PG复制标识详解（Replica Identity） · 复制标识详解](/pg/replica-identity/#复制标识详解)
- [PG复制标识详解（Replica Identity） · 重建唯一索引](/pg/replica-identity/#重建唯一索引)
- [PG复制标识详解（Replica Identity） · 使用FULL复制标识](/pg/replica-identity/#使用full复制标识)

### 逻辑复制如何追快照，改表与切流守什么铁律？ {#logical-rep-statemachine-ddl-seq}

新表先由 Sync Worker 拷快照追增量，就绪后交全局 Apply Worker 重放；大库初同步须防多临时槽撑爆源库 WAL。日常与割接死守两条铁律：切流前必须手工把下游序列推高至 `max(id)` 之上防主键冲突；在线改表严格遵循“加列先下游后上游、删表先上游后下游”顺序。

- [PostgreSQL 逻辑复制详解 · 逻辑复制状态机](/pg/logical-replication/#逻辑复制状态机)
- [PostgreSQL 逻辑复制详解 · 局限性](/pg/logical-replication/#局限性)
- [PostgreSQL 逻辑复制详解 · 两端列定义不一致](/pg/logical-replication/#两端列定义不一致)

### 撞上复制冲突或源端失联，如何解围防爆盘？ {#logical-rep-conflict-and-slots}

撞上唯一约束违背或缺列时，下游重放进程会以 5 秒周期无限重启报错，须联动排查下游日志与上游积压位点，修平冲突数据或调 `pg_replication_origin_advance()` 跳过问题事务。两类边界禁靠订阅自动管槽：同实例自复制须先手工建槽再设 `create_slot = false` 防死锁；远端失联急删订阅须先置空 `slot_name` 解绑，并在远端恢复后立即清理孤儿槽防撑爆磁盘。

- [PostgreSQL 逻辑复制详解 · 复制冲突](/pg/logical-replication/#复制冲突)
- [PostgreSQL 逻辑复制详解 · 管理复制槽](/pg/logical-replication/#管理复制槽)

### PG 17 补齐了哪些逻辑复制短板以逼近零停机？ {#pg17-logical-failover-and-upgrade}

正如核心组成员 Jonathan Katz 所总结，严苛业务已转向追求“1 秒停机上限”。在 PG 17 前，跨版本 `pg_upgrade` 或高可用切主都会令逻辑槽作废，逼下游重刷 TB 级数据；PG 17 一举打通了原地升级保留逻辑槽、Failover Slot 主从同步以及将物理从库秒转逻辑订阅端的 `pg_createsubscriber`，配合原生块级增量备份彻底拼齐零停机升级闭环。

- [展望 PostgreSQL 的2024 · 逻辑复制是如何助益于双主，蓝绿部署，零停机升级，以及其他工作流的](/pg/pg-in-2024/#逻辑复制是如何助益于双主蓝绿部署零停机升级以及其他工作流的)
- [PostgreSQL 17 发布：摊牌了，我不装了！ · 针对高可用与大版本升级的逻辑复制改进](/pg/pg-17/#针对高可用与大版本升级的逻辑复制改进)
- [PostgreSQL 17 beta1 发布！ · 分区和分布式工作负载增强](/pg/pg-17-beta1/#分区和分布式工作负载增强)
