---
title: "The Open-Source Maintainer of Last Resort Is Back: vchord Yesterday, Mooncake Today"
date: 2026-11-05
authors: [vonng]
summary: >
  The day after taking over vchord, Lao Feng took on pg_mooncake too: rescuing its docs and blog, updating it for pg_duckdb and pgrx, and keeping it working for Pigsty users.
tags: [PostgreSQL, Extension, Open Source]
images: [home.webp]
---

> [Originally published on WeChat](https://mp.weixin.qq.com/s/hvOHVOmZqFozun6O5eIkDg)

Lao Feng, open source's maintainer of last resort, is back yet again...

Yesterday I published a piece about `vchord`, [**a look at taking over a vector database extension in a day**](/en/pg/maintain-vchord/). Before that post had even settled, I casually took on another extension of roughly the same size—**`pg_mooncake`**. As it happens, it is written in Rust too. Since I had already taken over `vchord`, I figured I might as well go all the way and maintain `pg_mooncake` too.

<https://mooncake.pgsty.com/>

![The new Mooncake documentation site homepage](home.webp)

## Why Take Over pg_mooncake?

The immediate reason is simple: **the upstream was acquired, and the subextension was about to be left without support.**

Mooncake Labs, the team behind `pg_mooncake`, was acquired by Databricks this year. The usual open-source script is that once a startup team is absorbed by a large company, the open-source projects it leaves behind are unlikely to keep receiving maintenance.

![The upstream pg_mooncake repository, whose latest commit is already a year old](upstream.webp)

And this was precisely when a critical major-version update landed underneath it. `pg_mooncake` is a subextension built on `pg_duckdb`; **DuckDB 2.0.0** was released recently, with plenty of changes under the hood, and the parent extension `pg_duckdb` followed with a new release. With dependencies this tight, an upgrade to the parent makes the child unusable unless the child is updated to match.

The original team had already been acquired and moved on, with no word for over a year. So what do you do? You step in and take it over.

## The Usual Three-Move Playbook: Rescue, Revive, and Backstop

After taking it on, I followed the same familiar playbook:

**First: rescue the documentation and blog.** Its official documentation site was gone; visiting `mooncake.dev` now redirects straight to the Databricks website. Fortunately, the Internet Archive still had historical snapshots. I dug the complete documentation set and historical blog posts out of the dusty archives. Honestly, it would be a shame to let such a good extension rot unfinished.

![Restored Mooncake technical documentation](docs.webp)

![Restored Mooncake engineering blog](blog.webp)

**Second: update it for the new stack and give the code another lease on life.** `pg_mooncake` had been stuck at `0.2`; this time I took it straight to **`0.3`**, added compatibility with **`pg_duckdb 1.2`**, and upgraded the underlying **`pgrx`** framework to its latest version, 0.19.3. When **PostgreSQL 19** arrives, I will update it for that too.

Why did I bother? Because I know several Pigsty users actually use it. The biggest sin in maintaining a distribution is to provide an extension in one release, then tell users it disappeared when the next release arrives. That is awkward. Someone has to take the baton. And I had just finished `vchord`; the first time is a learning curve, the second is routine.

**Third: keep it on a light maintenance schedule and evolve it as needed.** It is not much of a day-to-day burden. There is no need to keep tinkering with it; once a year, catch up with a PostgreSQL major release or an update to `pgrx` or `pg_duckdb`. If users need something new, they can ask; if it looks sensible and is easy enough, Lao Feng will do it.

![The pg_mooncake download and installation guide](install.webp)

## Upstream Can Walk Away; the Distribution Has to Keep Users Covered

As PostgreSQL continues to eat the database world, having a few good extension cards in hand is a nice position to be in.

Apache AGE, a graph database extension for PG, was once used by many people. It stalled for a while when its core maintainer lost their job. At the time I thought: if nobody takes it over, I will. Fortunately, interest in graph databases heated up again, and the project came back to life on its own.

Not every open-source project gets that lucky. Upstream startups get acquired, pivot, or abandon projects altogether; half-finished projects are simply part of the open-source ecosystem. **I build a distribution; my job is to package, compile, and distribute software. No matter how upstream projects are abandoned or their maintainers walk away, if the distribution layer can keep users supplied and prevent the software supply chain from breaking, that is enough.**

Yesterday's `vchord` and today's `pg_mooncake` are two attempts in that direction. Once you understand PostgreSQL's internals and the architecture of its lower-level extensions, the whole thing is manageable and reliable at a high level; for users, being able to keep using it reliably matters more than anything.

The extensions discussed yesterday (`vchord`) and updated today (`pg_mooncake`), along with the rest of the collection, are now officially released and ready to use. They are all included in the **Pigsty** extension repository and work out of the box, support **PG 14 through PG 18**, and cover **16 operating systems**. You can download the packages directly or install them with your system package manager.

![The pg_mooncake packages and platform support matrix in the Pigsty extension repository](packages.webp)
