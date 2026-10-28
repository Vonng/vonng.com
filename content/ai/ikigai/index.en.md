---
title: "AI Software Engineering: Choose Problems You Care About"
date: 2026-10-28
authors: [vonng]
summary: >
  AI has driven the cost of prototyping software down to nearly zero, leaving conviction, verification, and long-term maintenance as the real bottlenecks. The first rule of choosing what to build is dogfooding: solving your own concrete problems is what carries you through the final 20%, builds trust, and compounds into an unfair advantage.
tags: [AI, Software Engineering, Philosophy, Commentary]
---
Friends keep asking me: "Vonng, you're burning through fifteen $200 AI subscriptions at once. What on earth are you building?"

I have written about plenty of what came out of that—a bit of everything, really. To borrow an investing term, AI has driven the cost of a starter position down to nearly zero. At this intensity of vibe coding, I have already taken a swing at almost every idea that first crossed my mind. Some were good, some bad; some worked out, and others fell flat.

After working through that backlog, one lesson stood out: you can use raw compute to spray small exploratory bets everywhere, but you cannot size up a high-conviction bet that way. Not every interesting idea is meant for me to build. Forcing a project into existence only to leave it unmaintained just creates digital landfill.

That brings us to the central question of vibe coding: choosing what to build.

## 1. First Principle: Build for Yourself

I have argued before that in AI-era software engineering, humans remain genuinely irreplaceable in two areas:

1. Supplying ideas, taste, and the conviction to see them through
2. Owning engineering verification, distribution, and trust

The second is mostly a matter of engineering execution, which I have covered many times before. Today I want to focus on the first: choosing what to build. You can buy compute, but you cannot buy conviction. No matter how many tokens you pay for—even with 15 agents running in parallel—their output still queues up behind one person for review: you. Your attention, mental energy, and context bandwidth remain hard physical bottlenecks.

At this point, deciding what to build—and what not to build—often matters more than how the code gets written.

After shipping dozens of AI-assisted projects large and small, I have arrived at a simple rule of thumb that has held up remarkably well:

- Everything I genuinely needed to use myself eventually succeeded in one way or another.
- Everything I had no real use for—projects dreamed up from thin air or built purely for novelty—ended up failing.

## 2. Which of Ikigai's Four Circles Is AI Rewriting?

Discussions about career choices and motivation often bring up the *ikigai* (生きがい) model—"a reason for being"—usually drawn as the intersection of four circles:

1. What you love (passion)
2. What you are good at (skill)
3. What you can get paid for (business)
4. What the world needs (value)

> Further reading: "What Is Ikigai, and How Can You Use It to Find Meaning in Life?" — Yixinli (壹心理)

In the past, "what you are good at" was a steep barrier. If a systems engineer wanted to build a polished frontend framework or desktop app, the friction of learning an unfamiliar toolchain and language ecosystem was enough to stop most attempts before they started. You might have had plenty of good ideas, but without the specialized implementation skills, you simply could not ship them.

Today, AI is rewriting three of those four circles:

- **"What you are good at" has widened dramatically:** The bar has dropped from "can write it by hand" to "can tell whether AI got it right." As long as you have sound engineering judgment and taste, AI can bridge the gaps in your craft.
- **"What can make money" has a new floor:** High development costs used to mean only mass-market problems were worth funding. Now that implementation is much cheaper, niche long-tail needs that never penciled out before are suddenly viable.
- **"What the world needs" has run into software inflation:** When anyone can spin up an application over a weekend with AI, supply floods the market. We no longer have a shortage of software; we have a shortage of software people can trust. The question has shifted from "does it exist?" to "do I trust it?"

The one circle AI cannot draw for you is the fourth: what you actually care about. AI can write code, dig through documentation, run tests, and assemble software, but it has no "want." It cannot want something on your behalf.

By the Theory of Constraints, a system's output is governed by its tightest bottleneck. Once AI flattens the barrier of specialized implementation skill, the bottleneck in software engineering shifts to human intent and care.

As an aside, the original Japanese term *ikigai* (生きがい) has very little to do with making money. It simply means "the thing that makes you want to get out of bed in the morning." The familiar four-circle Venn diagram was actually a remix popularized by a Western blogger around 2014. In a sense, AI is stripping away that utilitarian overlay and returning *ikigai* to its original meaning.

## 3. What Does Passion Mean in Engineering?

Talk of "passion" easily slides into motivational fluff. In engineering, however, caring about a problem and using the software yourself is not a vague emotion—it drives four concrete engineering mechanisms:

**First, it keeps requirements honest.**
: AI can take ten thousand steps fast, but someone still has to point it in the right direction. When you rely on a tool every day, the requirements are concrete and tied to friction you feel firsthand. When you invent an idea out of thin air, you are guessing what users might want. Imaginary users never file issues. Feedback from one real user—starting with yourself—beats ten thousand hypothetical ones.

**Second, it acts as a filter against AI's mediocre defaults.**
: The bottleneck in AI engineering is not generation; it is verification. Because AI output is fundamentally a probabilistic average, it gravitates toward a passable 80 out of 100. If you are building something you do not use yourself, it is tempting to wave it through as soon as it compiles and the UI looks decent. Heavy daily use turns your workflow into continuous integration testing. A vague error message or an extra click grates on you until you push the AI through a dozen rounds of revisions. That refusal to settle for 80 when it could be 95 is what we call engineering taste.

**Third, it supplies the stamina for the final 20%.**
: AI compresses the 0-to-80% prototype phase into a few hours, but what actually wears engineers down is the unglamorous 80-to-100% grind: packaging, compatibility, documentation, upgrade paths, and edge cases. Worse, as a codebase grows, it eventually hits a wall—context rots, the agent starts looping in circles, and the architecture threatens to unravel. Plenty of AI-generated repositories on GitHub have their final commit in week two for a simple reason: the author does not use them. Extrinsic motivation rarely survives the first real wall. Needing the tool to get your own work done tomorrow morning is what forces you to sit down, decompose modules, and help the AI refactor.

**Fourth, it gives you the resilience to outlast hype cycles.**
: Clever engineers like to calculate ROI before picking a project, which means every problem that looks profitable on paper is already crowded. Genuine interest pushes you into hard work that looks uneconomical on a spreadsheet. Unlike people chasing quick wins or building purely for a paycheck, someone who actually cares about the craft can tolerate working in obscurity—neither chasing every hot trend nor abandoning a project just because nobody is clapping yet. That patch of ground is uncrowded precisely because the spreadsheet crowd did the math, shook their heads, and walked away. Resilience lets you stay where they left.

Together, these mechanisms compound into a position that is very hard to copy. When sustained interest and grit keep you digging long after others have stopped, you naturally carve out a moat of your own.

![Finding a unique niche through sustained engineering focus](focus.webp)

Take PostgreSQL as an example. Plenty of people like PostgreSQL. Far fewer have spent years operating massive production clusters down at the metal, and fewer still have both the inclination and the engineering range to distill that operational experience into a reproducible open-source PostgreSQL RDS platform and Linux-native distribution—and maintain the entire stack solo. None of those traits is magic on its own, but stack all of them together and I end up in a category of one.

## 4. Looking Back: Day-Zero Payback as User Number One

Looking back at my own open-source projects through this lens makes the pattern obvious.

Pigsty is the clearest example. Many people assume it is a high-availability PostgreSQL RDS setup for small or mid-sized deployments. In reality, it was designed from day one for PostgreSQL fleet management—scaling from a single node up to ten thousand instances on the same underlying architecture.

Why did Pigsty stick? Because both my clients and I had real database fleets to run. Later, as Pigsty evolved to cover personal PostgreSQL runtimes and devboxes as well, I moved every piece of my own infrastructure onto it—six machines on my home LAN and six servers in production.

On Pigsty, I am user number one. I know firsthand what I need as a DBA, an ops engineer, and an independent developer. Seen that way, Pigsty could never lose money as an open-source project: as long as it ran my own clusters and machines cleanly, the R&D investment had already paid for itself at second zero of release. Everything that followed—community adoption and commercial revenue—was pure upside on top of a tool that had already broken even through personal use.

- [What Is a PostgreSQL Distribution?](/en/pg/what-is-pg-distro/)

- [Pigsty Passes 5,000 Stars: A One-Person PostgreSQL Distribution](/pigsty/star-5000/)

- [Forging a China-Rooted, Global PostgreSQL Distro](/en/pg/forge-a-pg-distro/)

The same pattern holds across several other projects:

### Calibrating Ambition to Usage Depth: Object Storage (Silo)

Interest comes in degrees, and your engineering ambition should match how deeply you actually rely on a piece of software. Take object storage: I depend on it enough to fork and maintain an open-source server after upstream walked away, shipping security patches and fixing IAM permissions and Object Lock. But my usage does not go nearly deep enough to justify writing a brand-new object storage engine from scratch. Knowing how deep your own need goes tells you where to draw the boundary.

- [MinIO's First Anniversary: How to Bring a Dead Open-Source Project Back to Life](/en/db/minio-silo-1year/)

- [Silo: A Maintained, MinIO-Compatible Object Store](/en/db/long-live-silo/)

- [MinIO Is Dead, Long Live MinIO](/en/db/minio-resurrect/)

### Pain-Driven Evolution: The Oink Documentation Framework

Why would a database guy write a documentation framework called Oink? Because I write a massive amount of documentation. Between engineering docs for PostgreSQL and Pigsty and the doc-driven AI development workflow I now rely on daily, I needed a cohesive way to organize and publish content. My sites used to be a fragmented mess across Hugo, Docusaurus, Hextra, Mintlify, and Nextra/Next.js on Vercel. Eventually I got tired of the sprawl and built Oink to consolidate blogs, books, technical docs, and even photo galleries under a single framework.

- Oink: Distilling Anthropic's Website Style

- [Oink: Build Modern Websites with Markdown](/en/ai/oink-intro/)

- [OINK: After Six Years of Wrestling with Documentation Frameworks, Codex Finally Got Me Over the Line](/en/db/oink-release/)

Today, all 40 of my local and public websites run on Oink. Its releases do not follow any grand roadmap; I spin up a new site, hit a missing feature, and add it. Iteration by iteration, my clients started adopting it for their own sites, and even an Apache Top-Level Project migrated over. Oink only has a little over a hundred stars on GitHub, but as its heaviest daily user, it does exactly what I need—and that is enough.

The same logic drives Pig (a PostgreSQL package manager), Sow (a repository manager), and Barn (a VM manager I have not publicly released yet but use internally every day). They keep improving for one simple reason: I use them in anger every single day.

## 5. Do You Love the Nail, or Just the Hammer?

What about the projects that failed? There were plenty of those too. I built some flashy experiments early on—using AI to graft etcd, MinIO, or the S3 protocol onto PostgreSQL. They were fun to hack together and made for eye-catching demos. Step back from the architectural stunt, though, and ask a basic question: would I ever run this in production? No. And if I would not touch it myself, what real value does publishing it create?

Reviewing those shelved experiments made a key distinction clear: do you care about the **process of building**, or the **result of using**? Put differently, do you love the hammer or the nail? Vibe coding is a slot machine for dopamine. You type a few prompts, watch code cascade down the terminal, see the build pass, and get the same rush as pulling a lever in a casino or hitting an ultra-rare gacha pull. Plenty of developers get their hands on AI and spin up repositories at a frantic pace, mistaking the thrill of swinging a giant hammer for genuine creative conviction—without caring much about the nail at all.

How do you tell whether you care about the nail or just the hammer? Before sizing up your commitment to a project, run through this checklist:

- Was this problem bothering you before you picked up the AI hammer, or did you invent a problem just to have something to hit?
- Once it works, will it enter your daily workflow today and replace an existing tool?
- If you publish it and nobody stars it or cares, will you still maintain it a year from now?
- Are you willing to sit with the AI and grind through the tedious, unglamorous final 20%?
- If it breaks at 2 a.m., does it wake you up?

If the answer is no, you are probably just enjoying swinging the hammer.

## 6. The Converse: How to Evaluate Other People's Open-Source Software

Flip the principle around and it works just as well for choosing dependencies as it does for choosing projects.

In an era of AI-driven software abundance, the scarce resource is trust. How do you pick a reliable tool out of a sea of half-baked GitHub repositories? My filter now is simple: does the author have **skin in the game**? Do they actually rely on this thing themselves?

"The author dogfoods this heavily every day" is the strongest endorsement in open source—worth far more than a polished README.

Take `magpie`, an open-source tool I started using recently. It solves a concrete problem: when you hold a dozen AI subscriptions across different providers and accounts, how do you aggregate them behind a single gateway and route traffic cleanly to different underlying agents? It is a classic N-by-N routing and credential management headache.

![Magpie AI subscription routing gateway interface](magpie.webp)

I evaluated several open-source gateways before settling on `magpie`. The deciding factor was simple: I know the author, `yetone` (we follow each other on X), and he is his own heaviest user. He tinkers with it constantly and runs his daily workflow through it. You can see that in the release cadence and how quickly rough edges get smoothed out.

Software fed by its author's own daily friction feels solid in practice. Better yet, studying how the tool is designed often teaches you workflow patterns and surfaces needs you had not articulated yourself.

## 7. Closing Thoughts

Back to the opening question: with effectively unlimited tokens and compute on tap, what should we build, and how should we choose?

The more capable AI becomes, the stronger the temptation to conjure software out of thin air. Yet the cheaper compute gets, the more discipline it takes to hold the simplest line: stop writing software for imaginary users, and write software for yourself.

When implementation skill is no longer an insurmountable wall and compute is just a monthly utility bill like power or water, caring about real engineering details, refusing to settle for passable defaults, and having the conviction to keep polishing are the only forms of productivity money still cannot buy.
