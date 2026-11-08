---
title: "PostgreSQL Ecosystem Update: The AI Bug-Hunting Crunch"
date: 2026-11-06
authors: [vonng]
summary: >
  AI vulnerability hunting has open-source maintainers scrambling to patch, with PostgreSQL 19 and its extension ecosystem seeing a rush of updates. Here's a look at OrioleDB, DuckDB 2.0, vector search, unusual extensions, and my recent work on Chinese translations, Barn, Crib, and CapsLock.
tags: [PostgreSQL, AI, PG Ecosystem, Extension]
images: [overview.webp]
---

In two recent posts, [The Cloud Is About to Be Shot Full of Holes](/en/cloud/blackwall/) and [The Internet Has Already Been Shot Full of Holes](/en/cloud/net-attack/), I wrote about an uncomfortable reality: **AI is putting the entire software world through a trial by fire.**

With AI vulnerability hunters and automated scanners running flat out, open-source communities are getting buried in bug reports and security issues almost daily. Even the famously steady PostgreSQL community has been caught up in it: **PG 19 has already been delayed by this wave of fixes.**

If all goes well, the release will be frozen and packaging will begin on November 9, with the final release the following week. My main wish right now is that no nasty surprise turns up in the next few days to push it back again.

The PG core is hardly alone. Across the extension ecosystem, maintainers are shipping releases in quick succession and struggling to keep up with security problems.

![Overview of recent PostgreSQL ecosystem updates](overview.webp)

The clearest sign is **PostGIS 3.7.0**. Security problems in two companion extensions had previously affected nearly every major managed PG cloud provider. For 3.7.0, PostGIS decided to cut them loose: it **removed `address_standardizer` and `postgis_tiger_geocoder` from the core package entirely**. They are now built and distributed separately. When AI is finding holes everywhere, shedding non-core components and shrinking the attack surface seems sensible.

Recent changelogs are full of similar hardening work: `emaj 5.0.1` fixed a privilege escalation vulnerability, `pg_anon 3.3.2` shipped a security update, and extensions everywhere have been churning out patches. When upstream moves this fast, those of us packaging and distributing its software have to keep up. Over the past month or two, I've been tracking core and extension releases at roughly **one batch a week**. With this latest round of updates, here's a look at the major changes in the PG ecosystem, plus a few odd things I've been building on the side.

## 1. Engine Milestones: OrioleDB Goes Stable, Multimodel Branches Arrive

The highlight of this batch is **OrioleDB's long-awaited stable release**.

If you've run into the limitations of PG's storage engine, you'll know OrioleDB's approach: undo logs and modern page-level concurrency control, designed to eliminate the bloat and frequent-update bottlenecks of PG's native heap-based MVCC. After a long beta period—we were still packaging `1.8-beta16` and `1.10~beta19` last month—OrioleDB has finally dropped the beta label with **version 1.10.1**, covering three mainstream PG branches: **PG 16.15, PG 17.11, and PG 18.6**. Several other major engines and releases are now available too:

- **Babelfish 6.2.0 officially supports PG 18**: Babelfish, which provides SQL Server protocol and T-SQL compatibility, now ships `babelfish-18` at **6.2.0**, based on PG 18.6 and including all four companion extensions. The PG 17 branch has also moved to **5.7.0**.

- **CloudBerry 2.2.0 is out**: a major release from one of the leading open-source MPP data warehouse projects.

- **PG flavors, all in one place**: alongside the standard PGDG builds, heavily customized PG branches have been shipping fixes in quick succession. I've brought them all into the repository: Alibaba Cloud's **PolarDB 17** (updated to `17.11.1.0-2PGSTY`, with a PolarStore SDK update), the graph database **AgensGraph 18** (updated to `2.18.6.1`), the Oracle-compatible **IvorySQL 5.6** (based on PG 18.6, with 38 extensions), the multimaster distributed engine **pgEdge 15–18** (bundling the latest `Spock 5.0.13`), and **Percona's `pgtde-18`**, which focuses on transparent data encryption (updated to 18.6.1).

I've packaged all of these as ready-to-use RPMs and DEBs across 16 Linux platforms. Give them a try.

## 2. DuckDB 2.0 and Some Unusual New Extensions

The past two months have brought a steady stream of new packages and major extension upgrades. A few stand out:

### 1. DocumentDB 1.0 Goes Stable, DuckDB 2.0 Arrives

Microsoft's open-source MongoDB-compatible engine, **DocumentDB**, has reached **1.0**, supporting PG 16–18. On the analytics and lakehouse side, DuckDB 2.0 has arrived: **`pg_duckdb 1.2.0`** and **`duckdb_fdw 2.0.2`** both now use the latest **DuckDB 2.0.0** engine. The two still cannot coexist in the same instance; pick one. Add the **3.6.0** release of **`pg_lake`**, a fix in **`pg_parquet`** for temporary file leaks during streaming COPY, **Citus 14.3.0**, and **TimescaleDB 2.31.0**, and PG's native lakehouse toolchain is looking considerably stronger.

### 2. Search and Vector Extensions Move Ahead

We maintain **`vchord`**, which is now at `1.2.0-2PGSTY`, with improved reranking accuracy for `vchordg` and `halfvec` candidate sets. Its companion extensions, **`vchord_bm25`** and **`pg_tokenizer`**, have both reached their **1.0.0 stable releases**, with native `tsvector` support and external Lindera 6 dictionaries. ParadeDB's `pg_search` (0.26.5) has also been releasing frequently, as have `pg_fts` (1.16.0), `pg_turbovec` (2.15.0), and `pgroonga` (4.1.0).

![PostgreSQL search and vector extensions](search.webp)

### 3. A Few Inventive New Extensions

Some interesting newcomers have joined the catalog:

- **`pg_agent_gate` (0.4.1)**: a permissions gatekeeper for the AI era, controlling what LLM agents can access in the database.

- **`pg_opencc` (0.1.0)**: a thin wrapper around libopencc that I built with Claude. It uses OpenCC to convert between Simplified and Traditional Chinese, supports PG 14–18, and saves you from hauling text back to the application layer just to normalize or convert it.

![Documentation for the pg_opencc extension](extensions.webp)

- **`pg_statecharts` (0.1.0)**: finite state machines and statechart transitions directly inside PostgreSQL.

- **`pg_grammar_guard` (0.4.9) and `pg_living_assertions` (0.5.10)**: syntax guardrails and dynamic, continuously checked data assertions inside the database.

- **`kafgres` (0.3.2)**: lets PG moonlight as a Kafka broker. Other additions include **`pg_tre` (4.6.1)** for approximate regular expressions (fuzzy regex matching), **`pg_nanotime` (0.2.0)** for nanosecond timestamps, and **`pg_kv` (0.1.0)**, a fast, nonpersistent key-value store backed by shared memory.

## 3. Taking Over Projects, Fixing Bugs, and Cleaning Up After Big Tech

Maintaining a package repository across more than a dozen operating systems and hundreds of extensions often means doing the unglamorous work of keeping the open-source supply chain running. A few stories from these batches deserve a mention.

### Almost Taking Over `pg_mooncake`, Then Sending the Fixes Upstream

The long-neglected `pg_mooncake` had been stuck on an old version, unable to work with the new `pg_duckdb 1.2.0` (DuckDB 2.0) and `pgrx`. I went in and updated it to `0.3.0`, intending to take over maintenance as well.

[Rescuing Another Open-Source Project: Yesterday vchord, Today Mooncake](/en/pg/fork-pg-mooncake/)

Just after I'd built the packages, Mooncake Labs' CEO got in touch and said the team was still willing to maintain the project. Having the original developers look after it is good news, so I submitted all the compatibility changes upstream.

### Fixing Upstream Bugs Along the Way, Including AWS's

Building and running QA across every supported platform often turns up obscure upstream bugs. Sometimes I don't feel like filing a report and just fix them in a patch. The amusing part is that `pgactive` and `pgcollection` are AWS extensions. You'd think they'd be free of such elementary mistakes. I cleaned those up too. In a sense, a broad packaging and distribution matrix is one of the best stress tests the open-source ecosystem has.

## 4. Side Projects to Burn Through Tokens

That's enough extension packaging. Here are a few other things I've been tinkering with. With plenty of tokens and a good AI workflow, it can be surprisingly hard to stop building.

### 1. Teaching PG Chinese: Core Messages and Documentation for All 508 Releases

First, two bits of good news on Chinese localization.

As I mentioned before, I've finished translating the PG 19 core messages into Chinese. The better news is that **the supported PG 15 through PG 18 branches will officially include the Chinese translations in next week's minor releases too!** In about a week, all the mainstream PG branches will have new releases that speak fluent, natural Chinese.

![Chinese translation coverage for PostgreSQL messages](pg-zh.webp)

*At the time of writing, Simplified Chinese, Traditional Chinese, and Swedish are the only three languages with 100% coverage across all messages.*

Another large project is nearly done: **translating the entire history of PG documentation into Chinese**. I previously translated [the official PG documentation for all **31 major versions**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493128&idx=1&sn=d28faa447c8f9b527d872189ca3aed7b&scene=21#wechat_redirect). Recently, I **[put my entire GLM subscription token allowance into it](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493329&idx=1&sn=2841675aa9c3e4c4c78d6901e096c73d&scene=21#wechat_redirect)**, running translation jobs in the background around the clock for the past week or two. With those 31 major versions finished, I've moved on to the documentation for **all 508 minor releases** in PG's history. It's now **about 80% complete**. Once the remaining 20% is done, we'll have translated every version of the official PostgreSQL documentation, all the way back to the project's beginnings. That's a satisfying thought.

To make bilingual reading easier, my documentation framework **Oink** is now at **version 1.5.1**, with a new **side-by-side bilingual view**. When reading technical books or documentation in Chinese and English, the two panes scroll smoothly in sync. It works very well. I couldn't be bothered to pad out a separate post about it, so consider this its brief plug.

![Oink's side-by-side bilingual reading view](oink.webp)

### 2. Barn: Launch a Local Fleet of Agent VMs on Your Laptop

We also quietly released **Barn**, a virtual machine manager. I've been happily using it in private for a while, without announcing or promoting it. My rule has always been to get plenty of use out of a tool myself first.

Think of it as a lightweight, self-contained Vagrant: **a way to spin up a fleet of VMs on your Linux or macOS laptop with one click**, or more directly, **a local sandbox for AI agents**. Whatever system environment your agent needs to experiment with, you can have a clean local VM running in seconds.

The best part is that it **can launch macOS VMs directly**. Apple's virtualization terms limit a Mac host to two concurrent macOS VMs, but that still **takes your agent's computer-use environments from 1 to 3** on the same machine, safely isolated and at very little cost. If you're running a busy fleet of agents that need multiple computer-use environments, give it a try. Barn's design and uses deserve a separate post later.

![Barn virtual machine manager](barn.webp)

### 3. Crib and CapsLock: Trying My Hand at Native macOS Apps

Alongside Barn, I have two small native macOS tools I use frequently:

**Crib**: a local PG documentation browser I built for myself and am now polishing for a public release. It effectively puts the whole `pg.center` knowledge base on your computer, giving you instant offline search through every version of PG's documentation in a lightweight native macOS app.

It can also browse and search the full text of Oink-based websites offline.

![Barn virtual machine manager](crib.webp)

**CapsLock**: a productivity tool I use hundreds or thousands of times a day on my laptop. I used to piece together the key remapping and app switching with a pile of Karabiner configuration files. Then I figured that, with tokens to spare, I might as well build a dedicated app. Customizing it and changing app rules is much easier that way. It was also my first attempt at native macOS app development.

![CapsLock productivity tool for macOS](capslock.webp)

**Barn, Crib, and CapsLock are all fully native macOS apps**. To distribute them properly, I've recently worked through the whole process: signing up for an Apple developer account, signing the apps with certificates, notarizing them, and packaging them. It was an interesting exercise. When they're ready for their public debut, I'll introduce each one in its own post.
