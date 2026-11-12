---
title: 规格驱动（SDD）与上下文工程
linkTitle: SDD 与上下文
description: 文档驱动开发、工程中心法则、Agent OS 进程模型与上下文窗口调度。
weight: 30
icon: fa-solid fa-compass-drafting
---

代码合成廉价化后，工程成败完全前移至收敛搜索空间的规格文档（SDD）与人工验收底线。看透“记忆是环境的补集”，用可读的运行时地皮、目录检索与显式群聊容器取代臃肿中间件，才是上下文工程的正道。

## 一、文档驱动（SDD）与工程中心法则 {#sdd-and-dogma}

### 什么是软件 3.0 与“写意编程”协作范式？ {#software-3-and-xieyi}

正如 Karpathy 所揭示，自然语言已继确定性代码（1.0）与神经网络权重（2.0）之后跃升为“软件 3.0”接口。我主张把 Vibe Coding 译为国画里的“写意编程”而非误导性的“氛围编程”：手敲代码如“工笔”，传达高维意图重神似正是“写意”。在攻克长尾可靠性前，最佳形态是靠红绿 Diff 调动人类视觉核验、配“自主性滑块”的人机外骨骼。

- [软件3.0时代，AI带来的范式转移 · Andrej Karpathy：软件正在再次发生改变](/ai/software-3-0/#andrej-karpathy软件正在再次发生改变)
- [软件3.0时代，AI带来的范式转移 · 部分自主应用：人与 AI 并肩协作](/ai/software-3-0/#部分自主应用人与-ai-并肩协作)
- [Vibe Coding 应当翻译为“写意编程” · 先看看有哪些候选](/ai/vibe-coding-translate/#先看看有哪些候选)
- [Vibe Coding 应当翻译为“写意编程” · 为什么“写意编程”最好](/ai/vibe-coding-translate/#为什么写意编程最好)

### 随口糊代码为何必崩，大工程如何践行中心法则？ {#central-dogma-prd}

凭感觉随口糊代码遇上中大型工程必成屎山，我的第一铁律是“可以不读代码，绝不能不读需求文档”。开工前先打磨 PRD 收敛搜索空间，严守“意图（DNA）→规格 Story（RNA）→干净新会话合成代码（蛋白质）”的单向中心法则，再配合异构双模互审、容器冒烟验收，并将跨平台编译脏活下放给只报摘要的子代理以隔离主上下文。

- [文档驱动：AI 软件工程的第一秘籍 · 许愿与设计](/ai/sdd/#许愿与设计)
- [写代码一文不值的时代，什么才值钱？ · 设计：中心法则：从意图到代码的信息级联](/ai/try-codex/#设计中心法则从意图到代码的信息级联)
- [Codex/Claude 脚踏车要蹬冒烟了 · 几条实用技巧](/ai/bicycle/#几条实用技巧)

### 不逐行手审代码时，算力预算与验收底线立在哪？ {#qa-token-budget}

糊出 80 分半成品极省算力，但要把基础软件推向敢上生产的 95 分，70%～80% 的 Token 预算都必须砸在暴力测试、对抗找茬与架构纠偏上。单测可交给双模互审，但验收签字等于押上个人信誉，绝不能外包：我强制要求同步交付代码级 `Get Started` 手册并亲自照着跑通，同时归档记录每次权衡缘由（Why）的 `Session Log` 作为灵魂资产。

- [文档驱动：AI 软件工程的第一秘籍 · 为什么要写好文档](/ai/sdd/#为什么要写好文档)
- [文档驱动：AI 软件工程的第一秘籍 · 测试与验收](/ai/sdd/#测试与验收)
- [文档驱动：AI 软件工程的第一秘籍 · 一个具体的例子：Silo](/ai/sdd/#一个具体的例子silo)

### 模型返回概率而非定论时，软件逻辑如何动态结晶？ {#crystallization-and-cost-matrix}

未来软件逻辑将沿“三层梯度”动态结晶：陌生任务由前沿模型写一次性探索脚本，跑顺后收敛为百毫秒“无嘴模型”判别点，摸透后再固化为确定性函数。判断层首次将客观概率原样上交最懂赔付成本的应用层，让控制流回归代码 `if` 并按代价矩阵算贝叶斯阈值——若漏报赔 50、误报赔 5，最优阈值绝非拍脑袋的 `0.9`，而是 `0.09`。

- [应用层塌缩：当 Agent 吃掉软件，护城河退守数据库 · 五、固化结晶的梯度](/ai/sor-harness/#五固化结晶的梯度)
- [无嘴模型：AI 的 OLTP 时刻 · 八、if 的回归，与代价矩阵](/ai/jev-shutup-model/#八if-的回归与代价矩阵)

### 为何外部重写数据库难落地，算力真正该接盘什么？ {#vibe-porting-and-takeover}

百万行跨语言移植只适合原团队自译：Bun 烧 16.5 万美元自译仍踩 19 个回归，外部重写 PostgreSQL 根本搬不走测试流量与兜底责任人。对成熟底座该用 AI 考古邮件沉淀可复现 Failing Test；而在 MinIO 停摆的真空带，单人凭 7 个订阅一月即可将 Silo 推成超 2200 Star 的社区标准。

- [AI 用 Rust 重写 PostgreSQL？别逗了 · 三、Bun 恰好是个对照组](/ai/rewrite-pg-in-rust/#三bun-恰好是个对照组)
- [AI 用 Rust 重写 PostgreSQL？别逗了 · 七、pgrust 真正值得留下什么](/ai/rewrite-pg-in-rust/#七pgrust-真正值得留下什么)
- [OPC 一个月烧 1000 刀订阅，能有多少产出？ · Silo：从 Fork 到一整套产品](/ai/yield-with-agents/#silo从-fork-到一整套产品)

## 二、Agent OS、上下文架构与记忆真相 {#agent-os-and-context}

### 为何独立记忆框架是死路，记忆是环境的补集？ {#memory-complement-of-env}

第三方 Memory SDK 毫无壁垒：剥掉类脑术语不过是建几张表封几条 SQL，还不如百字 `memory-skill.md` 让模型直连 PostgreSQL 自写查询；Anthropic 实验也证实硬塞先验记忆规则反而拉低收益。本质上，记忆是环境的补集——当监控随时可查、操作收敛于 CLI、规范写进文档，可读有序的环境自己就能回答现状，单份 `agents.md` 足矣。

- [记忆是环境的补集 · 一、Anthropic 说了什么](/ai/memory-vs-context/#一anthropic-说了什么)
- [记忆是环境的补集 · 二、记忆是环境的补集](/ai/memory-vs-context/#二记忆是环境的补集)
- [三分天下：为什么Agent Memory框架是死路 · 三、它没有壁垒](/ai/agent-memory-framework/#三它没有壁垒)

### 如何低成本根治编程智能体的跨会话隔夜失忆？ {#cross-session-wiki}

编程 Agent 隔夜失忆，散装笔记易自相矛盾，而离线“做梦”整理动辄烧上亿 Token 算不平账。最划算的是双层沉淀：底层用数据库与编年体日志托底原始轨迹，顶层靠 SDD 维护互链 Markdown Wiki 并在 `AGENTS.md` 提炼决策索引，实测准确率升至 61% 且单题立省 2 万 Token。

- [文档驱动：AI 软件工程的第一秘籍 · 开发与修复](/ai/sdd/#开发与修复)
- [记忆是环境的补集 · 五、Markdown 与 Wiki](/ai/memory-vs-context/#五markdown-与-wiki)

### 顶级工具为何弃向量库回 grep，检索怎么选？ {#grep-over-rag}

Claude Code 弃向量库回归目录加 `grep`，只因静态切片盲猜一次且背负同步税；目录配多轮搜索能边找边改主意，Pigsty 凭零向量扛住月均上亿 PV。选型看资料：量小直塞上下文，代码手册交 Agent 自搜，唯海量杂乱合同邮件才需“全文抓精确码 + 向量补同义词 + 权限过滤”混合栈。

- [RAG 没死，但也快了 · Claude Code 最后选了 grep](/ai/rag-is-dead/#claude-code-最后选了-grep)
- [RAG 没死，但也快了 · 先看资料，再选架构](/ai/rag-is-dead/#先看资料再选架构)

### 单对话框小秘书遇大工程为何拉胯，群聊才是正解？ {#group-chat-context-container}

临时执行 Session 可藏入底层，但包含仓库、规范与权限的“工作上下文”绝不能隐藏；单对话框靠后台猜语义路由，一句“清理垃圾”派错现场就是删库事故。如同连 PostgreSQL 必先声明库与角色，按项目建群点进去 `@` Agent 才能零成本显式绑定目录与权限分级，还能拉异构御三家同群互审制衡、折叠争论呈交摘要由人类拍板。

- [评 DeepSeek Super-Agent：为什么小秘书遇上大工程就拉胯？ · Context 到底是什么？](/ai/ds-super-agent/#context-到底是什么)
- [评 DeepSeek Super-Agent：为什么小秘书遇上大工程就拉胯？ · 群聊是正确的形态](/ai/ds-super-agent/#群聊是正确的形态)
- [评 DeepSeek Super-Agent：为什么小秘书遇上大工程就拉胯？ · 多对多的上下文容器](/ai/ds-super-agent/#多对多的上下文容器)

### 智能体为何处在 DOS 时刻，内存进程卡在哪？ {#agent-os-memory-process}

映射回计算机体系：LLM 是 CPU，上下文是内存，数据库是磁盘；裸操终端恰如无隔离保护的 DOS。头号战场是充当虚拟内存的上下文工程——缓存命中仅未命中 1/10 成本，须拿文件当 Swap 并守住八二算力记忆比；而套壳 `while` 编排只是伪红海，7×24 守护进程的抢占与断点恢复才是真蓝海。

- [AI Agent 的操作系统时刻 · 一、核心框架：Agent OS 的五大子系统](/ai/agent-os/#一核心框架agent-os-的五大子系统)
- [AI Agent 的操作系统时刻 · 二、内存管理：最复杂也最重要的战场](/ai/agent-os/#二内存管理最复杂也最重要的战场)
- [AI Agent 的操作系统时刻 · 进程管理：表面红海，深水无人](/ai/agent-os/#进程管理表面红海深水无人)

### 通用模型持续吞噬能力后，真正的壁垒与身体在哪？ {#runtime-body-and-moat}

写代码是当场造工具的元技能，死板垂直工作流与 `SKILL.md` 技巧迟早被通用模型吞噬。抄不走的地头蛇护城河是脚下的运行时地皮——预置监控全家桶的确定性沙箱、幂等 CLI 与精确注释的数据库 Schema。迈向真专家须分两步：先赋予持久有状态、能结合无嘴模型与事务热插拔的运行时“身体”推至 85 分，再靠持续微调将实战体感回灌进“权重”。

- [记忆是环境的补集 · 三、环境是真正的壁垒](/ai/memory-vs-context/#三环境是真正的壁垒)
- [专家能被蒸馏吗？ · 七、给 Agent 一个身体](/ai/tacit-knowledge/#七给-agent-一个身体)
- [应用层塌缩：当 Agent 吃掉软件，护城河退守数据库 · 四、驾驶舱：Codex、Jev、DSH](/ai/sor-harness/#四驾驶舱codexjevdsh)
- [Claude Code 可观测性怎么做？ · 沙箱环境](/ai/claude-observability/#沙箱环境)

### 个人助理为何收敛为落户四件套，桌面系统谁能赢？ {#secretary-runtime-os}

各家个人 Agent 趋同演化出“云电脑 + 独立身份 + 钱包 + IM 群聊”四件套，本质是给硅基劳动力在数字世界“上户口”。操作存量 GUI 软件离不开完整图形桌面：macOS 赢在本地，但给几十亿人低成本发云桌面必由免费易虚拟化的 Linux 胜出；叠加稀疏 MoE 冷门专家卸载技术让老显卡跑起百亿模型，正从软硬双线瓦解苹果的软件地租与内存暴利。

- [欢迎来到 AI 秘书大爆发的时代 · 形态学](/ai/secretary-era/#形态学)
- [欢迎来到 AI 秘书大爆发的时代 · Agent Runtime](/ai/secretary-era/#agent-runtime)
- [苹果新品：512 GB 金子内存、触屏 MacBook 与越来越无聊的刀法 · 最好的本地 AI 盟友，最狠的存储屠夫](/ai/bad-apple/#最好的本地-ai-盟友最狠的存储屠夫)
