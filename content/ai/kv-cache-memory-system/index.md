---
title: "从 KV Cache 到 AI 内存系统：大模型推理架构的演进"
date: 2026-03-23
authors: [xieydd]
summary: >
  摘要 这篇文章想回答一个看似分散、其实高度统一的问题：为什么这两年围绕大模型推理的系统创新，越来越不像是在“优化一个神经网络”，反而像是在“设计一个内存系统”？
tags: [大模型, AI, 架构]
---

> 原作者：xieydd · [微信公众号转载页](https://mp.weixin.qq.com/s/cagTlPJF13JZybqPXyacSw)

> **摘要**\
> 这篇文章想回答一个看似分散、其实高度统一的问题：为什么这两年围绕大模型推理的系统创新，越来越不像是在“优化一个神经网络”，反而像是在“设计一个内存系统”？\
> \
> 如果把 2023 年以前的大模型工程叙事概括成“拼 FLOPS、拼 Tensor Core、拼训练吞吐”，那么 2024–2026 年的推理叙事，已经明显转向了另一条主线：`KV cache`、`TTFT/TPOT`、`continuous batching`、`prefix reuse`、`prefill/decode disaggregation`、`hierarchical cache`、`CXL memory pool`。

这不是偶然。Transformer 的自回归推理天然会把“历史”变成一块不断增长、必须反复访问的状态；而 RLHF/RLVR、reasoning、agent workflow、长上下文和多轮交互，又把这块状态推到了系统设计的正中央。OpenRLHF 甚至直接指出，在 PPO 风格的 RLHF/RLVR 里，**inference 阶段经常占到总运行时间的 90% 以上**；同一时期，Mooncake、LMCache、Strata、KVFlow、Beluga、TraCT 这类系统则在从不同层面把 KV cache 提升为“一等公民”。1

站在今天回看，真正的变化不是“某个 kernel 更快了”，而是**推理系统的重心，正在从计算图转向内存图**。本文会沿着这条线，把 Mac/Uma、NVIDIA/NVLink、FlashAttention、vLLM、RL rollout、Mooncake、LMCache、CXL，以及 2025–2026 的新论文串成一条完整主线。2

------------------------------------------------------------------------

### 目录

- 1. 大模型推理的本质：Prefill vs Decoding
- 2. KV Cache：Transformer 推理的真正状态变量
- 3. 为什么瓶颈会从 compute 转向 memory
- 4. RL / Agent：为什么后训练把问题推向 decoding
- 5. 为什么 Mac / UMA 会重新变重要
- 6. 为什么 FlashAttention 救不了 decoding
- 7. 推理优化的四层结构：kernel、engine、model、hardware
- 8. Continuous Batching：从“请求级”到“token 级”调度
- 9. 模型结构如何直接决定系统上限：MQA / GQA
- 10. KV Cache 其实是一种高度冗余的外部记忆
- 11. 为什么很多线上系统仍然在“重复计算历史”
- 12. 第一代 KV-centric 架构：DistServe、Mooncake、LMCache
- 13. 为什么 Mooncake / LMCache 不是终点
- 14. 新一代 Memory-centric 架构：Strata、CAKE、R-KV、KVFlow、FastSwitch、CacheBlend
- 15. CXL：看起来像终极答案，为什么现实里还很难
- 16. LLM serving 正在变成一个“操作系统问题”
- 17. KV cache 之后是什么：Mamba、RWKV 与“在线压缩记忆”
- 18. 结语：三条真正的主线

------------------------------------------------------------------------

### 1. 大模型推理的本质：Prefill vs Decoding

现代主流 LLM，大多沿着 GPT 这条 **causal decoder-only Transformer** 路线发展：输入是“到目前为止的上下文”，输出是“下一个 token 的概率分布”。这与 BERT 这种**bidirectional encoder** 路线的根本区别在于：GPT 类模型天然支持逐 token 自回归生成，而 BERT 的预训练目标是 masked language modeling，本质上依赖左右文共同参与表示计算。换句话说，**KV cache 只对 causal decoder 天然成立**，对 BERT 这种双向编码器并不是一等机制。3

一旦把推理过程按执行阶段拆开，你会发现 LLM serving 其实不是一个统一的工作负载，而是两个物理性质很不一样的阶段叠在一起。

第一阶段是 **prefill**。它读取整段输入 prompt，对所有输入 token 做一次前向传播，并为每一层生成后续要复用的 K/V 状态。这个阶段的并行度高、矩阵乘比例大、GPU Tensor Core 能用得很满，所以更接近我们熟悉的“训练前向”形态。Sarathi-Serve 和 DistServe 都明确把 prefill 视为高延迟、但能显著吃满 GPU 计算资源的阶段。4

第二阶段是 **decoding**。模型每次只生成一个 token，然后把这个 token 追加到历史，再生成下一个 token。这个阶段每一步的算子规模不大，GPU 不容易被纯算力吃满；真正贵的是：**你必须把历史 KV cache 读回来参加注意力计算**。Sarathi-Serve 直接指出，decode iteration 虽然单次延迟低，但计算利用率也低，因此系统必须依赖 batching 才能把吞吐做起来。4

这就是理解后面所有系统工作的第一把钥匙：\
**prefill 更像 compute-bound，decode 更像 memory-bound。**\
当然，这不是绝对的，而是 workload-dependent。文档摘要、RAG、大段代码分析等长输入场景，prefill 会非常重；实时聊天、长输出推理、RL rollout、agent 多轮执行，则会让 decode 和 KV cache 问题变得更突出。DistServe 在实际实验中就专门区分了 chatbot、programming assistant、document summary 这类不同 workload，并强调 TTFT 与 TPOT 目标并不相同。5

所以，后面凡是看到有人说“LLM 推理是算力问题”或“LLM 推理是内存问题”，你都应该先追问一句：**你说的是 prefill 还是 decode？你说的是哪类 workload？**

------------------------------------------------------------------------

### 2. KV Cache：Transformer 推理的真正状态变量

如果只从算法式子看，自注意力似乎只是\
`Attention(Q, K, V) = softmax(QK^T)V`。\
但在推理系统里，这个式子最重要的副产品不是输出，而是**历史状态如何被保存**。

在 causal decoder 中，每来一个新 token，模型都会在每一层计算该 token 对应的 `K` 和 `V`，并把它们保存下来；之后生成新 token 时，当前 token 的 `Q` 只需要去和**全部历史的 K/V**交互即可。于是，KV cache 实际上存的是：**每一层、每个历史 token 的 Key 和 Value 表示**。它不存 `Q`，因为 `Q` 只属于“当前这一拍”；它也不存完整的 attention 矩阵，因为后者随当前 `Q` 的变化而变化，而且体量更大。这个机制依赖 causal mask：历史不会被未来改写，所以过去 token 的 K/V 可以安全复用。6

这件事在系统层面的意义非常大。\
如果没有 KV cache，那么第 `t` 步生成时，你需要重新对前 `t-1` 个 token 做前向计算，相当于重复计算整个历史；有了 KV cache 之后，你只需要对**新 token**做一次增量前向，但仍然要把历史 K/V 读出来参加注意力。于是，问题从“反复重算历史”变成了“反复读取历史”。Shazeer 在 Multi-Query Attention 论文里对这一点说得非常直接：**incremental decoding 慢，核心是反复加载巨大的 K/V 张量所带来的 memory-bandwidth cost。**7

也因此，KV cache 不是某个实现细节，而是 Transformer 自回归推理的**真正状态变量**。对于一个有 `L` 层、`H_kv` 个 KV 头、每头维度 `d`、上下文长度 `T`、batch 为 `B` 的模型，KV cache 的规模大致按\
`O(L * H_kv * d * T * B)`\
增长。你一旦把 `T` 拉长，把 `B` 拉高，或者让一次请求分裂成多条 trajectory，这块状态就会迅速膨胀。CAKE、R-KV、FlexiCache 这类 2025 年的论文，本质上都是在承认并处理这一事实：**KV cache 本身已经大到必须被压缩、分层、淘汰和预测。**8

这里还有一个经常被忽略的差别：模型参数 `weights` 是**共享且静态**的，而 KV cache 是**按请求增长且互不共享**。前者是“把知识装进模型里”；后者更像“把每次推理的思考过程存起来”。这会直接导致一个系统级分水岭：同样是显存/内存占用，**weights 的成本更偏容量，而 KV 的成本更偏容量 + 带宽 + 延迟**。这也是为什么我后面会说，未来很多场景里，KV cache 的压缩价值可能比参数压缩更大。9

------------------------------------------------------------------------

### 3. 为什么瓶颈会从 compute 转向 memory

很多关于 LLM 推理的争论，实际上都输在“把 workload 混为一谈”上。\
更精确的说法不是“推理越来越偏向 decode”，而是：

> **只要工作负载在走向多轮、长历史、长输出、长 CoT、可复用上下文，系统瓶颈就会从 prefill 的计算，逐渐转向 decode 阶段对 KV cache 的访问。**

这和“prompt 到底变长还是变短”不是一回事。

先看最容易理解的聊天场景。如果用户输入短、系统提示稳定，而输出较长，那么 prefill 只做一次，decode 却要重复几十上百次；这时 decode 的累计成本很容易压过 prefill。Sarathi-Serve、DistServe 和 OpenRLHF 都是在这种“prefill 与 decode 特性完全不同”的观察上做系统设计的。4

但这并不意味着所有工作负载都如此。\
在 RAG、长文总结、代码仓分析等任务里，输入可能有几千到几十万 token，输出却很短；这类 workload 的第一个大问题是 TTFT，因为模型必须先把长输入完整 prefill 完。LinkedIn 那篇关于 prefix reuse 调度的理论论文就明确把“long-prompt, short-output”视为一个 prefill-dominant 区间，并指出在这种场景下，prefix reuse 对 TTFT 非常关键。10

真正有意思的是 **agent / reasoning / RL rollout**。\
这些场景里，逻辑上的“上下文”确实在变长：模型思考、调用工具、读回工具输出、再继续思考，历史不断追加。但如果系统能有效复用 KV cache，那么增长的不是“每轮重新 prefill 的计算量”，而是“需要继续维护和读取的历史状态量”。也就是说，**长 history 并不自动等于更重的 prefill；它可能意味着更大的 KV cache、更高的 decode memory pressure。** OpenRLHF 明确把 long CoT 视为训练效率的关键瓶颈，并把 vLLM 接入 rollout engine 来缓解长推理链带来的推理负担。R-KV 更进一步，直接把 reasoning model 的“超长输出导致 KV cache 爆炸”作为问题出发点。1

这也是为什么我会说：\
**“长 prompt”和“长 history”不是同一件事。**

- 长 prompt，如果每次都要重新喂进去，是 prefill 问题。
- 长 history，如果以 KV cache 形式被保留下来，是 decode / memory 问题。

现代 API 和 serving system 的大量创新，恰恰都是围绕这个区别展开的：prompt caching、prefix reuse、PD disaggregation、hierarchical cache，本质上都在努力把“重复计算的长 prompt”转换成“可复用的长 history”。11

------------------------------------------------------------------------

### 4. RL / Agent：为什么后训练把问题推向 decoding

如果只看 SFT 时代，训练的主角还是标准的 forward/backward：数据集给定，模型吃进去，算损失、回传梯度。那是典型的“训练是核心、推理只是辅助”的时代。

但后训练，尤其是 RLHF、RLVR、reasoning-oriented RL、agentic RL，不再是这样。\
今天的一个典型 PPO/GRPO 风格循环更像：

1.  1\. 给 prompt；
2.  2\. 模型 rollout 出一条或多条答案/轨迹；
3.  3\. 奖励模型、验证器、工具执行器或环境给反馈；
4.  4\. 再基于这些 rollout 更新参数。

在这个 pipeline 里，**训练并不是直接对固定样本做优化，而是先生成样本，再训练**。于是系统重心自然向 rollout 倾斜。OpenRLHF 的论文给了一个非常重的判断：在 PPO 风格 RLHF/RLVR 中，**inference phase often accounts for over 90% of total runtime**，因为模型要在每个 inference step 里生成成千上万个 token。1**RLVR (Reinforcement Learning from Value Reflection)** 作为新一代 agentic RL 方法，进一步放大了这个问题：它需要模型在 rollout 过程中不断反思、修正自己的轨迹，导致轨迹长度通常比普通 RLHF 更长，KV cache 需要保留的状态也更大。最近的工程经验指出，在 terminal environment 这类复杂 agent 场景中，rollout 轨迹长度很容易达到数千 token，而且每个 policy update 需要采样多条轨迹，KV cache 的内存压力会比传统推理场景高出一个数量级。40

一旦接受这点，很多原本看似奇怪的系统设计就变得顺理成章了。\
ECHO-2 直接提出把 centralized learning 和 distributed rollout inference 分开，让 rollout 生成从数据中心 GPU 集群外溢出去；AgentRL 提出 fully-asynchronous generation-training pipeline，用来支撑多轮、多任务 agent RL；OpenRLHF 则把 rollout engine 和 actor/training engine 显式拆开，并强调异步数据流对长 CoT 时代尤其重要。12

为什么 rollout 会特别“难”？因为它同时具备几个糟糕特征：

第一，它是 **decode-heavy** 的。\
不是一次性吞掉一段输入，而是 token-by-token 往前走。1

第二，它的长度高度不规则。\
同一批 prompt，有的几步就完成，有的会展开很长的 chain-of-thought；在 agent setting 里，不同工具调用还会导致轨迹长度进一步分叉。AgentRL 和 OpenRLHF 都把 asynchronous pipeline 当成必要设计，而不是锦上添花。13

第三，它天然会放大 KV cache。\
如果一个 prompt 不只采样 1 条输出，而是采样 `k` 条 trajectory；如果每条 trajectory 还会持续增长；如果中间还要保留 verifier、tool use、multi-turn state，那么系统不只是多了 `k` 次计算，而是多了 `k` 份不断膨胀的历史状态。R-KV 把 reasoning output 的冗长性视为核心问题，正是因为 reasoning model 的“输出长度”已经直接映射到 KV cache 成本。9

我之前提出的一个猜想——“后训练需要 Mac，可能是因为 rollout 时间比 train 时间更多”——方向是对的，但更准确的说法应该是：

> **不是简单因为 rollout 更久，而是因为 rollout 把问题从 backward-dominated 变成了 decode/KV-dominated.**

这也是为什么越来越多 post-training 框架会把 vLLM、SGLang 这类 serving engine 嵌进训练框架：OpenRLHF 明确把 vLLM 当作长 CoT RLHF/RLVR 的关键基础设施；其论点不是“生成顺便用一下推理引擎”，而是“推理本身已经是训练效率的核心瓶颈”。1

------------------------------------------------------------------------

### 5. 为什么 Mac / UMA 会重新变重要

很多人谈 Mac 跑大模型，容易把它误解成“Apple GPU 能和 NVIDIA 拼训练吞吐”。这基本不是重点。\
Mac 重新变重要，核心不是因为它在纯算力上赢了，而是因为它在**内存系统组织方式**上走了另一条路。

Apple 在官方材料里反复强调 unified memory architecture：M3 家族的描述是“单一内存池，芯片里所有技术都能访问同一份数据而无需在多个内存池之间拷贝”；M2 Ultra 则明确给出 **800GB/s system memory bandwidth**，并支持**192GB unified memory**；到 2025 年的 M3 Ultra，Apple 进一步给到**最高 512GB unified memory** 和**超过 800GB/s 的内存带宽**；而到了 2026 年 3 月，M5 Max 官方规格已经达到**614GB/s unified memory bandwidth**。Apple 自己甚至把“直接在设备内存里运行超大 LLM”当成 Mac Studio 的 AI 卖点之一。14

这对 LLM 推理意味着什么？\
不是“Mac 的 GPU 比 H100 快”，而是：

1.  1. **模型权重、KV cache、CPU-side orchestration 可以共享同一大内存池；**
2.  2. **很多 CPU/GPU 协作场景不再需要显式拷贝；**
3.  3. **只要容量够，单机可以把更大的 working set 放在一个统一地址空间里。**

Apple 对 MLX 的描述也很直接：MLX 利用 Apple silicon 的 unified memory architecture，CPU 和 GPU 之间运行操作时**不需要来回搬数据**。15

这正好击中 decode-heavy / rollout-heavy 工作负载的软肋。\
因为 decode 的难点本来就不是做一个巨大的 GEMM，而是**如何低成本地读取和维护一大块历史状态**。如果你的模型、KV cache、tool runtime 和 CPU/GPU orchestration 共享一个大内存池，那么系统层的“摩擦损耗”会明显小很多。Apple 的表述一直围绕高带宽、低延迟、单池共享，而不是独立显存 + PCIe copy。14

但这并不等于“Mac 全面优于 NVIDIA”。\
NVIDIA 仍然在 prefill、训练和高并发 serving 上拥有压倒性生态与算力优势。H100 级别产品的 HBM 带宽已经达到 **3TB/s** 量级，而 Grace Hopper GH200 还通过**NVLink-C2C 的 900GB/s coherent interface** 提供 CPU+GPU coherent memory model。NVIDIA 自己的官方说法就是：GH200 通过 NVLink-C2C 提供硬件级 memory coherency。16

换句话说，NVIDIA 并不是没看到 Apple 这条路，而是在沿着另一条更可扩展的路径逼近它：\
从传统的“离散 GPU + PCIe”，到“NVLink 互联”，再到“Grace Hopper coherent memory model”，再到今天围绕 CXL、shared memory pool、PD disaggregation 的一系列论文。Apple 的意义更像是：**它让很多人第一次真正感受到，统一内存不是移动设备卖点，而是 LLM 推理的结构性优势。**17

所以，如果你问“为什么后训练也有人要 Mac”，我会给出一个更谨慎的判断：

> **在 cluster-scale post-training 上，NVIDIA 仍然是主角；但在本地实验、低并发 rollout、长上下文推理、agent 原型、长 CoT 调试这类 memory-centric 场景里，Mac 的 UMA 确实切中了关键痛点。**

这不是“Mac 比 NVIDIA 更强”，而是“**当 workload 从 FLOPS 转向 working set 时，内存架构开始决定体验**”。18

------------------------------------------------------------------------

### 6. 为什么 FlashAttention 救不了 decoding

FlashAttention 是过去几年最重要的 attention kernel 创新之一，但它经常被误用为“attention 已经优化完了”的证据。实际上，FlashAttention 解决的是**prefill 的一个核心痛点**，而不是 decode 的根问题。

FlashAttention 的原论文把问题表述得非常明确：标准 attention 的关键瓶颈不是理论 FLOPS，而是 **HBM 与片上 SRAM 之间的 IO**。它通过 tiling 方式避免 materialize 巨大的中间 attention 矩阵，从而显著减少 HBM 读写。这个优化对长序列 prefill 非常有效，因为 prefill 阶段会面对大规模的 `N x N` 注意力结构。19

但 decode 完全不是这个形态。\
在 decoding 的第 `t` 步，当前只有一个新 token，因此 `Q` 的序列长度几乎是 1，而 `K/V` 的长度是历史长度 `t-1`。这时 attention 更像一个 `1 x N` 的查询过程，而不是一个要显式构造 `N x N` 中间矩阵的过程。换句话说，decode 的问题不是“中间 attention matrix 太大”，而是“**历史 K/V 必须被完整读一遍**”。Shazeer 的 MQA 论文把 incremental decoding 的瓶颈直接归因于 repeated loading of large keys and values tensors。19

这就是为什么你会看到一个非常反直觉的结论：

- FlashAttention 对 prefill 常常非常关键；
- 但对 decode，它更多是在**局部 kernel 效率**上锦上添花，而不是改变瓶颈。

因为 decode 真正无法绕开的，是 `O(N)` 的 KV read。你可以减少 kernel overhead，可以更好地融合一些计算，但只要模型还是标准 causal attention，历史状态就必须被访问。Sarathi-Serve 之所以强调 batching、chunked-prefill 和 stall-free schedule，而不是把希望完全押在 attention kernel 上，背后就是这个现实：**decode 的系统瓶颈不再是单个算子本身。**4

在 2026 年 3 月 5 日，FlashAttention-4 进一步优化了异构计算和片上内存管理，在长序列 prefill 上继续获得显著提升，但核心观察仍然成立：对 incremental decoding 而言，瓶颈的本质仍然是对历史 KV 的反复读取，而非 kernel 内的计算调度。即使 kernel 效率再优化一个量级，只要你需要每一步都读完整历史，memory 带宽仍然会是核心约束。

这也是理解后面所有系统设计的第二把钥匙：\
**当瓶颈是“必须读历史”时，优化方向就会从 kernel 下沉到 memory layout、cache reuse、调度和体系结构。**

------------------------------------------------------------------------

### 7. 推理优化的四层结构：kernel、engine、model、hardware

为了不把各种技术混成一锅，我更喜欢把 LLM 推理优化分成四层：

#### 第一层：kernel 层

典型代表就是 FlashAttention。\
它关心的是：**单个 attention / decode kernel 如何更少搬 HBM、更多留在片上 SRAM，如何更高效地执行**。这层很重要，但它只回答“这一步怎么算更快”。19

#### 第二层：engine 层

典型代表是 Orca、vLLM、SGLang、Sarathi-Serve。\
这层关心的是：**请求如何被动态调度、KV cache 如何被分页/复用、prefill 与 decode 如何协同、如何提高 GPU 利用率与 goodput**。Orca 把 request-level scheduling 改成 iteration-level scheduling；vLLM 用 PagedAttention 解决 KV 内存碎片；SGLang 用 RadixAttention 做前缀复用；Sarathi-Serve 通过 chunked-prefill 平衡吞吐与延迟。20

#### 第三层：model 层

典型代表是 MQA / GQA、以及更激进的 Mamba / RWKV 方向。\
这层关心的是：**如果 decode 慢是因为要读太多 K/V，那能不能让 K/V 变少，甚至不用 K/V？** MQA 直接共享 K/V；GQA 折中共享；Mamba/RWKV 则试图把历史压成递归状态。7

#### 第四层：hardware 层

典型代表是 Apple UMA、Grace Hopper coherent memory、CXL memory pool。\
这层关心的是：**既然历史必须读，那能不能让“读”这件事更像访问本地内存，而不是频繁跨总线搬数据？** Apple 走 unified memory；NVIDIA 用 GH200 把 coherent memory 带进 CPU+GPU；Beluga、TraCT、CXL-SpecKV 则尝试把更大的共享内存池引入集群级推理。14

如果只盯着第一层，你会觉得问题是“attention 还不够快”。\
如果看到第二层，你会意识到问题是“GPU 经常在等、不够满”。\
如果看到第三层，你会发现“模型本身就在决定系统带宽压力”。\
如果再看到第四层，你就会明白：**今天很多所谓 AI infra 的创新，本质已经不是神经网络论文，而是 memory system 论文。**

------------------------------------------------------------------------

### 8. Continuous Batching：从“请求级”到“token 级”调度

LLM serving 的一个基本矛盾是：decode 每一步的计算量很小，不 batch 很容易吃不满 GPU；但一旦 batch，序列长度和完成时间又高度不一致，传统 static batching 会制造大量浪费。

Orca 是这条线的源头之一。它提出 **iteration-level scheduling**：系统不是把一批请求整体跑完再换下一批，而是以“迭代”为单位调度，每次只让引擎执行单次迭代，然后马上允许新请求进入、已完成请求退出。Orca 论文把这件事的收益说得很清楚：对于 Transformer-based generative models，这种按 iteration 调度的方式显著优于传统 request-granularity serving。20

vLLm 把这条思路进一步工程化。\
其 PagedAttention 论文的出发点是：KV cache 又大又动态增长，传统连续分配方式既浪费显存又难以高吞吐 serving。PagedAttention 把 KV cache 管成类似操作系统分页的形式，以支撑更灵活的请求装配和内存复用。21

一旦 KV cache 能被分页管理，**continuous batching** 才真正成立。\
它的核心不是“一次多攒几个请求”，而是：**每个 decode step 都重新组 batch**。谁结束了就退出，谁新到就尽快插入；batch 生命周期从“一个请求的完整生成期”缩短为“一个 token step”。这和静态 batching 的本质区别，不在于 batch 更大，而在于 batch 的重组粒度更细。Orca 的迭代级调度、vLLM 的 continuous batching、TensorRT-LLM 的 in-flight batching，本质都在做这件事。20

为什么它能把 GPU 利用率显著拉高？\
因为 decode 阶段单个请求的计算太小，必须把多个请求的“下一 token”拼在一起算，才能提高张量并行度；而静态 batching 会被最长请求拖住，短请求完成后留下的“空座位”无法立刻补入。continuous batching 把等待最长请求的串行模式，改造成了 token-level 的流水线模式。Sarathi-Serve 进一步指出，decode batching 对 overall throughput 特别有效，但 prefill 与 decode 混排又会制造 stall，因此需要 chunked-prefill 来减轻这种互扰。4

当然，continuous batching 也不是“batch 越大越好”。\
Revisiting SLO and Goodput Metrics in LLM Serving、DistServe、以及一系列后续工作都提醒我们：在线 serving 的目标不是单纯最大吞吐，而是满足 TTFT / TPOT / 尾延迟等 SLO 的 **goodput**。batch 太大，虽然吞吐可能继续升一点，但 TPOT、P99 latency 可能恶化，最终 goodput 反而下降。22

所以，continuous batching 的真正目标不是“无限放大 batch”，而是：

> **在给定的 KV 带宽、尾延迟和 SLO 约束下，让 GPU 在每个时间片都尽可能做有价值的 token 计算。**

这已经非常像操作系统里的在线调度问题，而不再像经典深度学习里的“固定 batch 训练”。

------------------------------------------------------------------------

### 9. 模型结构如何直接决定系统上限：MQA / GQA

如果你理解了 decode 的核心成本是“不断读历史 K/V”，那 MQA / GQA 的意义就会变得非常清楚。

Shazeer 在 2019 年提出 MQA 时，问题定义几乎就是现在整个行业的共同语言：incremental decoding 之所以慢，是因为 repeated loading of large keys and values tensors 带来了 memory-bandwidth cost。MQA 的解法简单粗暴：**让所有 query heads 共享同一组 K/V heads**。这样做并不会减少 query head 数量，但会显著减少 K/V 的尺寸，从而降低 decode 的带宽压力。7

GQA 则是这条路线的工程折中。\
Google 的 GQA 论文明确指出：MQA 推理很快，但质量可能下降；于是他们提出 grouped-query attention，在“每头独立 K/V”和“全头共享 K/V”之间取一个中间点。论文结论也很清楚：**uptrained GQA 的质量接近 MHA，而速度接近 MQA。**23

这件事的重要性，在系统层面远超“注意力机制换了个变体”。\
因为当你减少 `H_kv` 的时候，减少的不只是 KV cache 占用，还减少了**每一步 decode 必须读回来的数据量**。换句话说：

- MHA 把系统拖向 memory wall；
- MQA/GQA 在主动降低单请求的 memory footprint；
- 这会直接推高可实现的 optimal batch size，并改善 TTOT/throughput 曲线。

这正是“模型设计开始服务系统效率”的典型例子。它不是单纯为了学术上更优雅，而是在用结构设计换系统带宽。7

从这个角度看，很多人把“模型架构”和“系统优化”分成两个世界，其实已经不太成立了。\
GQA 并不是一个脱离部署场景的纯模型创新；它是在非常明确地回应 serving 时代的物理瓶颈。后面你再看 CAKE、R-KV、FlexiCache 这类方法，会发现这条线更进一步：不只是让 K/V 变少，还要让 K/V **更聪明地存在**。8

2024 年底到 2025 年初，这条演化路线又走出了关键几步：

#### MLA：DeepSeek V3.1 的低秩压缩 KV

DeepSeek V3.1 提出的 **Multi-Head Latent Attention (MLA)**，把 MQA/GQA 的思路推向了新的高度。它不再是简单共享 K/V 头，而是对 K/V 做**低秩投影压缩**，把原始 K/V 投影到更低维度的 latent space 存储，需要时再恢复。这种方法在保持模型质量的同时，能把 KV cache 体积压缩**30–50%**，显著降低了 decode 阶段的带宽压力。MLA 的意义在于：它证明了模型架构可以主动通过**表示压缩**来服务系统级的内存效率，而不只是被动等待系统层面的优化。

#### Lightning Indexer：DeepSeek V3.2 的增量 KV 优化

DeepSeek V3.2 进一步推出 **Lightning Indexer**，针对 MLA 做了增量推理优化。它把 KV cache 的索引结构从全局压缩变成了增量更新，新 incoming token 的 KV 可以直接写入压缩缓存而不需要重新压缩整个序列，从而在保持压缩比的同时不增加延迟开销。这再次说明：**模型结构和内存系统设计必须协同进化**——压缩带来了容量好处，但增量更新的工程问题必须一起解决才能落地。

#### Attention Residuals：Kimi / MiniMax 的分层 KV 保持

Kimi 和 MiniMax 在近期的推理优化中都采用了类似 **Attention Residuals** 的思路：它们不再对所有层、所有 token 保留完整精度的 KV，而是只在底层保留完整 KV，高层只保留 residuals 或增量信息。这种分层压缩进一步降低了总体 KV 体积，同时因为底层 attention 更多关注局部位置，高层更多关注抽象语义，这种非均匀压缩对模型质量的影响非常有限。它代表了另一个方向：**利用 attention 机制本身的层次特性来做非均匀 KV 压缩**。

这些新进展继续验证着同一个方向：模型架构设计正在越来越主动地回应推理时的内存瓶颈，而不是把所有问题都丢给系统侧解决。模型定义了 KV 的冗余结构，系统才能在这个结构上做更精细的管理。

------------------------------------------------------------------------

### 10. KV Cache 其实是一种高度冗余的外部记忆

如果说 2023 年以前，很多系统还默认“KV cache 就是该存的东西，想办法装下就好”，那么 2025 年以后，一个越来越强的共识是：

> **KV cache 不是最优表示，只是最保守表示。**

它保留了 Transformer 为了不丢信息而存下来的全部历史状态，但这些状态在时间、层次、head 和 token 维度上都存在显著冗余。

R-KV 的问题设定很有代表性：reasoning models 往往会生成过长的 chain-of-thought，这会导致“prohibitively large KV caches during inference”。作者进一步指出，传统 KV 压缩方法在 reasoning model 上容易失败，因为 reasoning token 里既有真正关键的推理状态，也有大量冗余 token；R-KV 通过 redundancy-aware compression，在只保留 **10% KV** 的情况下接近满血效果，甚至在 16% KV 下能超过 full KV baseline。9

CAKE 则从另一个角度说明“冗余”不是均匀分布的。\
它把 KV eviction 建模成一个 layer-aware、time-aware 的资源分配问题：不同层的 attention pattern 不同，不同 token 的重要性还会随时间移动。结果非常激进：在 LongBench 和 NeedleBench 上，CAKE 只保留 **3.2% KV cache** 仍能维持性能，并在长上下文下显著降低 decode latency。8

FlexiCache 又提供了第三种视角：\
attention heads 在时间上的稳定性并不一样。有些 heads 会反复关注接近的 top-K 页，有些则频繁变化。于是系统就没必要对所有 heads 一视同仁：稳定的 head 可以只在 GPU 上保留 top-K 页面，其余下沉到 host memory；不稳定的 head 则保留更多 GPU-resident pages。24

如果把这三类工作放在一起看，你会发现它们共同指向一个结论：

1.  1. **很多 token 的贡献是稀疏的；**
2.  2. **很多层和很多 heads 的贡献并不对等；**
3.  3. **很多历史状态可以被压缩、淘汰、延迟加载或部分重算。**

这时，KV cache 就越来越像一种“外部记忆系统”而不是“固定中间结果”。\
Transformer 过去的做法，本质上是把历史逐 token 存档；但一个更成熟的 memory system 会问：哪些应该保留在热层？哪些可以降层？哪些其实只是冗余副本？哪些应该预测性预取？哪些干脆可以忘掉？8

所以我会说，未来很多推理系统里，**KV compression 的战略价值可能比参数量化还高**。\
参数压缩解决的是“模型能不能装下”；KV 压缩解决的是“系统能不能真正跑起来、跑得快、跑得稳”。R-KV 和 CAKE 的结果已经在很大程度上证明了这一点。8

------------------------------------------------------------------------

### 11. 为什么很多线上系统仍然在“重复计算历史”

到这里，一个自然问题是：既然 KV cache 这么重要，为什么很多线上系统没有把它彻底用好？

答案是：**因为系统工程的最优解，不等于单请求计算的最优解。**

在 API 层面，很多云服务长期采用的是近乎 stateless 的交互模型。\
OpenAI 的 Chat Completions 文档写得很明白：请求里要提供 `messages`，也就是“the conversation so far”；这意味着客户端要把历史对话内容一起发回来。后来 Responses API 加入了 `previous_response_id`、Conversations 等状态机制，可以“store and retrieve conversation state across Response API calls”，并且 Prompt Caching 允许对**完全相同的前缀**做自动缓存。但从系统角度看，这仍然和“把某个用户会话的完整 KV cache 长期 pin 在某个 GPU 上”不是一回事。25

为什么大家不直接做强 stateful KV serving？\
因为那会让会话和特定 GPU / 节点强绑定，恶化负载均衡、容错和多租户隔离。只要请求可以落到任意副本，副本就必须能在不知道前情的情况下接住请求；于是最保守的设计就是让客户端或上层服务把必要上下文重新发来。Prompt Caching 是一个很聪明的折中：OpenAI 官方文档明确说 cache hits 只可能出现在 **exact prefix matches** 上，而且现在还能通过 `prompt_cache_key` 和最长 24 小时的 extended prompt caching 来提高命中率。它确实能减少 prefill 成本，但它仍然是“**围绕前缀重用做的工程折中**”，而不是通用的跨请求 KV 内存系统。11

这就是很多“伪 agent”系统的本质。\
逻辑上，它们看起来是多轮 agent：用户问一句、工具跑一轮、模型再思考一轮。\
但物理上，很多时候它们其实是：**每一轮都重新构造 prompt，再做一次 full prefill**。\
当上下文越来越长、链路越来越多、工具越来越复杂时，你看到的不是“状态被稳态保留”，而是“历史被反复重放”。这会让 prefill 成本非常高，也解释了为什么 prompt caching / prefix reuse / PD disaggregation 会变得如此重要。11

所以，线上系统的真实矛盾不是“工程师不知道 KV cache 有用”，而是：

> **如何在可扩展、可容错、可调度的云架构里，尽量恢复 KV cache 的好处。**

第一代 KV-centric 系统，就是在解这个矛盾。

------------------------------------------------------------------------

### 12. 第一代 KV-centric 架构：DistServe、Mooncake、LMCache

如果说 vLLM 和 SGLang 主要解决的是“单引擎或单节点内，如何更好地跑”，那么 2024 年开始的一批系统开始把问题升级为：

> **跨请求、跨节点、跨阶段，KV cache 应该怎么成为系统级资源？**

这条线里，DistServe、Mooncake、LMCache 是三个非常关键的坐标。

#### DistServe：先把 prefill 和 decode 拆开

DistServe 的出发点是 goodput：\
现有 serving 系统把 prefill 与 decode 混在一起跑，会同时带来 **prefill-decoding interference** 和**resource coupling**。前者让两个阶段互相拖累；后者让资源配置无法针对 TTFT 与 TPOT 分别优化。于是 DistServe 直接做**prefill/decode disaggregation**：把 prefill 分到一批 GPU，把 decode 分到另一批 GPU，再按应用的 TTFT/TPOT 目标联合优化资源分配与并行策略。论文报告在不同模型和 workloads 上，DistServe 能在延迟约束下显著提升可服务请求率。5

DistServe 的重要性不在于它是唯一答案，而在于它第一次非常系统地把一个常识变成了架构原则：\
**prefill 和 decode 不是同一类资源需求。**

#### Mooncake：把 KV cache 提升为调度核心

Mooncake 更进一步。\
它直接把自己定义为 **KVCache-centric disaggregated architecture**。在 Mooncake 里，prefill 集群和 decode 集群是分离的，同时系统会利用 GPU 集群里原本被低估的 CPU、DRAM、SSD、NIC 资源来构建一个分布式 KV cache；核心则是围绕 KV cache 设计的 scheduler，用来在吞吐、SLO 和过载情况下平衡调度。Mooncake 论文报告在 Kimi 相关工作负载下，真实场景里可以多处理约**75% 请求**。26

Mooncake 的思路非常值得注意：\
它已经不再把 KV cache 当成“模型执行之后顺手留下来的临时副产品”，而是把它当成**系统调度的对象**。\
这是一个很大的范式转变。

#### LMCache：把 KV cache 变成共享层

如果 Mooncake 更偏架构与调度，那么 LMCache 更像是把 KV 抽象成一个可插拔的 cache layer。\
LMCache 论文把自己的定位说得非常清楚：它从 vLLM 和 SGLang 这类现代 LLM engine 里提取并存储 KV cache，然后**跨 queries、cross engines**共享这些 KV cache，既支持 prefix reuse，也支持 PD disaggregation 下的跨引擎 KV transfer。论文报告，和 vLLM 结合时，吞吐在一些 workload 上可提升到**15x**。27

所以如果你非要给三者一个最简洁的分工，我会这样总结：

- **DistServe**：先把 prefill 和 decode 分开，解决两阶段互扰；
- **Mooncake**：让 KV cache 成为分布式调度核心；
- **LMCache**：把 KV cache 抽象成可存储、可迁移、可复用的系统层。

与此同时，SGLang 的 RadixAttention 提供了另一种非常关键的能力：**在复杂 LM program 中自动发现并复用共享前缀**。SGLang 论文强调，它的 runtime 可以利用 RadixAttention 实现 KV cache reuse，并在多种任务上大幅提高吞吐。28

有意思的是，到 2026 年初，Mooncake 和 LMCache 官方文档已经明确展示了二者的集成：Mooncake 可以作为 LMCache 的后端存储和传输引擎，官方甚至直接展示了 LMCache + Mooncake + vLLM 的 PD-disaggregated demo。也就是说，现实里它们并不是“二选一”的关系，而是常常叠加使用。29

------------------------------------------------------------------------

### 13. 为什么 Mooncake / LMCache 不是终点

如果 Mooncake / LMCache 已经把 KV 提成一等公民，为什么 2025 年以后还会冒出一大堆“下一代”论文？

因为当你把 KV 做成系统级资源之后，新的瓶颈会立刻暴露出来。

#### 第一，KV 太大，搬不动

Mooncake/LMCache 的默认设定仍然是：\
**KV 值得存、值得搬、值得复用。**\
但一旦上下文变长、请求变多、agent 变复杂，KV cache 的体积会很快膨胀到 GPU 容量之外。此时问题就从“有没有 cache”变成“**cache 如何从 CPU/SSD/远程内存高效回到 GPU**”。

Strata 的摘要对此几乎是点名式批评：长上下文下，分层缓存不可避免，但把大块 cached contexts 重新加载回 GPU 时会遇到严重瓶颈——**paged layouts 带来的 fragmented I/O 无法吃满带宽，现有 scheduler 又不考虑 cache-loading delay，结果系统变成 loading-bound 而不是 compute-bound。**30

#### 第二，prefix reuse 会和延迟目标冲突

自动 prefix reuse 并不自动等于更好的 online latency。\
LinkedIn 那篇关于 RadixAttention 调度的 NeurIPS 2025 论文做了一件很重要的事：它把“有 prefix reuse 的在线调度”形式化之后证明，**在 TTFT 约束下，这个问题是 NP-hard 的**。更直观地说，简单地贪心追求 longest-prefix-match，可能会让某些请求的 TTFT 爆掉。作者因此提出 k-LPM，用来平衡 prefix reuse 与 fairness/waiting time。10

这说明什么？\
说明 Mooncake / LMCache 把“缓存能不能用”解决了，但“缓存什么时候用、优先给谁用”还没有彻底解决。

#### 第三，agent workload 的复用模式和普通 LRU 不一样

KVFlow 直接把矛头指向 agentic workflows：\
当前系统虽然会做 prefix caching，但通常采用 LRU 淘汰策略，这会在 agent 即将下一次被调用前把其 KV cache 提前丢掉。KVFlow 因而引入 workflow-aware 的 Agent Step Graph、细粒度 eviction，以及主动 prefetch。它本质上是在说：**agent 场景下，缓存管理必须理解工作流结构，而不能只看最近访问。**31

#### 第四，公平性和抢占有上下文切换成本

FastSwitch 又暴露了另一个问题：\
现有 block-based KV cache 分配虽然减少了内存浪费，但会导致上下文切换粒度不足、切换开销高。FastSwitch 因此提出一种 fairness-aware serving system，专门优化 preemption/context switching 的效率。换句话说，**当 KV 成为状态后，抢占不再是免费动作。**32

#### 第五，精确前缀命中本身就过于苛刻

在 RAG 这类场景里，两个请求往往不是“完全相同前缀”，而是“共享大量检索上下文但并不严格前缀一致”。CacheBlend 就是在这个问题上往前走了一步：它不再要求严格 prefix match，而是允许复用已缓存的 KV，再对少量 token 的 KV 做 selective recompute，从而在 RAG 上显著改善 TTFT 和吞吐。33

所以，Mooncake / LMCache 之所以“不是最新”，不是因为它们过时了，而是因为它们把问题推进到了下一阶段。\
它们解决的是：**让 KV 进入系统视野。**\
而下一代工作解决的是：**当 KV 已经成为系统资源后，如何处理 I/O、调度、agent reuse、分层缓存、公平性和局部重算。**

------------------------------------------------------------------------

### 14. 新一代 Memory-centric 架构：Strata、CAKE、R-KV、KVFlow、FastSwitch、CacheBlend

我更愿意把 2025 年之后的工作叫做 **memory-centric**，而不是简单的 KV-centric。因为这时研究重心已经不只是“缓存有没有被复用”，而是：

> **如何把 KV cache 管理成一个真正的分层内存系统。**

#### Strata：分层缓存 + GPU-assisted I/O + cache-aware scheduling

Strata 可以看作 Mooncake/LMCache 之后最系统的一次升级。\
它关注的不是“怎样做 prefix reuse”，而是“**当长上下文 cache 被分层存储后，如何高效把它重新搬回 GPU**”。论文提出 GPU-assisted I/O、GPU/CPU layout decoupling 和 cache-aware scheduling，并报告在长上下文基准上相对 vLLM + LMCache 可实现**最高 5x 更低 TTFT**。30

这类工作很关键，因为它把“KV cache 存在哪”从一个 yes/no 问题变成了一个多级层次问题：HBM、CPU DRAM、SSD，乃至更远的内存池，都是缓存层的一部分。

#### CAKE：Layer-aware eviction

CAKE 的贡献，是把“删谁”这件事变得全局且结构化。\
它不再把 eviction 看成简单 LRU，而是结合 layer-specific preference 与 temporal dynamics 去做 cascading allocation。最值得记住的不是具体算法，而是它的结果背后的信号：**很多层、很多 token、很多时刻的 KV 实际上并不值钱。**8

#### R-KV：Reasoning-specific compression

R-KV 之所以值得单独拎出来，是因为它直接对应了当下最火的 workload：reasoning。\
作者指出 reasoning models 经常会生成 excessively long outputs，而 existing compression approach 又会在 reasoning failure 上翻车，于是他们专门针对 reasoning 冗余做压缩。结果同样非常有标志性：**10% KV 接近满血性能，16% KV 甚至能超过 baseline**。9

这说明 reasoning 场景不只是“更长”，还意味着**冗余结构有别于普通聊天输出**。

#### FlexiCache：按 head 稳定性做层次管理

FlexiCache 进一步把 memory policy 做到了 attention head 层级：\
稳定的 heads，只保留 top-K pages 在 GPU；不稳定 heads，保留更多热页。这代表着另一个很重要的趋势：**缓存管理正在越来越细粒度地靠近模型内部结构**。24

#### KVFlow：workflow-aware cache for agents

KVFlow 则非常明确地站在 agent workflow 一侧。\
它的核心思想很简单但很有力：agent workload 不是随机序列，而是带有工作流依赖的 Agent Step Graph；因此缓存策略应该“知道”哪个 agent 下一步更可能被再次激活。KVFlow 再加上 fully overlapped prefetch，本质上已经很像 CPU cache 里的“预测下一步会用什么”。31

#### FastSwitch：context switching 也是成本

FastSwitch 说明，当你把大量请求都做成可抢占的、可中断的 KV-stateful 过程时，**context switching 本身会成为瓶颈**。这和操作系统里的进程切换越来越像：不是说抢占不能做，而是抢占的粒度、上下文布局、恢复成本都必须被认真设计。32

#### CacheBlend：从 exact prefix reuse 走向 approximate reuse

CacheBlend 值得注意，是因为它指出 exact prefix reuse 过于局限。\
对于 RAG 之类场景，共享上下文不一定是“完全一样的开头”，但仍然值得复用一大块历史。CacheBlend 用少量 selective recompute 把这种近似重用变成可能，这实际上把“缓存”和“计算”做成了连续体，而不是非此即彼。33

把这些工作放在一起看，你会发现新一代架构的关键词已经不是简单的 “cache reuse”，而是：

- hierarchical tiers
- cache-aware scheduling
- workflow-aware eviction
- partial recompute
- proactive prefetch
- fairness-aware switching

这已经完全是 memory system 的语言了。

------------------------------------------------------------------------

### 15. CXL：看起来像终极答案，为什么现实里还很难

CXL 之所以让人兴奋，是因为它表面上很像一条“兼得”的路线：\
容量可以扩展、内存池可以共享、load/store 语义更自然、看起来又比 RDMA 更像真正的内存。

Beluga 的摘要就很有代表性：它提出通过 CXL switch 让 GPU 和 CPU 访问一个 shared large-scale memory pool，并强调这种 load/store access semantics 能带来 near-local memory latency、减少同步与编程复杂度。论文在 vLLM 上报告了相对 RDMA baseline 显著 TTFT 和吞吐改善。34

但如果因此得出“CXL 就是最终解”，那就太乐观了。

#### 第一，CXL 解决的是容量，不是 HBM 级带宽

HBM 的价值不只是近，而是**又近又宽**。\
CXL 能做出更大的共享内存池，但它不会自动给你 HBM 级吞吐。Beluga 的改进之所以成立，是相对 RDMA 等更曲折路径而言；并不意味着 CXL 可以无成本替代 GPU 本地显存。34

#### 第二，CXL 不是自动 coherent 的天堂

TraCT 的摘要非常有教育意义。\
它明确指出，为了实现基于 CXL shared memory 的 rack-scale KV cache，必须处理 **synchronization, consistency, and data management on non-coherent CXL memory**。换言之，现实里的 CXL，至少在很多商用品质和部署形态下，并不是“天然全局一致的 UMA”。你还是要自己补软件协议。35

#### 第三，数据移动不见得比重算便宜

只要 KV 足够大、访问足够碎、竞争足够高，跨层搬运本身就会成为主成本。TraCT 专门把 KV transfer 视为 PD disaggregation 的 fundamental bottleneck；CXL-SpecKV 则不得不引入 speculative prefetch + FPGA compression/decompression，才能把 disaggregated KV-cache 的代价压住。35

#### 第四，CXL 方案经常不得不引入更多“系统补丁”

Beluga 通过 shared pool + native load/store 降低编程复杂度；TraCT 通过软件级同步机制处理 non-coherence；CXL-SpecKV 又通过 speculative prefetch 和压缩去弥补带宽/延迟问题。你会发现，CXL 不是一个“买来即用”的硬件银弹，而是一个**要求系统/软件/硬件协同设计**的平台。34

所以我会把 CXL 的真实定位概括成一句话：

> **CXL 很重要，但它更像“新增一层内存层级”，而不是“让所有远程内存都变成本地 HBM”。**

一旦这样理解，很多现象就不矛盾了：\
为什么 CXL 方案总在讨论 prefetch、压缩、shared pool、non-coherence、software sync？\
因为它们在本质上做的是——**承认远程内存仍然更慢，然后尽量把这份慢掩盖掉。**

------------------------------------------------------------------------

### 16. LLM serving 正在变成一个“操作系统问题”

如果把今天的主流 LLM serving 系统和 5 年前的 DNN serving 系统一对比，最大的变化不是模型更大，而是抽象层变了。

你会看到一整套越来越像操作系统的概念：

- `pages / blocks`：PagedAttention 像虚拟内存分页；21
- `radix tree`：RadixAttention 像基于前缀的共享索引；28
- `cache hit / miss`：prompt caching、prefix reuse、KVFlow、CacheBlend 都在围绕命中率做文章；11
- `eviction policy`：CAKE、KVFlow、FastSwitch 都在研究谁该被驱逐；8
- `prefetch`：KVFlow、CXL-SpecKV、Beluga 这类系统都在强调预测性加载；31
- `scheduling under SLO`：DistServe、Revisiting SLO and Goodput、LinkedIn 那篇 k-LPM 理论工作，都把 serving 视为 latency-constrained online scheduling。5

甚至“好不好”的评价指标都越来越不像传统训练。\
训练时代，大家比的是 tokens/sec、TFLOPS utilization、samples/sec。\
Serving 时代，越来越关键的是：**TTFT、TPOT、P99、SLO attainment、goodput**。Revisiting SLO and Goodput Metrics in LLM Serving 明确指出，传统 goodput 指标甚至会鼓励一些违背用户体验的行为，因此需要重新定义 serving 指标框架。22

这意味着一个非常根本的变化：\
以前我们常说“LLM infra 的核心是分布式训练系统”。\
现在更准确的说法也许是：**LLM serving 的核心正在变成一个面向 KV state 的在线内存操作系统**。

这个“操作系统”要解决的事情包括：

1.  1\. 如何把状态拆成页；
2.  2\. 如何在多层存储中放置；
3.  3\. 如何决定谁驻留 GPU；
4.  4\. 如何预测谁下一步会用；
5.  5\. 如何平衡公平、吞吐和尾延迟；
6.  6\. 如何在必要时压缩、重算、抢占和迁移；
7.  7\. 如何让 prefix sharing 和多租户服务共存。

从这个角度看，Mooncake/LMCache 只是“把文件系统建起来”的第一步；Strata、KVFlow、FastSwitch、Beluga、TraCT，则在往“完整内存管理器”方向走。

------------------------------------------------------------------------

### 17. KV cache 之后是什么：Mamba、RWKV 与“在线压缩记忆”

如果把问题继续追到底，一个更激进的问题会冒出来：

> **既然大家已经承认 KV cache 很大、很贵、很冗余，那为什么不干脆不要 KV cache？**

这就是 Mamba、RWKV 这类方向的吸引力。

Mamba 的核心主张很明确：Transformer 在长序列上存在根本性的计算效率问题，因此它用 selective state spaces 去构建一种**linear-time sequence model**。论文强调 Mamba 是 fully recurrent 的，并报告在语言建模上获得很强性能，同时推理吞吐优于同规模 Transformer。36

RWKV 的表述也很直接：它想结合 Transformer 可并行训练的优点与 RNN 高效推理的优点，实现线性扩展的推理过程。37

如果用一句更系统的话来说，Transformer 的 KV cache 是一种“**把历史逐 token 存档**”的外部记忆；而 Mamba/RWKV 这类模型更像在尝试一种“**在线压缩记忆**”：不是把每一段历史都原样保留，而是把历史不断压缩进一个递归状态里。

这条路线的诱惑非常大，因为它从根子上避免了“每步必须读完整历史 K/V”的问题。\
但现实也很清楚：截至 2026 年，Transformer 仍然是工业部署的主流，围绕 KV cache 的系统创新还在高速推进。这说明产业界的短中期共识不是“马上替换 Transformer”，而是“**先把 KV-based world 优化到极致**”。36

所以，KV cache 之后的未来，大概率不是一个瞬间翻篇的故事，而是两条线并行：

- 一条线继续把 Transformer serving 做成真正成熟的 memory system；
- 另一条线探索如何用 state-space / recurrent / hybrid 架构，把“历史存储成本”在模型层面降下来。

这两条线并不冲突。相反，今天围绕 KV cache 做出的所有系统认知，都会成为理解下一代序列架构的基础。

------------------------------------------------------------------------

### 18. 结语：三条真正的主线

如果要把整篇文章浓缩成三条主线，我会这样总结。

#### 第一条：从 Compute 到 Memory

Transformer 训练时代，焦点是 FLOPS；\
Transformer 推理时代，焦点越来越是 **working set、带宽、延迟、状态复用**。\
FlashAttention 重要，但它不是终局；真正的终局问题是：**历史信息该如何被存储、访问、迁移和压缩。**19

#### 第二条：从 Stateless 到 Stateful

云上 API 为了可扩展、可容错和多租户，天然偏向 stateless；\
但 agent、多轮对话、长 CoT、RL rollout，又天然需要 stateful。\
于是过去两年最重要的 serving 创新，几乎都在试图调和这对矛盾：prompt caching、prefix reuse、RadixAttention、LMCache、Mooncake、DistServe、KVFlow、Beluga、TraCT。它们的共同目标都是：**在不牺牲云架构弹性的前提下，尽量恢复状态复用的收益。**11

#### 第三条：从 Model 到 System，再到 Memory OS

过去我们常把“模型创新”和“系统优化”分开看。\
但今天，GQA 这种结构设计直接影响带宽；R-KV 这种压缩方法直接影响 serving 成本；KVFlow/FastSwitch/Strata 这种系统工作又在深度利用模型内部的时间稳定性、前缀结构和层间差异。到这个阶段，模型、引擎、调度、内存层级其实已经被绑在一起。23

所以，这篇文章真正想表达的不是“Mac 好还是 NVIDIA 好”，也不是“Mooncake 和 LMCache 过没过时”。\
我更想强调的是：

> **大模型推理的下一阶段，越来越不是一个“神经网络算子优化”问题，而是一个“如何把历史变成可管理内存”的系统问题。**

一旦你接受这一点，很多过去看似碎片化的现象就会统一起来：

- 为什么 RL rollout 让 inference 比 training 更贵；
- 为什么 Mac 的统一内存会重新有意义；
- 为什么 FlashAttention 不够；
- 为什么 vLLM、SGLang、Mooncake、LMCache、Strata、Beluga、TraCT 会同时出现；
- 为什么 CXL 让人兴奋又让人头疼；
- 为什么 KV cache compression 可能比参数压缩更重要；
- 为什么未来的 LLM serving，看起来越来越像一个操作系统。

而这，也许才是过去两年 AI infra 最值得被认真理解的变化。

------------------------------------------------------------------------

### 参考阅读（按主题分组）

#### 基础机制

1.  6. *Attention Is All You Need* — Transformer 与 masked decoder。6
2.  7. *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* — 双向 encoder 路线。3
3.  8. *Language Models are Unsupervised Multitask Learners* — GPT 路线的代表性早期文本。38

#### Kernel / Engine

1.  19. *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness*。19
2.  20. *Efficient Memory Management for Large Language Model Serving with PagedAttention*（vLLM）。21
3.  21. *Orca: A Distributed Serving System for Transformer-Based Generative Models*。20
4.  22. *Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve*。4
5.  23. *SGLang: Efficient Execution of Structured Language Model Programs*。28

#### 模型结构与 KV

1.  7. *Fast Transformer Decoding: One Write-Head is All You Need*（MQA）。7
2.  8. *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*。23
3.  9. *CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences*。8
4.  10. *R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration*。9
5.  11. *FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management*。24

#### 架构与系统

1.  5. *DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving*。5
2.  6. *Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving*。26
3.  7. *LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference*。27
4.  8. *Strata: Hierarchical Context Caching for Long Context Language Model Serving*。30
5.  9. *KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows*。31
6.  10. *FastSwitch: Optimizing Context Switching Efficiency in Fairness-aware Serving Systems*。32
7.  11. *CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion*。33
8.  12. *LLM Query Scheduling with Prefix Reuse and Latency Constraints*。10
9.  13. *Revisiting SLO and Goodput Metrics in LLM Serving*。22

#### RL / Agent / Post-training

1.  1. *OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework*。1
2.  2. *ECHO-2: A Large-Scale Distributed Rollout Framework for Cost-Efficient RL Post-Training*。12
3.  3. *AgentRL* / *Agent Lightning* 这类 agentic RL 基础设施工作。13

#### 硬件与内存系统

1.  14\. Apple 官方关于 unified memory、M2 Ultra、M3 Ultra、M5 Pro/Max、MLX 的材料。14
2.  15\. NVIDIA Grace Hopper / GH200 官方 coherent memory 材料。39
3.  16. *Beluga*, *TraCT*, *CXL-SpecKV* — CXL/shared memory 方向。34
