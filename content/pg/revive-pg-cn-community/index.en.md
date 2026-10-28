---
title: "Reviving the Chinese-Speaking PostgreSQL Community"
date: 2026-10-12
authors: [vonng]
summary: >
  A PostgreSQL community starts with its users. With a distribution, documentation, package mirrors, localized messages, and a Chinese-language portal now in place, the next step is connecting them into a community that serves users across the Chinese-speaking world.
tags: [PostgreSQL, PG Ecosystem, Open Source]
images: [featured.webp]
---
PostgreSQL is the world's most advanced open-source database, and one of the very few major open-source projects genuinely run by its community rather than controlled by a single company. I have always believed that the soul of an open-source project lives in its community, not its code.

So today I want to talk about something I have kept to myself for years: **reviving the Chinese-speaking PostgreSQL community.** The idea has been on my mind for several years, but I held back from saying it out loud. Slogans are cheap; you need concrete work to back them up. Now that I finally have something to show, let me start with a piece that goes live next week.

## Revival Implies Decline

Talking about a revival implies there was a decline. That part is regrettable. China's PG community was reasonably active a few years ago, but in recent years its voice has faded and activity has slowed to a trickle, with barely a few signs of life all year. Against PostgreSQL's surging adoption worldwide, the contrast is stark.

The community's former chair was my business partner and colleague, and I know most of the people in that circle. As early as 2018, I repeatedly suggested that the community build a few practical things for users:

1. Run a domestic download mirror for PostgreSQL, since most mirror sites in China did not carry the PGDG repositories at the time.
2. Keep the Chinese documentation current. Volunteers were translating the manuals, but they routinely lagged behind by several major versions—often a year or two out of date.
3. Build a community PostgreSQL distribution to rally a small group of developers around shared code.

You know how the story went. None of those materialized. The community stayed busy running conferences and meetups while its voice faded and momentum stalled. Plenty of factors contributed, but two stand out to me.

**First, China's domestic database push pulled people away.** A wave of vendors forked, reskinned, or wrapped PostgreSQL into proprietary products, and many refused to acknowledge their PG lineage at all. People cared more about tending their own patch of turf than building shared public infrastructure. Take openGauss: early on, it still identified as part of the PG community; later, it marketed itself as "100% independently developed," spun up its own camp, and took a sizable group of contributors with it. Several rounds of fragmentation left the community badly depleted.

**Second, users stopped being the priority.** Conferences increasingly resembled trade shows. The community used to hold several events a year; eventually, it struggled to pull together even a single annual conference. When it did happen, the program read like a string of vendor infomercials: speakers took turns pitching products and peddling hype on stage, while users in the audience walked away with nothing practical they could use at work. It functioned more like an annual vendor reunion and dinner than a conference for users.

The end result was a **hollowed-out community**. What, in practice, was it giving users?

Documentation? As far as I recall, the community's Chinese translation stalled at PG 15. Package repositories? None. Alibaba Cloud, Tencent Cloud, and Tsinghua University eventually mirrored the PGDG repositories, but when upstream changed its sync mechanism, those mirrors sat broken for months. I ended up building and running a mirror myself. Only after I criticized the outage publicly did a few providers fix theirs—and even then, those were corporate and university mirrors, not community infrastructure.

[Chokepoint: PostgreSQL Cuts Off Mirror Sync Channels](/en/pg/pg-mirror-break/)

[What the PostgreSQL Mirror Cutoff Reveals About Software Supply Chain Trust](/en/pg/pg-mirror-pigsty/)

Conferences? Even those were gradually falling apart.

## A Community's Roots Are in Its Users

What should an open-source community actually look like? Percona's Peter Zaitsev once framed it well: an open-source community has three layers—**developers, vendors, and users**. Many people spend their energy organizing vendors, but the user community is the root.

Viewed through that lens, the problem with the Chinese PG community is obvious. A local **developer community** never really took shape; PostgreSQL is built by contributors worldwide, and relatively few open-source projects from China have made a dent in the global PG ecosystem.

**A vendor community existed for a while, then splintered.** The Chinese community effectively operated as a loose vendor alliance, closer to a trade guild. Even that function lost relevance as China's domestic IT localization drive (*Xinchuang*) took hold and each vendor went its own way.

**A user community was never seriously built.** Yet that is the broadest and most foundational layer of all.

The PostgreSQL world naturally divides into core developers, vendors, and user groups—and user groups organize by country, city, or language. The Chinese PostgreSQL community should have been the textbook example: a user group serving the entire Chinese-speaking world.

What is a user group supposed to do? Nothing complicated: **build what users actually need.** For a Chinese-speaking PostgreSQL user, the checklist is straightforward:

- A distribution that works out of the box
- Chinese documentation that keeps pace with upstream releases
- Fast, reliable package mirrors in China
- Complete Chinese localization of server and client messages
- A Chinese-language portal
- A local forum where people can ask questions and compare notes

That list has barely changed from what I proposed seven or eight years ago.

## Stepping Up Myself

For years I stayed away from this because it looked like far too much work for one person. It turns out that assumption is no longer true.

**No flagship project from the Chinese community?** Pigsty, the PostgreSQL distribution I maintain, is now one of the most widely adopted open-source PG projects to come out of China, and currently the most-starred Linux-native PG distribution on GitHub. It solves the most common practical obstacle users face: getting PostgreSQL into production. From bare metal to a production-grade cluster, it provisions high availability, point-in-time backup and recovery, monitoring, and extensions in one go—effectively an open-source, self-hosted RDS. A community of nearly 3,000 users has formed around it.

**[Building a PostgreSQL Distribution Rooted in China, for the World](/en/pg/forge-a-pg-distro/)**

**No up-to-date Chinese documentation?** Working with AI agents, I translated the official PostgreSQL manuals across more than 30 major versions—from 6.3 through 20—and paired them with better full-text search. I also maintain Chinese documentation for essential ecosystem tools including Patroni, pgBackRest, PgBouncer, and pgBadger.

[Chinese PostgreSQL Docs Are Live: All 11 Major Versions](/en/pg/pgsql-cc-online/)

[Chinese Documentation for PostgreSQL 18, 17, 16, 15, and 14](/en/pg/pgdoc-cn/)

**Half-finished message localization?** Simplified Chinese translations landed in PG 19 Beta 4, and Traditional Chinese ships with RC1. An automated translation and upstream-tracking workflow is now in place too, so from PG 19 onward, Chinese message coverage will stay current.

[PostgreSQL Now Speaks Chinese](/en/pg/pg-nls/)

[Why Localize PostgreSQL into Chinese?](/en/pg/pg-zh-tw/)

**No domestic package repositories?** I maintain a China mirror for PGDG along with an extension repository, served free of charge via CDN. Across 16 Linux distributions, it packages and distributes nearly 600 extensions and tools from the PG ecosystem, handling over a million downloads a month.

[The Most Complete PostgreSQL Extension Repository](/en/pg/pg-ext-repo/)

[pig: A Package Manager for PostgreSQL and Its Extensions](/en/pg/pig/)

**No Chinese-language portal?** The community portal and PG knowledge base are live at [pgsql.cc](https://pgsql.cc/). It tracks authoritative updates from `postgresql.org` daily, provides Chinese full-text search and a structured PG knowledge graph, and runs a daily news column that has been publishing for over six months.

[pg.center: The PostgreSQL Website in Chinese](/en/pg/pg-center/)

[A Daily News Column for the Chinese PostgreSQL Site](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493166&idx=1&sn=67e34928473b23e7cbf6169f9e0260cb&scene=21#wechat_redirect)

**No voice for Chinese developers in the global PG community?** Earning a voice means showing up at conferences in person, talking to people face to face, building trust, and doing the upstream work. Over the past few years, that effort has moved several things forward:

- The PG extension catalog I built is now used not only by Pigsty, but also by PG vendors and service providers around the world. See: [Extensions for Everyone: PGConf.Dev 2026 Talk](/en/pg/extensions-for-everyone/)
- [Helped bring LoongArch (`loong64`) into PostgreSQL's official APT repository](/pg/pg-apt-loong64/)
- [Identified flaws in PostgreSQL's GB18030 encoding support and helped get them fixed upstream](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487665&idx=1&sn=7792bc69e14bdcd606ec7780ed087101&scene=21#wechat_redirect)
- Rust extensions are starting to enter the PGDG repositories: Devrim went from flatly rejecting any Rust extension to accepting the Rust-based `postgresql_anonymizer` into the Yum repository.

My point is simple: this is doable. The Chinese-speaking PG world now has a cohesive developer group, projects of its own, and active representation in the global community.

## Capability Is No Longer the Bottleneck—Commitment Is

A few years ago, any one of the items above would have kept a small team busy for months: translating full manuals across 31 historical major versions, localizing more than 60,000 messages, building and distributing packages across 16 OS platforms. Tackling that alone with two hands would have been like moving a mountain one shovelful at a time.

Now we have AI. Agents can do real work in volume. One person directing a fleet of agents can ship what used to require a dedicated team. Once execution capacity is no longer the bottleneck, everything comes down to two things: **your vision for what ought to exist, and your commitment to seeing it through.**

If the motivation is purely commercial—"let's put on a conference and collect sponsorship checks"—it probably won't work, and even if it does, it won't matter much. But if you care about the craft and want more people to run PostgreSQL well, the work is both doable and worth doing. Genuine care and follow-through cannot be automated. In an era when AI can generate almost anything, they are the one thing it cannot replace.

## Reviving a Community for Users

To be clear upfront: **I have no interest in running a vendor community.** The playbook of going cap in hand to vendors, selling sponsorship tiers, and staging trade shows has been around forever, and plenty of people still run it. I will leave that to them. What I want to build is straightforward: if you use PostgreSQL, the resources here should make your job easier; when you hit a problem or have an idea worth sharing, you should have a place to talk with peers.

A user community needs a concrete value proposition. It cannot vaguely claim to "serve PG users" without delivering anything tangible. That is why the distribution sits at the center, with Chinese documentation, message localization, package mirrors, and user forums built around it. One more point: **a Chinese-language community is not just a mainland China community.** Taiwan, Singapore, and Malaysia all have large Chinese-speaking user bases. That is why Traditional Chinese was included in the localization work from the start. I know many friends in the PG community across Taiwan and Southeast Asia, and this community belongs to the entire Chinese-speaking world.

Next, I plan to fill in the remaining pieces step by step:

- A complete getting-started tutorial series in Chinese
- Practical, interesting user case studies
- Occasional podcasts and technical talks

## Many Hands Make a Community

One last practical note: AI lets one person build a lot of infrastructure, but plenty of things still cannot be done solo.

Software and extensions need real-world testing. Translations need readers who spot awkward phrasing and bugs. Case studies need practitioners willing to share what they learned in production. Forums need experienced users willing to answer questions. A community is only a community when it belongs to more than one person. I am happy to lay the groundwork; the rest takes all of us pitching in.

![An elephant-headed wizard and a child riding a donkey cart toward a distant village](featured.webp)

Whether you have a story from running PostgreSQL in production, spotted a bug in the packages, translations, documentation, or knowledge graph, or just want a place to talk shop about PostgreSQL, you are welcome to join us.
