---
title: "RAG 没死，但也快了"
date: 2026-09-02
authors: [vonng]
summary: >
  RAG 这个词还活着，但向量 RAG 那套架构是 4K 窗口逼出来的应急方案。约束没了，向量召回退成了一个默认算子，活下来的检索全是数据库最擅长的事。
tags: [AI, PostgreSQL, 向量, 技术评论]
ai: true
---

发明 RAG 的人，专门买了个域名，用来证明 RAG 没死。

今晚老冯要参加 PG 三十周年系列直播的第七期，主题是 PG + AI。主持人做了份手卡，里面有一问是这么写的：

> “RAG 火了两年了——就是让大模型‘查你的私有资料’再回答。PG 在这套架构里到底扮演什么角色？只存向量，还是连元数据、权限、对话记忆都兜住？”

老冯盯着这个问题看了半天，觉得它问错了。

不是问得不好，是问题的前提已经站不住了：**RAG 这个词还活着，但 RAG 这套架构正在退场，它的心脏——向量召回——已经退成了一个默认算子。** 问 PG 在一个退场中的架构里演什么角色，意义不大；有意义的问题是，这套架构退场之后，什么东西留下来了。

先把利益相关说了：老冯做 PostgreSQL 发行版，pgvector 是 Pigsty 打包的第一批扩展之一，[PGEXT.CLOUD](https://pgext.cloud/) 上收了两千多个 PG 扩展的元数据。所以下面凡是对老冯有利的数字，都主动打了折；凡是对老冯不利的事实，也照说不误。

## 发明者的辟谣

去年这个话题吵得很凶，老冯本来想直接写一篇《RAG 已死》。动笔前翻了翻原始资料，发现标题得往回收半步。

2020 年把 RAG 这个词带到世界上的那篇论文，共同作者之一 Douwe Kiela，现在是 Contextual AI 的 CEO。2025 年他专门写了篇博客，标题就叫《RAG is dead, long live RAG!》，反驳“长上下文让 RAG 过时”的说法，公司还为此买了个域名。2026 年 1 月 The New Stack 又采访了他一次，他的说法是：大家把它重新包装成了 context engineering，里面包含 MCP 和 RAG；RAG 里的 R 就是 retrieval，你用 MCP 做检索，那也是 RAG。文章还提到，RAG 仍然在 Contextual AI 的技术栈里，只是首页上不再突出这个词。

所以发明者没有放弃 RAG，老冯不能替他宣布死亡。但请注意：一个技术名词，需要它的发明者买个域名出来论证它没死，需要把定义放宽到“只要检索了就算”才能活着，还要从自家首页上撤下来——这个词的处境，大家心里有数。

RAG 的字面意思是“检索增强生成”，只要模型在生成前去外面找了东西，都算。这个定义宽到没法死。而大多数人 2023 年学到、2024 年上线、今天还在跑的那个“RAG”，是一个具体得多的东西：

> 文档切片 → embedding → 存向量库 → 问题也转成向量 → 余弦相似度 → 捞 Top-K → 塞进 prompt。

这条流水线的心脏是向量召回。老冯这篇要说的就是它：**作为架构的 RAG 正在退场，向量召回从靶心退成了一个默认算子。** 取代它的是两样更老、更笨、更好用的东西：全文检索，和让 Agent 自己多翻几轮。

## Coding Agent 最后选了 grep

第二份证词比发明者的辟谣硬得多。

Claude Code 的创造者 Boris Cherny，2025 年 5 月在 Latent Space 播客上讲过：他们早期试过 RAG，试过几种搜索工具，最后落在 agentic search 上，因为它“outperformed everything, by a lot”。2026 年初他在 X 上又补了一段：早期版本的 Claude Code 用的是 RAG 加本地向量库，很快发现 agentic search 效果更好，也更简单，还没有安全、隐私、信息陈旧、可靠性那些老毛病。

Anthropic 后来把这个做法写进了方法论。2025 年 9 月那篇《Effective context engineering for AI agents》说得很具体：`CLAUDE.md` 这类文件预先塞进上下文，剩下的靠 `glob` 和 `grep`，让模型即时（just-in-time）去取它需要的文件，绕开索引过期的问题；读一个文件，文件引用另一个文件，递归读下去，上下文是自己攒出来的，这叫渐进披露（progressive disclosure）。

翻译成人话：**地表最强的 Coding Agent，最后选择了 `grep`。**

不是因为向量检索不好，是因为让模型自己去找，比你替它猜准。

学术界在往同一个方向跑。Search-R1 这类工作用强化学习训练模型，让它在推理过程中自己决定什么时候搜、搜什么，在 7B 模型上相对经典 RAG 基线有两成以上的相对提升。论文自己管这个叫 retrieval-augmented reasoning。活下来的是多轮、自适应、由模型驱动的检索；退场的是一次性、固定 Top-K、由相似度驱动的召回。MCP 没有标准化任何检索算法，它只是把“检索”从一条要专门搭的流水线，变成了 Agent 随手就能调的一个工具。

## RAG 是 4K 时代逼出来的应急方案

要理解向量 RAG 为什么会退场，得先理解它为什么会生。

RAG 论文 2020 年就发了，比 ChatGPT 早两年半，当时没几个人在意。让它变成人人会念的三个字母的，是 2023 年的上下文窗口：ChatGPT 4K，后来 8K，GPT-4 最大 32K。你有一本三百页的产品手册想让模型照着回答，塞不进去。怎么办？

于是有了这套流水线：把文档切成小块，每块用 embedding 模型转成向量，存进向量数据库；用户提问时把问题也转成向量，做相似度搜索，捞出最像的 Top-K 个块，塞进 prompt，让模型照着答。

挑的办法其实有很多——倒排索引、BM25、知识图谱，这些东西都比 RAG 老得多——但 embedding 加余弦相似度是当时最顺手、教程最多、一个下午能跑通 Demo 的那个。整条流水线——切片、embedding、向量库、相似度、Top-K——**每一个环节都是对“窗口太小”这个约束的妥协。**

问题是，约束消失了，架构还留在原地。

## 三个结构性病根

有人会说，“窗口大了 RAG 就没用了”这个论证太粗糙。行，那不谈窗口，只谈向量召回自己的毛病。这三条不是调参能调好的，是方案的先天缺陷。

**第一，切片有损。**

embedding 模型编码的是一个 chunk，chunk 是切出来的，切就会切断东西。指代消解丢了——“它”指的是谁？否定词被切断了——“以下项目不予报销”切成两半，“不予报销”在前一块，项目清单在后一块。跨段推理没了——结论在第三段，前提在第一段，你只捞回了第三段。

更根本的矛盾是：语义匹配喜欢小而精确的块，块越小向量越“纯”；上下文理解需要大而完整的块，模型得看到前后文。一个向量不可能同时满足这两个要求。Late Chunking、Anthropic 的 Contextual Retrieval，都是在给切片补上下文——补丁本身就说明伤口在哪。

大模型拿到一堆逻辑碎片怎么办？它会创造性补完。**所谓 RAG 幻觉，很大一部分不是模型在瞎编，是你喂给它的东西本来就是碎的。** agentic search 读的是整个文件，上下文是完整的，不需要事后拼。

**第二，Top-K 是一个设计缺陷，不是一个参数。**

向量召回永远返回 K 条。K 等于 5 它就给你 5 条；没有答案的时候，它也要捞回 5 条最像的垃圾。一个不会说“没有”的检索，接上一个倾向于顺着说的生成模型，幻觉是必然产物，不是意外。

当然可以补：加相似度阈值、加 reranker、训练拒答。但每补一层，“一次余弦 Top-K”就离“一次”更远一步，最后你搭出来的已经是一整套检索系统，向量只是其中一路。而 `grep` 返回空就是空。Agent 拿到空结果会换个词再搜，而不是抱着五条不相干的东西开始编。

**第三，相似不等于相关。**

你搜“哪些项目不能报销”，向量召回给你返回“报销流程说明”，因为这两句话在向量空间里离得很近——它们都在说报销。

现代 embedding 模型能编码一点否定和条件，但也只是一点。相似度给的是“长得像”，不是“逻辑上相关”。它在否定、条件、数字、错误码、产品型号、人名这些地方翻车最多，而这些恰恰是企业知识库里最常被问到的东西。搜索引擎二十年前就靠倒排索引加 PageRank 把“相关性”做到了很高的水平，RAG 把它退化回了“相似性”，然后花两年时间用 reranker 往回补。怪幽默的。

BM25 和 `grep` 对专有名词、错误码、型号是精确命中。三个病根，一条 `grep` 加一个会多翻几轮的 Agent，正好各治一条。

## 成本曲线在反向移动

再说回窗口。

今天主流模型的窗口是百万 token 级别，够装好几本《三体》。而向量 RAG 那套流水线的成本是固定的：embedding 模型要选型、要升级，升级了要把全部语料重新 embedding 一遍；索引要建、要维护；向量库要运维、要监控、要跟主库同步；切片策略要调、要评估。每一个环节都要人盯着。

有个段子。一位开发者花两周搭了一套 RAG 管线，处理一个两百页的内部文档站。做完有人提醒他：你整个语料库加起来只有十五万 token，直接塞进模型就完事了。两周的活，一个下午的事。

老冯自己也是这样。Pigsty 的全部文档加起来也就十几万 token 的量级。真要做文档问答，直接塞长上下文的效果比搭 RAG 还好——模型能看到所有交叉引用，RAG 只能看到它捞回来的那几片。当然，调用量一大，每次请求的 token 成本和首字延迟会把你推回去建索引；但在动手切片之前，先问一句“我真的需要召回吗？”这个问题两年前没人问，现在必须问。

所以准确的说法不是 RAG 死了，是 RAG 的适用区间被切成了三段：

- **语料二十万 token 以下**，几十页文档的量级：直接塞长上下文，不做检索。工程复杂度接近零，效果往往还更好。这是目前增长最快的用法。
- **二十万到几千万 token**：混合检索——BM25 加向量，加元数据过滤，加 reranker，chunk 从 512 提到 1024 甚至 2048。这已经不是 2023 年那个 RAG 了。
- **几千万 token 以上**，企业级知识库：Agentic Retrieval。不再一次性检索，让 Agent 用工具多轮逐步深入——先定位文档，再定位章节，再提取段落。检索是一个工具，不是一条流水线。

三段的分界线随模型价格和调用频率漂移，别抠数字。注意第二段和第三段里发生了什么：**活下来的 RAG，已经不是靶心是向量库的那个 RAG 了。**

## 向量成了 JSON

写到这里要刹一下车：向量不会消失，它只是退成了一个默认算子。

它的主场至少有三块：图片、音频、视频，这些东西没有字可以 `grep`，模糊检索只能靠 embedding；推荐、去重、相似匹配，找“跟这个差不多的”，向量一直是这里的标准答案；还有文本检索里的补充召回，同义词、跨语言、口语化的问法，关键字匹配不到的时候向量能兜一下。

这就是老冯 2023 年说的那句话——**向量是 AI 时代的 JSON。** 到处都用，每个数据库都得支持，但它是一种数据类型、一个算子，不是一种架构。为 JSON 单独建一个数据库这事有人干过，叫 MongoDB，后来 PG 加了个 `jsonb`。

## 顺便，专用向量数据库也快了

向量召回退居二线，专用向量数据库的存在理由跟着走了一半。另一半，它自己早就丢了。

老冯 2023 年写过一篇《[专用向量数据库凉了吗？](/db/svdb-is-dead/)》，当时的判断是两句话：向量的存储与检索是真实需求，会随 AI 发展水涨船高；但这里没有多少位置留给专用向量数据库。三年过去，一个字不用改。而且不用老冯论证，资本已经用钱投过票了：

- Databricks 2025 年 5 月收购 Neon，约 10 亿美元。公告里有个数字：Neon 上超过八成的数据库是 AI Agent 自动创建的，不是人建的。
- Snowflake 2025 年 6 月收购 Crunchy Data，约 2.5 亿美元。
- AWS 2026 年 8 月宣布收购 DuckLabs，DuckDB 背后的公司，项目本身留在基金会。
- Pinecone，2023 年以 7.5 亿美元估值融资的向量数据库旗手，据 The Information 2025 年 8 月报道正在找买家，此前丢掉了 Notion 这个大客户。

这几年真金白银的并购，买的是两家 Postgres 公司和一家 DuckDB 公司，一家专用向量库都没有。资本不是不懂 AI，资本是看明白了：**“能跑 AI 负载的 Postgres”是资产，“向量数据库”是功能。**

今天的专用向量库早就不只做余弦 Top-K 了，metadata filter、混合检索、rerank、多租户、备份，该有的都有。它们缺的不是功能，是位置。

**位置一，一个合格的向量数据库，首先得是一个合格的数据库。** 高可用、备份恢复、时间点恢复、ACID、访问控制、监控、驱动——这些东西跟向量一点关系都没有，但缺一个就上不了生产。PostgreSQL 把这些做了三十年，pgvector 是它上面一两万行代码的一个扩展。这就是 PG 不讲武德的地方：它拿一个全能数据库的合力，去打一个专用单品。

**位置二，一致性。** 这条在 benchmark 表格上一个格子都占不到，但每个管过生产库的人第一眼就会看。用独立向量库，你得从主库抽数据、转成向量、同步过去。用户在 PostgreSQL 里 `DELETE` 了一行，向量库里那条没删——你就有了一条能被检索到的幽灵记录。CDC、outbox、对账都能补，但每一样都是额外的工程，每一样都是潜在的事故点。pgvector 的模式是同库、同事务、同备份、同权限，你 `ROLLBACK` 的时候，向量跟着回来。这个能力专用向量库给不了，不是它们不想，是它跨了进程边界。

**位置三，活下来的检索需要什么。** 混合检索、元数据过滤、行级权限、版本与来源管理、多轮检索的中间状态——这全部是数据库最擅长的事。而退场的那部分，把一堆向量塞进去做一次余弦 Top-K，恰恰是专用向量库最核心的卖点。

有人会反驳：`grep` 在代码库好使，代码是结构化文本，函数名变量名本身就是关键字；企业知识库是非结构化的，`grep` 不管用。这个反驳对了一半。非结构化文本的关键字检索叫 BM25，它在专有名词、错误码、型号这些地方比向量准得多，而这恰恰是纯向量方案最容易翻车的地方。所以答案是混合检索，而混合检索需要一个能同时做 BM25、向量、元数据过滤、行级权限的系统。那个系统叫数据库，不叫向量库。

## HNSW 的税

有人会说：pgvector 性能不行啊，插入有硬伤，每写一条既要写 WAL 又要改索引图，这两件事在 PG 里是打架的。

这个说法半对。对的那一半，老冯帮大家说准；错的那一半，正好是答案。

先纠一个用词：pgvector 的 HNSW 图不在什么“内存里”，它就存在 PG 的索引页里，跟 B-tree 一模一样走 `shared_buffers` 和 WAL。这个区别重要，因为它既是问题的根源，也是答案的根源。

冲突是真的，有三条。这三条不是老冯说的，是 TensorChord 团队——pgvecto.rs 和 VectorChord 的作者——早期照 pgvector 的路子在 PG 页存储上做 HNSW 时实测出来、公开写在文档里的：

**第一，WAL 放大。** 插入一个 2 KB 的向量，产生 20 KB 以上的 WAL，十倍上下。HNSW 插入一个点要修改多条边，每一次变更都要记日志。

**第二，锁竞争。** HNSW 是分层的，层越高点越少，顶层那几个点是每一次插入和每一次查询的必经之路，在结构上就是全局热点。这解释了一个反直觉的现象：pgvector 的插入不是“慢”，而是并发一上来就扩展不动。

**第三，并行化。** PG 一条语句一个进程，缺线程安全的 API，他们想并行化索引构建，撞上 `Too many shared buffer locked`。这条 pgvector 0.6 之后自己翻过去了大半，现在支持并行构建。

三条里最关键的是第一条的定性：HNSW 插入要改多条边，写放大是这个算法固有的。任何人用任何存储引擎，只要想做一个崩溃之后不丢数据的 HNSW，就得付这笔钱。具体几倍看实现，但账单是 HNSW 开的，不是 PG 开的。

而且这件事不用推理，有人把实验完整做完了。TensorChord 走了三步：

**第一步**，照 pgvector 的路子在 PG 页存储上做 HNSW，撞墙。

**第二步**，做 pgvecto.rs，把索引的存储和内存整个搬出 PostgreSQL，架构参考 FreshDiskANN，本质是 LSM：新向量先写 writing segment，后台异步转成不可变的 growing segment，再跟 sealed segment 合并。收益三条：插入不被索引修改阻塞，批量修改提升吞吐，不可变段没有读写锁竞争。看起来赢麻了。

但代价写在他们自己文档的对比表里：WAL 支持这一行，`data` 是有，`index` 是 `working in progress`。翻译成 DBA 听得懂的话：把索引搬出 PG 的存储引擎，就同时失去了这个索引的时间点恢复和物理复制。主库挂了切到从库，向量索引是什么状态？老板说恢复到昨天下午三点，数据能回去，索引回不去。

**第三步**，做 VectorChord，回到 PG 的页存储，但把索引结构换掉——IVF 加 RaBitQ，不用 HNSW 了。IVF 是倒排列表：向量归到最近的聚类中心，插入就是往一个 posting list 上 append，改一个页，没有双向边，没有级联修复，没有全局热点。代价挪到读侧——查询要扫多个列表——再用 RaBitQ 把向量压到几个比特，让扫描变得极便宜，最后用全精度重排把精度捞回来。**VectorChord 不是优化了 HNSW，它是换了一个天生对写友好的结构，再用量化把读的代价压回去。**

官方数字：相比 pgvector 的 HNSW，查询最多快 5 倍，插入吞吐最多高 16 倍；一亿条 768 维向量，32 GB 内存，P50 延迟 35 毫秒，召回 95%。厂商口径，大家打个折听。

三步走的结论是：**问题不在 PG 的存储引擎——绕开存储引擎那条路他们走过了，代价是丢掉 PITR 和物理复制；最后的解法是换索引结构，不是换存储引擎。**

顺便，Milvus、Qdrant 那些漂亮的写入吞吐是怎么来的？Milvus 的 growing/sealed segment，Qdrant 的 mutable/immutable segment，跟 pgvecto.rs 当年是同一条路——写进去先攒着，索引回头异步建。那个吞吐衡量的是“数据落到 growing segment 的速度”，不是“数据能被索引检索到的速度”。中间那段窗口期，新数据靠暴力扫描被搜到，或者按一致性配置干脆搜不到。

**这是两个不同的语义，被放进了同一张表格里比较。** PG 里 `INSERT` 返回的那一刻，这条向量就在索引里，而且在事务里。这个保证是要花钱买的，WAL 就是它的标价。你可以说这价格太贵、我的场景不需要——但你不能假装另一边没付这笔钱。他们只是把账记到了别的地方：记到了 PITR 上，记到了物理复制上，记到了“写完查不到”的那个窗口期上。

## 为什么向量索引不进内核

还有个流传很广的说法：PG 18 把向量索引放进内核了。

没有。PG 18 去年九月 GA，现在跑到 18.6；PG 19 现在是 Beta 3，马上 GA，新东西是属性图查询 SQL/PGQ、`REPACK`、`pg_plan_advice`，里面没有一个字是向量。pgvector 今年 7 月发的 0.8.6 依然是个扩展。

而且不是还没排上。2025 年 3 月有人在 pgsql-general 邮件列表上问，能不能把 `vector`、`halfvec` 做成像 `jsonb` 那样的原生类型。社区老炮 Christophe Pettus 回了一封：不要指望这个功能在未来五年内进核心。理由三条：

一，你列了三个功能重叠的扩展，这本身就说明社区对内核里该放什么没有共识。

二，往内核加一个类型是永久的维护负担。**类型一旦进核心几乎撤不出来**——去翻归档里关于 `money` 类型的讨论，看看一个进了核心又没人维护的类型是什么下场。而 `money` 的复杂度跟向量根本不是一个量级。

三，PostgreSQL 的设计就是要有一个繁荣的扩展生态。这种功能能用扩展做，恰恰是 PG 区别于其他数据库的地方。

这是他的个人意见，PG 也没有一个能对五年后做承诺的委员会。但这就是社区的态度。

把第二条放到今天看：如果 2023 年社区脑子一热，把当时最火的那版 HNSW 塞进内核，今天 PG 背的就是一个 2023 年的实现，永远撤不掉。而实际发生的是，这三年向量索引的路线一条变三条——HNSW、DiskANN、IVF 加 RaBitQ——各有取舍地并存，**PG 内核一行代码都没为它们改过。**

那为什么 PG 19 能把属性图查询放进内核？因为 SQL/PGQ 是 ISO SQL 标准的一部分，向量不是。**标准化的东西进内核，时髦的东西进扩展。** 这不是一次判断，这是一条纪律。正因为有这条纪律，PG 才敢让扩展生态野蛮生长——内核不会被生态绑架。

向量索引是一个索引类型，不是一个产品品类。索引类型应该长在数据库里，而不是反过来长一个数据库出来。

## 真正该问的问题

回到手卡上那一问，“PG 在 RAG 架构里扮演什么角色”。老冯的回答是：这个问题该换成——**Agent 需要数据库提供什么。**

有个流行说法，“数据库是 AI 的海马体”。这个比喻不对。海马体负责的是记忆的编码和取回，记忆本身分布在皮层各处。说数据库是海马体，等于说数据库只是个查询引擎，太窄了。

更准确的说法：数据库是 Agent 的状态平面，是它的外存。用操作系统的内存层次来类比——上下文窗口是 RAM，向量索引和全文索引里的热数据是 Swap，PostgreSQL 全量是硬盘。

PG 手里有几张被严重低估的牌，专用向量库一张都没有：

- **`LISTEN/NOTIFY`**：Agent 之间的信号总线。
- **`SELECT ... FOR UPDATE SKIP LOCKED`**：现成的任务队列，中小规模够用，不用为一个队列引一套 Kafka。
- **PITR 加 PG 18 的 CoW 克隆**：要回到昨天下午三点，靠 WAL 归档和时间点恢复；要给 Agent 开个分支做实验，PG 18 的 `file_copy_method = clone` 在支持 reflink 的文件系统上毫秒级复制一整个库。一个回到过去，一个复制当下。
- **ACID**：多个 Agent 并发写同一份状态的时候，事务是最省心的共享状态层。

Neon 那个数字值得再看一眼：八成的库是 Agent 自己建的。Agent 需要的不是一个向量索引，是一个能开事务、能回滚、能分支、能审计的东西——那个东西叫数据库。

市面上标榜“AI Native”“Agent Native”的数据库，大多数还停留在概念营销阶段。你问他们什么叫 Agent Native，很难得到一个技术上站得住的回答，好像加了向量支持就算了——跟当年“Cloud Native Database”的定义一样模糊。如果真要定义，老冯认为该分两层：核心需求是持久化状态、事务边界、能力授权、血缘审计；扩展需求才是向量、全文、图。市面上的项目大多在解决第二层，而第二层恰恰是 PG 白送的那一层。

**没有身体的灵魂是幽灵，没有数据库的 Agent 是聊天机器人。**

## 结语

向量 RAG 是上下文窗口只有 4K 的时代被逼出来的应急方案。三年过去，那个约束消失了，架构还留在原地；RAG 这个词还活着，向量召回退成了一个默认算子，而很多人还在为一个已经不存在的约束付账。

十年前我们问要不要上 NoSQL，五年前问要不要上云原生数据库，两年前问要不要上向量数据库，今天问要不要上 AI 原生数据库。

这四个问题的答案碰巧是同一个：**先把 Postgres 用明白。**

---

## 参考资料

- 老冯，《[专用向量数据库凉了吗？](/db/svdb-is-dead/)》，2023 年 11 月。
- 老冯，《[AI 时代，PostgreSQL 凭什么赢了？](/ai/postgres-and-ai/)》，2026 年 4 月。
- Lewis et al.，[《Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks》](https://ai.meta.com/research/publications/retrieval-augmented-generation-for-knowledge-intensive-nlp-tasks/)，2020 年。
- Douwe Kiela，[《RAG is dead, long live RAG!》](https://contextual.ai/blog/is-rag-dead-yet)，Contextual AI Blog，2025 年。
- Richard MacManus，[《RAG isn't dead, but context engineering is the new hotness》](https://thenewstack.io/rag-isnt-dead-but-context-engineering-is-the-new-hotness/)，The New Stack，2026 年 1 月，Douwe Kiela 访谈。
- Latent Space 播客，[《Claude Code: Anthropic's Agent in Your Terminal》](https://www.latent.space/p/claude-code)，2025 年 5 月；Boris Cherny 在 X 上的补充说明，2026 年 2 月。
- Anthropic，[《Effective context engineering for AI agents》](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)，2025 年 9 月；[《Introducing Contextual Retrieval》](https://www.anthropic.com/engineering/contextual-retrieval)，2024 年 9 月。
- Jin et al.，[《Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning》](https://arxiv.org/abs/2503.09516)，2025 年。
- TensorChord，[pgvecto.rs 与 pgvector 对比文档](https://github.com/tensorchord/pgvecto.rs#comparison-with-pgvector)；[VectorChord 官方基准测试](https://blog.vectorchord.ai/vectorchord-store-400k-vectors-for-1-in-postgresql)。
- [Databricks 收购 Neon 公告](https://www.prnewswire.com/news-releases/databricks-agrees-to-acquire-neon-to-deliver-serverless-postgres-for-developers--ai-agents-302454992.html)，2025 年 5 月；[TechCrunch 关于 Snowflake 收购 Crunchy Data 的报道](https://techcrunch.com/2025/06/06/startups-weekly-its-buying-season/)，2025 年 6 月；[Amazon 收购 DuckLabs 公告](https://www.aboutamazon.com/news/company-news/aws-ducklabs)，2026 年 8 月 26 日。
- The Information，[《Top-Funded AI Database Startup Pinecone Considers a Sale》](https://www.theinformation.com/articles/top-funded-ai-database-startup-pinecone-considers-sale)，2025 年 8 月。
- pgsql-general 邮件列表，[《pgvector as standard PostgreSQL feature?》](https://www.postgresql.org/message-id/DBAP191MB12893E8288EBE762637FA86CB0D92%40DBAP191MB1289.EURP191.PROD.OUTLOOK.COM)，2025 年 3 月，Christophe Pettus 回复。
- PostgreSQL Global Development Group，[PostgreSQL 19 Beta 3 发布公告](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/)与[发布说明](https://www.postgresql.org/docs/release/19.0/)，2026 年 8 月。
