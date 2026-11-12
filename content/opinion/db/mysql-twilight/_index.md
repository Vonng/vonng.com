---
title: MySQL 谢幕、跑分真相与黑稿祛魅
linkTitle: MySQL 谢幕与跑分
description: MySQL 正确性破产与治理死局、Uber 弃 PG 考古祛魅、压测玄学与客观选型。
weight: 20
icon: fa-solid fa-scale-unbalanced
---

MySQL 的历史谢幕并非败给营销，而是死于事务正确性破产、新版本性能倒退与私有产权加云白嫖的公地悲剧。剥去跑分刷榜与钓鱼黑稿的迷雾，存量向 PostgreSQL 单向置换的大局早已注定。

## 一、功能空心化、性能倒退与正确性破产 {#mysql-collapse}

### MySQL 9.x 的向量与新优化器究竟有多少干货？ {#mysql-9x-cold-leftovers}

从 9.0 到 8.0 停服后唯一的长期支持版 9.7 LTS，MySQL 端出的始终是敷衍冷饭：开源版与商业版 `VECTOR` 连跨八个版本仍是换皮 `BLOB`，连十行 C 代码的距离函数与向量索引都死锁在 Oracle HeatWave 云上；企业版独占的 JS 存储过程比 PG `plv8` 晚了 13 年；迟到五年的 Hypergraph 优化器默认关闭且不支持 Hint 与传统 `EXPLAIN`。反观 PG 早已卷出一年提速 150 倍的向量扩展群。

- [MySQL 9.7：还是那碗冷饭 · 花架子依旧的向量能力](/db/mysql-97-bye/#花架子依旧的向量能力)
- [MySQL vs PostgreSQL @ 2025 · 新功能](/db/mysql-vs-pgsql/#新功能)
- [MySQL安魂九霄，PostgreSQL驶向云外 · 糊弄了事的向量类型](/db/mysql-is-dead/#糊弄了事的向量类型)

### 简单读写 MySQL 更快吗，为何海量用户死守 5.7？ {#mysql-8x-perf-regression}

“简单读写 MySQL 更快”的旧教条早已破产，它正深陷“版本越新、性能越差”的怪圈。Mark Callaghan 与 Marco Tusa 在 `sysbench` 及 TPC-C 下的回归压测一致证实：MySQL 8.0/8.4 相比 5.6/5.7 吞吐暴跌 20%～40%，死守 5.7 完全是规避 TPS 折损的理性自保。诚如 Peter Zaitsev 所批驳，这是 Oracle 长期漠视性能工程的恶果；同期 PG 17 写入较 PG 10 反涨 30%～70%，重度写吞吐已呈 2～5 倍碾压。

- [MySQL vs PostgreSQL @ 2025 · 性能劣化的 MYSQL](/db/mysql-vs-pgsql/#性能劣化的-mysql)
- [MySQL安魂九霄，PostgreSQL驶向云外 · 越新越差的性能表现](/db/mysql-is-dead/#越新越差的性能表现)
- [MySQL性能越来越差，Sakila将何去何从？ · 这些测试说明了什么？](/db/sakila-where-are-you-going/#这些测试说明了什么)
- [Oracle最终还是杀死了MySQL · 参考阅读](/db/oracle-kill-mysql/#参考阅读)

### 调参与换分支能救 MySQL 8.x 吗，缺并行后果如何？ {#mysql-tuning-and-parallelism}

靠调参或换分支难以扭转颓势。Marco Tusa 实测表明，官方 MySQL 8.0 默认参数在小数据集下表现稀烂，手工深调才勉强逼近 5.7；高并发争用下官方 8.4 仅强于垫底的 MariaDB 11.3，唯 Percona 8.0 能稳住吞吐。更致命的是，如 Peter Zaitsev 警告，面对动辄数百核的现代服务器，开源 MySQL 至今拒不支持并行查询，连简单 `GROUP BY` 都卡在单核，人为设卡推销专有云只会逼走开发者。

- [MySQL性能越来越差，Sakila将何去何从？ · 与 Percona 的 MySQL 和 MariaDB 比会怎样？](/db/sakila-where-are-you-going/#与-percona-的-mysql-和-mariadb-比会怎样)
- [Oracle最终还是杀死了MySQL · 参考阅读](/db/oracle-kill-mysql/#参考阅读)

### MySQL 默认可重复读真能防异常吗，真实水位如何？ {#mysql-rr-jepsen-collapse}

金融账务系统绝不可轻信 MySQL 的 ACID 承诺——其 8.0 默认可重复读（RR）公然违背官方文档快照保证。Jepsen 对 8.0.34 的实测揭露：RR 事务先读某列、仅更新同行另一列后重读，9048 个事务中竟有 126 个读到外部并发新值，一次本地写入便引狼入室破坏快照！Elle 检测更证实它连单调原子视图（MAV）底线都已击穿，真实正确性劣于 PG 的读已提交，外加超万张表重启即崩的硬伤。

- [MySQL正确性竟如此垃圾？ · 隔离性问题：不可重复读](/db/bad-mysql/#隔离性问题不可重复读)
- [MySQL正确性竟如此垃圾？ · 原子性问题：非单调视图](/db/bad-mysql/#原子性问题非单调视图)
- [MySQL vs PostgreSQL @ 2025 · 正确性](/db/mysql-vs-pgsql/#正确性)

### 开串行化或降 RC 手工加锁能补救正确性吗？ {#mysql-sr-and-rc-for-update}

两条补救路全是深坑。开启 MySQL Serializable 纯属鸡肋：云 RDS 旧默认参数会在副本诱发 G2 撕裂读，且如李海翔“一致性八仙图”所示，它靠昂贵死锁检测硬扛冲突，吞吐骤降。而“降到 RC 再满地写 `SELECT FOR UPDATE`”是向业务转嫁并发控制，实测人肉锁争用更伤性能且易漏锁错账；反观 PG 的 SSI 仅以微弱开销便兑现了真串行化。

- [MySQL正确性竟如此垃圾？ · 串行化问题：鸡肋且糟糕](/db/bad-mysql/#串行化问题鸡肋且糟糕)
- [MySQL正确性竟如此垃圾？ · 正确性与性能的利弊权衡](/db/bad-mysql/#正确性与性能的利弊权衡)
- [MySQL安魂九霄，PostgreSQL驶向云外 · 无可救药的质量水平](/db/mysql-is-dead/#无可救药的质量水平)

## 二、治理死局、三国终局与增量易主 {#governance-and-verdict}

### 究竟是谁杀死了 MySQL，PG 生态又该如何鉴戒？ {#who-killed-mysql}

杀死 MySQL 的是“Oracle 独占产权加云巨头搭便车白嫖”的公地悲剧。据 Peter Zaitsev 与 Marco Tusa 复盘，收购 Sun 后稳健十余年的 Oracle 眼看 AWS 等拿开源内核狂赚数十亿美元却零回馈，遂为强推 HeatWave 大裁核心研发、退回黑盒开发并把性能与新特性锁死上云，逼得 Percona 连跳七个 9.x 创新版。PG 虽靠中立社区免疫单厂绑架，仍须靠 Pigsty 等开源本地发行版制衡公有云闭源管控锁定。

- [MySQL 9.7：还是那碗冷饭 · MySQL 为什么会变成这样？](/db/mysql-97-bye/#mysql-为什么会变成这样)
- [Oracle最终还是杀死了MySQL · 参考阅读](/db/oracle-kill-mysql/#参考阅读)
- [MySQL性能越来越差，Sakila将何去何从？ · 一些思考](/db/sakila-where-are-you-going/#一些思考)
- [MySQL vs PostgreSQL @ 2025 · 究竟是谁杀死了 MySQL？](/db/mysql-vs-pgsql/#究竟是谁杀死了-mysql)
- [MySQL安魂九霄，PostgreSQL驶向云外 · 究竟是谁杀死了 MySQL？](/db/mysql-is-dead/#究竟是谁杀死了-mysql)

### 两大分支为何难挽败局，MySQL 阵营还有出路吗？ {#can-mysql-camp-catchup}

现有分支已难挽狂澜。如 Peter Zaitsev 拆解：架构上 MySQL 缺失自定义类型与可插拔索引，断了向量时代创新根基；治理上 Oracle 独占商标、双许可并强制签 CLA，扼杀了友商共建。Percona 受制于 100% 兼容包袱不敢大改，MariaDB 则严重分叉失配且商业体被私募收购。若 Oracle 拒绝将社区版捐给中立基金会，MySQL 阵营唯一生路只剩效仿 Valkey 联手换牌分叉重生。

- [MySQL还有机会赶上PostgreSQL吗？ · 所有权和治理](/db/can-mysql-catchup/#所有权和治理)
- [MySQL还有机会赶上PostgreSQL吗？ · 架构](/db/can-mysql-catchup/#架构)
- [MySQL还有机会赶上PostgreSQL吗？ · 总结](/db/can-mysql-catchup/#总结)
- [Oracle还能挽救MySQL吗？ · 参考阅读](/db/can-oracle-save-mysql/#参考阅读)

### 关系型“三国演义”中，治理与基因如何决定胜负？ {#governance-and-trilogy}

主流关系型博弈拼的是“德才兼备”：Oracle 技术深厚但授权天价、法务横行，属“有才无德”；MySQL 靠早年“糙猛快”走红，等 PG 补齐快与猛后只剩允许报错事务部分提交的“糙”，属“才浅德薄”。PG 凭独立社区、类 BSD 协议与优质源码孕育繁荣插件生态；反观 Oracle 2025 年裁撤半数 MySQL 研发，逼得 PlanetScale 上线 PG，老兵联署承认其沦为遗产。

- [PostgreSQL：最成功的数据库 · 但是，为什么呢？](/pg/pg-is-no1/#但是为什么呢)
- [为什么PostgreSQL是最成功的数据库？ · vs MySQL](/pg/pg-is-best/#vs-mysql)
- [PostgreSQL vs MySQL 2026 · 六、社区治理](/pg/pg-vs-mysql-2026/#六社区治理)
- [PostgreSQL vs MySQL 2026 · 二、厂商战略动向](/pg/pg-vs-mysql-2026/#二厂商战略动向)
- [PostgreSQL好处都有啥 · 生态健康](/pg/pg-is-good/#生态健康)

### 为什么说 PG 已赢下增量世界，而 MySQL 沦为遗产？ {#pg-vs-mysql-verdict}

超大规模选型以 2010 年为分水岭：Meta、GitHub 等 MySQL 案例皆属历史遗存；此后崛起的 OpenAI、Figma、Notion、探探与过半 YC 新创项目清一色默认选 PG。Docker Hub 周拉取量 3.8:1、AWS 实例比 3:2、Aurora DSQL 弃用 MySQL 以及 Vercel 存储零推荐，均宣告增量彻底易主。六年份额涨跌相关系数高达 `r = -0.96`，坐实存量正单向置换为 PG 增量，踏空 AI 的 MySQL 终将退化为数据库界的 PHP。

- [PostgreSQL vs MySQL 2026 · 七、总体判断](/pg/pg-vs-mysql-2026/#七总体判断)
- [PostgreSQL vs MySQL 2026 · 时代特征](/pg/pg-vs-mysql-2026/#时代特征)
- [PostgreSQL取得对MySQL的压倒性优势](/pg/pg-beats-mysql/)
- [如何看待 MySQL vs PGSQL 直播闹剧 · MySQL 的用户都流失到哪儿去了？](/pg/mysql-pg-live-drama/#mysql-的用户都流失到哪儿去了)

### 中外数据库演进为何差十年，人群结构如何迁移？ {#ten-year-lag-and-demographics}

全球搜索指数显示，各国 PG 与 MySQL 热度差同发达程度呈 `r = 0.6` 强正相关，美俄早已反超；中国曲线右移约十年，MySQL 至 2015 年才见顶，这正是国内曾叹 PG 熟手难招的成因。拆解 9 万份画像：5.6% 新手偏爱 MySQL 入门，94.4% 专业开发者青睐 PG，唯一显著流向便是从 MySQL 单向升迁至 PG——死守旧栈无异于押注电子管而错失晶体管。

- [如何看待 MySQL vs PGSQL 直播闹剧 · 菜鸟都在哪儿呢？](/pg/mysql-pg-live-drama/#菜鸟都在哪儿呢)
- [如何看待 MySQL vs PGSQL 直播闹剧 · 哪些国家 PostgreSQL 更流行？](/pg/mysql-pg-live-drama/#哪些国家-postgresql-更流行)
- [驳《MySQL：这个星球最成功的数据库》 · 中国特色](/pg/rebut-mysql-best/#中国特色)
- [PostgreSQL好处都有啥 · 问题](/pg/pg-is-good/#问题)

## 三、榜单祛魅、薪资溢价与跑分真相 {#benchmarks-and-myths}

### 搜索指数与“中国加权”为何推翻不了 PG 第一？ {#rebut-dbengines-and-china-weight}

拿 DB-Engines 总榜否定 PG 第一站不住脚：它只是抓热搜词的二手指数，分不清喜爱还是报错踩坑，又让有五种拼写的 PG 吃亏，效力远逊 9 万样本一手问卷——何况其编辑部八年五授 PG 年度冠军。即便按 8% 中国权重与百度指数强行校正，全球流行度仍是 PG（43.46%）压过 MySQL（43.24%）；AWS 全球实例早已 1:1 且 PG 营收反超，“0.1% 营收”纯属谣言。

- [驳《MySQL：这个星球最成功的数据库》 · 搜索引擎指数更权威？](/pg/rebut-mysql-best/#搜索引擎指数更权威)
- [PostgreSQL荣获2024年度数据库之王！（第五次） · 让我们来看看更多详细的数据](/pg/pg-dbeng-2024/#让我们来看看更多详细的数据)
- [驳《MySQL：这个星球最成功的数据库》 · 中国加权校正后的估算流行度](/pg/rebut-mysql-best/#中国加权校正后的估算流行度)
- [驳《MySQL：这个星球最成功的数据库》 · PostgreSQL 营收是 MySQL 0.1%？](/pg/rebut-mysql-best/#postgresql-营收是-mysql-01)

### 用 PG 的开发者真能比用 MySQL 多赚四成吗？ {#pg-developer-salary-premium}

就业市场早已用真金白银给出定价。核算全球 44,354 份专业开发者薪酬样本，PG 开发者年薪中位数（62.5 万元）比 MySQL（54.3 万元）高出 15%，样本超 600 人的全部 31 个国家无一例外满足 PG 高于全体均值、全体均值高于 MySQL 的铁律。而在受早期大厂路径依赖影响、PG 采用率仅 27.6% 的中国市场，人才稀缺直接将 PG 中位数（42.1 万元）推至 MySQL（30.8 万元）的 1.37 倍，成为跳出 CRUD 内卷的最优杠杆。

- [用PG的开发者，年薪比MySQL多赚四成？ · 太长不看](/pg/pg-dev-salary/#太长不看)
- [用PG的开发者，年薪比MySQL多赚四成？ · 关键发现](/pg/pg-dev-salary/#关键发现)
- [用PG的开发者，年薪比MySQL多赚四成？ · 关于数据库流行度](/pg/pg-dev-salary/#关于数据库流行度)
- [为什么PostgreSQL前途无量？ · 弃暗投明？](/pg/pg-is-great/#弃暗投明)

### 单机 PG 性能极限有多强，对决 MySQL 谁更快？ {#single-node-pg-extreme-perf}

现代多核与 NVMe 已将单机 PG 武装成吞吐怪兽：亿级行 `pgbench` 实测中，10 核 M1 Max 即达 24 万点查 QPS，96 核 `c5d.metal` 物理机常规安全配置跑出 62.6 万点查与 7.2 万读写 TPS，极限调优更飙至 200 万 QPS 与 13.7 万 TPS。至于 MySQL 官网炫耀的百万点查，实为关停 Binlog、`fsync` 与双写的非生产刷分；若对等卸除落盘约束同台对决，PG 点查直冲 233 万 QPS，同限 48 并发仍超 MySQL 峰值 43%。

- [PostgreSQL 到底有多强？ · PGBENCH](/pg/pg-performence/#pgbench)
- [PostgreSQL 到底有多强？ · Dirty Hack](/pg/pg-performence/#dirty-hack)

### “慢 360 倍”黑稿与刷榜 TPC-C 耍了什么把戏？ {#debunk-360x-and-tpcc}

网传“PG 慢 360 倍”是不敢贴复现脚本的钓鱼黑稿：故意挂起长空闲事务锁死快照阻塞回收，再刷百万行更新制造死元组堆积——如同关掉垃圾回收器证明语言慢，生产靠空闲超时与 HOT 更新早已杜绝。同理，斥数亿元堆机器刷十年无人问津的三十年前 TPC-C 老榜，参考价值不如 `sysbench`，纯属透支信誉的营销放卫星。

- [PG被黑慢MySQL 360倍，这次我真忍不了 · PostgreSQL vs MySQL @ 2025](/pg/pg-360x-slower/#postgresql-vs-mysql--2025)
- [如何看待 MySQL vs PGSQL 直播闹剧 · 更新：关于打榜 SB 行为](/pg/mysql-pg-live-drama/#更新关于打榜-sb-行为)
