---
title: "Reviving the Chinese-Speaking PostgreSQL Community"
date: 2026-10-12
draft: true
authors: [vonng]
summary: >
  A PostgreSQL community starts with its users. With a distribution, documentation, package mirrors, localized messages, and a Chinese-language portal in place, the next step is to build a community that serves users across the Chinese-speaking world.
tags: [PostgreSQL, PG Ecosystem, Open Source]
images: [featured.webp]
---
PostgreSQL is the world's most advanced open-source database. It is also one of the few open-source projects truly run by its community, with no single company holding the reins. I have always believed that the soul of an open-source project lies in its community, not its code.

So today I want to talk about something I have kept to myself for years: **reviving the Chinese-speaking PostgreSQL community.** I had the idea several years ago but felt awkward saying it out loud. Slogans are cheap; you need something to show for them. I finally have a few things to show, so let me start with something you will be able to see next week.

## Revival implies decline

To talk about a revival is to acknowledge a decline. That saddens me. The Chinese-speaking PG community was reasonably active a few years ago. Lately it has grown quieter and quieter, with barely a few signs of life each year. The contrast with PostgreSQL's growth around the world is hard to miss.

The community's former chair was my business partner and colleague, and I know most of the people in that circle. As early as 2018, I repeatedly suggested that the community do a few practical things for users:

1. Set up a PG download mirror in China. Many mirror sites did not carry the PGDG repositories back then.
2. Keep the Chinese documentation up to date. People were translating it, but the translations often lagged by several major versions, or a year or two.
3. Build a community PostgreSQL distribution and use it to bring together a small group of developers.

You know what happened next. None of this got off the ground. The community stayed busy organizing conferences and meetups, but its voice faded and the community itself sank further into inertia. There are many reasons. Here are the two I can see most clearly.

**First, China's domestic database push pulled people away.** A slew of databases heavily modified PG, reskinned it, or wrapped it in a new product; many simply refused to acknowledge their PG roots. People cared more about their own patch of turf than shared infrastructure. Take openGauss: early on, it acknowledged being part of the PG community. Later it started claiming to be “100% independently developed,” struck out on its own, and took a group of people with it. Several rounds of fragmentation left the community badly depleted.

**Second, users stopped being the priority.** Conferences increasingly resembled trade shows. We used to have several events a year; eventually, even the annual conference became hard to organize. When it did happen, it looked more and more like a string of product commercials. Vendors took turns pitching and bullshitting on stage, while users left with nothing they could actually use. It was closer to an annual vendor reunion and dinner than a conference for users.

The result was a **hollowed-out community**. What, exactly, did it provide for users?

Documentation? As far as I recall, the community's Chinese translations stopped at PG 15. A package repository? No. Alibaba Cloud, Tencent Cloud, and Tsinghua University eventually set up PGDG mirrors, but when upstream stopped updating their feeds, those mirrors went stale for months too. In the end, I had to build a mirror myself. After I criticized the situation publicly, a few others caught up. But those were efforts by companies and universities, with little to do with the community.

[PGDG Cuts Off Mirror Synchronization](/en/pg/pg-mirror-break/)

[The PostgreSQL “Supply Cut” and Trust in the Software Supply Chain](/en/pg/pg-mirror-pigsty/)

Conferences? Even those were gradually falling apart.

## A community starts with its users

What should a community look like? Percona's Peter Zaitsev once made a point along these lines: an open-source community has three layers—**developers, vendors, and users**. Many people focus on the vendor community, but the user community is the foundation.

Apply that lens to the Chinese-speaking PG community, and the problem becomes clear. A Chinese-speaking **developer community** never really got off the ground. PG is built by developers around the world, and relatively few projects from China have made a mark in its ecosystem.

**There was a vendor community. It fell apart.** The Chinese-speaking community effectively became a vendor alliance, a loose association resembling a trade guild. Even that role became marginal as China's push for domestically controlled IT took hold and each vendor went its own way.

**A user community was never taken seriously.** Yet that is the broadest and most fundamental layer.

The PG world already has many overlapping communities: core developers, vendors, and users. User communities can be organized around countries, cities, or languages. A Chinese-speaking PostgreSQL community should be a natural example: a user group spanning the entire Chinese-speaking world.

What should a user group do? There is nothing mysterious about it: **build what users need.** For a Chinese-speaking user, the list is straightforward:

- A distribution that works out of the box
- Chinese documentation that keeps pace with releases
- Reliable package mirrors in China
- Complete Chinese localization of software messages
- A Chinese-language portal
- A local community where people can talk and ask for help

That list has barely changed from the suggestions I made seven or eight years ago.

## Time to do it myself

I used to stay away from this because I thought there was too much work for one person. Then I discovered that might not be true.

**No flagship project for the Chinese-speaking community?** My project, Pigsty, is now probably the strongest open-source project to come out of China's PG ecosystem. It has earned a place among PG distributions worldwide and has more GitHub stars than any other Linux-native PG distribution. It addresses users' biggest obstacle: putting PG to work. From bare metal to a production-grade PostgreSQL service, it sets up high availability, backup and recovery, monitoring, and extensions in one go—effectively an open-source, enterprise-grade RDS. A small community of nearly 3,000 people has formed around it.

**[Building a PostgreSQL Distribution Rooted in China, for the World](/en/pg/forge-a-pg-distro/)**

**No Chinese documentation?** Working with AI agents, I translated the official PostgreSQL manuals for more than 30 major versions, from 6.3 through 20, and added better full-text search. I also maintain Chinese documentation for surrounding tools such as Patroni, pgBackRest, PgBouncer, and pgBadger.

[Chinese PostgreSQL Docs Are Live: All 11 Major Versions](/en/pg/pgsql-cc-online/)

[Chinese Documentation for PostgreSQL 18, 17, 16, 15, and 14](/en/pg/pgdoc-cn/)

**Half-finished message localization?** Simplified Chinese made it into PG 19 Beta 4; Traditional Chinese ships with RC1. The workflow for automated translation and tracking upstream changes is in place too. From PG 19 onward, Chinese coverage should no longer be a problem.

[PostgreSQL Now Speaks Chinese](/en/pg/pg-nls/)

[Why Localize PostgreSQL into Chinese?](/pg/pg-zh-tw/)

**No package repository in China?** I maintain a Chinese PGDG repository and mirror, distributed through a CDN and free for everyone to use. I package and distribute nearly 600 extensions and software packages from the PG ecosystem across 16 Linux platforms, with more than a million downloads a month.

[A Comprehensive Repository for PostgreSQL Extensions](/en/pg/pg-ext-repo/)

[A Package Manager for PostgreSQL Engines and Extensions](/en/pg/pig/)

**No Chinese-language portal?** The community site and PG knowledge base are ready too: [pgsql.cc](https://pgsql.cc/). It tracks authoritative updates from postgresql.org every day, with better Chinese full-text search, a distinctive PG knowledge graph, and a daily news column that has been running for more than six months.

[pg.center: The PostgreSQL Website in Chinese](/en/pg/pg-center/)

[A Daily News Column for the Chinese PostgreSQL Site](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493166&idx=1&sn=67e34928473b23e7cbf6169f9e0260cb&scene=21#wechat_redirect)

**Chinese developers have no voice in the PG world?** Then we need to attend conferences and meet people face to face. That is how you get heard, build trust, and get things moving. Over the past few years, we have made some progress:

- The PG extension catalog I built is now used by many PG vendors and service providers around the world, as well as Pigsty. See: [Extensions for Everyone: My PGConf.Dev 2026 Talk](/en/pg/extensions-for-everyone/).
- [I helped get the LoongArch architecture into PostgreSQL's official APT repository.](/pg/pg-apt-loong64/)
- [I identified flaws in PG's GB18030 support and helped get them fixed upstream.](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487665&idx=1&sn=7792bc69e14bdcd606ec7780ed087101&scene=21#wechat_redirect)
- Rust extensions are starting to enter PGDG repositories too. Devrim went from flatly refusing any Rust extension to including the Rust-based anonymizer in the Yum repository.

My point is simple: this is possible. The Chinese-speaking PG world now has a cohesive developer community, projects of its own, and a voice and representation in the global community.

## Capability is no longer the bottleneck. Commitment is.

A few years ago, many of these tasks would each have kept a small team busy for months: translating complete manuals for 31 historical major versions, localizing more than 60,000 messages, packaging and distributing software across 16 platforms. Doing all that with one pair of hands would have been like moving a mountain one shovelful at a time.

But now we have AI. Agents can do work, and a lot of it. One person directing a group of agents can do what once required a whole team. When capability is no longer the obstacle, two other things matter: **your vision for what you want to build, and your commitment to doing it.**

If the goal is merely commercial—“I'll organize a conference and collect some sponsorship money”—it probably will not work. Even if it does, there is little point. But if you love PG and want more people to use it and use it well, this is work you can take on and carry through. That passion and commitment are unique to you. In an age when AI can do just about anything, they are precisely what it cannot replace.

## The community I want to revive is for users

Let me be clear: **I have no interest in building a vendor community.** The model of going cap in hand to companies, rounding up sponsorships, and organizing trade shows has been around for years. People are still doing it, so I will leave that to them. What I want is this: if you use PostgreSQL, the resources here should help you. When you have a problem or an idea, you should have a place to share it and discuss it with others.

A user community needs a concrete reason to exist. It cannot vaguely promise to “serve PG users” without saying what it provides. That is why the distribution is the core, with Chinese documentation, localization, and the user community built around it. One more thing: **a Chinese-speaking community reaches beyond mainland China.** Taiwan, Singapore, and Malaysia all have many Chinese-speaking users. That is part of why I included Traditional Chinese in this localization effort. I know plenty of friends in the PG community from Taiwan and Southeast Asia. This community should belong to the entire Chinese-speaking world.

Here is what I want to add next:

- A complete getting-started guide in Chinese
- Real, interesting stories from users
- Occasional podcasts and talks

## Many hands make a community

One last practical point: AI lets one person do a great deal, but there are still many things one person cannot solve.

Software and extensions need testing. Translations need people to spot mistakes. User stories need real users to tell them. A community needs people willing to answer other people's questions. It is a community because it belongs to more than one person. I will get things started; the rest depends on all of us pitching in.

![An elephant wizard and a child ride a donkey cart toward a distant village](featured.webp)

Whether you have a new story to share about using PostgreSQL, have found a problem with the software, translations, documentation, or knowledge graph, or simply want somewhere to talk about PostgreSQL, you are welcome to join us.
