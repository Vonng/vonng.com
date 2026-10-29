---
title: "How Will the AI Bubble Burst?"
date: 2026-10-17
authors: [vonng]
summary: >
  AI capability, real-world adoption, and financial capital are moving on three out-of-sync curves. Demand is narrow and deep, while pricing, credit, and duration have fallen into a triple mismatch: how will the bubble unwind, and who captures the technological surplus left behind?
tags: [AI, Commentary, Business]
aliases: [/ai/buble-break/]
---

> This article is 70% AI-generated, synthesized from a four-way debate between Vonng, Claude, Gemini, and ChatGPT. Data is as of October 17, 2026. Nothing here constitutes investment advice.

Looking around in October 2026, anyone who both writes production code and reads corporate balance sheets feels a jarring sense of whiplash.

On one side is a capital boom that has defied gravity. North America's four hyperscalers have pushed their 2026 capital expenditure (CapEx) guidance to roughly $725 billion[^1], up another 77% year-over-year. Bank of America estimates that this spending wave will consume 94% of their operating cash flow[^2]—and in Q2 2026, it pushed Alphabet, once a relentless cash-printing machine, into negative free cash flow of roughly -$5.9 billion[^3] for the first time since its 2004 IPO. Private markets can no longer contain a beast of this size: after SpaceX raised $75 billion in June, Anthropic is sprinting toward an IPO at a target valuation of $1.8 trillion to $2 trillion[^4], while OpenAI, holding firm to a $1 trillion valuation floor, has pushed its listing window to 2027[^5].

On the other side is an unsettlingly quiet real economy. According to the U.S. Census Bureau's Business Trends and Outlook Survey (BTOS)[^6], only 21.7% of U.S. businesses actually used AI in production in July 2026 (edging up to 23.2% in August); among the nearly 80% that did not, 61.6% of owners said outright that AI had no relevance to their business. Consumer numbers are just as sobering: ING estimates[^7] that only 2% to 3% of U.S. households pay for AI subscriptions. Casual consumer subscriptions cannot come close to covering the depreciation and power bills of a trillion-dollar infrastructure buildout.

[AI Adoption May Not Run That Deep](/en/ai/funnel/)

We have trillion-dollar infrastructure priced as if the entire economy is being rewritten overnight, set against sluggish adoption on the ground. The obvious conclusion many draw is: **The AI bubble is about to burst because the real demand simply isn't there.**

Yet when you lay out the hardest numbers from recent quarters—financial ledgers, credit spreads, and API routing traffic—and run them through rounds of ruthless adversarial stress-testing, that intuition turns out to be **only half right**.

The financial capital curve has indeed reached a precarious high plateau, but claiming there is "no demand" misses the mark. When this AI mania goes through a major reckoning, it will not die from a lack of demand. It will die from the resonance of three structural fractures: **a premium mismatch, a credit mismatch, and a duration mismatch.**

## TL;DR

- **Where we stand:** Model capability is still climbing steeply, real-world adoption is "narrow and deep," and financial capital sits on a high plateau.

- **How it unwinds:** Most likely not a single crash, but a **two-stage unwind**—first **multiple compression** in H1 2027, followed by **capacity digestion and credit clearing** from H2 2027 into 2028.

- **The first domino:** It will not be hyperscalers voluntarily cutting CapEx. Ahead of that sit three triggers: **an equity supply tsunami, peripheral high-leverage credit defaults, and open-weight models puncturing the frontier premium**.

- **Scenario probabilities:** Two-stage unwind (45%), hard landing (25%), 1998-style bubble continuation (15%), exogenous supply-chain shock (15%).

- **The endgame baseline:** Across every path, token costs drop another order of magnitude, industry adoption advances in order of verifiability, and one-person companies (OPCs) proliferate. What truly separates the paths is **who ultimately captures the technological surplus**.

## 1. Unbundling Three Out-of-Sync Curves

The biggest mistake in debating whether AI has peaked is collapsing everything into a single curve.

Gartner's Hype Cycle tracks **public expectations**; evolutionary economist Carlota Perez, in *Technological Revolutions and Financial Capital*, distinguishes between the "Installation Period" and the "Deployment Period" to describe **the handover of power from financial capital to production capital**. Unbundle AI today and you see three curves moving on completely different clocks:

```echarts {height="710px" full=true class="ai-bubble-curves"}
baseOption:
  animation: false
  backgroundColor: transparent
  aria:
    enabled: true
    description: Three conceptual curves on independent scales. In October 2026, technical capability is still climbing steeply, adoption diffusion is narrow and deep, and financial capital sits on a high plateau. Dots mark the current assessment; dashed lines show illustrative paths rather than empirical data or quantitative forecasts. Toggle the legend to switch between continuation and correction paths for financial capital.
  tooltip:
    trigger: item
    confine: true
    extraCssText: 'max-width: 260px; white-space: normal; line-height: 1.6;'
    textStyle:
      fontSize: 14
  title:
  - text: Technical Capability · Still Climbing Steeply
    subtext: Model ceiling keeps rising
    left: 12
    top: 8
    textStyle:
      fontSize: 16
    subtextStyle:
      fontSize: 12
  - text: Adoption Diffusion · Narrow & Deep
    subtext: Deep in a few verticals, early across the economy
    left: 12
    top: 244
    textStyle:
      fontSize: 16
    subtextStyle:
      fontSize: 12
  - text: Financial Capital · High Plateau, Mismatches Building
    subtext: Pricing runs ahead of real-world diffusion
    left: 12
    top: 480
    textStyle:
      fontSize: 16
    subtextStyle:
      fontSize: 12
  legend:
    data:
    - Continuation
    - Correction
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
    name: Stage →
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
    name: Stage →
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
    name: Stage →
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
    name: Capability
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
    name: Breadth
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
    name: Pricing
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
  - name: Technical Capability
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
      formatter: "Technical Capability | Oct 2026<br/>Still climbing steeply as model ceilings rise.<br/>Technical progress outlives capital cycles."
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
        formatter: Now
        position: top
        distance: 10
        fontSize: 13
      data:
      - name: Oct 2026
        coord:
        - 72
        - 52
      tooltip:
        formatter: "Technical Capability | Oct 2026<br/>Still climbing steeply as model ceilings rise.<br/>Technical progress outlives capital cycles."
  - name: "Technical Capability: Potential Path"
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
      formatter: "Technical Capability | Potential Path<br/>Capability ceiling continues to rise.<br/>Dashed line is conceptual, not a quantitative forecast."
    emphasis:
      focus: series
    data:
    - - 72
      - 52
    - - 82
      - 78
    - - 90
      - 100
  - name: Adoption Diffusion
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
      formatter: 'Adoption Diffusion | Oct 2026<br/>Deep usage in a few verticals, early across the broader economy.<br/>Defined by a "narrow and deep" profile.'
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
        formatter: Now
        position: top
        distance: 10
        fontSize: 13
      data:
      - name: Oct 2026
        coord:
        - 34
        - 20
      tooltip:
        formatter: 'Adoption Diffusion | Oct 2026<br/>Deep usage in a few verticals, early across the broader economy.<br/>Defined by a "narrow and deep" profile.'
  - name: "Adoption Diffusion: Potential Path"
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
      formatter: "Adoption Diffusion | Potential Path<br/>Spreading from a few beachheads into broader industries.<br/>Requires engineering sandboxes and institutional guardrails."
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
  - name: Financial Capital
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
      formatter: "Financial Capital | Oct 2026<br/>Sitting on a high plateau, priced ahead of real-world diffusion.<br/>Mismatches are building; timing of the unwind remains contested."
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
        formatter: Now
        position: top
        distance: 10
        fontSize: 13
      data:
      - name: Oct 2026
        coord:
        - 48
        - 93
      tooltip:
        formatter: "Financial Capital | Oct 2026<br/>Sitting on a high plateau, priced ahead of real-world diffusion.<br/>Mismatches are building; timing of the unwind remains contested."
  - name: Continuation
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
      formatter: "Financial Capital | Continuation Path<br/>High valuations hold and the major peak is pushed out.<br/>A plausible scenario, not a guaranteed outcome."
    emphasis:
      focus: series
    data:
    - - 48
      - 93
    - - 70
      - 96
    - - 100
      - 100
  - name: Correction
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
      formatter: "Financial Capital | Correction Path<br/>Valuations reset, then recover gradually after clearing.<br/>Technical progress does not equal capital returns."
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
    - text: Technical Capability · Still Climbing Steeply
      subtext: Model ceiling keeps rising
      left: 12
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 12
    - text: Adoption Diffusion · Narrow & Deep
      subtext: Deep in a few verticals, early across the economy
      left: 12
      top: 244
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 12
    - text: Financial Capital · High Plateau, Mismatches Building
      subtext: Pricing runs ahead of real-world diffusion
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
      - Continuation
      - Correction
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
      name: Stage →
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
      name: Stage →
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
      name: Stage →
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
    - text: Technical Capability
      subtext: Still climbing steeply
      left: 3%
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 13
    - text: Adoption Diffusion
      subtext: Narrow & deep, early rollout
      left: 36%
      top: 8
      textStyle:
        fontSize: 16
      subtextStyle:
        fontSize: 13
    - text: Financial Capital
      subtext: High plateau, mismatches building
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

*Conceptual illustration, not to scale; each chart runs on its own axis. Dots mark our October 2026 assessment; dashed lines show potential trajectories. Technical progress ≠ capital returns. Hover for details, or click the "Continuation / Correction" legend to toggle paths.*

1. **Technical capability curve: Still climbing steeply.** From long-horizon reasoning to complex tool use, the intelligence ceiling continues to advance quarter by quarter, nowhere near a plateau.

2. **Adoption diffusion curve: Extremely "narrow and deep."** Economy-wide penetration sits just above 20%, yet real commercial revenue is driven like a steel spike into a handful of vertical workflows.

3. **Financial capital curve: At the high plateau marking the end of the Installation Period.** In September, the Federal Reserve voted unanimously to hike rates by 25 bps to 3.75%–4.00%[^8] (its first rate hike in three years), mega-unicorns are lining up to distribute shares to public markets, and infrastructure financing is shifting from internal cash flow to off-balance-sheet leverage. Nearly every late-cycle warning light from past technological revolutions is now flashing.

**A bubble bursting never means the technology drops to zero; it means the yawning gap between the financial capital curve and the adoption diffusion curve gets forcibly closed.** When the dot-com bubble burst in 2001–2002, global internet traffic kept compounding rapidly. What collapsed was capital pricing that had pulled forward ten years of expectations.

## 2. Demand Isn't Missing—It's Just Brutally Narrow

Any claim that "there is no demand" gets demolished by the numbers leaked from Anthropic's October 14 investor presentation[^9] (unaudited figures reported by the *Financial Times*, as a public S-1 filing has not yet been released): its revenue jumped from roughly $4.8 billion in Q1 2026 to $11.5 billion in Q2, and hit **$16.8 billion** in Q3—meaning a single quarter of revenue exceeded 3.6x its entire 2025 full-year total. Anthropic also told investors that its Q3 adjusted operating margin reached roughly 11% (excluding stock-based compensation), operating cash flow turned positive, and every $1 spent on compute generated $1.70 in revenue.

Why do frontier labs pull in tens of billions of dollars when ordinary people barely know anyone paying for top-tier AI? Because counting human heads is an obsolete metric in the age of agents.

The unit of compute consumption is not the human user, but the token. A single coding agent running loops in the background 24/7 burns through as many tokens in a day as hundreds of office workers typing into a chat box. The true ceiling of demand is the economic value of tasks that can be reliably automated, not population multiplied by a $20 monthly subscription.

The real vulnerability is not that demand is fake, but that **it is overwhelmingly lopsided**. According to Menlo Ventures, a staggering 54% of enterprise spending on AI coding goes to Anthropic alone[^10], compared with 21% for OpenAI. That concentration has allowed Anthropic—despite having a fraction of ChatGPT's monthly active users—to overtake OpenAI in annualized revenue (ARR).

### Why Did Software Engineering Become the Only Super-Wedge?

From engineering first principles, the speed at which AI diffuses across any industry can be compressed into an unforgiving formula:

**Diffusion Speed** ≈ **Verifiability** × **Reversibility** × **Accountability**

Software engineering became a tens-of-billions-of-dollars commercial loop because it is one of the rare greenhouses in the economy where all three variables are maxed out: **deterministic compilers and automated test suites provide low-cost verification; Git and sandboxed environments provide near-zero-cost reversibility; and the human engineer who hits Enter to merge the code absorbs the accountability.** If an agent botches 10,000 lines of code inside a sandbox and fails the test suite, you revert and rerun—without creating a single cent of bad debt in the physical world.

What about the other 80% of the corporate world? Wiring funds, shipping inventory, performing surgery, signing contracts—all three properties are missing.

Anyone who builds infrastructure knows that fault-tolerance primitives are nothing new: databases have long had transactions, rollbacks, snapshots, point-in-time recovery (PITR), and branching; financial systems have double-entry bookkeeping, automated reconciliation, and dual authorization. **Only two things are actually missing: foolproof interfaces to an irreversible physical world, and legal, insurance, and regulatory frameworks for assigning liability.**

Diffusing AI beyond software engineering is far from impossible, but it requires building out engineering sandboxes and institutional guardrails one industry at a time. Following this formula down the stack, the next wedges to open up will inevitably be **data analytics and SQL, IT and security operations, customer support with human escalation, and back-office financial reconciliation**—while law, medicine, and physical supply chains will come last. That buildout is measured in years, not the quarters Wall Street is pricing in.

### Is the Coding Wedge Starting to Dull?

Subtler signals are already surfacing. Even inside the sharpest wedge—coding—Anthropic's quarter-over-quarter revenue growth decelerated from roughly 140% in Q2 to roughly 46% in Q3[^11], and its net new quarterly revenue (around $5.3 billion) came in below the prior quarter's addition (around $6.7 billion) for the first time.

To be fair, no single factor explains the slowdown. According to the *Financial Times*, Anthropic told investors that "distillation"—competitors querying its models to train their own—previously accounted for 5% to 7% of total revenue[^12], and tightened risk controls in Q3 squeezed out much of that traffic (Anthropic had earlier unilaterally alleged that operators linked to Alibaba's Qwen team conducted roughly 28.8 million interactions with Claude across nearly 25,000 fake accounts between April 22 and June 5[^13]). Combined with compute constraints, API price cuts, and customers routing workloads to cheaper models, Q3's deceleration cannot be casually equated with "peak demand."

Still, the arithmetic on the ledger is unforgiving: $16.8 billion in Q3 revenue translates to roughly $67 billion annualized, and the company has not updated its run-rate figure since disclosing a $65 billion annualized run-rate in late July[^14]. Yet investor expectations for its year-end annualized revenue sit at $100 billion to $110 billion[^15]. Clearing that bar will require a steep re-acceleration in Q4.

In my view, whether [personal secretary agents](/en/ai/secretary-era/) can cross the chasm into mainstream adoption may be the decisive variable. Otherwise, a small cohort of heavy-pedaling power users will struggle to carry a valuation story of this magnitude.

## 3. The Triple Mismatch: Premium, Credit, and Duration

Put a narrow revenue wedge next to a trillion-dollar infrastructure buildout, and the fragility of today's AI market comes into sharp focus across three mismatches:

### 1. Premium Mismatch: A Bifurcated Token Market

Bulls love to invoke Jevons paradox: cheaper inference drives an explosion in volume, lifting total revenue. That argument is only half right, because the token market has split cleanly in two:

**The Commodity Layer is undergoing price collapse.** On the developer routing platform OpenRouter, Chinese open-weight models have captured over 30% of weekly U.S. enterprise token volume since February 2026; at their mid-July peak, Chinese models hit a 46.4% share, overtaking U.S. domestic models at 35.7%[^16]. The reason is brutally simple: they are 60% to 90% cheaper. DeepSeek V4 Flash costs just $0.14 per million input tokens—less than one-thirty-sixth the price of GPT-5.5 ($5.00). When San Francisco AI startup Lindy switched its workflows over from Claude, its inference bill dropped by 90%[^17]. (One caveat: OpenRouter reflects developer routing traffic, not the entire enterprise market. Anthropic holds just over 10% of token volume on OpenRouter, yet commands a far larger share of total enterprise revenue. Put differently, **Chinese models are winning volume, while Western frontier labs are still winning revenue.**)

**The Frontier Layer is defending its premium purely through a capability gap.** Leading closed-model providers even raised prices by roughly 12% in the first half of the year, offsetting the deflationary pull of open models. The combined ~$3 trillion target valuation of Anthropic and OpenAI rests entirely on the assumption that this frontier premium will hold. **Here, cheap open-weight models are merely the amplifier; the fatal fuse is a slowdown in frontier capability gains.** As long as frontier models maintain a generational lead on long-horizon, complex agent workflows—backed by U.S. congressional scrutiny and geopolitical fencing against Chinese models—they can protect part of their closed-source premium in Western enterprise and government markets. But the moment the capability curve flattens and open models close the gap within six months, that pricing moat will erode fast.

### 2. Credit Mismatch: Not Panic, Just Pricier Debt

With internal cash flows spoken for, compute infrastructure is morphing into an elaborate exercise in off-balance-sheet financial engineering.

The textbook example is the $60 billion "Project North Star"[^18], revealed on October 16: to procure roughly 1.5 gigawatts of Google TPU capacity without loading the debt directly onto Anthropic's balance sheet, the financing is structured through a special purpose vehicle (SPV). Roughly $42 billion in senior debt is backstopped by Broadcom; for the $18 billion junior debt tranche, Anthropic offered Blackstone a **double-digit yield above 10%** to anchor $9 billion of the facility (comparable public-market credit yields around 7%). The deal remains under negotiation, with the remaining $9 billion in junior debt potentially syndicated to other investors at lower yields.

There is no need to sensationalize a 10% yield as "Wall Street smart money shorting AI"—rating agency KBRA rates Anthropic at BB+, just one notch below investment grade[^19], and junior debt lacking a Broadcom guarantee naturally commands a higher spread. **What matters is the marginal shift:** back in June, when Apollo and Blackstone arranged Anthropic's previous $35 billion chip financing facility[^20], the $4.5 billion junior tranche—likewise unbacked by Broadcom—carried a coupon of just 8.5%[^21]. In four short months, while the Fed hiked by only 25 bps, the junior credit cost of off-balance-sheet AI financing jumped by **more than 150 bps**. The credit market is not panicking yet, but capital is getting visibly more expensive.

### 3. Duration Mismatch and the "Two Circular Loops"

A GPU has an economic useful life of four to five years, yet frontier labs are locking themselves into rigid ten-year commitments. According to a draft prospectus reviewed by Reuters, Anthropic faces at least $518 billion in mostly non-cancellable compute and cloud commitments over roughly the next decade[^22], including a minimum commitment of $111.1 billion to Google alone. Meanwhile, Broadcom, Apollo, and Blackstone have set up a 20-gigawatt (GW) AI compute financing platform that Bank of America analyst Tom Curcuruto estimates could carry up to $370 billion in senior debt by mid-2029[^23].

Connect the balance sheets of the hyperscalers, chipmakers, and model labs, and so-called "circular financing" actually splits into two loops with very different risk profiles:

- **The OpenAI Closed Loop (Microsoft, Oracle, CoreWeave, SoftBank, Nvidia):** This comes closest to the 2000-era vendor-financing playbook of Lucent and Nortel. Note a crucial accounting detail: multi-hundred-billion-dollar compute contracts signed with cloud providers are not booked immediately as current cloud revenue; they sit in **Remaining Performance Obligations (RPO, or contracted backlog)**, where they prop up equity valuations and debt capacity. Microsoft disclosed in January 2026 that roughly 45% of its $625 billion commercial RPO is tied directly to OpenAI alone[^24]. On the other side of the table, SoftBank—scrambling to fund its $30 billion follow-on investment in OpenAI—is carrying a $40 billion unsecured bridge loan maturing on March 25, 2027[^25]. A single buyer burning tens of billions in cash each year is holding up half the upstream order book.

- **The Anthropic Semi-Closed Loop (Google, Amazon, Broadcom):** Broadcom lending Anthropic money to lease chips co-designed by Broadcom is textbook vendor financing as well, and customer concentration remains a real risk—nearly a quarter of Anthropic's 2025 revenue came from just two customers. Even so, it is underwritten by genuine external enterprise revenue and positive operating cash flow.

The takeaway is clear: **if this heavily leveraged chain snaps, it will almost certainly break first inside the cash-bleeding OpenAI loop and the highly leveraged peripheral neoclouds orbiting it.**

## 4. Why Hyperscaler CapEx Cuts Are the Last Domino, Not the First

Many investors are waiting to wake up one morning and hear Microsoft or Google announce a 20% CapEx cut on an earnings call as the starting gun for the crash.

**Stop waiting. That will be the final confirmation, never the opening trigger.**

Look back at the 2000 telecom bubble: the Nasdaq peaked and cracked in March 2000, yet downstream telecom carriers did not slash capital spending until 2001, a full year later. Today's hyperscalers are locked in a textbook prisoner's dilemma where the first to blink cedes cloud market share. More importantly, there are no idle "dark GPUs" sitting in racks today—compute rental rates are still rising. Data from SemiAnalysis shows that 1-year contract hourly rates for H100s rose nearly 40%, from $1.70 in October 2025 to $2.35 in March 2026[^26]; and on October 1, neocloud provider Nebius raised on-demand H100 pricing from $3.85 to $4.50 per hour while hiking its newest B300 instances by 21%[^27]. As long as spot rates are climbing, no hyperscaler with a cloud business will voluntarily hit the brakes.

Over the next 6 to 18 months, three earlier dominoes are far more likely to fall first:

1. **Domino 1: The Equity Supply Tsunami.** One of the classic academic explanations for the spring 2000 dot-com crash comes from Ofek and Richardson's (2003) *Journal of Finance* study[^28]—in a market with short-sale constraints, a concentrated wave of insider lock-up expirations overwhelms public-market liquidity. Look at the calendar from late 2026 through mid-2027: SpaceX, which went public in June, hits its standard 180-day lock-up expiration around year-end; Anthropic plans to raise roughly $100 billion in November, placing its lock-up expiration around May 2027; and lined up behind them are OpenAI (still demanding a $1 trillion valuation) and neocloud provider Nscale, which filed its prospectus in September. With benchmark interest rates near 4%, hundreds of billions of dollars in fresh equity supply will be competing for cash from the exact same pool of public institutional buyers.

2. **Domino 2: Peripheral High-Leverage Credit Defaults.** In a tightening cycle, peripheral players with floating-rate debt, concentrated customer bases, and high-yield private credit always crack first. Once the gigawatt-scale campuses that broke ground in 2026–2027 come online en masse in the second half of 2027, supply catching up with demand will send GPU rental rates rolling over. That in turn will trip residual-value guarantees and cross-default clauses inside SPVs, turning localized stress into a chain reaction. Anthropic's own draft prospectus explicitly warns that certain default events would accelerate the majority of its lease obligations while restricting its access to the Broadcom-backed financing facility of up to $42 billion.

3. **Domino 3: Open-Weight Models Puncturing the Frontier Premium.** Another "DeepSeek moment": the day an open-weight model matches closed frontier flagships on long-horizon coding agents at one-tenth the inference cost, the valuation models of the leading labs will lose their anchor overnight.

Only after those three dominoes fall and public-market multiples contract will CapEx cuts finally arrive around **early 2028**. Even then, the first to swing the axe will not be Microsoft or Google, which have massive enterprise cloud customer bases to absorb capacity. It will far more likely be **Meta**—which has no public cloud business to rent out excess compute and was forced into a cost-slashing "Year of Efficiency" in 2023 after its stock was cut in half in 2022—or **Oracle**, constrained by its balance sheet and credit spreads.

## 5. Steelmanning the Bull Case and the Two-Year Probability Tree

At this point, a bucket of cold water is in order: **beware of narratives that fit together too neatly.**

Tversky and Kahneman famously warned against the **conjunction fallacy**: if you chain together ten independent events that each carry a 70% probability into a tightly scripted four-act drama, the joint probability of the whole sequence playing out is just 2.8%. Cherry-picking only bearish data is a recipe for trapping yourself in an echo chamber.

Before laying out the final scenarios, we need to steelman the strongest bull case:

- **This cycle's leaders have real revenue and cash flow:** Most dot-com darlings in 2000 barely had revenue, whereas Anthropic just booked $16.8 billion in a single quarter with positive operating cash flow, and the hyperscalers' core businesses remain cash-printing juggernauts.

- **Compute is still scarce:** Rental rates for three-to-four-year-old H100s are still rising, and the industry has zero equivalent of the unlit "dark fiber" buried underground in 2000.

- **Growth is moving at a historic clip:** According to Reuters, Anthropic showed investors projections calling for $190 billion to $200 billion in annual revenue by 2028[^29]. If frontier labs can actually sustain 2x to 3x annual growth, today's seemingly absurd trillion-dollar buildout will be grown into and absorbed by compounding revenue rather than cleared through a crash.

Respecting those counter-facts means our outlook for the next two years (Q4 2026 – Q4 2028) should not be a deterministic one-way street, but a four-branch **probability tree**:

Below is the author's **subjective probability distribution** for Q4 2026 through Q4 2028; hover over each bar for the core mechanics of that path.

```echarts {height="320px" full=true class="ai-bubble-probabilities"}
animation: false
backgroundColor: transparent
aria:
  enabled: true
  description: "Author's subjective scenario probabilities for Q4 2026 to Q4 2028: B Two-Stage Unwind 45%, C Hard Landing 25%, A Bubble Continuation 15%, D Exogenous Shock 15%. Total probability: 100%."
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
  - B · 2-Stage Unwind
  - C · Hard Landing
  - A · Continuation
  - D · External Shock
series:
- name: Subjective Probability
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
    name: B · 2-Stage Unwind
    itemStyle:
      color: '#507f9b'
    tooltip:
      formatter: "B · Two-Stage Unwind (Milder 2001)<br/>Subjective probability: 45%<br/>Multiple compression first, capacity & credit clearing second; hyperscalers and top labs survive."
  - value: 25
    name: C · Hard Landing
    itemStyle:
      color: '#b06e59'
    tooltip:
      formatter: "C · Hard Landing (2000 + Stagflation)<br/>Subjective probability: 25%<br/>Premium collapse, further rate hikes, and cross-defaults hit simultaneously, dragging the macroeconomy into recession."
  - value: 15
    name: A · Continuation
    itemStyle:
      color: '#4f897a'
    tooltip:
      formatter: "A · Bubble Continuation (1998 Replay)<br/>Subjective probability: 15%<br/>A 20%–30% pullback followed by new highs; delays the major peak at the cost of a larger final reckoning."
  - value: 15
    name: D · External Shock
    itemStyle:
      color: '#aa8746'
    tooltip:
      formatter: "D · Exogenous Shock (Black Swan)<br/>Subjective probability: 15%<br/>Taiwan Strait, Middle East, or major AI safety incident interrupts the standard cycle."
```

Unpacking the four branches:

- **Scenario B (Baseline — Two-Stage Unwind, 45%):** Assumes enterprise diffusion advances slowly on a multi-year clock, the frontier premium gradually narrows, and interest rates stay elevated. **Act I (H1 2027) is multiple compression:** a wave of IPO lock-up expirations collides with decelerating growth, shifting public-market valuation anchors from forward narratives back to current gross margins and pulling the sector down 25% to 35%. **Act II (H2 2027–2028) is capacity and credit clearing:** gigawatt-scale campuses come online in bulk and push GPU rental rates down, peripheral neoclouds and SPVs restructure their debt, Meta or Oracle trims CapEx in early 2028, and the sector draws down 35% to 55% from peak to trough.

- **Scenario C (Hard Landing, 25%):** Open-weight parity punctures the frontier premium, energy inflation forces the Fed into further rate hikes, and SPV cross-defaults hit all at once. Collapsing compute prices break the circular-financing chain, triggering a restructuring-scale crisis—or outright accounting scandal—inside the cash-burning OpenAI loop or among highly leveraged neoclouds. Private credit losses spill over, the AI sector drops more than 60%, industry-wide CapEx is slashed by over 30% in 2028, and the U.S. economy is dragged straight into recession.

- **Scenario A (1998 Replay, 15%):** Adoption rapidly expands into second-tier wedges, the frontier premium holds firm, and interest rates peak. Much like 1998—when the S&P 500 fell nearly 20% before surging for another year and a half to its March 2000 peak—the market digests a 20% to 30% pullback in 2027 and rallies to new highs, pushing the true peak past 2028 at the cost of an even more violent reckoning down the road.

- **Scenario D (Exogenous Shock, 15%):** A Taiwan Strait supply-chain crisis, an escalating war in the Middle East, or a major AI safety incident that triggers a regulatory freeze. If wafer supply is disrupted, the narrative flips overnight from "compute glut" to "absolute shortage," turning existing GPU fleets and local hardware into scarce strategic hard currency.

There is an overlooked macroeconomic linkage here: according to ING's August 2026 estimates, investment in AI software, hardware, and data centers accounted for roughly one-third of U.S. GDP growth in 2026[^30]. That means an economic downturn does not require mass white-collar unemployment to light the fuse—in fact, an empirical paper published by the NBER and IZA in September[^31] found that the average unemployment rate for recent U.S. college graduates aged 22 to 25 stood at 7.3% this summer, well within the normal range since 2022 and showing no statistically significant AI-driven spike. **When a category responsible for one-third of GDP growth decelerates from +77% to zero or negative growth, that deceleration alone is a macroeconomic recession trigger.**

To tell which branch we are actually traveling down, ignore the talking heads and watch this dashboard:

| Signal to Watch | Key Threshold | Path Implication |
| --- | --- | --- |
| Anthropic's first two post-IPO earnings reports | QoQ revenue growth above **25%** vs. below **10%** | Above 25% points toward **A (Continuation)**; below 10% points toward **B (Two-Stage Unwind)** |
| Anthropic's year-end 2026 annualized revenue | Whether it surges from **~$67B** to the expected **$110B** | A wide miss confirms the coding wedge is downshifting |
| Long-term & on-demand GPU rental rates | When rates **stop rising and roll over** | A rollover signals new capacity has caught up with demand, kicking off **Act II of B** |
| Junior tranche yields on off-balance-sheet AI debt | Whether yields keep widening after jumping from **8.5%** to **10%+** | Continued widening signals rising risk of peripheral credit defaults |
| OpenAI's 2027 IPO | Whether it clears smoothly at a **$1T** valuation | Another delay or a down-round IPO is a strong top signal |
| Early-2028 CapEx guidance | Whether **Meta** or **Oracle** cuts guidance first | Separates **B (Orderly Unwind)** from **C (Hard Landing)** |

## 6. The Endgame: As the Coasean Boundary Collapses, Are We New Freeholders or Digital Sharecroppers?

Step back from the next two years of market swings and look past 2028. Whether the transition plays out as an orderly digestion or a violent shakeout, three hard structural realities will define the landscape once the tide goes out:

**First, SaaS will not be wiped out, but "thin-wrapper UIs" are dead.** Public markets already priced in the initial "AI kills traditional software" panic earlier this year: between mid-January and mid-February 2026, North American software stocks shed roughly $1 trillion in market cap, and Salesforce fell 40.9% in the first half of the year[^32] as Wall Street realized that agents compress seat-based licensing. Yet software spending is not disappearing; it is mutating. SaaS products that amount to a thin workflow UI will be crushed by in-house enterprise agents, while foundational software that holds core business state—true **Systems of Record**—will survive and pivot from charging per seat to charging per delivered outcome.

**Second, an accounting write-down is not physical scrap—the legacy of cheap compute will be far larger than most expect.** A common worry is that GPUs become obsolete in five years, leaving behind none of the thirty-year physical legacy of 19th-century railroads or 2000-era dark fiber. That conflates two different things: **financial bankruptcy wipes out book debt and depreciation schedules on a balance sheet, but the physical silicon does not evaporate.** Once peripheral SPVs default, restructure, and take massive accounting write-downs, those H100 and B200 clusters—now stripped of their capital cost—will keep humming at full load as long as the price per million tokens covers the marginal cash cost of electricity and data-center operations. Add in the gigawatt-scale data-center shells that have already cleared multi-year permitting bottlenecks and built out substations, and the token cost per unit of capability will very likely drop another order of magnitude by 2028.

**Third, the Coasean boundary of the firm will collapse, pushing one-person companies (OPCs) from the fringes into the mainstream.** Nobel laureate Ronald Coase answered why firms exist back in his 1937 paper *The Nature of the Firm*: companies hire hundreds or thousands of employees and tolerate bloated hierarchies because **market transaction costs—search, contracting, delivery, and verification—are too high**. When AI drives down external transaction costs faster than large corporations can eliminate internal coordination friction, the optimal boundary of the firm shrinks inward—all the way down to **a single person**.

This shift does not need to wait for the bubble to burst. Economic historian Paul David famously showed why manufacturing productivity took roughly forty years to take off after the invention of the electric dynamo in the late 19th century: factories built around a central steam-driven line shaft had to retire before new plants designed natively around **unit drive**—putting an independent electric motor on every machine—could take over the market. **Today's AI-native one-person companies and three-to-five-person engineering teams are those unit-drive factories.** Feeding on collapsing commodity token prices, they are already growing rapidly on the edges; the capital shakeout of the next two years will simply act as an **accelerator**, flooding the market with cheap compute and top-tier talent.

Still, before giving in to rosy techno-optimism, it is worth asking a colder question:

**When one-person companies bloom everywhere, will we have ushered in a class of "new freeholders" who own their means of production—or merely created a class of "digital sharecroppers" who bear all their own risk while working for compute empires?**

For one thing, AI does not repeal power-law distributions. A tiny fraction of solo companies run by elite architects and domain veterans will indeed generate the revenue of a hundred-person firm; the vast majority near the median will remain micro-operators barely scraping by.

More importantly, **who captures the economic surplus?** Ask yourself: when hyperscalers find that raw GPU compute has turned into a low-margin commodity and their free cash flow is under pressure, where will they claw back their margins? **They will lean on ecosystem lock-in—defending or quietly raising prices on traditional high-margin cash cows like storage, managed databases, and network egress fees.**

If a solo operator's model intelligence, context memory, core transactional database, and distribution and payment rails are all locked into two or three surviving cloud and model oligopolies, then every dollar saved from falling transaction costs will eventually be taxed away through token premiums, state-storage rents, and platform tolls. The vaunted "one-person company revolution" would do little more than turn Big Tech employees once protected by labor laws into zero-base-salary digital sharecroppers—bearing 100% of market risk while paying monthly rent to cloud landlords.

What separates a freeholder from a sharecropper has never been how clever your prompts are. It comes down to two things:

1. **Hot-swappable open-weight model alternatives that keep you from being held hostage to any single closed-source premium.**

2. **A sovereign core data stack that you fully control, can migrate across clouds at will, and can run on bare metal or local hardware.**

On the surface, the 2026–2028 shakeout is the unwinding of Wall Street's trillion-dollar CapEx bubble. Beneath the surface, it is the opening battle over **who owns the technological surplus of the next thirty years**.

The bubble will eventually clear. When the waters recede and we climb the Slope of Enlightenment, may you stand as a free builder who owns your foundation and means of production—not a tireless digital sharecropper tending someone else's cloud plantation.

## References

[^1]: [North America's four hyperscalers have pushed their 2026 CapEx guidance to roughly $725 billion](https://startupfortune.com/big-techs-725-billion-ai-spending-wave-is-turning-free-cash-flow-into-a-distant-memory/)

[^2]: [Bank of America estimates that this spending wave will consume 94% of the hyperscalers' operating cash flow](https://247wallst.com/investing/2025/11/10/bank-of-america-just-issued-a-stark-warning-the-ai-boom-is-hitting-a-cash-crunch/)

[^3]: [Alphabet recorded roughly -$5.9 billion in free cash flow in Q2 2026](https://www.tikr.com/blog/alphabets-free-cash-flow-just-went-negative-heres-what-the-debt-behind-it-says)

[^4]: [Anthropic is sprinting toward an IPO at a target valuation of $1.8 trillion to $2 trillion](https://www.techmeme.com/261014/p56)

[^5]: [OpenAI has confirmed it is delaying its IPO window to 2027](https://thenextweb.com/news/openai-ipo-delay-2027-altman-1-trillion)

[^6]: [U.S. Census Bureau Business Trends and Outlook Survey (BTOS)](https://www.wework.com/ideas/research-insights/the-new-ai-divide)

[^7]: [ING estimate on U.S. AI adoption and economic contribution](https://talkmarkets.com/article/how-much-is-ai-contributing-to-us-economic-growth-1787193106)

[^8]: [The Federal Reserve voted unanimously in September 2026 to raise rates by 25 bps to 3.75%–4.00%](https://www.raisin.com/en-us/news/fed-rate-decision-policy-breakdown-september-2026/)

[^9]: [Financial figures leaked from Anthropic's October 14 investor presentation](https://lilithai.dev/radar/anthropic-tells-investors-quarterly-revenue-up-nearly-50-to-16-8bn-ahead?lang=en)

[^10]: [Up to 54% of enterprise spending on AI coding goes to Anthropic alone](https://valueaddvc.com/blog/openai-vs-anthropic-which-ai-company-is-winning-the-enterprise-in-2026)

[^11]: [Anthropic's QoQ revenue growth decelerated from roughly 140% in Q2 to roughly 46% in Q3](https://www.techmeme.com/261014/p56)

[^12]: [Anthropic told investors that "distillation" previously accounted for 5% to 7% of total revenue](https://lilithai.dev/radar/anthropic-tells-investors-quarterly-revenue-up-nearly-50-to-16-8bn-ahead?lang=en)

[^13]: [Operators linked to Alibaba's Qwen team allegedly conducted roughly 28.8 million interactions with Claude across nearly 25,000 fake accounts between April 22 and June 5](https://www.binance.com/en-IA/square/post/346765717322417)

[^14]: [Anthropic disclosed a $65 billion annualized revenue run-rate in late July 2026](https://aibusinessweekly.net/p/anthropic-statistics)

[^15]: [Investor expectations for Anthropic's year-end annualized revenue reach $100 billion to $110 billion](https://www.cnbc.com/2026/10/14/anthropic-third-quarter-revenue-16-8-billion.html)

[^16]: [Chinese open-weight models have captured over 30% of weekly U.S. enterprise token volume on OpenRouter since February 2026, peaking at 46.4% in mid-July vs. 35.7% for U.S. models](https://taskpool.ai/blog/chinese-ai-models-enterprise-risk)

[^17]: [DeepSeek V4 Flash costs $0.14 per million input tokens vs. $5.00 for GPT-5.5; San Francisco startup Lindy cut inference costs by 90% after switching from Claude](https://followin.io/vi/feed/26363711)

[^18]: [The $60 billion "Project North Star" chip financing deal](https://www.livemint.com/ai/artificial-intelligence/anthropic-offers-blackstone-double-digit-yield-in-chip-financing-deal-what-the-60-billion-deal-entails-11792204532812.html)

[^19]: [KBRA rates Anthropic at BB+, one notch below investment grade](https://thedeepdive.ca/anthropics-junk-credit-rating-went-unreported-during-35-billion-ai-financing/)

[^20]: [Apollo and Blackstone close $35 billion chip financing deal for Anthropic](https://thepaypers.com/fintech/news/apollo-and-blackstone-close-usd-35-billion-chip-financing-deal-for-anthropic)

[^21]: [The junior tranche coupon in the June 2026 financing was 8.5%](https://ng.investing.com/news/company-news/apollo-blackstone-finalize-35-billion-ai-chip-financing-for-anthropic-2546759)

[^22]: [Anthropic's compute and cloud commitments over roughly the next decade total at least $518 billion](https://origami.sa/en/blog/anthropic-ipo-prospectus-risk-factors/)

[^23]: [BofA analyst Tom Curcuruto estimates the Broadcom AI financing platform could carry up to $370 billion in senior debt by mid-2029](https://www.benzinga.com/markets/prediction-markets/26/08/61219624/broadcom-ai-financing-370-billion)

[^24]: [Microsoft disclosed in January 2026 that roughly 45% of its $625 billion commercial RPO is tied directly to OpenAI](https://thedailydollar27.substack.com/p/microsofts-625-billion-signal-most)

[^25]: [SoftBank secured a $40 billion unsecured bridge loan maturing March 25, 2027 to fund its $30 billion follow-on investment in OpenAI](https://www.investing.com/news/stock-market-news/softbank-secures-40-billion-loan-to-fund-openai-investment-93CH-4584494)

[^26]: [SemiAnalysis data showing 1-year contract hourly rates for H100s rose nearly 40%, from $1.70 in October 2025 to $2.35 in March 2026](https://eu.36kr.com/zh/p/4022220823171208)

[^27]: [Neocloud provider Nebius raised on-demand H100 pricing from $3.85 to $4.50 and hiked B300 pricing by 21%](https://timeline.sohu.com/news/kvIswyTgRy)

[^28]: [Ofek and Richardson (2003), "DotCom Mania: The Rise and Fall of Internet Stock Prices," *Journal of Finance*](https://econpapers.repec.org/RePEc:bla:jfinan:v:58:y:2003:i:3:p:1113-1137)

[^29]: [Anthropic projected $190 billion to $200 billion in 2028 revenue in investor presentations](https://aibusinessweekly.net/p/anthropic-statistics)

[^30]: [ING estimates from August 2026 showing AI software, hardware, and data center investment accounted for roughly one-third of 2026 U.S. GDP growth](https://talkmarkets.com/article/how-much-is-ai-contributing-to-us-economic-growth-1787193106)

[^31]: [NBER and IZA empirical paper published in September 2026 on recent graduate unemployment](https://docs.iza.org/dp18945.pdf)

[^32]: [Salesforce shares fell 40.9% in H1 2026](https://www.saasrise.com/news/salesforce-shares-plunge-40-in-h1-2026-amid-aiagentic-fear-b14605d4-a9bc-4622-b92d-50b6f04ca459)
