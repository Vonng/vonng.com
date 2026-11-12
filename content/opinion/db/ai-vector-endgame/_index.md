---
title: 向量数据库祛魅、BM25 检索与 Agent 状态库
linkTitle: 向量祛魅与 AI 状态库
description: 独立向量数据库消亡逻辑、pgvector 与 ParadeDB 混合检索、Agent 时代零胶水底座。
weight: 110
icon: fa-solid fa-wand-magic-sparkles
---

独立文档库与专用向量库皆是阶段性弯路，大模型时代的长期记忆、BM25 混合检索与并行智能体状态终将坍缩回同一 ACID 事务边界，由超融合 PostgreSQL 一统底座。

## 一、NoSQL 幻灭与独立向量库祛魅 {#nosql-and-vector-disenchantment}

### 文档库为何是弯路，PG 如何零成本平替芒果？ {#mongodb-covered-by-pg-jsonb}

无模式文档库只是重蹈反范式冗余覆辙，诚如 Stonebraker 所断定，可扩展关系模型天生向下兼容文档。MongoDB 在 Jepsen 一致性测试中漏洞百出，JSON 读写与分析更在 OnGres/EDB 实测中被单机扛数百 TB 的 PostgreSQL `JSONB` 吊打；配齐 FerretDB 协议兼容层，不改代码即可零授权费平替闭源 SSPL 的芒果。

- [MongoDB没有未来：好营销救不了烂芒果 · 功能被PGSQL覆盖](/db/bad-mongo/#功能被pgsql覆盖)
- [MongoDB没有未来：好营销救不了烂芒果 · 正确性与性能被吊打](/db/bad-mongo/#正确性与性能被吊打)
- [MongoDB没有未来：好营销救不了烂芒果 · MongoDB没有未来](/db/bad-mongo/#mongodb没有未来)

### 芒果营销水分与套壳 PG 做分析的真相是什么？ {#mongodb-marketing-and-bi-hoax}

MongoDB 是 Stonebraker 痛批“靠好营销卖烂产品”的典型：公关上拿客户总估值碰瓷成大单金额，生产中放任无模式写入沦为脏数据泥潭。更讽刺的内幕被 John De Goes 扒出：MongoDB 3.2 吹嘘的 SQL BI 连接器，竟靠 Python Multicorn FDW 把文档粗暴拍平丢字段后塞进隐藏的 PostgreSQL 查询——与其倒进 PG，不如直接用 PG。

- [MongoDB没有未来：好营销救不了烂芒果 · 烂产品靠营销上位](/db/bad-mongo/#烂产品靠营销上位)
- [MongoDB：现在由PostgreSQL强力驱动？ · 掀开内幕](/db/mongo-powered-by-pg/#掀开内幕)
- [MongoDB：现在由PostgreSQL强力驱动？ · 再见了，MongoDB！](/db/mongo-powered-by-pg/#再见了mongodb)

### 关系库生态繁荣，为何芒果却沦为造假孤岛？ {#mongodb-ecosystem-island}

繁荣生态源于边界克制与共生分润。据 John De Goes 披露，MongoDB 伙伴团队直属首席营收官，一心榨取传统大厂费用而冷落原生周边创业者，亲手造出生态荒漠；面对报表刚需只能大包大揽，明知旧版 FDW 毫无算子下推仍强行上线赝品。数据库厂商的正道是死磕 ACID、列存与复制等内核硬骨头，而非隐瞒依赖透支诚信。

- [MongoDB：现在由PostgreSQL强力驱动？ · MongoDB：孤家寡人，孤岛一座](/db/mongo-powered-by-pg/#mongodb孤家寡人孤岛一座)
- [MongoDB：现在由PostgreSQL强力驱动？ · 全力以赴](/db/mongo-powered-by-pg/#全力以赴)

### 向量检索是真需求，独立向量库为何迅速遇冷？ {#dedicated-vector-db-pseudo-demand}

独立向量数据库是两头受挤的伪需求：小场景被暴涨 32 倍的大模型长上下文吞噬，标准场景被成熟关系库迅速接管。如 Stonebraker 与 Andy Pavlo 所言，向量库只是“关系型 Blob + 内存图索引”——PG 百万行内核搞定事务灾备，`pgvector` 不到两千行 C 代码即补齐向量；Supabase 百万级 1536 维实测其在延迟、吞吐与成本上全线优胜 Pinecone。

- [2025 年度数据库世界总结：石破天 vs Andy Pavlo 对谈录 · 4. 向量数据库是"内存图索引 + 关系型 blob"，护城河不宽](/db/db-year-review-2025/#4-向量数据库是内存图索引--关系型-blob护城河不宽)
- [专用向量数据库凉了吗？ · 向量数据库是一个伪需求吗？](/db/svdb-is-dead/#向量数据库是一个伪需求吗)
- [专用向量数据库凉了吗？ · 通用数据库 vs 专用数据库](/db/svdb-is-dead/#通用数据库-vs-专用数据库)
- [专用向量数据库凉了吗？ · 案例PvP：pgvector vs pinecone](/db/svdb-is-dead/#案例pvppgvector-vs-pinecone)

### 算力泡沫出清，二线库被私募收割说明了什么？ {#gpu-db-death-and-pe-harvest}

数据库市场正在冷酷出清伪命题泡沫。按 Andy Pavlo 复盘，Voltron Data 倒闭与 HeavyDB 被收编，印证现代 CPU 列存算力早已商品化，独立 GPU 库难逃死刑；同时风投撤离向量库，MariaDB、Couchbase、SingleStore 批量落入私募股权手中榨取存量维护费，而蹭 AI 风口强赶付费客户两月搬迁的 Tembo 更反证基建唯靠长期契约存活。

- [Andy Pavlo：2025 数据库世界年度总结 · Andy 的看法](/db/db-in-2025/#andy-的看法-4)
- [数据库茶水间：OpenAI拟收购Supabase ？ · 搞 DB 的狂蹭 AI](/db/openai-supabase-rumor/#搞-db-的狂蹭-ai)

## 二、向量是新 JSON 与库内混合检索质变 {#vector-and-hybrid-search}

### 为什么说“向量是新 JSON”并驱动下个十年？ {#vector-is-the-new-json}

正如 Jonathan Katz 复盘 `json` 到 `jsonb` 演进所揭示的：只要能把关联数据留在成熟关系栈内，开发者宁忍早期局限也不愿拆库。PG 原生数组缺距离算子、`cube` 锁死 100 维装不下 1536 维 Embedding，催生了向量扩展；正如十年前 `JSONB` 统合文档与关系缔造黄金十年，`pgvector` 与快达 20 倍的 HNSW 索引必将领跑 AI 十年。

- [向量是新的 JSON · JSON 简史：PostgreSQL 实现](/pg/vector-json-pg/#json-简史postgresql-实现)
- [向量是新的 JSON · 向量崛起：一种新 JSON](/pg/vector-json-pg/#向量崛起一种新-json)
- [向量是新的 JSON · 译者评论](/pg/vector-json-pg/#译者评论)

### 加装向量插件为何胜过拆库，亿级实测性能如何？ {#pgvector-vs-standalone-vector-db}

合格的向量库首先得是合格的数据库：大模型权重只是有损压缩，精确长期记忆须入库做 K-NN 召回；在 PG 内装 `pgvector` 同表存取业务列与向量，免跨库同步且白捡 ACID 与 PITR。它借 ANN 索引以 `lists` 与 `probes` 权衡召回与延迟，M1 Max 单核实测百万条 1536 维仅 8ms、1 亿条 128 维 5ms、SIFT 1M 低至 1.8ms，挂从库即可线性扩吞吐。

- [AI大模型与向量库 PGVector · AI是怎么工作的](/pg/llm-and-pgvector/#ai是怎么工作的)
- [AI大模型与向量库 PGVector · PG向量插件 PGVECTOR](/pg/llm-and-pgvector/#pg向量插件-pgvector)
- [向量是新的 JSON · PGVECTOR: 开源PG向量扩展](/pg/vector-json-pg/#pgvector-开源pg向量扩展)
- [AI大模型与向量库 PGVector · PGVECTOR 的性能](/pg/llm-and-pgvector/#pgvector-的性能)

### 搜索引擎切入 PG 原生块存储为何是一次质变？ {#paradedb-bm25-and-block-storage}

外挂 Elasticsearch 饱受同步延迟之苦，内置 `tsvector` 又缺 BM25 评分与大表混合排序。ParadeDB 将 Rust 搜索库 Tantivy 封装进库内免除 ETL，而真正的质变在 `pg_search` 0.14：它告别私管外部文件的“缝合怪”形态，全面接入 PG 原生块存储与缓冲池，写入提速数倍并原生打通 WAL 流复制、崩溃恢复、PITR 与 MVCC。

- [PG生态新玩家：ParadeDB · ParadeDB解决什么问题？](/pg/paradedb/#paradedb解决什么问题)
- [PG生态新玩家：ParadeDB · ParadeDB 的构建方式](/pg/paradedb/#paradedb-的构建方式)
- [PostgreSQL 生态前沿进展 · ParadeDB](/pg/pg-frontier/#paradedb)

## 三、Agent 状态底座与 BaaS 动静分离 {#agent-state-and-baas}

### 软件坍缩为智能体加数据库，资本为何加冕 PG？ {#db-invariant-in-ai-era}

前端正坍缩为对话框，后端半数被智能体替代、半数下沉进 BaaS，唯独承载状态的数据库是 AI 时代唯一坚挺的不变量，软件全面收敛为 `Agent + Database`。从 OpenAI、Cursor 靠主从 PG 扛顶级负载，到 Databricks 十亿美元买 Neon、Supabase 获重金追捧，资本已加冕 PG；但终极决战在于谁先把分支、图谱、向量与 MCP 整合为开箱即用的智能体平台。

- [别争了，AI时代数据库已经尘埃落定 · 为什么是 PostgreSQL？](/db/db-for-ai/#为什么是-postgresql)
- [数据库茶水间：OpenAI拟收购Supabase ？ · OpenAI 收购 Supabase？](/db/openai-supabase-rumor/#openai-收购-supabase)
- [Agent 需要什么样的数据库？ · 六、真正的竞争在哪里](/db/agent-native-db/#六真正的竞争在哪里)

### 智能体为何困成缸中之脑，需补齐哪三大器官？ {#agent-brain-in-a-vat-and-organs}

智能体在现场笨重健忘，病根在于栖身“关系库 + 向量库 + 脚本”割裂栈中缺失统一“数字躯体”，重启失忆且跨网反射弧漫长。突破自主天花板须在库内补齐三大器官：靠 `PL/Python`、`PL/Rust` 数据共址锻造零延迟“肌肉记忆”；融合向量与图谱构建动态“联想记忆”（GraphRAG 多跳准确率 87%，纯向量仅 23%）；借数据分支瞬时克隆赋予反事实试错的“想象力”。

- [Agent 需要什么样的数据库？ · 一、缸中之脑](/db/agent-native-db/#一缸中之脑)
- [Agent 需要什么样的数据库？ · 三、范式革命的三个维度](/db/agent-native-db/#三范式革命的三个维度)

### 智能体数据库要重写内核吗，为何唯独选 PG？ {#agent-db-boring-tech-pg}

支撑智能体范式革命无需重写底层存储引擎：向量、图遍历、库内计算与分支克隆只是扩展索引、存储过程与 MVCC 写时复制的自然延伸，久经考验的 ACID、WAL 与优化器仍是精确地基。专用库各管一摊，而唯有允许扩展深度介入规划器与事务系统的 PostgreSQL，能把 `pgvector`、`Apache AGE` 与 BM25 收进同一 ACID 边界，根除跨库同步泥潭。

- [Agent 需要什么样的数据库？ · 四、一个被忽视的真相](/db/agent-native-db/#四一个被忽视的真相)
- [Agent 需要什么样的数据库？ · 五、PostgreSQL 的压倒性优势](/db/agent-native-db/#五postgresql-的压倒性优势)

### 如何用 PGFS 给并行智能体装时光机与共享脑？ {#agent-state-pgfs-time-machine}

多智能体并行与跨机协同时，裸文件锁与轮询只会造出蹩脚数据库。用 JuiceFS 把文件元数据与数据块同存 PostgreSQL（PGFS），所有文件写入即汇入同一套 WAL 事务：零硬件成本即可让工作区文件与业务表同步做微秒级 PITR 回滚并瞬时克隆试错分支；多端凭一行连接串即可挂载百 MB/s 缓存目录，配合 MVCC 与 `LISTEN/NOTIFY` 建成“共享大脑”。

- [把 Agent 的状态放进数据库 · Agent 到底需不需要数据库？](/db/agent-state-db/#agent-到底需不需要数据库)
- [把 Agent 的状态放进数据库 · 杀手锏一：时光机](/db/agent-state-db/#杀手锏一时光机)
- [把 Agent 的状态放进数据库 · 杀手锏二：共享大脑](/db/agent-state-db/#杀手锏二共享大脑)

### 自建全栈后端与智能体底座为何必须动静分离？ {#self-host-supabase-and-dify}

突破 Supabase 云 500MB 门槛后，存储溢价较本地 NVMe 贵三四个数量级，且仅开放 64 个扩展并将 `pg_graphql`、`wrappers` 等锁进私有镜像；照搬官方或 Dify 演示 Compose 混编裸库与冗余向量容器更缺容灾监控。生产正解是动静分离：无状态网关跑容器，有状态底座统一交给预装齐 440+ 扩展与 `pgvector` 的高可用原生 PG 集群托管。

- [自建Supabase：创业出海的首选数据库 · Supabase是什么？](/db/supabase/#supabase是什么)
- [自建Supabase：创业出海的首选数据库 · 为什么要自建？](/db/supabase/#为什么要自建)
- [PG系创业公司Supabase：`$80M` C轮融资 · Supabase  B 轮/C 轮融资 `80M $`](/pg/supabase-series-c/#supabase--b-轮c-轮融资-80m-)
- [使用Pigsty自建Dify：AI工作流平台 · Pigsty的准备工作](/pg/dify-setup/#pigsty的准备工作)

### 传统控制台为何卡住 AI，轻量后端怎上生产？ {#insforge-mcp-baas-production}

编码智能体十分钟能写出前端，却常卡在配库上线，因为传统 BaaS 网页控制台是为人类点鼠标设计的黑盒。InsForge 架起 MCP 语义层，让 Agent 直接读写表结构、RLS 与日志闭环全栈交付，并砍掉开源 Supabase 十余个容器里的重网关，用 TypeScript 与 PostgREST 瘦身至 5 个容器；上生产时甩掉内置单节点容器库、接入 Pigsty 高可用底盘即可兼得敏捷与稳健。

- [InsForge：为 Vibe Coding 而生的 Supabase · 关键差异：语义层](/db/insforge/#关键差异语义层)
- [InsForge：为 Vibe Coding 而生的 Supabase · 架构拆解：简化版 Supabase](/db/insforge/#架构拆解简化版-supabase)
- [InsForge：为 Vibe Coding 而生的 Supabase · 纳入 Pigsty 全家桶](/db/insforge/#纳入-pigsty-全家桶)
