---
title: "SOTA: First Impressions of Fable 5.2 and Gemini Carbon"
date: 2026-11-11
authors: [vonng]
summary: >
  Fable 5.2 and Gemini Carbon found twenty more vulnerabilities in Silo on their first pass, despite repeated audits. Here is how this generation of frontier models is changing my work, from taking over PostgreSQL extensions and a database kernel to rebuilding my two-pizza team around three leading model providers.
tags: [AI, Agent, Software Engineering]
images: [rank.webp]
---

The frontier model releases have come thick and fast over the past two days: Anthropic brought out Fable 5.2, Google released Gemini Carbon, and Qwen 4 Max followed right behind. OpenAI reportedly has something coming tomorrow, too; GPT Astra 6.2 will probably get a full rollout soon. Fable handed out two Resets, and Codex will also be handing out a Banked Reset.

Much of this timing comes down to Anthropic filing its IPO prospectus and officially starting its roadshow today. Anthropic has pulled out the stops, putting its latest Fable 5.2 straight into the $20 Pro tier for people to try. Credit where it is due: the model is remarkably capable.

![Artificial Analysis model intelligence index compared with cost per task](rank.webp)

View the original charts: [AA Intelligence Index](https://artificialanalysis.ai/#artificial-analysis-intelligence-index-chart) · [Intelligence Index vs. Cost per Task](https://artificialanalysis.ai/#intelligence-index-vs-cost-per-task-chart).

*An unofficial leaderboard is still a leaderboard. It has at least a little signal.*

The other vendors were hardly going to sit quietly. In the spirit of "one company takes the stage, everyone else heckles," they are firing off new models during Anthropic's IPO roadshow, getting their punches in while everyone is watching.

My reaction is equal parts excitement and resignation.

## Twenty More Vulnerabilities, Just Like That

Only a few days ago, I had just come through a barrage of CVEs and bugs.

Silo, the object storage project I maintain, had inherited a pile of problems from upstream MinIO. I had recently put GPT Astra and Claude Opus 5.5 to work combing through the accumulated legacy mess and security hazards. I kept fixing things until neither Astra nor Opus could find any new vulnerabilities, no matter how many times they reviewed the code. On November 9, I happily shipped a new release.

[![Closed GitHub issues for Silo vulnerabilities and bug fixes](silo.webp)](https://github.com/pgsty/silo/issues?q=is%3Aissue%20state%3Aclosed)

Then, almost immediately, the new models arrived.

I ran Fable 5.2 over the code, and out came five security vulnerabilities. I followed up with Gemini Carbon, which promptly found another fifteen. I just stared at the results. There was nothing for it but to get back to patching.

![Multiple AI agents auditing Silo for security issues and fixing vulnerabilities](audit.webp)

Seen another way, this was a concrete demonstration of the jump in model capability. Repeated reviews with the previous generation still missed things that the new frontier models spotted straight away. With each generation, I can see the quality of the software I work on improve another notch.

## The Economics Changed: Taking On Extensions and Database Kernels

With Opus 5.5, Fable 5.2, and Gemini Carbon, I also started working seriously on PostgreSQL kernels and extensions.

When building the Pigsty distribution, I used to draw a clear boundary: packaging and integration, with the occasional small patch. I generally stayed away from the kernel and low-level extensions. I could do the work, but the return on the effort was too low. As one person, I could not afford that much time and energy. Once Fable 5.2 and Carbon could reliably fill the role of a seasoned kernel engineer, the economics changed completely.

I already thought of frontier AI agents in the Fable 5.1 to 6 era as advanced specialists. With Fable 5.2 and Carbon, I would put them closer to seasoned experts. In plain terms, you can hand them database kernel development and verification.

Recently, I have taken on a few things I would not previously have considered. First, I took over full maintenance of two extensions: the vector extension `vchord` and the analytics extension `Mooncake`. Then I decided I might as well keep going: I forked and took over `OpenHalo`, a PostgreSQL kernel compatible with MySQL's syntax and wire protocol.

[![PG.CENTER's catalog of PostgreSQL kernels, including OpenHalo and other open-source projects](halo.webp)](https://doc.pg.center/#kernels)

That kernel had been stuck on PG 14 ever since it was open-sourced, and PG 14 reaches end of life in a few days. With Fable and Carbon, I upgraded it straight to PG 18.6 and fixed a pile of MySQL compatibility issues along the way. I plan to move it straight on to PG 19 in a few days.

**Productivity to Spare: Taking Over “Legacy” Open-Source Projects in Bulk and Rebuilding the Toolchain**

*“When compute is your hammer, everything looks like a nail.” With the day job more than covered, I can branch out to take over core ecosystem projects and build low-level tools of my own.*

| Adopted or in-house project | Upstream background or tool replaced | Role in the infrastructure stack | Evolution and current status |
| --- | --- | --- | --- |
| [Silo](https://github.com/pgsty/silo) | MinIO (abandoned by a billion-dollar unicorn) | Enterprise-grade S3-compatible open-source object storage | Branched out to take over maintenance · 4,630 ★ · nearly 8 million downloads · 240+ projects migrated |
| [VectorChord](https://github.com/pgsty/vchord) | vchord (the original author entrusted it to me last week) | High-performance vector database extension for PostgreSQL | Popular vector extension with 2,000+ ★ · Maintaining it at the author's invitation |
| [Mooncake](https://github.com/pgsty/pg_mooncake) | pg_mooncake (acquired by Databricks) | PostgreSQL extension for real-time columnar analytics | 2,000+ ★ · Community project left behind after the acquisition · Took over full maintenance and development |
| [OpenHalo](https://github.com/pgsty/openhalo) | openHalo (kernel fork with an alternative wire protocol) | PostgreSQL kernel fork compatible with the MySQL protocol | Took over the kernel fork · Integrated into the standard build and upgraded to PG 18.6 |
| [Oink](https://github.com/pgsty/oink) | Replaces the heavyweight Google Docsy | AI-native foundation for engineering documentation and static sites | Built in-house as a replacement · Knowledge management platform and SDD · Powers dozens of sites |
| [Barn](https://github.com/pgsty/barn) | Replaces the abandoned HashiCorp Vagrant | Orchestration tool for local, multi-node VM fleets | Built in-house as a replacement · Spins up local test clusters across 16 OS variants with one command |
| [sow](https://github.com/pgsty/sow) & [pig](https://github.com/pgsty/pig) | Replaces the cumbersome traditional APT / YUM toolchain | Software repository manager and extension package manager | Built an end-to-end repository and package management workflow · Built my own Linux distribution |

Seeing these old projects come back to life is satisfying. The internet is full of people showing off videos and little demos made with Fable 5.2. I am not that bored, and I am too stingy with my tokens to spend them on that. Taking over and reviving demanding open-source projects with frontier models actually pushes the limits of what they can do.

- [MinIO, One Year On: Bringing a Dead Open-Source Project Back to Life](/en/db/minio-silo-1year/)
- [I've Taken Over Another Open-Source Project](/en/pg/maintain-vchord/)
- [Back for Another Helping: Yesterday vchord, Today Mooncake](/en/pg/fork-pg-mooncake/)

## Reorganizing My Two-Pizza Team

Judging purely by the quality of its software engineering work, Fable 5.2 is clearly the best model I have used so far. Gemini Carbon, which arrived amid rumors of "Talking to God," matches it in practice. Both are visibly ahead of the current Astra 6 in actual engineering work. Astra's rigor in backend development is still hard to beat, though. Once Astra 6.2 arrives, the three will probably draw level again, occupying the top tier with a clear gap to the rest.

At this point, the best setup is to keep each of the leading models on hand and put them to work together.

I previously wrote about [the personalities of large language models](/en/ai/llm-personaility/), and those observations still hold. Until now, my main subscription mix was **10 Codex, 3 Claude, 1 Gemini, plus 1 GLM**. Manage them as people, and their strengths become quite distinct:

- **Claude is the product manager and my second-in-command (INTP)**: creative, perceptive, good at coordinating the big picture and designing the overall architecture, and willing to make a call. I go to Claude whenever I need a direction or a design. It is an excellent architect and a reliable source of ideas.

- **Codex is the architect and workhorse (INTJ)**: dependable and tireless, extremely rigorous, sometimes to the point of being overly defensive. It tests and retests the same problem endlessly. It can be verbose, but the core code it produces is exceptionally solid. It is outstanding at backend work and state of the art at creating graphics, too.

- **Gemini is the writer (ENTP)**: I used to rely on it mainly for writing. It excels at technical documentation, marketing copy, and polishing articles. With Carbon, its engineering ability has caught up with the top tier, so it can finally join the main development team as well.

- **Chinese models do the grunt work**: checking documentation for consistency, verifying details, and scanning huge volumes of logs. All the repetitive chores. GLM costs RMB 1,700 for a year. At that price, what more do you want?

![Model roles, subscription allocation, and the PostgreSQL task queue scheduling architecture](team.webp)

With both Fable 5.2 and Carbon making such large gains in engineering, I am changing my subscription plan. I intend to cut back from ten Codex subscriptions and move to a balanced **3-3-3 lineup**:

- 3 Codex subscriptions at the $500 tier
- 3 Claude Ultra subscriptions at the $200 tier, potentially expanding to 6
- 3 Google AI Ultra subscriptions at the $200 tier

That gives each of my three main development machines one subscription from each of the big three. Add GLM and Grok for the grunt work, then me, and we have a standard **twelve-person two-pizza team**. Eleven of us are agents, **but I can eat both pizzas myself.**

The hardware behind this team is six computers on my local network plus six cloud instances: twelve machines in total, all managed through Pigsty. I eat my own dog food. Scheduling is simple, too: a shared PostgreSQL database holding a task queue.

[![Monitoring dashboard for local and cloud infrastructure managed through Pigsty](workers.webp)](https://demo.pigsty.cc/)

The lead agent inserts tasks into a table; subagents claim work from it. If they discover new problems while working, they automatically create follow-up tasks in the same table. Run these dozen or so subscriptions at full concurrency, and they can quickly fan out into dozens of workers tackling tasks in parallel.

Keeping dozens of concurrent workers from going off the rails does take a few engineering tricks. I can get into those after I finish talking a big game at the China Enterprise AI Conference and Tsinghua over the next few days.

## Time for a Plug

A couple of upcoming events: the day after tomorrow, November 13, I will give a keynote at the China Enterprise AI Conference titled "One Person, One Agent Team: How Much Can One Person Get Done?" I will also join a panel debate (read: mutual roasting).

![China Enterprise AI Conference keynote poster: One Person, One Agent Team: How Much Can One Person Get Done?](talk.webp)

On Sunday, I will also speak at Tsinghua University on "The Mythical Man-Month: How Far Can a One-Person Database Company Go?" Come along and share your thoughts.
