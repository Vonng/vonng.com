# 记忆是环境的补集

11 月 6 日，Anthropic 发了一篇工程博客 [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)，用一组实验讲透了 Agent 怎么跨会话积累经验，写得非常好。这个话题老冯一直很关心。今年我写过好几篇关于 Agent 的文章，多次聊了这个问题：**[Agent 的壁垒到底在哪？](https://mp.weixin.qq.com/s/V3r5lAJw4s9Ehl2j0mAFXg)**

在年初那篇《[强龙不压地头蛇](https://mp.weixin.qq.com/s/V3r5lAJw4s9Ehl2j0mAFXg)》里，老冯给出的判断是：Agent 的机会不在于 Agent 本身，而在于它运行的环境 —— Agent Runtime；纯靠 Agent 这一层，没有任何壁垒。

不过那时候我手里只有日常干活的体感，没有硬数据。Anthropic 这篇文章表面上聊的是“记忆”，但读完不难发现，他们跑出来的数据，恰恰站在了“环境”这一边。



## 一、Anthropic 说了什么

先说结论：**记忆的关键不在怎么存，而在记什么。会记的模型，只记环境里看不到的东西。**

这个结论最直接的证据，来自他们跑的宝可梦实验。Sonnet 3.7 一边玩一边记，狂写了 413 个文件、近百万字符的笔记，最后只拿到 1 枚徽章；而 Fable 5 只写了 9 个文件、四万多字符，却拿下了 4 枚。

核心差别在记了什么。Sonnet 3.7 见什么记什么，连屏幕上本来就看得到的状态也往本子上抄，抄着抄着状态就过时了。Fable 5 的原则正好相反：屏幕上看得到的一概不记，只记屏幕给不了的东西——策略、计划，以及验证过的规则。虽然两个模型差了好几代，放在一起比不算严格控制变量，但指出的方向非常清楚。

那这种“挑着记”的本事从哪来？另一组实验给出的答案是：来自模型自己。挂上同一套记忆机制，Opus 5.5 在 CL-Bench 上的得分从 0.655 涨到了 0.838，而 Sonnet 4.6 只从 0.330 微涨到 0.364。强模型懂得把规则、证据和踩过的坑串在一起记下来，弱模型却只会堆砌一堆未经验证的猜测。反过来，如果你非要给强模型立规矩——比如硬性规定“只许记录失败”——记忆带来的收益反而会缩水。

> 衍生结论就是：现在这些所谓记忆框架，可能都是昙花一现的临时玩意。因为只有模型本身才知道应该记什么，记哪些。它完全可以直接对接 FS/DB 设计任何自己想要的结构，不需要画蛇添足的先验。

最后一个问题：记错了怎么办？有一局宝可梦里，Agent 记错了一条路线，结果在月见山里死磕了三圈，最后只能放弃。Anthropic 的解法叫 dreaming（做梦）：离线回放原始日志，把写错的笔记改掉，再把碎片整理成互相链接的 Wiki。等把那条写错的路线改过来，原来卡死的路一下就走通了。

整篇文章串起来逻辑很简单：记什么交给模型自己挑，只记环境给不了的；万一记错了，就拿原始日志出来对账。



## 二、记忆是环境的补集

“只记环境里看不到的东西”，这句话反过来念就是：**记忆是环境的补集。** 环境能直接告诉你的，根本不用记；环境本身越可读，Agent 需要背在身上的记忆就越少。

对这句话，我是有[切身体感](https://mp.weixin.qq.com/s/4dy75-gEmFf0amxuo0hVOQ)的。

今年 1 月老冯上线过一个 [DBA Agent](https://mp.weixin.qq.com/s/4dy75-gEmFf0amxuo0hVOQ)。我当时根本没去搭什么 harness，也没写一行 Python 代码，更没接任何记忆中间件。全身上下就一个简简单单的 `agents.md` 文件：把我整个[文档站的目录索引](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247493214&idx=1&sn=3caff1da5367f517a35e983bd068522b)丢进去，再告诉它环境里的监控在哪、数据库在哪、密码怎么拿、出了问题去哪看。

就这么一个文本文件，DBA Agent 就直接上线了。

是不是有点滑稽？但这还真不是糊弄，现在很多用户就是这么拿到生产环境里用的，实际效果远超他们的预期。之前我在《[百万流量](https://mp.weixin.qq.com/s/wM9To5f9qkCRxFpTl8GmJg)》那篇文章里晒过后台数据，老冯文档站的请求量暴增，其中 [90% 以上的流量](https://mp.weixin.qq.com/s/1U7gbxLTP7RUF3ZD9e7TVg)全来自这些 Agent。

它为什么不需要复杂的记忆系统？说白了，**所有 Agent 的问题的核心，最后都会变成 [Context（上下文与环境）管理](https://mp.weixin.qq.com/s/vo_mDk9e2aw-yyHXpgP63Q)问题。** 老冯在之前 [锐评 DS SuperAgent 的文章](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247493853&idx=1&sn=3e810101dbf3d78c605b7e1fc8b88b42) 里就讲过，做 Agent 第一重要的事，永远是如何设计 Context。这就像你开一家公司，要搭组织架构、拆分工作职责，你真正要设计的是一套运转规则——说白了就是“立法”，创造秩序：工具在哪、边界在哪、能干什么、不能干什么。

设计环境，就像开一家公司：要搭组织架构、拆分工作职责，你真正要设计的是一套运转规则——说白了就是“立法”，创造秩序：工具在哪、边界在哪、能干什么、不能干什么。

当这套环境高度可读、规矩全部立好之后：[指标和日志随时能去监控里查](https://mp.weixin.qq.com/s/4dy75-gEmFf0amxuo0hVOQ)，操作全部收敛在命令行里，规范和参数都明明白白写在文档里。Agent 拎包入住就行，留给它记的，只剩下“这家客户有什么特殊怪癖”和“[上次为什么这么做决策](https://mp.weixin.qq.com/s/vo_mDk9e2aw-yyHXpgP63Q)”——给它配个小记事本就绰绰有余了。反过来，要是把它丢进一个[黑盒环境](https://mp.weixin.qq.com/s/V3r5lAJw4s9Ehl2j0mAFXg)里，它就得拼命拿本子记“昨天改过什么参数”、“哪台机器磁盘快满了”。

记得越多，错得越多，只要错上一条，就是又一座走不出去的月见山。

所以真正有壁垒的，是这套设计好的上下文环境。



## 三、环境是真正的壁垒

顺着这个逻辑推到底：记什么，是模型自己的本事；剩下的，靠环境来扛。那 Agent 这一层，还能剩下什么？结论其实已经呼之欲出了：**有壁垒的从来不是 Agent，而是运行时环境本身。**

老冯一直觉得，很多做纯 Agent 创业的公司全是在瞎扯淡。因为 Agent 这一层根本留不住任何壁垒，很快那点东西就被模型厂商消化吸收了。

你想靠自研 harness 建壁垒？路边一条做得过 Claude Code、Codex、Pi、Hermes 这些 harness 吗？退一步不卷通用框架，去卷垂直领域的 Data Agent、Law Agent 行不行？照样没戏。

要明白，在所有的 Agent 里面，**Coding Agent 是最难的，也是皇冠上的明珠。** 因为写代码是一种通用的元技能——它的本质就是“发明工具来解决问题”：如果现有的工具解决不了问题，它就当场写代码造一个工具来解决。那你凭什么认为，自己拍脑袋、先验设定出来的那套死板流程，能比一个会自己造工具的 Coding Agent 干得更好？这个概率同样趋近于零。



老冯那个 DBA Agent，其实也不是什么垂直 Agent。底下就是一个通用的 Coding Agent，加一份 `agents.md`，跑在 Pigsty 的环境里。垂直的部分**全在环境里**，不在 Agent 里。

更何况，你在 `agents.md`、`SKILL.md` 里攒下的那些精妙小技巧与 know-how，说到底只是思路。著作权只保护表达，不保护思路，用不了几个月，这些技巧就会被洗进下一代大模型的训练语料里，被底层模型直接吸收消化。

那么，什么是有壁垒的？Agent 运行的环境。强龙不压地头蛇：通用大模型和 Coding Agent 是过江的强龙。我那份 `agents.md` 只是一张地图，谁都能抄，但抄过去没用，因为它指向的那块地抄不走：600 多个扩展在 16 个发行版上的构建流水线、高可用和 PITR、那套监控栈。**地头蛇的本钱，不是手里的地图，而是脚下那块地皮。**

这也是 Personal Agent 和 Personal Computer 2.0 最近这么火的原因：给 Agent 配一台自己的电脑，就是给它一块自己的地皮。既然壁垒在环境，那环境的底子该怎么打？Anthropic 后半篇正好给了一份踩坑清单。



## 四、拿着锤子找钉子

Anthropic 在后半篇列了不少工程难题，基本都出在“做梦”和 Wiki 维护上。但在老冯看来，这些全是数据库领域早就解决掉的老问题：

| Anthropic 遇到的问题                           | 数据库里叫什么          |
| ---------------------------------------------- | ----------------------- |
| 多个 Agent 写同一张共享表，57 条事实丢了 16 条 | 丢失更新（Lost Update） |
| 第二轮做梦专门去修 9 个死链                    | 外键约束（Foreign Key） |
| 怎么不全量重查也能让记忆保鲜                   | 增量视图维护（IVM）     |
| 按访问频率决定多久做一次梦                     | autovacuum 的触发阈值   |

再退后一步看它的整体架构：[原始日志就是 WAL](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247493853&idx=1&sn=3e810101dbf3d78c605b7e1fc8b88b42)，是[唯一事实来源（Single Source of Truth）](https://mp.weixin.qq.com/s/RVrbaY06Hb46R25DKpo_Rw)；笔记和 Wiki 是物化视图；而所谓的“做梦”，本质上就是离线批处理加上 `VACUUM`。

当然，老冯是做数据库的，手里拿着锤子，看什么都像钉子。这把锤子我也确实抡了大半年——从《[AI Agent 的操作系统时刻](https://mp.weixin.qq.com/s/JcSkvhUUKRMsLrt37-xQCA)》、《[AI 说：我有智慧，但无人生](https://mp.weixin.qq.com/s/_jEQ6zRs5Wwj83ljmmVToQ)》到《[三分天下](https://mp.weixin.qq.com/s/bWpka2OzrJFyrbmrecIQUw)》，好几篇文章都在讲同一个判断：Agent 记忆的终局是数据库。

但这大半年自己真刀真枪用下来，我发现有数据库还没到那一步，**反而 [Markdown 知识管理](https://mp.weixin.qq.com/s/vo_mDk9e2aw-yyHXpgP63Q)是 Agent 的刚需。**



## 五、Markdown 与 Wiki

Anthropic 自己的测试数据就印证了这一点。他们让 Agent 通过“做梦”，把一大堆原始语料整理成互相链接的 Wiki，然后去测答题准确率：只搜原始语料是 53%，只看 Wiki 是 48%，而把两者结合起来，准确率直接涨到了 61%，平均每道题还能省下约 2 万个 token。[原始事实加底层检索](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247493214&idx=1&sn=3caff1da5367f517a35e983bd068522b)是地基，这是数据库的活；但在地基上面叠一层[结构良好的 Wiki](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247493853&idx=1&sn=3e810101dbf3d78c605b7e1fc8b88b42)，效果才最好。

这个 Wiki 是什么？说白了，就是一堆良好组织，互相链接的 Markdown 文件。

“做梦”是很贵的。Anthropic 整理那份 Wiki 花了上亿 token，按最高档粗算，得被提问几千次才能回本。让每个野生的 Agent 各自去做梦，这账怎么算都亏；但如果我们[事先把一份高质量的 Wiki 维护好](https://mp.weixin.qq.com/s/vo_mDk9e2aw-yyHXpgP63Q)，[让所有过来的 Agent 反复读取](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247493214&idx=1&sn=3caff1da5367f517a35e983bd068522b)，这笔账就非常划算了。

这也是为什么老冯最近花了不少时间做 [Oink](https://mp.weixin.qq.com/s/MU5xKj-llGIyOP0pTsuxnA)。表面上看，它是一个文档框架，但你也可以把它理解为一个基于 Markdown 的 Wiki 知识库。我手上每开一个开源项目，都会标配一套这样的 Wiki。

我现在写代码也是这么干的，我管它叫 SDD（Spec-Driven Development，我更愿意叫它文档驱动开发）：把所有核心知识集中沉淀在项目的 Wiki 里。这比放任 Agent 在项目的 `docs`、`research notes`、`reports` 目录里随地大小便要好太多了。那些散落一地的笔记没人整理、互相矛盾、版本错位，攒到最后，全是一堆等着爆雷的“月见山笔记”。

我虽然没有像 Anthropic 那样专门跑基准测试、做定量分析，但日常干活的体感非常明显：把这套规矩立起来之后，AI Engineering 的实际效果要好上太多。



## 结语

回到开头那个问题：Agent 的壁垒到底在哪？

老冯认为，真正的壁垒在于可复制的，秩序井然，高信息密度的上下文环境。对于 Data Agent 来说，你精心准备的分析师指南 Skill 不是壁垒，但每个字段都写满准确详情注释的数据库 Schema / Catalog 是壁垒。对于 DBA Agent 来说，你的 SOP 手册不是壁垒，提供完整监控系统与 IaC / CLI 管理工具的环境，是是壁垒。

记忆是环境的补集。最好的上下文管理，就是让环境准备好一切上下文，让 Coding Agent 自己来探索。谁拥有这样的环境，谁就是那条地头蛇。

> 广告时间：Pigsty (https://pigsty.cc)，为你的 Personal Agent 提供一个自主可控的数字家园。


## 参考

- [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)，Anthropic，2026-11-06
- [AI Agent 的操作系统时刻](https://mp.weixin.qq.com/s/JcSkvhUUKRMsLrt37-xQCA)，2026-01
- [AI 说：我有智慧，但没有人生](https://mp.weixin.qq.com/s/_jEQ6zRs5Wwj83ljmmVToQ)，2026-03
- [三分天下：为什么 Agent Memory 框架是死路](https://mp.weixin.qq.com/s/bWpka2OzrJFyrbmrecIQUw)，2026-04
- [OpenAI hires OpenClaw creator](https://www.tomshardware.com/tech-industry/openai-hires-genius-openclaw-creator-but-popular-ai-assistant-will-remain-open-source-sam-altman-says-creator-will-work-on-smart-agents-in-new-role)，Tom's Hardware
