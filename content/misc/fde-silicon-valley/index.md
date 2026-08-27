---
title: "Forward Deployed Engineer —— 硅谷版\"交付工程师\""
date: 2025-12-15
authors: [ma-gong]
summary: >
  2025年，硅谷突然掀起了一股Forward Deployed Engineer（FDE）招聘热潮。Open
tags: [软件工程, 工具, 商业]
---

> 原作者：瑞典马工 · [微信公众号转载页](https://mp.weixin.qq.com/s/Lk3rqDJVY-J6UouXXdxkHA)

2025年，硅谷突然掀起了一股Forward Deployed Engineer（FDE）招聘热潮。OpenAI计划在年底前招50个FDE，Anthropic、Databricks、Google DeepMind也全在招。LinkedIn上FDE岗位发布量激增800%，行业媒体把它吹成"AI时代最热门职位"。

我的第一反应是：这不就是我们中国10年前的"交付工程师"吗？驻场实施，售后支持，技术售前 —— 换个洋气的名字，就成了硅谷"创新"？

更有意思的是，我去查了一下这个概念的发源地Palantir。结果发现他们前CFO Colin Anderson公开批评FDE模式是"lighting equity on fire"（点燃股权烧钱），还说有"spectacular pyres of time and treasure and travel expenses that amounted to nothing"（时间、金钱和差旅费的壮观火堆，最后什么都没产出）。

连自己人都看不下去了，怎么还能成为全行业追捧的"创新模式"？

这个故事让我想起了中国的"中台"热潮。2015年阿里巴巴推出中台概念，五年内所有大厂跟进，行业口号是"不做中台就死"。结果2023年，阿里自己放弃了中台战略。

我斗胆预测，Forward Deployed Engineer会是下一个"中台" —— 一个看起来很美，实际上问题重重，最终会被行业抛弃的buzzword。

### FDE到底是什么？皇帝的新衣

我们先看看Palantir官方怎么定义FDE：

> Deltas are part of Business Development, and their mandate is to achieve technical outcomes for our customers. As part of a team that directly supports one customer, a Delta focuses on technology-driven value creation: deploying and customizing Palantir platforms to tackle critical business problems

再看看FDE的日常工作：

> "Most weeks, I spend a couple of days working at the customer premises, some of that time in meetings with technical or business stakeholders, and the rest of the time monitoring, debugging, deploying, or configuring our software for that customer."

翻译成大白话就是：每周去客户现场2-3天，开会、调试、部署、配置软件。回到办公室写点小代码改动，和产品团队开会，处理邮件。

这不就是中国软件行业的"交付工程师"、"驻场实施"、"售后工程师"吗？

金蝶、用友这些中国ERP厂商，都有大量实施顾问。他们通过合作伙伴网络提供实施服务，帮客户部署、配置、定制系统。但你见过金蝶把"ERP实施顾问"包装成"革命性创新岗位"，然后让LinkedIn职位发布量激增800%吗？

没有。因为这就是个正常的岗位，不值得大惊小怪。

我这里提出一个判断标准，姑且称之为"The Spreadsheet Test"：

如果我卖你Excel，你能用。如果我卖你"Excel Platform"，但你需要我的工程师on-site 3天/周才能做表格，我没有产品 —— 我有个非常贵的表格顾问服务。

同理，如果你的"AI平台"、"数据平台"需要permanent embedded engineers才能运行，你卖的不是产品，是工程师的时间。

### 数据说话：Palantir的真实面目

让我们看看数据。Palantir有个历史事实很少有人提：直到2016年，这家"软件公司"的FDE数量超过了软件工程师数量。

这是哪门子的软件公司？

2024年的数据更有意思。Palantir总员工3,936人，其中工程人员1,383人（占44%）。但他们现在不公开FDE和普通软件工程师的比例了。为什么不公开？我猜是因为这个比例说出来会让人怀疑他们到底是不是软件公司。

再看收入构成。2024年Palantir总收入\$2.9B，其中政府客户占55%（\$1.57B），商业客户占45%（\$1.30B）。更关键的是趋势：2019年到2024年，政府收入占比从46.5%增长到55%。

注意了，他们一边对外宣传商业市场的巨大成功，一边实际上越来越依赖政府合同。这说明什么？说明在正常的商业市场，FDE模式很难成功。

还有个有意思的数字：FDE的薪资中位数是\$221K，普通软件工程师是\$195K。看起来FDE更值钱？实际上只高13%，但要承受：

- 每周3-4天在客户现场
- 大量差旅
- Glassdoor上员工评价"Bad work-life balance"
- 开发模式被内部人描述为"jungle combat: quick-and-dirty code"

13%的溢价，换来的是生活质量大幅下降和技术债务累积。这买卖值吗？

最精彩的是Palantir前CFO Colin Anderson的评价。他说FDE模式在某些市场有效，在其他市场则是"lighting equity on fire"。他观察到"overlapping and wasted work, multiple teams on similar problems"（重复浪费的工作，多个团队在解决类似问题），结果是"many failures – spectacular pyres of time and treasure and travel expenses that amounted to nothing"（许多失败 —— 时间、金钱和差旅费的壮观火堆，最后什么都没产出）。

连自己的CFO都这么说，你还觉得这是个好模式？

### 为什么FDE只能在高腐败行业生存？

看到这里你可能会问：既然FDE模式这么有问题，为什么Palantir还能拿到这么多合同，市值还这么高？

答案很简单：revolving door（旋转门）。

2022年，美国前20大防务承包商雇佣了672名刚从Pentagon退休的官员。前参谋长联席会议主席Joseph Dunford退休5个月后就加入了Lockheed Martin董事会。美国国防部自己的审计发现，防务承包商通过腐败和浪费实现了40-50%的利润率。

这就是美国国防采购的现实：承包商给Pentagon官员许诺高薪工作，官员在位时给承包商慷慨的合同，退休后去承包商那里拿高薪。Operation Illwind是美国历史上最大的国防采购腐败案，起诉了60多名承包商、顾问和政府官员，包括Pentagon的助理部长和海军副助理部长。

Palantir在这个生态系统里如鱼得水。2003年成立时，传统VC都拒绝投资，是CIA的风投部门In-Q-Tel成了早期投资人。更绝的是，情报机构不只是投钱，还"帮助设计产品"，和Palantir工程师"iterative collaboration"了近三年。

换句话说，CIA出钱，CIA设计产品，然后CIA成为客户。这是完美的政府承包商模式。

我朋友说过一个很生动的比喻。他说："中国最强关系华为公司，也不能对着中石油说'我他妈的也不知道能给你做什么，我先派个fde入场，查看你的数据，占用你的时间，然后做个mvp给你看看，你到时候再决定。当然，你第一天就要付费'。这不神经病么。"

为什么在中国这是神经病，在美国国防市场就能行得通？因为美国国防采购有足够的腐败空间，让这种模式成为可能。

在正常的商业市场，甲方要明确的交付物，要可比较的报价，要能更换供应商。FDE模式本质上是lock-in by design（设计性锁定） —— 一旦你的团队依赖了Palantir的FDE，你就很难换掉他们。

这在国防市场可以，因为决策者不花自己的钱，也不用对纳税人负责。但在正常商业市场，CFO会算账的。

### 当FDE遇到真实世界：NHS惨案

让我们看看FDE模式在相对透明的市场表现如何。

2023年11月，英国NHS（国家医疗服务体系）给Palantir签了一个7年、£330 million的合同，建设全国数据平台。这是个大单，Palantir肯定很开心。

一年后，实际情况如何？

调查发现，215家NHS医院中，只有不到25%真正在使用Palantir的系统。很多医院信托直接拒绝部署，称其为"step backwards on existing systems"（比现有系统还退步）。

合同本身也很可疑。586页合同中，416页被redacted（涂黑）。数据保护条款在合同签署后还在"subject to commercial negotiation"（商业谈判中）。患者无法opt-out（退出）数据收集。

这就是FDE模式在透明市场的真实表现：有政治关系能拿到合同，但产品垃圾还是垃圾，用户不买账就是不买账。

我对此毫不意外。一个需要permanent embedded engineers才能运行的"平台"，怎么可能scale到215家医院？每家医院都派FDE驻场？成本谁来承担？

这个案例完美说明了FDE模式的根本缺陷：它不是一个可扩展的商业模式。

### "中台"的美国孪生兄弟

说到这里，我必须讲讲中国的"中台"（zhongtai）故事，因为它和FDE简直是一模一样的剧本。

2015年，阿里巴巴推出"中台"概念。所谓中台，是"enterprise-level capability reuse platform"（企业级能力复用平台）。听起来很美对吧？

结果五年内，腾讯、百度、字节、滴滴、京东、美团全都跟进，搞自己的中台。行业口号变成了："不做中台就死。"Gartner 2020年把中台列入"Peak of Inflated Expectations"（过度膨胀的期望顶峰）。

但问题来了。连中台的定义都说不清楚。行业报告写："Even today, we don't even have a clear definition for what Zhong Tai is"（即使到今天，我们都没有中台的清晰定义）。

2023年，故事的高潮来了：阿里巴巴CEO张勇在公开信中说要把中台"made light and thin"（轻量化）。翻译成大白话就是：中台战略搞不下去了，要放弃了。

推广中台的阿里巴巴，自己放弃了中台。

现在看看FDE：

| 特征       | 中台 (Zhongtai)   | FDE                            |
|------------|-------------------|--------------------------------|
| 定义清晰度 | "没有清晰定义"    | "和中台一样混乱"（我朋友原话） |
| 推广者     | 阿里巴巴          | Palantir                       |
| 传播速度   | 5年内所有大厂跟进 | 2025年岗位激增800%             |
| 内部批评   | 2023年CEO承认失败 | CFO批评"烧钱"                  |
| Hype Cycle | Peak → 幻灭       | 正在Peak                       |

这个parallel（平行）简直完美。两个都是概念模糊的buzzword，两个都是大厂推广后全行业跟风，两个都是推广者自己最后放弃。

中国人看"中台"热潮，和美国人看FDE热潮，心态应该是一样的：这个我见过。

我朋友还有个讽刺性的观察："中国军工信息化公司又没有把军代表岗位取个backward deployed manager，然后宣传这是世界先进模式。"

他的意思是：每个行业都有on-site的角色，这不稀奇。只有在hype-driven（炒作驱动）的环境里，这些普通岗位才会被rebranded（重新包装）为"革命性创新"。

### 产品 vs. 咨询公司：一个根本性问题

让我们回到最根本的问题：Palantir到底是软件公司还是咨询公司？

软件产品的定义是什么？我认为至少要满足以下条件：

1.  客户可以相对独立地使用
2.  不需要供应商的permanent staff
3.  可以通过partner网络或客户IT team部署
4.  有清晰的功能边界和API

看看Kingdee（金蝶）和UFIDA（用友）。他们是中国最大的ERP厂商，提供SaaS模式，按用户数按月收费。实施通过授权合作伙伴完成，不需要金蝶的工程师permanent on-site。这是个正常的软件产品商业模式。

再看Microsoft Office、Salesforce、AWS。客户可以self-service，有documentation，有API，有partner生态。供应商提供产品和平台，客户和partners负责实施和运维。

Palantir呢？行业报告说客户"become dependent on company's employees"（依赖公司员工）。FDE直接commit fixes to the platform。每个客户的部署可能是不同的fork。

这还是产品吗？

我前面提的Spreadsheet Test就是要问：如果你的"平台"需要permanent on-site engineers才能使用，你卖的是产品还是人力？

对比一下传统防务承包商：

- Lockheed Martin卖F-35战斗机：交付后能飞，有维护手册
- Boeing卖787客机：交付后能用，航空公司可以自己运营
- Raytheon卖导弹防御系统：安装后能操作，有培训和文档

Palantir卖"数据平台"：需要permanent FDE team on-site，否则玩不转。

本质区别在哪？硬件公司卖的是产品，Palantir卖的是工程师的时间 + 一个GitHub repo。

如果FDE真的只是短期实施，帮客户onboarding，那还说得过去。但Palantir的模式是permanent embedded。这就不是实施，是outsourcing（外包）了。

换句话说，Palantir的商业模式更接近Accenture、Deloitte这些咨询公司，而不是Microsoft、Oracle这些软件公司。但他们的市值是按软件公司估的，这才是问题所在。

### FDE病毒正在传播

讽刺的是，就在Palantir的FDE模式问题重重的时候，硅谷其他公司正在疯狂复制这个模式。

OpenAI在2025年初成立了FDE团队，计划年底前招到50人。他们的FDE职责是"embed with Fortune 500s to actually apply generative AI, fine-tuning models, building new agentic workflows, and proving the business case"。

注意那个词："proving the business case"（证明商业价值）。这不就是售前吗？

Anthropic把FDE叫"Applied AI Engineers"，计划5倍扩张团队。ElevenLabs、Databricks、Salesforce、Google DeepMind全在招FDE。

结果就是LinkedIn上FDE职位发布量激增800%。行业媒体欢呼"AI时代最热门职位"。

我看到这个场景，脑子里只有一个念头：这是"中台"重演。

2015年阿里推中台，2020年Gartner说peak hype，2023年阿里放弃。从Peak到幻灭，8年时间。

2016年Palantir的FDE比SWE还多，2024年自己CFO批评烧钱，2025年全行业跟风。这个故事会怎么结束？

我有两个猜测：

**乐观猜测**：OpenAI、Anthropic这些公司会吸取Palantir的教训，把FDE做成短期的pre-sales和onboarding角色，而不是permanent embedded。这样FDE模式能够持续。**悲观猜测**（也是我更倾向的）：AI行业正在重复"中台"的错误。把一个老掉牙的交付模式包装成"创新"，全行业groupthink跟风，3-5年后发现这个模式根本不scalable，然后集体放弃。

为什么我更倾向悲观猜测？因为：

1.  Palantir自己的CFO都批评FDE烧钱，为什么其他公司觉得自己能做得更好？
2.  NHS的25%采用率说明这个模式在透明市场很难成功，为什么AI公司觉得企业市场会不一样？
3.  如果这个模式真的有效，为什么Palantir越来越依赖政府合同，而不是商业市场？

800%的增长不代表validation（验证），可能只是groupthink（集体思维）。记住，"中台"在中国也是所有大厂都跟进，最后还不是推广者自己放弃？

### 我见过这个电影：打假启示

作为在中国云计算领域打假多年的老兵，我对FDE模式持深度怀疑。我见过太多次类似的模式了。

我朋友说得好："我在中国云计算打假打了不少南郭先生，去美国AI届试一下能不能弄点声音出来。"

南郭先生有什么共同特征？

1.  **概念模糊，定义不清**：问他到底是什么，说不清楚，只能用buzzword堆砌
2.  **大厂背书，声势浩大**：有大公司推，有媒体吹，有投资人捧
3.  **理论上听起来很美**：画的饼很大，但细节经不起推敲
4.  **实践中问题重重**：真正去用，发现到处是坑
5.  **最终推广者自己放弃**：风向一变，当初吹得最厉害的人跑得最快

FDE完美符合这个pattern：

我预测，3-5年后回看，FDE会和"中台"一样，成为一个行业笑话。到时候会有人写文章说："还记得2025年全行业都在招FDE吗？那时候我们真是太naive了。"

### 结论：美国的中科红旗

我朋友有个很精辟的比喻：Palantir是"美国的中科红旗"。

中科红旗是什么？中国的Linux发行版，产品页挂国旗，靠政府关系拿合同，技术平平，最终政策风向一变就倒闭了。典型的"patriotic vaporware"（爱国蒸汽软件）。

Palantir也是：产品页挂美国国旗，靠CIA关系起家，靠Pentagon合同生存，技术谈不上有多先进（NHS用户说"step backwards"）。唯一的区别是Palantir的political connection更深，所以还能继续玩下去。

但这个模式能持续多久？我朋友说："如果川普下台的时候，他的股票还有这么高，我就做空他。"

我不知道Palantir的未来如何，但我知道FDE模式不是AI行业的未来。

给AI公司（OpenAI、Anthropic们）的建议：

1.  **要么真正productize**：学Kingdee用partner网络，不要自己养FDE大军
2.  **要么承认你是咨询公司**：按hourly rate收费，不要按软件license收费
3.  **别走国防承包商的路**：那条路需要极深的政治关系，你们没有

给Palantir的建议：继续做美国的金蝶 + 中科红旗吧，但别指望正常市场接受这套。NHS已经证明了：在透明市场，FDE模式玩不转。

最后，我想说：Forward Deployed Engineer不是什么创新，就是传统的交付工程师、驻场实施，换了个洋气的名字罢了。如果你真的有好产品，客户能自己用，或者通过partners部署。如果你的"平台"离不开permanent on-site team，说明你的产品还没做好，或者压根就不是个产品。

换句话说，Forward Deployed Engineer是胡扯，Delivery Engineer倒可能是朴实真理。只不过后者拿不到VC的钱，也上不了LinkedIn的热门职位榜。

------------------------------------------------------------------------

作为见证过中国云计算和"中台"兴衰的老兵，我对FDE持深度怀疑。这个pattern我见过太多次了：概念火爆 → 全行业跟风 → 问题暴露 → 推广者放弃。

有在Palantir或OpenAI做FDE的朋友，欢迎在评论区打脸，告诉我为什么FDE这次不一样。有认同我观点的同好，欢迎转发，让更多人看穿这个硅谷版"交付工程师"的真面目。

我个人认为，3-5年后，FDE会和"中台"一样，成为一个行业笑话。到时候我们再来复盘，看看谁说对了。

有兴趣讨论这个话题的朋友，欢迎在公众号留言。我尤其期待来自FDE从业者的具体反驳 —— 用数据和案例说话，而不是buzzword和情怀。
