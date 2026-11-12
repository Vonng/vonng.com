---
title: 开发规约、强类型主键建模与无锁在线改表
linkTitle: 开发规约与无锁改表
description: 沙箱自学飞轮、小写命名与 C.UTF-8 排序铁律、BIGINT/UUIDv7 选型及无锁改列。
weight: 240
icon: fa-solid fa-table-columns
---

糟糕的大小写命名、依赖 `glibc` 的脆弱排序与 32 位主键，是多年后逼停大表的罪魁祸首。死守小写命名、内置 `C.UTF-8` 排序与强类型规约，并掌握影子列无锁改表术，才能让核心库十年演进不债台高筑。

## 一、学习路径、命名秩序与核心开发规约 {#learning-and-conventions}

### 如何避开黑盒误区，用 AI 沙箱吃透现代 PG？ {#learn-pg-fast-flywheel}

学 PG 最忌干啃书本或在 Docker、云 RDS 黑盒里打转。正道是在廉价 Linux 虚拟机上用 Pigsty 十分钟拉起生产同构原生环境，请 Claude Code 驻场围着真实数据集大胆试错，搞砸了剧本两分钟重建或零空间克隆即可；再沿性能、可靠性、运维、开发与架构五条脉络亲手验证 PG 10 至今贡献近四成核心功能的历代新特性，方能练成肌肉记忆。

- [如何快速上手学习 PostgreSQL？ · 如何入门 PG？](/pg/learn-pg-fast/#如何入门-pg)
- [如何快速上手学习 PostgreSQL？ · 请老师登场](/pg/learn-pg-fast/#请老师登场)
- [快速掌握PostgreSQL版本新特性](/pg/pg-version-features/)

### 进阶独当一面的数据库大法师要打通哪三大支柱？ {#postgres-mage-pillars}

进阶“Postgres 大法师”必须贯通“生态洞察、内核级开发与确定性管理”三大支柱：宏观层看透扩展生态、向量与 DuckDB 融合及开源协议，用单一关系库收敛多模负载；中观开发吃透线缆协议、隔离异常、函数易变性、特种索引、排他约束与逻辑解码；底层管理闭环掌控黄金指标、连接池与复制拓扑、无锁改表、膨胀回卷治理乃至 `pg_filedump` 绝境抢救。

- [专栏：Postgres 大法师 · 生态](/pg/mage/#生态)
- [专栏：Postgres 大法师 · 开发](/pg/mage/#开发)

### 库内外对象如何命名，才能根除引号污染与路由混乱？ {#naming-convention-order}

混用大小写是 SQL 工程的万恶之源。库内表、列、索引与函数必须严控在 63 字节内的小写 `snake_case`，彻底杜绝双引号转义污染，严禁触碰保留字、`pg` 前缀、`xmin/ctid` 系统列名及默认 `public` 模式；库外集群则直接对齐合法 DNS 三段式（`pg-<biz>-<tld>`），搭配固定的 `primary`、`replica`、`offline` 服务后缀，令域名路由与监控标签天然自洽。

- [PostgreSQL 规约（2024版） · 0x01 命名规范](/pg/pg-convention/#0x01-命名规范)

### 服务端为何必锁 C.UTF-8 防索引静默腐坏？ {#collation-utf8-immutability}

依赖操作系统 `glibc` 排序规则是生产库头号暗雷：底层 OS 一升级导致字符序漂移，B-Tree 文本索引就会静默腐坏并击穿唯一约束。服务端必须锁死 `UTF8` 与 `C` / `C.UTF-8`，PG 17 新增的内置不可变 UTF-8 排序提供者更从内核层根除了跨平台漂移（同步带来 `JSON_TABLE` 与 `COPY ON_ERROR`）。国标 GB18030 靠客户端转码兼容即可，正如龙芯须先合入主流开源发行版才能进 PGDG 官方源。

- [PostgreSQL 17 发布：摊牌了，我不装了！ · 进一步丰富的开发者体验](/pg/pg-17/#进一步丰富的开发者体验)
- [PostgreSQL 17 beta1 发布！ · 开发者体验](/pg/pg-17-beta1/#开发者体验)
- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · 议题：关于对龙芯提供支持](/pg/pgcondev-2024/#议题关于对龙芯提供支持)

### 建表有哪些强类型铁律，为何严禁高频更新宽表？ {#table-design-mvcc-width}

建表须榨干强类型红利：优先用 `TIMESTAMPTZ`、`NUMERIC`、`JSONB` 等原生类型，禁用补空格且无性能优势的 `CHAR(n)`，自增列弃 `SERIAL` 改标准 `IDENTITY` 或有序 UUIDv7，且每表必配主键或唯一身份列支撑逻辑复制。因 MVCC 每次 `UPDATE` 都会整行复制新元组，超 15 列的宽表高频更新会引爆剧烈写放大与膨胀，必须按冷热属性共享主键纵向拆表。

- [PostgreSQL 规约（2024版） · 0x02 设计规范](/pg/pg-convention/#0x02-设计规范)
- [PostgreSQL开发规约（2018版） · 0x02 设计规范](/pg/pg-convention-2018/#0x02-设计规范)

## 二、主键发号、强类型建模与无锁在线改表 {#id-types-and-online-ddl}

### 主键为何禁用 32 位整型，雪花算法输在哪？ {#bigint-vs-snowflake}

32 位 `INTEGER` 上限仅 21 亿，遭遇高频冲突重试或 `UPSERT` 极易耗尽溢出导致全站停写，事后跨主外键改列代价惨重，故整数主外键必须一律用 64 位 `BIGINT`。而在分布式发号中，Twitter SnowflakeID 并非银弹：它既要依赖中心协调分配 10-bit 机器号，又对服务器物理时钟回拨毫无招架之力，时钟一旦回调几乎必然撞号造出脏数据。

- [故障档案：序列号消耗过快导致整型溢出 · 内因：类型使用不当](/pg/sequence-overflow/#内因类型使用不当)
- [UUID性质原理与应用 · SnowflakeID](/pg/uuid/#snowflakeid)

### 时序 UUID 强在哪，历史日志如何逆向补号？ {#uuid-v1-bit-backfill}

PG 内建紧凑的 16 字节 `uuid` 类型；相比全随机写爆缓存的 UUIDv4，UUID v1 将 60-bit 百纳秒时间戳低 32 位置顶，在 7.1 分钟窗内严格单调递增、跨窗均匀散列，并靠 14-bit `clock_seq` 抵御时钟回拨。针对通用库只能生成当前时刻 ID 的局限，利用 PG 定长位串（`BIT`）算子按 1582 年公历纪元偏移重排位域，十余行 PL/pgSQL 即可为历史日志逆向补齐合法 UUID v1。

- [UUID性质原理与应用 · UUID概览](/pg/uuid/#uuid概览)
- [UUID性质原理与应用 · 一些问题](/pg/uuid/#一些问题)

### 为何禁有符号整型存 IPv4，历史区划怎样回溯？ {#inet-and-temporal-adcode}

把本质为 `uint32` 的 IPv4 塞进有符号 `INTEGER` 会让超 `127.255.255.255` 的半数地址溢出变负数，彻底摧毁范围比较；正道是直接采用紧凑可读且自带子网算子的原生 `inet` 类型。同理在行政区划建模中，用编码五级层次的 12 位国标码作主表主键，将多源飞地拆入围栏子表，再配 `tstzrange` 有效时段列与多边形共建复合 GiST 索引，即可精准回溯任意历史时刻的归属区划。

- [GeoIP 地理逆查询优化 · 0x01 网络地址类型](/pg/geoip/#0x01-网络地址类型)
- [PostGIS高效解决行政区划归属查询 · 回溯支持](/pg/adcode-geodecode/#回溯支持)

### 为何改列常触发整表重写，不停机改列的机理是什么？ {#online-alter-column-lock-split}

查 `pg_cast` 中 `castmethod = 'b'` 可知，除 `varchar` 扩长或转 `text` 等少数二进制兼容转换外，`INT` 升 `BIGINT`、`FLOAT` 转 `DECIMAL` 或 `TEXT` 转 `JSONB` 均会持 `AccessExclusiveLock` 重写整表阻塞读写数小时，且带索引列必触发全量重建锁。不停机改列的核心是锁拆分：秒级加影子列、挂 `BEFORE` 触发器双写增量、低锁分批回填存量，最后在毫秒级排他锁事务内原子换名。

- [在线修改PG字段类型 · 常规操作](/pg/migrate-column-type/#常规操作)
- [在线修改PG字段类型 · 基本思路](/pg/migrate-column-type/#基本思路)

### 大表主键无锁升 64 位，如何均匀切片并防膨胀？ {#alter-pk-histogram-vacuum}

在线抢救 `INT` 主键大表时，先加 `BIGINT` 影子列与双写触发器，存量刷完并并发建好唯一索引后，仅在末尾毫秒级强锁事务内用 `PRIMARY KEY USING INDEX` 升格约束并换名。回填切忌固定步长硬切以免撞上数据倾斜，应直读 `pg_stats.histogram_bounds` 等频直方图边界配 `lead()` 生成均匀 `BETWEEN` 分片，并在每批后穿插 `pg_sleep` 与显式 `VACUUM` 原地复用死元组空间。

- [在线修改主键列类型 · 在线升级流程](/pg/alter-type/#在线升级流程)
- [在线修改主键列类型 · 批量更新逻辑](/pg/alter-type/#批量更新逻辑)
- [在线修改主键列类型 · 优化与改进](/pg/alter-type/#优化与改进)
