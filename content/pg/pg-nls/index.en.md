---
title: "Nobody Has Touched PostgreSQL's Chinese Error Messages in Seven Years"
date: 2026-09-16
authors: [vonng]
draft: true
summary: >
  PostgreSQL's Simplified Chinese message catalogs stopped on June 5, 2019. Only 9 of the 28 catalogs clear the 80% packaging threshold, the server's own catalog — the source of nearly every ERROR you actually see — sits at 61%, and it still ships mistranslations like rendering "out of memory" as "memory overflow," which sends people debugging in exactly the wrong direction. Translation debt comes due, and right now it is compounding.
tags: [PostgreSQL, NLS, i18n, Translation]
---

> Every Chinese error message you have ever seen in `psql` was last updated on June 5, 2019.

PostgreSQL has an official Chinese interface. `initdb`, `psql`, and every ERROR the server throws all run through an official set of gettext message catalogs.
The machinery is called [NLS](https://www.postgresql.org/docs/current/nls.html), and it is a different thing from the documentation: docs are written for you to read, messages are what the machine spits at you.

I went and checked where this stands today on [babel.postgresql.org](https://babel.postgresql.org/). It's uglier than I expected.

![Message catalog completion by language for PostgreSQL 19; Simplified Chinese at 66%](languages.png)

Take the horizontal cut first. Across the 28 message catalogs: German, Swedish, Ukrainian and Georgian all at 99%, Japanese 98%, Russian 91%, Korean 89%. Simplified Chinese: 66%, behind Greek and Italian.

The Republic of Georgia has 3.7 million people, barely more than one district of Shanghai, and it got all 28 catalogs to 99%.

![Simplified Chinese across all 28 catalogs: only 9 clear the 80% packaging threshold, and the main postgres catalog sits at 61%](catalogs.png)

Now the vertical cut. PostgreSQL has a hard rule: a catalog has to reach 80% before it is eligible to ship in a release. Below that line it simply doesn't get packaged. Of the 28 Simplified Chinese catalogs, 9 make it.

And the more important the catalog, the worse it is. The server's own `postgres` catalog — 6,826 messages, more than half of all the message text in the tree, the origin of nearly every ERROR you will ever look at — 61%. `libpq`, which every language driver in existence sits on top of, 408 messages — 12%. `pg_upgrade`, the thing a major version upgrade depends on, the moment you most need to understand what went wrong — 23%.

![The header of src/backend/po/zh_CN.po: PO-Revision-Date frozen at 2019-06-05, untouched for seven years and three months](crime-scene.png)

Open the file header and you'll see why.

`PO-Revision-Date: 2019-06-05`. `Project-Id-Version: postgres (PostgreSQL) 12`. Generated with [Poedit](https://poedit.net/) 1.5.7, a 2013 build.

This is not a historical archive. This is [the file on REL_19_STABLE](https://github.com/postgres/postgres/blob/REL_19_STABLE/src/backend/po/zh_CN.po) today, and master carries an identical copy.
From PG 12 to PG 19, seven years and three months, eight major releases, and not one byte of that header has changed.

Everything written into PostgreSQL over those seven years — logical replication, JIT, parallel query, `REPACK`, async I/O — has an empty Chinese column. Around 2,660 strings in the server catalog have never had a Chinese translation at all.
And of the 5,213 that were translated back then, roughly 1,000 no longer match today's msgid, because the source moved out from under them. Dead entries.

![A gallery of mistranslations: four renderings of out of memory, 「臭虫报告至」, pg_ctl losing its %m, and an ecpg argument mismatch](museum.png)

Worse than untranslated is mistranslated.

The same `out of memory` gets four different Chinese renderings in today's tree: 「内存用尽」 (*memory used up*), 「内存不足」 (*insufficient memory*), 「内存耗尽」 (*memory exhausted*), and 「**内存溢出**」 — *memory overflow*.
The first three are fine. The fourth is wrong. OOM means you asked for memory and did not get it, a clean failure. An overflow is a write past the end of a buffer that corrupts whatever sits next to it. For anyone staring at a broken system, those two point in opposite directions.
The error is contagion from Java, where `OutOfMemoryError` and `StackOverflowError` are taught side by side until, somewhere along the way, they collapse into one Chinese word.

`Report bugs to` comes out as 「臭虫报告至」 — literally *report bedbugs to*, the insect rather than the defect. Fourteen catalogs say it that way. It is a 2001 rendering left behind by the first translator, and it has lived straight through to 2026.

Two more are real bugs, not matters of taste:

In `pg_ctl`, `invalid binary "%s": %m` becomes 「无效的二进制码 "%s"」 — the `%m` is swallowed whole. When it fires you learn which file is wrong, and you never learn what errno said. The same string is translated correctly in other catalogs.

The `ecpg` one is nastier. The msgid has exactly one `%s`; the translation writes `%1$s` and `%2$s`. Which means that under a Chinese locale, this message goes off and reads an argument that was never passed.

---

## So I Went and Built Something

Somebody has to pick this up. I've made a start. I ran the whole PG 19 zh_CN catalog set end to end, and it lives here:

**[https://pgsql.cc/nls/](https://pgsql.cc/nls/)**

To be clear about what it is and what it isn't:

- **The first draft is machine translated.** I'll say so plainly in the mail to upstream; I'm not hiding it. But machine translation is only the draft. Every string gets a human pass before anything is submitted.
- **It ships with a full PostgreSQL glossary and a set of exception rules.** Every inconsistency above traces to the same root: nobody agreed on terminology. The same word is rendered 28 different ways across 28 catalogs, each translator going on feel. Pin the glossary down, and what's left is a writing problem.
- **Consistent across versions.** One msgid must translate to the same Chinese string from PG 10 through PG 20. That sounds like it should go without saying. It is the single most annoying engineering problem on the whole site.
- **You can browse by catalog, read msgid and msgstr side by side, and search.** See a bad string, send it straight to me.

Whatever comes out of this goes through PostgreSQL's normal process — the [pgsql-translators mailing list](https://www.postgresql.org/list-pgsql-translators/) — and lands upstream. No separate fiefdom.

---

One last thing.

This used to be a small problem. Not many people run a database under a Chinese locale to begin with, and if a message doesn't parse you switch back to English.

That's changed. These messages are corpus now. Every troubleshooting post the Chinese-language web turns up, every piece of PostgreSQL knowledge an LLM has picked up in Chinese, traces back to these strings and to secondhand retellings of them. One wrong 「内存溢出」 sitting here gets repeated across millions of conversations, by a path you have no way to trace.

Translation debt comes due. And right now it's compounding.

<!--
Data verification notes (all pulled fresh on 2026-09-15, reproducible):
- Per-language and per-catalog completion: babel.postgresql.org, 19 branch, Last update 2026-09-15T12:57:57Z
  Only the 17 languages with a substantially complete set of 28 catalogs are used for the horizontal
  comparison, to avoid languages with 1-3 catalogs inflating the ranking
- 66% is the arithmetic mean over the 28 catalogs; weighted by message count it is 62%
- 9 above the line: the zh_CN catalogs at >=80% are initdb 94, plpgsql 91, ecpg 93, plpython 96,
  pg_ctl 81, pg_config 95, plperl 93, ecpglib 96, pltcl 95
- File header: raw.githubusercontent.com/postgres/postgres/REL_19_STABLE/src/backend/po/zh_CN.po
- The 2660 / 1000 figures are derived: 6826x(1-61%)~=2662 untranslated; 5213 entries in the old file in
  the repo - ~4164 counted as translated by babel => ~1049 mismatched. Both are worded as "around"
- The four mistranslations: all confirmed by grep against the REL_19_STABLE branch, with the originals
  shown in the image for verification
- The four claims about pgsql.cc/nls in the body (machine-translated draft, glossary, cross-version
  consistency, page features) are written from what you described previously; check them against the
  current state of the site yourself before publishing
- Suggest adding a screenshot of pgsql.cc/nls at the top of the "So I Went and Built Something" section
-->
