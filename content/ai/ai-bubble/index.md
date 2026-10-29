---
title: "AI 泡沫将如何破裂？"
date: 2026-10-17
authors: [vonng]
summary: >
  AI 的技术能力、应用扩散与金融资本并不同步。需求窄而深，溢价、信用与时间却出现三重错配：泡沫会如何出清，留下的技术红利又将归谁所有？
tags: [AI, 技术评论, 商业]
aliases: [/ai/buble-break/]
---

> 本文 AI 含量 70%，源于老冯与 Claude、Gemini、ChatGPT 的四方探讨，汇总成文，数据截至 2026 年 10 月 17 日，不构成任何投资建议。

站在 2026 年 10 月的节点上环顾四周，任何一个既在一线写代码、又看企业资产负债表的人，都会感受到一种强烈的精神分裂。

一面是沸腾到失去地心引力的资本奇观：北美四大云巨头将今年的资本开支（CapEx）指引一路推高至约 7250 亿美元[^1]，比去年再涨 77%。美国银行测算，这笔庞大的开支将吞噬巨头们 94% 的经营现金流[^2]，甚至让昔日印钞机一样的 Alphabet 在今年二季度录得约 -59 亿美元的自由现金流[^3]——这是它自 2004 年上市以来的头一回。一级市场已经装不下这头吞金巨兽了：继 SpaceX 今年 6 月募走 750 亿美元后，Anthropic 正以 1.8 万亿到 2 万亿美元的目标估值冲刺 IPO[^4]，而死守 1 万亿美元估值底线的 OpenAI 则已确认将上市窗口推迟至 2027 年[^5]。

另一面却是冷清得令人不安的现实世界。根据美国人口普查局（BTOS）的抽样调查[^6]，今年 7 月全美在业务中真正用上 AI 的企业占比只有 21.7%（8 月小幅升至 23.2%）；而在那近八成没用 AI 的企业里，高达 61.6% 的老板直言“这东西跟我的业务毫无关系”。消费端的数据同样骨感：据 ING（荷兰国际集团）估算[^7]，全美只有 2% 到 3% 的家庭在为 AI 订阅掏钱，大众消费端的浅层订阅根本包不住万亿基建的折旧与电费。

[AI 深透率，可能没那么高](/ai/funnel/)

一边是按“整个经济体彻底重写”来定价的万亿基建，另一边是步履蹒跚的现实渗透。很多人的感觉会是：**AI 泡沫马上要破了，因为根本没那么多真实需求。**

但当你把近几个季度最硬的财务账本、信贷利差和路由流量全部摊在桌面上，做完几轮近乎残酷的对抗式压力测试后，这个直觉其实 **只对了一半**。

金融资本曲线确实已经站上了顶部的高危平台期，但说“没有需求”是错的。如果这一轮 AI 狂潮迎来大出清，它绝不会死于需求消失，而是会死于三道结构性裂痕的共振：**溢价错配、信用错配、以及时间错配。**

## 太长不看

- **我们在哪：** 技术能力曲线仍在陡升，应用扩散曲线“窄而深”，金融资本曲线已处在顶部平台。

- **怎么出清：** 大概率不是一次性崩盘，而是**两段式出清**——2027 年上半年先经历“估值压缩”，2027 年下半年到 2028 年再经历“产能落地与信用出清”。

- **第一张骨牌：** 绝不是云巨头主动砍 CapEx，排在最前面的是**新股供给洪水、外围高杠杆信用断裂、以及前沿溢价被开源刺穿**。

- **概率分布：** 两段式出清（45%）、硬着陆（25%）、1998 式泡沫延续（15%）、外生供应链断裂（15%）。

- **终局底线：** 无论走哪条路，Token 都会再降一个数量级，行业扩散都会按“可验证性”的顺序推进，一人公司（OPC）都会变多。各条路径真正的区别，是**技术剩余价值最后归谁所有**。

## 一、拆开三条不同步的曲线

讨论 AI 在不在泡沫顶点，最大的误区是把所有事情揉成一条线。

Gartner 的技术成熟度曲线描述的是**大众心理预期**；而演化经济学家卡萝塔·佩蕾丝（Carlota Perez）在《技术革命与金融资本》里划分的“安装期（Installation）”与“展开期（Deployment）”，描述的是**金融资本与生产资本的权力交接**。如果把今天 AI 的局势拆解开，你会看到三条完全不同步的曲线：

```echarts {height="710px" full=true class="ai-bubble-curves"}
baseOption:
  animation: false
  backgroundColor: transparent
  aria:
    enabled: true
    description: 三条独立尺度的概念曲线。2026 年 10 月，技术能力仍在陡峭上行，应用扩散窄而深，金融资本已到高位平台。圆点标出当前判断；虚线表示后续可能路径，不代表实测数据或定量预测。金融资本的延续与调整路径可通过图例切换。
  tooltip:
    trigger: item
    confine: true
    extraCssText: 'max-width: 260px; white-space: normal; line-height: 1.6;'
    textStyle:
      fontSize: 14
  title:
  - text: 技术能力 · 仍在陡峭上行
    subtext: 模型上限持续抬升
    left: 12
    top: 8
    textStyle:
      fontSize: 16
    subtextStyle:
      fontSize: 12
  - text: 应用扩散 · 窄而深，仍待铺开
    subtext: 少数场景深入，全社会覆盖仍在早期
    left: 12
    top: 244
    textStyle:
      fontSize: 16
    subtextStyle:
      fontSize: 12
  - text: 金融资本 · 高位平台，错配累积
    subtext: 定价领先于真实扩散
    left: 12
    top: 480
    textStyle:
      fontSize: 16
    subtextStyle:
      fontSize: 12
  legend:
    data:
    - 延续
    - 调整
    right: 12
    top: 525
    itemWidth: 24
    itemHeight: 12
    textStyle:
      fontSize: 12
  grid:
  - left: 44
    right: 24
    top: 84
    height: 116
    width: auto
  - left: 44
    right: 24
    top: 320
    height: 116
    width: auto
  - left: 44
    right: 24
    top: 556
    height: 116
    width: auto
  xAxis:
  - type: value
    gridIndex: 0
    min: 0
    max: 100
    name: 演进阶段 →
    nameLocation: middle
    nameGap: 14
    nameTextStyle:
      fontSize: 11
      padding: 0
      align: center
    axisLabel:
      show: false
    axisTick:
      show: false
    splitLine:
      show: false
    axisLine:
      show: true
      lineStyle:
        opacity: 0.4
  - type: value
    gridIndex: 1
    min: 0
    max: 100
    name: 演进阶段 →
    nameLocation: middle
    nameGap: 14
    nameTextStyle:
      fontSize: 11
      padding: 0
      align: center
    axisLabel:
      show: false
    axisTick:
      show: false
    splitLine:
      show: false
    axisLine:
      show: true
      lineStyle:
        opacity: 0.4
  - type: value
    gridIndex: 2
    min: 0
    max: 100
    name: 演进阶段 →
    nameLocation: middle
    nameGap: 14
    nameTextStyle:
      fontSize: 11
      align: center
      padding: 0
    axisLabel:
      show: false
    axisTick:
      show: false
    splitLine:
      show: false
    axisLine:
      show: true
      lineStyle:
        opacity: 0.4
  yAxis:
  - type: value
    gridIndex: 0
    min: 0
    max: 110
    name: 能力水平
    nameGap: 12
    nameTextStyle:
      fontSize: 11
    axisLabel:
      show: false
    axisTick:
      show: false
    splitLine:
      show: false
    axisLine:
      show: true
      lineStyle:
        opacity: 0.4
  - type: value
    gridIndex: 1
    min: 0
    max: 110
    name: 覆盖广度
    nameGap: 12
    nameTextStyle:
      fontSize: 11
    axisLabel:
      show: false
    axisTick:
      show: false
    splitLine:
      show: false
    axisLine:
      show: true
      lineStyle:
        opacity: 0.4
  - type: value
    gridIndex: 2
    min: 0
    max: 110
    name: 定价水平
    nameGap: 12
    nameTextStyle:
      fontSize: 11
    axisLabel:
      show: false
    axisTick:
      show: false
    splitLine:
      show: false
    axisLine:
      show: true
      lineStyle:
        opacity: 0.4
  series:
  - name: 技术能力
    type: line
    xAxisIndex: 0
    yAxisIndex: 0
    smooth: 0.35
    showSymbol: false
    symbol: circle
    lineStyle:
      width: 3
      type: solid
      opacity: 1
    itemStyle:
      color: '#507f9b'
    tooltip:
      formatter: 技术能力｜2026 年 10 月<br/>仍在陡峭上行，模型上限持续抬升。<br/>技术进步可跨越资本周期。
    emphasis:
      focus: series
    data:
    - - 0
      - 1
    - - 14
      - 2
    - - 28
      - 5
    - - 42
      - 11
    - - 54
      - 21
    - - 64
      - 36
    - - 72
      - 52
    markPoint:
      symbol: circle
      symbolSize: 16
      label:
        show: true
        formatter: 现在
        position: top
        distance: 10
        fontSize: 13
      data:
      - name: 2026 年 10 月
        coord:
        - 72
        - 52
      tooltip:
        formatter: 技术能力｜2026 年 10 月<br/>仍在陡峭上行，模型上限持续抬升。<br/>技术进步可跨越资本周期。
  - name: 技术能力：可能路径
    type: line
    xAxisIndex: 0
    yAxisIndex: 0
    smooth: 0.35
    showSymbol: false
    symbol: circle
    lineStyle:
      width: 3
      type: dashed
      opacity: 0.7
    itemStyle:
      color: '#507f9b'
    tooltip:
      formatter: 技术能力｜可能路径<br/>能力上限继续抬升。<br/>虚线为概念推演，不是定量预测。
    emphasis:
      focus: series
    data:
    - - 72
      - 52
    - - 82
      - 78
    - - 90
      - 100
  - name: 应用扩散
    type: line
    xAxisIndex: 1
    yAxisIndex: 1
    smooth: 0.35
    showSymbol: false
    symbol: diamond
    lineStyle:
      width: 3
      type: solid
      opacity: 1
    itemStyle:
      color: '#4f897a'
    tooltip:
      formatter: 应用扩散｜2026 年 10 月<br/>少数场景使用很深，全社会覆盖仍在早期。<br/>当前特征是“窄而深”。
    emphasis:
      focus: series
    data:
    - - 0
      - 1
    - - 12
      - 2
    - - 24
      - 7
    - - 34
      - 20
    markPoint:
      symbol: diamond
      symbolSize: 16
      label:
        show: true
        formatter: 现在
        position: top
        distance: 10
        fontSize: 13
      data:
      - name: 2026 年 10 月
        coord:
        - 34
        - 20
      tooltip:
        formatter: 应用扩散｜2026 年 10 月<br/>少数场景使用很深，全社会覆盖仍在早期。<br/>当前特征是“窄而深”。
  - name: 应用扩散：可能路径
    type: line
    xAxisIndex: 1
    yAxisIndex: 1
    smooth: 0.35
    showSymbol: false
    symbol: diamond
    lineStyle:
      width: 3
      type: dashed
      opacity: 0.7
    itemStyle:
      color: '#4f897a'
    tooltip:
      formatter: 应用扩散｜可能路径<br/>从少数场景向更多行业铺开。<br/>扩散需要补齐工程沙箱与制度配套。
    emphasis:
      focus: series
    data:
    - - 34
      - 20
    - - 50
      - 46
    - - 65
      - 73
    - - 80
      - 91
    - - 100
      - 96
  - name: 金融资本
    type: line
    xAxisIndex: 2
    yAxisIndex: 2
    smooth: 0.35
    showSymbol: false
    symbol: roundRect
    lineStyle:
      width: 3
      type: solid
      opacity: 1
    itemStyle:
      color: '#aa8746'
    tooltip:
      formatter: 金融资本｜2026 年 10 月<br/>处在高位平台，定价领先于真实扩散。<br/>错配不断累积，调整节奏仍有分歧。
    emphasis:
      focus: series
    data:
    - - 0
      - 1
    - - 12
      - 10
    - - 22
      - 38
    - - 30
      - 70
    - - 38
      - 87
    - - 45
      - 94
    - - 48
      - 93
    markPoint:
      symbol: roundRect
      symbolSize: 16
      label:
        show: true
        formatter: 现在
        position: top
        distance: 10
        fontSize: 13
      data:
      - name: 2026 年 10 月
        coord:
        - 48
        - 93
      tooltip:
        formatter: 金融资本｜2026 年 10 月<br/>处在高位平台，定价领先于真实扩散。<br/>错配不断累积，调整节奏仍有分歧。
  - name: 延续
    type: line
    xAxisIndex: 2
    yAxisIndex: 2
    smooth: 0.35
    showSymbol: false
    symbol: circle
    lineStyle:
      width: 3
      type: dotted
      opacity: 0.7
    itemStyle:
      color: '#aa8746'
    tooltip:
      formatter: 金融资本｜延续路径<br/>高位定价继续维持，大顶推迟。<br/>这是一种可能路径，不是确定结局。
    emphasis:
      focus: series
    data:
    - - 48
      - 93
    - - 70
      - 96
    - - 100
      - 100
  - name: 调整
    type: line
    xAxisIndex: 2
    yAxisIndex: 2
    smooth: 0.35
    showSymbol: false
    symbol: circle
    lineStyle:
      width: 3
      type: dashed
      opacity: 0.7
    itemStyle:
      color: '#aa8746'
    tooltip:
      formatter: 金融资本｜调整路径<br/>资本定价回落，出清后逐步修复。<br/>技术进步不等于资本回报。
    emphasis:
      focus: series
    data:
    - - 48
      - 93
    - - 56
      - 76
    - - 64
      - 38
    - - 74
      - 24
    - - 86
      - 30
    - - 100
      - 47
media:
- query:
    maxWidth: 640
  option:
    title:
    - text: 技术能力 · 仍在陡峭上行
      subtext: 模型上限持续抬升
      left: 12
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 12
    - text: 应用扩散 · 窄而深，仍待铺开
      subtext: 少数场景深入，全社会覆盖仍在早期
      left: 12
      top: 244
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 12
    - text: 金融资本 · 高位平台，错配累积
      subtext: 定价领先于真实扩散
      left: 12
      top: 480
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 12
    grid:
    - left: 44
      right: 24
      top: 84
      height: 116
      width: auto
    - left: 44
      right: 24
      top: 320
      height: 116
      width: auto
    - left: 44
      right: 24
      top: 556
      height: 116
      width: auto
    legend:
      data:
      - 延续
      - 调整
      right: 12
      top: 525
      itemWidth: 24
      itemHeight: 12
      textStyle:
        fontSize: 12
    xAxis:
    - type: value
      gridIndex: 0
      min: 0
      max: 100
      name: 演进阶段 →
      nameLocation: middle
      nameGap: 14
      nameTextStyle:
        fontSize: 11
        padding: 0
        align: center
      axisLabel:
        show: false
      axisTick:
        show: false
      splitLine:
        show: false
      axisLine:
        show: true
        lineStyle:
          opacity: 0.4
    - type: value
      gridIndex: 1
      min: 0
      max: 100
      name: 演进阶段 →
      nameLocation: middle
      nameGap: 14
      nameTextStyle:
        fontSize: 11
        padding: 0
        align: center
      axisLabel:
        show: false
      axisTick:
        show: false
      splitLine:
        show: false
      axisLine:
        show: true
        lineStyle:
          opacity: 0.4
    - type: value
      gridIndex: 2
      min: 0
      max: 100
      name: 演进阶段 →
      nameLocation: middle
      nameGap: 14
      nameTextStyle:
        fontSize: 11
        align: center
        padding: 0
      axisLabel:
        show: false
      axisTick:
        show: false
      splitLine:
        show: false
      axisLine:
        show: true
        lineStyle:
          opacity: 0.4
- query:
    minWidth: 641
  option:
    title:
    - text: 技术能力曲线
      subtext: 仍在陡峭上行
      left: 3%
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 13
    - text: 应用扩散曲线
      subtext: 窄而深，仍待铺开
      left: 36%
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 13
    - text: 金融资本曲线
      subtext: 高位平台，错配累积
      left: 69%
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 13
    grid:
    - left: 5%
      right: auto
      width: 26%
      top: 100
      height: 220
    - left: 38%
      right: auto
      width: 26%
      top: 100
      height: 220
    - left: 71%
      right: auto
      width: 26%
      top: 100
      height: 220
    legend:
      top: 352
      right: 3%
    xAxis:
    - nameLocation: middle
      nameGap: 14
      nameTextStyle:
        padding: 0
        align: center
    - nameLocation: middle
      nameGap: 14
      nameTextStyle:
        padding: 0
        align: center
    - nameLocation: middle
      nameGap: 14
      nameTextStyle:
        padding: 0
        align: center
```

*概念示意，不按比例；各图演进尺度独立。圆点为 2026 年 10 月的阶段判断，虚线为可能路径。技术进步 ≠ 资本回报。悬停查看说明，点击“延续 / 调整”图例可切换路径。*

1. **技术能力曲线：仍在陡峭攀升。** 从长链条推理到复杂工具调用，模型的智力上限依然在按季度迭代，远没到技术停滞的时候。

2. **应用扩散曲线：极度“窄而深”。** 全社会渗透率只有两成出头，但真实的商业收入像一根钢针一样，死死扎在少数垂直场景里。

3. **金融资本曲线：已处在安装期最末端的顶部平台。** 美联储在 9 月全票通过加息 25 个基点至 3.75%–4.00%[^8]（三年来首次加息），超级独角兽排队向二级市场派发筹码，基建融资从烧自有现金转向表外加杠杆——历次技术周期见顶的晚期信号，基本都已经亮灯。

**所谓泡沫破裂，从来不是技术能力归零，而是“金融资本曲线”和“应用扩散曲线”之间的巨大落差被强行拉平。** 2001 到 2002 年互联网泡沫破灭时，全球互联网流量照样在高速增长，崩掉的只是透支了未来十年预期的资本定价。

## 二、需求没有不足，只是“窄得要命”

说“需求不足”会被数据直接打脸，看一眼 10 月 14 日 Anthropic 投资者会上流出的财务数字[^9]就明白了（按英国《金融时报》披露的未经审计口径，目前公开版 S-1 招股书尚未发布）：它今年一季度营收约 48 亿美元，二季度飙到 115 亿美元，三季度直接冲上 **168 亿美元**——单季收入就已经超过 2025 年全年的 3.6 倍。同时它向投资人披露，三季度调整后营业利润率已达约 11%（不含股权激励），经营现金流转正，每花 1 美元算力能换回 1.70 美元收入。

为什么普通人觉得身边没几个人深度付费，模型厂却能赚到几百亿美金？因为“数人头”的口径在 Agent 时代已经彻底失效了。

算力消耗的单位不是“人”，而是 Token。一个在后台 24 小时跑循环的 Coding Agent，一天烧掉的 Token 顶得上几百个聊天框里的普通白领。需求的真正上限是“能被可靠自动化的任务价值”，而不是“人口数量乘以 20 美元订阅费”。

真正要命的问题不在于需求是假的，而在于**需求极度偏科**。根据 Menlo Ventures 统计，企业在 AI 编程上的支出有高达 54% 流向了 Anthropic 一家[^10]，OpenAI 仅占 21%。这让整体月活用户规模远小于 ChatGPT 的 Anthropic，在年化收入（ARR）上反而实现了反超。

### 为什么偏偏只有“写代码”成了超级楔子？

如果从工程第一性原理出发，我们可以把 AI 在各行业的扩散速度压成一个非常冷酷的公式：

**扩散速度** ≈ **可验证性** × **可逆性** × **责任可归属**

软件工程之所以能跑通百亿美金的商业闭环，是因为它是人类社会里少有的、把这三项指标全部拉满的温室：**确定性的编译器与自动化测试集负责“低成本验证”，Git 与沙箱环境负责“近乎零成本的回滚（Reversibility）”，最后敲下回车合并代码的程序员负责“背锅”。** Agent 在沙箱里写废一万行代码，测试跑不通直接回滚重来，不会在现实世界里造成一分钱坏账。

但企业世界的另外八成呢？打款、发货、做手术、签合同，这三项全缺。

搞基础架构的人都知道，容错原语并不是今天才发明的：数据库早就有了事务（Transaction）、回滚、快照、时间点恢复（PITR）和分支；财务系统也有复式记账、自动对账与双人复核。**真正缺失的只有两样东西：一是与不可逆物理世界之间的防呆接口，二是法律、保险与监管层面的责任认定体系。**

这意味着，AI 往非编程领域的扩散绝不是“不可能”，而是必须一个行业一个行业地补齐工程沙箱与制度配套。顺着这个公式往下排，下一批能被撑开的楔子必然是：**数据分析与 SQL、IT 与安全运维、带人工升级兜底的客服、以及后台财务对账**；而法律、医疗与实体供应链注定排在最后。这个补课的速度是以“年”为单位的，绝不可能按华尔街期待的“季度”去爆发。

### 编程这把楔子，开始变钝了吗？

更微妙的信号已经浮出水面。哪怕在最锋利的编程楔子上，Anthropic 三季度的环比增速也从二季度的约 140% 降到了约 46%[^11]，单季净增美元收入（约 53 亿美元）首次低于上一季度（约 67 亿美元）。

客观地说，减速的原因并不单一。据《金融时报》报道，Anthropic 向投资人解释称，“蒸馏”（即竞争对手调用其模型输出来训练自家模型）带来的收入原本占到总营收的 5% 到 7%[^12]，而在三季度公司收紧风控后，这部分收入被大幅压缩（此前 Anthropic 还曾单方面指控，与阿里千问团队相关的操作者在 4 月 22 日至 6 月 5 日间通过近 2.5 万个虚假账号与 Claude 进行了约 2880 万次交互[^13]）。再加上算力受限、API 降价以及客户换用更便宜的模型，不能简单把三季度放缓等同于“需求见顶”。

但账面上的压力是实打实的：三季度 168 亿美元的收入折合年化约 670 亿美元，且公司自 7 月底披露 650 亿美元年化收入（Run-rate）[^14] 后便未再更新这一口径；而投资人目前对它年底的年化收入预期高达 1000 亿至 1100 亿美元[^15]。要想跨过这道坎，四季度必须交出一份陡峭的再加速答卷。

老冯觉得，[个人秘书助理 Agent](/ai/secretary-era/) 能否跨越鸿沟，被大众所接受，可能是问题的关键。否则，少量深度使用的头部蹬车用户，难以支撑起这么大的故事。

## 三、三重错配：溢价、信用与时间的绞索

把“窄楔子”和“万亿基建”放在一起看，当前 AI 市场的脆弱性就暴露无遗了。它集中体现在三重错配上：

### 1. 溢价错配：撕裂的 Token 市场

很多多头喜欢拿“杰文斯悖论”说事：推理越便宜，用量越暴涨，总收入反而更高。这话只说对了一半，因为今天的 Token 市场已经彻底撕裂成了两层：

**大宗通用层（Commodity Layer）正在经历价格坍塌。** 在开发者路由平台 OpenRouter 上，自今年 2 月起，中国开源模型每周都拿下美国企业三成以上的 Token 用量；到 7 月中旬峰值时，中国模型的份额达到 46.4%，反超美国本土模型的 35.7%[^16]。原因极其简单粗暴——便宜 60% 到 90%。DeepSeek V4 Flash 每百万输入 Token 仅售 0.14 美元，不到 GPT-5.5（5 美元）的三十六分之一；旧金山 AI 初创公司 Lindy 将工作流从 Claude 切过去后，推理成本直接砍掉了 90%[^17]。（当然需要补一句：OpenRouter 代表的是开发者路由流量，并不等于全部企业市场。Anthropic 在 OpenRouter 上的 Token 份额只有一成出头，但在整体企业市场的收入份额却远高于此。换句话说，**中国模型赢了量，西方头部实验室目前依然赢着钱。**）

**前沿闭源层（Frontier Layer）还在靠能力代差死守溢价。** 上半年头部闭源厂商甚至提价约 12%，对冲了开源模型拉低的均价。Anthropic 与 OpenAI 合计约三万亿美元的预期估值，全部押在“前沿溢价不会破”这个假设上。**在这里，廉价开源模型只是放大器，真正致命的引信是“前沿能力进步放缓”。** 只要前沿模型还能在长链条复杂 Agent 上保持代差，加上美国国会对中国模型的审查与地缘围栏，就能在欧美政企市场护住一部分闭源溢价；但一旦能力曲线斜率放缓、开源在半年内追平，前沿溢价防线就会迅速松动。

### 2. 信用错配：不是恐慌，而是信用正在变贵

当自有现金流被吃干抹净后，算力基建正在演变成一场精巧的“表外金融工程”。

最典型的样本是 10 月 16 日曝光的 600 亿美元“北极星计划（Project North Star）”[^18]：为了购买约 1.5 吉瓦的谷歌 TPU 算力，又不把债务直接堆在 Anthropic 自己的资产负债表上，这笔钱通过特殊目的实体（SPV）筹集。其中约 420 亿美元优先档由博通提供支持；而在 180 亿美元的次级档（Junior Debt）里，Anthropic 向黑石集团开出了 **10% 以上的双位数收益率**，请其锚定认购 90 亿美元（同类公开市场信用的收益率大约在 7%），这笔交易目前仍在谈判中，剩余 90 亿美元次级档未来可能以更低收益率分销给其他投资者。

我们不需要把这个 10% 渲染成“华尔街聪明钱在做空 AI”——评级机构 KBRA 给 Anthropic 的评级只比投资级低一档（BB+）[^19]，次级档由于没有博通兜底本来就要求高息。**真正值得盯住的是“边际变化”：** 今年 6 月，阿波罗与黑石为 Anthropic 筹组上一笔 350 亿美元芯片融资[^20]时，同样没有博通担保的 45 亿美元次级档，票面利率还只有 8.5%[^21]。短短四个月里，美联储只加息了 25 个基点，AI 表外融资的次级信用成本却上升了 **150 个基点以上**。信贷市场还没有恐慌，但筹码正在肉眼可见地变贵。

### 3. 时间错配与“两个循环圈”

GPU 的经济折旧寿命只有四五年，模型厂背上的却是跨越十年的刚性合同。据路透社看到的招股书草稿披露，Anthropic 未来约十年的算力与云承诺至少高达 5180 亿美元[^22]，大部分不可取消，其中仅对谷歌一家的最低承诺就有 1111 亿美元。另一边，博通与阿波罗、黑石搭建了规模达 20 吉瓦（GW）的 AI 算力融资平台，美银分析师 Tom Curcuruto 估算，到 2029 年中该平台最高可能背负约 3700 亿美元的优先债[^23]。

如果把云巨头、芯片厂和模型厂的账本连起来看，所谓的“循环融资”其实分成了风险截然不同的两个圈子：

- **OpenAI 闭合圈（微软、甲骨文、CoreWeave、软银、英伟达）：** 最接近 2000 年朗讯与北电的卖方信贷模板。注意一个会计细节：云厂商签的几千亿算力长约并不是在当期直接确认为云收入，而是记进**剩余履约义务（RPO，即积压订单）**，用来支撑股价和发债能力。微软今年 1 月披露，其高达 6250 亿美元的商业 RPO 中，约 45% 直接绑在 OpenAI 一家身上[^24]；而另一边，软银为了兑现对 OpenAI 的 300 亿美元追加投资，还背着一笔将在 2027 年 3 月 25 日到期的 400 亿美元无担保过桥贷款[^25]。一个自身每年烧掉数百亿现金的大买家，撑起了上游半壁江山的订单簿。

- **Anthropic 半闭合圈（谷歌、亚马逊、博通）：** 博通借钱给它租博通参与设计的芯片，同样是标准的卖方信贷；而且其 2025 年近四分之一的收入来自两个大客户，客户集中度同样是风险。但它至少有真实的外部企业收入打底，现金流已经转正。

结论非常清晰：**如果这条加满杠杆的锁链要断，大概率会先从现金流高度失血的 OpenAI 圈及其外围高杠杆新云厂商（Neocloud）断开。**

## 四、为什么“云巨头砍 CapEx”是最后一张牌？

很多人在等某天早上醒来，看到微软或谷歌在财报会上宣布砍掉两成资本开支，以此作为泡沫破裂的发令枪。

**别等了，那是最后一张确认牌，绝不是第一张触发牌。**

回看 2000 年的电信泡沫：纳斯达克在 2000 年 3 月见顶崩盘，但下游电信运营商直到整整一年后的 2001 年才开始大砍资本开支。今天的云巨头正处在教科书般的囚徒困境里，谁先停手谁就丢掉云市场份额；更何况眼下根本没有闲置的“暗 GPU”，算力租金还在涨——SemiAnalysis 的数据显示，H100 一年期合约时租从去年 10 月的 1.70 美元涨到了今年 3 月的 2.35 美元，涨幅近 40%[^26]；就在 10 月 1 日，新云厂商 Nebius 又把 H100 按需价格从 3.85 美元上调至 4.50 美元，最新的 B300 更是上涨了 21%[^27]。在现货还在涨价的时候，没有任何一家有云业务的巨头会主动踩刹车。

未来 6 到 18 个月里，更可能率先倒下的是前面这三张骨牌：

1. **第一张牌：新股供给洪水（Equity Supply Tsunami）。** 金融学界对 2000 年春季互联网泡沫破裂最经典的解释之一，来自 Ofek 与 Richardson（2003）发表在《金融学刊》的研究[^28]：在做空受限的市场里，大量内部人筹码集中解禁，会击穿二级市场的承接力。看一眼 2026 年底到 2027 年中的排期表：6 月上市的 SpaceX 按常规 180 天禁售期推算将在年底前后解禁；Anthropic 计划 11 月募资约千亿美元，对应的解禁期落在 2027 年 5 月前后；后面还排着坚持 1 万亿估值的 OpenAI，以及 9 月已递交招股书的新云厂商 Nscale。在近 4% 的基准利率下，数千亿美元的新增股票要从同一批二级市场机构兜里掏钱。

2. **第二张牌：外围高杠杆信用断裂。** 加息周期里，永远是浮动利率、客户集中、靠高息私募债输血的外围玩家先出事。一旦 2026–2027 年开工的吉瓦级园区在 2027 年下半年集中并网，供给追上需求导致 GPU 租金掉头向下，SPV 里的残值担保和交叉违约条款（Cross-default）就会被触发，把局部问题变成链式反应。Anthropic 的招股书草稿就明确写着：某些违约事件会让大部分租赁债务立即到期，同时限制它动用博通那笔最高 420 亿美元的融资。

3. **第三张牌：前沿溢价被开源刺穿。** 再来一次“DeepSeek 时刻”：当开源权重模型在长链条 Coding Agent 上追平闭源旗舰、而调用成本只有十分之一时，头部实验室的估值模型将在一夜之间失去锚点。

只有当这三张牌倒下、二级市场估值回撤之后，资本开支的下调才会在 **2028 年初** 前后姗姗来迟。而且第一个挥刀砍预算的，也不会是有海量企业云客户兜底的微软或谷歌，更可能是 **Meta**（它没有对外出租算力的公有云业务来消化过剩产能，2022 年股价腰斩后，2023 年就被逼着搞过一次大砍支出的“效率之年”）或者是受制于资产负债表与信用利差的 **甲骨文**。

## 五、最强的反方与未来两年的“概率树”

写到这里必须先泼一盆冷水：**警惕把故事讲得太圆满。**

特沃斯基和卡尼曼早就警告过“合取谬误（Conjunction Fallacy）”：如果你把十个各有 70% 把握、且彼此独立的具体事件串成一部环环相扣的四幕剧，十环连乘下来的真实概率只剩 2.8%。如果我们只挑看空的数据，就会掉进自己搭建的回音室。

因此，在给出最终推演前，必须把最强的多头反方（The Bull Case）公平地摆在台面上：

- **这次的龙头真有现金流：** 2000 年的互联网新贵大多连营收都没有，而今天的 Anthropic 单季入账 168 亿美元且现金流为正，云巨头的传统主业依然是超级印钞机。

- **算力至今一卡难求：** 上市三四年的 H100 租金还在涨，全行业没有出现 2000 年那种埋在地下不发光的“暗光纤”。

- **增速是商业史级别的：** 据路透社报道，Anthropic 向投资人展示的 2028 年营收预测高达 1900 亿至 2000 亿美元[^29]。如果头部实验室真能维持每年两三倍的增长，今天看似离谱的万亿基建，最终会被狂奔的收入追上并消化，而不是靠崩盘来出清。

尊重这些反方事实，我们对未来两年（2026 Q4 – 2028 Q4）的判断就不应该是一条宿命论的单行道，而是一棵包含四个分支的**概率树**：

以下为作者对 2026 年第四季度至 2028 年第四季度的**主观概率判断**，悬停可查看各条路径的核心特征。

```echarts {height="320px" full=true class="ai-bubble-probabilities"}
animation: false
backgroundColor: transparent
aria:
  enabled: true
  description: 作者对 2026 年第四季度至 2028 年第四季度的主观情景判断：B 两段式出清 45%，C 硬着陆 25%，A 泡沫延续 15%，D 外生断裂 15%。概率合计 100%。
tooltip:
  trigger: item
  confine: true
  extraCssText: 'max-width: 260px; white-space: normal; line-height: 1.6;'
  textStyle:
    fontSize: 14
grid:
  left: 120
  right: 48
  top: 20
  bottom: 36
xAxis:
  type: value
  min: 0
  max: 50
  interval: 25
  axisLabel:
    formatter: '{value}%'
    fontSize: 11
  splitLine:
    lineStyle:
      type: dashed
      opacity: 0.25
yAxis:
  type: category
  inverse: true
  axisTick:
    show: false
  axisLine:
    show: false
  axisLabel:
    fontSize: 13
    margin: 12
  data:
  - B · 两段式出清
  - C · 硬着陆
  - A · 泡沫延续
  - D · 外生断裂
series:
- name: 主观概率
  type: bar
  barMaxWidth: 28
  showBackground: true
  backgroundStyle:
    color: rgba(148, 163, 184, 0.12)
    borderRadius: 4
  itemStyle:
    borderRadius:
    - 0
    - 4
    - 4
    - 0
  label:
    show: true
    position: right
    formatter: '{c}%'
    fontSize: 16
    fontWeight: bold
  emphasis:
    focus: self
  data:
  - value: 45
    name: B · 两段式出清
    itemStyle:
      color: '#507f9b'
    tooltip:
      formatter: B · 两段式出清（温和版 2001）<br/>主观概率：45%<br/>先估值压缩，后产能与信用出清；巨头与头部实验室存活。
  - value: 25
    name: C · 硬着陆
    itemStyle:
      color: '#b06e59'
    tooltip:
      formatter: C · 硬着陆（2000 + 滞胀）<br/>主观概率：25%<br/>溢价塌缩、继续加息、交叉违约同时发生，拖累宏观衰退。
  - value: 15
    name: A · 泡沫延续
    itemStyle:
      color: '#4f897a'
    tooltip:
      formatter: A · 泡沫延续（1998 重演）<br/>主观概率：15%<br/>一次两三成的回调后再创新高，大顶推迟，最终清算更大。
  - value: 15
    name: D · 外生断裂
    itemStyle:
      color: '#aa8746'
    tooltip:
      formatter: D · 外生断裂（黑天鹅）<br/>主观概率：15%<br/>台海、中东或重大 AI 安全事故，打断常规周期推演。
```

把这四根树枝展开来看：

- **情景 B（基准路径，45%）：** 前提是行业扩散按“年”缓慢推进，前沿溢价逐步收窄，利率维持高位。**上半场（2027 H1）是估值压缩：** 新股解禁洪峰叠加增速换挡，二级市场估值锚从“远期叙事”切回“当期毛利”，板块回撤 25% 到 35%。**下半场（2027 H2–2028）是产能与信用出清：** 吉瓦级园区集中并网令 GPU 租金拐头向下，外围新云与 SPV 债务重组，Meta 或甲骨文在 2028 年初下调资本开支，板块整体从顶部回撤 35% 到 55%。

- **情景 C（硬着陆，25%）：** 开源追平刺穿前沿溢价、能源通胀迫使美联储继续加息、SPV 交叉违约，三件事同时发生。算力单价雪崩击穿循环融资链条，烧钱最凶的 OpenAI 圈或高杠杆新云爆发重组级危机乃至财务丑闻；私募信贷亏损外溢，AI 板块跌幅超过 60%，2028 年全行业资本开支砍掉三成以上，直接把美国经济拖入衰退。

- **情景 A（1998 重演，15%）：** 楔子向第二梯队快速扩围，前沿溢价守住，利率见顶。就像 1998 年标普跌近两成后又狂飙一年半才在 2000 年见顶一样，2027 年市场仅经历一次两三成的回调便再创新高，把真正的大顶推迟到 2028 年以后——代价是最终那次清算的量级更加惊人。

- **情景 D（外生断裂，15%）：** 台海供应链冲击、中东战局失控，或者重大 AI 安全事故引发监管急冻。一旦发生晶圆供应中断，“算力过剩”的逻辑会在一夜之间翻转为“绝对短缺”，存量 GPU 与本地硬件反而成为奇货可居的战略硬通货。

这里有一个极少被提及的宏观联动细节：按 ING 今年 8 月的测算，AI 软硬件与数据中心投资撑起了 2026 年美国 GDP 增长的约三分之一[^30]。这意味着，根本不需要等所谓的“白领大失业”来引爆经济危机——事实上，NBER 与 IZA 今年 9 月发布的实证论文[^31]显示，今年夏天美国 22 到 25 岁应届本科生的平均失业率为 7.3%，仍落在 2022 年以来的正常区间内，并没有因为 AI 出现统计上的显著跃升。**当一项贡献了三分之一 GDP 增速的投资，其增长率从 77% 掉到零甚至负增长时，这个减速本身就是一台宏观衰退触发器。**

至于怎么判断我们正走在哪根树枝上，不需要听信任何分析师的嘴，盯紧下面这张仪表盘就够了：

| 观测信号 | 核心检验点 | 路径指向 |
| --- | --- | --- |
| Anthropic 上市后前两份季报 | 环比增速高于 **25%**，还是低于 **10%** | 前者偏向 **A（泡沫延续）**，后者偏向 **B（两段式出清）** |
| Anthropic 年底年化收入 | 能否从约 **670 亿美元**冲上预期的 **1100 亿美元** | 大幅落空，确认编程楔子换挡 |
| GPU 长约与按需租金 | 何时**停止上涨并拐头向下** | 拐头即新产能追上需求，**B 下半场**启动 |
| AI 表外债务次级档收益率 | 从 **8.5%** 升至 **10% 以上**后是否继续走阔 | 继续走阔，外围信用断裂风险上升 |
| OpenAI 2027 年上市 | 能否以 **1 万亿美元**估值顺利完成 | 再推迟或打折上市，是强烈见顶信号 |
| 2028 年初资本开支指引 | **Meta** 或**甲骨文**是否率先下调 | 区分 **B（温和出清）** 与 **C（硬着陆）** |

## 六、终局：科斯边界坍缩，我们是“新自由民”还是“新佃农”？

跳出未来两年的涨跌博弈，把目光投向 2028 年之后。无论中间经历的是温和消化还是暴烈洗牌，大水退去后的产业版图，已经浮现出三条极其坚硬的底线：

**第一，SaaS 不会团灭，但“薄壳 UI”必死。** “AI 杀死传统软件”的恐慌，二级市场在今年初其实已经定过一次价了：今年 1 月中到 2 月中，北美软件股蒸发了约 1 万亿美元市值；Salesforce 今年上半年股价下跌 40.9%[^32]，因为华尔街看穿了“按人头收费（Seat-based）”的模式会被 Agent 压缩。但软件支出并没有消失，而是在经历一场基因突变：只有一层薄薄工作流 UI 的 SaaS，会被企业自建的 Agent 碾碎；而沉淀了核心业务状态、作为底层“记录系统（System of Record）”的底座软件会活下来，并从“按席位收租”转向“按交付结果收费”。

**第二，“会计减值”不等于“物理报废”，廉价算力遗产比想象中更庞大。** 很多人担心 GPU 五年就淘汰，留不下像当年铁路和暗光纤那样能用三十年的遗产。这里要分清两件事：**金融破产抹掉的是资产负债表上的账面债务和折旧包袱，但物理显卡不会跟着一起蒸发。** 当外围 SPV 违约重组、完成巨额会计减值（Write-down）后，那些资本成本被清零的 H100、B200 显卡，只要每产出百万 Token 的售价还能覆盖“电费 + 机房运维”的边际现金成本，就会继续在机房里满负荷运转。再加上那些已经走完漫长审批、建好变电站的吉瓦级机房外壳，到 2028 年，单位能力的 Token 成本大概率会再降一个数量级。

**第三，科斯边界坍缩，一人公司（OPC）从边缘走向主流。** 诺奖得主罗纳德·科斯（Ronald Coase）在 1937 年的《企业的性质》里早就给出了终极答案：企业之所以要雇佣几百上千人、忍受臃肿的科层制，根本原因是**市场上的交易成本（搜寻、签约、交付、验收）太贵了**。当 AI 让外部交易成本下降的速度，快过大公司消灭内部协调成本的速度时，企业的最优边界就会向内坍缩，最小可以坍缩到**一个人**。

这件事不需要等泡沫崩盘才会发生。经济史学家保罗·戴维（Paul David）曾研究过 19 世纪末的电力革命：电动机成熟后，制造业生产率之所以过了约四十年才起飞，是因为必须等依赖中央天轴传动的老厂房自然退役，由原生围绕“单机独立驱动”设计的新厂房接管市场。**今天原生于 AI 的一人公司与三五人极客团队，就是新建的“单机驱动工厂”。** 它们在大宗 Token 崩价的今天，已经在边缘地带野蛮生长；而未来两年的资本出清，只是帮它们一次性释放廉价算力与顶尖人才的**加速器**。

但在最后，我想打破技术乐观主义的玫瑰色幻想，抛出一个更冷酷的追问：

**当一人公司遍地开花时，我们究竟是迎来了掌控生产资料的“新自由民”，还是仅仅制造了一群替算力帝国打工、自负盈亏的“数字佃农”？**

首先，幂律分布（Power Law）不会因为 AI 而消失。极少数顶尖架构师和行业老兵组成的一人公司，确实能干出过去百人企业的营收；但中位数上的绝大多数，依然只是勉强糊口的微小个体。

更重要的是**剩余价值的归属**。试想一下：当云巨头发现 GPU 算力沦为同质化的低毛利商品、自身自由现金流承压时，它们会去哪里把利润找补回来？**它们很可能会利用生态锁定，在存储、托管数据库、网络出口流量费（Egress Fee）这些传统高毛利现金牛上死守价格，甚至变相加价。**

如果一个超级个体的模型智力、上下文记忆、核心业务数据库，乃至分发与支付通道，全部锁死在两三家幸存的云与模型寡头平台上——那么交易成本下降省出来的每一分钱，最终都会被平台通过 Token 溢价、状态存储税和过路费收走。所谓的“一人公司革命”，不过是把过去受劳动法保护的大厂雇员，变成了没有底薪、自担全部市场风险、还要按月给云地主交租的“数字佃农”。

决定你是自由民还是佃农的，从来不是你写了多精妙的 Prompt，而是两样东西：

1. **有没有随时可以热插拔、不被单一闭源溢价绑架的开源模型替代方案；**

2. **有没有完全自主可控、随时可以跨云迁移、甚至跑在裸金属和本地硬件上的核心数据底座；**

2026 到 2028 年的这场周期洗牌，表面上看是华尔街万亿资本开支的泡沫出清；但在更深的水位下，它是关于未来三十年**技术剩余价值归谁所有**的第一次决战。

泡沫终会散去。愿你在大水退去后的开悟之坡上，做那个手握底座与生产资料的自由建造者，而不是在别人的云端农庄里，做一辈子勤勤恳恳的数字佃农。

## 参考资料

[^1]: [北美四大云巨头将今年的资本开支（CapEx）指引一路推高至约 7250 亿美元](https://startupfortune.com/big-techs-725-billion-ai-spending-wave-is-turning-free-cash-flow-into-a-distant-memory/)

[^2]: [美国银行测算，这笔庞大的开支将吞噬巨头们 94% 的经营现金流](https://247wallst.com/investing/2025/11/10/bank-of-america-just-issued-a-stark-warning-the-ai-boom-is-hitting-a-cash-crunch/)

[^3]: [Alphabet 在今年二季度录得约 -59 亿美元的自由现金流](https://www.tikr.com/blog/alphabets-free-cash-flow-just-went-negative-heres-what-the-debt-behind-it-says)

[^4]: [Anthropic 正以 1.8 万亿到 2 万亿美元的目标估值冲刺 IPO](https://www.techmeme.com/261014/p56)

[^5]: [OpenAI 则已确认将上市窗口推迟至 2027 年](https://thenextweb.com/news/openai-ipo-delay-2027-altman-1-trillion)

[^6]: [美国人口普查局（BTOS）的抽样调查](https://www.wework.com/ideas/research-insights/the-new-ai-divide)

[^7]: [ING（荷兰国际集团）估算](https://talkmarkets.com/article/how-much-is-ai-contributing-to-us-economic-growth-1787193106)

[^8]: [美联储在 9 月全票通过加息 25 个基点至 3.75%–4.00%](https://www.raisin.com/en-us/news/fed-rate-decision-policy-breakdown-september-2026/)

[^9]: [10 月 14 日 Anthropic 投资者会上流出的财务数字](https://lilithai.dev/radar/anthropic-tells-investors-quarterly-revenue-up-nearly-50-to-16-8bn-ahead?lang=en)

[^10]: [企业在 AI 编程上的支出有高达 54% 流向了 Anthropic 一家](https://valueaddvc.com/blog/openai-vs-anthropic-which-ai-company-is-winning-the-enterprise-in-2026)

[^11]: [Anthropic 三季度的环比增速也从二季度的约 140% 降到了约 46%](https://www.techmeme.com/261014/p56)

[^12]: [Anthropic 向投资人解释称，“蒸馏”（即竞争对手调用其模型输出来训练自家模型）带来的收入原本占到总营收的 5% 到 7%](https://lilithai.dev/radar/anthropic-tells-investors-quarterly-revenue-up-nearly-50-to-16-8bn-ahead?lang=en)

[^13]: [与阿里千问团队相关的操作者在 4 月 22 日至 6 月 5 日间通过近 2.5 万个虚假账号与 Claude 进行了约 2880 万次交互](https://www.binance.com/en-IA/square/post/346765717322417)

[^14]: [7 月底披露 650 亿美元年化收入（Run-rate）](https://aibusinessweekly.net/p/anthropic-statistics)

[^15]: [投资人目前对它年底的年化收入预期高达 1000 亿至 1100 亿美元](https://www.cnbc.com/2026/10/14/anthropic-third-quarter-revenue-16-8-billion.html)

[^16]: [自今年 2 月起，中国开源模型每周都拿下美国企业三成以上的 Token 用量；到 7 月中旬峰值时，中国模型的份额达到 46.4%，反超美国本土模型的 35.7%](https://taskpool.ai/blog/chinese-ai-models-enterprise-risk)

[^17]: [DeepSeek V4 Flash 每百万输入 Token 仅售 0.14 美元，不到 GPT-5.5（5 美元）的三十六分之一；旧金山 AI 初创公司 Lindy 将工作流从 Claude 切过去后，推理成本直接砍掉了 90%](https://followin.io/vi/feed/26363711)

[^18]: [600 亿美元“北极星计划（Project North Star）”](https://www.livemint.com/ai/artificial-intelligence/anthropic-offers-blackstone-double-digit-yield-in-chip-financing-deal-what-the-60-billion-deal-entails-11792204532812.html)

[^19]: [KBRA 给 Anthropic 的评级只比投资级低一档（BB+）](https://thedeepdive.ca/anthropics-junk-credit-rating-went-unreported-during-35-billion-ai-financing/)

[^20]: [350 亿美元芯片融资](https://thepaypers.com/fintech/news/apollo-and-blackstone-close-usd-35-billion-chip-financing-deal-for-anthropic)

[^21]: [票面利率还只有 8.5%](https://ng.investing.com/news/company-news/apollo-blackstone-finalize-35-billion-ai-chip-financing-for-anthropic-2546759)

[^22]: [Anthropic 未来约十年的算力与云承诺至少高达 5180 亿美元](https://origami.sa/en/blog/anthropic-ipo-prospectus-risk-factors/)

[^23]: [美银分析师 Tom Curcuruto 估算，到 2029 年中该平台最高可能背负约 3700 亿美元的优先债](https://www.benzinga.com/markets/prediction-markets/26/08/61219624/broadcom-ai-financing-370-billion)

[^24]: [微软今年 1 月披露，其高达 6250 亿美元的商业 RPO 中，约 45% 直接绑在 OpenAI 一家身上](https://thedailydollar27.substack.com/p/microsofts-625-billion-signal-most)

[^25]: [软银为了兑现对 OpenAI 的 300 亿美元追加投资，还背着一笔将在 2027 年 3 月 25 日到期的 400 亿美元无担保过桥贷款](https://www.investing.com/news/stock-market-news/softbank-secures-40-billion-loan-to-fund-openai-investment-93CH-4584494)

[^26]: [SemiAnalysis 的数据显示，H100 一年期合约时租从去年 10 月的 1.70 美元涨到了今年 3 月的 2.35 美元，涨幅近 40%](https://eu.36kr.com/zh/p/4022220823171208)

[^27]: [新云厂商 Nebius 又把 H100 按需价格从 3.85 美元上调至 4.50 美元，最新的 B300 更是上涨了 21%](https://timeline.sohu.com/news/kvIswyTgRy)

[^28]: [Ofek 与 Richardson（2003）发表在《金融学刊》的研究](https://econpapers.repec.org/RePEc:bla:jfinan:v:58:y:2003:i:3:p:1113-1137)

[^29]: [Anthropic 向投资人展示的 2028 年营收预测高达 1900 亿至 2000 亿美元](https://aibusinessweekly.net/p/anthropic-statistics)

[^30]: [按 ING 今年 8 月的测算，AI 软硬件与数据中心投资撑起了 2026 年美国 GDP 增长的约三分之一](https://talkmarkets.com/article/how-much-is-ai-contributing-to-us-economic-growth-1787193106)

[^31]: [NBER 与 IZA 今年 9 月发布的实证论文](https://docs.iza.org/dp18945.pdf)

[^32]: [Salesforce 今年上半年股价下跌 40.9%](https://www.saasrise.com/news/salesforce-shares-plunge-40-in-h1-2026-amid-aiagentic-fear-b14605d4-a9bc-4622-b92d-50b6f04ca459)
