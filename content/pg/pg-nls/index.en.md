---
title: "PostgreSQL's Chinese Error Messages Were Seven Years Stale. Not Anymore."
date: 2026-09-19
authors: [vonng]
summary: >
  Never set your PostgreSQL locale to zh_CN — that old rule expires with PostgreSQL 19. The Chinese message catalogs went seven years untouched and nearly got dropped from the release. A bone nobody could chew through in seven years, finished in seven days.
tags: [PostgreSQL, Translation]
---

If you have run PostgreSQL in China for any length of time, you know the unwritten rule: when you install the database, do not set the localization `locale` to `zh_CN` (Simplified Chinese). Use `en_US` and be done with it.

The rule is not superstition. It is scar tissue, accumulated by a generation of DBAs. But read what it actually says: to get a database that talks to you properly, a Chinese user has to start by turning off their own language.

As of PostgreSQL 19, the rule is void.

I rewrote PostgreSQL's Simplified Chinese localization from scratch. Six major versions, PG 14 through 19. 28 message catalogs. 67,487 strings. 100% coverage. Peter Eisentraut merged it into the upstream translation repository on September 18, and it ships with PostgreSQL 19.


--------

## Chinese Almost Got Dropped Entirely

PostgreSQL has real localization. Every English string the server emits has an official gettext message catalog behind it, and the machinery is called [NLS](https://www.postgresql.org/docs/current/nls.html).

Supporting the mechanism is not the same thing as any particular language being usable.

On July 24 this year, Thom Brown posted to the pgsql-translators list: six languages, in their current state, were not going to make it into PG 19. Czech, Greek, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese.

Here is why. PostgreSQL has a hard rule: a language ships in a release only if its message catalogs clear 80% coverage. Below that line, nothing gets packaged. [babel.postgresql.org](https://babel.postgresql.org/) keeps the status table, and it is not subtle.

Simplified Chinese: 66%. Traditional Chinese: 70%. Both under the line.

![Message catalog completion by language for PostgreSQL 19, with Simplified Chinese at 66%](languages.png)

Take the horizontal cut first. German, Swedish, Ukrainian and Georgian at 99%, Japanese 98%, Russian 91%, Korean 89%. Georgia has 3.7 million people, barely more than a single district of Shanghai, and it has all 28 catalogs at 99%.

The vertical cut is uglier. Of the 28 Simplified Chinese catalogs, 9 clear the line, and the more load-bearing the catalog, the worse it looks.

The server's own `postgres` catalog, 6,826 strings, more than half of all message text in the tree and the origin of nearly every ERROR you will ever read: 61%. `libpq`, which every driver in every language sits on top of, 408 strings: 12%.

![Simplified Chinese across all 28 catalogs: only 9 clear the 80% packaging threshold, and the main postgres catalog sits at 61%](catalogs.png)

66% does not mean "the Chinese is a bit rough." When gettext cannot find a translation it falls back to the English source, so what you actually get is an error whose first half is Chinese and second half is English. One tool speaking Chinese and the next speaking English inside the same upgrade. The same concept under two different words in two different places.

The problem is not that the Chinese is bad. The problem is that it is half there, and for any serious environment that is worse than plain English. Which is exactly why the old hands tell you to turn localization off.


--------

## Seven Years, Nobody

Open the file header and you can see how it happened.

This is [the file on REL_19_STABLE](https://github.com/postgres/postgres/blob/REL_19_STABLE/src/backend/po/zh_CN.po) as of today, and master carries an identical copy. From PG 12 to PG 19, seven years and three months, eight major releases, and not one byte of that header has changed.

PG 12 fell off the support calendar two years ago. Seven full years, and nobody.

![The header of src/backend/po/zh_CN.po, frozen since 2019 and untouched for seven years and three months](crime-scene.png)

A few of the client catalogs got sporadic repairs. A round of psql and libpq in 2021, pg_ctl in 2023, initdb in 2024. The biggest one just lay there.

Everything written into PostgreSQL over those seven years, logical replication and JIT and parallel query and async I/O, has an empty Chinese column. On the server side roughly 2,660 strings have never had a Chinese translation at all. And of the 5,213 that were translated back then, about 1,000 no longer match today's msgid because the source moved out from under them. They are still sitting in the file, and they will never be matched again.


--------

## The Museum of Mistranslations

Worse than untranslated is mistranslated.

![A gallery of mistranslations from the Simplified Chinese catalogs](museum.webp)

`Report bugs to` comes out as 「臭虫报告至」, literally *report the bedbugs to*. 臭虫 is the insect; the "defect" sense of bug never made it across. Fourteen catalogs say it that way. It is a 2001 rendering from the first translator, and it has lived straight through to 2026.

`out of memory` has four Chinese renderings in today's tree: 内存用尽, 内存不足, 内存耗尽, and **内存溢出**. The first three are fine. The fourth says *memory overflow*, and it is wrong. OOM is asking for memory and not getting it, a clean failure. An overflow is a write past the end of a buffer that corrupts whatever sits next to it. In the middle of an incident those two point in opposite directions: one sends you to add RAM, check connection counts and tune `work_mem`, the other sends you to read code. The error is contagion from Java, where `OutOfMemoryError` and `StackOverflowError` get taught side by side until they collapse into a single Chinese word.

Two more are outright bugs.

In `pg_ctl`, `invalid binary "%s": %m` loses the `%m` entirely in Chinese. When it fires you learn which file is wrong and never learn what errno said, and most of that message's value was in the `%m`.

The `ecpg` one is nastier. The msgid has exactly one `%s`; the translation writes `%1$s` and `%2$s`. Under a Chinese locale, that string goes off to read a second argument that was never passed.

So the old-timers' rule was earned. And more people walk into this than you would guess: install PostgreSQL on a macOS or Linux desktop running a Chinese UI and the locale follows the system, which means Chinese. Unless you have deliberately set it otherwise, it is easy to end up there.


--------

## Fine, I'll Do It

Why did I pick this up?

A while back I translated the whole PostgreSQL documentation set into Chinese, 18 major versions from 9.0 to 20, and put it at [pgsql.cc](https://pgsql.cc), maintaining a PostgreSQL knowledge graph alongside it. One thing the graph tracks is error messages and where they come from in the source. Working through that, the state of the Chinese became impossible to unsee.

![The SQLSTATE catalog on pgsql.cc: 263 status codes across 44 classes, covering PostgreSQL 7.4 through 20](status.webp)

Having come that far, I might as well finish the job.

On September 11 I [wrote to pgsql-translators](https://www.postgresql.org/message-id/CA1188D8-97A4-4F09-9E7F-42207C43BC34@vonng.com) volunteering to take over the Simplified Chinese catalogs.

I laid the method out plainly in that mail. The draft is machine translated, using the glossary from pgsql.cc. It is working material and not what I submit: every string gets a human pass against the English source and the existing translation, and only reviewed output with a clean `msgfmt` goes to the list. I offered two options, a full redo or filling the gaps and fixing the obvious errors, and said I preferred the first. Most of the inconsistencies are cross-file, and one pass against a fixed glossary solves what a pile of small patches cannot.

Nobody on the list objected. So, go.

September 13: a first batch, all 28 catalogs for PG 19, 12,702 strings, with an issue opened on Redmine.

September 17: every catalog on six branches, PG 14 through 19. 162 files, 67,487 strings, 100% translated, zero fuzzy, zero empty, `msgfmt --check --check-format` green across the board.

September 18: Peter Eisentraut merged them into PostgreSQL 19's translation repository.

![The pgtranslation Redmine activity feed: the zh_CN submissions for PG 14 through 19, and Peter Eisentraut marking the PG 19 issue committed on September 18](redmine.webp)

Seven years untouched. Seven days start to finish.

It burned eight 20x subscriptions.

![babel.postgresql.org after the merge, with Simplified Chinese at the top of the table](babel-now.webp)

PG 19 is not frozen yet and upstream strings are still moving. The `postgres` catalog shifted a few in the last couple of days and coverage slipped from 100% to 99%. So I also maintain [pgsty/pgnls](https://github.com/pgsty/pgnls), which tracks upstream changes with a release a day, and I will submit a final 100% pass after the freeze.

Traditional Chinese got the same treatment and is essentially done. When PG 19 ships, both zh_CN and zh_TW will be at 100%.

![The pgsty/pgnls repository, tracking upstream message changes with daily releases](pgnls-repo.webp)


--------

## How the Seven Days Went

No point being coy about it: the heavy lifting was done by Fable 5.1, Cloud Fable 5.1 and Codex Astra 6.

AI has made translation work far cheaper than it used to be. But this was not a matter of saying "please translate all of this into Chinese." Conservatively I put dozens of hours into it, including writing a workbench of my own purely to make side-by-side human review bearable:

https://pgsql.cc/nls

![The pgsql.cc/nls review workbench, showing msgid and msgstr side by side](pgsqlccnls.webp)

The hard part of translation was never moving a sentence from one language into another. The hard part is consistency. 67,487 strings, across 28 components, across six major versions: the same English has to be the same Chinese, and similar English has to be similar Chinese. A human doing that by hand burns out. A model doing it drifts. So the work is not in the translating, it is in nailing the rules down first.

The first pass is a full throwaway translation whose purpose is not the output but the terms. Several models then propose renderings for those terms independently, I cross-compare them and assemble a starting glossary, and I vet it entry by entry. Anything uncertain gets argued out, down to the modals: cannot, shall not and must not each get exactly one Chinese form, no improvising at the keyboard. With the glossary frozen, write the style guide and the conventions, stuffed with positive and negative examples. Translate against that. Then run the consistency checks, once across components and once across versions, and send every mismatch back through.

A glossary is the soul of professional translation. Translating *Designing Data-Intensive Applications* (both editions), *PostgreSQL Internals*, and 18 major versions of the PostgreSQL docs is what produced it. In professional translation, once the glossary is settled, most of the ceiling on quality is settled with it.

AI genuinely cut the cost of this work by an order of magnitude. A bone nobody could chew through for seven years now takes seven days. But run that backwards: precisely because it only takes seven days, seven years of nobody doing it is that much harder to excuse.


--------

## What Exactly Did the "Domestic" Databases Produce?

The first thing I wondered before starting was whether somebody had already done this. There is no shortage of Chinese databases built on PostgreSQL, and localizing into Chinese is supposedly the whole selling point. Was there something lying around I could just pick up?

I went and looked. A whole pile of these databases ship a `zh_CN.po` identical to upstream's, down to the byte. Grep for 臭虫 or 内存溢出 and you hit every time.

![Chinese PostgreSQL-derived databases shipping the upstream zh_CN catalogs unchanged](downstream.webp)

That one is hard to let pass. What are the two most basic things a Chinese database is expected to ship? Chinese documentation and Chinese localization. Turning PostgreSQL's English errors into decent Chinese, so that Chinese users can understand what their own database is telling them, is the floor. Somebody should at least clear the floor.

The upstream Chinese translation has names in its file headers. He Weiping in 2001. Zhang Jie of Fujitsu from 2019 to 2023. Wang Dianjin of Cloudberry.

Not one of the vendors that makes its living off PostgreSQL is among them. In the end it fell to me, a one-man shop, to get it done.

There really are things state subsidies cannot buy, and caring about the work can.


--------

## Finally

Open source has no one handing out assignments, only people claiming them. The seat sat empty for seven years. Anyone could have taken it. Nobody did. Georgia, 3.7 million people, 28 catalogs at 99%: not because they are better at this, but because somebody over there put a hand up.

And now there is a clock on it.

Those mistranslations do not sit quietly in a `.po` file. They propagate into every PostgreSQL fork, into blog posts and Q&A threads and support tickets, out onto the open web, into training corpora, into models, and back out again as the standard answer, repeated by people who never saw the original. 内存溢出 started as four characters somebody typed years ago without thinking hard about it. Give it a few more years and it could be what the entire Chinese-speaking technical world believes OOM means, and fixing it at that point is no longer a matter of editing one file. Cleaning the source while you still can is cheaper than plugging ten thousand holes downstream.

「臭虫报告至」 lasted twenty-five years. It does not survive PostgreSQL 19.

So next month, when you install PostgreSQL 19, try setting the locale to `zh_CN`. This time it actually works.
