---
title: 选型与路线之争
linkTitle: 选型与路线之争
description: 数据库需求金字塔、MySQL 谢幕与 PostgreSQL 胜出、MongoDB 与专用向量库祛魅、AI 状态库终局。
weight: 10
icon: fa-solid fa-scale-balanced
---

绝大多数商业软件本质上都是数据密集型应用——前端皮肤会坍缩为对话框，后端胶水会被智能体吞噬，唯独对抗物理断电与并发竞态的数据库状态机是穿越周期的不变量。过去十年间，受困于单一商业公司产权垄断与公有云白嫖死循环的 MySQL 已在正确性、性能与多模创新上全面掉队，无模式文档库与独立向量库亦在祛魅后退潮；而四十年前种下“可扩展性”种子的 PostgreSQL，正凭中立治理与上千款生态插件加冕为数据库世界的 Linux 内核，携手端侧 SQLite 与分析引擎 DuckDB 重塑 AI 时代的数据底座。本篇系统拆解选型第一性原理、MySQL 谢幕始末、去 O 事务对比、NoSQL 与向量库祛魅、湖仓超融合以及 Agent 原生数据库的终局脉络。

## 一、选型第一性原理与数据库需求金字塔 {#principles-and-pyramid}

### 为什么学透数据库原理比死磕算法更能决定上限？ {#why-learn-db-principles}

除科学仿真、模型训练与游戏引擎外，绝大多数系统都是数据密集型应用——业务代码只是搬运数据的胶水，“数据表就是数据结构，索引与查询就是算法”，在数据库面前后端也是前端。范式理论、关系代数、ACID 隔离与 WAL 复制绝非象牙塔教条，而是平衡冗余复杂度、用 GiST 树把秒级 KNN 压进 1 毫秒换千倍提速、防高并发错账与脑裂丢数的实战武器。切忌脱离实战空背概念，先上手 PostgreSQL 与 Redis 做出真实系统，被慢 SQL 和并发竞态折磨后再结合《DDIA》反刍内核，方能进阶为真正的架构师。

- [为什么要学习数据库原理](/db/why-learn-database/)：阐明“表即数据结构、索引与查询即算法”的栈底逻辑，串联范式、关系代数、ACID、WAL 的生产价值与“先实战踩坑再反刍原理”的学习路径。

### 生产数据库的准入底线与高阶比拼维度是什么？ {#db-demand-pyramid}

类比马斯洛模型，内核 ACID 正确性（生理）与防泄密、冷备加 WAL 时间点恢复（安全）是生产不可妥协的底线，兜不住这两层只是会令企业破产的残次品。多副本高可用与监控告警仅算有人照看的“归属本分”，拉开选型段位的“尊重需求”是性能、硬件账单与管理复杂度的综合 ROI——公有云 RDS 正因高昂溢价在此失了体面。再往上，“没有观测就谈不上控制”，唯有让数字化的全栈可观测性（感知）与声明式基础设施即代码（行动）互为对偶，叠加大模型将专家 SOP 产品化（决策），才能迈向自治圣杯。

- [数据库需求层次金字塔 · 安全需求](/db/demand-pyramid/#安全需求)：界定 ACID 事务正确性与冷备加 WAL 归档兜底的数据可恢复性为生产数据库不可妥协的准入及格线。
- [数据库需求层次金字塔 · 尊重需求](/db/demand-pyramid/#尊重需求)：提出以性能、成本与管理复杂度的综合比值（ROI）衡量产品竞争力，剖析公有云 RDS 的高溢价短板。
- [数据库需求层次金字塔 · 审美需求](/db/demand-pyramid/#审美需求)：构建可观测感知、声明式 IaC 控制与大模型智能决策三位一体的数据库自治演进路线。

### 为什么有硬伤的默认选型能横行，如何打破惯性？ {#mysql-baijiu-obedience-test}

互联网行业的 MySQL 就像酒桌上的高度白酒，是借早期 LAMP 与大厂权威塑造成的“服从测试”——选它意味着随大流踩坑而无需担责，提议 PostgreSQL 则要写报告独自背负“非主流”风险。选型更是暴露思维惰性的“吐真剂”：嘴上嫌 PG 学习曲线陡，身体却花三年背诵把子查询改 JOIN、拿中间表替 CTE、靠外部工具补锁表 DDL 的擦屁股套路，本质是为逃避认知失调而死守舒适区。默认绝不等于合适，好数据库应当让人舒适而非逼人给烂设计打补丁。

- [MySQL与白酒：互联网行业的服从测试 · 三、服从测试](/db/mysql-baijiu/#三服从测试)：以酒桌白酒文化类比互联网默认选型惯例，揭示组织避责政治如何压倒严肃的技术评估。
- [MySQL与白酒：互联网行业的服从测试 · 五、吐真剂](/db/mysql-baijiu/#五吐真剂)：拆穿“够用了”“学习曲线陡”等选型托词背后的从众心理、技术投资失误与认知防御机制。
- [MySQL与白酒：互联网行业的服从测试 · 七、选择的勇气](/db/mysql-baijiu/#七选择的勇气)：批判替糟糕内核设计打补丁的所谓“最佳实践”，倡导回归服务于人的工程标尺独立决策。

### 该走专业化还是一体化，主从架构上限有多高？ {#monolith-pg-vs-sharding}

现代硬件与插件生态已把选型钟摆推回“一体化”：PostgreSQL 就像智能手机，两千万条乃至十几 TB 向量用 `pgvector` 轻松拿捏，几十 TB 内根本犯不着碰分布式库。正如 OpenAI 工程师 Bohan Zhang 披露，ChatGPT 仅凭未分片的“一主四十多从”PG 便扛下百万 QPS 与五亿月活，击碎了“高并发必分库分表”迷思。而按 Matt Blewitt 剖析，FoundationDB（单事务限 10MB/5 秒）、TigerBeetle（Zig 加确定性仿真专攻账本）与 CockroachDB 等专用库，唯有靠严苛“自我设限”才能在百 TB 强一致或跨洲容灾等窄域立足。

- [AI时代的数据库与DBA将何去何从 · 一体化还是专业化，如何选型？](/db/ai-dba-job/#一体化还是专业化如何选型)：用“智能手机”隐喻论证几十 TB 以内优先采用一体化 PostgreSQL 以免除跨异构系统的一致性与运维税。
- [OpenAI：将PostgreSQL伸缩至新阶段 · 结果](/db/openai-pg/#结果)：披露 OpenAI 未分片单主加 40 余只读副本支撑五亿月活、百万级 QPS 且九个月仅一次零级事故的生产实绩。
- [七周七数据库（2025年） · 分层数据库](/db/7-week-7-db/#分层数据库)：剖析 FoundationDB、TigerBeetle 与 CockroachDB 如何通过硬性边界约束换取百 TB 事务、金融零容错与跨地域强一致能力。

## 二、MySQL 谢幕：正确性破产、性能倒退与治理死局 {#mysql-twilight-and-oracle}

### MySQL 9.x 的向量支持与新优化器有多少干货？ {#mysql-9x-cold-leftovers}

从时隔八年发布的 9.0 到 8.0 EOL 后唯一的长期支持版 9.7 LTS，MySQL 端出的始终是敷衍冷饭：社区版与商业版 `VECTOR` 连跨八个版本仍是换皮 `BLOB`，连十行 C 代码的 `DISTANCE()` 函数与向量索引都死锁在 Oracle HeatWave 云上，逼得各家分支另造轮子；企业版独占的 JS 存储过程比 PG `plv8` 晚了 13 年；迟到五年的 Hypergraph 优化器默认关闭，且不支持 Hint 与传统/JSON `EXPLAIN`，抽风只能在生产裸奔。反观 PG 早已卷出一年提速 150 倍的向量扩展群与实时列存。

- [MySQL 9.7：还是那碗冷饭 · 花架子依旧的向量能力](/db/mysql-97-bye/#花架子依旧的向量能力)：实锤 MySQL 9.0 至 9.7 向量类型仍为无距离函数与索引的空壳，并揭露 Hypergraph 优化器默认关闭且缺乏 Hint 与 `EXPLAIN` 干预手段。
- [MySQL vs PostgreSQL @ 2025 · 新功能](/db/mysql-vs-pgsql/#新功能)：对比 PostgreSQL 向量生态一年 150 倍跃升及 T0 级 OLAP 进击与 MySQL 9.x 换皮 `BLOB`、锁死企业版老特性的巨大代差。
- [MySQL安魂九霄，PostgreSQL驶向云外 · 糊弄了事的向量类型](/db/mysql-is-dead/#糊弄了事的向量类型)：解剖 MySQL 9.0 仅提供 `VECTOR_DIM` 的残缺向量文档与迟到 13 年的企业版 JS 函数如何令其再度踏空 AI 浪潮。

### 简单读写 MySQL 更快吗，为何海量用户死守 5.7？ {#mysql-8x-perf-regression}

这条旧教条早已破产——MySQL 正陷入“版本越新、性能越差”的怪圈。Mark Callaghan 与 Percona 专家 Marco Tusa 在 sysbench 和 TPC-C 下的回归测试一致证实：MySQL 8.0/8.4 相比 5.6/5.7 吞吐暴跌 20%～40%，冒风险升级反遭惨重 TPS 折损，死守 5.7 完全是理性的工程自保。诚如 Peter Zaitsev 所批驳，这绝非加功能的必然代价，而是 Oracle 长期漠视性能工程的恶果；同期 PostgreSQL 17 写入较 PG 10 反涨 30%～70%，读吞吐高出 MySQL 25%～100%，重度写场景更达 2～5 倍碾压。

- [MySQL vs PostgreSQL @ 2025 · 性能劣化的 MYSQL](/db/mysql-vs-pgsql/#性能劣化的-mysql)：汇总 Mark Callaghan 回归测试与 JuiceFS 元数据实测，展示 MySQL 8.x 吞吐暴跌 25%～40% 而 PG 17 读写全面反超的量化账本。
- [MySQL安魂九霄，PostgreSQL驶向云外 · 越新越差的性能表现](/db/mysql-is-dead/#越新越差的性能表现)：对比五年间 MySQL 性能持续滑坡与 PostgreSQL 写入跃升 30%～70% 的剪刀差，宣告简单 OLTP 性能神话瓦解。
- [MySQL性能越来越差，Sakila将何去何从？ · 这些测试说明了什么？](/db/sakila-where-are-you-going/#这些测试说明了什么)：呈现 Marco Tusa 在不同数据集与隔离级别下的 sysbench 及 TPC-C 跑分，证实 5.7 吞吐全面领先 8.0 与 8.4。
- [Oracle最终还是杀死了MySQL · 参考阅读](/db/oracle-kill-mysql/#参考阅读)：援引单线程负载剧烈退化数据，戳穿“功能迭代必然牺牲性能”借口并指向 Oracle 对性能工程团队的长期忽视。

### 调参与换分支能救 MySQL 8.x 吗，缺并行后果如何？ {#mysql-tuning-and-parallelism}

靠调参或换分支难以扭转颓势。Marco Tusa 实测表明，官方 MySQL 8.0.36 默认参数在小数据集下表现稀烂，手工深调才能逼近 5.7（逼得 Oracle 在 8.4 LTS 紧急大改默认值）；而在高并发锁争用下，官方 8.4 仅强于垫底的 MariaDB 11.3，唯有 Percona 8.0.36 能勉强稳住吞吐。更致命的是，如 Peter Zaitsev 警告，面对动辄数百核的现代 CPU，开源 MySQL 仍拒不支持并行查询，连简单的 `GROUP BY` 都卡在单核，人为设卡推销 HeatWave 只会把开发者推向 PostgreSQL 与 ClickHouse。

- [MySQL性能越来越差，Sakila将何去何从？ · 与 Percona 的 MySQL 和 MariaDB 比会怎样？](/db/sakila-where-are-you-going/#与-percona-的-mysql-和-mariadb-比会怎样)：对比默认配置与手工调优后官方 MySQL 8.0/8.4、Percona Server 与 MariaDB 11.3 在高并发争用下的真实吞吐分野。
- [Oracle最终还是杀死了MySQL · 参考阅读](/db/oracle-kill-mysql/#参考阅读)：剖析开源版缺失并行查询以及将向量检索、JS 特性锁入专有云/企业版如何加速开发者逃离。

### MySQL 默认可重复读真能防异常吗，真实水位如何？ {#mysql-rr-jepsen-collapse}

金融账务系统绝不可轻信 MySQL 的 ACID 承诺——其 8.0 默认可重复读（RR）公然违背官方文档快照保证。Jepsen 对 8.0.34 的实测揭穿真相：RR 事务先读 `name`，仅更新同行 `gender` 后重读 `name`，9048 个事务中竟有 126 个读到外部并发改写的新值，一次本地写入等同于引狼入室篡改快照！Elle 检测器更证实它连 Kleppmann 降级判定的“单调原子视图（MAV）”都达不到，单节点竟会同读一并发事务的新值与未提交旧值，实际正确性劣于 PG 的读已提交（RC），外加超万张表重启即崩的恶性 Bug。

- [MySQL正确性竟如此垃圾？ · 隔离性问题：不可重复读](/db/bad-mysql/#隔离性问题不可重复读)：复现 Jepsen 对 MySQL 8.0.34 的测试现场，揭露 RR 事务内执行更新即破坏一致性快照导致不可重复读的内核缺陷。
- [MySQL正确性竟如此垃圾？ · 原子性问题：非单调视图](/db/bad-mysql/#原子性问题非单调视图)：基于 Elle 偏序检测证明 MySQL RR 击穿单调原子视图（MAV）底线，真实隔离水位劣于主流数据库的读已提交。
- [MySQL vs PostgreSQL @ 2025 · 正确性](/db/mysql-vs-pgsql/#正确性)：对照 MySQL 伪快照隔离、超万张表重启崩溃 Bug 与 PostgreSQL 原生可串行化快照隔离（SSI）及 815 种 ICU 排序规则的工程底蕴。

### 开串行化或降 RC 手工加锁能补救正确性吗？ {#mysql-sr-and-rc-for-update}

两条补救路全是坑。开启 MySQL Serializable 纯属鸡肋：不仅 RDS 旧默认参数 `replica_preserve_commit_order=OFF` 会在副本诱发 G2 撕裂读，且如李海翔“一致性八仙图”所示，它靠昂贵的死锁检测硬扛冲突，吞吐骤降到官方文档只敢列为权宜之计。而常见的“降到 RC 再满地写 `SELECT FOR UPDATE`”是向业务层转嫁并发控制责任，TPC-C/YCSB 实测人肉锁争用比强隔离更伤性能，且极易漏锁错账。现代算力早已过剩，PostgreSQL 的 SSI 以微弱开销兑现零异常真串行化，证明正确性绝不该被牺牲。

- [MySQL正确性竟如此垃圾？ · 串行化问题：鸡肋且糟糕](/db/bad-mysql/#串行化问题鸡肋且糟糕)：结合 RDS 副本 G2 撕裂读实测与“一致性八仙图”，拆解 MySQL Serializable 依赖死锁检测拖垮吞吐的机制硬伤。
- [MySQL正确性竟如此垃圾？ · 正确性与性能的利弊权衡](/db/bad-mysql/#正确性与性能的利弊权衡)：用 TPC-C/YCSB 锁争用数据批驳“RC + 手工 `FOR UPDATE`”怪圈，论证硬件过剩时代以 SSI 默认保障 100% 正确性的合理性。
- [MySQL安魂九霄，PostgreSQL驶向云外 · 无可救药的质量水平](/db/mysql-is-dead/#无可救药的质量水平)：总结早年牺牲正确性换性能的草莽捷径如何在性能优势丧失后沦为致命质量出血点。

### 曾稳健十余年的 Oracle，为何亲手杀死了 MySQL？ {#oracle-heatwave-killed-mysql}

代码 GPL 公开不等于真开源。据 Peter Zaitsev 与 Marco Tusa 复盘：收购 Sun 后十余年，Oracle 曾严守“商业转化绝不妨碍采用”的铁律，仅将审计防火墙放入商业版；转折点出在云巨头拿开源 MySQL 狂赚数十亿美元却零代码回馈，叠加 Oracle 强推 OCI HeatWave 专有云。拒当冤大头的 Oracle 索性大裁核心研发、退回黑盒开发，把性能优化与重磅特性全锁上云，逼得 Percona 跳过全部七个 9.x 创新版并预警其沦为“遗留技术”，一代默认库就此谢幕。

- [MySQL 9.7：还是那碗冷饭 · MySQL 为什么会变成这样？](/db/mysql-97-bye/#mysql-为什么会变成这样)：剖析单一厂商控盘引发的裁撤团队、黑盒开发与 Percona 跳过七个创新版乱象，见证 MySQL 滑向遗留技术。
- [Oracle最终还是杀死了MySQL · 参考阅读](/db/oracle-kill-mysql/#参考阅读)：阐明“转化永不妨碍采用”的开源商业化铁律，复盘 Oracle 为强推 HeatWave 锁死核心特性自毁长城的过程。
- [MySQL性能越来越差，Sakila将何去何从？ · 一些思考](/db/sakila-where-are-you-going/#一些思考)：从云大厂白嫖数十亿美元零回馈的博弈视角，解释 Oracle 私藏云端性能优化并把存量用户逼向 PG 的困局。

### 云白嫖与原厂锁死如何毁掉生态，PG 该防什么？ {#tragedy-of-commons-pg-lesson}

杀死 MySQL 的是“Oracle 独占产权 + 云厂搭便车白嫖”的公地悲剧：AWS 等云巨头拿内核卖 RDS/Aurora 躺赚高毛利却绝不回馈竞争对手，Oracle 则彻底摆烂社区版，双方合谋榨干了生态生命力。前车之鉴下，PostgreSQL 虽靠中立社区治理避开了单点绑架，但同样面临云巨头用闭源管控软件独吞运维暴利、把内核研发成本甩给社区的隐忧。生态既需留着对手防垄断懈怠，更亟需像 Pigsty 这样开箱即用的开源本地 RDS 替代品去制衡公有云霸权。

- [MySQL vs PostgreSQL @ 2025 · 究竟是谁杀死了 MySQL？](/db/mysql-vs-pgsql/#究竟是谁杀死了-mysql)：揭示私有产权与云厂白嫖合谋掏空 MySQL 的深层机理，警示 PG 生态须以开源本地发行版抵御公有云管控锁定。
- [MySQL安魂九霄，PostgreSQL驶向云外 · 究竟是谁杀死了 MySQL？](/db/mysql-is-dead/#究竟是谁杀死了-mysql)：对比单一公司资产与社区共同治理的抗风险差异，剖析云厂商闭源运维层独吞利润的结构性危机。

### 两大分支为何难挽败局，MySQL 阵营还有出路吗？ {#can-mysql-camp-catchup}

为防 PostgreSQL 独占市场而懈怠，行业本需要健康的对手，但现有分支难堪大任。如 Peter Zaitsev 拆解：架构上 MySQL 缺自定义类型与可插拔索引；治理上 Oracle 独占商标、双许可并强制签 CLA，断了友商共建之路。Percona 受制于 100% 兼容包袱不敢大改；MariaDB 虽当过鲶鱼，却已严重分叉失配、基金会无完整商标权且商业实体被私募收购。若 Oracle 拒绝效仿 OpenOffice 将社区版捐给中立基金会，阵营唯一生路只剩效仿 Valkey 联手换牌分叉重生。

- [MySQL还有机会赶上PostgreSQL吗？ · 所有权和治理](/db/can-mysql-catchup/#所有权和治理)：对比 Oracle 独占商标与双许可对供应商共建的扼杀，以及 PostgreSQL 中立治理加宽松协议汇聚的滚雪球势能。
- [MySQL还有机会赶上PostgreSQL吗？ · 架构](/db/can-mysql-catchup/#架构)：点明缺失自定义数据类型、操作符与可插拔索引框架是导致 MySQL 在向量时代创新失速的架构病根。
- [MySQL还有机会赶上PostgreSQL吗？ · 总结](/db/can-mysql-catchup/#总结)：剖析 Percona 兼容束缚与 MariaDB 分叉及私募化困局，提出效仿 Valkey 联合分叉换牌重生的唯一突围方案。
- [Oracle还能挽救MySQL吗？ · 参考阅读](/db/can-oracle-save-mysql/#参考阅读)：剖析 CLA 知识产权障碍、维持开源关系库双雄竞争防垄断的必要性，以及移交独立基金会或启动“计划 B”的抉择。

## 三、PostgreSQL 加冕与去 O 实战对比 {#pg-coronation-and-oracle}

### 治理之外，驱动 PG 吞噬数据库世界的引擎是什么？ {#stonebraker-extensibility-seed}

治理优良却无人问津的开源项目不在少数——Oracle 失误只是推开需求侧大门，中立治理也只是护城河，供给侧真正的发动机是图灵奖得主 Stonebraker 在 1986 年种下的“可扩展性”元能力。把自定义类型、操作符与 GiST/GIN 索引做成一等公民，让外部团队免改内核便长出破千款插件：从 PostGIS、JSONB 到 `pgvector` 及 `pgvectorscale`、`VectorChord` 等“扩展的扩展”，连续三轮吃尽时代红利，官方镜像周下载量拉开 MySQL 四倍，单栈即可平替多套异构库。

- [是 Oracle 的失误让 PostgreSQL 赢了吗？ · 五、但 Stonebraker 也没说错——他种下的那颗种子](/db/thank-oracle/#五但-stonebraker-也没说错他种下的那颗种子)：追溯 1986 年“将扩展做成一等公民”的元设计如何催生繁荣插件生态，并令 PG 通信协议成为无人敢不兼容的事实标准。
- [MySQL 9.7：还是那碗冷饭 · 换个方向看看 PG](/db/mysql-97-bye/#换个方向看看-pg)：盘点 PostGIS、JSONB 与向量扩展群连续卡位三代浪潮的战果，以四倍镜像下载量印证开发者的用脚投票。
- [MySQL安魂九霄，PostgreSQL驶向云外 · 日渐落后的功能特性](/db/mysql-is-dead/#日渐落后的功能特性)：援引 CMU 数据库可扩展性研究，展示破千款扩展如何将 PostgreSQL 升格为替代多套异构组件的全栈数据平台。

### PG 线缆协议如何成事实标准并零代码接管异构库？ {#pg-wire-protocol-compatibility}

Stonebraker 与 CMU 教授 Andy Pavlo 已在年度对谈中盖棺定论：“Postgres 已经赢了”。当 MySQL v9 爆出超八千张表即崩溃的荒唐缺陷时，AWS 分布式旗舰 Aurora DSQL 首发仅兼容 PG 线缆协议而彻底无视 MySQL；如 Matt Blewitt 所言，PG 已演变为数据库界的 Linux 内核，未来十年主旋律是各大 PG 发行版之争。更致命的是其跨库协议兼容矩阵：`DocumentDB`/`FerretDB` 兼容 Mongo，`Babelfish` 兼容 MSSQL，`IvorySQL` 兼容 Oracle，`openHalo` 原生兼容 MySQL 线协议，零代码即可接管存量应用。

- [2025 年度数据库世界总结：石破天 vs Andy Pavlo 对谈录 · 3. Postgres 已经赢了，押注 Postgres 是正确选择](/db/db-year-review-2025/#3-postgres-已经赢了押注-postgres-是正确选择)：收录两位泰斗关于社区共治击败企业私产、各大云巨头全面统一押注 PG 线缆协议及内部发行版主导权新战局的论断。
- [MySQL vs PostgreSQL @ 2025 · 兼容性](/db/mysql-vs-pgsql/#兼容性)：梳理覆盖 MongoDB、MSSQL、Oracle 乃至 `openHalo` 原生兼容 MySQL 线缆协议的全行业 PG 兼容生态矩阵。
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法：数据库杂闻](/db/pavlo-2024-review/#andy-的看法数据库杂闻)：对比 MySQL v9 超八千张表崩溃乱象与 AWS Aurora DSQL 独尊 PG 线缆协议、Supabase 收购 OrioleDB 的产业风向标。
- [七周七数据库（2025年） · 老冯评论](/db/7-week-7-db/#老冯评论)：对比 2013 与 2025 两代榜单更迭，确立 PostgreSQL 作为通用七层协议标准与底层“Linux 内核”的十年终局定位。

### 开发者调查何时王座易主，选型呈现什么虹吸效应？ {#so2022-turning-point-siphon}

王座交替早在 StackOverflow 2022 七万开发者调查中便已定局：近五万专业开发者里，PostgreSQL 以 46.5% 首次反超 MySQL（45.7%）夺魁，并以超 70% 喜爱率击败常年霸榜的 Redis，包揽最流行、最喜爱、最想学“三冠王”。选型流向和弦图更显露残酷的“单向虹吸”：高达 23% 的在用 MySQL 开发者（逾 1.1 万人）计划次年迁往 PG，反向回流近乎为零。叠加 DB-Engines 上 Oracle、MySQL 与 SQL Server 集体滑坡而 PG 逆势大涨 9.2%，全口径登顶只是时间问题。

- [StackOverflow 2022数据库年度调查 · 最流行的数据库](/db/so2022-db/#最流行的数据库)：记录 PostgreSQL 在专业开发者中首次反超 MySQL 并包揽流行度、喜爱度与渴望度三冠王的分水岭数据。
- [StackOverflow 2022数据库年度调查 · 现在用什么以及想用什么？](/db/so2022-db/#现在用什么以及想用什么)：拆解开发者迁移和弦图，实证 23% MySQL 用户流向 PG 而反向回流近乎归零的单向虹吸效应。
- [StackOverflow 2022数据库年度调查 · DBEngine](/db/so2022-db/#dbengine)：基于传统三强集体下跌与 PG 逆势大涨 9.2% 的斜率剪刀差，推演全球数据库总榜登顶时间表。

### 从云实例占比到中国市场，PG 逆转到了哪一步？ {#global-and-china-pg-adoption}

看硬核产业指标，云原生、AI 与合规三重浪潮已彻底改写版图：三大公有云全面首推 PG，AWS RDS 上 PG 与 MySQL 实例比已达 6:4（多出 50%）；Vercel 存储大半是 PG 衍生品，Cursor、Dify、Notion 等 AI 独角兽清一色默认选 PG；类 BSD 协议更在合规上碾压 Oracle 的 GPL。地缘上，受制裁的俄罗斯市场不受单一公司控制的 PG 采用率高达 60.5%（两倍于 MySQL）；即便在曾占 58.2% 的 MySQL 大本营中国，受国产信创推动比例也已从 1:5 追至 1:2，增量市场全面反超。

- [MySQL与白酒：互联网行业的服从测试 · 六、潮水的方向](/db/mysql-baijiu/#六潮水的方向)：从三大云首推、`pgvector` AI 卡位与类 BSD 合规优势三方面总结 PG 接管新项目默认席位的大势。
- [MySQL vs PostgreSQL @ 2025 · 厂商](/db/mysql-vs-pgsql/#厂商)：披露 AWS RDS 实例数 6:4 反超、新一代云旗舰弃 MySQL 独尊 PG 以及中国市场增量逆转的详实盘点。
- [MySQL安魂九霄，PostgreSQL驶向云外 · 枯萎收缩的生态规模](/db/mysql-is-dead/#枯萎收缩的生态规模)：对比全球、俄罗斯（60.5% 采用率）与中国信创市场的数据演变，论证技术先进性向生态份额的必然兑现。

### 对比事务正确性，Oracle 可串行化为何输给了 PG？ {#oracle-fake-serializable}

号称顶级商业数据库的 Oracle 其实虚标了最高隔离级别。如 Cybertec 专家 Laurenz Albe 实测揭露，Oracle 标称的 `SERIALIZABLE` 底层只是快照隔离（SI）：面对并发“先查计数后按规则插入”场景，它会放行典型的写偏斜（Write Skew）异常致约束失守，未指定立即段创建时甚至莫名抛虚假序列化错误。放眼主流关系型 DBMS，唯有 PostgreSQL（及其衍生系）凭可串行化快照隔离（SSI）真正实现了严格等价于串行执行的 `SERIALIZABLE` 隔离。

- [对比Oracle与PostgreSQL事务系统 · 老冯评论](/db/oracle-pg-xact/#老冯评论)：结合并发计数插入实测，拆穿 Oracle 将快照隔离虚标为 `SERIALIZABLE` 放行写偏斜的真相，确立 PG 真串行化的独一地位。

### 从 Oracle 迁往 PG，事务回滚与 MVCC 有哪些坑？ {#oracle-to-pg-migration-pitfalls}

去 O 迁移必须吃透两大机制差异。按 Laurenz Albe 总结：第一，Oracle 执行 DDL 隐式提交不可悔，普通 SQL 报错仅做语句级回滚；PostgreSQL 支持事务内安全回滚 DDL，但任一语句出错会中止整个事务——切忌在长批处理中滥用 `SAVEPOINT` 模拟容错，否则必触发子事务雪崩。第二，Oracle 靠 UNDO 表空间存旧版而怕大批量删改，PG 表内多版本存储不怕大删改却极怕长事务阻塞 `autovacuum` 致表膨胀与事务 ID 回卷；同时 `id = id + 1` 等唯一约束须声明 `DEFERRABLE`，非主键更新应改用 `FOR NO KEY UPDATE`。

- [对比Oracle与PostgreSQL事务系统 · 语句级回滚](/db/oracle-pg-xact/#语句级回滚)：对比事务性可回滚 DDL 与语句报错中止整个事务的语义差异，警示去 O 迁移滥用保存点引发的子事务灾难。
- [对比Oracle与PostgreSQL事务系统 · 事务的大小和持续时间限制](/db/oracle-pg-xact/#事务的大小和持续时间限制)：剖析 UNDO 表空间与表内多版本存储对批量修改、长事务膨胀、延迟唯一约束及 `FOR NO KEY UPDATE` 行锁选型的约束。

## 四、MongoDB 与专用向量数据库祛魅 {#nosql-and-vector-disenchantment}

### 为什么文档库是弯路，PG 如何零成本平替 MongoDB？ {#mongodb-covered-by-pg-jsonb}

诚如 Stonebraker 所断定，无模式文档库只是重蹈几十年前反范式数据冗余的覆辙，遇多对多关系便捉襟见肘，而可扩展关系模型天生向下兼容文档。MongoDB 不仅在 Jepsen 一致性评测中一塌糊涂，看家的 JSON 读写与分析也在 OnGres/EDB 实测中被单机可扛数百 TB 的 PostgreSQL `JSONB` 全面吊打。当闭源改 SSPL、孤家寡人的 MongoDB 被迫回头补课 SQL 与 ACID 时，早已没理由舍弃超融合 PG——配齐 FerretDB 等协议兼容层，不改一行代码即可零授权费平替。

- [MongoDB没有未来：好营销救不了烂芒果 · 功能被PGSQL覆盖](/db/bad-mongo/#功能被pgsql覆盖)：从关系模型向下兼容文档模型的理论高度出发，展示 `JSONB` 加 FerretDB 协议兼容层零代码平替 MongoDB 的路径。
- [MongoDB没有未来：好营销救不了烂芒果 · 正确性与性能被吊打](/db/bad-mongo/#正确性与性能被吊打)：汇总 Jepsen 一致性漏洞报告与 OnGres/EDB 基准测试，证实 PG 在 OLTP 与 OLAP JSON 负载上双双碾压 MongoDB。
- [MongoDB没有未来：好营销救不了烂芒果 · MongoDB没有未来](/db/bad-mongo/#mongodb没有未来)：论证“能打败一个生态的只有另一个生态”，剖析闭源 SSPL 单一厂商回头补齐 SQL/ACID 后无力抗衡 PG 帝国的终局。

### MongoDB 营销水分与分析器套壳 PG 的真相是什么？ {#mongodb-marketing-and-bi-hoax}

Stonebraker 曾点名痛批 MongoDB 是“靠好营销卖烂产品”的典型：公关上把“卖给估值 300 亿公司”碰瓷成“击败 PG 赢 300 亿大单”，生产中放任无模式写入更易沦为畸形脏数据垃圾箱，令成熟工程师单向逃往 PG。更讽刺的内幕被 SlamData 创始人 John De Goes 扒出：MongoDB 3.2 吹嘘的 SQL BI 连接器，竟是靠 Python Multicorn FDW（`mongoose_fdw`、`yam_fdw`）把文档粗暴展平丢字段后抽入隐藏的 PostgreSQL 跑查询！既然官方分析出路都是拍平倒进 PG，兼顾文档与分析不如直接用 PG。

- [MongoDB没有未来：好营销救不了烂芒果 · 烂产品靠营销上位](/db/bad-mongo/#烂产品靠营销上位)：揭批碰瓷客户估值的误导性公关话术，以及无模式滥用导致生产库沦为脏数据泥潭并引发工程师单向逃离的现实。
- [MongoDB：现在由PostgreSQL强力驱动？ · 掀开内幕](/db/mongo-powered-by-pg/#掀开内幕)：顺着 Tableau 驱动与 GitHub FDW 源码实锤 MongoDB 3.2 BI 连接器底层套壳隐藏 PostgreSQL 且缺乏算子下推的内幕。
- [MongoDB：现在由PostgreSQL强力驱动？ · 再见了，MongoDB！](/db/mongo-powered-by-pg/#再见了mongodb)：总结原生 JSON 与水平扩展加持下的“MongoDB 终结者”定位，点破“与其导出展平进 PG 不如直接用 PG”的选型常识。

### 为什么关系库生态繁荣，MongoDB 却沦为造假孤岛？ {#mongodb-ecosystem-island}

繁荣生态源于边界克制与共生分润。据 John De Goes 披露，MongoDB 合作伙伴团队直属首席营收官，一门心思从传统大厂榨取费用，对原生 NoSQL 工具初创公司冷漠弃之，CTO 甚至公开宣称“没有原生分析工具”。亲手造出生态荒漠后，面对企业报表、备份刚需，有限的产品团队只能硬着头皮大包大揽，明知旧版 FDW 毫无算子下推仍执意上线赝品。数据库厂商的正道是死磕 ACID、列存与跨中心复制等核心引擎硬骨头，而非靠隐瞒底层依赖透支商业诚信。

- [MongoDB：现在由PostgreSQL强力驱动？ · MongoDB：孤家寡人，孤岛一座](/db/mongo-powered-by-pg/#mongodb孤家寡人孤岛一座)：剖析以榨取传统大厂费用为导向的畸形伙伴体系如何扼杀原生周边创业生态，将自身困成一座孤岛。
- [MongoDB：现在由PostgreSQL强力驱动？ · 全力以赴](/db/mongo-powered-by-pg/#全力以赴)：还原高管无视 FDW 技术缺陷强行上线的决策内情，阐明深耕核心引擎能力与扶持伙伴生态的健康商业边界。

### 向量检索是真需求，为什么独立向量数据库迅速遇冷？ {#dedicated-vector-db-pseudo-demand}

独立向量数据库是两头受挤的伪需求：小微场景被暴涨 32 倍的大模型长上下文与平台托管吞噬，标准场景被成熟数据库迅速接管。如 Stonebraker 与 Andy Pavlo 所言，向量库只是“关系型 Blob + 内存图索引”——PG 用上百万行 C 代码解决事务与灾备，而 `pgvector` 不到两千行 C 代码就搞定向量存取，复杂度差万倍，99% 场景无需拆库。况且大模型推理动辄秒级，检索从 10ms 压到 1ms 毫无体感；Supabase 百万级 1536 维实测 `pgvector` 延迟、吞吐与成本全优胜 Pinecone，还能单库 SQL 搞定元数据混合过滤。

- [2025 年度数据库世界总结：石破天 vs Andy Pavlo 对谈录 · 4. 向量数据库是"内存图索引 + 关系型 blob"，护城河不宽](/db/db-year-review-2025/#4-向量数据库是内存图索引--关系型-blob护城河不宽)：收录两位学者对向量库内存受限、更新昂贵及作为简单索引原语被主流数据库一年全线补齐的定性判断。
- [专用向量数据库凉了吗？ · 向量数据库是一个伪需求吗？](/db/svdb-is-dead/#向量数据库是一个伪需求吗)：拆解大模型长上下文上移、通用数据库扩展下沉与超大规模大厂基于 FAISS 自研对独立向量库的三重挤压。
- [专用向量数据库凉了吗？ · 通用数据库 vs 专用数据库](/db/svdb-is-dead/#通用数据库-vs-专用数据库)：用百万行数据库内核对比两千行向量插件的万倍复杂度悬殊，揭示外部向量库带来的冗余搬运与灾备残缺代价。
- [专用向量数据库凉了吗？ · 案例PvP：pgvector vs pinecone](/db/svdb-is-dead/#案例pvppgvector-vs-pinecone)：援引百万级高维向量压测数据与端到端推理延迟账本，论证单一关系库内统一 SQL 混合检索的压倒性优势。

### GPU 数据库倒闭与二线厂商被私募收割说明了什么？ {#gpu-db-death-and-pe-harvest}

数据库市场正在冷酷出清泡沫。按 Andy Pavlo 复盘，全明星 Voltron Data 倒闭与 HeavyDB 被收编，印证了现代 CPU 列存扫描连接算力早已商品化，独立 GPU 数据库难逃死刑，OLAP 胜负手已转向优化器质量与体验；同时风投撤出向量库，MariaDB、Couchbase、SingleStore 接连被私募股权（PE）私有化榨取存量维护费。另一头，像 Tembo 这样攒出两百个 PG 扩展便突然关停云库、只给付费客户两个月搬迁去蹭 AI 热点的投机客，更反证基础设施唯靠长期契约与热爱方能存活。

- [Andy Pavlo：2025 数据库世界年度总结 · Andy 的看法](/db/db-in-2025/#andy-的看法-4)：剖析基础算力商品化对独立 GPU 数据库的致命打击，以及增长停滞的二线数据库厂商批量落入私募股权手中的终局。
- [数据库茶水间：OpenAI拟收购Supabase ？ · 搞 DB 的狂蹭 AI](/db/openai-supabase-rumor/#搞-db-的狂蹭-ai)：痛批创业公司 Tembo 突然抛弃数据库托管主业、强赶付费客户两个月内搬迁以追逐 AI 风口的失信投机行为。

## 五、DuckDB 超融合、数仓终局与开源反垄断 {#duckdb-olap-and-open-source}

### DuckLake 新范式凭什么颠覆重型云数仓与目录栈？ {#duck-paradigm-pg-s3-duckdb}

列式引擎已成同质化大路货——如 Andy Pavlo 剖析 Databricks 砸 20 亿美元抢下 Tabular 所示，数仓巨头争夺的是 S3 表格式目录统治权；然而 Fivetran 统计显示生产中位数分析查询仅扫 100MB 数据，单机引擎绰绰有余！AWS 收购 DuckLabs 正是押注“鸭子范式”：DuckLake 把元数据塞回 PostgreSQL、Parquet 落进 S3、计算交给无状态 DuckDB（及 `pg_duckdb`、`pg_mooncake` 等缝合插件），直接端掉繁琐的“Iceberg + 独立 Catalog”栈；企业更可用 Pigsty 一键拉起 PG + RustFS + DuckDB 零成本自建平替。

- [AWS 收购 DuckDB：鸭子飞进亚马逊雨林 · 鸭子范式：元数据进 PG，数据放 S3](/db/aws-get-duckdb/#鸭子范式元数据进-pg数据放-s3)：拆解 DuckLake 以 PG 管元数据加 S3 存 Parquet 取代重型湖仓目录的极简范式，给出零成本全开源自建平替方案。
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法：Databricks 与 Snowflake](/db/pavlo-2024-review/#andy-的看法databricks-与-snowflake)：复盘 20 亿美元 Tabular 收购战与 Polaris/Unity 目录开源博弈，揭示列存引擎商品化后围绕对象存储元数据的决战重心。
- [Andy Pavlo: 2024年度数据库回顾 · Andy 的看法：DuckDB 与 PostgreSQL](/db/pavlo-2024-review/#andy-的看法duckdb-与-postgresql)：援引中位数分析查询仅扫描 100MB 的真实负载数据，论证将列存向量化 DuckDB 嵌入 PG 引爆的 OLAP 超融合革命。

### 嵌入式双雄如何侧翼突围，融 MySQL 语法为何徒劳？ {#duckdb-pg-fusion-and-embedded}

在 PostgreSQL 稳坐服务端铁王座的时代，唯一能从侧翼分羹的是 SQLite 与 DuckDB 这两款零依赖进程内引擎：它们绕开传统运维交付链路，离应用最近——如 Matt Blewitt 梳理，SQLite 借 Litestream 与单用户单库掀起端侧“本地优先”复兴，DuckDB 则通吃多格式文件成为单机万能 OLAP，仅在超大规模实时摄取时让位于 ClickHouse。DuckDB 从 SQL 到 PL/pgSQL 全面主动对齐 PG，谁把二者缝合最优雅谁就赢下 OLAP；反观阿里云向 DuckDB 提交 MySQL 语法兼容被拒，证明替凋亡生态续命难逆大势。

- [DuckDB 开发者大会四连击：扩展，加密，存储过程，边缘分析 · 老冯点评](/db/duckcon-2026/#老冯点评)：阐明嵌入式双雄绕开传统交付链路的侧翼卡位逻辑，对比围绕 PG 的 DuckDB 缝合大赛与强塞 MySQL 语法兼容被拒的结局。
- [七周七数据库（2025年） · 本地优先数据库](/db/7-week-7-db/#本地优先数据库)：盘点 SQLite 本地优先架构复兴与 DuckDB 单机万能分析生态位，厘清嵌入式引擎与 ClickHouse 的负载分界线。

### 传统数仓为何沦为期货死人，巨头并购藏着什么杀招？ {#big-data-dead-and-tam-veto}

传统“大数据”已是期货死人：单机 PostgreSQL 一旦与 DuckDB 或 Iceberg 彻底打通列存分析，99.99% 的企业单库即可兼办事务与分析，直接裁撤 ETL 链路与大数据部门。这正是 2025 年巨头合围 PG 的底牌——如 Andy Pavlo 盘点，Databricks 砸 10 亿美元买 Neon，微软发 HorizonDB，Vitess 元老启动 Multigres 与 Neki；而 Snowflake 砸 2.5 亿美元现金买 CrunchyData 除补 OLTP 外，更借麾下核心元老 Tom Lane 对 PG 表访问接口（TAM）的一票否决权，精准牵制对手存储引擎缝合节奏。

- [别争了，AI时代数据库已经尘埃落定 · 大数据期货死人](/db/db-for-ai/#大数据期货死人)：论证单节点 PG 融合列存分析覆盖 99.99% 企业需求后，独立数仓与繁琐 ETL 税丧失立身之本的必然终局。
- [别争了，AI时代数据库已经尘埃落定 · PG 内核的否决权](/db/db-for-ai/#pg-内核的否决权)：透视 Snowflake 收购 CrunchyData 背后围绕核心组成员 Tom Lane 及表访问方法接口（TAM）展开的社区话语权博弈。
- [Andy Pavlo：2025 数据库世界年度总结 · PostgreSQL 持续称霸](/db/db-in-2025/#postgresql-持续称霸)：全景梳理 Databricks、Snowflake、微软与各大分片中间件团队在 2025 年全面合围增强版 PostgreSQL 的产业版图。

### 巨头争抢稀缺 PG 人才时，独立开源发行版如何破局？ {#open-source-distro-anti-monopoly}

全球真正具备深厚内核功底的独立 PostgreSQL 团队屈指可数，巨头动辄数亿美金并购本质是争抢稀缺人才当生态代理人的“抢椅子游戏”。面对公有云与寡头借闭源管控层筑起的新垄断，不拿风投、独立盈利的“一人公司”开源发行版（如 Pigsty）根本无法被收编：把裸机高可用、连接池、PITR、可观测性与数百扩展打磨成免费开箱利器，每年直接抹平上亿元高溢价云 RDS 账单，正是开源生态抗衡垄断的终极鲶鱼。

- [别争了，AI时代数据库已经尘埃落定 · 人才是最关键的因素](/db/db-for-ai/#人才是最关键的因素)：揭示巨头并购争抢稀缺核心 PG 人才的本质，阐明独立开源发行版拒被收编、以零元购自建能力掀翻云溢价的鲶鱼效应。
- [专栏：数据库老司机 · PG 生态篇](/db/guru/#pg-生态篇)：浓缩“MySQL 退潮、PostgreSQL 吞噬世界”的历史收敛脉络，汇总裸机发行版落地连接池与 PITR 兑现硬件红利的实战心法。

## 六、AI 与 Agent 时代的数据库终局 {#ai-agent-database-endgame}

### 当软件坍缩为智能体加数据库，资本为何一致加冕 PG？ {#db-invariant-in-ai-era}

前端正坍缩为对话框，传统后端一半被智能体替代、一半下沉进 BaaS，唯独数据库承载的状态是 AI 时代唯一坚挺的不变量，软件全面收敛为 `Agent + Database`。从 OpenAI、Cursor 靠主从 PG 扛起顶级负载，到 Databricks 十亿美元买 Neon、20 亿估值的 Supabase 传出获 OpenAI 洽购，资本已用真金白银加冕 PostgreSQL。但真正的商业决战不在底层内核而在上层生态整合——谁先把分支、图谱、向量与 MCP 封装成统一的记忆与技能抽象，谁就能定义 Agent 原生平台。

- [别争了，AI时代数据库已经尘埃落定 · 为什么是 PostgreSQL？](/db/db-for-ai/#为什么是-postgresql)：剖析前后端萎缩后数据库作为唯一确定性底座的价值跃升，汇总顶级 AI 独角兽实践与巨头重金并购加冕 PG 的证据链。
- [数据库茶水间：OpenAI拟收购Supabase ？ · OpenAI 收购 Supabase？](/db/openai-supabase-rumor/#openai-收购-supabase)：解读 Neon 与 Supabase 密集并购传闻背后的赛道收敛信号，点明押中 `pgvector` 与开发体验的 PG 标的如何独占资本聚光灯。
- [Agent 需要什么样的数据库？ · 六、真正的竞争在哪里](/db/agent-native-db/#六真正的竞争在哪里)：论证底层扩展内卷之上，“将无聊技术整合封装为开箱即用 Agent 原生平台”才是十亿美元级战略价值的真正归宿。

### 为什么智能体常沦为“缸中之脑”，需补齐哪三大器官？ {#agent-brain-in-a-vat-and-organs}

强推理 Agent 在工程现场常显笨重健忘，症结不在引擎慢，而在栖身于“JSON + 脚本”或“向量库 + 关系库 + 缓存”的割裂架构中，缺失统一“数字躯体”——重启失忆、并发竞态，每次行动都要跨越序列化与网络往返的漫长反射弧。突破自主天花板急需库内补齐三大器官：用 `PL/Python`、`PL/Rust` 让函数与数据共址化作零延迟“肌肉记忆”；融合向量与知识图谱构建动态语义图谱（GraphRAG 多跳准确率 87%，纯向量仅 23%）化作“联想记忆”；借 `Git for Data` 瞬时拉起分支做反事实推演化作安全试错的“想象力”。

- [Agent 需要什么样的数据库？ · 一、缸中之脑](/db/agent-native-db/#一缸中之脑)：诊断割裂存储栈引发的重启失忆、并发竞态与跨网络序列化反射弧延迟，提出一体化数据容器“数字躯体”命题。
- [Agent 需要什么样的数据库？ · 三、范式革命的三个维度](/db/agent-native-db/#三范式革命的三个维度)：定义库内计算肌肉记忆、向量图谱融合联想记忆（87% vs 23% 多跳准确率对比）与数据分支反事实推演三大演进维度。

### 智能体数据库要重写内核吗，为什么 PG 是唯一基座？ {#agent-db-boring-tech-pg}

支撑 Agent 的范式革命无需重写底层存储引擎：向量、图遍历、库内计算与分支时间旅行只是扩展索引、存储过程及 MVCC/写时复制的自然延伸，数十年验证的 ACID、B-Tree、WAL 与优化器等“无聊技术”仍是精确地基。Pinecone 只懂向量、Neo4j 只懂图，而 Agent 需同时调用关系、向量、图、全文与时序——唯有允许扩展深度介入规划器、执行器与事务系统的 PostgreSQL，能把 `pgvector`、`Apache AGE` 与 BM25 收进同一 ACID 边界，免除跨库同步泥潭。

- [Agent 需要什么样的数据库？ · 四、一个被忽视的真相](/db/agent-native-db/#四一个被忽视的真相)：厘清新型 Agent 原语与传统扩展索引、存储过程及 MVCC 的同源关系，重申成熟 ACID 与 WAL 内核不可动摇的基石地位。
- [Agent 需要什么样的数据库？ · 五、PostgreSQL 的压倒性优势](/db/agent-native-db/#五postgresql-的压倒性优势)：对比单一模态专用库的局限，阐明 PostgreSQL 在单一 ACID 事务边界内深度组合关系、向量、图与全文检索的独一统治力。

### 如何用 PGFS 给并行智能体装上时光机与共享大脑？ {#agent-state-pgfs-time-machine}

单机玩具用本地目录加 Git 或 SQLite 足矣，一旦进入多 Sub-Agent 并行、跨设备协同与持续数据保护（CDP），裸文件锁与轮询只会造出蹩脚数据库。用 JuiceFS 把文件元数据与数据块同存 PostgreSQL（PGFS），所有文件写入即共享同一套 WAL 事务：零专用硬件成本即可让文件、未入库配置与业务表精确回滚到误删前一微秒（PITR）并瞬时克隆试错分支；任意 Linux/macOS/Windows 机器凭一行连接串即可挂载百 MB/s 缓存工作区，配合 MVCC 与 `LISTEN/NOTIFY` 建成多机“共享大脑”。

- [把 Agent 的状态放进数据库 · Agent 到底需不需要数据库？](/db/agent-state-db/#agent-到底需不需要数据库)：划清单机玩具与多 Agent 并行、跨设备协同、审计容灾的分水岭，批判在文件系统上重复发明脆弱数据库锁的反模式。
- [把 Agent 的状态放进数据库 · 杀手锏一：时光机](/db/agent-state-db/#杀手锏一时光机)：详解基于 JuiceFS + PostgreSQL（PGFS）共用 WAL 实现文件与业务数据微秒级一致性时间点恢复与瞬时分支克隆的机制。
- [把 Agent 的状态放进数据库 · 杀手锏二：共享大脑](/db/agent-state-db/#杀手锏二共享大脑)：展示用 Pigsty 声明式拉起 PGFS 后凭一行连接串跨平台挂载编码 Agent 记忆目录，并结合 MVCC 与通知原语消除并发冲突。

### 创业出海为何偏爱 Supabase，增长后为何必须自建？ {#self-host-supabase-baas}

Supabase 以 PostgreSQL 为核，一站式集成认证、实时消息、边缘函数、存储与自动生成的 REST/GraphQL 接口，省去后端胶水代码，让小团队只写表结构配 Vibe Coding 前端即可全栈出海。但业务一破官方云 500MB 免费门槛，云存储溢价便急剧膨胀，而本地企业级 NVMe SSD 性价比高出三到四个数量级；且多租户云仅开放 64 个扩展，另有 `pg_graphql`、`wrappers`、`supautils` 等 10 个核心扩展未进 PGDG 源而隐性锁死容器镜像。用 Pigsty 原生包解耦自建，方能解锁 440 个扩展与多内核自由。

- [自建Supabase：创业出海的首选数据库 · Supabase是什么？](/db/supabase/#supabase是什么)：拆解以 PostgreSQL 为核心集成认证、实时流、存储与自动 API 生成的全栈架构如何赋能小微团队极速交付。
- [自建Supabase：创业出海的首选数据库 · 为什么要自建？](/db/supabase/#为什么要自建)：算清突破 500MB 后本地 NVMe 相比云存储三至四个数量级的成本账，破除 64 个扩展阉割与 10 个私有打包扩展的镜像锁定。

### 传统控制台为何卡住 AI，轻量后端如何稳健上生产？ {#insforge-mcp-baas-production}

AI 十分钟能写出前端，却常卡在配库与认证上线，因为传统 BaaS 网页控制台是为人类点鼠标设计的黑盒。InsForge 架起基于 MCP 的语义层，让 Coding Agent 直接读表结构与 RLS、调工具建表配认证查日志，打通 Vibe Coding 最后一公里；并砍掉开源 Supabase 约 15 个容器里的 Kong、Elixir、Supavisor 等重组件，用轻量 TypeScript 加 PostgREST 与 Deno 围着 PG 瘦身至 5 个容器。上生产时甩掉内置单节点容器库、接入 Pigsty 高可用 PG 底盘，即可兼得敏捷与稳健。

- [InsForge：为 Vibe Coding 而生的 Supabase · 关键差异：语义层](/db/insforge/#关键差异语义层)：对比面向人类点击的图形控制台黑盒，解析基于 MCP 协议暴露表结构、RLS 与日志工具如何让 Agent 自主闭环全栈后端。
- [InsForge：为 Vibe Coding 而生的 Supabase · 架构拆解：简化版 Supabase](/db/insforge/#架构拆解简化版-supabase)：拆解砍掉多语言重型网关中间件、以核心 PostgreSQL 配轻量 TypeScript 将十余个容器压缩至五个的极简架构。
- [InsForge：为 Vibe Coding 而生的 Supabase · 纳入 Pigsty 全家桶](/db/insforge/#纳入-pigsty-全家桶)：补齐新兴 Agent 后端内置单节点容器库缺失的高可用、备份恢复与可观测短板，实现上层敏捷接口与企业级 PG 底盘的解耦结合。
