---
title: 数据库与 PostgreSQL
linkTitle: 数据库板块
description: 合并数据库老司机（109 篇）与 PostgreSQL 大法师（170 篇）共 279 篇文章，拆分为 25 个专题、307 条一句话核心观点与原文锚点导航。
weight: 20
icon: fa-solid fa-database
no_list: true
---

汇集 [数据库老司机](/db/)（109 篇）与 [PostgreSQL 大法师](/pg/)（170 篇）两大专栏十年沉淀的全部 **279 篇已发布中文文章**，贯通宏观选型与路线之争、国产数据库审计、极简主义与 DuckDB/向量融合、500+ 扩展与 Pigsty 发行版哲学、Silo 开源续命、高可用备份克隆、MVCC 内核机理以及高阶 SQL 工程规约，拆细为 **25 个专题页面、307 条核心观点**。点击任意问题即可直达对应细分专题页的具体观点与原文锚点：

## 一、选型金字塔与 PostgreSQL 吞噬世界 {#pg-ate-world}

> 专题全文：[《选型金字塔与 PostgreSQL 吞噬世界》（16 问）→](/opinion/db/pg-ate-world/)

- [为什么学透数据库原理比死磕算法更能决定上限？](/opinion/db/pg-ate-world/#why-learn-db-principles) —— 数据表即数据结构、索引查询即算法，实战踩坑后反刍内核才是架构师正道。
- [生产数据库的准入底线与高阶比拼维度是什么？](/opinion/db/pg-ate-world/#db-demand-pyramid) —— ACID 与冷备 PITR 是生死底线，性能成本管理比（ROI）与可观测自治拉开上限。
- [为什么有硬伤的默认选型能横行，如何打破惯性？](/opinion/db/pg-ate-world/#mysql-baijiu-obedience-test) —— 默认选型常沦为避责的服从测试，好数据库应服务于人而非逼人给烂设计打补丁。
- [该走专业化还是一体化，主从架构上限有多高？](/opinion/db/pg-ate-world/#monolith-pg-vs-sharding) —— 几十 TB 内首选一体化 PG，未分片一主四十从即可扛下五亿月活与百万 QPS。
- [PG 凭什么从学院原型长成数据库界的 Linux？](/opinion/db/pg-ate-world/#from-berkeley-to-linux) —— 全球社区共治叠加企业级基石与可扩展架构，使新数据范式得以在库内原生生长。
- [全球开发者调研如何印证 PG 的断层统治力？](/opinion/db/pg-ate-world/#survey-and-ranking-dominance) —— 58.2% 使用率包揽三冠王，44% 净喜爱指数与 47% 需求度提前锁定增量江山。
- [为何说可扩展性才是 PG 跨越三波浪潮的撒手锏？](/opinion/db/pg-ate-world/#extensibility-three-waves) —— 凭 PostGIS、JSONB 与 `pgvector` 完成三十年三级跳，八年五夺年度数据库总冠军。
- [为什么“一切皆用 Postgres”能根治组件泛滥？](/opinion/db/pg-ate-world/#just-use-postgres) —— 单库平替缓存、队列与文档库砍掉跨库胶水代码，百台 PG 零缓存即可扛 250 万 TPS。
- [硬件跃迁与 DuckDB 合流如何颠覆数仓与新内核创业？](/opinion/db/pg-ate-world/#hardware-duckdb-convergence) —— 百核大内存加 `pg_duckdb` 推动超融合，无数量级优势的新内核终将被 PG 扩展吞并。
- [列存扩展与冷热分层如何打破 PG 的百 TB 瓶颈？](/opinion/db/pg-ate-world/#in-db-olap-and-tiered-storage) —— 库内向量化引擎杀入 ClickBench 前十，配合 S3 冷热分层即可单栈承载 PB 级负载。
- [为什么软件架构正向数据库坍缩，库内写逻辑可行吗？](/opinion/db/pg-ate-world/#db-is-the-arch) —— 算力富余加 LLM 扫清存储过程门槛，应用架构正加速向 `Agent + Database` 坍缩。
- [在 Agent 时代，多元持久化为何成了诱发幻觉的毒药？](/opinion/db/pg-ate-world/#ai-agent-zero-glue) —— 异构多库挤占上下文并放大幻觉，单条 ACID SQL 与 `psql` 才是零胶水执行底座。
- [为什么自然语言写 SQL 频失灵，Agent 最缺什么？](/opinion/db/pg-ate-world/#text-to-sql-and-agent-acid) —— 真实数仓私有黑话令裸调模型跌至两三成准确率，长链路读写 Agent 亟需 ACID 兜底。
- [如何靠 PG 扩展纯 SQL 检索 PDF 并开箱交付？](/opinion/db/pg-ate-world/#pg-extensions-pdf-and-pig) —— 纯 SQL 串联远程拉取与 PDF 全文向量检索，借 Pigsty 预编译 400 余款扩展开箱即用。
- [如何一条 SQL 亚秒算完百万行扑克 24 点？](/opinion/db/pg-ate-world/#sql-poker-24-and-extension) —— 质数乘积无序编码配合字典表连接 0.58 秒扫完百万行，禁用扩展测 PG 纯属自缚手脚。
- [既然多进程怕高并发，为什么 PG 不内置连接池？](/opinion/db/pg-ate-world/#why-no-builtin-pool) —— 内核坚守“发动机”简洁边界，由开源发行版预装同步连接池实现无感“整车交付”。

## 二、MySQL 谢幕、跑分真相与黑稿祛魅 {#mysql-twilight}

> 专题全文：[《MySQL 谢幕、跑分真相与黑稿祛魅》（14 问）→](/opinion/db/mysql-twilight/)

- [MySQL 9.x 的向量与新优化器究竟有多少干货？](/opinion/db/mysql-twilight/#mysql-9x-cold-leftovers) —— 开源向量连跨八版仍是换皮 `BLOB`，距离函数锁死专有云且新优化器默认关闭。
- [简单读写 MySQL 更快吗，为何海量用户死守 5.7？](/opinion/db/mysql-twilight/#mysql-8x-perf-regression) —— 8.x 吞吐较 5.7 倒退两至四成，同期 PG 17 写入反涨并实现重度写数倍碾压。
- [调参与换分支能救 MySQL 8.x 吗，缺并行后果如何？](/opinion/db/mysql-twilight/#mysql-tuning-and-parallelism) —— 调参仅勉强逼近旧版，百核时代开源版仍卡死单核无并行查询以推销专有云。
- [MySQL 默认可重复读真能防异常吗，真实水位如何？](/opinion/db/mysql-twilight/#mysql-rr-jepsen-collapse) —— Jepsen 实锤事务内更新即破坏快照并击穿单调原子视图，正确性劣于读已提交。
- [开串行化或降 RC 手工加锁能补救正确性吗？](/opinion/db/mysql-twilight/#mysql-sr-and-rc-for-update) —— 死锁检测拖垮串行化吞吐，业务层手工加锁更伤性能且易漏锁，远逊 PG 真 SSI。
- [究竟是谁杀死了 MySQL，PG 生态又该如何鉴戒？](/opinion/db/mysql-twilight/#who-killed-mysql) —— 云巨头白嫖叠加 Oracle 裁员锁死 HeatWave 酿成公地悲剧，PG 需靠开源发行版防锁定。
- [两大分支为何难挽败局，MySQL 阵营还有出路吗？](/opinion/db/mysql-twilight/#can-mysql-camp-catchup) —— 缺可扩展架构且受商标与兼容包袱束缚，唯一生路是捐献基金会或效仿 Valkey 分叉。
- [关系型“三国演义”中，治理与基因如何决定胜负？](/opinion/db/mysql-twilight/#governance-and-trilogy) —— Oracle 有才无德、MySQL 才浅德薄，唯有独立社区加宽松协议的 PG 德才兼备。
- [为什么说 PG 已赢下增量世界，而 MySQL 沦为遗产？](/opinion/db/mysql-twilight/#pg-vs-mysql-verdict) —— 2010 年后新贵默认选 PG，六年份额呈 `-0.96` 强负相关单向置换，MySQL 终将 PHP 化。
- [中外数据库演进为何差十年，人群结构如何迁移？](/opinion/db/mysql-twilight/#ten-year-lag-and-demographics) —— 国内演进滞后全球约十年，新手拿 MySQL 入门而九成四专业开发者单向升迁至 PG。
- [搜索指数与“中国加权”为何推翻不了 PG 第一？](/opinion/db/mysql-twilight/#rebut-dbengines-and-china-weight) —— 热搜词指数受多拼写稀释，即便按 8% 中国权重校正全球流行度与云营收仍是 PG 占优。
- [用 PG 的开发者真能比用 MySQL 多赚四成吗？](/opinion/db/mysql-twilight/#pg-developer-salary-premium) —— 全球 31 国薪资中位数 PG 全线领先，中国因低渗透人才稀缺溢价更高达 1.37 倍。
- [单机 PG 性能极限有多强，对决 MySQL 谁更快？](/opinion/db/mysql-twilight/#single-node-pg-extreme-perf) —— 96 核单机 PG 极限达 200 万点查，对等卸除落盘约束更以 233 万 QPS 反超 MySQL。
- [“慢 360 倍”黑稿与刷榜 TPC-C 耍了什么把戏？](/opinion/db/mysql-twilight/#debunk-360x-and-tpcc) —— 黑稿靠恶意挂起长空闲事务制造死元组膨胀，数亿堆机器刷老旧 TPC-C 纯属营销放卫星。

## 三、去 O 实战、商业库平替与协议拟态 {#oracle-commercial-exit}

> 专题全文：[《去 O 实战、商业库平替与协议拟态》（10 问）→](/opinion/db/oracle-commercial-exit/)

- [治理之外，驱动 PG 吞噬世界的底层引擎是什么？](/opinion/db/oracle-commercial-exit/#stonebraker-extensibility-seed) —— 将类型与索引做成一等公民的可扩展基因，催生逾千款插件连续吃尽三代浪潮红利。
- [PG 如何成为协议标准并零代码合围四大主流库？](/opinion/db/oracle-commercial-exit/#pg-wire-protocol-compatibility) —— 向上成为云旗舰默认线缆协议，向下借四大兼容扩展零代码接管前五数据库负载。
- [开发者调查何时王座易主，选型呈现什么虹吸效应？](/opinion/db/oracle-commercial-exit/#so2022-turning-point-siphon) —— 2022 年首夺专业开发者三冠王，高达 23% 在用 MySQL 开发者单向迁入且零回流。
- [从云实例占比到中国市场，PG 逆转到了哪一步？](/opinion/db/oracle-commercial-exit/#global-and-china-pg-adoption) —— AWS 实例比达 6:4、俄罗斯超六成采用，中国市场亦借信创从 1:5 追至增量反超。
- [对比事务正确性，Oracle 可串行化为何输给了 PG？](/opinion/db/oracle-commercial-exit/#oracle-fake-serializable) —— Oracle 底层仅用快照隔离虚标最高级别并放行写偏斜，唯有 PG 实现真串行化 SSI。
- [从 Oracle 迁往 PG，事务回滚与 MVCC 有哪些坑？](/opinion/db/oracle-commercial-exit/#oracle-to-pg-migration-pitfalls) —— 严禁滥用保存点引发子事务雪崩，防长事务阻塞回收造成表膨胀并善用延迟唯一约束。
- [去 O 遇上闭源遗留包，为何绕不开 IvorySQL？](/opinion/db/oracle-commercial-exit/#oracle-sysdate-and-ivorysql) —— 扩展改不动解析器以兼容裸 `SYSDATE`，IvorySQL 避开协议雷区实现双端口语法平替。
- [为什么盲目引入分布式 NewSQL 是过早优化？](/opinion/db/oracle-commercial-exit/#newsql-premature-optimization) —— 分布式单核吞吐落后数倍至数量级，单机 PG 15TB 与 40 万 TPS 已够 99% 企业受用终生。
- [为什么算力过剩与大模型推动 Web 逻辑回流数据库？](/opinion/db/oracle-commercial-exit/#omnigres-backend-in-db) —— 单机算力富余叠加 LLM 扫清存储过程高门槛，库内直跑 Web 全栈重获极简工程优势。
- [数据库产品为何必须从盯着 DBA 转向赋能开发者？](/opinion/db/oracle-commercial-exit/#shift-from-dba-to-developer) —— 运维底线只守存量，用丰富扩展与自托管 BaaS 帮开发者一行 SQL 顶千行代码才赢增量。

## 四、硅谷十亿并购潮、协议定力与云收编博弈 {#mna-license-cloud}

> 专题全文：[《硅谷十亿并购潮、协议定力与云收编博弈》（15 问）→](/opinion/db/mna-license-cloud/)

- [全球风投与云巨头财报为何把筹码全押在 PG 上？](/opinion/db/mna-license-cloud/#capital-all-in-on-pg) —— 硅谷新创密集拿下十亿美元级估值与并购，Azure PG 覆盖近六成世界 500 强定调终局。
- [三大分析巨头为何斥重金吞噬独立 PG 初创公司？](/opinion/db/mna-license-cloud/#why-olap-giants-buy-pg-startups) —— 争抢多 Agent 状态事实源入口并遏制库内 HTAP 威胁，纯正开源希望回落 `pg_duckdb`。
- [ClickHouse 如何不动内核完成对 PG 的双向合围？](/opinion/db/mna-license-cloud/#clickhouse-pg-symbiosis) —— 借 PeerDB 卡住 CDC 入口、扩展直查咬合，并左右布局长寿生产库与短命 Agent 库。
- [巨头“买人不买项目、开放底层”打着什么阳谋算盘？](/opinion/db/mna-license-cloud/#cloud-oligarchs-buying-maintainers) —— 资助开放底层以锁定上层 Catalog 收费站，全员收编维护者悄然瓦解多雇主制衡。
- [内核归属社区买不走，下半场“发行版战争”争什么？](/opinion/db/mna-license-cloud/#linux-kernel-distro-war) —— 竞争转向人才、发行版体验与账单控制面，自我造血的开源发行版照样稳坐牌桌。
- [为何 PG 永远卖不掉，也绝不会修改宽松开源协议？](/opinion/db/mna-license-cloud/#will-pg-change-license) —— 无 CLA 分散版权断绝出售与改证可能，中立多方共治永久锁死类 BSD 宽松定力。
- [改协议防云白嫖，为何 Redis 遭反噬而 AGPL 成均衡？](/opinion/db/mna-license-cloud/#redis-es-license-equilibrium) —— Redis 强改协议引爆 Valkey 分叉反扑，Elastic 受夹击退回 AGPLv3 印证商业均衡点。
- [传染性协议真能防云吗，为何有人主张告别 GPL？](/opinion/db/mna-license-cloud/#kleppmann-critique-of-copyleft) —— 云厂轻易绕开传染性协议且代码倾倒割裂生态，强制数据互操作与采购倾斜更有效。
- [为何从 AGPL 切回 Apache，不防白嫖怎么站着挣钱？](/opinion/db/mna-license-cloud/#agpl-to-apache-stand-tall) —— 90 分软件用 Apache 2.0 免费赠送换极端场景锤炼，靠质保与 100 分实战兜底站着挣钱。
- [公有云专有 PG 与托管 RDS 藏着多大的溢价陷阱？](/opinion/db/mna-license-cloud/#cloud-rds-markup-and-lockin) —— 同配 RDS 较裸金属溢价近 20 倍，专有存储与 I/O 计费刺客更蚕食主权与工程能力。
- [“云吞噬开源”断了什么活水，为何本地优先重于源码？](/opinion/db/mna-license-cloud/#cloud-eats-oss-and-local-first) —— 云托管暴利消灭甲方开源岗掐断回馈，防云端封号断供的本地运行权比源码更关生死。
- [编译围墙易破且上游难改证，如何防被云寡头圈养？](/opinion/db/mna-license-cloud/#exit-right-free-distro-defense) —— 社区打包即可捅破编译围墙，唯有下游对标 Debian 的自由发行版能捍卫自建退出权。
- [反击云垄断靠什么武器，云与开源终局走向何方？](/opinion/db/mna-license-cloud/#rebel-alliance-and-power-grid) —— 全栈开源联盟平替闭源管控层，推动底层 IaaS 微利电网化并剥离上层软件暴利溢价。
- [PGDG 镜像断流暴露了什么软件供应链命门？](/opinion/db/mna-license-cloud/#pgdg-mirror-supply-chain) —— 二进制仓库无免费兜底义务且套壳库遇事全隐身，独立打包与交付信任才是供应链命门。
- [龙芯跑通内核四年后，为何进官方仓库才算真能用？](/opinion/db/mna-license-cloud/#loong64-official-apt-repo) —— 接入官方持续构建与签名流水线免去编译运维黑洞，让国产架构从“能跑”跃升至“能维护”。

## 五、全球顶会破冰、30 本译著与中文社区复兴 {#community-cn-revival}

> 专题全文：[《全球顶会破冰、30 本译著与中文社区复兴》（9 问）→](/opinion/db/community-cn-revival/)

- [国内有三百款套壳库，为何社区贡献曾被评“负分”？](/opinion/db/community-cn-revival/#china-shell-forks-negative-score) —— 核心贡献挂零而上百款换皮库零回馈搞负优化，闭门白嫖终致国际社区失语。
- [本土数据库如何走出“套壳内卷、仅四家盈利”困局？](/opinion/db/community-cn-revival/#escape-shell-involution) —— 撕掉伪自研贴纸坦诚拥抱开源 PG，凭全球通用硬通货换取上游信任与话语权。
- [无大厂光环的独立开发者，如何三年站上全球顶会？](/opinion/db/community-cn-revival/#three-year-climb-to-pgconfdev) —— 从场边旁听到 5 分钟闪电控场，终凭百万月下载扩展基建登顶温哥华正式讲台。
- [国际核心社区如何拓宽荣誉体系，本土分享切中了啥？](/opinion/db/community-cn-revival/#community-mentorship-and-missing-link) —— 导师制叠加扩展贡献者徽章破壁，中国双议题分别打通扩展交付与治理反馈断桥。
- [中文社区为何一度空心化，真正的复兴该以谁为根？](/opinion/db/community-cn-revival/#revive-cn-community-user-root) —— 摒弃厂商广告展销会，以泛中文用户组为根并靠单兵 Agent 舰队重筑公共基建。
- [AI 随手可译的时代，为何要把六万条内核报错汉化？](/opinion/db/community-cn-revival/#why-native-nls-localization) —— 扫除国产衍生库沿用二十五年的错译防污染语料，七天将 6.7 万条简繁消息合入上游。
- [AI 流水线如何终结文档断档，补齐存量与全史 508 版？](/opinion/db/community-cn-revival/#ai-pipeline-full-version-docs) —— 国标术语对齐加专家纠偏一日交付三大件，并向横跨 31 大版 508 小版全史手册总攻。
- [无广告同构门户如何打破“二手博客喂坏模型”循环？](/opinion/db/community-cn-revival/#clean-cn-portal-ecosystem) —— 靠 `pgsql.cc`、`pg.center` 与 `pgext.cloud` 三座无广告一手门户重塑高质量中文底座。
- [一天精译 30 本专著并榨干问题工具靠什么章法？](/opinion/db/community-cn-revival/#translate-30-books-and-isolation) —— 多语种术语库加三审三校直译俄法名作，隔离问题工具专喂公开手册零泄密榨干余值。

## 六、国产数据库大炼钢铁与套壳考古审计 {#domestic-audit}

> 专题全文：[《国产数据库大炼钢铁与套壳考古审计》（10 问）→](/opinion/db/domestic-audit/)

- [“自研”与“纯血”为何一步步沦为了反义词？](/opinion/db/domestic-audit/#death-of-pure-blood) —— 三四百款换皮库抹平开源血缘贴“纯血”骗补，被国际学界戳穿并透支了全行业自主信用。
- [“焊死证伪通道”为何比虚荣吹牛更阴毒百倍？](/opinion/db/domestic-audit/#welded-falsification-and-paraquat) —— 用立场审讯捂嘴替代技术答疑如同喷洒百草枯，彻底废掉了行业自愈的工程纠偏回路。
- [口号竞标与信用超发留下了什么工程总账单？](/opinion/db/domestic-audit/#engineering-corruption-bill) —— 口号评标催生百个驻场分支与假开源恶债，但情怀修不好故障，开发者早已用脚投票。
- [为何持牌国产库深陷“机场出租车”死循环？](/opinion/db/domestic-audit/#airport-taxi-loop) —— 百余厂商靠测评牌照在采购温室圈地宰客，除达梦外普遍亏损，深陷政策温室死循环。
- [剥离水军软文，国产库在全球真实体量有多大？](/opinion/db/domestic-audit/#global-footprint-and-llm-audit) —— 46 款上榜国产库全球热度总和仅占千分之五，漫天中文软文甚至带偏了主流大模型。
- [所谓颠覆式自研内核，为何多是“考古学创新”？](/opinion/db/domestic-audit/#archaeological-innovation) —— 基于十年前 PG 9.2 底座堆砌 PPT 特性，甚至把普通条件索引包装成院士级黑科技。
- [同样给开源套壳，为何许多国产库做成负价值？](/opinion/db/domestic-audit/#negative-value-shell) —— 零回馈上游却改废标准接口、排斥插件并阉割开源功能，纯属拆精装房卖高价毛坯。
- [拿单边客户充数，暴露了国产 HTAP 什么窘境？](/opinion/db/domestic-audit/#htap-no-applause) —— NewSQL 全球热度微不足道，官网三大 HTAP 标杆全靠纯分析或未开 OLAP 的单边客户充数。
- [为何基础软件急需“懂车帝封闭高速式”实测？](/opinion/db/domestic-audit/#dongchedi-for-db) —— 唯有中立硬核机构搭建极限测试场戳破换皮泡沫，才能避免拿全国性生产事故买单。
- [红帽系替代选谁，为何慎碰魔改的欧拉系统？](/opinion/db/domestic-audit/#el-distro-and-openeuler) —— 生产首选 Rocky、信创首选龙蜥；OpenEuler 破坏底层依赖与 LLVM，迫使数据库全套重编。

## 七、信创定价、国测应对与九级开源主权 {#domestic-sovereignty}

> 专题全文：[《信创定价、国测应对与九级开源主权》（12 问）→](/opinion/db/domestic-sovereignty/)

- [为何国产数据库硬仗本质是“含 P 量”内战？](/opinion/db/domestic-sovereignty/#pg-purity-civil-war) —— PG 正吞噬数据库世界，国产库战力全取决于版本新、魔改少、兼容社区生态的“含 P 量”。
- [告别盲目分布式，本土库真正的硬核增量在哪？](/opinion/db/domestic-sovereignty/#centralized-and-modern-hw) —— 放弃硬分叉与伪分布式，100% 兼容上游 PG 并深耕扩展发行版与新硬件加速才是真增量。
- [数据库公允价是多少，云账单过多少必须下云？](/opinion/db/domestic-sovereignty/#fair-pricing-and-cloud-exit) —— 全球公允价每核每年一两万元买专家兜底；云账单过百万该算账，过千万必须下云自建。
- [央行招标百元每节点，真是国产库市场常态吗？](/opinion/db/domestic-sovereignty/#twenty-dollar-polardb) —— 大客下云重创高毛利云利润池，倒逼云巨头以 130 元倒贴价搅局抢夺顶级金融信创标杆。
- [国测榜单有何悖论，为何原生 PG 没能迅速清场？](/opinion/db/domestic-sovereignty/#national-test-paradox) —— 国测榜近半为 PG 子孙却排斥原版 PG，一线多靠稻草人应付，静待开源裸机 RDS 降本掀桌。
- [必选国测产品时，如何花小钱兼得面子与里子？](/opinion/db/domestic-sovereignty/#decouple-ms-and-db) —— 将管控与内核解耦，选裸机开源高含 P 量国测内核配通用管控，兼顾过审与退回 PG 自由。
- [开源库真会被卡脖子吗，谁在盼着把大门关死？](/opinion/db/domestic-sovereignty/#chokehold-myth) —— 宽松开源无法被封锁；套壳商贩卖焦虑排斥原生开源，只为垄断“翻墙权”高价寻租。
- [真需要“内核自研”还是断供不停的“运维可控”？](/opinion/db/domestic-sovereignty/#ops-sovereignty) —— 俄断供实战证明紧跟开源主干的运维可控才是真主权，闭门硬分叉终将丧失补丁自愈力。
- [按九级金字塔算，带授权锁的伪自研为何是倒退？](/opinion/db/domestic-sovereignty/#nine-level-pyramid) —— 开源天然处于 L4，捆绑到期停机 License 锁的伪自研库实则倒退回 L2 受限二进制。
- [瑞士强制政务软件开源，给数字主权打了什么样？](/opinion/db/domestic-sovereignty/#swiss-embag-and-oss-way) —— 瑞士以刚性立法强制公共代码开源破除利益锁定，拥抱开源共产主义远胜死磕兼容组装。
- [“国产”标签被劣币污染下，哪些本土力量真能打？](/opinion/db/domestic-sovereignty/#real-competitive-players) —— PolarDB、TiDB 与 Pigsty 等在海外赢得口碑，证明真精品诞生于全球搏杀而非政策温室。
- [合规脱钩锁死跨国采购后，本土开源库如何出海？](/opinion/db/domestic-sovereignty/#geopolitics-and-oss-dumping) —— 深耕亚洲商业服务基本盘，同时在欧美用纯免费开源零元倾销直接掀翻高价云 RDS 饭桌。

## 八、分布式伪需求、微服务反思与硬件红利 {#minimalism-hardware}

> 专题全文：[《分布式伪需求、微服务反思与硬件红利》（13 问）→](/opinion/db/minimalism-hardware/)

- [为何分布式 OLTP 对九成九企业都是伪需求？](/opinion/db/minimalism-hardware/#distributed-oltp-myth) —— 分布式事务折损七成性能且排障极重，十万元单机 PG 即可扛百万 QPS 与 32TB 大表。
- [亚马逊都在退回单体，微服务泡沫为何集中破灭？](/opinion/db/minimalism-hardware/#microservices-bad-idea) —— 单一团队滥用网络调用违背加尔定律，Prime Video 退回单体立省九成成本戳破了拆分泡沫。
- [基础软件忙于标书打勾，会酿成什么隐形危机？](/opinion/db/minimalism-hardware/#immune-system-silent-exit) —— 招投标导向逼走充当免疫系统的挑剔开发者并倒向开源自建，导致产品判断力空心化。
- [为何“先优化碳基程序员，再优化硅基核”才划算？](/opinion/db/minimalism-hardware/#bio-core-over-cpu-core) —— 一颗程序员碳基核抵三千余颗硅基核，高溢价已从低毛利内核转向解放人脑的管控层。
- [AI 越能秒出方案，为何越要重读 DDIA？](/opinion/db/minimalism-hardware/#why-read-ddia-in-ai-era) —— 大模型极易顺滑产出过度设计，唯有吃透底层权衡框架才能守住人类架构验收权。
- [从手翻三月到半天译完，人机协作铁律是什么？](/opinion/db/minimalism-hardware/#ddia-translation-workflow) —— 人类锁死三千词术语表与语感基线，按小节压缩窗口驱动多路 Agent 并行实现百倍提速。
- [如何用最小闭环与懒加载对抗基础软件臃肿耦合？](/opinion/db/minimalism-hardware/#minimal-loop-and-lazy-load) —— 推倒紧耦合初版从最小可验收闭环演进，配合编译期按需挂载与懒加载消除冗余。
- [对象存储能取代本地盘吗，真实适用边界在哪？](/opinion/db/minimalism-hardware/#object-storage-vs-local-nvme) —— S3 适合分析与日志底座，但毫秒级延迟、流量账单与私有化现实锁死了 OLTP 边界。
- [新硬件红利巨大，为何公有云上难产新一代库？](/opinion/db/minimalism-hardware/#modern-hardware-cloud-deadlock) —— 云巨头私藏 1 微秒级 RDMA 与新型存储指令对外只卖阉割实例，制造了新库难产死循环。
- [云订阅够便宜了，为何还要买 512G 本地主机？](/opinion/db/minimalism-hardware/#mac-studio-data-sovereignty) —— 买 512GB 统一内存静音主机不为省钱，只为本地跑百 GB 大模型与数仓以守住数据主权。
- [Agent 狂吃硬盘，如何做本地万兆分层存储？](/opinion/db/minimalism-hardware/#pc-nas-synology-tiering) —— 群晖稳保权威主数据，刷 Pigsty 的全闪 PC NAS 承接测试库与向量应用，万兆解放本机。
- [为何 AI 终结装机仙人，搭机柜成了下云必修课？](/opinion/db/minimalism-hardware/#homelab-decloud-prerequisite) —— AI 抹平了硬件装机门槛，家用四节点万兆机柜配 Pigsty 正是一人自托管下云的实战沙盘。
- [折腾遍桌面 Linux，工程师该如何选系统？](/opinion/db/minimalism-hardware/#macos-desktop-debian-server) —— 桌面锁死 macOS 保工具链与肌肉记忆，生产服务器返璞归真收敛回 Debian 与 Ubuntu。

## 九、湖仓 Catalog 税、数仓终局与“本体论”祛魅 {#lakehouse-ontology}

> 专题全文：[《湖仓 Catalog 税、数仓终局与“本体论”祛魅》（10 问）→](/opinion/db/lakehouse-ontology/)

- [独立目录为何沦为收租层，且自带权限裂缝？](/opinion/db/lakehouse-ontology/#catalog-rent-and-security-gap) —— 独立目录本质是按次收租的 PG 表，签发凭证直读文件更导致即时撤权与行列安全失效。
- [元数据放回关系库，为何单机四级阶梯就够用？](/opinion/db/lakehouse-ontology/#metadata-in-db-and-pg-duckdb) —— 元数据回归 SQL 表可实现百倍内联提速与跨表事务，单机四级阶梯足以替代重型集群。
- [开放数据栈收敛向哪三项，PG 与列存边界在哪？](/opinion/db/lakehouse-ontology/#open-data-standards-and-f3) —— 现代栈收敛向 PG、OTel 与 Iceberg，而列存格式需靠内嵌 WASM 解码器打破解析割裂。
- [Palantir 吹嘘的“本体论”到底是什么？](/opinion/db/lakehouse-ontology/#what-is-palantir-ontology) —— 本质就是表、列、外键与存储过程的数据建模，借专有格式把开放概念异化为锁客高墙。
- [只是数据建模，它凭什么撑起四千亿美元市值？](/opinion/db/lakehouse-ontology/#palantir-fde-and-radar) —— 靠情报界政商准入拿单，并将驻场 ETL 外包人力计入研发费用粉饰出百倍 SaaS 估值。
- [谁在买天价本体论，国内跟风为何必蹈中台覆辙？](/opinion/db/lakehouse-ontology/#ontology-cargo-cult) —— 买家图公款免责而被黑盒锁定；国内无国防红利盲目跟风，必重演数据中台覆灭宿命。
- [鸭子范式凭什么颠覆重型云数仓与湖仓目录栈？](/opinion/db/lakehouse-ontology/#duck-paradigm-pg-s3-duckdb) —— 生产查询中位数仅 100MB，PG 管元数据加 S3 与 DuckDB 直接端掉天价湖仓目录栈。
- [嵌入式双雄如何突围，兼容 MySQL 为何徒劳？](/opinion/db/lakehouse-ontology/#duckdb-pg-fusion-and-embedded) —— SQLite 与 DuckDB 绕开运维占领端侧与单机分析，全面对齐 PG 而拒接退潮的 MySQL 语法。
- [传统数仓为何沦为期货死人，巨头并购藏何杀招？](/opinion/db/lakehouse-ontology/#big-data-dead-and-tam-veto) —— 单机 PG 融合列存覆盖九成九需求宣判数仓死刑，巨头斥资十亿并购争抢内核话语权。
- [巨头疯抢稀缺内核人才，独立开源发行版如何破局？](/opinion/db/lakehouse-ontology/#open-source-distro-anti-monopoly) —— 不拿风投的一人公司无法被巨头收编，以开箱即用的免费裸机发行版掀翻云 RDS 垄断。

## 十、小数据复兴、DuckDB 合体与时序流计算 {#duckdb-olap-stream}

> 专题全文：[《小数据复兴、DuckDB 合体与时序流计算》（8 问）→](/opinion/db/duckdb-olap-stream/)

- [为什么说行业在分布式大数据上白白错付了十年？](/opinion/db/duckdb-olap-stream/#small-data-lost-decade) —— 生产查询中位数仅 100MB，笔记本靠 DuckDB 外存溢出即可跑完 60 亿行 TPC-H。
- [为何分布式 HTAP 成了无人鼓掌的演出？](/opinion/db/duckdb-olap-stream/#htap-knork-illusion) —— 部门墙与行列存物理互斥令分布式 HTAP 沦为刀叉捆绑，标杆案例仍靠外挂同步跑单边。
- [国产分布式库热炒 HTAP 暴露了什么自救焦虑？](/opinion/db/duckdb-olap-stream/#htap-efficiency-inversion) —— 92 核集群跑 50 仓仅抵笔记本跑 300 仓，算力严重倒挂暴露了分布式失宠后的自救焦虑。
- [为何 PG 融合列存引擎能补短板并终结双轨制？](/opinion/db/duckdb-olap-stream/#pg-kiss-duckdb) —— PG 企业治理骨架配 DuckDB 顶级列存算力，免 ETL 保 ACID 直接终结库仓双轨制。
- [微内核与块级加密如何让嵌入式列存既轻又全能？](/opinion/db/duckdb-olap-stream/#duckcon-kernel-and-edge) —— 靠按需扩展、256KB 先压后密、流式栈存储过程与边缘定向广播兼得零依赖与高性能。
- [时序超表为何坚持宽表，且十亿行写入快二十倍？](/opinion/db/duckdb-olap-stream/#timescaledb-wide-table-and-hypertable) —— 宽表消除标签叉积膨胀，自动分块锁住热索引常驻内存使十亿行写入提速二十倍。
- [时序超表适用边界在哪，查询为何易爆共享内存锁？](/opinion/db/duckdb-olap-stream/#timescaledb-boundaries-and-locks) —— 稀疏 KV 与冷批处理不宜强上；跨分块查询易耗尽默认 64 锁槽位，须按分块数两倍预调。
- [如何免搭重型流引擎，在关系库内跑实时流式聚合？](/opinion/db/duckdb-olap-stream/#pipelinedb-continuous-views) —— 用 PipelineDB 外表接流配合连续视图内存增量物化免落明细，记得调大后台工作进程池。

## 十一、向量数据库祛魅、BM25 检索与 Agent 状态库 {#ai-vector-endgame}

> 专题全文：[《向量数据库祛魅、BM25 检索与 Agent 状态库》（14 问）→](/opinion/db/ai-vector-endgame/)

- [文档库为何是弯路，PG 如何零成本平替芒果？](/opinion/db/ai-vector-endgame/#mongodb-covered-by-pg-jsonb) —— 可扩展关系模型向下兼容文档，`JSONB` 性能与一致性双杀芒果，配 FerretDB 可零代码平替。
- [芒果营销水分与套壳 PG 做分析的真相是什么？](/opinion/db/ai-vector-endgame/#mongodb-marketing-and-bi-hoax) —— 无模式易沦为脏数据泥潭，其官方 BI 连接器实为通过 FDW 拍平导进隐藏 PG 的套壳方案。
- [关系库生态繁荣，为何芒果却沦为造假孤岛？](/opinion/db/ai-vector-endgame/#mongodb-ecosystem-island) —— 营收导向压榨伙伴扼杀了原生工具生态，迫使官方硬上无算子下推的残次连接器沦为孤岛。
- [向量检索是真需求，独立向量库为何迅速遇冷？](/opinion/db/ai-vector-endgame/#dedicated-vector-db-pseudo-demand) —— 向量仅是两千行索引原语，长上下文与 `pgvector` 两头挤压令独立向量库失去生存空间。
- [算力泡沫出清，二线库被私募收割说明了什么？](/opinion/db/ai-vector-endgame/#gpu-db-death-and-pe-harvest) —— CPU 列存商品化判了独立 GPU 库死刑，停滞二线厂商与短视投机客终被市场与私募出清。
- [为什么说“向量是新 JSON”并驱动下个十年？](/opinion/db/ai-vector-endgame/#vector-is-the-new-json) —— 开发者拒绝跨库割裂，正如十年前 `JSONB` 收编文档库，`pgvector` 与 HNSW 正复刻下个十年统治力。
- [加装向量插件为何胜过拆库，亿级实测性能如何？](/opinion/db/ai-vector-endgame/#pgvector-vs-standalone-vector-db) —— 同表存取免同步且白捡 ACID 容灾，单核亿级检索仅 5 毫秒，挂只读从库即可线性扩展吞吐。
- [搜索引擎切入 PG 原生块存储为何是一次质变？](/opinion/db/ai-vector-endgame/#paradedb-bm25-and-block-storage) —— ParadeDB 接入原生块存储与缓冲池后彻底打通 WAL 复制、PITR 与 MVCC，免除异构 ES 同步。
- [软件坍缩为智能体加数据库，资本为何加冕 PG？](/opinion/db/ai-vector-endgame/#db-invariant-in-ai-era) —— 软件收敛为智能体加数据库，PG 已获巨头重金加冕，上层记忆与分支平台封装才是终极战场。
- [智能体为何困成缸中之脑，需补齐哪三大器官？](/opinion/db/ai-vector-endgame/#agent-brain-in-a-vat-and-organs) —— 割裂存储导致失忆与高延迟，须在库内补齐共址计算、图谱向量融合与数据分支三大器官。
- [智能体数据库要重写内核吗，为何唯独选 PG？](/opinion/db/ai-vector-endgame/#agent-db-boring-tech-pg) —— 新原语皆为传统内核机制延伸，唯独 PG 能在同一 ACID 事务内统合关系、向量、图与全文检索。
- [如何用 PGFS 给并行智能体装时光机与共享脑？](/opinion/db/ai-vector-endgame/#agent-state-pgfs-time-machine) —— 基于 JuiceFS 与 PG 共用 WAL 流，赋予智能体文件微秒级时间点回滚、瞬时分支与跨机并发共享。
- [自建全栈后端与智能体底座为何必须动静分离？](/opinion/db/ai-vector-endgame/#self-host-supabase-and-dify) —— 本地 NVMe 省三四个数量级成本且破除扩展阉割，无状态跑容器、有状态归高可用 PG 才稳健。
- [传统控制台为何卡住 AI，轻量后端怎上生产？](/opinion/db/ai-vector-endgame/#insforge-mcp-baas-production) —— 借 MCP 语义层打通 Agent 自主建表配权，精简至五容器并外接企业级高可用 PG 底盘上生产。

## 十二、可扩展性魔法与 PostgreSQL 发行版哲学 {#distro-philosophy}

> 专题全文：[《可扩展性魔法与 PostgreSQL 发行版哲学》（12 问）→](/opinion/db/distro-philosophy/)

- [可扩展性为何是 PG 吞噬数据库世界的魔法？](/opinion/db/distro-philosophy/#why-extensibility-eats-db-world) —— 保守内核与正交扩展产生乘数效应，以单一超融合平台取代多套异构专用库削减复杂度。
- [单机编译就能跑，生产为何仍需 PG 发行版？](/opinion/db/distro-philosophy/#why-pg-needs-a-distro) —— 裸内核离生产整车隔着自愈容灾鸿沟，透明可接管的开放信任供应链才是发行版终极壁垒。
- [只给打补丁软件包的发行版为何难平替云库？](/opinion/db/distro-philosophy/#orchestration-and-observability) —— 缺自动化编排与离线源斩不断云锁定，唯有自愈管控配千项指标诊断监控方能平替 RDS。
- [不套容器黑盒，如何在裸机与沙箱交付自愈库？](/opinion/db/distro-philosophy/#iac-sandbox-and-datalet) —— 靠无代理幂等剧本串联秒级自愈集群，配合同构本地沙箱与低代码大屏拉齐研发运维体验。
- [什么是“元发行版”，如何赋权十余种异构内核？](/opinion/db/distro-philosophy/#what-is-meta-distribution) —— 解耦控制平面与底层内核，用同一套高可用监控与六百扩展底座赋能十余种异构分支反垄断。
- [云厂商阉割扩展又白嫖，下半场为何属开源栈？](/opinion/db/distro-philosophy/#cloud-vampirism-and-local-first) —— 公有云高价白嫖且阉割核心扩展，唯有全功能本地优先开源发行版能夺回主权并省九成云税。
- [防白嫖浪潮下，发行版与包管理为何归宽松证？](/opinion/db/distro-philosophy/#relicense-to-apache2) —— 事实标准之争拼下游集成度，逆势回归 Apache 2.0 消除合规顾虑才能坐稳公共上游。
- [个人如何靠吃狗粮与中国高并发站上全球上游？](/opinion/db/distro-philosophy/#dogfooding-and-global-upstream) —— 经 250 万 QPS 极限实战淬炼，再啃下六七万跨平台包苦活成为全球同行的软件供应链上游。
- [单机版维多利亚为何能四倍速碾压普罗米修斯？](/opinion/db/distro-philosophy/#victoriametrics-replace-prometheus) —— 热路径零分配令单机顶替 12 台物理机且资源降四分之三，双单机双抓即可优雅替代分布式集群。
- [洛基为何沦为慢扫描，哪类开源项目值得托付？](/opinion/db/distro-philosophy/#victorialogs-vs-loki-pure-oss) —— Loki 缺全文索引易扫崩内存，列存压缩十倍且无风投催命变脸的 VictoriaLogs 才值得托付。
- [十万级软件仓上对象存储，如何做到原子发布？](/opinion/db/distro-philosophy/#sow-state-machine-atomic-publish) —— 借 SQLite 缓存将五万对象展开压至 300 毫秒，严守最后切入口指针契约实现无事务原子发布。
- [前端交付商品化后，文档站如何单二进制长寿？](/opinion/db/distro-philosophy/#oink-hugo-zero-node-docs) —— 靠 AI 融合三家所长并砍光 Node 与外部 CDN 依赖，单 `hugo` 二进制断网直出保五年长寿。

## 十三、500+ 扩展交付革命、包管理器 pig 与供应链安全 {#pig-supply-chain}

> 专题全文：[《500+ 扩展交付革命、包管理器 pig 与供应链安全》（14 问）→](/opinion/db/pig-supply-chain/)

- [扩展为何总装不上，包管理为何只做系统薄封？](/opinion/db/pig-supply-chain/#why-pig-wraps-native-pkg) —— 抛弃系统包另造私有格式是弯路，4MB 零锁定 `pig` 薄封 `apt/dnf` 并兜底国内源才可靠。
- [容器发镜像不香吗，为何死磕八十槽位原生包？](/opinion/db/pig-supply-chain/#containers-vs-linux-native-pkg) —— 主机生产与容器镜像构建底层皆依赖 `apt/dnf`，原生二进制仓是破解组合爆炸的唯一地基。
- [已有官方软件源，为何仍缺七成扩展必须自建？](/opinion/db/pig-supply-chain/#pgdg-gaps-and-rust-ban) —— 官方源拒收 Rust 扩展且双系割裂，自建补充源借 AI 修补对齐才补齐超七成第三方生态。
- [维护五百个扩展，会撞上哪些底层兼容与命名雷？](/opinion/db/pig-supply-chain/#abi-glibc-rust-naming-traps) —— 小版本破 ABI、`glibc` 符号断层与访问方法命名抢占频发，须靠低版本构建与元数据避撞。
- [智能体构建考古如何破五百大关并给上游捉虫？](/opinion/db/pig-supply-chain/#ai-build-archaeology-and-qa) —— AI 构建考古攻克跨系顽疾推破五百大关，16 平台滚动测试矩阵更能反向修补上游大厂漏洞。
- [第三方二进制仓如何自证清白并赋能内核演进？](/opinion/db/pig-supply-chain/#reproducible-builds-and-kernel-ci) —— 全开源脚本支持离线容器可复现编译自证清白，同时充当内核大版本与线程化演进的验证场。
- [苦筑数年的扩展仓库壁垒，为何免费送给同行？](/opinion/db/pig-supply-chain/#open-repo-for-peers-and-vendors) —— 以 Apache 2.0 搭配零流量费 CDN 免费赋能同行，用正和共赢确立全球扩展分发事实标准。
- [如何用目录、仓库与包管理终结扩展选型断层？](/opinion/db/pig-supply-chain/#catalog-repo-manager-trinity) —— 三位一体打通双语百科、全平台预编译仓与 `pig`，用标准化数字身份证把选型上线缩为一行命令。
- [扩展百科如何兼顾人机双友好，为何五改归朴？](/opinion/db/pig-supply-chain/#dual-friendly-docs-and-hugo) —— 纯净 Markdown 底稿喂饱 Agent、编译期短代码服务人类，五代折腾印证回归 Hugo 最稳妥。
- [高校镜像为何忌做生产上游，供应链靠谁兜底？](/opinion/db/pig-supply-chain/#mirror-sla-and-supply-chain-trust) —— 高校公益镜像无 SLA 承诺易断更，生产关键链路必须靠有人担责兜底的自控仓库。
- [源码正常的官方包，为何爆 18EB 假内存溢出？](/opinion/db/pig-supply-chain/#valkey-packaging-seam-bug) —— 陈年下游补丁混用内存释放函数且打包跳过了内核自检，令假溢出暗雷在接缝潜伏九年。
- [静态审查为何漏掉打包暗雷，智能体最该干啥？](/opinion/db/pig-supply-chain/#agent-package-destruction-testing) —— 静态审查抓不住跨层链接耦合，Agent 算力应投入全平台实装与注入故障的破坏性验证。
- [安装包内嵌泛域名私钥多致命，吊销怎难止血？](/opinion/db/pig-supply-chain/#wildcard-private-key-leak-ocsp) —— 泄露泛域名私钥可无感劫持全站流量与更新，OCSP 软失败令吊销滞后，私钥须锁入硬件模块。
- [内核清洗俄籍维护者，击碎了哪些无国界幻觉？](/opinion/db/pig-supply-chain/#linus-bdfl-and-geopolitical-split) —— Linux 本属个人独裁配 GPL 分叉竞争，但地缘清洗警示开源已按主权裂变，必须备好自主底牌。

## 十四、新存储引擎、PostGIS 时空加速与 FDW 武器库 {#multimodal-arsenal}

> 专题全文：[《新存储引擎、PostGIS 时空加速与 FDW 武器库》（8 问）→](/opinion/db/multimodal-arsenal/)

- [为何四倍吞吐才配换引擎，新引擎有何致命险？](/opinion/db/multimodal-arsenal/#orioledb-4x-and-tam-risks) —— OrioleDB 凭四倍吞吐与 S3 分层推迟分库，但自定义表访问方法直击数据完整性，尝鲜须谨慎。
- [异构协议拟态与兼容分支有哪些限制与代价？](/opinion/db/multimodal-arsenal/#protocol-mimicry-and-fork-tradeoffs) —— 协议代理受限于特殊文档格式，而改动解析器符号的兼容内核会导致预编译扩展全线失效。
- [新运行时与领域对象如何把库变成控制平面？](/opinion/db/multimodal-arsenal/#pg-as-data-control-plane) —— 免超管 Wasm 运行时、外卸算力与领域类型扩展收敛进单条 SQL，把 PG 升维为数据控制平面。
- [如何借库内文件系统做容灾并闭环隐私脱敏？](/opinion/db/multimodal-arsenal/#pgfs-pitr-and-pg-anonymizer) —— PGFS 共用 WAL 实现附件与库表同秒回滚，内核级安全标签声明式脱敏根除外部脚本漏列。
- [传统画框为何解不好近邻，空间索引怎压至毫秒？](/opinion/db/multimodal-arsenal/#postgis-knn-and-btree-gist) —— 告别半径画框魔数，用 GiST 流式算子配 `btree_gist` 复合聚簇将亿级表查询从 30 秒压至 1 毫秒。
- [行政区划与百万网段定位如何榨出十万级并发？](/opinion/db/multimodal-arsenal/#geodecode-and-inetrange-gist) —— 多边形切分聚簇令逆地理编码飙至 35 万 TPS，自定义 `inetrange` 范围索引将 IP 定位压至 0.34 毫秒。
- [如何巧用外部表管道免代理用 SQL 查宿主机？](/opinion/db/multimodal-arsenal/#file-fdw-unix-pipes) —— 借 `file_fdw` 管道配控制符分隔直拉系统命令输出，零代理在库内用 SQL 实时关联宿主机指标。
- [生产装空间与外部表扩展为何严禁盲目手编？](/opinion/db/multimodal-arsenal/#postgis-mongofdw-package-first) —— 复杂原生依赖链与失实构建脚本暗坑遍布，生产环境必须优先复用经验证的系统二进制包。

## 十五、MinIO 猝死、Silo 续命战与孤儿项目接盘 {#minio-silo-rescue}

> 专题全文：[《MinIO 猝死、Silo 续命战与孤儿项目接盘》（16 问）→](/opinion/db/minio-silo-rescue/)

- [十亿下载的对象存储霸主，为何步步自毁生态？](/opinion/db/minio-silo-rescue/#why-minio-self-destructed) —— 十亿估值资本催命将免费用户视为负资产，靠阉割断供与漏洞恐慌逼买商业版自毁信任。
- [六万星明星项目，按数据库标准看有多草台？](/opinion/db/minio-silo-rescue/#minio-under-pg-standard) —— 林纳斯定律在深水区失灵，末版潜伏假超时、分层误删生产数据与 9.8 分鉴权伪造等坏账。
- [原厂断供跑路，社区分叉如何避商标雷无缝接盘？](/opinion/db/minio-silo-rescue/#fork-legality-and-trademark) —— 借不可撤回的 AGPLv3 合法分叉并彻底更名避开商标雷，严锁磁盘与接口契约零停机接力。
- [清缴陈年漏洞与重建信任，如何守住不折腾边界？](/opinion/db/minio-silo-rescue/#hardening-and-silo-manifesto) —— 不做新特性专注修洞，用显式开关保护存量兼容，以不签 CLA 与透明溯源锁死开源承诺。
- [不写一行代码，单兵如何靠双模型对抗扛下修洞？](/opinion/db/minio-silo-rescue/#blind-manager-adversarial-agents) —— 靠两家异构大模型互掐编写与敌对审计补丁，叠加成熟打包管线将单兵维护成本降十倍。
- [双模型已能自主修洞，为何仍需人类拍板与众测？](/opinion/db/minio-silo-rescue/#human-judgment-and-crowd-moat) —— 打破历史兼容的取舍背锅唯有人工决断，全球生产众测与维护者持续在场才是终极壁垒。
- [主流开源对象存储，能否立即无缝平替存量集群？](/opinion/db/minio-silo-rescue/#no-silver-bullet-alternative) —— Ceph 太重而新兴方案缺权限或运维闭环，打齐安全补丁配内网隔离远胜盲目切换生涩引擎。
- [迁往新一代存储引擎，有哪些红线与仲裁差异？](/opinion/db/minio-silo-rescue/#rustfs-migration-and-quorum) —— 原地替换须全停机且限未加密盘，四挂二变砖与缺失 `/metrics` 拉取端点会冲击容灾监控。
- [有了宽松协议新引擎，生态为何仍需无聊的接替者？](/opinion/db/minio-silo-rescue/#silo-vs-rustfs-boringness) —— 新引擎演进必致运维漂移，Silo 拒绝新特性使缺陷总量收敛，专为存量提供零改动平替。
- [审视商业开源存储，为何盯商业边界胜过看许可证？](/opinion/db/minio-silo-rescue/#governance-cla-over-apache2) —— 宽松协议配 CLA 集权随时可重演断供，白纸黑字的发包承诺与商业边界比许可证更关键。
- [云存储掌门人收编分析鸭，预示着怎样的终局？](/opinion/db/minio-silo-rescue/#s3-acquires-duckdb-compute) —— 网络协议让嵌入式引擎具备云计费能力，S3 直接整合表格式与 DuckDB 使计算沦为存储配件。
- [自动扫洞渡劫期，停更项目与扩展怎沦为后门？](/opinion/db/minio-silo-rescue/#archived-oss-and-ai-vuln-era) —— 大模型全天候扫洞令失修代码急速腐化，归档断供更引发 CVE 无人认领与合规失效真空。
- [巨头天价并购为何裁掉备份支柱，公地怎破局？](/opinion/db/minio-silo-rescue/#snowflake-crunchy-commons-tragedy) —— AI 预算扭曲与云巨头白嫖挤压灾备公地，唯靠纯粹热爱配企业级付费支持双轮跨越周期。
- [备份神器归档七天获救，逼定价能抄作业吗？](/opinion/db/minio-silo-rescue/#pgbackrest-forced-pricing) —— 靠断供逼商业方算清替换账单需极高不可替代性，三天即现抢跑分叉足见行业自律脆弱。
- [团队被收编后子扩展为何断粮，续命靠哪三招？](/opinion/db/minio-silo-rescue/#forking-mooncake-and-vchord) —— 父依赖升级令失联子扩展瞬间瘫痪，靠抢救文档、硬核升级依赖链与年度兜底三招稳住交付。
- [供应链昂贵，为何孤儿接盘与入官方源门槛极高？](/opinion/db/minio-silo-rescue/#supply-chain-cost-and-stewardship-moat) —— 免费用户是宝贵众测团，但持续接盘与入官方源皆需真实用户盘子、硬核基建与分发公信力。

## 十六、为什么拒绝生产 Docker 跑库与 K8s 大辩论 {#no-docker-k8s}

> 专题全文：[《为什么拒绝生产 Docker 跑库与 K8s 大辩论》（10 问）→](/opinion/db/no-docker-k8s/)

- [为何 Docker 小版本升级会让索引报废？](/opinion/db/no-docker-k8s/#docker-glibc-index-corruption) —— 未锁系统代号的小版本升级会静默跨越 glibc 版本击穿 B-Tree 排序不变量，导致全库索引报废。
- [如何从根源斩断 glibc 升级毁索引的祸根？](/opinion/db/no-docker-k8s/#pg17-builtin-locale) —— 启用 PG 17 内置 C.UTF-8 排序提供程序斩断系统库依赖，局部按需调用 ICU 规则。
- [容器化跑生产库会引入哪些致命可靠性陷阱？](/opinion/db/no-docker-k8s/#docker-stateful-mismatch) —— 本地卷废掉迁移弹性却徒增复合故障点，命名空间隔离更易诱发双实例烤糊数据。
- [为何贪图初始化便利会毁掉数据库日常运维？](/opinion/db/no-docker-k8s/#container-day2-operations) —— 容器割裂包管理与备份管道，令装扩展、原地升级与拉起大从库陷入长期抽象泄漏。
- [“容器跑库几年没出事”为何只是幸存者偏差？](/opinion/db/no-docker-k8s/#container-survivor-bias) —— 可靠性只看极端故障下的 RTO/RPO 兜底，核心 OLTP 库离裸 Linux 越近越简单可靠。
- [OLTP 库进 K8s 为何陷入存储双输？](/opinion/db/no-docker-k8s/#k8s-pet-vs-cattle) —— 挂云盘损失数量级 IO 性能，绑本地盘废掉调度弹性并拖慢集群灾难恢复。
- [数据库进 K8s 为何违背分层并引爆排障复杂度？](/opinion/db/no-docker-k8s/#k8s-layer-inversion-complexity) —— 底层状态倒置诱发循环依赖雪崩与逃逸风险，叠加网络存储抽象后排障状态空间爆炸。
- [支持数据库进 K8s 的正方有哪些核心技术论据？](/opinion/db/no-docker-k8s/#k8s-counterpoint-operator) —— 正方主张靠 Operator 自愈与本地盘多副本普及管控，但封装藏不住凌晨三点的抽象泄漏。
- [万物皆上 K8s 是分工演进还是简历驱动杂耍？](/opinion/db/no-docker-k8s/#k8s-resume-driven-vs-economics) —— 现代裸机 PG 足撑企业上市，盲目上 K8s 多是简历驱动开发把复杂度账单留给雇主。
- [普通企业该用什么方案替代 K8s 管好数据库？](/opinion/db/no-docker-k8s/#bare-metal-iac-alternative) —— 用裸机或本地虚拟化配合 Ansible 声明式 IaC 发行版，兼得满血 NVMe 与自动化高可用。

## 十七、高可用 SOTA 拓扑、Etcd 暗雷与百万 QPS 连接池 {#ha-pooling-migration}

> 专题全文：[《高可用 SOTA 拓扑、Etcd 暗雷与百万 QPS 连接池》（15 问）→](/opinion/db/ha-pooling-migration/)

- [为何别信几个九 SLA，高可用硬指标是什么？](/opinion/db/ha-pooling-migration/#rto-rpo-over-sla) —— 高可用只认 RTO 与 RPO，靠 Patroni 延迟熔断或同步提交兜底并修掉 300 秒启动超时。
- [无共享流复制相比 RAC 与 Raft 赢在哪？](/opinion/db/ha-pooling-migration/#shared-nothing-vs-rac-raft) —— 消除存储单点与 Raft 写放大税，单主百兆级 WAL 配合数十只读副本可扛百万 QPS。
- [高可用如何幂等接入，VIP 与 DNS 怎么选？](/opinion/db/ha-pooling-migration/#haproxy-vip-dns-access) —— 全节点对称部署 HAProxy 屏蔽主从差异，按网络条件取舍 VIP 或 DNS 并以元节点自举。
- [同步集群如何编排级联拓扑与分级故障止血？](/opinion/db/ha-pooling-migration/#sync-cascade-topology-fencing) —— 并列直挂同步从库与流式归档防单点挂死，切主先严密隔离旧主再用 pg_rewind 归建。
- [Linux 原生编排赢在哪，为何必锁离线源？](/opinion/db/ha-pooling-migration/#k8s-vs-linux-native-distro) —— Linux 原生链路最短但忌裸连公网源，须靠发行版排雷并锁死本地离线软件源快照。
- [为何默认配置的 Etcd 是高可用集群定时炸弹？](/opinion/db/ha-pooling-migration/#etcd-2gb-timebomb) —— Etcd 默认关闭自动压实，写满 2GB 配额即转入维护模式罢工，上线前必须显式开启。
- [管控停摆如何解耦保命，黑盒商业软件怎么兜底？](/opinion/db/ha-pooling-migration/#control-data-plane-decoupling) —— 管控与存储解耦确保 Etcd 故障不伤数据，替换生产级 PG 底座可为黑盒软件外挂 PITR。
- [千级直连为何雪崩，连接池如何扛百万 QPS？](/opinion/db/ha-pooling-migration/#pgbouncer-scale-and-congestion) —— 多进程模型直连超载会引爆 LWLock 争用，靠多实例 PgBouncer 将万级连接收敛至个位数。
- [为何不能混用连接池，三种池化模式该怎么选？](/opinion/db/ha-pooling-migration/#pgbouncer-modes-and-routing) —— 在线交易走事务池高复用与熔断切流，管理操作与离线 ETL 绕过连接池直连实例。
- [如何观测 PgBouncer 水位并零中断维护？](/opinion/db/ha-pooling-migration/#pgbouncer-stats-and-reload) —— 紧盯 cl_waiting 排队水位，用 PAUSE 与 -R 套接字传递热升级且禁混用 query_timeout。
- [单主冲刺百万 QPS 如何控写负载与杀僵尸连接？](/opinion/db/ha-pooling-migration/#openai-pg-primary-scaling) —— 冻结原库增量写表、死守 5 秒锁超时轻量 DDL，并用连接最大寿命清退假活跃僵尸连接。
- [云 RDS 如何束缚 OpenAI，自建赢在哪？](/opinion/db/ha-pooling-migration/#cloud-rds-castration-vs-self-hosted) —— 云 RDS 阉割超管与系统权限锁死高级可观测与灰度调优，本地 NVMe 自建可全量解锁。
- [“空中换引擎”如何零停机迁移且步步可回滚？](/opinion/db/ha-pooling-migration/#zero-downtime-dual-write-migration) —— 靠幂等双写与分片短锁实现可回滚三步割接，避开双 psql 管道提前 0.1 秒放锁竞态。
- [平替微软库与对接 Dify 有哪些基建坑？](/opinion/db/ha-pooling-migration/#mssql-babelfish-and-dify-ops) —— WiltonDB 须纳管 1433 高可用与 PITR，对接 Dify 须预装向量扩展并收口代理路由。
- [自建 Supabase 与代理层须补哪些护栏？](/opinion/db/ha-pooling-migration/#production-supabase-and-mcp) —— 重签密钥并配齐 S3 冷备与三节点同步集群，在连接池代理层为 MCP 补齐权限防火墙。

## 十八、物理备份 PITR、瞬间克隆、删库急救与逻辑复制 {#backup-clone-cdc}

> 专题全文：[《物理备份 PITR、瞬间克隆、删库急救与逻辑复制》（17 问）→](/opinion/db/backup-clone-cdc/)

- [逻辑转储与 PITR 边界在哪，时间线有何深意？](/opinion/db/backup-clone-cdc/#backup-overview-pitr-timeline) —— 热备即持续 PITR 重放，8 位十六进制时间线前缀隔离历史分支以防日志覆写。
- [有了高可用热备，为何仍需延迟温备与流式归档？](/opinion/db/backup-clone-cdc/#warm-standby-and-pg-receivewal) —— 延迟温备抵御人为误删并持续验证备份，pg_receivewal 配合同步提交实现零丢数归档。
- [pgBackRest 如何跑满吞吐并揪出坏块？](/opinion/db/backup-clone-cdc/#pgbackrest-engine-and-stanza) —— 多核并行压缩跑满千兆网吞吐，传输同步核验页面校验和并靠异步归档防爆盘。
- [备份工具历经停更续命，生产为何切忌慌忙跳车？](/opinion/db/backup-clone-cdc/#pgbackrest-supply-chain-and-stay) —— 备份握有最高数据权限需严防供应链投毒，竞品各有硬伤且主线已续命宜按兵不动。
- [自建环境如何亚秒级零空间克隆 TB 级大库？](/opinion/db/backup-clone-cdc/#cow-reflink-instant-clone) —— 基于 XFS 写时复制与 PG 18 原生克隆，569 毫秒零空间派生近 800GB 真实沙盒。
- [实例级 Fork 如何零闪断救误删并赋能智能体？](/opinion/db/backup-clone-cdc/#instance-fork-pitr-and-agent-cli) —— 原子备份包裹写时复制秒拉影子实例演练 PITR，配结构化预演 CLI 安全编排。
- [将 PG 挂载为文件系统适合什么业务场景？](/opinion/db/backup-clone-cdc/#pgfs-boundary) —— 适合低频中小附件场景，牺牲部分裸吞吐以白嫖 ACID 事务与 PITR 秒级恢复。
- [为何单盘删光数据库与备份是神仙难救的死局？](/opinion/db/backup-clone-cdc/#same-disk-xfs-unrecoverable) —— NVMe 加 XFS 同盘删光文件后无法靠 pg_filedump 掏残骸，必须事前隔离异机冷备。
- [为何企业宁花几十万抢救，也不事前搭好备份？](/opinion/db/backup-clone-cdc/#bianque-preventive-economics) —— 治未病无戏剧性易被忽视，但零成本开源备份防线的性价比碾压事后几十万抢救百倍。
- [生产库爆炸的黄金抢救期，管理层最忌讳什么？](/opinion/db/backup-clone-cdc/#golden-window-escalation) —— 切忌在头 48 小时黄金窗口开会砍价，须建立分钟级拍板授权的紧急事故升级预案。
- [基础软件越新越安全吗，主机高危漏洞怎么修？](/opinion/db/backup-clone-cdc/#cve-regression-patch-baseline) —— 代码回归会让新系统反中招，须按包版本核查并用系统包管理器后向补丁固化进基线。
- [流式 CDC 为何能收编异构库，靠哪四块基石？](/opinion/db/backup-clone-cdc/#cdc-vs-etl-and-four-pillars) —— 以 PG 为单一事实源收编异构从库，依托逻辑解码、快照导出、流复制与复制槽闭环。
- [逻辑解码有何妙用，生产上须兜底哪四大盲区？](/opinion/db/backup-clone-cdc/#logical-decoding-plugins-and-pitfalls) —— 可反向生成回滚 SQL，但须兜底缺 DDL 序列、同步提交挂死、重复投递与切主丢槽。
- [复制标识有何约束，换索引与开 FULL 有何坑？](/opinion/db/backup-clone-cdc/#replica-identity-traps) —— 候选索引须全列非空，替换索引漏刷会使标识退化报错，大表禁开 FULL 防全表扫描。
- [逻辑复制如何追快照，改表与切流守什么铁律？](/opinion/db/backup-clone-cdc/#logical-rep-statemachine-ddl-seq) —— 切流前必须推高订阅端序列防主键冲突，改表死守加列先下游、删表先上游的顺序。
- [撞上复制冲突或源端失联，如何解围防爆盘？](/opinion/db/backup-clone-cdc/#logical-rep-conflict-and-slots) —— 冲突时修数据或推进位点解围，远端失联解绑订阅后务必清理上游孤儿槽防爆盘。
- [PG 17 补齐了哪些逻辑复制短板以逼近零停机？](/opinion/db/backup-clone-cdc/#pg17-logical-failover-and-upgrade) —— 打通升级保留逻辑槽、切主槽同步与物理从库转逻辑订阅，告别 TB 级数据重刷。

## 十九、版本升级风控、运维纪律与 AI 时代的造车 DBA {#upgrade-ops-dba}

> 专题全文：[《版本升级风控、运维纪律与 AI 时代的造车 DBA》（17 问）→](/opinion/db/upgrade-ops-dba/)

- [为何 PG 19 临门大砍特性，大版本怎么选？](/opinion/db/upgrade-ops-dba/#pg19-cuts-and-major-version-cadence) —— 可靠性高于功能清单，新大版本至少等 11 月 .1 小版本及核心扩展就绪再上生产。
- [旧大版本五年 EOL 意味着什么，如何平滑跨代？](/opinion/db/upgrade-ops-dba/#major-eol-and-blue-green-upgrade) —— 五年停产后不再发安全补丁，宜赶在过保前用逻辑复制蓝绿部署零停机跨代升级。
- [铁桶般的 PG 为何单次井喷 28 个 CVE？](/opinion/db/upgrade-ops-dba/#ai-fuzzing-cve-explosion) —— 大模型符号推理配 Fuzzer 令挖洞成本塌方，正对三十年存量 C 代码做系统性重扫。
- [为何连不可信源端或漏双端升级会让宿主机沦陷？](/opinion/db/upgrade-ops-dba/#client-reverse-attack-and-pgdump-cve) —— 恶意上游可借符号链接反制客户端，修补 pg_dump 偷换关系漏洞必须双端同步升级。
- [为何 PG 连年小版本翻车，生产节奏怎么拿捏？](/opinion/db/upgrade-ops-dba/#minor-release-regressions-and-buffer) —— 封闭赶工安全补丁频发回归故障，无紧迫漏洞威胁时应避开首发留出两周缓冲期。
- [小版本为何破 ABI，遇高分漏洞该抢修吗？](/opinion/db/upgrade-ops-dba/#minor-abi-contract-and-cve-tradeoff) —— 内部结构体变动曾撞崩扩展 ABI，须对冲高分漏洞苛刻利用前提与补丁回归半径。
- [为何小版本升级不能只换二进制，怎么人工善后？](/opinion/db/upgrade-ops-dba/#minor-upgrade-post-fix-and-ha-bugs) —— 替换二进制不改存量目录与坏索引，升级后必须按发布说明刷写系统表与重建索引。
- [集群四层实体如何拆解，实例名为何禁带主从词？](/opinion/db/upgrade-ops-dba/#entity-model-and-naming-rules) —— 拆解集群节点实例服务四层抽象，实例名终生不变并将动态主从角色剥离至服务层。
- [高危 DDL、误删急救与例行保养死守哪些军规？](/opinion/db/upgrade-ops-dba/#ddl-redlines-and-routine-maintenance) —— 禁强杀进程与直接删表，索引强制并发创建，日常巡检表膨胀与事务年龄防回卷。
- [如何免密穿透跳板机并规范部署远程管理工具？](/opinion/db/upgrade-ops-dba/#ssh-bastion-and-pgadmin-ops) —— 用公私钥配合 ProxyCommand 与连接复用秒穿跳板机，以虚拟环境 Web 模式部署管理台。
- [有了发行版与内核书，普及 PG 还缺哪块拼图？](/opinion/db/upgrade-ops-dba/#implicit-context-skills-and-tutorials) —— 新手常卡在买云机、配域名与通 SSH 等文档外的隐性工程常识，亟需全栈实战教程。
- [裸跑内核为何必踩坑，国内为何缺造车 DBA？](/opinion/db/upgrade-ops-dba/#pg-engine-vs-distro-dba) —— 裸内核只是发动机，须靠集成高可用备份监控的整车发行版跨越攒车高门槛。
- [分析与交易岗谁先被替代，自动调优边界在哪？](/opinion/db/upgrade-ops-dba/#olap-vs-oltp-ai-replacement) —— 代码生成型 OLAP 岗先被冲击，成熟发行版默认参数已够用使自动调优商业空间有限。
- [AI 重塑阶层下，顶级 DBA 如何拿百倍杠杆？](/opinion/db/upgrade-ops-dba/#dba-service-as-software-leverage) —— 底层基本功在 AI 时代逆势升值，靠 90% 管控软件加 9% 智能体兑现专家百倍杠杆。
- [手敲代码的程序员谢幕后，如何转型智能体指挥官？](/opinion/db/upgrade-ops-dba/#programmer-to-agent-commander) —— 人类价值向设计品味与结果担责两端收敛，须拉满顶配算力在实战中锤炼统帅手感。
- [当标准答案通货膨胀，为何提问与品味是终极壁垒？](/opinion/db/upgrade-ops-dba/#question-and-taste-moat) —— 大模型是编译器而追问是负熵源码，真实历练沉淀的品味是对抗平滑平庸的最后护城河。
- [老司机跨界前端与出海开源，什么才是真硬骨头？](/opinion/db/upgrade-ops-dba/#cross-stack-and-english-first-docs) —— 专家半天指路即可靠 AI 摆平跨栈重构，出海真硬骨头是人工打磨英文优先权威文档。

## 二十、WAL 日志先行、MVCC 膨胀治理与新硬件演进 {#wal-mvcc-bloat}

> 专题全文：[《WAL 日志先行、MVCC 膨胀治理与新硬件演进》（8 问）→](/opinion/db/wal-mvcc-bloat/)

- [PostgreSQL 先写脏页还是先写 WAL？](/opinion/db/wal-mvcc-bloat/#wal-before-dirty-page) —— 内存先改脏页再构造日志，刷盘靠页头 pd_lsn 触发 XLogFlush 强制日志先落盘。
- [追加写 MVCC 与新存储引擎该如何权衡？](/opinion/db/wal-mvcc-bloat/#mvcc-tradeoff-and-tam) —— 追加写换取无锁读与流复制优势，实验性 UNDO 或列存引擎慎上核心生产以防锁死。
- [表空间该如何核算，怎样零 I/O 测算膨胀率？](/opinion/db/wal-mvcc-bloat/#table-size-and-bloat-estimate) —— 汇总表树与索引核算真实容量，用统计视图对齐公式可在 50 毫秒内零 I/O 算完大库膨胀。
- [表体积为何只增不减，pg_repack 有何坑？](/opinion/db/wal-mvcc-bloat/#autovacuum-and-pg-repack) —— 并发清理不缩减物理文件，pg_repack 须预留双倍空间并在强杀后手工清理残留触发器。
- [单机 PG 的吞吐上限与新硬件演进方向在哪？](/opinion/db/wal-mvcc-bloat/#scalability-ceiling-and-hardware) —— 单机上限在百兆级 WAL 重放，正攻克异步直接 I/O 并向 HBM 与 CXL 异构内存演进。
- [多线程化为何难落地，C 扩展 ABI 有多脆弱？](/opinion/db/wal-mvcc-bloat/#threading-and-extension-abi) —— 多线程化会打破数百个 C 扩展私有内存假设，细微结构体变动即可引爆指针寻址崩溃。
- [小版本升级为何会在流复制与 TOAST 上翻车？](/opinion/db/wal-mvcc-bloat/#minor-upgrade-regressions) —— 底层并发恢复与 TOAST 多字节估算切片耦合极深，曾引发备库自死锁与截取报错。
- [初始化为何必守 C.UTF8 而禁设中文排序？](/opinion/db/wal-mvcc-bloat/#locale-c-utf8-and-nls) —— 非 C 排序慢十倍且废掉前缀索引扫描，旧版中文消息目录更存在反向错译与越界缺陷。

## 二十一、并发隔离异常、八级锁队列与时间编码基石 {#isolation-locks-time}

> 专题全文：[《并发隔离异常、八级锁队列与时间编码基石》（12 问）→](/opinion/db/isolation-locks-time/)

- [MySQL 半成功事务错在哪，PG 怎样容错？](/opinion/db/isolation-locks-time/#acid-atomicity-savepoint) —— MySQL 放行报错事务部分提交违背原子性，PG 默认中止事务并靠隐式保存点优雅容错。
- [SQL 隔离级别如何名实错位，读已提交有何隐患？](/opinion/db/isolation-locks-time/#isolation-levels-and-read-skew) —— SQL 标称隔离名实错位，读已提交难防丢失更新与读偏差，备份对账须用快照隔离。
- [快照隔离为何漏掉写偏差，如何根治跨行并发异常？](/opinion/db/isolation-locks-time/#write-skew-and-ssi) —— 快照隔离漏检不相交行写偏差，根治须靠悲观锁物化冲突或启用 SSI 乐观重试。
- [一致性与 CAP 被误读多久，分布式为何靠共识？](/opinion/db/isolation-locks-time/#consistency-cap-and-consensus) —— ACID 不变量不同于线性一致性，共识算法旨在解决协调者单点可用性死穴。
- [形式化验证难落地，基础软件靠什么守住质量底线？](/opinion/db/isolation-locks-time/#formal-verification-vs-battle-testing) —— TLA+ 重在暴露隐含假设而 DST 落地滞后，海量真实生产负载众测闭环才是终极防线。
- [站在数据库内核视角，如何对区块链与智能合约祛魅？](/opinion/db/isolation-locks-time/#blockchain-byzantine-wal) —— 区块与智能合约本质是哈希链 WAL 与存储过程，吞吐孱弱且商用场景极窄。
- [八级表锁如何演化，为何视图里查不到磁盘行锁？](/opinion/db/isolation-locks-time/#table-locks-and-vxid) —— 八级表锁完备解耦读写与维护自斥，行锁记在元组头并借事务 ShareLock 阻塞等待。
- [毫秒级加空列为何引发雪崩，大表 DDL 怎么拆？](/opinion/db/isolation-locks-time/#lock-queue-and-online-ddl) —— 排队中的排他锁会阻塞后续全部只读请求，线上 DDL 必设锁超时并拆分为弱锁并发步进。
- [线缆协议如何定界，手写七层连接代理要注意什么？](/opinion/db/isolation-locks-time/#wire-protocol-and-proxy) —— v3 协议靠 ReadyForQuery 确定性定界，七层代理不卸载 TLS 时须回单字节 N 降级 SSL 探测。
- [本地抓包为何不见明文，混杂与监控模式差在哪？](/opinion/db/isolation-locks-time/#wireshark-capture-and-rfmon) —— 本地抓明文须走回环口并禁 SSL，跨无线网嗅探原始 802.11 帧须开网卡射频监控模式。
- [闰秒与 2038 大限何来，存时间有哪些暗坑？](/opinion/db/isolation-locks-time/#leap-seconds-2038-timestamptz) —— 4 字节时间戳面临 2038 溢出，PG 必用 TIMESTAMPTZ 并禁传数字时区串防反转。
- [为何 UTF-16 成包袱而 UTF-8 通吃？](/opinion/db/isolation-locks-time/#utf8-vs-utf16-encoding) —— UTF-16 代理对兼具变长与端序包袱，UTF-8 凭无端序、兼容 ASCII 与前缀自同步一统天下。

## 二十二、黄金监控指标、PG Load 水位与慢查询微分治理 {#monitoring-and-tuning}

> 专题全文：[《黄金监控指标、PG Load 水位与慢查询微分治理》（11 问）→](/opinion/db/monitoring-and-tuning/)

- [三千指标如何做减法，为何 QPS 管不住水位？](/opinion/db/monitoring-and-tuning/#golden-metrics-hierarchy) —— 报错仅能事后报丧而 QPS 抹平请求轻重，唯有归一化饱和度能统领告警与扩容。
- [如何构造跨机型归一化的 PG Load 指标？](/opinion/db/monitoring-and-tuning/#pg-load-kpi) —— 对连接池事务总时长求导除以核数即得 PG Load，统一吞吐、延迟与空闲长事务惩罚。
- [内置统计视图有何滞后，新一代查询遥测怎么做？](/opinion/db/monitoring-and-tuning/#stats-collector-and-telemetry) —— 内置统计视图有三重滞后，逐条分位数遥测宜用无背压环形队列旁路流式推入 ClickHouse。
- [日志怎么配，如何免搭 ELK 用 SQL 查？](/opinion/db/monitoring-and-tuning/#csvlog-and-file-fdw) —— 开启 csvlog 按周轮转并用 file_fdw 映射外部表，免搭 ELK 即可用 SQL 原地分析日志。
- [CPU 不高为何负载爆表，怎样读懂主机指标？](/opinion/db/monitoring-and-tuning/#linux-cli-diagnostics) —— Load 含不可中断磁盘睡眠进程，内存看零换页，磁盘看 iostat 队列与延迟。
- [存储与异构库 OLTP 压测有哪些口径与红线？](/opinion/db/monitoring-and-tuning/#fio-and-sysbench-benchmark) —— FIO 须绕过缓存测 8KB 随机与 1MB 顺序吞吐且禁写生产裸盘，异构对比统一用 sysbench。
- [裸查统计视图有何盲区，怎样揪出刷日志真凶？](/opinion/db/monitoring-and-tuning/#pgss-blindspots-and-wal) —— PGSS 须做时序差分算每秒执行时长，求导 wal_fpi 可揪出回滚废事务与只读提示位刷盘。
- [上千类 SQL 按何优先级调优，怎样定性慢查询？](/opinion/db/monitoring-and-tuning/#macro-tuning-workflow) —— 优先治理全局占比大头，用窗口平均 RT 区分硬件饱和与单句劣化，靠块行比抓缺索引。
- [高频点查为何严控一毫秒内，慢查询怎样五步止血？](/opinion/db/monitoring-and-tuning/#one-ms-sla-and-slow-query) —— 30 有效核配 1ms 延迟恰撑起 3 万 QPS，按五步法核实顺序扫描并在线补索引即可止血。
- [零扫描索引能直接删吗，清理废索引有哪些陷阱？](/opinion/db/monitoring-and-tuning/#dummy-and-duplicate-indexes) —— 清理废索引须剔除唯一约束并核对部分索引条件，一律走 CONCURRENTLY 无锁删除。
- [脚本编排 psql 跑批如何防半提交与锁库？](/opinion/db/monitoring-and-tuning/#psql-bash-and-batch-ops) —— 跑批必加遇错即停与单事务参数，海量清洗借库内状态表拆为微事务步进。

## 二十三、生产雪崩复盘：XID 回卷、死锁自救与裸页抢救 {#postmortems-and-rescue}

> 专题全文：[《生产雪崩复盘：XID 回卷、死锁自救与裸页抢救》（10 问）→](/opinion/db/postmortems-and-rescue/)

- [分库减半负载为何反致崩盘，连接池怎样被吞噬？](/opinion/db/postmortems-and-rescue/#shard-paradox-and-pool-starvation) —— 迁走快查询推高重请求并发占比触发劣化，慢查询蚕食打满连接池彻底挤死快请求。
- [配了超时为何仍堆慢查询，从库假死怎样秒级回血？](/opinion/db/postmortems-and-rescue/#cancel-request-and-watch-rescue) —— 客户端弃等须发 Cancel Request 才生效，假死急救用半秒轮询取消查询免重连风暴。
- [报错退出的备份工具如何毒化连接池，怎样根治？](/opinion/db/postmortems-and-rescue/#pgbouncer-connection-pollution) —— 低版 pg_dump 清空搜索路径后报错退出会污染事务池，须强制开启每次归池重置会话。
- [事务号回卷为何逼停生产库，急救冻结要注意什么？](/opinion/db/postmortems-and-rescue/#xid-wraparound-rescue) —— 32 位事务年龄逼近 21 亿会停写护盘，须含 TOAST 表按年龄降序拉满流控精准冻结。
- [表不大为何主键序列会溢出，无法改表时怎样续命？](/opinion/db/postmortems-and-rescue/#sequence-overflow-rescue) —— UPSERT 每次暗耗序列号致 32 位主键溢出，绝境可挖空洞 ID 建队列发号表赢取改表窗口。
- [重启时钟回拨为何会让 Patroni 拒绝接管？](/opinion/db/postmortems-and-rescue/#ntp-stepback-patroni-failure) —— NTP 晚于 PG 启动并回拨时钟会导致 postmaster.pid 时间校验失配，开机必先同步时钟。
- [坏扩展锁死超级用户如何自救，怎样预留逃生通道？](/opinion/db/postmortems-and-rescue/#broken-extension-global-2964) —— 坏预加载库锁死全连接时须停库十六进制抹除 global/2964，日常必留纯净超管逃生号。
- [遇到数据页损坏如何算偏移并从备库无损捞数？](/opinion/db/postmortems-and-rescue/#invalid-page-ctid-recovery) —— 按 8KB 块号对 1GB 整除取模定位坏页偏移，优先去健康流复制从库按 ctid 无损捞回记录。
- [生产主库为何严禁开启坏页内存抹零参数？](/opinion/db/postmortems-and-rescue/#zero-damaged-pages-trap) —— 坏页内存抹零会放行重复主键击穿从库唯一性，且会被 VACUUM 格式化落盘永久毁灭现场。
- [实例烤糊无法启动时，如何从裸数据页抢救全库？](/opinion/db/postmortems-and-rescue/#pg-filedump-bare-metal-rescue) —— 先按固定 OID 还原四张字典表生成 pg_filedump 脚本，再拼回 TOAST 切片并逐字节解码数组。

## 二十四、开发规约、强类型主键建模与无锁在线改表 {#schema-types-ddl}

> 专题全文：[《开发规约、强类型主键建模与无锁在线改表》（10 问）→](/opinion/db/schema-types-ddl/)

- [如何避开黑盒误区，用 AI 沙箱吃透现代 PG？](/opinion/db/schema-types-ddl/#learn-pg-fast-flywheel) —— 弃用云与容器黑盒，在两分钟重建的原生沙箱中配终端 AI 导师验证五大演进脉络。
- [进阶独当一面的数据库大法师要打通哪三大支柱？](/opinion/db/schema-types-ddl/#postgres-mage-pillars) —— 贯通多模极简生态观、协议索引内核级开发与黄金监控无锁急救三大确定性支柱。
- [库内外对象如何命名，才能根除引号污染与路由混乱？](/opinion/db/schema-types-ddl/#naming-convention-order) —— 库内严守 63 字节纯小写下划线根除双引号污染，库外对齐 DNS 三段式统一路由与监控。
- [服务端为何必锁 C.UTF-8 防索引静默腐坏？](/opinion/db/schema-types-ddl/#collation-utf8-immutability) —— OS 升级致 glibc 漂移会静默毁坏索引，服务端须锁死内置不可变 C.UTF-8 排序规则。
- [建表有哪些强类型铁律，为何严禁高频更新宽表？](/opinion/db/schema-types-ddl/#table-design-mvcc-width) —— 坚持强类型与标准身份列，超 15 列高频更新宽表须冷热纵向拆分防写放大。
- [主键为何禁用 32 位整型，雪花算法输在哪？](/opinion/db/schema-types-ddl/#bigint-vs-snowflake) —— 整数主键必用 64 位 BIGINT 防溢出，SnowflakeID 受制于机器号协调与时钟回拨撞号死穴。
- [时序 UUID 强在哪，历史日志如何逆向补号？](/opinion/db/schema-types-ddl/#uuid-v1-bit-backfill) —— UUID v1 兼顾局部单调与防回拨，借 PG 位串算子可按历史时间戳逆向合成与反解。
- [为何禁有符号整型存 IPv4，历史区划怎样回溯？](/opinion/db/schema-types-ddl/#inet-and-temporal-adcode) —— 有符号整型存 IPv4 致半数地址变负宜改用 inet，区划配 tstzrange 复合 GiST 可回溯历史。
- [为何改列常触发整表重写，不停机改列的机理是什么？](/opinion/db/schema-types-ddl/#online-alter-column-lock-split) —— 非二进制兼容改列会锁表重写，须靠影子列、触发器双写与分批回填无锁切换。
- [大表主键无锁升 64 位，如何均匀切片并防膨胀？](/opinion/db/schema-types-ddl/#alter-pk-histogram-vacuum) —— 借等频直方图均匀切片回填，每批穿插显式 VACUUM 抑膨胀并用 USING INDEX 瞬时切主键。

## 二十五、特种索引陷阱、排他约束与高阶 SQL 武器库 {#indexes-advanced-sql}

> 专题全文：[《特种索引陷阱、排他约束与高阶 SQL 武器库》（16 问）→](/opinion/db/indexes-advanced-sql/)

- [如何按负载匹配 PG 索引，并避开空值降序暗坑？](/opinion/db/indexes-advanced-sql/#index-selection-and-nulls-order) —— 按负载匹配 BRIN/GIN/GiST 与部分索引，可空列降序查询与索引须同步声明 NULLS LAST。
- [为何 GIN 数组重叠搜索会退化为平方级复杂度？](/opinion/db/indexes-advanced-sql/#gin-overlap-quadratic-catalog) —— 底层 arrayoverlap 采用双层循环逐一比对，双侧长数组重叠检索呈平方级爆炸须截断词表。
- [如何免外部组件，用原生 PG 做亚毫秒模糊搜索？](/opinion/db/indexes-advanced-sql/#custom-chinese-fuzzy-search) —— 用不可变函数提取中英拼音词素建 GIN 表达式索引召回，配编辑距离精排达亚毫秒响应。
- [向空库注入生产统计信息后，为何执行计划仍失真？](/opinion/db/indexes-advanced-sql/#pg-regresql-planner-hook) —— 规划器默认探测空表物理页缩放估算，须借 pg_regresql 钩子强制锁定注入的目录统计值。
- [地道 SQL 如何敬畏三值逻辑并削减往返开销？](/opinion/db/indexes-advanced-sql/#three-valued-logic-and-idioms) —— 可空列安全判等须用 IS NOT DISTINCT FROM，借 EXISTS 短路、数组参数与 RETURNING 折叠往返开销。
- [如何用专属语法取分组极值并靠索引消除排序？](/opinion/db/indexes-advanced-sql/#distinct-on-group-top1) —— DISTINCT ON 配确定性排序一步截分组首行，复合索引对齐列序与空值规则可消除排序。
- [自定义函数为何毁索引，三级易变性契约差在哪？](/opinion/db/indexes-advanced-sql/#function-volatility-contract) —— 默认 VOLATILE 禁走索引条件且逐行重算，只读与纯函数须分别显式声明 STABLE 与 IMMUTABLE。
- [如何用一行排他约束根除会议撞期与网段重叠？](/opinion/db/indexes-advanced-sql/#exclude-constraint-gist) —— 依托 btree_gist 与 EXCLUDE 排他约束，一行 DDL 即可在引擎层拦截区间交叉与网段重叠。
- [高频存储过程如何根治临时表膨胀与回滚丢日志？](/opinion/db/indexes-advanced-sql/#pg-variables-and-autonomous-log) —— 用 pg_variables 内存变量免除临时表目录膨胀，配 dblink 伪自治事务留存回滚诊断日志。
- [纯 SQL 能否闭环推荐系统，自连接边界在哪？](/opinion/db/indexes-advanced-sql/#sql-itemcf-recsys-boundary) —— 三元组自连接可五分钟闭环协同过滤，上规模须靠离线长尾剪枝突破二次方瓶颈。
- [生产大表用触发器与逻辑复制，须防哪些锁与暗坑？](/opinion/db/indexes-advanced-sql/#trigger-locks-and-replica-role) —— 停触发器必用 USER 防废除外键，留意建触发器重锁、COPY 逐行触发及逻辑复制角色隔离。
- [如何用触发器实现防篡改审计，且不拖垮业务写入？](/opinion/db/indexes-advanced-sql/#audit-trigger-security-fillfactor) —— 用 SECURITY DEFINER 锁搜索路径防篡改，配满填充因子压实页面并捕获异常免回滚业务。
- [多实例如何免挂外部队列，靠 PG 原生同步缓存？](/opinion/db/indexes-advanced-sql/#listen-notify-cache-sync) —— 行级触发器配 pg_notify 透明广播变更主键，客户端监听回源拉取即可强一致同步本地缓存。
- [高并发流量如何靠快慢隔离与连接池纪律防雪崩？](/opinion/db/indexes-advanced-sql/#traffic-isolation-and-pgbouncer) —— 慢查询物理剥离至 Offline 从库，在线走事务连接池严控 1ms 超时并禁改会话参数防污染。
- [Go 操作连接池时，如何防范句柄泄漏与空值崩溃？](/opinion/db/indexes-advanced-sql/#go-sql-pool-leak-null) —— 维护 sql.DB 单例、严格关闭 Rows 并用 Exec 执行写操作，靠 NOT NULL 与 COALESCE 根除空值崩溃。
- [Go 预编译语句为何会爆炸，有状态操作如何隔离？](/opinion/db/indexes-advanced-sql/#go-prepare-and-tx-state) —— 池化 Stmt 繁忙时会跨连接裂变预编译句柄，单连接有状态操作必须显式绑定在 sql.Tx 内。
