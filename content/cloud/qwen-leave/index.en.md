---
title: "Shockwaves at Alibaba Qwen: The Soul of the Team Walks Away"
date: 2026-03-04
authors: [vonng]
summary: >
  Qwen lead Justin Lin publicly announced his departure, followed by more core-team exits and a wave of speculation about compute allocation, KPI pressure, and organizational power shifts inside Alibaba.
tags: [AI, LLM, Alibaba Cloud]
ai: true
aliases: ["/ai/qwen-leave/"]
---
I had become more optimistic about Alibaba over the last year, largely because the Qwen team seemed to be doing real work: shipping strong models, contributing to open source, and earning genuine international attention.

That is why this personnel shock felt so significant.

On March 3, 2026, Qwen technical lead Justin Lin posted a short farewell message on X:

> [!SOCIAL] Junyang Lin `@JustinLin610`
>
> me stepping down. bye my beloved qwen.
{avatar="avatar-justinlin610.webp" date="2026-03-04" url="https://x.com/JustinLin610/status/2028865835373359513" platform="x"}

Not long after, the public narrative turned from resignation to upheaval.

## 1. Publishing one night, gone the next

Qwen contributor Chen Cheng replied bluntly that leaving had not really been Justin Lin's choice, and that they had still been shipping models together the night before.

> [!SOCIAL] Chen Cheng `@cherry_cc12`
>
> I'm truly heartbroken. I know leaving wasn't your choice. Just last night, we were side by side launching the Qwen3.5 small model. I honestly can't imagine Qwen without you.
>
> > [!SOCIAL] Junyang Lin `@JustinLin610`
> >
> > me stepping down. bye my beloved qwen.
> {avatar="avatar-justinlin610.webp" url="https://x.com/JustinLin610/status/2028865835373359513"}
{avatar="avatar-cherry-cc12.webp" date="2026-03-04" platform="x"}

That timing is what made the incident feel less like a planned career transition and more like a sudden internal power move.

The same day, other researchers also announced departures, including Kaixin Li and Binyuan Hui. Kaixin Li mentioned that Qwen had once planned to build a technical outpost in Singapore, but that the plan was no longer viable after Lin's exit.

> [!SOCIAL] Kaixin Li `@kxli_2000`
>
> Signing off from @Alibaba_Qwen. Grateful for the chance to work with such brilliant minds. Proud of our impact. Onwards and upwards!
{avatar="avatar-kxli-2000.webp" date="2026-03-04" platform="x"}

> [!SOCIAL] Kaixin Li `@kxli_2000`
>
> Qwen could have had a Singapore base, all thanks to Junyang. But now that he's gone, there's no reason left to stay here.
{avatar="avatar-kxli-2000.webp" date="2026-03-04" platform="x"}

> [!SOCIAL] Arjun `@arjunkocher`
>
> qwen was doing so good. why are we seeing these sudden departures?
{avatar="avatar-arjunkocher.webp" platform="x"}

## 2. Eighteen months of talent drain

Lin's departure did not happen in isolation. Over roughly the last year and a half, leadership across language, speech, and vision had already been thinning out.

![Timeline of key departures from Tongyi Lab](timeline.webp)

The larger concern is not just turnover. It is the sense that the original core of Tongyi Lab has been repeatedly destabilized.

## 3. What may be behind it

Public discussion on X and in the broader AI community points to four recurring explanations:

1. **Mismatch between compute and research**: too much compute goes to delivery demands and not enough to frontier work.
2. **Misaligned KPIs**: rumors suggest consumer metrics such as DAU were being pushed onto foundation-model teams.
3. **Constant org reshuffles**: changing reporting lines often means changing power centers.
4. **External parachute leadership**: speculation quickly focused on who might be inserted next.

> [!SOCIAL] 宝玉 `@dotey`
>
> Qwen tech lead Junyang Lin posted a brief farewell on X today: "me stepping down. bye my beloved qwen."
>
> Compiled with help from Grok and Claude:
>
> **[1] It happened abruptly**
>
> Just yesterday, the Qwen team released the Qwen3.5 small model series—four sizes from 0.8B to 9B with vision support and switchable reasoning, running locally in just 7 GB of RAM while outperforming models several times larger. The community was thrilled.
>
> By this morning, the tech lead announced he was leaving.
>
> Even more surprising, it wasn't his own decision. Qwen contributor Chen Cheng responded right away: "leaving wasn't your choice." She said they had launched the Qwen3.5 small models together the night before and couldn't imagine Qwen without him.
>
> **[2] He wasn't the only one to leave**
>
> Junyang Lin isn't alone. Hyperbolic Labs CTO Yuchen Jin confirmed that another core lead, Binyuan Hui, has also left—two people who would stay up until 6 a.m. Beijing time collaborating on model launches.
>
> Shortly afterward, Kaixin Li—a core contributor to Qwen3.5, Qwen VL, and Qwen Coder—posted his own farewell: "Signing off from Alibaba Qwen. Grateful for the chance... Onwards and upwards!"
>
> At least three to four core contributors are confirmed out so far.
>
> **[3] What actually happened?**
>
> Piecing together the responses paints roughly this picture:
>
> Alibaba Cloud changed how it evaluates the Qwen team. Xinyu Yang criticized Alibaba Cloud for judging a foundation-model research team on consumer app metrics like DAU, and replacing Junyang with a non-core former Google Gemini engineer. Manage a foundation-model lab like an app team, and innovation stops.
>
> You Jiacheng put it even more bluntly: "Alibaba-Cloud kicked out Qwen's tech lead." He noted the successor may be Hao Zhou, whose background leans toward reinforcement learning, leaving the community skeptical about whether he can steward Qwen.
>
> Others said new leadership bypassed Junyang to manage the team directly—effectively sidelining him. Multiple insiders pointed to the same phrase: internal politics.
>
> **[4] Qwen3 may be the swan song**
>
> Panda (Jiaxi Cui) was pessimistic: after Junyang's exit, the Qwen3 line could be the team's last masterpiece for a long while as the org pivots toward commercialization.
>
> There is logic to that reading. Technically Qwen is formidable—massive Hugging Face downloads, beloved by researchers and developers—yet compared with ByteDance's Doubao, its consumer footprint in China is weak. Alibaba Cloud leadership may have decided to change direction and leadership over that gap.
>
> Yuchen Jin worries Qwen may stop shipping frontier open-source models altogether and shift to a closed commercial path.
>
> **[5] Reaction from the open-source community**
>
> The response on X has been overwhelmingly one-sided.
>
> Nathan Lambert called it a "legendary run." Unsloth AI thanked Qwen for its open-source contributions. Martin Ziqiao Ma said Qwen had been a bridge between frontier labs and the outside community—and that bridge may now break.
>
> Criticism was sharp as well. Maziyar PANAHI joked he hoped they start a new lab and force Alibaba to acquire it back for $2 billion as a lesson. Hugo Pinheiro asked a question on many people's minds: why do business decision-makers always wreck things right when they are working?
>
> The line circulating most widely in the community: "Qwen is nothing without its people."
>
> **[6] Where will they go next?**
>
> Nothing is confirmed yet. Community speculation includes founding a new lab, joining open-source-friendly teams like DeepSeek, or even calls for Elon Musk's xAI and Hugging Face to recruit them immediately.
>
> Wherever they land, their track record speaks for itself—from small models to flagships, text to multimodal, this is the group that made Qwen happen.
>
> **[Bottom line]**
>
> This is the classic big-company collision between open-source ideals and commercialization mandates. The Qwen team earned enormous industry prestige and developer goodwill through open-source models—none of which may count as a KPI on an internal scorecard.
>
> > [!SOCIAL] Junyang Lin `@JustinLin610`
> >
> > me stepping down. bye my beloved qwen.
> {avatar="avatar-justinlin610.webp" url="https://x.com/JustinLin610/status/2028865835373359513"}
{avatar="avatar-dotey.webp" date="2026-03-04" platform="x"}

> [!SOCIAL] Rainier `@mtrainier2020`
>
> Damn—they still can't let go of the obsession that outside hires know better.
>
> > [!SOCIAL] TVA Trader `@tvatrader`
> >
> > *Replying to @mtrainier2020*
> >
> > Idiots parachuted someone in from DeepMind.
> {avatar="avatar-tvatrader.webp"}
{avatar="avatar-mtrainier2020.webp" platform="x"}

> [!SOCIAL] Rainier `@mtrainier2020`
>
> FYI
>
> > [!SOCIAL] Yuchen Jin `@Yuchenj_UW`
> >
> > End of an era. Qwen lost its tech lead.
> >
> > When we launched the Qwen 3 Next endpoints on Hyperbolic with Junyang and his team, they were still online at 6am Beijing time! ...
> {avatar="avatar-yuchenj-uw.webp"}
{avatar="avatar-mtrainier2020.webp" platform="x"}

> [!SOCIAL] Rainier `@mtrainier2020`
>
> Doesn't look like it—sounds like the lead was pushed out. He was still discussing issues and shipping last night, and by the next day he was gone.
>
> > [!SOCIAL] 咸角鱼 `@Wm8Bp`
> >
> > *Replying to @mtrainier2020*
> >
> > Qwen has been doing pretty well—why such massive personnel turnover? Are they planning to launch a startup?
{avatar="avatar-mtrainier2020.webp" platform="x"}

> [!SOCIAL] Rainier `@mtrainier2020`
>
> Looks like real upheaval at Qwen—quite a few people are leaving at the same time.
>
> > [!SOCIAL] Kaixin Li `@kxli_2000`
> >
> > *Replying to @kxli_2000 and @Alibaba_Qwen*
> >
> > Qwen could have had a Singapore base, all thanks to Junyang. But now that he's gone, there's no reason left to stay here.
> {avatar="avatar-kxli-2000.webp"}
{avatar="avatar-mtrainier2020.webp" platform="x"}

These are all plausible dynamics in a large cloud company trying to turn a frontier model team into a product and business unit at the same time.

## 4. My read

### Qwen may keep shipping, but something important has changed

The models may still launch. The APIs will still run. The app may still grow.

But the globally visible, open-source-native human face behind Qwen is gone.

> [!SOCIAL] Aakash Gupta `@aakashgupta`
>
> Junyang Lin built Qwen from a side project inside Alibaba’s Tongyi Lab into the most-forked open-source model family on Hugging Face. Over 300 million downloads. More than 100,000 derivative models. Qwen3.5 benchmarks rivaling Claude Sonnet 4.5 and GPT-5-mini at a fraction of the inference cost. He did this while Alibaba was primarily an e-commerce company that treated AI as a cloud services add-on.
>
> He also told you the problem a month ago. At an industry event, Lin said compute constraints were eating Qwen’s research capacity because resources were “increasingly tied up in day-to-day delivery rather than R&D.” The team had a roadmap to scale beyond 10 trillion parameters. That takes GPUs. Alibaba Cloud’s GPU allocation priorities are set by a $400 billion e-commerce conglomerate, not an AI-first lab.
>
> The timing here is surgical. Qwen3.5 small models dropped yesterday. The medium models shipped last week. The full 397B flagship went open-source two weeks ago. Lin shipped the entire 3.5 generation, then walked.
>
> This is the pattern you see when a technical leader finishes the product cycle they committed to and decides the next cycle requires resources or organizational structure they won’t get. DeepSeek pulled ahead by giving researchers unconstrained compute budgets inside a hedge fund. Moonshot raised billions specifically for frontier training runs. Qwen’s research team competes for GPU hours against Alibaba’s recommendation engines, search infrastructure, and cloud customer workloads.
>
> The question for Alibaba: do you spin Qwen into an independent entity with its own compute budget, or do you keep it as a division that subsidizes cloud revenue? Lin’s departure suggests he already knows the answer.
>
> > [!SOCIAL] Junyang Lin `@JustinLin610`
> >
> > me stepping down. bye my beloved qwen.
> {avatar="avatar-justinlin610.webp" url="https://x.com/JustinLin610/status/2028865835373359513"}
{avatar="avatar-aakashgupta.webp" platform="x"}

That matters more than many executives think. A project like Qwen does not just need model checkpoints. It needs a living bridge to global developers.

### Cloud companies are often bad homes for model teams

I have long thought that frontier model teams should not be too tightly fused to cloud-company logic. Cloud businesses optimize for delivery, utilization, internal politics, and monetization. Research teams need room to spend compute on uncertain bets.

### Organization still beats money

Alibaba can spend aggressively. But no amount of money automatically fixes organizational friction. If your best researchers think they are trapped inside delivery quotas and KPI theater, you can still lose them.

## Closing

Qwen will probably continue as a product line. But the team that made it feel alive to the outside world has clearly been shaken.

That may be the most serious loss of all.

![A personal note on Alibaba's internal culture](featured.webp)

The reporting and commentary around this incident rely heavily on public discussion from X and other open sources. Some details remain difficult to verify independently, so treat the organizational interpretation with appropriate caution.
