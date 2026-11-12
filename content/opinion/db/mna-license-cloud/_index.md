---
title: 硅谷十亿并购潮、协议定力与云收编博弈
linkTitle: 并购潮与开源协议
description: 数仓巨头吞噬 PG 创业公司、开源许可证变局、云厂商收编新阳谋与计算自由。
weight: 40
icon: fa-solid fa-chess-rook
---

PostgreSQL 赢下内核终局后，主战场已上移为数仓巨头与云寡头的收编博弈。分散版权护住了社区内核不被买断，但唯有全栈开源的自由发行版与本地优先退出权，才能打破云端账单刺客与圈养锁定。

## 一、十亿并购潮、巨头阳谋与发行版战争 {#mna-and-distro-war}

### 全球风投与云巨头财报为何把筹码全押在 PG 上？ {#capital-all-in-on-pg}

资本寒冬里，数据库赛道的聪明钱已被 PG 生态包揽。硅谷创业标准栈收敛为前端托管加 Neon/Supabase 托管 PG：Supabase 两轮 8000 万美元后再融两亿美元，与十亿美元级并购的 Neon 双双冲上十亿至二十亿美元估值。微软 CEO 纳德拉更在财报会点名 Azure PG 连续三季加速增长并覆盖近六成世界 500 强，宣告赛道终局。

- [PG生态赢得资本市场青睐：Databricks收购Neon，Supabase融资两亿美元，微软财报点名PG · 老冯评论](/pg/pg-capital-market/#老冯评论)
- [PG系创业公司Supabase：`$80M` C轮融资 · Supabase  B 轮/C 轮融资 `80M $`](/pg/supabase-series-c/#supabase--b-轮c-轮融资-80m-)

### 三大分析巨头为何斥重金吞噬独立 PG 初创公司？ {#why-olap-giants-buy-pg-startups}

AI 时代数据库已收敛为“服务端 PG 加嵌入式 SQLite/DuckDB”：短命小库下沉至嵌入式或秒级分支，多 Agent 共享状态的唯一事实源仍是 PG。面对“PG + DuckDB”合流直逼数仓腹地，三大巨头纷纷挥舞支票簿抢占入口：Databricks 十亿美元买下 Neon 后再收 Mooncake Lab，Snowflake 吞下 Crunchy Data，ClickHouse 收购 Xata。独立扩展 `pg_mooncake` 被招安后停更八个月，纯正开源 HTAP 的重担终落回官方 `pg_duckdb` 肩上。

- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · 尘埃落定](/pg/clickhouse-got-xata/#尘埃落定)
- [月饼好吃：又一家PG扩展公司被Databricks收购](/pg/databricks-buys-again/)

### ClickHouse 如何不动内核完成对 PG 的双向合围？ {#clickhouse-pg-symbiosis}

在“PG 扛在线事务加列存做实时分析”成标配后，精明巨头绝不对抗 PG，而是贴着扩展边界共生。ClickHouse 走出连环棋：先收 10 倍 CDC 提速的 PeerDB 卡住数据源入口；再用 `pg_clickhouse` 与 `pg_stat_ch` 插件咬合；最后左联 Ubicloud 托管长寿生产库，右收写时复制与缩容至零的 Xata 承接短命 Agent 小库，不改内核拼齐闭环。

- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · ClickHouse 的 PG 布局](/pg/clickhouse-got-xata/#clickhouse-的-pg-布局)
- [ClickHouse收购PeerDB：这浓眉大眼的也要来搞 PG 了？ · References](/pg/clickhouse-peerdb/#references)

### 巨头“买人不买项目、开放底层”打着什么阳谋算盘？ {#cloud-oligarchs-buying-maintainers}

云与数仓巨头已进化出两套精致阳谋：一是“开放一层、收费站上移一层”，如 Snowflake 斥资 1.645 亿美元买下 Crunchy Data 并开源 `pg_lake`，资助 PG 走 Iceberg 以锁定上层 Catalog 治理收费；二是“买人不买项目”，如 AWS 将 DuckDB 留给基金会却全员收编核心团队，保住 MIT 协议却瓦解多雇主制衡。如今近半 PG 核心贡献者领着云寡头薪水，云存储分层有人抢做，私有高可用与连接池却无人发薪。

- [Catalog Bullshit：把数据库拆开，再租给你一张 PostgreSQL 表 · 开放一层，收费站上移一层](/db/catalog-bullshit/#开放一层收费站上移一层)
- [AWS 收购 DuckDB：鸭子飞进亚马逊雨林 · 买人不买项目](/db/aws-get-duckdb/#买人不买项目)
- [是 Oracle 的失误让 PostgreSQL 赢了吗？ · 六、真正的考验不来自 Oracle，来自云](/db/thank-oracle/#六真正的考验不来自-oracle来自云)

### 内核归属社区买不走，下半场“发行版战争”争什么？ {#linux-kernel-distro-war}

全球数据库迁移已呈“万流归宗汇入 PG”之势，只剩错位避战或封装 PG 两条路。如 Linux 一统后竞争转向红帽与 Debian，社区宪法确保无人能私有化 PG 内核；独立 DBaaS 被并购后，战场转向人才争夺、发行版体验与账单控制面锁定。不烧风投、靠现金流把 Pigsty 做成 Supabase 官方推荐三大自建方案之一，单兵照样稳坐牌桌。

- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · 格局演变：发行版战争](/pg/clickhouse-got-xata/#格局演变发行版战争)
- [PostgreSQL 已主宰数据库世界 · 迁移图](/pg/so2025-pg/#迁移图)
- [StackOverflow 2024调研：PostgreSQL已经杀疯了 · 小结](/pg/pg-is-no1-again/#小结)
- [PG生态赢得资本市场青睐：Databricks收购Neon，Supabase融资两亿美元，微软财报点名PG · 老冯评论](/pg/pg-capital-market/#老冯评论)

## 二、开源许可证定力与商业博弈均衡 {#license-and-monetization}

### 为何 PG 永远卖不掉，也绝不会修改宽松开源协议？ {#will-pg-change-license}

PostgreSQL 免疫吞并与改证的护城河写在每个源文件头部：不同于 MySQL 集中版权打包易主，PG 从不签 CLA，版权分散在上千贡献者手中，法律上不存在能卖掉它或改证的主体。如核心组成员 Jonathan Katz 所言，加拿大中立组织、商标保卫战与多方制衡（含俄罗斯团队平等参与）锁死了类 BSD 定力，铸就全球及国产衍生库第一母体。

- [是 Oracle 的失误让 PostgreSQL 赢了吗？ · 三、真正的护城河，写在每个源文件的头部](/db/thank-oracle/#三真正的护城河写在每个源文件的头部)
- [PostgreSQL会修改开源许可证吗？ · PostgreSQL会修改开源许可证吗](/pg/pg-license/#postgresql会修改开源许可证吗)
- [如何看待 MySQL vs PGSQL 直播闹剧 · BSD 是流氓协议？？](/pg/mysql-pg-live-drama/#bsd-是流氓协议)
- [驳《MySQL：这个星球最成功的数据库》 · BSD 是流氓协议？？](/pg/rebut-mysql-best/#bsd-是流氓协议)

### 改协议防云白嫖，为何 Redis 遭反噬而 AGPL 成均衡？ {#redis-es-license-equilibrium}

MongoDB、ES 与 Redis 改签 SSPL，是被公有云白嫖再拉分叉贴牌“真开源”逼出的自卫，撕开了僵化 OSI 沦为云厂保护伞的虚伪。但如 Andy Pavlo 所析，Redis 架构较简、创始人隐退且含大量大厂代码，强改证即招致 Valkey（64.7% 喜爱度）与云降价 30% 反扑；Elastic 受夹击退回 AGPLv3，Supabase 因简陋自建跌至 47.2% 亦印证口碑铁律。

- [Redis不开源是“开源”之耻，更是公有云之耻 · 修改协议的开源软件](/db/redis-oss/#修改协议的开源软件)
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法](/db/pavlo-2024-review/#andy-的看法)
- [ElasticSearch又重新开源了？？？ · 老冯评论](/db/elasticsearch-reopen/#老冯评论)
- [PostgreSQL会修改开源许可证吗？ · 译者评论](/pg/pg-license/#译者评论)
- [PostgreSQL 已主宰数据库世界 · 喜爱度](/pg/so2025-pg/#喜爱度)

### 传染性协议真能防云吗，为何有人主张告别 GPL？ {#kleppmann-critique-of-copyleft}

从《DDIA》作者 Martin Kleppmann 的视角看，靠 AGPL 逼云巨头开放代码几乎落空：大厂只会绕道宽松替代品、重写或买授权，改证只是商业防卫而非护卫自由。且 GPL 只能逼企业应付式倾倒魔改代码，无法强制持续维护，反倒转嫁包袱并因协议不兼容割裂生态；他因此主张转向宽松协议，改靠实时数据互操作立法与公共采购制衡云锁定。

- [是时候和GPL说再见了 · 促进软件自由的法律工具](/db/goodbye-gpl/#促进软件自由的法律工具)
- [是时候和GPL说再见了 · GPL-家族许可证的其他问题](/db/goodbye-gpl/#gpl-家族许可证的其他问题)

### 为何从 AGPL 切回 Apache，不防白嫖怎么站着挣钱？ {#agpl-to-apache-stand-tall}

我在许可证上踩过真坑：AGPLv3 在基础软件两头不讨好——既触发法务红灯劝退打算自建的 OpenAI 团队，又拦不住云架构师替客户私有代部署白嫖。AI 赋予单兵数十倍杠杆后，真开源最大回报已是极端场景锤炼与口碑连接。将软件打磨至超云 RDS 的 90 分完成态用 Apache 2.0 免费送，靠质保契约与 100 分实战兜底才能“站着挣钱”。

- [从AGPL到Apache：Pigsty 协议变更的思考 · AGPLv3 的糟糕实践](/pg/pigsty-relicense/#agplv3-的糟糕实践)
- [从AGPL到Apache：Pigsty 协议变更的思考 · 商业模式：站着挣钱](/pg/pigsty-relicense/#商业模式站着挣钱)
- [从AGPL到Apache：Pigsty 协议变更的思考 · 那为什么不用 ELv2 / SSPL / BSL？](/pg/pigsty-relicense/#那为什么不用-elv2--sspl--bsl)

## 三、云账单刺客、供应链主权与计算自由 {#cloud-sovereignty-and-freedom}

### 公有云专有 PG 与托管 RDS 藏着多大的溢价陷阱？ {#cloud-rds-markup-and-lockin}

算笔硬账：AWS 宁夏区 96 核 NVMe 裸金属年租仅 11 万～15 万元（自购五年托管不到 10 万），对标托管 RDS 年费却高达 286.7 万元，溢价近 20 倍！如 Percona 警示，云巨头正借 AlloyDB 内存与 Aurora I/O 计费刺客重演锁定剧本，某平台下云后月支出直接砍半；几分钟扩容的小甜头远抵不上丧失主权与团队退化的代价。

- [PostgreSQL 到底有多强？ · 关于成本](/pg/pg-performence/#关于成本)
- [为什么PostgreSQL前途无量？ · vs 云数据库](/pg/pg-is-great/#vs-云数据库)
- [PostgreSQL主宰数据库世界，而谁来吞噬PG？ · MongoDB 能告诉我们 PostgreSQL 将走向何方吗？](/pg/proprity-pg/#mongodb-能告诉我们-postgresql-将走向何方吗)
- [PostgreSQL主宰数据库世界，而谁来吞噬PG？ · 成本波动难以预测](/pg/proprity-pg/#成本波动难以预测)

### “云吞噬开源”断了什么活水，为何本地优先重于源码？ {#cloud-eats-oss-and-local-first}

纯血开源靠“免费采用—催生甲方专家岗—产消合一者回馈”分摊成本；但公有云把每核每月 20 元裸金属套上闭源管控卖到 300～1300 元，独吞暴利并消灭甲方开源岗，掐断社区活水。如我与 Kleppmann 所强调，计算自由头号敌人已是云端 PaaS/SaaS：本地闭源软件在原厂倒闭后仍能跑副本导数据，锁在云上一旦封号断供便净身出户，“本地优先”重于源码。

- [Redis不开源是“开源”之耻，更是公有云之耻 · 软件行业的范式转移](/db/redis-oss/#软件行业的范式转移)
- [Redis不开源是“开源”之耻，更是公有云之耻 · 计算自由的头号敌人](/db/redis-oss/#计算自由的头号敌人)
- [是时候和GPL说再见了 · 敌人变了](/db/goodbye-gpl/#敌人变了)

### 编译围墙易破且上游难改证，如何防被云寡头圈养？ {#exit-right-free-distro-defense}

云巨头写代码办大会堪称模范，却把数十亿营收锁进 Aurora 闭源壳；独立厂商想把 Rust 扩展或 OrioleDB 藏在编译门槛后防自建，但社区打齐十大 Linux 安装包便一捅即破。面对“只想把你养熟”的寡头，公有云按小时收钱的本是高可用、备份、监控与连接池等外围管控，唯一对冲是在下游做对标 Debian 的自由发行版（如 Pigsty），守住自建退出权。

- [是 Oracle 的失误让 PostgreSQL 赢了吗？ · 结语：新时代的敌人](/db/thank-oracle/#结语新时代的敌人)
- [Andy Pavlo：2025 数据库世界年度总结 · 一、PostgreSQL 赢了，然后呢？](/db/db-in-2025/#一postgresql-赢了然后呢)
- [开放数据标准：Postgres，OTel，与Iceberg · 关于开源](/db/open-data-standard/#关于开源)

### 反击云垄断靠什么武器，云与开源终局走向何方？ {#rebel-alliance-and-power-grid}

反击云垄断最致命的武器是组建“反叛军联盟”拼生产力——用 K8s/Proxmox、Silo/Ceph 与 Pigsty 全栈开源平替暴利的 EC2、S3 和 RDS 管控层，维护者亦须靠订阅光明正大造血。以电力史推演终局：算力存储是电，云软件是家电——没人接受冰箱必须锁在发电站按月租用；底层 IaaS 终将微利公用事业化，暴利云软件必在本地优先冲击下剥离溢价。

- [Redis不开源是“开源”之耻，更是公有云之耻 · 法律工具与集体行动](/db/redis-oss/#法律工具与集体行动)
- [Redis不开源是“开源”之耻，更是公有云之耻 · 博弈均衡会走向哪里](/db/redis-oss/#博弈均衡会走向哪里)

### PGDG 镜像断流暴露了什么软件供应链命门？ {#pgdg-mirror-supply-chain}

“开源无断供”只对源码成立，日烧 10TB 带宽的二进制仓库并无免费兜底义务。2025 年 PGDG 迁海外 CDN 并关停同步，致国内镜像停更数月、补丁断流；云大厂失联，两三百家白嫖公共源的套壳“国产库”无一兜底，证明花架子 Fork 防不住供应链卡脖子。我借 AI 两小时搭起国内免费 CDN 镜像——比开源更稀缺的是不推诿的交付信任。

- [从PG“断供”看软件供应链中的信任问题 · 供应链风险](/pg/pg-mirror-pigsty/#供应链风险)
- [卡脖子：PGDG切断镜像站同步通道](/pg/pg-mirror-break/)
- [从PG“断供”看软件供应链中的信任问题 · 如何解决供应链风险？](/pg/pg-mirror-pigsty/#如何解决供应链风险)
- [从PG“断供”看软件供应链中的信任问题 · 我行我上](/pg/pg-mirror-pigsty/#我行我上)

### 龙芯跑通内核四年后，为何进官方仓库才算真能用？ {#loong64-official-apt-repo}

龙芯早在 2022 年靠 1 KB 补丁编通 PG 内核，但生产最怕“自己编译”——后续小版本更新与数百扩展构建矩阵才是运维黑洞，原版包缺位更让套壳库浑水摸鱼。凭高质量补丁、555 扩展仓库实绩与寄送构建主板攒够信任后，`loong64` 终入 Debian 与 PGDG 官方仓库共享签名流水线，两条 `apt install` 即从“能跑”跃升至“能维护”。

- [龙芯，正式进入 PostgreSQL 官方仓库 · 卡住的，不是 PostgreSQL 内核](/pg/pg-apt-loong64/#卡住的不是-postgresql-内核)
- [龙芯，正式进入 PostgreSQL 官方仓库 · 从“能跑”，到“能维护”](/pg/pg-apt-loong64/#从能跑到能维护)
- [龙芯，正式进入 PostgreSQL 官方仓库 · 在全球开源生态里发挥影响力](/pg/pg-apt-loong64/#在全球开源生态里发挥影响力)
