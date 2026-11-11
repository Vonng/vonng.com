---
title: 扩展生态与发行版哲学
linkTitle: 扩展生态与发行版
description: 超 500 个扩展的天花板与包管理器 pig、向量/OLAP/时空/存储引擎革新、开源接盘侠与 PostgreSQL 发行版哲学。
weight: 20
icon: fa-solid fa-puzzle-piece
---

PostgreSQL 能以三十岁高龄吞噬数据库世界，底牌在于“保守内核守住可靠底线、激进扩展开疆拓土”的双层演化架构。但当公有云 RDS 阉割灵魂插件、官方源排斥新兴 Rust 生态、资本并购导致明星项目断粮时，唯有打通超 500 个扩展的跨平台二进制供应链（`pig` 与 `PGEXT`），并用内核可插拔的开源“元发行版”把自治运维主权交还用户，才能释放 PG 的全部潜能。本篇凝练 56 篇文章、124 条工程判断，拆解发行版哲学、扩展交付革命、向量与检索、OLAP 与时序、多模武器库及开源供应链续命之道。

## 一、可扩展性魔法与发行版哲学 {#distro-philosophy}

### 可扩展性为何是 PG 吞噬数据库世界的魔法？ {#why-extensibility-eats-db-world}

PostgreSQL 拥有犹太经典“托拉与塔木德”式的双层结构：内核如《托拉》般克制以死守可靠性，数百个扩展如《塔木德》般敏捷回应新命题，叠加“无主公共品”治理消除了私有化顾虑。正如 Ajay Kulkarni 所言，2011 年落地的 Extension 体系免除了中心化协调。它具备双重乘数效应：一是底座复用，两千行 `pgvector` 免费继承百万行内核的 ACID、PITR 与流复制；二是正交组合，PostGIS、TimescaleDB、ParadeDB 与 Citus 叠加产生 `1+1>>2` 的化学反应。探探 250 万 TPS、200TB 数据的实战证明，用单一 PG 替代多套专用库正是削减系统复杂度的最优解。

- [PostgreSQL，三十而立 · 五、托拉与塔木德](/pg/pg-turns-30/#五托拉与塔木德)：剖析保守内核与激进扩展互为表里的双层演化结构，以及“无主公共品”治理消除商业私有化顾虑的机制。
- [为什么PostgreSQL是未来数据库的事实标准？ · PostgreSQL 已经成为一个平台](/pg/pg-for-everything/#postgresql-已经成为一个平台)：梳理 2011 年 Extension 体系如何免除中心化内核协调，吸收地理、时序、图与向量能力使 PG 升维为统一数据平台。
- [PostgreSQL 正在吞噬数据库世界 · 极致可扩展性的魔法](/pg/pg-eat-db-world/#极致可扩展性的魔法)：拆解两千行 `pgvector` 复用百万行内核基建与多扩展正交组合产生指数级化学反应的底层机理。
- [PostgreSQL：最成功的数据库 · 先进之才](/pg/pg-is-no1/#先进之才)：结合探探 250 万 TPS、200TB 核心集群兼任缓存、分析与队列的实战，论证单一 PG 选型如何克制过早优化的架构膨胀。

### 单机编译就能跑，生产为何仍需 PG 发行版？ {#why-pg-needs-a-distro}

单机 `postgres` 进程 `initdb` 后只能算裸发动机，而企业生产要交付的是整车：主库挂了谁接管、坏备份谁发现、误删怎么做秒级 PITR、连接池如何切流、参数漂移怎么拉回。当 OLTP 内核之争尘埃落定，价值高地已转向“数据库发行版”——做 BaaS 发行版的 Supabase 五年估值 50 亿美元，反超深耕内核二十年的 EDB（10～20 亿美元）数倍。静态选型与脚本皆可模仿，唯独背后透明可审计、CVE 爆发即刻修补、五年后仍在场兜底的“开放信任供应链”抄不走，这与把用户锁进黑盒的云 RDS 托管信任截然不同。

- [什么是 PostgreSQL 发行版？ · 二、搬到 PostgreSQL：相似，但不相同](/pg/what-is-pg-distro/#二搬到-postgresql相似但不相同)：厘清裸内核进程与高可靠生产数据服务之间的工业化鸿沟，界定发行版整合工程决策与长期信用的核心使命。
- [立足中国，面向全球的 PostgreSQL 发行版 · 数据库发行版大战拉开序幕](/pg/forge-a-pg-distro/#数据库发行版大战拉开序幕)：对比新锐发行版 Supabase 50 亿美元估值与传统内核商 EDB 的差距，揭示“内核称王、发行版争霸”的产业拐点。
- [PostgreSQL：最成功的数据库 · 展望未来](/pg/pg-is-no1/#展望未来)：阐明数据库竞争重心如何从单纯 Software 转向整车级 Software-enabled Service，开启数据库界的 Debian 与 Ubuntu 之争。
- [什么是 PostgreSQL 发行版？ · 尾声：发行版是一条信任的供应链](/pg/what-is-pg-distro/#尾声发行版是一条信任的供应链)：对比云 RDS 黑盒“托管信任”与开源发行版可审计、可随时接管的“开放信任供应链”，点明长期社区信用才是终极壁垒。

### 只给打补丁软件包的发行版为何平替不了 RDS？ {#orchestration-and-observability}

在发行版“选型、打包、编排管控”三层中，选型已收敛至 Patroni、pgBackRest 与 Prometheus，打包有 PGDG 托底，唯独把静态包变成自愈活系统的“编排管控”无公地可躺。Percona 虽贡献了 `pg_tde`，但只丢几个裸包离替代 RDS 差着十万八千里——必须靠一键 IaC 剧本与本地离线源同时斩断云、网络与专家三重锁定。此外，云 RDS 默认的十几个图表只是判死活的“血氧计”，生产监控需深入库表索引采集 1155 类指标做“核磁共振”，乃至由内核后台进程直读共享内存暴露 HTTP 指标，消除外置 `pg_exporter` 在崩溃恢复拒连时的盲区。

- [什么是 PostgreSQL 发行版？ · 3. 编排与管控：把静态包变成活系统](/pg/what-is-pg-distro/#3-编排与管控把静态包变成活系统)：拆解发行版三层架构，指出打通故障自愈切换、副本补齐与防状态漂移的编排管控层才是追平 RDS 体验的决胜场。
- [PostgreSQL主宰数据库世界，而谁来吞噬PG？ · Percona 发行版](/pg/proprity-pg/#percona-发行版)：剖析仅提供打补丁二进制包的传统形态局限，论证离线软件源与自动化 IaC 剧本对于摆脱云、网络及专家锁定的必要性。
- [开箱即用的PG发行版：Pigsty · 全面专业的监控系统](/pg/pigsty-intro/#全面专业的监控系统)：对比云监控粗浅的生命体征面板，展示覆盖 1155 类库表索引指标的 Prometheus + Grafana 诊断级可观测体系。
- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · 第三天：Unconference](/pg/pgcondev-2024/#第三天unconference)：剖析外置探针在实例崩溃恢复期的失明缺陷，提出通过内核后台进程直读共享内存原生导出 Prometheus 指标的演进路线。

### 如何不套容器黑盒，在裸机与沙箱交付自愈集群？ {#iac-sandbox-and-datalet}

生产落地绝不能止步于手动 `yum install` 裸跑实例。采用声明式配置清单与幂等 Ansible 剧本，仅凭 SSH 无 Agent 模式即可纳管千台节点，底层串联 DCS、Patroni 与内置 HAProxy，实现主库故障秒级自愈切换且只读流量零中断，10 分钟拉高生产下限。为弥合研发与运维割裂，提供与线上完全同构的单节点及四节点本地虚拟机沙箱，三行命令即可在笔记本上演练切换并获取实时 SQL 监控反馈；而预打通的 PG + Grafana + ECharts 底座更可充当低代码数据应用引擎（Datalet），免前后端胶水代码直接交付日志挖掘与时空大屏。

- [开源PG全家桶上手指南 · 谁会感兴趣？](/pg/pg-stack-guide/#谁会感兴趣)：论证为何必须将专业监控、高可用管控与 PostGIS/TimescaleDB 分析能力打包成一条龙全家桶以抬升生产下限。
- [开箱即用的PG发行版：Pigsty · 稳定可靠的部署方案](/pg/pigsty-intro/#稳定可靠的部署方案)：详解声明式配置与无 Agent 幂等剧本如何串联 Patroni 与 HAProxy，交付节点对等、秒级自愈的高可用集群。
- [开源PG全家桶上手指南 · 相关分享](/pg/pg-stack-guide/#相关分享)：介绍与生产架构完全一致的本地多节点虚拟机沙箱，帮助开发者在个人电脑上演练故障切换并获得即时性能反馈。
- [开箱即用的PG发行版：Pigsty · 灵活开放的扩展机制](/pg/pigsty-intro/#灵活开放的扩展机制)：展示 PostgreSQL 结合 Grafana 与 ECharts 构建可分发低代码数据小应用（Datalet）的跨界生产力。

### 什么是“元发行版”，如何赋权十余种异构内核？ {#what-is-meta-distribution}

面对 OrioleDB、Babelfish、IvorySQL、OpenHalo 与 Cloudberry 等修改内核的 PG 家族亚种，为每颗内核重造运维轮子纯属浪费。将底层控制平面与特定内核解耦，即可升维成“元发行版（Meta Distribution）”——内核可插拔，平台能力不变，切换内核只需换一份包与一行 `./configure -c` 模板。在巨头并购圈地潮下，Pigsty 一边将跨 16 个 Linux 发行版的近 600 个扩展开放给全行业，一边把十余种开源内核接入同一套高可用、PITR 与监控底座，一条命令平替高价低能的云 DBaaS，死守本地优先防线使生态垄断无法得逞。

- [什么是 PostgreSQL 发行版？ · 五、再往前一步：Meta Distribution](/pg/what-is-pg-distro/#五再往前一步meta-distribution)：阐述控制平面与内核解耦的设计哲学，演示如何通过切换包与配置模板复用整套运维体系。
- [Oracle 兼容的 PG 真的有用吗？ · Pigsty：一个"元发行版"](/pg/ivorysql/#pigsty一个元发行版)：说明如何将 14 个 Linux 平台的构建交付、监控、备份与 IaC 底座横向赋能给 IvorySQL、Babelfish、OpenHalo 等异构分支。
- [PostgreSQL主宰数据库世界，而谁来吞噬PG？ · Pigsty 元发行版](/pg/proprity-pg/#pigsty-元发行版)：痛陈公有云 DBaaS 的扩展阉割与劣质云盘溢价，展示用统一开源元发行版将“软件自由”转化为平价企业级 RDS 的路径。
- [PostgreSQL 吞噬数据库世界后，巨头开始吞噬 PG 公司 · 老冯评论](/pg/clickhouse-got-xata/#老冯评论)：剖析巨头收购潮下“全开放扩展仓库 + 跨内核监控管控底座”如何构筑反垄断、守住本地优先底线的护城河。

### 云厂商阉割扩展又白嫖，为何下半场属于开源发行版？ {#cloud-vampirism-and-local-first}

凭借原生 JSON 与 FerretDB 等协议拟态层，PG 在“最想要”增量榜（19%）一举反超 MongoDB（17%），与缓存互补的 Redis 确立双寡头。但击败闭源与 NoSQL 后，最大的威胁变成了套壳售卖高价 RDS 却极少回馈社区的公有云，截断了开源就业与贡献飞轮；正如 Martin Kleppmann 所言，“计算自由的新敌人是云软件”。更糟的是，阿里云、AWS 等 RDS 受制于多租户安全与 AGPLv3 协议，禁用了 TimescaleDB、Citus、ParadeDB、`duckdb_fdw` 等大批灵魂扩展。Fork 魔改内核毫无前途，凝聚数百扩展与自治栈打造“数据库界的 Ubuntu”，才能帮用户夺回主权并省下 50%～90% 云税。

- [为什么PostgreSQL是最成功的数据库？ · 最想要](/pg/pg-is-best/#最想要)：结合调查数据解析 PG 如何凭内置 JSON 与协议拟态层截流文档库需求、反超 MongoDB 登顶增量榜首。
- [为什么PostgreSQL是最成功的数据库？ · 展望未来](/pg/pg-is-best/#展望未来)：引述 Martin Kleppmann 论断剖析云厂商套壳白嫖对开源飞轮的破坏，提出以本地优先开源 RDS 夺回主权与九成成本。
- [PostgreSQL 正在吞噬数据库世界 · 还有什么可以做的？](/pg/pg-eat-db-world/#还有什么可以做的)：批判魔改 PG 内核的伪创新路线，揭露公有云 RDS 因多租户安全与许可证限制大规模阉割核心扩展的现实梗阻。
- [PostgreSQL 正在吞噬数据库世界 · 知行合一的实践：Pigsty](/pg/pg-eat-db-world/#知行合一的实践pigsty)：围绕可扩展性、可靠性、图形化可观测性与高可用等六大价值主张，阐明开源发行版如何实现云数据库平权。

### 防白嫖浪潮下，发行版与 pig 为何回归 Apache 2.0？ {#relicense-to-apache2}

PG 主干永久锁死超宽松协议，因此 Citus、ParadeDB 等新兴扩展纷纷采用强传染 AGPLv3 或双许可分层阻击云寡头。Pigsty 2.0 也曾用 AGPLv3 与 ELv2 筑防线，但在发行版洗牌期我意识到：标准之争拼的是谁能成为下游广泛集成的上游公器。无论是底层包管理 `pig` 与扩展源，还是立志做“数据库界 Debian”的元发行版底盘，唯有放弃源码可用协议枷锁、逆势回归无限制的 Apache 2.0（唯一底线是别瞎吹 100% 自研国产库），才能消除 Omnigres、AutoBase 及定制内核厂商的合规顾虑，把朋友搞得多多的。

- [PostgreSQL会修改开源许可证吗？ · 译者评论](/pg/pg-license/#译者评论)：梳理 PG 主干不可改协议的历史约束，对比外围新兴扩展与发行版转向 AGPLv3 及双许可阻击云厂商的分层策略。
- [从AGPL到Apache：Pigsty 协议变更的思考 · 做数据库世界的 Debian](/pg/pigsty-relicense/#做数据库世界的-debian)：阐明在发行版格局洗牌期放弃 ELv2 回归 Apache 2.0 的战略考量，通过零限制开放成为下游子发行版的公共上游。
- [小猪骑大象：PG内核与扩展包管理神器 · Pig 使用什么开源协议，如何考虑？](/pg/pig/#pig-使用什么开源协议如何考虑)：解析包管理器与扩展构建仓库率先采用 Apache-2.0 让渡利益、换取 AutoBase 与 Omnigres 等友商默认集成的共赢逻辑。

### 个人如何靠“吃狗粮”与中国高并发站上全球上游？ {#dogfooding-and-global-upstream}

独立开发者能打磨出整车级发行版，起点在于身兼 PM、研发与重度用户“吃自己狗粮”，绝不在痛点上敷衍，再靠宽松协议汇集社区众力跨越个人局限。更硬的底气来自中国极限规模试炼场：这套体系是在探探全局 250 万 QPS、百套顶配物理机集群与重度存储过程高压锅里经无数真实故障锤炼出来的，对全球常规场景形成降维打击。而真正的开源出海不是翻译文档抢终端，是在各方嫌累的空白处把四五百个扩展打通 14 个 Linux 发行版双架构（六七万个包），让海外同行做饭直接用你的“大米”。

- [开箱即用的PG发行版：Pigsty · 关于Pigsty](/pg/pigsty-intro/#关于pigsty)：复盘以“吃自己狗粮”方式从自用监控自然生长出完整管控栈的历程，以及用 Apache 2.0 开源跨越个人色彩局限的思考。
- [立足中国，面向全球的 PostgreSQL 发行版 · 立足中国：规模是最好的试炼场](/pg/forge-a-pg-distro/#立足中国规模是最好的试炼场)：还原探探 250 万 QPS 与百套顶配物理机集群的极限实战背景，说明中国超大规模互联网负载如何锻造出降维打击方案。
- [立足中国，面向全球的 PostgreSQL 发行版 · 面向全球：成为供应链的上游](/pg/forge-a-pg-distro/#面向全球成为供应链的上游)：阐释啃下六七万个跨平台扩展包构建苦活、成为海外数据库同行直接依赖的软件供应链上游的高阶出海路径。

## 二、500+ 扩展交付革命与包管理器 pig {#pig-and-delivery}

### 扩展为何总“装不上”，pig 为何只做系统包薄封装？ {#why-pig-wraps-native-pkg}

野生社区散布着 1,617 个扩展，筛除停更与玩具后真正可稳定交付约 511 个；唯有免编译安装且受供应链信任，生态超能力才算落地。如今手编 PostGIS 已是失传技能，PGXN 现场编译、预制镜像或裸拉 `.so` 在生产均脆弱别扭，最可靠的正道唯有系统签名的 RPM/DEB 包，Trunk 等抛弃 `yum/apt` 另造私有格式纯属舍本逐末。仅 4MB 的零依赖 Go 工具 `pig` 坚持做原生 `apt/dnf` 的零锁定薄封装，抹平 16 个发行版与 PG 版本差异且随时可退回原生命令，并自建国内镜像兜底了 PGDG 断 rsync 导致的阿里云、清华源断更困局。

- [人人可用的 PG 扩展 · 2. 可扩展性很重要](/pg/extensions-for-everyone/#2-可扩展性很重要)：给出从 1,617 个野生扩展筛出 511 个可交付包的漏斗数据，论证共享二进制交付层对 DBA、作者、厂商与内核研发的四重价值。
- [PostgreSQL神功大成！最全扩展仓库来了！ · PG 扩展分发现状](/pg/pg-ext-repo/#pg-扩展分发现状)：横向对比 PGXN 源码编译、容器镜像与 `.so` 直拉的运维弊端，确立 `yum/dnf/apt` 签名二进制包在生产环境的正统地位。
- [小猪骑大象：PG内核与扩展包管理神器 · 为什么用操作系统包管理器？](/pg/pig/#为什么用操作系统包管理器)：批判抛弃操作系统包管理重造私有格式的弯路，阐明 `pig` 在原生 RPM/DEB 之上构建统一抽象的极简设计。
- [PG扩展云：解锁 PG 生态的全部潜力 · 简单易用命令行](/pg/pgext-cloud/#简单易用命令行)：详解 4MB `pig` CLI 的零供应商锁定特性，以及自建国内双栈加速镜像解决国内大厂镜像源停更断档的实践。

### 容器发镜像不香吗，为何死磕 80 槽位原生包？ {#containers-vs-linux-native-pkg}

5 个 PG 大版本乘以 16 个 Linux 发行版，每个扩展需打满 80 个构建槽位，规模是容器镜像（10 个槽位）的 8 倍。但这块硬骨头绝不能用发 Docker 镜像绕过去：首先，大量企业生产库依旧直接用包管理器跑在裸机或虚机上；其次，容器不改 Dockerfile 重建即丢扩展，全塞单镜像不安全、按自由混搭预建静态镜像又会触发天文数字组合爆炸；更本质的是，拆开几乎所有 Postgres 容器的 Dockerfile，底层清一色都在用 `apt/dnf` 拉 DEB/RPM 包！即便云原生走向动态合成 OCI 镜像，其地基依然长在 Linux 原生二进制仓之上。

- [人人可用的 PG 扩展 · 12. 为什么要做 Linux 原生包？](/pg/extensions-for-everyone/#12-为什么要做-linux-原生包)：对比单扩展 80 个原生包槽位与 10 个容器槽位的规模差异，点明生产主机与容器构建底层同样仰仗 APT/YUM 原生包的事实。
- [小猪骑大象：PG内核与扩展包管理神器 · 谁还用包管理器，Docker不香吗？](/pg/pig/#谁还用包管理器docker不香吗)：剖析容器环境下扩展持久化与多插件自由混搭的运维噩梦，揭示容器镜像无法绕开底层操作系统软件包的本质。
- [Postgres Extension Day，咱们不见不散 · 4. Postgres 点菜：自选扩展的动态容器镜像](/pg/pgext-day/#4-postgres-点菜自选扩展的动态容器镜像)：梳理云原生动态合成 OCI 镜像与裸机统一 RPM/DEB 二进制仓库在破解扩展组合“维度爆炸”上的协同分工。

### 已有官方 PGDG 源，为何仍缺七成扩展必须自建？ {#pgdg-gaps-and-rust-ban}

单靠向 PGDG 提需求解不了全栈扩展之渴：官方源仅约 135～150 个包，仅半数对齐 YUM 与 APT；更致命的是官方 YUM 明确拒收任何 Rust 扩展，直接堵死自建 Supabase 必需的 `pg_graphql`、`wrappers` 等二十多款 PGRX 插件，也扛不动 `pg_duckdb`、`plv8` 等单次编译一小时的巨无霸。在商业包管理器相继弃坑后，参照 EPEL 思路自建仓库，借 Claude Code 修复近百个失修趴窝扩展、双向移植对齐 APT/YUM 独有包，独自挑起超 72% 第三方扩展重担并将双端缺失率压至 6%，彻底终结了编译地狱。

- [小猪骑大象：PG内核与扩展包管理神器 · PGDG官方仓库有什么问题？](/pg/pig/#pgdg官方仓库有什么问题)：剖析官方源数量偏少且 RPM/DEB 严重割裂的短板，提出以“EPEL 式”补充仓库拉平三大 Linux 阵营体验鸿沟。
- [PostgreSQL神功大成！最全扩展仓库来了！ · 怎么办？我行我上！](/pg/pg-ext-repo/#怎么办我行我上)：记录官方 YUM 仓库拒收 Rust 扩展堵死 Supabase 与 DuckDB 新生态的背景，说明自建跨阵营软件源的必然性。
- [PG扩展云：解锁 PG 生态的全部潜力 · 无可比拟的数量](/pg/pgext-cloud/#无可比拟的数量)：对比官方百余包规模，展示借助 AI 兜底修复近百个弃坑插件与升级 `pgrx`、独自撑起超七成第三方扩展版图的成果。
- [PostgreSQL神功大成！最全扩展仓库来了！ · PG 扩展大全](/pg/pg-ext-repo/#pg-扩展大全)：详述横跨多代 PG 大版本与主流 Linux 发行版双向移植对齐、将 APT/YUM 双端缺失率收敛至 6% 的构建矩阵。

### 维护五百个扩展，会撞上哪些 ABI、Rust 与命名雷？ {#abi-glibc-rust-naming-traps}

野外矩阵远比“版本 × 系统”凶险：PG 17.1 小版本曾破 ABI 击穿 TimescaleDB；EL 升级 OpenSSL 3.5 迫使按 9.6/9.7/10.1 拆源；如 `duckdb_fdw` 作者 alitrack 所揭示，高版本 Ubuntu（`glibc 2.31`）编出的动态库在 RHEL（`glibc 2.17`）必因缺符号崩溃，须低版本构建或静态并入源码；而 Rust 扩展编译极慢、体积数十 MB 且 `pgrx` 版本割裂。CMU 研究者 Abigale Kim 实证了深钩子重型插件间的冲突，实战更频发命名抢占——三大全文扩展争抢 `bm25` 访问方法导致无法同库共存，三个插件争抢 `libduckdb` 被迫改为主子挂载，须靠对象级目录元数据前置避撞。

- [人人可用的 PG 扩展 · 24. Rust 问题](/pg/extensions-for-everyone/#24-rust-问题)：盘点 PG 17.1 小版本破 ABI、EL 小版本升级 OpenSSL 拆源，以及 Rust 扩展编译慢、包体大与 `pgrx` 版本漂移的多维乘积爆炸。
- [duckdb_fdw v1.0.0来了，第13届 PostgreSQL 中国技术大会见 · 引用链接](/pg/duckdb-fdw-1-0/#引用链接)：剖析跨发行版复用动态库时的 `glibc` 向下兼容铁律，对比低版本动态库构建与源码静态并入编译两种解法。
- [人人可用的 PG 扩展 · 26. 命名冲突](/pg/extensions-for-everyone/#26-命名冲突)：以三款扩展争抢 `bm25` 访问方法及多插件争抢 `libduckdb` 为例，论证通过对象级目录元数据前置消解同库冲突。
- [让PG停摆一周的大会：PGCon.Dev 2024 参会记 · 数据库中的无政府状态](/pg/pgcondev-2024/#数据库中的无政府状态)：引述 CMU 对 PG 覆盖 9/10 类扩展点的量化研究，揭示重型扩展间执行链路冲突规律及 RPM/DEB 承载 99% 生产分发的现实。

### AI 构建考古与全矩阵测试如何破五百并反向捉虫？ {#ai-build-archaeology-and-qa}

分发壁垒不在薄薄一层 CLI，而在横跨 RHEL/Debian 双体系多架构的构建工程力——早年连原 Greenplum 团队都苦于缺双栖专家而只发单 CentOS 包。如今 AI Coding Agent 对“构建系统考古”形成降维打击：牵涉 Boost/Eigen/Cairo 复杂开关的化学库 `rdkit` 与搁置两年的 EL10 `plv8` 一两轮即跑通，将总扩展推破 504 个（第三方 332 个），碾压仅不到 30 个三方插件的云 RDS。以结构化目录实现“源码进、签名包出”与文档衍生冒烟测试，不仅两天可增 50 个包，16 平台滚动 QA 矩阵更顺手修补了 AWS 官方 `pgactive` 与 `pgcollection` 的低级 Bug。

- [504 个扩展，PG 生态的天花板在哪？ · 从一个化学扩展说起](/pg/extension-504/#从一个化学扩展说起)：复盘借助编码 Agent 攻克 `rdkit` 与 EL10 `plv8` 跨平台移植难题、将总交付规模推破 504 大关并碾压托管 RDS 的实战。
- [人人可用的 PG 扩展 · 30. 让它可维护](/pg/extensions-for-everyone/#30-让它可维护)：拆解结构化目录驱动的标准化 spec 构建与文档衍生冒烟测试流水线，展示单人高效维护超五百扩展矩阵的方法论。
- [小猪骑大象：PG内核与扩展包管理神器 · 这个项目的核心壁垒是什么？](/pg/pig/#这个项目的核心壁垒是什么)：点明 CLI 外壳之下兼具 PG 内核功底与 RHEL/Debian 双系多架构打包排障手艺才是难以复制的工程壁垒。
- [渡劫期的 PostgreSQL 生态大更新 · 顺手给上游（包括 AWS）修 Bug](/pg/eco-update-202611/#顺手给上游包括-aws修-bug)：展示 16 个 Linux 发行版每周滚动构建与自动化测试如何暴露单一环境盲区，顺手修补 AWS 官方扩展 Bug 并反哺上游。

### 第三方二进制仓如何自证清白并赋能内核演进？ {#reproducible-builds-and-kernel-ci}

回应软件供应链“投毒质疑”最硬核的答案是 100% 开源可复现构建：公开全部打包 spec、补丁与工具链，任何机构只需十几行 Dockerfile 配合 `pig build pkg`，即可在离线隔离容器内从上游源码打出完全一致的 RPM/DEB 仓。这套底座更直接加速了 PG 内核演进：衡量新大版本就绪度的真标尺是扩展适配率，集中构建修补让 PG 17 不到三个月跑通 300+ 扩展，周期较 PG 16 缩短一半；同时首次让核心开发者能一键验证重大架构补丁（尤其是受困于兼容性的“进程改线程”工程）对四百余扩展的冲击。

- [PG扩展云：解锁 PG 生态的全部潜力 · 开源、供应链与信任](/pg/pgext-cloud/#开源供应链与信任)：阐明通过全套构建脚本开源与 `pig build pkg` 离线容器可复现编译彻底消除跨国供应链信任芥蒂的机制。
- [中国厂商首次站上 PGConf.dev 主题演讲台 · 我的演讲主题是什么？](/pg/pgconfdev-china-keynote/#我的演讲主题是什么)：揭示 444 个扩展统一构建矩阵如何替 PostgreSQL 核心团队解开“进程改线程”内核演进的扩展兼容性验证死结。
- [PostgreSQL 12 过保，PG 17 上位 · PG17扩展](/pg/pg12-eol-pg17-up/#pg17扩展)：对比 PG 16 苦等半年与 PG 17 不到三个月集齐 300+ 主力扩展的速度跃升，印证集中构建源对新大版本落地的加速效应。

### 苦筑数年的扩展仓库壁垒，为何免费开放给同行？ {#open-repo-for-peers-and-vendors}

每次 PG 大版本升级都会打断一批失修插件，仓库维护者扮演着修补匠与“你卷你的、我全都要”的中立军火商——亲自修补失联扩展、助推 `duckdb_fdw` 共享动态库、帮 ParadeDB 打通打包，再靠 Cloudflare 免流量 CDN 与低成本国内源兑现永久免费承诺。将 `PGEXT.CLOUD` 与 `pig` 以 Apache 2.0 免费送给竞争同行，实则是确立事实标准的正和共赢：Omnigres、AutoBase 与 StackGres 纷纷接入平添四百余扩展，OrioleDB、TensorChord 也借此一键触达全球；国内 PG 衍生厂商更应告别闭门造车，几行配置接入即可零成本追平国际生态代差。

- [PG扩展云：解锁 PG 生态的全部潜力 · 目前的进展](/pg/pgext-cloud/#目前的进展)：展示以 Apache 2.0 独立开放仓库后，赋能 Omnigres、AutoBase 等同行发行版及十余家扩展与分支内核团队的生态共赢版图。
- [PostgreSQL神功大成！最全扩展仓库来了！ · 一些感想与体会](/pg/pg-ext-repo/#一些感想与体会)：复盘修补失联插件、向上游提 PR 的修补匠日常，以及依托零流量费 CDN 维持中立永久免费公共服务的成本结构。
- [PostgreSQL高峰论坛：参会小记](/pg/pg-summit-2025/)：呼吁本土 PG 系数据库厂商告别低水平重复打包内耗，直接复用开源跨平台扩展仓库零成本追平国际前沿生态。

### 如何用“目录 + 仓库 + 包管理”终结选型断层？ {#catalog-repo-manager-trinity}

长期以来“找不到、看不懂、装不上”令 PG 扩展生态陷入“有酒无杯”窘境：传统列表只给名字，DBA 得在翻 GitHub、查商业协议风险、核对兼容与解编译报错间耗尽心力。单靠列表救不了交付，必须把“双语百科目录 + 跨 14 平台 5 代 PG 的预编译仓 + `pig` 包管理器”打通为闭环三件套。按 16 大分类为 464+ 扩展建立开源“数字身份证”——完整标注开发语言、许可证风险、是否需改 `shared_preload_libraries` 重启、是否含 DDL 及依赖冲突矩阵，才能把选型到上线压缩为复制粘贴一行命令。

- [PG 扩展百科全书：中英双语，开箱即用 · 为什么要做这件事](/pg/pgext-pedia/#为什么要做这件事)：剖析传统扩展列表在协议排查、兼容确认与源码编译上的体验断层如何阻碍生态潜力释放。
- [PG 扩展百科全书：中英双语，开箱即用 · 三件套：目录 + 仓库 + 包管理器](/pg/pgext-pedia/#三件套目录--仓库--包管理器)：阐明双语百科目录、全平台 RPM/DEB 预编译仓库与 `pig` 包管理器三位一体打通发现到安装闭环的架构设计。
- [PG 扩展百科全书：中英双语，开箱即用 · 这不是一个列表，而是一本百科全书](/pg/pgext-pedia/#这不是一个列表而是一本百科全书)：详解涵盖 16 大分类、许可证风险、预加载重启属性与冲突关系的扩展“数字身份证”开源元数据规范。

### 扩展百科如何兼顾人机双友好，为何五改归 Hugo？ {#dual-friendly-docs-and-hugo}

分发不能只管装包不管用法：对 Citus、TimescaleDB、PostGIS 等书本级巨无霸建独立精翻子站，对仅一页 README 的常规扩展汉化内嵌详情页，才能闭环最后一公里。AI 时代目录站须兼顾“Agent 与人类双友好”：底稿坚守干净低噪的纯 Markdown 供大模型高效解析，表现层在编译期借 Hugo 短代码与 CSS 渲染交互式包矩阵大表。历经五代折腾——试水过繁琐的 Next.js、难撑大站的轻量主题，也踩过未备案独立域名国内抽风的坑——最终回归初选的 Hugo + Docsy 并合入备案主站，印证 Boring Technology 才最稳妥。

- [464个扩展开箱即用：新版 PG 扩展目录发布 · 不只是有包，还要有文档](/pg/pg-ext-catalog-464/#不只是有包还要有文档)：介绍巨无霸扩展建独立精翻子站与常规扩展内嵌汉化 README 的分层文档聚合策略。
- [464个扩展开箱即用：新版 PG 扩展目录发布 · 同时对 Agent 友好，对人类友好](/pg/pg-ext-catalog-464/#同时对-agent-友好对人类友好)：阐述底层纯净 Markdown 保障 Agent 解析效率、编译期短代码与 CSS 兼顾人类交互体验的双重友好架构。
- [464个扩展开箱即用：新版 PG 扩展目录发布 · 五个版本，兜兜转转回到原点](/pg/pg-ext-catalog-464/#五个版本兜兜转转回到原点)：复盘从轻量主题、Next.js 独立未备案站最终回归 Hugo + Docsy 备案主站的五代演进教训。

## 三、AI 向量、BM25 全文检索与应用架构收敛 {#vector-and-search}

### 为什么说“向量是新的 JSON”并驱动下一个十年？ {#vector-is-the-new-json}

正如 Jonathan Katz 复盘 PG 9.2 简陋文本 `json` 到 9.4 二进制 `jsonb` 历史所揭示的：只要能把关联数据留在同一套成熟关系栈里，开发者宁可容忍早期局限，也不愿引入独立专用库。大模型拉低了多模态 Embedding 门槛，但 PG 原生 `array` 缺距离算子、`cube` 被锁死在 100 维内（装不下 1536 维向量），这一断层催生了专门向量扩展。十年前 `JSONB` 合体 MongoDB 与 MySQL 缔造了黄金十年；十年后，随着 `pgvector` 入官方源及较 IVFFLAT 快达 20 倍的 HNSW 落地，向量必将接棒领跑 AI 十年。

- [向量是新的 JSON · JSON 简史：PostgreSQL 实现](/pg/vector-json-pg/#json-简史postgresql-实现)：回顾 PG 从初代文本校验 `json` 到高性能二进制 `jsonb` 追平专用文档库并反哺 SQL 标准的演进规律。
- [向量是新的 JSON · 向量崛起：一种新 JSON](/pg/vector-json-pg/#向量崛起一种新-json)：剖析大模型 Embedding 普及背景下，原生 `array` 缺距离计算与 `cube` 100 维上限的能力断层如何催生向量插件。
- [向量是新的 JSON · 译者评论](/pg/vector-json-pg/#译者评论)：对标十年前 `JSONB` 统合文档与关系库的战略拐点，预判 `pgvector` 与 HNSW 索引对 PG 未来十年的生态拉动。

### 加装 pgvector 为何胜过专用库，亿级性能如何？ {#pgvector-vs-standalone-vector-db}

大模型只是将语料有损压缩在权重里的“计算大脑”，精确长期记忆必须编码存入向量库做 K-NN 召回。选型铁律是“合格的向量库首先得是合格的数据库”——给 PG 加装 `pgvector`，同表并排存取业务文本与向量，免去跨库同步并白捡 ACID、PITR 与高可用。高维精确搜索极贵，`pgvector` 借 `ivfflat` 等近似最近邻（ANN）索引按 k-means 聚簇（`lists`），用 `probes` 权衡延迟与召回率。M1 Max 单核实测：百万条 1536 维约 8ms，1 亿条 128 维 Top 1 仅 5ms，SIFT 1M 低至 1.8ms（约 500 QPS），挂只读从库即可线性扩展吞吐。

- [AI大模型与向量库 PGVector · AI是怎么工作的](/pg/llm-and-pgvector/#ai是怎么工作的)：阐明神经网络 Embedding 数学机理，解释有损压缩的大模型参数为何必须依赖外部向量库承载精确长期记忆。
- [AI大模型与向量库 PGVector · PG向量插件 PGVECTOR](/pg/llm-and-pgvector/#pg向量插件-pgvector)：论证站在成熟 PG 肩膀上并排存取业务字段与向量、免除异构同步并继承灾备监控底座的务实优势。
- [向量是新的 JSON · PGVECTOR: 开源PG向量扩展](/pg/vector-json-pg/#pgvector-开源pg向量扩展)：解析近似最近邻（ANN）索引异于传统 B-Tree 的检索哲学，以及通过 `lists` 与 `probes` 平衡延迟与召回率的机制。
- [AI大模型与向量库 PGVector · PGVECTOR 的性能](/pg/llm-and-pgvector/#pgvector-的性能)：给出百万级 1536 维、亿级 128 维与 SIFT 1M 毫秒级单核实测延迟数据，说明依托只读从库水平扩展 QPS 的架构路径。

### ParadeDB 切入 PG 原生块存储为何是一次质变？ {#paradedb-bm25-and-block-storage}

在主库旁外挂 Elasticsearch 既笨重又饱受同步延迟与重建索引之苦；但只用内置 `tsvector`，大表排序极慢且缺标准 BM25 评分、分面统计与向量混合打分。ParadeDB 将对标 Lucene 的 Rust 搜索库 Tantivy 封装为原生索引扩展，免 ETL 在库内完成混合检索。真正的质变发生在 `pg_search` 0.14：它告别早期绕过缓冲池私管外部文件的“缝合怪”形态，全面切入 PG 原生块存储与 Buffer Cache——不仅索引构建与写入吞吐翻数倍，更原生打通了 WAL 流复制、崩溃恢复、PITR 与完整 MVCC，晋升生产级一等公民。

- [PG生态新玩家：ParadeDB · ParadeDB解决什么问题？](/pg/paradedb/#paradedb解决什么问题)：对比外挂 Elasticsearch 的同步运维痛点与内置 `tsvector` 缺失大表 BM25 及混合打分的短板，界定原生搜索扩展生态位。
- [PG生态新玩家：ParadeDB · ParadeDB 的构建方式](/pg/paradedb/#paradedb-的构建方式)：解析基于 Rust Tantivy 打造原生 Postgres 索引、免除外部 ETL 并在 ACID 事务内实时同步倒排索引的架构。
- [PostgreSQL 生态前沿进展 · ParadeDB](/pg/pg-frontier/#paradedb)：剖析 `pg_search` 从私管外部文件重构为接入 PG 原生块存储与缓冲池，从而打通 WAL 复制、PITR 与 MVCC 的里程碑意义。

### 自建 Supabase 与 Dify 为何必须动静分离收敛？ {#self-hosting-supabase-and-dify}

无论自建开源 BaaS Supabase 还是 AI 平台 Dify，直接把官方演示 Docker Compose 搬上生产都是反模式。官方模板把裸 PG、Redis 与单独拆出的 `pgvector` 容器混编在一起，既无高可用、备份与监控，又违背“如无必要，勿增实体”——元数据既已在 PG 内，直接启用 `pgvector` 即可兼任向量库，何必多养一套冗余容器？正确的生产姿势是“动静分离”：无状态网关与 `dify-worker` 用容器拉起；有状态底座交给预装齐 `supautils`、`pg_graphql`、`wrappers`、`vault` 与 `pgvector` 的高可用发行版集群托管。

- [PG系创业公司Supabase：`$80M` C轮融资 · Supabase  B 轮/C 轮融资 `80M $`](/pg/supabase-series-c/#supabase--b-轮c-轮融资-80m-)：拆解自托管 Supabase 的动静分离架构，说明为何必须用预装齐全套自研插件的外部高可用 PG 集群承接有状态层。
- [使用Pigsty自建Dify：AI工作流平台 · Pigsty的准备工作](/pg/dify-setup/#pigsty的准备工作)：指出官方 Compose 混编有状态组件与独立拆出向量容器的弊病，演示用单一高可用 PG + `pgvector` 精简收敛 AI 数据栈。

## 四、OLAP 列存踢馆、时序超表与流式计算 {#olap-timeseries-stream}

### DuckDB 与 PG 内核合体如何填平 OLAP 短板？ {#duckdb-fills-pg-olap-gap}

列存分析曾是 PG 最后短板：ClickBench 基准中原生 PG（x47）与 TimescaleDB（x103）曾落后 ClickHouse（x3～x4）十余倍，但 ParadeDB `pg_analytics`（x10）与嵌入式王者 DuckDB（x3.2）接入后一举直抵塔尖！DuckDB 短于多并发事务、权限隔离与高可用，恰是 PG 看家本领；内核合体免 ETL 且保 ACID，直接粉碎了给 DuckDB 薄皮套壳圈钱的迷梦。早在国际缝合大赛前，个人开发者 alitrack 已打磨四年 `duckdb_fdw`（借 `duckdb_execute` 破单写约束并反向加速本地表），反倒是国内大厂沉迷边角内卷、集体漏判了主战场剧变。

- [PostgreSQL 正在吞噬数据库世界 · OLAP 领域迎来踢馆者](/pg/pg-eat-db-world/#olap-领域迎来踢馆者)：用 ClickBench 实测倍率对比原生 PG、ClickHouse 与 DuckDB/ParadeDB 扩展，宣告 PG 免 ETL 跃入 OLAP 第一梯队。
- [谁整合好DuckDB，谁赢得OLAP世界 · DuckDB的短板与其中的机遇](/pg/pg-duckdb/#duckdb的短板与其中的机遇)：剖析 DuckDB 并发安全治理短板与 PG 企业级底座的完美互补，预判内核级扩展合体对套壳 OLAP 项目的降维清场。
- [duckdb_fdw v1.0.0来了，第13届 PostgreSQL 中国技术大会见 · 引用链接](/pg/duckdb-fdw-1-0/#引用链接)：复盘 `duckdb_fdw` 从借道 SQLite 包装器到引入 `duckdb_execute` 破除并发约束、乃至反向加速 PG 本地表查询的演进脉络。
- [第七届PG生态大会：一些感想 · 扩展很重要，但很多人没意识到](/pg/pgconf-china-7th/#扩展很重要但很多人没意识到)：对比 Andy Pavlo 总结的国际 DuckDB 与 Tantivy 扩展赛马热潮，批评国内厂商忽视可扩展性主战场的战略迟钝。

### TimescaleDB 为何选宽表且十亿行写入快二十倍？ {#timescaledb-wide-table-and-hypertable}

专用时序库推崇的 `<metric, tags, timestamp, value>` 窄表会把同台设备同秒多指标拆散，导致序列数随标签叉积爆炸且割裂相关性；TimescaleDB 坚持关系宽表存单次采样全部度量，静态元数据拆到维表按需 `JOIN`，免除冗余膨胀。写入上，原生 PG 单表超五千万行后二级 B-Tree 溢出内存引发随机 I/O 雪崩，吞吐从 10 万+ 跌至 5 千行/秒；TimescaleDB 将超表自动切分为适中物理子表（Chunk），锁住热索引常驻内存，十亿行下仍稳居 11 万行/秒（快 20 倍），过期数据直接 `drop_chunks` 删物理文件免 `VACUUM`。

- [TimescaleDB 快速上手 · 宽表模型](/pg/timescale-install/#宽表模型)：对比窄表标签叉积爆炸弊端，阐明关系型宽表存同刻多维指标并关联静态元数据维表的建模优势。
- [TimescaleDB 快速上手 · 更高的写入速率](/pg/timescale-install/#更高的写入速率)：剖析五千万行后原生 B-Tree 溢出内存引发 I/O 雪崩的机理，展示超表自动切分 Chunk 锁住热索引与免 `VACUUM` 物理淘汰的威力。

### TimescaleDB 有何边界，为何查询易爆共享内存锁？ {#timescaledb-boundaries-and-locks}

寄生于 PG 使 TimescaleDB 原生继承完整 SQL、PostGIS 与生态工具，免去双栈运维痛苦。但海量 Chunk 会增加数毫秒规划开销：若仅需极简 KV 点查、数据高度稀疏无模式、对列存极限压缩比敏感或只跑低频离线批处理，专用列存或分布式文件系统更合适。生产上线更有必调暗雷：跨周期查询必须同时对涉及的所有物理 Chunk 子表及索引加锁，默认 `max_locks_per_transaction = 64` 极易被打爆并报 `FATAL: out of shared memory`！因该参数需重启生效，初始化时必须按 `2 * num_chunks` 预留足够锁槽位。

- [TimescaleDB 快速上手 · 何时不使用TimescaleDB？](/pg/timescale-install/#何时不使用timescaledb)：客观划定 TimescaleDB 在极简 KV 点查、高度稀疏无模式、极致冷压缩与离线批处理场景下的不适用边界。
- [TimescaleDB 快速上手 · 调参](/pg/timescale-install/#调参)：揭示跨分块查询并发锁耗尽默认 64 槽位引发 `out of shared memory` 的根因，给出按 `2 * num_chunks` 预调锁表容量的铁律。

### 如何免引重型流引擎，在 PG 内跑实时流式聚合？ {#pipelinedb-continuous-views}

面对监控指标或维基百科 PV 级高频流统计，无需复杂跨窗口乱序编排时，根本不必架设 Kafka + Flink 重型栈再写回数据库。PipelineDB 以预加载扩展形态将无界输入流抽象为 `FOREIGN TABLE`，在其上定义带 `action=materialize` 的连续视图（Continuous View）：外部通过 `COPY ... FROM STDIN` 持续灌入数据，库内在内存实时完成计数、求和及 P99 分位数等增量聚合，磁盘仅物化最终结果而免落海量原始明细。配置时除设置 `shared_preload_libraries = 'pipelinedb'` 重启外，必须同步调大 `max_worker_processes`（如 128），否则后台流计算进程配额不足必报错。

- [PipelineDB快速上手 · PipelineDB使用样例 —— 维基PV数据](/pg/pipeline-intro/#pipelinedb使用样例--维基pv数据)：演示用 `FOREIGN TABLE` 抽象无界数据流配合连续视图在内存中实时物化计数与分位数聚合、免落原始明细的实战用法。
- [PipelineDB快速上手 · PipelineDB安装与配置](/pg/pipeline-intro/#pipelinedb安装与配置)：点明预加载动态库之外必须同步调大 `max_worker_processes` 以支撑后台并行流计算进程池的配置红线。

## 五、新存储引擎、多模拟态与时空 FDW 武器库 {#storage-multimodal-arsenal}

### 为何 4 倍吞吐才配换引擎，OrioleDB 转正意味着什么？ {#orioledb-4x-and-tam-risks}

硬件过剩时代 40% 提速不值得换引擎，唯有 OrioleDB 靠剔除 OS 缓存、无锁页直连、Undo Log 根治膨胀与并行行级 WAL 实现的 4 倍吞吐，才够格推迟单机“分库”。Supabase 收购后将其转向“云原生存储”，本质是把冷数据从天价 EBS 卸载到廉价 S3，造出首个不脱离主干的开源存算分离方案。如今 OrioleDB 1.10.1 正式转正，与 DocumentDB 1.0、DuckDB 2.0 扩展群及 `pg_lake 3.6` 齐聚；但务必警惕：触碰事务可见性与数据页的 TableAM 引擎与底层 TDE 杀伤力十倍于普通插件，一旦暴雷直毁全库完整性，未经长周期生产验证切忌尝鲜。

- [OrioleDB来了！4x性能，消除顽疾，存算分离 · 极致性能，四倍吞吐](/pg/orioledb-is-coming/#极致性能四倍吞吐)：拆解剔除 FS Cache、无锁页直连、Undo Log 与并行行级 WAL 如何压降 IOPS、突破单机 OLTP 写入分库瓶颈。
- [OrioleDB来了！4x性能，消除顽疾，存算分离 · 云原生存储](/pg/orioledb-is-coming/#云原生存储)：揭示云厂商“云原生”即冷数据卸载 S3 的成本本质，点明 OrioleDB 免硬分叉实现开源 PG 存算分离的独特价值。
- [渡劫期的 PostgreSQL 生态大更新 · 1. DocumentDB 1.0 转正与 DuckDB 2.0 浪潮](/pg/eco-update-202611/#1-documentdb-10-转正与-duckdb-20-浪潮)：盘点 OrioleDB 1.10.1 正式版转正与 DocumentDB 1.0、DuckDB 2.0 系列扩展及 Babelfish 6.2 会师的多模里程碑。
- [尝鲜须谨慎：PG新存储引擎故障案例 · 经验与教训](/pg/new-storage-engine-risk/#经验与教训)：结合新存储引擎真实故障案例，警示自定义表访问方法（TAM）与底层 TDE 对全库可用性及数据完整性的致命风险边界。

### 异构协议拟态与兼容分支有哪些限制与扩展代价？ {#protocol-mimicry-and-fork-tradeoffs}

迁移异构存量业务有两条捷径：一是无状态协议代理 FerretDB，把 MongoDB 线缆协议实时翻译为 `JSONB` SQL 摆脱 SSPL 锁定，但需加 `authMechanism=PLAIN` 桥接 `scram-sha-256`，并避开 `NUL` 字符、嵌套数组及含 `.` 或 `$` 前缀键名等禁区；二是轻度内核分支，如双监听 5432/3306 并将 MySQL 库映射为 Schema 的 OpenHalo，可零改造复用高可用底座。但切往 IvorySQL 等改动解析器与符号的兼容内核时，最易忽视扩展代价：虽四行配置能继承管控栈，但原版预编译 C/Rust 扩展全部失效，必须从源码重编。

- [FerretDB：假扮成MongoDB的PG · 配置](/pg/ferretdb/#配置)：解析无状态协议转换层如何把 MongoDB 线缆命令翻译为 `JSONB` 与表达式索引，打通摆脱 SSPL 锁定的零代码迁移路径。
- [FerretDB：假扮成MongoDB的PG · 快速上手](/pg/ferretdb/#快速上手)：列出对接 `scram-sha-256` 必配的 `authMechanism=PLAIN` 参数，以及嵌套数组、特殊键名与 `NaN/Infinity` 等文档格式禁区。
- [OpenHalo：MySQL线缆兼容的PostgreSQL来了！ · 所以，我想试试，咋整？](/pg/openhalo-mysql/#所以我想试试咋整)：详解双端口监听下将 MySQL Database 映射为 PG Schema 并无缝接入 Patroni、pgBackRest 与监控底座的机制。
- [兼容Oracle的开源 PostgreSQL？ · 扩展](/pg/oracle-compatible-pg/#扩展)：揭示定制兼容内核修改解析器与符号表后导致原生预编译 C/Rust 扩展失效、必须从源码重编的生态代价。

### 新运行时与领域对象如何把 PG 变成数据控制平面？ {#pg-as-data-control-plane}

新工具链正打破 C 语言与超管特权壁垒：`pg_tle` 与 `pl/<any>` 支持免超管跑接近原生速度的 WebAssembly，单头 C++20 框架 `Cppgres` 消除易错样板，`SynchDB` 借 JNI 嵌入 Debezium 直拉 CDC 流；架构上，`pgvector-remote` 以 PG 为事务控制平面向外卸载重算力，`Spat` 借 DSM 共享内存内生长出类 Redis 服务。同时，百万化合物检索 `rdkit`、体积仅 JSONB 三分之一的 `pgproto`、金融精度 `pgbson`、混合排序 `pg_rrf` 与 43 亿边图矩阵 `one_sparse` 正把专业领域对象收进单条 SQL 事务，砍掉外部胶水微服务。

- [Postgres Extension Day，咱们不见不散 · 1. 从 pl/v8 到 `pl/<any>`：迈向更容易的扩展开发](/pg/pgext-day/#1-从-plv8-到-plany迈向更容易的扩展开发)：盘点免超管 WebAssembly 运行时、单头文件 C++20 框架 `Cppgres` 与 JNI 嵌入 Debezium 的跨语言扩展演进。
- [Postgres Extension Day，咱们不见不散 · 7. 作为控制平面的 Postgres：使用扩展卸载计算的挑战](/pg/pgext-day/#7-作为控制平面的-postgres使用扩展卸载计算的挑战)：探讨以 PG 为事务控制平面向外卸载算力（`pgvector-remote`）及利用 DSM 共享内存内生构建类 Redis 引擎（`Spat`）的架构质变。
- [504 个扩展，PG 生态的天花板在哪？ · 总结](/pg/extension-504/#总结)：展示化学分子 `rdkit`、紧凑序列化 `pgproto`、RRF 排序融合与十亿边稀疏矩阵图计算收敛进单条 SQL 事务削减胶水微服务的趋势。

### 如何靠 PGFS 做文件 PITR 并在库内闭环隐私脱敏？ {#pgfs-pitr-and-pg-anonymizer}

把状态资产与治理规则收归内核，能零硬件成本解开两道企业难题。一是库表与本地附件一致性容灾：Odoo、GitLab、Dify 传统快照无法对齐数据库 PITR；用 JuiceFS 把元数据与数据块全塞进 PG（PGFS），文件改动尽数写入 `jfs_blob` 汇入同一条 WAL 流，一次 `pgBackRest` 恢复即可让附件与库表同步回滚到同一秒。二是应对 GDPR 与个保法天价罚单的 PII 脱敏：外部清洗脚本极易漏列，Rust 重写的 PostgreSQL Anonymizer 2.0 用 `SECURITY LABEL` 在表 DDL 内建规则，组合静态遮罩、动态屏蔽与匿名转储就地锁死拖库风险。

- [PGFS：将数据库作为文件系统 · PGFS实战：文件系统也能PITR](/pg/pgfs/#pgfs实战文件系统也能pitr)：详解将 JuiceFS 元数据与对象块双双指向 PostgreSQL、借同一条 WAL 流实现文件系统与库表秒级同步 PITR 的实战方案。
- [PII数据安全合规与PG Anonymizer最佳实践 · 3. PostgreSQL Anomyizer](/pg/pg-anonymizer/#3-postgresql-anomyizer)：阐述用原生 `SECURITY LABEL` 语法在 Schema 定义阶段声明式绑定脱敏规则、取代高危外部清洗脚本的内核级治理思路。
- [PII数据安全合规与PG Anonymizer最佳实践 · 4. 快速上手](/pg/pg-anonymizer/#4-快速上手)：拆解静态遮罩、动态屏蔽视图与匿名转储三大模式配合假名洗牌加噪函数覆盖全生命周期合规用数的最佳实践。

### B 树画框为何解不好 KNN，PostGIS 如何压至 1ms？ {#postgis-knn-and-btree-gist}

在亿级 POI 表用传统 B 树经纬度框选解“附近的人”，困死在半径魔数里：圈 1 公里在无人区查空，放宽到 300 公里在商圈候选集雪崩，且高纬度平面欧氏近似严重失真。PostGIS 的 GiST（R 树）索引配 `<->` 算子按由近及远流式检索免除魔数——平面 `Geometry` 仅 1.6ms，WGS84 椭球面精确 `Geography` 约 3.4～4.5ms。若叠加类别等标量过滤，加载内置 `btree_gist` 把标量列融入高维建 `GIST(position, category)` 复合索引并 `CLUSTER` 聚簇，即可将亿级表查询从 30 秒压缩三万倍至 1 毫秒！

- [KNN极致优化：从RDS到PostGIS · Bad Case](/pg/knn-optimize/#bad-case)：剖析传统 B 树经纬度画框初筛在稠密商圈与稀疏无人区进退维谷的半径魔数死结及高纬度平面距离失真。
- [KNN极致优化：从RDS到PostGIS · LEVEL-4 GIST](/pg/knn-optimize/#level-4-gist)：详解 R 树 GiST 索引配合 `<->` 算子免半径流式排序原理，对比平面 `Geometry`（1.6ms）与球面精确 `Geography`（3.4～4.5ms）开销。
- [KNN极致优化：从RDS到PostGIS · LEVEL-5 btree_gist](/pg/knn-optimize/#level-5-btree_gist)：展示利用 `btree_gist` 构建空间与标量复合索引叠加物理聚簇，将亿级表带过滤 KNN 查询从 30,000ms 压至 1ms 的终极优化。

### 行政区划与百万 IP 定位如何用 GiST 榨出十万 QPS？ {#geodecode-and-inetrange-gist}

用最近城市中心点（Voronoi）或 GeoHash 查表做行政区划逆编码，在犬牙交错边界与敏感海域极易指鹿为马；用 10MB 权威 WGS84 边界配 `ST_Contains` 才绝对正确。顺应 R 树讨厌狭长畸形与飞地的特性，只判县级围栏免去省国界计算，并将 `MultiPolygon` 切分为饱满 `Polygon` 聚簇，单核可达 9100+ TPS（109 微秒），48 核达 35 万 TPS！同理，600 万 IP 段定位摒弃双列 `<=` 扫描，基于 `inet` 与 `SUBTYPE_DIFF` 构造 `inetrange` 挂载 GiST `@>` 索引，延迟从 900ms 压至 0.34ms，单机轻松十万 QPS。

- [PostGIS高效解决行政区划归属查询 · 0x01 正确至上](/pg/adcode-geodecode/#0x01-正确至上)：批驳中心点 Voronoi 划分与 GeoHash 字典在复杂边界及海域的失真硬伤，确立 10MB 权威边界多边形精确包含判定方案。
- [PostGIS高效解决行政区划归属查询 · 区域切分](/pg/adcode-geodecode/#区域切分)：演示剔除省国界冗余判定并将含飞地 `MultiPolygon` 拆解为饱满 `Polygon` 聚簇，把单次逆编码压进 109 微秒（48 核 35 万 TPS）。
- [GeoIP 地理逆查询优化 · 0x03 范围索引](/pg/geoip/#0x03-范围索引)：展示基于原生 `inet` 自定义 `inetrange` 范围类型并建立 GiST 包含索引，在 600 万 IP 段表上实现 0.34ms 极速定位。

### 如何巧用 file_fdw 管道免 Agent 用 SQL 查宿主机？ {#file-fdw-unix-pipes}

践行“SQL over Everything”，中小型场景采集宿主机进程与磁盘指标，不必维护定时写库脚本或额外部署 OSQuery。PostgreSQL 10 为内置 `file_fdw` 引入的 `PROGRAM` 选项打通了进程标准输出——查询外表时自动拉起 Shell 管道流式解析结果。针对 `ps aux`、`df` 空白不规整及命令参数含空格逗号的痛点，用 `awk` 将分隔符统一替换为罕见控制符 `\037`（`\x1F`）输出伪 CSV 即可避开列错位，在库内闭环采集与关联；仅需注意其只读边界，反向增删改控制则需交由 Multicorn 等自定义 FDW。

- [file_fdw妙用无穷——从数据库读取系统信息 · 创建外部表](/pg/file_fdw/#创建外部表)：演示利用 `PROGRAM` 管道实时拉取 `ps`/`df` 标准输出，并用 `awk` 配合 `\037` 控制字符安全规避命令参数列错位的技巧。
- [file_fdw妙用无穷——从数据库读取系统信息 · 有什么用](/pg/file_fdw/#有什么用)：对比外置定时脚本与 OSQuery，界定 `file_fdw` 库内零组件闭环采集只读指标的优势及需借力 Multicorn 的写控制边界。

### 生产装 PostGIS 与 C 扩展为何严禁盲目手编源码？ {#postgis-mongofdw-package-first}

交付 C/C++ 扩展必须死守“包管理优先于源码编译”。PostGIS 背后横跨 `GEOS`、`Proj`、`GDAL` 及拖入 `CGAL/Boost` 的三维库 `SFCGAL`，除追未发版上游快照外，生产环境组合 PGDG 与 EPEL 二进制包可靠百倍。早期手编粗糙第三方扩展如 `mongo_fdw` 更是步步惊心：文档谎称兼容 `1.0.0+`，实则必锁 `libbson/libmongoc 1.3.1` 避开非标 C99 报错，`json-c` 需手动补 `-fPIC`，隔离内网还得拆解私自联网的 `autogen.sh` 手写宏并按“序列化库 → C 驱动 → FDW”逐层构建 `ldconfig`。

- [源码编译安装 PostGIS · 3. PostGIS安装](/pg/postgis-install/#3-postgis安装)：说明在 RHEL/CentOS 生产环境组合 PGDG 官方源与 EPEL 源一键安装验证过的二进制包为何远胜手工编译。
- [源码编译安装 PostGIS · 必选依赖](/pg/postgis-install/#必选依赖)：梳理 `GEOS`、`Proj`、`GDAL`、`SFCGAL` 等底层原生库与空间算子的绑定关系，划定仅在追未发版快照时才编源码的准则。
- [PostgreSQL MongoFDW安装部署 · 安装 mongo_fdw](/pg/mongo_fdw-install/#安装-mongo_fdw)：还原内网手编 `mongo_fdw` 时遭遇文档失实、锁定 `1.3.1` 驱动对、补加 `-fPIC` 及拆解私自联网构建脚本的排障细节。
- [PostgreSQL MongoFDW安装部署 · mongo_fdw 的依赖](/pg/mongo_fdw-install/#mongo_fdw-的依赖)：总结优先复用系统包管理安装工具链、确需手编时严格按底层序列化库到驱动再到插件自底向上构建的规范。

## 六、AI 渡劫期、开源逼定价与接盘侠续命战 {#oss-stewardship-and-rescue}

### AI 挖洞渡劫期下，停更扩展与伴生包为何沦为后门？ {#ai-vuln-era-and-attack-surface}

AI 自动化扫洞正把开源软件栈拖入高压“渡劫期”：大模型把攻击者的放大镜升级成显微镜，不仅迫使稳健的 PG 19 因密集修洞延期，更终结了“成熟软件放着不改跑几年”的旧时代。各大云厂商因伴生组件漏洞集体中招后，PostGIS 3.7.0 壮士断腕将 `address_standardizer` 与 `postgis_tiger_geocoder` 踢出核心包独立分发以收敛攻击面。失修项目不叫“稳定”，只叫“敞着门”腐化——接手停摆八个月的 `vchord` 后用顶级模型全面审计，当场扫出二三十个隐患及多个 Crash/Segfault 致命缺陷。

- [渡劫期的 PostgreSQL 生态大更新 · 一、重磅内核与里程碑：OrioleDB 转正，多模分支齐聚](/pg/eco-update-202611/#一重磅内核与里程碑orioledb-转正多模分支齐聚)：记录 AI 火力扫洞导致 PG 19 延期，以及 PostGIS 3.7.0 在云厂商集体中招后剥离两大伴生扩展收敛攻击面的风向标事件。
- [老冯又接盘新开源项目了 · 二、为什么要接](/pg/maintain-vchord/#二为什么要接)：披露对停更八个月的 `vchord` 执行大模型深度审计当场挖出二三十处隐患与多个 Crash 缺陷的实况，警示失修代码腐化速度。

### 巨头 2.5 亿美元并购为何裁掉备份支柱，公地怎破局？ {#snowflake-crunchy-commons-tragedy}

pgBackRest 一度停更撕开了资本收编与 AI 预算扭曲抽空公地的残酷真相：David Steele 是在 Crunchy Data 领薪做开源的架构师，然而 Snowflake 斥资 2.5 亿美元收购 Crunchy 高喊“AI-native Postgres”后，却容不下一位灾备支柱维护者的岗位——在只认 GPU 与 Token 的预算表上，“不出事不显功”的备份最先成弃子。AWS 等云巨头靠托管 PG 年赚数十亿美元，却心安理得白嫖外围标准组件（赞助商一度仅剩 Supabase）。单靠善意必被磨穿，唯有跑通“纯粹热爱 + 企业付费支持”双轮才能跨越周期。

- [顶级开源备份工具 pgBackRest 停止维护 · 故事的真正背景](/pg/pgbackrest-archive/#故事的真正背景)：揭开 Snowflake 2.5 亿美元收购 Crunchy Data 后裁撤受薪维护者岗位的内幕，剖析 AI 淘金热预算扭曲对灾备基建的挤出效应。
- [顶级开源备份工具 pgBackRest 停止维护 · 更深层的观点](/pg/pgbackrest-archive/#更深层的观点)：痛批云巨头年入数十亿却白嫖外围核心组件的公地悲剧，论证“纯粹热爱 + 企业级付费支持”双轮驱动的可持续生存之道。

### pgBackRest 归档七天获救，“逼定价”能抄作业吗？ {#pgbackrest-forced-pricing}

pgBackRest 归档七天火速获赞助逆转绝非温情童话，而是把假装免费的公地按到死亡线上的“开源逼定价”：和平募捐无人理，只读断供逼商业方算清三笔账——换 Barman 重做演练极贵、自养团队 Fork 极贵，凑钱请原作者最便宜；不锁 MIT 代码只撤回个人时间信誉，用“消失”逼出了真实定价。但普通项目照搬必死：它能跑通全靠“不可替代、信誉极硬、Multigres 与 Percona 产品路线强绑定”三要素；即便如此，无基金会兜底的自律窗口也仅撑了三天，PGX Inc. 就因 SLA 压力抢拉了 `pgxbackup` 分叉。

- [pgBackRest 续命战与开源世界的逼定价 · 什么叫“逼定价”](/pg/pgbackrest-resume/#什么叫逼定价)：算清商业依赖方换工具、自养 Fork 与联合赞助的三笔经济账，解析不锁 MIT 代码只撤回个人信誉时间的博弈杠杆。
- [pgBackRest 续命战与开源世界的逼定价 · 这是一个特例吗？](/pg/pgbackrest-resume/#这是一个特例吗)：点明复现“归档逼定价”必须具备的不可替代性、个人信誉及金主产品路线强绑定三要素，剖析多金主联盟的后续磨合挑战。
- [pgBackRest 续命战与开源世界的逼定价 · 七天里发生了什么](/pg/pgbackrest-resume/#七天里发生了什么)：复盘归档七天内 Percona 呼吁克制与三天后 PGX Inc. 抢跑拉出 `pgxbackup` 分支的紧凑博弈，揭示纯靠行业自律协同的脆弱性。

### 团队被收购后子扩展为何断粮，接盘续命靠哪三板斧？ {#forking-mooncake-and-vchord}

初创团队一旦被大厂（如 Databricks 收编 Mooncake）收购，仓库常停摆且官网直跳买家；对架在 `pg_duckdb` 与 `pgrx` 上的子扩展 `pg_mooncake` 而言，底层 DuckDB 2.0 升级改接口便令其瞬间断粮。开源的 Free 是自由而非白嫖，原司锁仓时许可证赋予了下游另起炉灶守护 Immich 等万千用户的底牌。接盘硬核扩展靠三板斧：从归档快照捞回文档重建站点、升 0.3 硬核适配 `pg_duckdb 1.2` 与 `pgrx 0.19.3`、按年度大版本克制兜底——上游可跑路，发行版必须跨 PG 14–18 与 16 个系统稳稳接住。

- [开源接盘侠又来了：昨天 vchord，今天吃月饼 · 为什么要接盘 pg_mooncake？](/pg/fork-pg-mooncake/#为什么要接盘-pg_mooncake)：剖析初创团队被大厂收编后仓库停摆官网下线，导致强依赖父组件演进的 Rust 子扩展瞬间断粮失灵的连锁反应。
- [开源接盘侠又来了：昨天 vchord，今天吃月饼 · 老套路三板斧：抢救、续命、兜底](/pg/fork-pg-mooncake/#老套路三板斧抢救续命兜底)：总结从归档抢救重建文档站、紧扣 `pg_duckdb`/`pgrx` 依赖链升级续命、按年度大版本低频兜底的可持续接盘工程范式。
- [开源接盘侠又来了：昨天 vchord，今天吃月饼 · 上游可以跑路，发行版必须“稳稳接住”](/pg/fork-pg-mooncake/#上游可以跑路发行版必须稳稳接住)：阐明发行版作为软件供应链减震器的核心承诺——决不让上版本正常供应的扩展在下版本把真实生产用户晾在半空。
- [老冯又接盘新开源项目了 · 四、开源的 free，是自由](/pg/maintain-vchord/#四开源的-free是自由)：结合接盘 `vchord` 守护下游生态的实践，阐释开源许可证赋予社区在上游锁仓退场后合法分叉续命的自由底牌。

### 供应链昂贵，为何不是谁都能接盘孤儿项目或入官方源？ {#supply-chain-cost-and-stewardship-moat}

生产用开源稀缺的不是源码而是不断裂的供应链：维护近 600 扩展、月请求过亿的 `pgext.cloud` 需持续投入国内 CDN 与工程注意力；免费开放商业级仓库，是因为 AI 时代验证最贵，万千免费用户正是像 Cloudflare 免费层磨刀一样花钱买不到的全球众测团。孤儿项目十几个 Fork 唯极少数能活，因接盘须凑齐“重度自用绑定、十年验收判断力、Pigsty 分发渠道、叙事公信力”四拼图；进 PGDG 官方源同理——IBM `s390x` 因拉胯云机积压八小时且 20 个月零用户被清退，龙芯靠跨国寄送 3B6000 物理主板与真实用户盘子两月闭环入库。

- [老冯又接盘新开源项目了 · 五、代码免费，但供应链有成本](/pg/maintain-vchord/#五代码免费但供应链有成本)：对比 MinIO 删镜像引爆流水线的前车之鉴，算清维护月请求过亿、跨 16 个平台扩展仓库背后的带宽与人力注意力账单。
- [老冯又接盘新开源项目了 · 六、开源与商业化冲突吗？](/pg/maintain-vchord/#六开源与商业化冲突吗)：类比 Cloudflare 以免费层锤炼威胁情报的逻辑，阐明 AI 时代免费开源用户如何化身全球众测团反哺商业交付质量底盘。
- [老冯又接盘新开源项目了 · 七、接盘也不是谁都能接](/pg/maintain-vchord/#七接盘也不是谁都能接)：拆解成功接盘孤儿项目不可或缺的自用利益绑定、十年领域判断力、现成分发渠道与社区叙事公信力四项硬门槛。
- [龙芯，正式进入 PostgreSQL 官方仓库 · 凭什么给你干活？](/pg/pg-apt-loong64/#凭什么给你干活)：对比 IBM `s390x` 因拉胯云机与零用户被 PGDG 除名、龙芯凭寄送 3B6000 物理主板与真实用户基数两月入库的鲜明反差。
