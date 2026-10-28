---
title: "Why Localize PostgreSQL into Chinese?"
date: 2026-10-10
authors: [vonng]
summary: >
  Both Simplified and Traditional Chinese message catalogs in PostgreSQL 19 now meet the release threshold across all 28 components. Chinese localization lowers reading overhead during production incidents, gives new users a better first impression, and fills basic documentation and community gaps that went neglected for years.
tags: [PostgreSQL, PG Ecosystem, Documentation]
images: [featured.webp]
---
The PostgreSQL 19 release schedule is set: RC1 lands next Thursday, October 15, and barring surprises, the final release follows on October 29.

Good news for Chinese-speaking users along with it: following Simplified Chinese, **Traditional Chinese message localization is now in PG 19 as well**. Starting with this release, PostgreSQL speaks both Simplified and Traditional Chinese in full.

I wrote about the [Simplified Chinese work](/en/pg/pg-nls/) earlier. Today I want to explain why I did it in the first place.

![Peter Eisentraut confirming that Simplified and Traditional Chinese message translations for PostgreSQL 19 have been merged upstream](upstream.webp)

## Simplified and Traditional Chinese Both Clear the Bar

A quick recap: the Simplified Chinese (`zh_CN`) message translations [I submitted upstream](/en/pg/pg-nls/) shipped with 19 Beta 4. Over the past few days, I did another proofreading pass over Simplified Chinese, generated the Traditional Chinese (`zh_TW`) catalogs from that revised base, and submitted those upstream as well. They will ship with next week's RC1.

![Message translation coverage matrix for PostgreSQL 18 and 19 across 28 components and 30 languages](coverage.webp)

The numbers are public on PostgreSQL's official translation status site, [babel.postgresql.org](https://babel.postgresql.org/). The PG 19 branch has 28 translatable components totaling more than 12,600 messages—from the `postgres` server backend and the `psql` CLI client to utilities like `pg_dump`, `pg_basebackup`, and `pg_upgrade`.

![The PostgreSQL 19 message translation status table on babel.postgresql.org](babel.webp)

As of today, all 28 components sit at 98% or higher in both Simplified and Traditional Chinese: the `postgres` server catalog (6,806 strings) is at 99%, and `psql` (1,536 strings) is at 100%.

Across all 30 languages tracked upstream, **only five have every component at 98% or above: German, Swedish, Ukrainian, Simplified Chinese, and Traditional Chinese.** Long-standing translations for major languages like Japanese, French, Russian, and Spanish still have unfinished components.

![Overall translation coverage across 30 languages from PostgreSQL 18 to PostgreSQL 19](languages.webp)

Compare that with the PG 18 branch: in Simplified Chinese, `libpq` sits at 13%, `pg_upgrade` at 25%, and `pg_waldump` at 31%; in Traditional Chinese, `pg_combinebackup` is at 52% and `pg_basebackup` at 62%. Components below the release threshold are dropped from the release; those that clear it still fall back to English for every untranslated string. That is why PostgreSQL on a Chinese system used to produce half-Chinese, half-English output.

![Component-by-component translation coverage gains from PostgreSQL 18 to 19 in Simplified and Traditional Chinese](cn-progress.webp)

(All figures above come from [babel.postgresql.org](https://babel.postgresql.org/) as of October 10, 2026.)

Starting with PG 19, an automated translation and tracking workflow is also in place. One more merge will go in before the final release to bring every component to 100%. New upstream strings will be tracked continuously, with Simplified and Traditional Chinese updated in lockstep, so Chinese coverage won't fall behind again.

![The Chinese PostgreSQL message catalog repository and continuous translation maintenance workflow](workflow.webp)

## Traditional Chinese Is More Than Script Conversion

The shortcut for Traditional Chinese is to run the Simplified Chinese files through a converter like OpenCC. That falls short because mainland China and Taiwan use different technical vocabularies. Dictionary-based conversion catches some common words, but what it misses or mangles reads awkwardly to engineers in Taiwan. A few everyday examples:

![Technical terminology differences between mainland China and Taiwan for database, server, memory, file, default, field, transaction, and thread](terms.webp)

Instead of mechanical conversion, this Traditional Chinese edition was generated from the revised Simplified Chinese base, with regional terminology reviewed and adjusted across the catalog. I settled the term mappings one by one with help from Claude and Codex, and the overall result is solid. Because both editions come from the same base, they share the same structure, tone, and phrasing conventions, and will be updated together going forward.

![The pgsql.cc translation workbench comparing English, Simplified Chinese, and Traditional Chinese messages side by side](workbench.webp)

Even so, cross-strait language habits differ. If you are in Taiwan or use Traditional Chinese regularly, feedback is very welcome—if a string reads awkwardly or a term feels off, let me know. Every message and its translations can be browsed in the translation workbench at [pgsql.cc/nls](https://pgsql.cc/nls/).

## Why Localize When AI Is Already This Good?

I get asked this often: programmers work in English anyway, so why bother? Fair point. In my own shell environment, `locale` is pinned to English, and all my code comments are in English too. English is the lingua franca of software, and with AI at hand, anyone can paste an unfamiliar error into a prompt and get a translation in seconds. Why spend the effort?

I still think the work is worth doing, for three reasons.

**First, native-language reading is faster.** I can read English fine, but I can take in a page of Chinese at a glance; English takes an extra beat. During normal development you barely notice. At 3 a.m. during a production outage, with errors scrolling across the terminal, that extra beat is real. Nobody in the middle of an incident has time to open a chat window and ask an LLM to translate logs.

**Second, not every user reads English as comfortably as seasoned developers do.** Clearer Chinese error messages help a much broader group of Chinese-speaking users grasp what went wrong and why. Localization is never built for experts; it is built for everyone else.

**Third, half-baked localization hurts first impressions and raises the barrier for newcomers.** Most users run their OS in Chinese and never touch `locale` or `LANG`. Install PostgreSQL on a Chinese system, and Chinese messages are what you get by default. Before PG 19, those messages were stale, fragmentary, and mixed with English—far worse than plain English.

When a new user sees localization in that state, the natural reaction is: **Is this really PostgreSQL's standard of quality?** You either don't localize at all, or you do it properly. Leaving a half-finished job as the default is the worst option.

## Three Related Sites

Localized messages make error output readable, but using PostgreSQL well also takes documentation and reference material. For that, I built three sites: [pgsql.cc](https://pgsql.cc/), [pg.center](https://pg.center/), and [pgext.cloud](https://pgext.cloud/).

**[pgsql.cc](https://pgsql.cc/)** is the Chinese counterpart to postgresql.org, maintained by the Pigsty team. Everything on the upstream website has a Chinese version here. Its signature resource is the complete set of official PostgreSQL manuals across all 31 major versions from 6.3 through 20devel, translated into Chinese with consistent standards, style, and terminology. It also comes with improved full-text search for looking up database objects across versions.

![Full-text search and documentation preview on pgsql.cc](doc-search.webp)

The site also includes an extension encyclopedia, a daily PostgreSQL news feed, and a PostgreSQL knowledge graph. News and updates from the Chinese PostgreSQL community will be published here as well.

[Chinese PostgreSQL Docs Are Live: All 11 Major Versions](/en/pg/pgsql-cc-online/)

[A Daily News Column for the Chinese PostgreSQL Site](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493166&idx=1&sn=67e34928473b23e7cbf6169f9e0260cb&scene=21#wechat_redirect)

![The PostgreSQL daily news column on pgsql.cc](daily.webp)

**[pg.center](https://pg.center/)** is a bilingual English-Chinese site (defaulting to English) aimed at organizing knowledge from across the PostgreSQL world into a comprehensive reference encyclopedia. Recently, for instance, we indexed PostgreSQL's built-in objects—SQL commands, data types, functions, configuration parameters, and more—and mapped how each evolved across 31 major versions.

![The PostgreSQL object index on pg.center, tracking commands, data types, functions, and parameters across versions](objects.webp)

It also hosts the 31 major versions of the PostgreSQL manual, alongside bilingual documentation and indexes for Patroni, pgBackRest, PgBouncer, etcd, and HAProxy. If there are other projects or references you would like to see included, let us know and we will keep expanding it.

![Community component documentation index on pg.center](components.webp)

**[pgext.cloud](https://pgext.cloud/)** tracks the PostgreSQL extension ecosystem, cataloging more than 2,600 extensions with structured metadata and bilingual usage documentation for each one. Beyond the catalog, the PGSTY repository ships prebuilt binary packages for 600 quality extensions across 16 major Linux distribution releases, ready to install via RPM and DEB.

![The PostgreSQL extension catalog and RPM/DEB package matrix on pgext.cloud](extensions.webp)

Together, these sites serve as a portal for Chinese-language PostgreSQL documentation and tooling.

## Closing Thoughts

Localization may be a small thing in itself. While doing it, though, I kept coming back to a bigger question: why did basic work like this go untouched for so many years? What was the Chinese PostgreSQL community doing? And what were all the PostgreSQL-derived "domestic databases" in China doing?

The short answer, in my view, is the absence and decline of the Chinese PostgreSQL community. That brings us back to the title: why localize PostgreSQL into Chinese? My own environment runs in English, and I rarely read Chinese documentation. I will probably never use most of this work myself.

![An elephant and a pig practicing Chinese calligraphy in a classical garden, symbolizing PostgreSQL and Pigsty's Chinese localization work](featured.webp)

Still, I know plenty of Chinese-speaking users need it. And by shipping practical infrastructure that users actually benefit from, I want to take a shot at [reviving the Chinese-speaking PostgreSQL community](/en/pg/revive-pg-cn-community/). That is a larger topic, so I will save it for a dedicated post tomorrow.

That is all for today. Once PostgreSQL 19 ships, try installing it on a Chinese-language system—and if any phrasing reads awkwardly, let me know.
