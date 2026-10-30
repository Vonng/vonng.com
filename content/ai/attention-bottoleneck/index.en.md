---
title: "After the Attention Wall, What Keeps the AI Boom Alive?"
date: 2026-10-30
authors: [vonng]
summary: >
  AI coding and micro-dramas have both hit the ceiling of human attention, and personal agents cannot pick up the slack. AI for Science and embodied AI could drive the next wave, but neither will scale before the infrastructure bill comes due.
tags: [AI, Business, Commentary]
images: [wall.webp]
ai: true
---

> Data as of October 30, 2026. Based on discussions with Claude and Gemini. Nothing here is investment advice.

*Compute hits the attention wall.*

When I wrote "[Welcome to the AI Secretary Boom](/en/ai/secretary-era/)" and "[How Will the AI Bubble Burst?](/en/ai/ai-bubble/)" recently, I noted that the industry had pinned this trillion-dollar compute buildout on a single bet: whether personal secretary agents could cross into mainstream adoption. Only tens of millions of people write code worldwide, while billions use smartphones. Chat subscriptions and coding tools alone cannot pay a bill of this size.

A month later, after testing Meta's Muse, Manus's Cue, and several new personal assistants, my takeaway is simple: **secretaries will not save the narrative.** That leaves a practical question: where are paid tokens actually going right now? Once today's main pools hit the ceiling of human attention, what keeps the AI story going—and can any of it arrive before the bubble clears?

## 1. Two Main Pools Hit the Wall at Once

Look across global compute consumption today, and only two large pools have working commercial loops where buyers keep paying: enterprise **software engineering** in the US, and **video generation**—led by micro-drama apps like ByteDance's Hongguo—in China.

In June, Chinese digital publisher COL Group (中文在线) shared a breakdown of domestic token consumption in an investor briefing: AI micro-dramas and video generation took 55%, e-commerce marketing 24%, and software development 15%. Commentators often pair that with a widely cited estimate that 58% of US token consumption goes to writing code. The exact numbers are debatable, but the split holds up: **the US uses AI to write code; China uses AI to make micro-dramas. One is anchored in production, the other in consumption.**

The problem is that both pools have just hit a wall at the same time.

![featured.webp](featured.webp)

### Vibe Coding Fatigue

On the production side, fatigue showed up first among heavy users. Talking recently with several friends who run fleets of coding agents in parallel, I heard the same thing from all of them: they have run out of ideas worth building. As I argued in "[AI Software Engineering: Choose Problems You Care About](/en/ai/ikigai/)," building anything of real value takes sustained human attention—you cannot just type a wish into a prompt and call it done.

**Total token volume has not dropped, but marginal usage has shifted from high-density greenfield builds to routine maintenance.** Starting a new project and designing an architecture require expensive frontier flagships; once a workflow settles into routine checks and bug fixes, cheap small models or open-weight models are good enough. For model labs counting on frontier pricing premiums to recoup their capex, a drop in marginal value per token is worse than a drop in raw API calls.

GitHub shows the same congestion. New repositories are surging, and every niche is packed with vibe coders holding hammers in search of nails. Search any problem space and you will find dozens of AI-generated wheels. Code generation can speed up without limit, but software still ends with a person: developers reviewing diffs, and users finding, testing, and debugging tools. All of that burns human attention. Even if an agent tests candidate repos for you, a human still makes the final call.

The bottleneck in software has shifted from production to distribution and consumption.

### Micro-Dramas: Viewers Stayed, Supply Flooded the Zone

In January, ByteDance's micro-drama app Hongguo passed 100 million daily active users, becoming the company's fifth app to hit that mark after Toutiao, Douyin, Doubao, and Fanqie Novel. According to QuestMobile, Hongguo's average daily time spent per monthly active user reached roughly 151 minutes in Q3—first among all major Chinese mobile apps, ahead of WeChat and Douyin. China's overall micro-drama market has already overtaken its annual box office.

Consultancy CIC (灼识咨询) estimates that AI micro-drama releases will jump from 60,000 titles in 2025 to a projected 170,000 this year. COL Group cites an even higher figure: over 40,000 new releases per month in Q1 alone, matching the entire 2025 output of live-action micro-dramas. The two definitions differ, but the scale is clear: supply growth has outrun human attention by more than an order of magnitude.

I have used Hongguo for a long time, yet I have not opened it in weeks. With hundreds of thousands of shows piled up, there is no way to keep pace. After enough episodes, the recycled tropes blur into fatigue. Without a micro-drama equivalent of Douban (China's IMDb/Letterboxd) to filter out junk, finding a good show through organic recommendations has gotten hard.

Micro-dramas are broadcast media: tokens are burned on the supply side, but monetized on the consumption side. Once viewer attention tops out at 151 minutes a day, multiplying supply tenfold adds zero watch time—it only dilutes traffic. Starting in Q2, orders for external production teams shrank as platforms built in-house studios to control cost and quality. Douyin committed over RMB 1.5 billion in minimum guarantees for live-action micro-dramas this year, while Hongguo reportedly tightened guarantees for photorealistic AI series (Hongguo disputed parts of those reports). Once viewer attention hit the ceiling, platforms stepped in and hit the brakes on AI supply.

### The Attention Ceiling

Code and micro-dramas have hit the same wall: on the production side, the mental bandwidth to scope and review work; on the consumption side, the hours available to watch.

Herbert Simon pointed this out in 1971: a wealth of information creates a poverty of attention. Half a century later, generative AI has pushed that constraint to the limit.

Global compute consumption roughly follows a simple equation:

> **Token Consumption ≈ Human Attention × Token Density per Attention-Minute + Background Machine Loops**

A few billion people stay awake for sixteen hours a day. Whether they spend that time reviewing code or watching micro-dramas, the total pool of human attention is fixed. Machines can spin in the background on their own: suppliers can roll the dice on endless low-grade videos, and the more slop AI generates, the more AI is needed to filter and summarize it—just like the old spam-versus-antispam arms race.

**So human attention does not cap raw token throughput, but it caps effective commercial revenue.** Unless machines can close the loop in the physical or business world without human review, the bill is ultimately settled based on the value humans actually absorb and sign off on.

During a bubble, you can pitch the market on throughput; when the bubble clears, you settle up in revenue. In the 2000 dot-com crash, the market priced companies on eyeballs first and liquidated them on profits later. Right now, a gap is opening: COL Group's own token call volume is still growing more than 20% week over week, while Anthropic's quarter-over-quarter revenue growth slowed from roughly 140% in Q2 to about 46% in Q3.

The scarcer attention gets, the more weight shifts to distribution channels. Micro-dramas show this clearly: industry practitioners note that ByteDance's Seedance is currently the only video model capable of industrial-scale production, and ByteDance also owns Hongguo, the largest distribution funnel. With the model in one hand and traffic in the other, ByteDance squeezes independent studios from both sides. **Once supply is no longer scarce, traffic entry points and distribution channels hold the pricing power.**

## 2. Personal Secretaries Won't Save the Compute Narrative

With the existing pools topping out, the market placed its hopes on personal assistant agents. The pitch is appealing: billions of smartphone users, each with a digital secretary and a cloud computer burning tokens in the background 24/7. Yet once you actually use these assistants for a few weeks, the illusion fades fast.

**Hurdle 1: Nothing worth delegating.** For a few dozen dollars a month, anyone can feel like an executive. The problem is that **in the past, only executives had secretaries—not just because secretaries were expensive, but because only executives had enough work worth delegating.** For an ordinary person, ordering takeout, replying to a message, or adding a calendar event takes seconds; explaining the context to a secretary takes more work than doing it yourself. As I wrote in "[How Do You Burn Through 10 $200 Codex Subscriptions?](/en/ai/10x-subscription/)," AI is a multiplier, not an adder. If the multiplicand is near zero, a bigger multiplier still yields near zero.

**Hurdle 2: Real life has no `ROLLBACK`.** Once money is sent, a home address is shared, or a message goes out, you cannot take it back. Almost every high-value action in the real world is irreversible and has to run as a two-phase commit: a secretary can compare prices, draft messages, and fill out forms to finish the `PREPARE` step, but you still have to press `COMMIT` and own the outcome yourself. That is why coding became a breakout wedge while personal assistants struggle: if code breaks, you fix it or revert; in daily life, consequential decisions pull your own attention right back in at the final step.

**Hurdle 3: Gatekeepers closed the doors.** Trillion-dollar capex is never paid back by subscriptions alone; it is paid back by sitting at transaction chokepoints and taking a cut or selling ads. Super-apps have given a uniform answer: no. When ByteDance's Doubao phone assistant launched late last year, WeChat started forcing users offline the next night. Shortly after Meta's Muse hit number one on the US App Store, Amazon blocked it from placing orders on its site. Shopify opened its doors, but the largest platforms shut theirs. Without transaction cuts and ad revenue, a secretary is left with a small monthly fee—nowhere near enough to cover the compute buildout.

**Hurdle 4—and the most basic: It is a tool that saves time, not a sink that kills time.** Entertainment apps run with human nature: the more idle you are, the more compute they burn. A secretary is event-driven: it wakes up when a task arrives and goes back to sleep when done. Everyday tasks like managing calendars, replying to emails, and logging expenses are shallow, short-chain jobs. They neither run for hours in recursive loops like coding agents nor need an expensive frontier model; cheap small models or on-device models will eventually handle them. Personal agents will become common, but they cannot support frontier model margins.

Counting on digital secretaries to rescue token revenue was looking in the wrong place from the start.

## 3. Two Next-Wave Trunks, Too Slow for the Debt Clock

Set personal secretaries aside. To bypass or break through the human attention ceiling, the remaining options on the table grow out of two main trunks: one extends coding's verifiable reasoning so machines can work in closed loops without human review; the other pushes video generation deeper into **World Models**.

### Verifiable Reasoning: From Back-Office Automation to AI for Science

The first trunk splits verifiable reasoning into two branches. The near-term branch is enterprise **back-office automation** (SQL, ops, reconciliation, customer support), where outputs feed directly into business workflows without passing through human eyeballs. The long-term branch pushes into basic research: **AI for Science**.

The commercial logic for AI for Science is straightforward: if a frontier model with a one- or two-generation lead can work like a top scientist, why settle for selling tokens by the million? Model labs can step onto the field themselves to go after ***big results***—turning compute into mathematical proofs, chip layouts, new material formulas, and drug molecules, and making money on patents.

The shovel-sellers have already started digging for gold. Two days ago, Anthropic disclosed its acquisition of [Mithril Medicine](https://www.rdworldonline.com/anthropic-acquires-mithril-medicine-one-person-biotech/). Closed in July, the deal bought a one-person-company (OPC) biotech with a single full-time employee, whose two rare muscular dystrophy programs became Anthropic's first internal drug pipeline. Earlier in April, Anthropic paid roughly $400 million in stock for Coefficient Bio, a team of fewer than ten people; on October 20, OpenAI bought drug-discovery agent startup Orchestra Bio.

Yet Mithril—that exact one-person biotech—exposes the bottleneck in this track. Working alone, its founder used Claude to coordinate 11 contract labs and took a therapy candidate from concept to positive mouse data in under 18 months. Design and coordination were compressed to the limit, but contract labs still have to manufacture the antibodies, wet labs still have to measure binding affinity, and mice still have to be raised and tested one by one. Human clinical trials will not start until late 2028 at the earliest.

**AI can compress thinking time, but it cannot compress physical reaction time.** Walk into scientific research, and the attention ceiling simply becomes the **experimental throughput ceiling**. Within AI for Science, subfields sort by how easily results can be verified: **mathematical proofs**, which machines can check in a closed loop, move fastest; **chip design**, where everything before tape-out can be simulated and rolled back, comes next; **new materials**, which require lab synthesis and testing, move slower; and **novel drugs**, which need years of irreversible testing in mice, monkeys, and humans, sit at the back of the line.

### World Models: Real-Time Games and Embodied AI

The second trunk follows video generation deeper into **World Models**, splitting commercially into two branches: on the virtual side, real-time generative games and the metaverse; on the physical side, embodied AI.

Games are the ultimate sink for compute. Anyone who has played *Stellaris* knows the picture: once a civilization's material output outstrips physical needs, idle populations are placed into custom virtual worlds, burning compute nonstop to produce happiness and social stability. In terms of our earlier equation, a micro-drama is broadcast media—generated once, watched by millions—so token usage per minute of attention is tiny. A real-time generative game can be a one-on-one session: if a player is online for an hour, the model runs inference for an hour. **With total human attention fixed, the only way to multiply compute demand by orders of magnitude is to raise token density per minute of attention.** Real-time interactive games turn the attention ceiling into a compute floor.

Under the hood, both branches share the same technical base: generating an interactive virtual world on screen in real time and simulating physical environments so a robot can plan actions follow the same path. Their tolerances differ—a game only needs to look plausible, while a robot must get physical interactions right to replace human physical labor outside the attention pool. Seen from this angle, the hundreds of thousands of AI micro-dramas on Hongguo today are society paying tuition for video models—a pre-training subsidy for future world models.

In practice, though, gaming is still stuck at the porting stage: studios use AI to make traditional games faster and cheaper, nowhere near real-time custom generation, because inference costs too much. Embodied AI is further out, held back by physical interaction data and hardware costs, and remains at least three to five years away.

Put the two trunks side by side and an ironic paradox for compute infrastructure appears: **one side is a "slow variable" that no pile of GPUs can rush; the other is an "expensive variable" that cannot survive unless GPU prices crash.** Research is gated by lab throughput, robotics by data and hardware, and enterprise back offices by compliance rules—building more data centers will not speed up mouse trials or corporate governance. Real-time games could absorb massive compute tomorrow, but they are blocked by high unit inference costs—unless data centers are overbuilt until compute prices collapse.

And that is exactly what the bubble is doing.

## 4. A Race That Won't Beat the Credit Clock

Plot every direction on two axes: how much value each token generates, and how fast that value turns into cash.

A trillion-dollar capex bill needs cash cows in the top-right quadrant: high value, fast payback. Right now, the only workload in that quadrant—coding—is running into the attention wall.

Meanwhile, the capital market's clock is ticking. In my bubble essay, my base case (45% probability) was a two-stage unwind: valuation compression in the first half of 2027, followed by peak capacity delivery and credit clearing from late 2027 into 2028. That leaves a window of one to two years for a new revenue driver to take over.

```echarts {height="540px" full=true class="overflow-hidden"}
animation: false
backgroundColor: transparent
textStyle: {fontFamily: 'system-ui, sans-serif'}
aria:
  enabled: true
  description: Qualitative chart. X-axis shows payback speed; Y-axis shows value density per token. Coding sits in the top right but is hitting the attention wall. AI for Science, back-office automation, and embodied AI offer high value but slow payback. Personal agents and games sit in the bottom left; micro-dramas sit in the bottom right. The dashed arrow shows how a 10x drop in compute cost could speed up payback for games.
title:
  - text: Trillion-Dollar Capex Needs the Top Right
    subtext: Coding is the only workload there—and it is hitting the attention wall
    left: 4
    top: 8
    textStyle: {fontSize: 20, fontWeight: 650}
    subtextStyle: {fontSize: 12}
  - {text: 'High value, slow payback', left: 52, top: 88, textStyle: {fontSize: 12, fontWeight: 400}}
  - {text: Quadrant the bubble needs, right: 16, top: 88, textStyle: {fontSize: 12, fontWeight: 650}}
  - {text: 'Low value, slow payback', left: 52, bottom: 58, textStyle: {fontSize: 12, fontWeight: 400}}
  - {text: 'Fast payback, low value', right: 16, bottom: 58, textStyle: {fontSize: 12, fontWeight: 400}}
tooltip:
  trigger: item
  triggerOn: mousemove|click
  confine: true
  extraCssText: 'max-width: 230px; white-space: normal; line-height: 1.6;'
grid: {left: 52, right: 16, top: 88, bottom: 58}
xAxis: &axis
  type: value
  min: 0
  max: 100
  name: 'Payback Speed: Slow → Fast'
  nameLocation: middle
  nameGap: 24
  nameTextStyle: {fontSize: 13}
  axisLabel: {show: false}
  axisTick: {show: false}
  axisLine: {show: true, lineStyle: {opacity: 0.5}}
  splitLine: {show: false}
yAxis:
  <<: *axis
  name: 'Value per Token: Low → High'
  nameGap: 28
series:
  - type: scatter
    symbolSize: 14
    itemStyle: {color: '#80918a', opacity: 1}
    label: {show: true, formatter: '{b}', position: right, distance: 10, fontSize: 14, fontWeight: 550, textBorderColor: transparent}
    emphasis: {scale: 1.5, itemStyle: {shadowBlur: 12, shadowColor: 'rgba(59,130,246,0.25)'}}
    data:
      - {name: AI for Science, value: [6, 88], tooltip: {formatter: '<b>{b}</b><br>Bottlenecked by wet-lab throughput and clinical trial timelines.'}}
      - {name: Back-Office Automation, value: [30, 74], tooltip: {formatter: '<b>{b}</b><br>Bottlenecked by liability and enterprise governance; rollout takes years.'}}
      - {name: Embodied AI, value: [9, 60], tooltip: {formatter: '<b>{b}</b><br>Bottlenecked by physical data and hardware; still 3–5 years out.'}}
      - {name: Coding, value: [74, 83], symbolSize: 22, itemStyle: {color: '#3b82f6'}, label: {fontWeight: 700}, tooltip: {formatter: '<b>{b}</b><br>Already monetizing, now hitting the human attention wall.'}}
      - {name: Personal Agents, value: [21, 37], tooltip: {formatter: '<b>{b}</b><br>Bottlenecked by trust, irreversible actions, and platform gatekeepers.'}}
      - {name: 'Micro-Dramas / Video', value: [80, 30], label: {position: left}, tooltip: {formatter: '<b>{b}</b><br>High volume, low value; revenue is capped by viewer attention.'}}
      - {name: 'Games / Metaverse', value: [27, 17], label: {position: bottom}, tooltip: {formatter: '<b>{b}</b><br>Bottlenecked by unit compute cost. Needs a 10x price drop to shift right.'}}
    markArea:
      silent: true
      itemStyle: {color: 'rgba(148,163,184,0.04)'}
      label: {show: false}
      data:
        - [{xAxis: 0, yAxis: 50}, {xAxis: 50, yAxis: 100}]
        - [{xAxis: 50, yAxis: 50, itemStyle: {color: 'rgba(59,130,246,0.09)'}}, {xAxis: 100, yAxis: 100}]
        - [{xAxis: 0, yAxis: 0}, {xAxis: 50, yAxis: 50}]
        - [{xAxis: 50, yAxis: 0}, {xAxis: 100, yAxis: 50}]
    markLine:
      silent: true
      symbol: none
      label: {show: false, textBorderColor: transparent}
      lineStyle: {color: '#94a3b8', width: 1, type: solid, opacity: 0.45}
      data:
        - {xAxis: 50}
        - {yAxis: 50}
        - [{coord: [29, 17], lineStyle: {type: dashed, color: '#b88746', opacity: 1}, label: {show: true, formatter: After 10x cheaper compute, position: middle, fontSize: 12}}, {coord: [73, 17], symbol: arrow}]
```

*Qualitative illustration, not empirical measurements; hover or tap each point to view its bottleneck.*

Line up the contenders on the other side of this race, and none of them will arrive in time:

- **Enterprise back-office automation** is the closest to paying off: in SQL, ops, reconciliation, and customer support, outputs are consumed by workflows rather than human eyes, so attention does not cap it. Instead, it is gated by liability and institutional rules—every industry has to build sandboxes, audit trails, and accountability mechanisms first. Rollout is measured in years, not quarters.
- **Mathematical proofs** are making real progress, but a theorem rarely turns into tens of billions of dollars in annual revenue.
- **Chip design** may show results between 2027 and 2028, but taking a chip from layout to tape-out and mass production takes years; the cash comes back slowly.
- **Novel drugs**, even moving as fast as Mithril, will not reach clinical trials until late 2028. Early assets can be licensed out for upfront payments, but against a trillion-dollar buildout, that is a drop in the bucket.
- **Embodied AI** is three to five years away.

The biggest miss is real-time generative gaming. It faces a hard financial constraint: **compute cost per user-hour must fall below what one hour of human attention can monetize.** At current ad and gaming monetization rates, an hour of attention is worth roughly a few dozen cents. As long as real-time inference costs far more than that, the business model does not close. Cost is not the only problem either—visual consistency, latency, and gameplay design are still unsolved.

All of these paths are real, and most will likely work—they just cannot beat the bubble's maturity schedule. In my previous essay, I left room for a "1998-style boom," where the market pulls back 20% to 30% before rallying to new highs if wedges expand fast enough. With the old pools hitting the attention wall and the new pools too slow to bridge the gap, the odds of that scenario need to come down further.

## 5. The Bubble's Crash Sets Up the Sequel

If revenue cannot beat the credit clock, a downcycle is hard to avoid. Over a longer horizon, though, a bursting bubble is never the end of a technology wave.

After the dot-com crash in 2001, telecom carriers that had borrowed heavily to lay fiber went bankrupt and restructured one after another, leaving vast networks of unlit "dark fiber" underground. It took years to absorb that excess capacity, and what finally put it to work was YouTube and streaming video—bandwidth-heavy businesses whose unit economics never would have penciled out at peak bubble prices. The wreckage of the bubble became the foundation for the next phase.

This AI cycle will likely follow the same script, and the bubble will leave behind more than GPUs. Permitted power allocations, gigawatt-scale data center shells with substations already built, and a cohort of battle-tested engineers will all remain as fuel for the next cycle.

**The exact bottleneck blocking games and world models today—unit compute cost—is what a bursting bubble will clear.** Once compute prices drop by 90% or 99%, "wasting compute" becomes commercially viable for the first time. At that point, real-time rendered games, evolving virtual worlds, and always-on world models stop being luxuries; applications that make no financial sense today will grow on top of cheap compute. **The death of the bubble is the precondition for the sequel.**

In that post-bubble world of **surplus compute and scarce attention**, the winning cards at the table are straightforward:

**The first card is distribution.** Compute and content can expand without limit, but human attention cannot be printed by a single extra second. Whoever controls the entry points to human attention holds ultimate pricing power.

**The second card is trust and curation.** The more AI floods the world with cheap output, the more people need reliable filters: micro-dramas need a Douban, and GitHub needs someone who can tell you which of fifty AI-built wheels is safe to run in production. Work that is actively maintained, backed by a real reputation, and owned by someone accountable when things break will command a premium again.

**The third card belongs to those who own their data foundations and business context.** Once the shakeout turns model inference into a cheap utility like electricity or water, the only scarce inputs left on the production side will be your own agency and core data. When the tide goes out, whether you capture the dividend of cheap compute as a freeholder or pay rent on someone else's cloud plantation comes down to two things: whether you can hot-swap the most cost-effective models at will, and whether you keep your core data in your own hands.

Machines can produce without limit, but humans still get only 24 hours a day. The wall this trillion-dollar bubble finally hits may not be compute or power, but the attention wall of flesh-and-blood humans.

What is on the other side of that wall? Likely a world where compute is cheap enough to burn freely. When that day comes, we can talk properly about games.

## References

- [Vonng: Welcome to the AI Secretary Boom](/en/ai/secretary-era/)
- [Vonng: How Will the AI Bubble Burst?](/en/ai/ai-bubble/)
- [Sina Finance / *Caijing*: Hongguo Time Spent and AI Micro-Drama Supply](https://t.cj.sina.com.cn/articles/view/1684012053/645ffc1501901snk2)
- [IT Home: Hongguo Crosses 100M DAU, Becoming ByteDance's Fifth 100M-DAU App](https://www.ithome.com/0/925/921.htm)
- [CLS (Cailianshe): China's Micro-Drama Market Surpasses Full-Year Box Office](https://www.cls.cn/detail/2064298)
- [*21st Century Business Herald*: AI Micro-Dramas Become the Largest Token Consumption Scenario](https://news.10jqka.com.cn/20260604/c677210327.shtml)
- [Caiwen: COL Group Investor Relations Activity Record](https://news.10jqka.com.cn/20260604/c677213256.shtml)
- [Huxiu: Fact-Checking Three Trending Claims Around AI Micro-Dramas](https://www.huxiu.com/article/4896918.html)
- [Huxiu / Zuihua: Hongguo's Pivot as Live-Action Micro-Dramas Regain Ground](https://m.huxiu.com/article/4863444.html)
- [R&D World: Anthropic acquires a one-person biotech that used Claude to coordinate 11 labs](https://www.rdworldonline.com/anthropic-acquires-mithril-medicine-one-person-biotech/)
- [Techstrong.ai: Anthropic Acquires One-Person Mithril Medicine](https://techstrong.ai/articles/anthropic-acquires-one-person-mithril-medicine-in-major-ai-drug-discovery-expansion/)
- [The Decoder: Anthropic Acquires Coefficient Bio](https://the-decoder.com/anthropic-drops-400-million-in-shares-on-an-eight-month-old-ai-pharma-startup-with-fewer-than-ten-employees/)
- [Axios: OpenAI acquires Orchestra Bio](https://www.axios.com/2026/10/20/exclusive-openai-biotech-startup-drug-development)
