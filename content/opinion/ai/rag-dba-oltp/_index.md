---
title: RAG 祛魅、具身 DBA 与无嘴模型 OLTP
linkTitle: RAG 祛魅与具身 DBA
description: 专用向量库与重型 RAG 退潮、PostgreSQL 统治力、DBA 具身化与无嘴模型首帧判别。
weight: 70
icon: fa-solid fa-database
---

专用向量库与脱离底层的调参玩具正在退潮，克制而可扩展的 PostgreSQL 已一统智能体数据底座。真正能上生产的 AI 基建，必须具身扎根原生运行时并以确定性兜底锁死风险。

## 一、RAG 退潮、向量祛魅与 PostgreSQL 统治力 {#rag-and-postgres}

### 向量为何只是基础数据类型，专用向量库输在何处？ {#vector-is-json}

正如没人会为存 JSON 拆套独立库，向量只是现代数据库标配的数据类型。专用向量库输在架构位置尴尬：把主数据放 PG、向量拆外部，删改一行记录就得背上沉重的 CDC 同步与对账债，远不如在单 PostgreSQL 事务内用 `pgvector` 原子维护原文、向量与权限。“揣而锐之，不可长保”，过度特化的组件最速朽，留白的通用底座最耐活。

- [RAG 没死，但也快了 · 向量还是有用，只是没那么神](/ai/rag-is-dead/#向量还是有用只是没那么神)
- [RAG 没死，但也快了 · 专用向量数据库，问题出在位置上](/ai/rag-is-dead/#专用向量数据库问题出在位置上)
- [赛博道德经：设计结构，而非规定行为 · 七、系统的“有”与“无”：通用基础设施的道家注解](/ai/cyber-daodejing/#七系统的有与无通用基础设施的道家注解)

### 内核克制的 PG 凭什么击败新贵赢下智能体时代？ {#why-pg-won-ai}

拒绝将向量硬塞进核心的 PostgreSQL 反而通吃全场，赢在“克制内核加极致可扩展性”这一元能力：170 万行成熟 ACID 内核托举约 8000 行 `pgvector` 便衍生出繁荣生态，一年提速 150 倍终结了独立向量赛道。单引擎统合关系、向量、JSON、GIS、全文与图，一行 SQL 省去千行胶水代码与上下文开销，与端侧 SQLite 共同锁定了双极胜局。

- [AI 时代，PostgreSQL 凭什么赢了？ · PG 做对了什么？](/ai/postgres-and-ai/#pg-做对了什么)
- [AI时代，软件从数据库开始 · AI 时代，哪些数据库有机会](/ai/ai-agent-era/#ai-时代哪些数据库有机会)
- [Claude Code泄密：MCP 爆火的隐藏真相 · Agent 时代数据库的命运](/ai/mcp-hidden-truth/#agent-时代数据库的命运)

### 价值坍缩终点为何归于 PG 并迈向终极运行时？ {#pg-ultimate-runtime}

从 Databricks 与 Snowflake 豪掷并购、Supabase 估值 50 亿美元到云厂悉数兼容，PostgreSQL 已成默认的“数字现实接口”。在 Agent OS 中，它身兼海马体、断点盘、向量页表、锁队列 IPC 与审计黑匣子五职，且模型零提示词即精通 `psql`；面向机器高频并发交互，PG 正借毫秒级分支向上吞并运行时、向下封装操作系统。

- [AI撕掉了软件的皮 · 六、价值坍缩的终点](/ai/saas-burn-pg-rise/#六价值坍缩的终点)
- [AI Agent 的操作系统时刻 · 三、外存（数据库）：确定性最高的机会](/ai/agent-os/#三外存数据库确定性最高的机会)
- [AI撕掉了软件的皮 · 七、终极运行时](/ai/saas-burn-pg-rise/#七终极运行时)

### 数据库世代更替看哪三要素，PG 凭什么逆袭？ {#mysql-to-pg-era}

按瑞典马工的三要素框架，数据库世代胜负取决于“套件绑定、标杆背书与生态正反馈”。MySQL 赢在 LAMP 分发与 Facebook 背书；PostgreSQL 逆袭 2020 年代，则因 Heroku 与 Vercel 将其设为平台隐形默认底座令选型摩擦归零，叠加 Instagram、OpenAI 背书与 BSD 协议激发云厂投入完成一统。

- [MySQL赢了2000s，PostgreSQL赢得2020s，谁将赢得AI时代？——数据库选型的三要素分析法 · 为什么 MySQL 赢了 2000s](/ai/db-choice-ai-era/#为什么-mysql-赢了-2000s)
- [MySQL赢了2000s，PostgreSQL赢得2020s，谁将赢得AI时代？——数据库选型的三要素分析法 · 要素一：技术套件 - 从具名技术栈到平台默认](/ai/db-choice-ai-era/#要素一技术套件---从具名技术栈到平台默认)

### 有技术硬伤的数据库为何仍能统治市场，选型怎么看？ {#three-factors-rational-choice}

三要素网络效应足以压倒技术硬伤，顺应套件生态往往是企业最理性的经济账。正如马工所举：国产库重金兼容 Oracle 是借存量套件与人才栈，无索引无主键的 BigQuery 凭 Spotify 标杆与跨云生态在北欧拿下 45% 采用率；互联网选 MySQL 或 PG 皆属特定套件约束下的理性博弈，工程师应抛弃阵营粉圈心态，用客观规律审视架构。

- [MySQL赢了2000s，PostgreSQL赢得2020s，谁将赢得AI时代？——数据库选型的三要素分析法 · 用三要素理论看 BigQuery 在北欧的流行](/ai/db-choice-ai-era/#用三要素理论看-bigquery-在北欧的流行)
- [MySQL赢了2000s，PostgreSQL赢得2020s，谁将赢得AI时代？——数据库选型的三要素分析法 · 研究问题，而不是当粉丝](/ai/db-choice-ai-era/#研究问题而不是当粉丝)

### 数据库选型权移交智能体后，靠什么决定赢家通吃？ {#agent-db-selection-power}

当 Neon 上 80% 新实例已由智能体自动创建，数据库选型权正移交 AI，开放文档完备度与社区语料密度反超跑分成为核心胜负手，滚起“语料越厚、越被默认推荐、新实践越多”的马太雪球。按马工三要素推演，下一阶段决胜关键在于嵌入 Claude Code、Cursor 等编程套件成为默认协作库，替大模型接管强一致事务、模式演进与会话审计。

- [AI 时代，PostgreSQL 凭什么赢了？ · Agent 的数据库选择权](/ai/postgres-and-ai/#agent-的数据库选择权)
- [MySQL赢了2000s，PostgreSQL赢得2020s，谁将赢得AI时代？——数据库选型的三要素分析法 · 条件一：成为 AI 编程套件的一部分](/ai/db-choice-ai-era/#条件一成为-ai-编程套件的一部分)

## 二、DBA 具身化、新 LAMP 栈与受控工具网关 {#embodied-dba-and-mcp}

### 为何单靠一根数据库连接串做不出专家级运维智能体？ {#ottertune-peephole-lesson}

数据库自动驾驶立于高可用备份“身体”、可观测“眼睛”与标准变更“手脚”之上。OtterTune 烧光 1200 万美元倒闭，死穴正是仅凭一根连接串调参——连接串只是门上猫眼，既无历史趋势也改不了重启参数，更穿不透 OS、磁盘与网络排查级联故障；脱离底层原生运行时，永远做不出专家级 DBA。

- [给 DBA Agent 以身体 · 8 数据库需求金字塔](/ai/dba-agent-body/#8-数据库需求金字塔)
- [Agent 的护城河：强龙不压地头蛇 · OtterTune：一个价值 1200 万美元的教训](/ai/agent-moat/#ottertune一个价值-1200-万美元的教训)
- [给 DBA Agent 以身体 · 21 没有 Runtime，就没有专家级 DBA](/ai/dba-agent-body/#21-没有-runtime就没有专家级-dba)

### 原生 Linux 为何才是运维智能体的最佳身体？ {#dba-runtime-iac-moat}

运维智能体的身体仅三种选择：云 RDS 是专有 API 锁死的“笼子”，K8s Operator 是抽象厚重的“太空服”，唯有 Pigsty 这类原生 Linux 开源发行版才是无黑盒短路径的自由剧场。声明式基础设施即代码（IaC）就是智能体的中心法则，一份配置清单即全局拓扑源码；“龙会换代，地不会变”，模型极速折旧，确定性运行时地盘才是真护城河。

- [Agent 的护城河：强龙不压地头蛇 · DBA Agent 的身体，只有三个选择](/ai/agent-moat/#dba-agent-的身体只有三个选择)
- [给 DBA Agent 以身体 · 24 IaC 是 Agent 的中心法则](/ai/dba-agent-body/#24-iac-是-agent-的中心法则)
- [Agent 的护城河：强龙不压地头蛇 · 龙会换代，地不会变](/ai/agent-moat/#龙会换代地不会变)

### 多租户云短板在哪，怎敢让智能体直连生产库？ {#prod-safety-net-copilot}

多租户云为防扩展提权漏洞（如 PostGIS 历史提权）被迫阉割两千余扩展，撑不起企业主权账本。敢让智能体连生产库的底气从不是模型不犯错，而是犯错兜得住的基础设施——把高可用、任意秒级回滚 PITR、零成本克隆与数百扩展封装成可读 Skill；同时因事故追责无法转移给机器，生产运维必须严守“只读诊断加人工拍板执行”边界。

- [应用层塌缩：当 Agent 吃掉软件，护城河退守数据库 · 七、云给不了的那一半](/ai/sor-harness/#七云给不了的那一半)
- [应用层塌缩：当 Agent 吃掉软件，护城河退守数据库 · 八、你敢让 Agent 连生产库吗](/ai/sor-harness/#八你敢让-agent-连生产库吗)
- [给 DBA Agent 以身体 · 26 只读建议可以，自动执行要谨慎](/ai/dba-agent-body/#26-只读建议可以自动执行要谨慎)

### 面向智能体开发的“新 LAMP”底座长什么样？ {#new-lamp-stack}

运维语料匮乏令部署监控成了写意编程最大卡点，新一代全栈底座已收敛为 `Linux + Agent + Monitoring + PostgreSQL`。借 JuiceFS 将文件元数据存入 PG，即可让代码与库共享 PITR 一键时光回滚；同理，合规自建生产级 Dify 无需魔改，只需用带 `pgvector` 的高可用外部 PG 替换内置玩具容器即可稳健托底。

- [软件3.0时代，AI带来的范式转移 · 老冯评论](/ai/software-3-0/#老冯评论)
- [给 DBA Agent 以身体 · 29 新时代的 LAMP Stack](/ai/dba-agent-body/#29-新时代的-lamp-stack)
- [Dify 被重复骑脸羞辱：我太难了！](/ai/dify-humiliated/)

### 数据库 MCP 怎安全落地，存储过程为何复兴？ {#mcp-and-stored-procedures}

早期裸开任意 SQL 的数据库 MCP 无异于生产自杀，必须像 Google GenAI Toolbox 那样用声明式 YAML 锁死带参数校验的白名单 SQL 模板，在单一网关统合多源引擎。更深层的趋势是存储过程文艺复兴：把多步逻辑下沉入库能将接口从细碎 DAO 拉升回高内聚 Service 层，省去上下文膨胀与网络往返，PG 与 Oracle 将分食最大红利。

- [Google AI工具箱：生产级数据库MCP来了？ · 快速上手](/ai/google-mcp/#快速上手)
- [Google AI工具箱：生产级数据库MCP来了？ · 特性说明](/ai/google-mcp/#特性说明)
- [Google AI工具箱：生产级数据库MCP来了？ · 老冯评价](/ai/google-mcp/#老冯评价)

### 狂飙期最致命的数据隐患在哪，上云就能保安全吗？ {#naked-db-security}

比起空谈远期模型失控，当下最致命的祸患是重算法轻运维导致的数据库公网裸奔。Wiz Research 几分钟便扫出 DeepSeek 曾将无认证 ClickHouse 敞开在公网 8123/9000 端口，浏览器即可直读超百万行日志与明文密钥；同时“上云保平安”纯属伪命题，云巨头屡爆高危漏洞证明安全只取决于专业治理而非主机归属。

- [Wiz: DeepSeek数据库暴露 · 主要启示](/ai/deepseek-db-exposed/#主要启示)
- [Wiz: DeepSeek数据库暴露 · 老冯评论](/ai/deepseek-db-exposed/#老冯评论)

## 三、无嘴模型 OLTP 时刻、内核重写迷思与发行版壁垒 {#oltp-model-and-kernel}

### 无嘴模型凭何开启 OLTP，嵌入控制流防哪三坑？ {#shutup-model-oltp}

自回归思维链是慢且波动的“全表扫描”OLAP，砍掉生成循环、只做前向直觉判别的无嘴模型则是“走索引点查”OLTP，延迟按 `max(2PL/C, W/B)` 压进百毫秒，首次能同步嵌入请求与数据库触发器。把概率层塞进控制流等于内置查询优化器，必须严防三坑：重尾错误须最小化最大遗憾、拒犯多问独立性假设谬误、持续反馈重校准对抗分布漂移。

- [无嘴模型：AI 的 OLTP 时刻 · 五、OLTP 时刻](/ai/jev-shutup-model/#五oltp-时刻)
- [无嘴模型：AI 的 OLTP 时刻 · 九、每个程序都要长出一个优化器](/ai/jev-shutup-model/#九每个程序都要长出一个优化器)

### Rust 重写数据库跑通测试就等于生产可用吗？ {#pgrust-truth-and-tests}

别信凭空造内核神话：`pgrust` 首版从零写了两个月即夭折，轰动社区的二版实为 `c2rust` 机械直译出满屏 `unsafe` 后，用 Claude 在 13 天洗出 240 万行译文，反证复杂内核离不开三十年源码沉积。跑通 4.6 万条 SQL 更非生产就绪：公开脚本关掉 `fsync` 串行测试，完全漏检并发锁竞争与掉电刷盘缺陷，“快 300 倍”实来自列存改造。

- [AI 用 Rust 重写 PostgreSQL？别逗了 · 一、你看到的已经是第二条命](/ai/rewrite-pg-in-rust/#一你看到的已经是第二条命)
- [AI 用 Rust 重写 PostgreSQL？别逗了 · 二、你测试的，到底是什么？](/ai/rewrite-pg-in-rust/#二你测试的到底是什么)

### 机械转译漏掉了哪几层内核可靠性，扩展为何是死门？ {#kernel-reliability-and-extensions}

数据库可靠性分回归测试、防御性代码形状、三十年邮件列表里的取舍因果与老兵防坑直觉四层；从 `fsyncgate` 到 Jepsen 反例都证明机械转译最多搬走前两层，带不走后两层默会知识。更致命的是 1600 余扩展（如百万行 PostGIS）深度耦合内部 C 接口与共享内存长期合同，跨语言重写必困于 `unsafe` 兼容税或生态断裂的死局。

- [AI 用 Rust 重写 PostgreSQL？别逗了 · 四、回归测试到底带走了什么](/ai/rewrite-pg-in-rust/#四回归测试到底带走了什么)
- [AI 用 Rust 重写 PostgreSQL？别逗了 · 五、扩展是一份长期合同](/ai/rewrite-pg-in-rust/#五扩展是一份长期合同)

### 代码极速通缩，为何自研替代内核仍难获信任？ {#code-deflation-trust-moat}

AI 把代码压成白菜价，却压不短生产信任必须熬的日历时间。魔改分支深陷悖论：不改无独立价值，大改如 openGauss 换线程模型后仅适配 GIS 就追债近两年，继承的兼容与信任全丢。检验自研真伪只看修 Bug 迭代能否跑赢全球社区；与其掀地基重造车，不如做好把成熟内核与数百扩展封装成开箱即用发行版的“赛车手”。

- [AI 用 Rust 重写 PostgreSQL？别逗了 · 六、代码在通缩，信任没有](/ai/rewrite-pg-in-rust/#六代码在通缩信任没有)
- [请 Claude 为老冯画像与估值 · 三、我认为真正有价值的几个洞见](/ai/claude-opc-eval/#三我认为真正有价值的几个洞见)

### 掌控扩展分发仓库与全矩阵打包为何具有咽喉级价值？ {#distro-repo-leverage}

从 npm、Docker Hub 到 RedHat Network，谁掌握软件分发仓库谁就握住了生态咽喉。在 PostgreSQL 缺乏官方扩展仓库的空白处，编目两千余扩展、打包近六百扩展并成为海外同行上游源的基建拥有极高战略期权；而千亿 Token 最强的杠杆正是填平这类苦力活，助我在 16 个发行版乘 5 个 PG 大版本上达成了 32,240 个构建组合全覆盖。

- [请 Claude 为老冯画像与估值 · 四、抛开商业，他有没有投资价值？](/ai/claude-opc-eval/#四抛开商业他有没有投资价值)
- [OPC 一个月烧 1000 刀订阅，能有多少产出？ · PGEXT.CLOUD：扩展生态](/ai/yield-with-agents/#pgextcloud扩展生态)
