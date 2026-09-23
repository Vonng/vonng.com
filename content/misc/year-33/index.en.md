---
title: "Thirty-Three"
date: 2026-09-21
authors: [vonng]
summary: >
  Turning 33, I look back on what may have been my most enjoyable year yet: one person, a team of agents, Pigsty, PostgreSQL's Chinese ecosystem, Silo—and, somehow, work-life balance.
tags: [AI, Pigsty, Essay]
---

It's my 33rd birthday today. Another year gone in a blink.

People say your sense of time gets hazier after 30: blink, and a year is gone. I do feel that, though perhaps for a different reason.

I've also heard another explanation, a homespun version of relativity: sit beside a hot stove, and a minute feels like a year; do something you love, and time flies. So I can't quite tell whether it's age or simply spending my days doing what I enjoy. I'm leaning toward the latter.

This has probably been the most enjoyable year of my life. I've had the freedom to tinker at the frontier of AI without distractions. Honestly, commanding an army of AI agents, winning battles and claiming territory, is tremendous fun and deeply satisfying. Better than playing video games, if you ask me. Sometimes I think I push it too hard: up at 6 a.m., a nap at noon, then back at it until midnight.

- [AGI Machine Guns Are Now Standard Issue](/en/ai/ai-machinegun-for-everyone/)
- [How Do You Burn Through 10 $200 Codex Subscriptions?](/en/ai/10x-subscription/)
- [What Can a One-Person Company Ship with $1,000 a Month in AI Subscriptions?](/en/ai/yield-with-agents/)

![AI subscriptions and quota usage](01.webp)

That sounds exhausting, but it really isn't. Once I've handed out the tasks, I spend much of my time browsing the web, writing, watching short dramas, or even playing a couple of rounds of Honor of Kings. It feels surprisingly leisurely. I have AI to thank for that: it lets someone working alone get an extraordinary amount done, move fast, and somehow achieve work-life balance.

A few years ago, everything now under the Pigsty umbrella would probably have taken more than a hundred people: packaging, distributing, and testing a dozen or so database engines and more than 400 extension projects across 16 Linux platforms; maintaining package repositories and observability infrastructure; Chinese documentation for 11 major PostgreSQL versions and [Chinese messages](/en/pg/pg-nls/) for six; a [Chinese community website](/en/pg/pgsql-cc-online/) and a comprehensive PG extension catalog. I also picked up the [object storage](/en/db/long-live-silo/) pieces after MinIO walked away, and that's shaping up nicely. There's plenty more I haven't even had time to write or talk about.

I've essentially been running a one-person company since 2022, and I like it. Some customers do worry about my bus factor: what happens if the one person keeping things running gets hit by a bus? That has cost me some business. But the sheer flexibility of working this way feels wonderful. At a moment when the world is shifting gears, I think that flexibility is essential.

Of course, this one-person company couldn't keep going without my customers' trust and support, or the encouragement of my users. I'll keep working to earn that trust and live up to the responsibility.

## The Year's Highlights

Let's finish with the main things that happened this year.

(Can't be bothered to write this bit. Claude, go sum it up.)

![Claude's summary of this year's project progress](02.webp)

<details>
<summary>Text version of Claude's summary</summary>

First, let's tally things up.

- **Six Pigsty releases**, from v4.0 to v4.5. Version 4.0 arrived in late January with 320 commits and nearly 400,000 lines changed—over 300,000 of them in monitoring dashboards. The license went from AGPLv3 back to Apache 2.0, and monitoring moved entirely to the Victoria stack. I called it "finished software." By v4.5 in August, the extension count had grown from 444 to 575, my own Silo had taken over object storage, and Valkey, Kafka, and MySQL had joined the lineup. Around March, pigsty.io drew 1.44 million unique visitors in 30 days. The documentation site for a self-hosted database distribution was getting the traffic of a midsize SaaS business.
- **The extension repository:** pgext.cloud catalogs metadata for more than 2,200 PG extensions and builds RPM/DEB packages for roughly 400 extension projects across 16 Linux distributions. I filled the gaps in the official PGDG package matrix one by one until the missing count hit zero. It's the largest extension repository in the PG world, with two to three times as many packages as the official repository.
- **Silo:** MinIO walked away; I picked up the pieces. In February, I wrote "MinIO Is Dead, Long Live MinIO." My own HN submission got two points. Someone else casually reposted it, and it hit the front page. Go figure. By August, Silo had 500,000 container image pulls and more than 2,000 stars. Over 30 open-source projects, including RAGFlow and Dokploy, had switched to it. I fixed more than a dozen security vulnerabilities, several critical ones with CVSS scores above 9. In September, MinIO deleted its Docker Hub repositories just as Silo shipped its official release.
- **Loongson joined the official PostgreSQL repository:** on July 22, loong64 became the fourth officially supported architecture on apt.postgresql.org.
- **PG learned to speak Chinese:** all 67,487 Chinese messages across PG 14 through 19 were redone, merged upstream, and set to ship with PG 19.
- **The PG website got a Chinese edition:** pgsql.cc went live, with Chinese manuals for all 11 major versions from PG 10 through 20. None left out.
- **Finished translating the second edition of DDIA:** I spent three months translating the first edition by hand in 2017. The last four chapters of the second edition took one morning.
- **Dug up a long-standing bug:** it lurked in every official Valkey DEB package. The one-line fix was merged upstream.
- **New tools:** the pig package manager reached v1.5; the sow repository manager handles a six-figure collection of artifacts; and all 18 of my websites migrated to the OINK documentation framework.
- **A few talks:** in May, I gave "Extensions for Everyone" at the PG 30th-anniversary developer conference in Vancouver. I joined several of the PG 30th-anniversary livestreams, and in June I spoke to students at Xidian University about PG.
- **Wrote nearly 200 articles.**

The entire workforce this year: me and a bunch of agents.

</details>

My projects are approaching 40,000 GitHub stars in total: 27,000 under my personal account and 11,000 under my one-person organization.

Over the past year, I made 9,418 commits, ranking in China's top 10 and the world's top 100.

![GitHub profile and open-source projects](03.webp)

My WeChat newsletter grew from 45,000 followers to 64,200.

Another year with zero sponsored posts, which lets me write with fewer strings attached. I don't run ads either. I even went out of my way to disable WeChat's ads so those annoying things wouldn't turn up in my articles.

![WeChat newsletter follower count](04.webp)

I picked up plenty of organic traffic this year. Across all my websites, monthly page views passed 100 million. Still no ads, ha.

![Cloudflare traffic overview across websites](05.webp)

![Cloudflare monthly requests, page responses, and traffic trends](06.webp)

![Website request volume and visitors by region](07.webp)

Google Analytics suggests something like 100,000 to 200,000 actual human users and visitors.

![Google Analytics active-user trends](08.webp)

![Google Analytics monthly and weekly active users](09.webp)

Pigsty has climbed to second place among PG distributions.

Leave out the Kubernetes distributions, and it's first.

![GitHub star history for PostgreSQL distributions and high-availability projects, September 20, 2026](10.webp)

That's about it. If you'd like to see what I've been up to this year, drop by my [personal website](https://vonng.com/en/).

![The vonng.com homepage](11.webp)

I couldn't be bothered with much of a birthday celebration either. I spent the day burning through Codex, emptying the tank again before tomorrow's reset. I did order an ice cream cake from Yeren Xiansheng, stuck a candle in it, and called it a birthday.

![Birthday cake with a lit candle at home](12.webp)
