---
title: "Documentation-Driven Development: The First Secret to AI Software Engineering"
date: 2026-08-29
authors: [vonng]
summary: >
  People often ask: how do I ensure quality when AI writes the code? My answer has four parts: documentation-driven development, adversarial review, brute-force testing, and complexity penalties.
tags: [AI, Agent, Software Engineering, Documentation, OINK]
ai: true
---

> Documentation is not an afterthought once the code is finished. It is an input before coding begins, working memory during development, and the acceptance standard at delivery.

A few days ago, I wrote [*AGI Machine Guns Are Now Standard Issue*](/en/ai/ai-machinegun-for-everyone/), about how I burned through more than a dozen AI subscriptions in a month and pushed a backlog of projects forward. The most common question in my inbox and comments was not “Which model is best?” It was: **How do you keep all that AI-generated code from becoming a mountain of crap?**

It is the right question. Once everyone has a machine gun, anyone can spray bullets. But writing code quickly does not mean building good software, much less software that will still be maintainable six months later. So I want to share the techniques and lessons I have developed over the past few months of engineering with AI.

There are four: **documentation-driven development, adversarial review, brute-force testing, and complexity penalties.** Sometimes the bluntest techniques work best. Any so-called secret sounds obvious once explained—but that does not make it any less effective.

This essay focuses on the first: documentation-driven development. It is the foundation for the other three, and the practice in which I have invested the most—so much that I ended up building a documentation framework specifically to put it into practice.

---

## Wishing and Design

I originally planned to begin with theory, provide some background, and then move on to practice. That felt needlessly elaborate. Let me start instead with the main problems I encounter when using AI to build and maintain medium-to-large software projects.

I call the first problem “wishing”: **stating clearly what you actually want.** For a small demo, almost any approach will do. For a software project of medium size or larger, this takes real skill.

You cannot simply tell an AI, “I want a database that runs on object storage,” or “Rewrite Patroni in Go; rewrite pgAdmin too.” Those wishes are too **high-level**. AI has not yet reached the point where a single sentence like that produces the entire system. The space in between contains a great many engineering details and architectural decisions, and you still have to make the calls yourself.

Wishing is the part of the entire process that demands the most effort from you. State the wish well enough, and an agent can run for days, implementing it piece by piece without your constantly adjusting or directing it. State it vaguely, and however energetically the agent runs, it is still running in the wrong direction.

What form should the final “wish” take? I think it should be a **PRD—a product requirements document**. Human involvement is essential here: you describe the requirements, the agent organizes them into a PRD, and then you read that document carefully.

**You may choose not to read the code, but you cannot choose not to read the requirements.** Only you can decide what you actually want.

If an entire PRD feels like too much, at least read its user stories. Have the agent describe the typical usage scenarios, then ask yourself: “Is this what I want?” Point out any mismatch and iterate until you can say, “Yes. That is it. Go build it.”

Take it from me: never, ever skimp on this step. Every shortcut you take here comes due later. Start building before you have described the requirements clearly, and the result is pure luck—a gacha pull. That is not necessarily a problem for a small project. Sometimes your first pull gets you 90% of the way there—you hit a top-rarity SSR. It happens. But engineering cannot run entirely on luck. If you can settle a choice during design, do not defer it until later.

Exploratory work is different. If you genuinely do not know which approach is good, some uncertainty is unavoidable. But you can at least narrow the viable search space and keep the agent from producing anything wildly unreasonable.

How much time should this take? In my experience, a medium-sized project deserves at least half a day—a full morning—to generate and review the PRD before implementation begins. Once that is done, let the agent run and burn through the subscription quota. Come back a day or two later for acceptance.

---

## Development and Repair

The second problem arises during development. Coding agents are not like human engineers; they have their own temperament. The simplest way to think of one is as an **amnesiac genius**.

Imagine hiring an exceptional engineer. They can write in any language, pick up any framework at a glance, and do a week of an ordinary engineer’s work in a day. But every morning, they arrive having forgotten everything from the day before. They no longer remember why the project was designed this way, which approaches failed, which traps the team fell into, or which gaps were deliberate. You have to explain it all again from scratch.

Human teams have always compensated for this problem informally. Veterans teach newcomers and recount old project lore over lunch. During code review, someone casually explains, “We wrote it this way back then because…” The knowledge that never made it into the code but genuinely keeps the project running has a name: [tribal knowledge](https://en.wikipedia.org/wiki/Tribal_knowledge).

An agent has no tribe and cannot join you for lunch. It has only three things to rely on: **code, tests, and documentation.**

This is one substantive change AI programming has brought. Documentation used to be supplementary material written after the code. Now documentation begins as an input before any code is written. Poor documentation once meant little more than a slower onboarding process for new engineers. Today, it can send an agent in the wrong direction, causing it to reimplement an approach you rejected long ago—and to implement it rather thoroughly, expending enormous effort on work that solves the wrong problem.

My answer is simple: **give the agent working memory.** But I emphatically do not mean lame-ass gimmicks like “install an MCP” or “install Claude Mem.” I mean managing working memory as documentation.

Left to itself, a coding agent will crap out stray Markdown files all over a project: a `PLAN.md` here, a `NOTES.md` there, plus a pile of `TODO` entries. Instead, make two requirements explicit:

1. **Preserve the full reasoning process.** Keep the raw record in the working directory, organized chronologically or by topic, with the complete process intact.
2. **Periodically summarize and index it.** Have the agent turn its prior working memory into an index in [`AGENTS.md`](https://agents.md/) or `CLAUDE.md`, recording what earlier threads and sessions did. When a similar problem appears later, it can revisit earlier reasoning and architectural decisions instead of repeating old mistakes.

**Both layers are essential.** You cannot put everything in one giant pile, so the top layer needs an index. But an index alone is not enough; the complete raw records must remain underneath it.

---

## Testing and Acceptance

The third problem is testing and acceptance.

Tests come in different tiers: unit tests, integration tests, and acceptance tests are not the same thing. Given the intelligence of current AI systems, I do not even look at unit or integration test code. Unless a change touches an especially critical path or breaks compatibility, I let the agent test its own work and report the results, then apply my second technique—**adversarial review**—as the quality gate.

Only when two top-tier agents review each other’s work and still cannot agree do I step in personally. That is already rare.

But there is one thing you cannot delegate: **acceptance testing**. Is what the agent built actually what you wanted? You obviously cannot tell the AI, “Do the acceptance testing for me.” You cannot outsource supervision and sign-off. If you will not even do that much, chances are overwhelming that what you get is garbage.

> **Acceptance means staking your own reputation on the result.** A responsible engineer cannot cut corners here.

So how should you conduct acceptance, and how much work can you safely avoid? You can ask AI to draft the acceptance plan.

This is where documentation starts to earn its keep. Work backward from the user: who will use this software? It may be a human or another agent.

If it is a human, how do people normally start using software? They probably visit your site, click `Get Started`, and follow a tutorial from the basic features through the core workflow. That is the standard pattern.

So require the agent to deliver more than code. It must also deliver instructions and a manual, maintained to the same standard as the code itself. Acceptance then means following that manual: does `Get Started` actually work? Can you really complete every step in the tutorial?

---

## Documentation-Driven Development

Once you examine those three stages, the conclusion becomes clear: coding with AI is fundamentally an exercise in context management. That is admittedly a truism—using an AI agent for anything is fundamentally about context management. But in software engineering, what exactly constitutes that context? Two things: **code and documentation.**

If the code is already highly self-describing and expressive—pure Python, plain scripts, self-explanatory formats such as YAML and DSLs, or simply a tiny project—you may not need separate documentation. But if you are writing Go or Rust, or building a complete medium-to-large project, documentation is essential.

> **My conclusion: treat documentation as seriously as code—perhaps even more seriously.**

Documentation falls into several categories:

1. **Design documents:** goals, constraints, proposed approaches, boundaries, and architectural trade-offs;
2. **Working-memory documents:** the two layers described above—the complete raw record and a periodically updated index;
3. **Reference and delivery documents:** reference material explaining how the system works, tutorials that guide users through complete workflows, release notes for each version, and decision documents recording architectural trade-offs.

How should you manage all these kinds of documents? You could dump them into a directory and ask an agent to summarize what it contains, but that is crude.

The key is this: **documentation must be easy to ship.** It is part of the deliverable, not a pile of internal scratch notes or something tossed casually into Obsidian or a cloud notebook.

From the first day of a software project, understand that you are shipping not only a binary but also documentation. They are equal deliverables. If the documentation must ship, write it properly from day one and manage it with a proper system.

My approach is to give **every project a companion documentation site**. You can keep a `docs` directory in the project or split it into a separate repository; I prefer a separate repository.

For these sites, I built [OINK](https://github.com/pgsty/oink), a Hugo theme based on Google’s [Docsy](https://github.com/google/docsy), with extensive customization and integration. It has three main advantages:

1. **Simple delivery.** It supports turnkey CI/CD on [GitHub Pages](https://pages.github.com/) and [Cloudflare Pages](https://pages.cloudflare.com/). Commit and push, and the documentation site builds and publishes automatically; there is no pipeline to babysit.
2. **Everything you need.** Code blocks, tabs, steps, diagrams and charts, formulas, file trees, full-text search, multiple languages, version switching, and backlinks for knowledge management are all built in. You can ship a polished documentation site immediately. Every page also has a plain Markdown version, and the whole site exposes [`llms.txt`](https://llmstxt.org/): humans read the rendered pages, while agents fetch Markdown directly from the same source.
3. **Minimal friction.** No giant `npm` frontend stack. A single Hugo binary builds the entire site offline at blistering speed; even a site with thousands of pages builds almost instantly, with live preview. If native Markdown can express something, OINK never reaches for a flashy component.

---

## Why Good Documentation Matters

Why invest so much effort in documentation? Who is it actually for?

First, put yourself in the user’s position. If a person or an agent wants to use your software, what will they do first? They are hardly going to poke at a binary until they figure it out. That is one possible model—another project of mine, [PIG](https://pig.pgsty.com/), follows it by embedding documentation in the binary and exposing structured documentation directly through `help`. The design is explained in [*Agent-Native CLI*](https://pig.pgsty.com/blog/design/agent-native-cli/). But I do not think this is a general solution. In most cases, users will start with your documentation.

Second, documentation is not only for users. It is also for you, and it is your most important acceptance standard. Few people will inspect AI-written code line by line. You may choose not to read the code, but you must at least read the documentation. If an AI has cobbled something together and you do not have time to test every detail by hand, you should at least inspect the accompanying reference documentation.

Today’s coding agents already perform like brilliant, expert engineers. Your role is that of a senior architect: assign work and accept the result. But agents are not yet intelligent enough to take any grand wish you casually make and implement the whole thing automatically.

That leads to one point I consider critical:

> **If you care about engineering quality, at least 70–80% of your tokens should go to quality control and testing, not writing code.**

Writing code is fast and does not consume many tokens. Exhaustive testing is what really burns tokens—and what raises quality. This is a defining feature of AI software engineering: AI can give you a result worth 70 or 80 points out of 100 in one pass, but you may spend 80% of the total cost earning the last 20 points.

If you want to ship something genuinely reliable—something others trust, something widely used, and something you trust yourself—this is not the place to economize. Know where you can cut corners and where you cannot.

You can be lazy about unit tests: there is no need to write them by hand or read them routinely. You cannot be lazy about whether the project is headed in the wrong direction or the architecture contains any profoundly stupid design choices. When you spot either, intervene promptly (steering) and pull the work back on course.

Conversely, if a project cannot deliver documentation of acceptable quality, I consider the project itself unacceptable.

The clearest example is my friend Jiang. As I described in the previous article, he is the gorilla with a machine gun who cobbled together five databases, an operating system, and a compiler. Recently he added an OLTP database built on object storage.

Objectively, that database may solve a real problem in some particular setting. Overall, however, it still belongs in the `garbage` category. Why? Because it has no decent documentation. Without documentation, nobody knows what it can do, where its boundaries lie, or how to sign off on it.

---

## A Concrete Example: Silo

After all that theory, consider a concrete example: [Silo](https://silo.pgsty.com/).

Silo is a [MinIO](https://github.com/minio/minio) fork that I maintain. Upstream eliminated the community edition, gutted the management console, stopped publishing binaries, and archived the repository; Silo keeps all of those things alive. It is now the most active MinIO fork, with 600,000 downloads and more than 2,500 stars, and many open-source projects have switched their default image to it.

How do I maintain it? For every issue, I create a design document that captures the complete design rationale and reasoning process. I consider this essential. When you use AI to build such a critical piece of infrastructure, most people’s first reaction is, “Can its quality really be trusted?”

So you have to record everything: what problems did we encounter? How did we reason about them? How were the critical decisions made?

[Silo’s FAQ](https://silo.pgsty.com/#faq) states the policy plainly: agents do most feature development and code review; every change must pass CI and human review; every substantive change is merged only after a human weighs its trade-offs; and the agents’ complete work logs and trade-offs are archived. When a fix later proves wrong, the thing you most want to know is why it was made in the first place.

I believe **the session log is the real asset a project accumulates**. Code records the what and the how. The why must appear in the documentation—or at least in comments.

These records are rarer and more valuable than the code itself. They turn the tribal knowledge described earlier into a durable project asset. Silo’s dozen-plus [security advisories](https://silo.pgsty.com/blog/security/) and [release notes](https://silo.pgsty.com/blog/release/) are the public output of this practice. Read them and judge for yourself.

One more point: for medium-to-large projects, the right approach is to move quickly in small steps. Do not try to cobble together one giant system in a single shot. Break the work into small units that can be accepted independently. Complex architectures evolve; they are not designed in one pass. That evolutionary history matters enormously.

Take PostgreSQL. Its code is valuable, but I would argue that its soul does not live in the code. It lives in thirty years of [community mailing lists](https://www.postgresql.org/list/) and in its exceptionally good [documentation](https://www.postgresql.org/docs/current/). After all, most users may never read PostgreSQL’s source code, but they will almost certainly consult its manual.

---

## What Comes Next

Beyond documentation-driven development, software engineering has a few classic techniques. I find three especially useful: **adversarial review, brute-force testing, and complexity penalties.**

Their principles are utterly straightforward, but simple ideas are often the most durable. As for elaborate, kitchen-sink skill suites such as [BMAD](https://github.com/bmad-code-org/BMAD-METHOD) and [Superpowers](https://github.com/obra/superpowers), I no longer use them this season.

I consider BMAD pure overengineering. It takes all the bureaucratic cruft of software engineering that may make sense for human teams and ports it unchanged to agents. Agents do not need such fine-grained division of labor. At this stage, two or three agents in adversarial roles, reviewing one another, are enough. Every agent is a generalist; just give two agents opposing briefs. That is enough. There is no need to split them further into product manager, architect, and test engineer.

Of course, this is only my experience from the current season, which began in July 2026. These days I go all-in on the strongest tier of models, use only the best, and never waste time on cheap little models. My rule is simple: **use the best tools for the hardest work.** That is why I burn tokens so quickly—an average of two and a half subscriptions a day. Even [Tibo’s wild Reset spree](/en/ai/codex-reset-end/) and several accounts in rotation are not quite enough. Only Saint Tibo’s Resets keep me afloat.

The next model release may change best practices again.

For now, I see two patterns worth exploring.

### Pattern One: Agents Enter Team Chat

One approach is to connect Claude to Slack through Claude Tag. It can see your chat history and discussions, and you can assign it work much as you would to a human colleague. Most importantly, it gains access to the “tribal knowledge” context described earlier. There is something genuinely interesting about assigning work with `@Agent` in a group chat. I think it is a promising model for humans and agents to coexist, interact, and collaborate.

### Pattern Two: A Super-Orchestrator

Tibo says the next major paradigm will be a highly capable orchestrator—Astra—directing a fleet of worker agents. I think that may be a better direction. According to Tibo, Astra will bring another enormous leap when it launches. Most people’s local machines may not even be able to run it; it may require a cloud-hosted machine.

I had considered burning one into existence for myself, or tinkering with an existing open-source project. But why waste time on that? Wait another two weeks and the official team will ship one. There is really no need to tinker, is there?

I will cover how the other three techniques—adversarial review, brute-force testing, and complexity penalties—work in practice another time.

---

## Final Thoughts

This essay has focused on what documentation-driven development looks like in practice, with a concrete example.

My [OINK framework](https://oink.pgsty.com/) has also recently stabilized. [Version 0.8.1](https://github.com/pgsty/oink/releases/tag/v0.8.1) is now out with all the essential features in place, and I have just submitted the theme to the [official Hugo theme registry](https://themes.gohugo.io/).

Using it is brutally simple: tell Codex or Claude, “Use the theme at `oink.pgsty.com`.” It will clone a [starter site](https://github.com/pgsty/oink-starter), edit the content, build it, and deploy it. You only have to write Markdown. Several friends are already using it to build documentation sites inside their companies.

Shipping a polished documentation site that works out of the box is far better than handing over a few scattered Markdown files crapped out across the repository.

I now build almost all my projects **in public**. Visit any of the sites below: their design rationale, release history, and contracts are all there as practical examples.

- [OINK](https://oink.pgsty.com/)
- [PIG](https://pig.pgsty.com/)
- [SOW](https://sow.pgsty.com/)
- [SILO](https://silo.pgsty.com/)
- [Farrow](https://farrow.pgsty.com/)
- [PG Exporter](https://exp.pgsty.com/)

**Code can be wished into existence. Quality cannot. Documentation sets the boundaries around the wish—and provides the evidence you need when it is time to sign off.**
