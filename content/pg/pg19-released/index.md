---
title: "PostgreSQL 19 正式发布：又一个里程碑"
date: 2026-11-19
authors: [vonng]
summary: >
  PostgreSQL 19 正式发布，补齐序列逻辑复制、在线 REPACK、执行计划控制与备库“读己之写”等能力，简繁中文消息也完整就绪。聊聊新版本的关键变化、扩展生态适配，以及为什么建议生产环境等到 19.1。
tags: [PostgreSQL, PG管理, PG开发]
---

PostgreSQL 19 今天（11 月 19 日）正式发布了。先说结论：这是一个具有里程碑意义的大版本，也是 PG 30 周年（或者 40 周年）的特殊纪念版本。

PG 19 不靠某一个炫目的大特性撑场面，而是把运维和开发里好几块长期的短板一次补齐：逻辑复制终于能同步序列，`REPACK` 进了主干，规划器有了类似 hint 的控制手段，备库也能做“读己之写”了。

另外，从这个版本开始，[PostgreSQL 会说完整的简体中文和繁体中文了](/pg/pg-nls/)。老冯的名字，也出现在了 PG 19 的致谢名单之中，嘿嘿。

![PostgreSQL 19 发行说明致谢名单中的 Ruohang Feng](pg19-credits.webp)

这个版本来得并不容易。按往年节奏，大版本九、十月就该发布了；今年 Beta 4 先一口气砍掉五个大特性，又赶上 AI 漏洞挖掘带来的密集修复，一路拖到了 11 月中旬。经过这么一轮筛选，最终留下来的这些特性，含金量反而更高。

今天就聊聊 PG 19 里几个显著的变化，以及老冯的升级建议。文末附上官方发布新闻的中文翻译，以及本版本的致谢名单。

## 一、运维上的显著改进

**逻辑复制支持序列。** 这补上了基于逻辑复制做迁移的最后一块短板。以前用逻辑复制做大版本升级或跨机迁移，表里的数据能实时同步，序列值却不会跟过去。切换之前必须手工把每个序列推到正确位置，稍有疏漏就是主键冲突。PG 19 里，发布端可以用 `FOR ALL SEQUENCES` 发布序列，订阅端用 `ALTER SUBSCRIPTION ... REFRESH SEQUENCES` 把序列同步到与发布端一致。基于逻辑复制的迁移，终于可以做到真正意义上的无损切换。

逻辑复制的整体状态也更好了。以前 `wal_level` 没有提前设成 `logical`，想用逻辑复制就得重启数据库；现在即使用的是默认的 `replica`，创建第一个逻辑复制槽时也会自动提升生效的 WAL 级别，不再需要重启，门槛低了很多。此外还新增了发布时用 `EXCEPT` 排除部分表、用 `retain_dead_tuples` 检测更新与删除冲突等能力，也修掉了一大批历史问题。

**REPACK CONCURRENTLY。** PG 19 这次回滚了不少特性，`REPACK` 一度也被认为可能保不住，好在最终留了下来。以前老冯常说：“如果你在 PG 里只能装一个扩展，那就装 pg_repack。”现在这个能力总算进了 PG 主干，开箱即用：`REPACK` 统一了 `VACUUM FULL` 和 `CLUSTER`，加上 `CONCURRENTLY` 就能在不阻塞读写的情况下回收膨胀、重排数据。从 19 开始，就应该直接用官方的 `REPACK` 了；18 及以下版本，pg_repack 扩展依然是首选。

**查询规划器控制。** 新增的 `pg_plan_advice` 和 `pg_stash_advice` 补全了大家一直想要的、类似 hint 的能力。前者用一套“计划建议”迷你语言来固定或试验执行计划，后者按查询 ID 存储建议并自动应用。线上某条 SQL 的计划突然变差时，不用改应用代码就能把它按回去。

几个默认值的变化也值得留意：JIT 改为默认关闭，跑大型分析查询的要记得手动打开；TOAST 默认压缩算法从 `pglz` 换成了 `lz4`；MD5 密码认证成功后会报警告，还在用 MD5 的该迁到 SCRAM 了。

## 二、开发与功能上的改进

大家寄予厚望的 SQL/PGQ 属性图查询在 Beta 4 被撤回了，但 PG 19 依然新增了几个对开发极为实用的功能。

**`WAIT FOR LSN`。** 读写分离架构里有个老问题：刚在主库写完，立刻去从库读，可能读不到刚写的数据。现在可以在从库上先执行 `WAIT FOR LSN`，等它把 WAL 回放到指定位置再查询，从而保证“读己之写”的一致性。应用层不用再自己轮询复制延迟，也不必把这类读请求统统打回主库。

**`INSERT ... ON CONFLICT DO SELECT`。** 看起来只是个小改动，写 SQL 时却非常实用。常见的“有就取、没有就建”（get or create），以前要么拆成两条语句，要么用 `DO UPDATE SET x = x` 这类写法硬凑出 `RETURNING`，既别扭，又会产生无谓的行版本。现在冲突时直接 `DO SELECT ... RETURNING` 把已有的行返回来，还能顺手用 `FOR UPDATE` 加锁，一次网络往返搞定。

**全文检索与 pg_trgm 的 locale 修正。** 以前内置全文检索和 pg_trgm 做字符分类时，不管数据库用什么 locale provider，一律走 libc。在 ICU 或 builtin provider 的库里，尤其是 `LC_CTYPE` 为 `C` 的时候，中文等非 ASCII 字符就容易被处理错。PG 19 改为使用数据库自身的 locale provider，总算能正确处理好 locale 了。不过这是个不兼容变更：用 pg_upgrade 升级这类数据库后，要重建相关索引，并重新计算已存储的 `tsvector`。

## 三、PG 19 会说中文了

PG 19 还有一个 Release Notes 里没有写的亮点：它完整支持了简体中文和繁体中文。

PG 19 全部 28 个需要翻译的组件里，简繁中文的消息翻译全部达到了发布标准，和瑞典语、法语、德语等少数几种语言一样，属于完整支持的第一梯队。“装 PG 别把消息语言设成 zh_CN”这条老规矩，从这个版本开始可以作废了。顺带一提，这一轮小版本里，PG 14 到 18 的简体中文翻译也一并更新了。

这件事是老冯做的。简体中文随 19 Beta 4 进入上游，繁体中文紧跟其后，来龙去脉在《[PostgreSQL 中文版来了](/pg/pg-nls/)》和《[为什么要做 PostgreSQL 汉化？](/pg/pg-zh-tw/)》里讲过。翻译做完只是第一步，更难的是持续维护：上游的消息每天都在变。所以老冯搭了一套自动化机制，每天扫描上游源代码里的消息变更并跟进翻译。这意味着中文支持不是一锤子买卖，而是可以持久、长期地自动维护下去。

PG 19.0 的中文文档已经翻译完了，应该在一两个小时内就会更新到 [pgsql.cc/docs](https://pgsql.cc/docs/) 和 [pg.center/zh/docs](https://pg.center/zh/docs/) 中。其他的网站也会在近期相应更新引用。

## 四、生态适配与生产建议

老冯这两天在澳门出差，不过已经安排了 Agent 小弟们在后台跟进研发，推动 Pigsty 适配 PG 19。生态工具、扩展仓库、数据统计口径，都在按 PG 19 调整，这需要一点时间。

**生产版本：等 19.1。** 按老冯一贯的建议，PG 19 虽然很强，但严肃的生产环境，建议等第一个小版本 19.1 发布后再正式上线，通常要等三个月左右。这三个月也足够大量扩展完成适配。去年 PG 18 发布时，老冯也是同样的建议，详见《[PostgreSQL 18 可以上生产用了吗？](/pg/pg18-production-ready/)》。老冯自己升 19 肯定没问题，如果你有水平在线的 DBA，也可以。但对于普通用户来说，还是等 19.1 更稳妥。

扩展这块，大家大可放心。老冯作为“开源接盘侠”，会推着五六百个扩展往前走。上游不合并，老冯可以直接打补丁；上游彻底没了回音，老冯也可以直接接盘维护。前不久接下的 [vchord](/pg/maintain-vchord/) 和 [pg_mooncake](/pg/fork-pg-mooncake/) 就是现成的例子。不过扩展的适配总归需要一点时间，用 Rust 编写 PG 扩展的框架 pgrx 也发布了 0.20.0 版本，再加上这一次所有 C 扩展都要全量重新编译一遍，测试 QA 十几万个包也要花不少时间。

**普通小版本：别等，该升就升。** 如果你暂时不升 19，至少也应该把这一批小版本升上去。这批小版本一口气修复了 52 个 CVE 和 140 多个 Bug（详见《[开源渡劫：PG 小版本发布，修复 52 个漏洞](/pg/minor-earthquake/)》），正赶上数据库“渡劫”的关键期。PG 14 也随这批更新正式退役，还在用 14 的朋友，该规划大版本升级了。

其他软件最好也安排时间修一修。比如 Nginx 最近刚爆出的一个大问题，这种对外的门户组件，建议赶紧把 Nginx 官方上游仓库加上升级一下，尤其是服务直通公网的时候。别等到被人拿了权限再后悔。老实说，现在这些升级操作交给 coding agent 来干都相当简单，没有多复杂。纯断网环境下可能还得自己手工操作，但也不是什么大问题。老冯的建议就一句话：小版本该升就升。

**Pigsty 新版本。** Pigsty 也很快会放出新版本。之前已经有 PG 19 的配置模板，微调一下、改改仓库地址就能发。但要把 PG 19 提升为默认版本，至少要等三个月后 19.1 发布。

今天关于 PG 19 的内容就是这些。下面是官方新闻稿的翻译。

## 附录一：PostgreSQL 19 发布新闻（中文翻译）

原文：[PostgreSQL 19 Released!](https://www.postgresql.org/about/news/postgresql-19-released-3449/)，发布者：PostgreSQL 全球开发组。

2026 年 11 月 19 日——PostgreSQL 全球开发组今日宣布发布 PostgreSQL 19，这是世界上最先进的开源数据库的最新版本。

PostgreSQL 在关键业务场景中的应用持续快速增长，PostgreSQL 19 为此简化了大规模运行此类负载时的运维管理与应用开发。本版本引入了 `REPACK (CONCURRENTLY)` 命令，用户可以在不中断现有业务的情况下，针对当前负载优化表。借助新的 `pg_plan_advice` 扩展，PostgreSQL 19 让用户能更好地掌控执行计划的稳定性与查询性能。开发者会在这个版本中发现许多令人愉悦的特性：从备库上的“读己之写”一致性，到可节省一次网络往返的“获取或创建”行为。

“30 多年来，全球开源社区把 PostgreSQL 打造成了一款各类组织放心托付其最关键数据的数据库。”PostgreSQL 核心团队成员 Jonathan Katz 表示，“PostgreSQL 19 延续了对可靠性的承诺，为用户提供了在不中断业务的前提下管理负载、以及构建跨多个系统的应用的新方式。”

PostgreSQL 是一款以可靠性、健壮性和可扩展性著称的创新型数据管理系统，受益于全球开发者社区 30 年的开源开发，已成为各种规模组织首选的开源关系型数据库。

### 简化负载管理

经常发生更新和删除的表会积累未使用的空间，即所谓的“膨胀”（bloat），这也会严重影响查询性能。以往需要用 `VACUUM FULL` 和 `CLUSTER` 命令处理这一问题，但它们各有代价，包括在清理完成前阻止对表的访问。PostgreSQL 19 引入了 `REPACK` 命令，它可以回收这些空间，并能按某个索引重新排列表中的数据；使用 `REPACK (CONCURRENTLY)` 时，还能在不阻塞读写的情况下完成。`REPACK` 取代了 `VACUUM FULL` 和 `CLUSTER` 命令，后两者为兼容性仍然可用。

PostgreSQL 查询规划器通常会为每个查询选出高效的执行计划，但计划可能随数据变化而改变，有时新计划反而更慢。PostgreSQL 19 新增了 `pg_plan_advice` 扩展，可以稳定计划选择，并能用“计划建议”（plan advice）这一迷你语言试验不同的计划。配套的 `pg_stash_advice` 扩展会存储这些建议，并根据查询标识符自动应用到相应查询上，因此无需修改应用程序就能修复变慢的计划。

PostgreSQL 19 还帮助 autovacuum 在繁忙系统上跟上节奏。autovacuum 现在可以使用并行工作进程清理索引，由新参数 `autovacuum_max_parallel_workers` 控制，并使用新的评分系统决定优先处理哪些表。读取表的查询现在可以在执行期间自动在可见性映射中将页面标记为全可见，从而减少后续 vacuum 需要做的工作。此外，在未指定表时，`vacuumdb --analyze-only` 现在也会分析分区表。

本版本新增了多个用于监控负载的视图，包括按锁类型统计的 `pg_stat_lock`、展示恢复状态的 `pg_stat_recovery`，以及展示 autovacuum 如何为表排定优先级的 `pg_stat_autovacuum_scores`。`EXPLAIN ANALYZE` 新增的 `IO` 选项以及 `auto_explain` 中对应的设置，可以报告异步 I/O 活动。PostgreSQL 19 还会在 `pg_stat_wal`、`EXPLAIN (ANALYZE, WAL)` 以及 vacuum 和 analyze 的日志事件中，报告全页镜像写入的 WAL 量。

### 分布式数据改进

以前，PostgreSQL 往往需要重启服务器才能启用逻辑复制，这在生产环境中可能造成中断。PostgreSQL 19 简化了逻辑复制的初始化：在创建第一个逻辑复制槽时，会自动将实际生效的 WAL 级别提升到 `logical`。你可以通过新参数 `effective_wal_level` 查看当前使用的 WAL 级别。

PostgreSQL 19 还新增了序列值的逻辑复制，可以在 `CREATE PUBLICATION` 中使用 `FOR ALL SEQUENCES` 发布序列。`CREATE PUBLICATION` 还新增了 `EXCEPT` 子句，可在以 `FOR ALL TABLES` 发布时排除部分表；`CREATE SUBSCRIPTION` 现在可以通过 `SERVER` 子句，从外部服务器（例如用 `postgres_fdw` 定义的服务器）获取连接设置。此外，新的订阅选项 `retain_dead_tuples` 让 PostgreSQL 能够检测与并发删除相冲突的更新，这类冲突会计入 `pg_stat_subscription_stats`。

对于将读请求发往备库的应用，PostgreSQL 19 通过新的 `WAIT FOR LSN` 命令提供“读己之写”一致性。备库上的会话可以使用 `WAIT FOR LSN`，在执行查询前等待备库将预写式日志（WAL）回放到指定的日志序列号（LSN），这样应用就能读到刚刚在主库上写入的数据。

PostgreSQL 19 还改进了对外部表的查询。借助新的 `import_stats` 选项，`postgres_fdw` 在执行 `ANALYZE` 时可以直接从远程服务器导入表统计信息，而不必对远程表进行行采样，这有助于查询规划器选出更好的计划。

### 开发体验与性能增强

PostgreSQL 19 新增 `INSERT ... ON CONFLICT DO SELECT`，允许 `RETURNING` 子句返回与插入相冲突的已有行，从而简化常见的“获取或创建”模式。`COPY` 现在可以将数据输出为 JSON（包括输出为单个 JSON 数组），SQL/JSON 路径语言也新增了 `lower()`、`upper()`、`replace()`、`split_part()` 和 `btrim()` 等字符串方法。此外，窗口函数 `lead()`、`lag()`、`first_value()`、`last_value()` 和 `nth_value()` 现在可以使用 `IGNORE NULLS` 跳过 `NULL` 值。`random()` 函数现在还可以在指定范围内生成随机日期和时间戳。

本版本还让许多负载在无需修改应用的情况下变得更快。PostgreSQL 19 提升了外键检查的性能——在测试中使批量插入快了近 2 倍；同时新增了更多查询规划器优化，例如在不存在 `NULL` 值时将 `NOT IN` 子句转换为更高效的反连接（anti-join），以及在连接之前执行提前聚合（eager aggregation）以减少需要处理的行数。PostgreSQL 19 还在 PostgreSQL 18 引入的异步 I/O 子系统基础上更进一步：当 `io_method` 设为 `worker`（默认值）时，PostgreSQL 现在会在新参数 `io_min_workers` 与 `io_max_workers` 之间自动调整 I/O 工作进程的数量，这两个参数取代了原来的 `io_workers`。在多通道负载中使用 `LISTEN` 和 `NOTIFY` 交换通知时，可扩展性也有所提升。

最后，新参数 `password_expiration_warning_threshold` 会在用户密码即将过期时发出警告。

### 其他值得关注的变更

PostgreSQL 19 新增服务器端的服务器名称指示（SNI）支持，单个 PostgreSQL 服务器可以根据客户端连接时使用的主机名，出示不同的 TLS 证书。你可以在新的 `pg_hosts.conf` 文件中配置主机名与证书、密钥的映射。PostgreSQL 19 现在还会在 `md5` 密码认证成功后发出警告，可通过 `md5_password_warnings` 参数关闭。`md5` 密码认证已在 PostgreSQL 18 中被弃用，并将在未来的版本中移除。如果需要基于密码的认证，请使用 SCRAM 认证。本版本还移除了对 RADIUS 认证的支持。

即时编译（JIT）现在默认禁用，因为 PostgreSQL 用来决定何时启用 JIT 的代价估算已被证明并不可靠。如果你运行大量大型分析查询，可能需要启用 JIT。当 PostgreSQL 构建时带有 LZ4 支持，默认的 TOAST 压缩方法现在是 `lz4`。

### 其他特性

PostgreSQL 19 还加入了许多其他新特性和改进，可能同样适用于你的场景。完整的新增与变更特性列表，请参阅[发行说明](https://www.postgresql.org/docs/19/release-19.html)。

### 关于 PostgreSQL

PostgreSQL 是世界上最先进的开源数据库，拥有由数千名用户、贡献者、公司和组织组成的全球社区。自 40 多年前诞生于加州大学伯克利分校以来，PostgreSQL 一直保持着无与伦比的发展速度。PostgreSQL 成熟的功能集不仅能与顶级商业数据库系统相匹敌，更在高级数据库特性、可扩展性、安全性和稳定性方面超越了它们。

## 附录二：PostgreSQL 19 致谢名单

以下人士（按字母顺序）作为补丁作者、提交者、审阅者、测试者或问题报告者，为本版本做出了贡献。名单取自[官方发行说明](https://www.postgresql.org/docs/19/release-19.html#RELEASE-19-ACKNOWLEDGEMENTS)。

这次名单太长了，完整列表请参阅：[PostgreSQL 19 致谢名单](https://www.postgresql.org/docs/19/release-19.html#RELEASE-19-ACKNOWLEDGEMENTS)。

![桌上的 PostgreSQL 小象与社区纪念徽章](slonik.webp)

## 延伸阅读

- 2026-11-06：[渡劫期的 PostgreSQL 生态大更新](/pg/eco-update-202611/)
- 2026-11-05：[开源接盘侠又来了：昨天 vchord，今天吃月饼](/pg/fork-pg-mooncake/)
- 2026-11-04：[老冯又接盘新开源项目了](/pg/maintain-vchord/)
- 2026-10-31：[工业流水线：一天翻译完 30 本 PG 书籍](/pg/translate-30-books/)
- 2026-10-22：[当互联网真被打成筛子](/cloud/net-attack/)
- 2026-10-21：[当云被打成筛子](/cloud/blackwall/)
- 2026-10-12：[复兴 PostgreSQL 中文社区](/pg/revive-pg-cn-community/)
- 2026-10-10：[为什么要做 PostgreSQL 汉化？](/pg/pg-zh-tw/)
- 2026-09-25：[PostgreSQL 19 Beta 4 发布：特性大砍](/pg/pg19b4-release/)
- 2026-09-19：[PostgreSQL 中文版来了](/pg/pg-nls/)
- 2026-09-10：[PG 中文文档发布：11 个大版本，一个不落](/pg/pgsql-cc-online/)
- 2026-08-14：[井喷：修了 28 个 CVE、110 个 BUG，PG 最新小版本发布](/pg/pg-186-cve/)
- 2026-05-15：[PostgreSQL 18.4、17.10、16.14、15.18 与 14.23 发布](/pg/pg-184-release/)
- 2026-05-05：[pgBackRest 续命战与开源世界的逼定价](/pg/pgbackrest-resume/)
- 2026-02-26：[PostgreSQL 号外紧急补丁版本发布！](/pg/pg-emergency-patch/)
- 2026-02-19：[号外：暂缓 PG 最新小版本安装与升级](/pg/pg-out-of-sync-202602/)
