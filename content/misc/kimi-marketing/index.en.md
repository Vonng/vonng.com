---
title: "Kimi's Marketing Backlash: Don't Burn Trust for Hype"
date: 2026-10-26
authors: [vonng]
summary: >
  The controversy over Kimi's overseas promotion exposes an old problem: paid promotion dressed up as word of mouth. How undisclosed ads poison technical information sources, and why I'd rather turn down sponsorships than lose the freedom to speak honestly.
tags: [AI, Business, Commentary]
images: [featured.webp]
---

Moonshot AI released its latest model, Kimi K3.1 Pro, a couple of days ago.

On paper, it had a strong hand: its Artificial Analysis Intelligence Index score rose from its predecessor's 44 to 55, close behind the leader, Claude Opus 5.5. Yet within hours of launch, it was facing a major backlash on X (Twitter).

It started when a creator outside China, [@elshayib_](https://x.com/elshayib_), decided to blow the whistle. In [a series of posts](https://x.com/elshayib_/status/2113710752741892476), he shared screenshots of what he said was a promotional brief Kimi had sent to creators. This is one party's account and remains unverified; Kimi has not yet responded. According to the screenshots, creators had to submit drafts for approval before posting. [The document supplied ready-made talking points](https://x.com/elshayib_/status/2113734602032312731), including “Kimi is an open-source Opus 5.5 at one-fifth the price” and “China just made Opus 5.5 free for everyone.”

The most damning instruction was [not to use the Paid Partnership label](https://x.com/elshayib_/status/2113710752741892476). There was also no need to link to the official website or tag the official account. A paid promotional post would then look just like an ordinary person's unsolicited recommendation.

In follow-up posts, he also shared screenshots of what he described as a [request to delete a critical comment](https://x.com/elshayib_/status/2113751173476049138) and [instructions to compare Kimi with Opus 5.5 and Astra on performance and cost](https://x.com/elshayib_/status/2113903850641842589).

The darkly comic part is that, around the time the document surfaced, a batch of blue-check accounts on X had already published [strikingly similar glowing “independent, hands-on reviews”](https://www.google.com/search?q=https://x.com/search%3Fq%3D%22Chinese%20Opus%22%20Kimi). Some creators apparently could not even be bothered to rewrite the suggested PR copy: they pasted it straight into their posts. Readers armed with the leaked brief called them out one by one in the replies: “You posted the promotional copy without changing a word?”

On the Chinese internet, this might pass for business as usual, hardly worth a raised eyebrow. In technical communities outside China, it ran into a wall. So let's use this episode to talk about model marketing, polluted information sources, and a few principles of my own.

## 1. Why I Lost Interest in Kimi

My daily setup centers on Codex, with Claude as my secondary tool, Gemini in a supporting role, and GLM handling odd jobs. I also run a few small Qwen models locally for embeddings and automatic speech recognition (ASR), with good results. I don't use DeepSeek much, and I've never used Kimi.

I tried GLM, another Chinese model, for a simple reason: several developer friends actually use it and gave me firsthand feedback that it was good. That seemed worth a try, so I paid for a plan: 1,700 yuan for a full year. Most other major AI services outside China only offer monthly subscriptions; by comparison, the annual plan cost very little. In practice, it has been handy for miscellaneous tasks.

I've heard people praise Kimi online, too. Oddly, though, few of the engineers I know actually use it. A few months ago, I seriously considered getting an account. If the online claims were right and it was even better than GLM, of course I wanted to see for myself. But seeing this sort of relentless, over-the-top marketing everywhere eroded both my trust and my interest in trying it.

The distinction is simple: my trust in GLM came from friends' firsthand experience; my interest in Kimi came from things I'd “heard online.” **Now that I know some of those recommendations may have been undisclosed promotions, how much of that earlier praise can I still trust?**

## 2. Imported Credibility and a Model Community Spared the Worst

Many Chinese companies have an old marketing habit: buy endorsements from English-language media or creators abroad, then bring screenshots home as evidence of foreign approval. The pitch exploits a lingering assumption: if someone outside China says it, perhaps it's more credible.

Honestly, I can hardly blame people for thinking that. Domestic marketing has burned through every last scrap of credibility. Some players in the car and smartphone industries deserve much of the “credit” for leading that race to the bottom: paid shills, coordinated PR copy, and manipulated comment sections have wrecked trust in reviews on the Chinese internet.

By comparison, China's model community had maintained a relatively civil, collegial atmosphere, with technical merit doing the talking. I think it has the earlier Pangu episode to thank for that. Without it, the community might have become the same cesspool as the domestic database industry operating under China's Xinchuang push to replace foreign IT with homegrown products.

If the allegations are true, this is Kimi's problem: its researchers worked themselves to the bone to build a model among the world's best, while its marketing still relied on a familiar domestic playbook of scripted talking points, mass posting, and undisclosed ads. You need to know who your core customers are. For these models, that means programmers and technical decision-makers, and **programmers are the least receptive audience for this stuff**.

## 3. Undisclosed Marketing Is Poisoning Our Information Sources

Media are often divided into three categories:

- **Paid Media**: You pay for placement.
- **Owned Media**: You publish through your own website or WeChat account.
- **Earned Media**: Your product is good enough that users spread the word voluntarily.

The marketing described in the brief amounts to an attempt to **buy the trust of Earned Media with a Paid Media budget**: demand absolute control over the copy—mandatory approval and instructions to pitch an “open-source Opus”—while claiming the credibility of spontaneous enthusiasm by omitting ad labels and posing as ordinary users.

What bothers me most is this: **undisclosed advertising is seriously contaminating the sources we rely on.**

I get most of my information through a human filter, loosely analogous to user-based collaborative filtering (UserCF). I am selective about whom I follow and actively manage what I take in. Accounts with poor content, little credibility, or bad reputations get removed. I keep the reliable firsthand sources.

I go to that trouble because official channels stopped being particularly trustworthy a long time ago. Vendor-published benchmark rankings, rankings from various testing organizations: I no longer trust them. This goes well beyond Kimi to benchmarks from AI and cloud vendors across the board.

To put it bluntly, many leaderboards are bullshit. I remember Dr.Qi making a similar point in a talk: you cannot trust the rankings. Whether a model is any good ultimately comes down to what developers say after using it.

But marketing teams quickly found a way around that defense: if nobody trusts leaderboards and everyone relies on word of mouth, buy the word of mouth.

Lately, it has become hard to miss how many replies on X are mass-produced by AI. They have that uncanny, almost-human feel. Some accounts' posts have the same plastic quality of assembly-line marketing. Incidentally, “marketing” is supposed to be a neutral term. On the Chinese internet, it has become almost an insult.

A friend used to run an MCN—a multi-channel network managing content creators—so I know the tricks. On Chinese platforms such as Xiaohongshu (RedNote), networks of accounts have long since become industrial production lines, churning out content at scale and overwhelming the feed. What looks like an ordinary person's account of a bad experience or a product they love is often a carefully engineered production. From every music cue and emotional beat in a video to the cheerleading in the top comments, it's all scripted. Once you see how it works, watching it can make you physically sick.

Chinese audiences may have been conditioned by repeated exposure to this playbook, learning to sift through advertorials for something useful. But I know the mindset of developers outside China fairly well, and the community cultures are very different. When you post about technology on X, people generally expect your own firsthand experience and technical judgment. Once they discover that you took money, deliberately concealed the sponsorship, and published the same promotional copy as everyone else, you face more than reputational damage: it also raises the prospect of violating the [FTC's Endorsement Guides](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking). The technical community's backlash can be immediate and fierce.

As more people take money to pose as unpaid enthusiasts, bad actors drive out good ones. Everyone starts wondering whether every technical recommendation is an ad. The whole community becomes toxic.

## 4. Why I Never Take Sponsorships

At this point, someone might ask: aren't you a content creator yourself? What do you think about getting paid for it?

My WeChat account has nearly 70,000 followers, and my total across platforms is well over 100,000. That puts me among the more prominent voices in databases and cloud computing. But I have one very simple, absolute rule: **no sponsorships.**

Today, publishing still isn't even a side business for me, because I don't make a penny from it. It's not for lack of opportunity. Every day, my WeChat inbox shows 99+ sponsorship pitches. Countless PR firms and media buyers want to place advertorials.

I've received offers to promote specific products, including Tencent EdgeOne, Qwen, various AI tools, and hardware such as mini PCs.

I've taken none of them, and I have no desire to. Friends have done the math for me: take those deals and become a full-time creator, and I might earn more than I do from my technical work. My answer goes back to Luo Yonghao's famous line to Wang Ziru during their [live confrontation on Youku](https://www.bilibili.com/video/BV1xW411H7c8/):

> **“You're already a kept man. How can you claim to be independent?”**

I started writing on WeChat to express what I actually think and share firsthand knowledge and experience. If expression is the point, I want the freedom to say what I mean without worrying about whose approval I might lose. Cloud vendor or database vendor, if your product is bad or you play games with developers, I'll call you out by name. If my criticism is reasoned, supported, and factual, what are you going to do about it? That is the great pleasure of speaking freely. Once I take a vendor's promotional money, writing becomes a job managing someone else's PR problems. All the fun is gone.

There is no shame in earning money. Taking ads openly and disclosing sponsorships is perfectly understandable. What I despise is commercial advertising disguised as objective technical judgment. Good firsthand sources are scarce enough already. In my own information filter, once I see a technical writer publish two or three undisclosed advertorials, I assume I probably can't trust what they say anymore. I block them.

### An Aside on AI Slop and the “AI Writing Police”

Since I've criticized those synthetic AI replies on X, I should also explain where I stand on AI-generated content.

Many people cannot distinguish **AI slop** from **AI-assisted writing**. To me, AI is a **multiplier**: zero times 100 is still zero. What matters in an essay is the thinking, the argument, and the firsthand experience behind it. If your head is empty, or you're churning out accounts to make a quick, grubby buck, the result will be worthless garbage. But if the thinking and structure are yours, what's wrong with using AI to polish the language and improve the prose—even if it retains a few supposedly telltale signs of AI?

I use AI to polish my own writing these days, too. I'm quite open about it: it helps me express myself more smoothly and efficiently.

[Yes, I Use AI to Write. So What?](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247491818&idx=1&sn=a437b73d9b3ceae1225a7f5457432d42&scene=21#wechat_redirect)

A couple of days ago, Reddit's Open Source community banned all AI-generated content. DHH reposted the news with a single word: *“retard”*. I share the sentiment. When someone ignores an article's facts and reasoning and drops a comment like “This reeks of AI” or “Too much AI in this,” I usually block them. If you have nothing to say about the argument and your only ambition is to act as a human AI-text detector, you don't have much to contribute.

And since I don't earn money from WeChat or need to indulge anyone who imagines they pay my bills, I have absolutely no qualms about hitting Block.

## 5. The Luxury of Speaking Freely

To me, the ideal position for a technical person looks like [DeepSeek](https://www.deepseek.com/): make a fortune from your core quantitative trading business, then enjoy doing research, releasing model weights and even open-sourcing inference infrastructure—things that could otherwise be core competitive advantages—without worrying about short-term returns. Or like [DHH](https://world.hey.com/dhh): achieve financial independence through SaaS products such as Basecamp and HEY, then spend your time tinkering with Omarchy, your Linux desktop configuration project, and saying exactly what you think online.

That's how I approach open source, too. The ideal is to have enough money already and write code for the pleasure of creating things. A few consulting engagements each year pay enough for me to live comfortably, and that suits me fine. The rest of the time, I can work on [Pigsty](https://pigsty.io/), my open-source PostgreSQL RDS distribution, and [Silo](https://silo.pgsty.com/), my object storage project, without needing anyone's approval. I can take on the cloud vendors, upset the status quo, and say what I want. There is real pleasure in telling the truth without pulling punches.

## Conclusion

Back to Kimi: honestly, I think this kind of marketing costs far more than it gains.

K3.1 Pro looks technically competitive. But changes to subscription quotas and high token consumption per task had already prompted plenty of complaints from paying users on [Reddit](https://www.reddit.com/r/LocalLLaMA/). Then came this overseas marketing controversy, with allegations that creators were being encouraged to pose as enthusiastic, unpaid users.

The days when a slide deck and a few PR releases could sell people on a model are long gone. When your audience consists of the world's most demanding, discerning programmers, perhaps the better approach is fewer RedNote-style influencer recommendation campaigns and more of that PR budget going directly toward developers' token allowances.

Look at OpenAI's Codex: it went from a few hundred thousand users to 40–50 million in just a few months, on the strength of its underlying model quality and a flood of generous daily quota resets. That's how you market a serious technical product.

Burning through the technical credibility and community goodwill your researchers worked so hard to build, all for a few cheap PR stunts, simply isn't worth it.

![Marionettes and a camera on a lunar set, a metaphor for manipulated word-of-mouth promotion](featured.webp)
