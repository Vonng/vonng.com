---
title: "AI Adoption May Not Run That Deep"
date: 2026-10-16
authors: [vonng]
summary: >
  From 2 billion chatbot users to 5,000 frontier lab insiders: a five-tier Fermi estimate of AI adoption shows broad reach, but surprisingly shallow depth.
tags: [AI, Agent, Commentary]
---

At DevDay in late September, OpenAI reported a staggering figure: [1.2 billion people use ChatGPT every week](https://openai.com/index/devday-2026-recap/). Two weeks later, Andrej Karpathy threw out a very different number: only about 5,000 people worldwide have seen frontier AI running at full tilt—a 240,000x gap.

Both numbers match what I see firsthand. I keep a dozen top-tier subscriptions active and orchestrate just as many agents around the clock. Meanwhile, most of my friends still use AI to polish copy, look things up, or chat to pass the time. We all call it "using AI," but we aren't using the same thing at all.

How many people actually push AI this hard? In "[AGI Machine Guns Are Now Standard Issue](/en/ai/ai-machinegun-for-everyone/)," I guessed fewer than 100,000. Today I want to pull together the public data and run a proper Fermi estimate. The short version: **plenty of people have tried AI, but remarkably few use it deeply.**


## The Gap in Karpathy's Funnel

On October 11, Karpathy reworked a note he had written in April into a four-tier funnel ([post breakdown](https://cellcog.ai/blog/karpathy-llm-understanding-funnel/)). As an OpenAI co-founder who [joined Anthropic this May](https://fortune.com/2026/05/19/who-is-andrej-karpathy-vibe-coding-anthropic-openai-rubiks-cube/), he has a clear view of what happens inside frontier labs. Grouping the world's population by depth of understanding and usage, he split it into four tiers:

- **~6 billion people (75%)**: Have barely touched an LLM.
- **1–2 billion people (~20%)**: Use free chatbots as search engines and writing assistants.
- **~20 million people (0.2%)**: Use frontier models for math and coding, and have watched an agent knock out weeks or months of work from a single prompt.
- **~5,000 people**: Sit inside top labs watching thousands of agents collaborate over weeks on massive software engineering projects, zero-day discovery, and frontier math.

Karpathy admits these numbers are gut estimates. As a directional map, the shape matches my own experience—except for the jump from 20 million straight down to 5,000. A 4,000x drop in a single step leaves a glaring gap.

Caught in the middle are independent power users outside the labs. They don't have uncapped internal compute, yet they routinely orchestrate a dozen or even several dozen agents in parallel—well past the stage of "using Claude Code to write some code." That is the missing middle I want to fill in.


## The Five-Tier Funnel

Estimated as of October 2026, the adoption funnel breaks down into five tiers by depth of use:

- **L1 — Chat users: ~2 billion.** Used an AI chat assistant within the past month.
- **L2 — Desktop agent users: ~45 million.** Have an agent tool like Claude Code, Codex, or ChatGPT Work execute real tasks at least once a week.
- **L3 — Power users: ~2 million.** Consistently max out a $200/month top-tier subscription.
- **L4 — Fleet commanders: ~80,000.** Routinely run ten or more agents in parallel, backed by a stack of top-tier subscriptions.
- **L5 — Inside frontier labs: ~5,000.** Core staff at frontier labs with effectively uncapped compute.

![Figure 1: The five-tier AI adoption funnel as of October 2026](fig1-funnel-2026-10-en.webp)

The chart has to use a logarithmic scale; drawn to true proportion, the bottom four tiers would collapse into a single thin line. One in four people on Earth has tried AI, but only one in 100,000 has ever commanded an agent fleet.


## Anchoring the Ends: L1, L2, and L5

In a Fermi estimate, you start with the tiers anchored by public data, then work inward to infer the opaque middle.

### L1 — Chat Users: ~2 Billion

The metric here is unique individuals who used any AI chat assistant in the past month, broken into three buckets:

- **ChatGPT**: OpenAI disclosed [1.2 billion weekly active users](https://openai.com/index/devday-2026-recap/) at DevDay.
- **Gemini**: [Passed 1 billion monthly active users](https://siliconangle.com/?p=812556) in August. Assuming a quarter of them don't use ChatGPT adds roughly 260 million net users.
- **China**: As of the first half of 2026, China had [over 700 million generative AI users](https://www.news.cn/20260929/40258c3794684c20ae7867909cdec2ce/c.html). That figure measures usage over a six-month window; applying a 20% haircut to convert to monthly actives yields roughly 600 million.

Together, that comes to roughly 2 billion people, or 24% of the world's population. Microsoft's device-telemetry estimate is lower: as of June, [18.8% of the global population aged 15–64 had used generative AI](https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/). However, Microsoft noted that expanding its tracking coverage in the next edition will significantly revise China's numbers upward, so I treat 18.8% as a lower bound.

### L2 — Desktop Agent Users: ~45 Million

OpenAI gave us a hard number: [Codex and ChatGPT Work together exceed 35 million weekly active users](https://vgtimes.com/tech-and-hardware/169376-openai-sums-up-devday-2026-new-agents-work-tools-and-cloud-codex.html).

Anthropic hasn't released an absolute user count for Claude Code, disclosing only in February that [annualized revenue had passed $2.5 billion and weekly active users had doubled in six weeks](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation). Still, we can triangulate from two directions:

- **From revenue**: Anthropic's [total annualized revenue reached $65 billion at the end of July](https://www.webull.ca/news-detail/15422614464930816). Assuming Claude Code accounts for 15%–20% of that and each weekly active user generates $100–$150 per month on average, that implies 6 million to 11 million users.
- **From developer surveys**: In the JetBrains developer survey, [39% of professional developers reported using Claude Code at work](https://aiunderstanding.org/news/36kr-reports-claude-code-led-github-copilot-in-jetbrains-2026-developer-survey). Out of roughly 40 million professional developers worldwide, halving that share to correct for active-user bias in survey respondents yields around 8 million.

Both methods converge, so I'll take 8 million for Claude Code. Cursor, Copilot Agent, Gemini CLI, and similar tools add roughly 7 million, while Chinese tools—Trae, Qoder, and domestic vendors' Coding Plans—add another 5 million (public data for the Chinese segment is thin, so this relies mostly on industry observation).

That totals roughly 55 million before deduplication. Subtracting overlap from people who use two or three tools at once leaves **45 million**, or 0.55% of the global population. Roughly 20 million of them use these tools to write code, lining up neatly with Karpathy's third tier.

### L5 — Frontier Lab Insiders: ~5,000

Here I take Karpathy's figure directly and cross-check it against lab headcounts. OpenAI had around 4,500 employees in March and [planned to double to 8,000 by year-end](https://engadget.com/ai/openai-reportedly-plans-to-double-its-workforce-to-8000-employees-161028377.html); Anthropic had [roughly 4,000 at the start of the year](https://www.longtermwiki.com/factbase/property/headcount). Including the other frontier labs puts total headcount in the 20,000–30,000 range.

Strip out operations, sales, and peripheral teams, and 5,000 is a reasonable estimate for core researchers and engineers who can point near-unlimited internal compute at frontier systems. Even under a looser definition, that number tops out around 15,000.


## The Opaque Middle: Following the Money

L3 and L4 have no public user counts, but the flow of money leaves a clear trail.

On October 5, the seventh edition of a16z's *Top 100 Gen AI Consumer Apps* report introduced [rankings based on actual card spend](https://a16z.com/100-gen-ai-apps-7/) from YipitData's US credit-card panel. Consumer billing follows a steep power law:

- Median monthly spend among paying users is just **$25**—basically a single standard subscription—and has barely budged in years.
- The top **10%** of users generate roughly half of all revenue.
- The top **1%** generate 19.5%, more than the bottom half combined (16.6%). They spend an average of **$903 a month**, up 80% from 18 months ago, primarily on automation, product development, and content creation.
- Only **13%** of paying users pay for a second AI product.

Enterprise spending is even more skewed: Ramp data shows that [the top 1% of customers account for 80% of OpenAI's and Anthropic's enterprise revenue](https://www.pymnts.com/news/artificial-intelligence/2026/openai-and-anthropic-get-80percent-of-revenue-from-1percent-of-customers/).

On the other side of the ledger sits a massive subsidy. SemiAnalysis estimates that a maxed-out $200/month ChatGPT Pro subscription consumes up to $14,000 worth of compute at API rates, while Claude Max 20x comes to roughly $8,000. An OpenAI top-tier subscriber only has to use [5.7% of the theoretical ceiling before the platform starts losing money](https://techspot.com/news/112759-openai-anthropic-cant-afford-have-everyone-use-ai.html). A vast base of light users is subsidizing a tiny cohort of compute whales at the tip of the pyramid.

Fitting a Pareto tail to the spending shares of the top 10% and top 1% yields an exponent of roughly 1.7, which lets us extrapolate the profile of the top 0.1%:

| Percentile | Monthly Spend Threshold | Average Monthly Spend | Rough Equivalent |
|---|---|---|---|
| Top 1% | ~$370 | $903 (measured by a16z) | One or two $200 top-tier plans, plus a stack of add-on tools |
| Top 0.1% | ~$1,400 | ~$3,500 (extrapolated) | Seven to eighteen $200 top-tier plans burning concurrently |

That matches the financial footprint of an agent fleet. Accordingly, I map **the top 1% of paying users to L3, and the top 0.1% to L4**.

What is the denominator? ChatGPT already had [over 50 million paying subscribers](https://aibusinessweekly.net/p/chatgpt-statistics) in February, and in [a16z's panel](https://a16z.com/100-gen-ai-apps-7/) its paid footprint is roughly three times that of Claude or Gemini. Deduplicating across the Big Three (ChatGPT, Claude, and Gemini), coding tools, and vertical products, I estimate **120 million** paying AI users worldwide, within a range of 80 million to 150 million.

### L3 — Power Users: ~2 Million

One percent of 120 million gives 1.2 million people paying with their own cards. Then there are heavy users on corporate accounts: among engineers tracked by Jellyfish, [the top 2% burn through 500 million tokens a week](https://workos.com/blog/nicholas-arcolano-jellyfish-token-maxing-diminishing-returns), running highly autonomous multi-agent pipelines. I estimate that enterprise cohort at 600,000–800,000, bringing the total to roughly **2 million**.

Usage behavior offers an independent cross-check. OpenAI's Codex paper reports that [over 10% of users manage three or more agents concurrently at some point during a given week](https://ideas.repec.org/p/arx/papers/2606.26959.html). Narrowing that down to people who work this way routinely gives roughly 4% of L2—or 1.8 million users, close to our spending-based estimate.

### L4 — Fleet Commanders: ~80,000

One-tenth of a percent of 120 million is 120,000. However, a16z notes that a substantial share of top-end consumer spend goes toward video generation and visual design. Assuming half of that group isn't running agent fleets leaves 60,000; adding roughly 20,000 engineers who run agent clusters on corporate API budgets brings the total to **80,000**. Measured another way, taking 0.1%–0.2% of L2 yields 45,000 to 90,000, landing in the same range.

For a sense of intensity, OpenAI's internal telemetry shows that its P99 (top 1%) power users [log more than 60 agent-hours per day](https://openai.com/index/how-agents-are-transforming-work/)—roughly three agents running nonstop around the clock. An L4 fleet commander outside the labs typically operates at three to ten times that daily volume.


## Nineteen Months: How the Funnel Grew

Applying the same methodology backward to March 2025 lets us plot the funnel quarter by quarter:

![Figure 2: Seven snapshots of the AI adoption funnel from March 2025 to October 2026](fig2-funnel-timeline-en.webp)

Back then, Claude Code had just launched in preview. L2 stood at just 1.5 million users, L3 at roughly 30,000, and L4 at no more than 1,000—fewer people than the researchers inside the labs. Users weren't reluctant to spend money; there simply weren't good tools yet for turning money into output. Three inflection points changed that:

1. **Mid-2025**: Claude Code was folded into the flat-rate monthly Max subscription. Power users began running it 24/7 in the background, burning through Anthropic's capacity until the company had to [introduce weekly rate limits in late July](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users).
2. **February 2026**: The [Codex desktop app launched](https://en.wikipedia.org/wiki/OpenAI_Codex_%28AI_agent%29), turning parallel multi-agent execution from a niche power-user hack into the default workflow.
3. **July 2026**: [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) brought agents to non-coding knowledge workers, more than doubling L2 in a single quarter.

![Figure 3: Key inflection points and user growth across all five tiers over nineteen months](fig3-funnel-growth-en.webp)


## Why Adoption Still Doesn't Run That Deep

**First, trying AI is not the same as using it deeply.** Roughly 24% of the world has chatted with an AI, but only **0.55%** actually delegates work to agents. a16z sees the same gap in the US: nearly half of respondents say they have used AI, yet [only 25% use it daily](https://a16z.com/100-gen-ai-apps-7/), and just 4.5% pay out of pocket for a personal subscription.

**Second, the middle tiers are exploding, but from a tiny base.** Over nineteen months, the middle three tiers grew 30x–80x while the two ends grew just over 2x. Conversion from L1 to L2 climbed from 0.17% to 2.2%—rapid growth, but the vast majority of users still haven't crossed that threshold.

**Third, headcount doesn't equal firepower.** L4 users outside the labs now outnumber L5 insiders 16 to 1, yet models in the class of Claude Mythos were [available to only about 150 organizations as of June](https://en.wikipedia.org/wiki/Claude_Mythos). Even if we max out every commercial subscription on the market, we are still only watching what Karpathy calls the "movie trailer."

**Fourth, rate limits are increasingly the bottleneck between L3 and L4.** As soon as subsidies tighten, heavy users feel the squeeze. In September, OpenAI temporarily paused new sign-ups for its $200 Pro plan; at DevDay, it [rolled out a $500/month Pro 500 tier and brought back the $200 plan with half its previous allowance](https://vgtimes.com/tech-and-hardware/169376-openai-sums-up-devday-2026-new-agents-work-tools-and-cloud-codex.html). Uber likewise [capped per-engineer spend on any single coding agent at $1,500 a month](https://workos.com/blog/nicholas-arcolano-jellyfish-token-maxing-diminishing-returns). How large a fleet you can run increasingly comes down to who is willing to pay for the compute.


## Where the Opportunities Lie

The daily online debates over whether AI is a bubble or an industrial revolution mostly come down to people at different tiers of the funnel talking past each other from completely different lived experiences. Once you see that gap clearly, the opportunities are straightforward.

**If you build applications and products, the biggest prize sits between L1 and L2.** Whoever flattens the barrier to entry so non-programmers routinely hand off everyday tasks to agents will capture the next tenfold wave. a16z is already seeing personal agents spread beyond developers.

**If you build infrastructure, prepare for a shift in who operates software.** As L2 grows from 45 million to 450 million, the primary user of software will no longer be a human clicking around a UI, but tireless agents running in the background. Databases and backend systems spun up, read, and written concurrently by thousands of agents will far outnumber the frontend apps opened by humans.

Deep AI adoption is still low, which means the story is just getting started. But if the chasm between early adopters and the early majority remains uncrossed for too long, this wave of euphoria may well tip from its "installation period" into a crash and reckoning.
