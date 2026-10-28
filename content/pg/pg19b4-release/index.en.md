---
title: "PostgreSQL 19 Beta 4: Five Major Features Reverted"
date: 2026-09-25
authors: [vonng]
summary: >
  PostgreSQL 19 Beta 4 reverted five major features at once: SQL/PGQ property graph queries, online data checksums, temporal UPDATE and DELETE, partition merge and split, and DDL reconstruction functions. Features can wait another year; reliability cannot. Meanwhile, Simplified Chinese message translations landed upstream in Beta 4, and pgsql.cc completed a 28-year archive of Chinese PostgreSQL manuals.
tags: [PostgreSQL, PG Development, Commentary]
---
> [Original WeChat post (in Chinese)](https://mp.weixin.qq.com/s/qAt4LBJh1pWXprsK7bLSXg)

Today is the Mid-Autumn Festival, a holiday traditionally about reunion. Happy holidays to everyone celebrating.

The news for the occasion, though, is less about things coming together than getting pulled apart: [PostgreSQL 19 Beta 4](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/) came out yesterday.

Normally a new beta is good news, but this one stings a little.

I maintain the [Chinese PostgreSQL documentation](/en/pg/pgsql-cc-online/) across all versions on [pgsql.cc](https://pgsql.cc/). Every time a new beta drops, I run a diff against upstream and sync the changes into the translation. This time, the diff came back with 618 lines added and 5,021 lines deleted—more than eight times as much removed as added in a single beta update.

The reason is simple: **in its final beta cycle, PG 19 reverted five major features at once.**

## What Got Cut

![Five features reverted from PG 19 and their revert dates: partition merge and split (Aug 27), SQL/PGQ property graph queries (Sep 7), object DDL reconstruction functions (Sep 13), temporal UPDATE and DELETE (Sep 15), and online data checksum toggle (Sep 16)](cuts.webp)

Three smaller changes were also rolled back: two extensions to `CREATE SCHEMA`, and a change that forced `LC_COLLATE` to `C` in the `postmaster` process.

None of the five pulled features were minor trimmings. SQL/PGQ brings SQL:2023 property graph queries to PostgreSQL, letting you run graph queries directly over relational tables; it was supposed to be PG 19's headline feature. Toggling data checksums online is something DBAs have waited years for. Merging and splitting partitions is one of the first operational tasks teams ask about when migrating from Oracle—and this is the second time it has been pulled, having met the same fate right before the PG 17 release.

## Why They Were Reverted

Reading the diffs, commit logs, and mailing list threads together, all five features ran into the same underlying problem: **it is not enough for a new feature to work in isolation; it has to fit cleanly into the database's existing invariants.** Those invariants still have to hold when objects are altered, transactions run concurrently, and data undergoes recovery.

- **SQL/PGQ**: Creating a property graph requires a primary key on the underlying table. Yet once the graph existed, you could drop that primary key and the graph would remain behind. Robert Haas pointed out this case, which doesn't even need concurrency to trigger: a constraint checked at creation time was simply never enforced afterward. With several behaviors still lacking consensus on what the right semantics should even be, the Release Management Team (RMT) decided to revert the feature rather than take on permanent backward-compatibility baggage.

- **Temporal `UPDATE` and `DELETE`**: `FOR PORTION OF` lets you modify a slice of a validity period—for instance, repricing only Q3 of an annual contract. But when two concurrent sessions modified non-overlapping periods of the same contract, the second session returned `UPDATE 0` and silently failed to apply its change, even though the two updates did not logically conflict. By mid-September there was still no agreement on the right concurrency semantics, and Peter Eisentraut made the call to revert. Note that only this DML syntax was pulled; range types and temporal constraints remain intact.

- **Partition merge and split**: When a parent table and its partitions had different generated-column expressions, merging partitions altered the generated-column values of existing rows, and logical decoding emitted only inserts without the corresponding deletes. You thought you were only reorganizing how rows were stored, and the database silently changed the data itself—a complete non-starter.

- **DDL reconstruction functions**: Emitting a bare `CREATE ROLE` statement is easy; reconstructing a role completely is hard, because dependencies across roles, databases, and database-level settings all get pushed back onto the caller. In practice, this meant writing a second `pg_dump` inside the server, where every new object attribute added in the future would have to be maintained in two places.

- **Online data checksums**: After several rounds of fixes during the beta cycle, the community still wasn't confident in the implementation. The whole point of checksums is to tell you whether your data is corrupt; if the state of the checksum mechanism itself is in doubt, it defeats its own purpose. The offline `pg_checksums` tool remains available.

I support this round of reverts. **PostgreSQL's greatest asset has never been a long feature checklist; it is dependability.** Waiting one more major release for a feature is not a big deal. Shipping a feature with flawed semantics into a GA release means users will build applications, schemas, and operational workflows around it—and fixing it afterward costs far more than a one-year delay.

A revert is not a death sentence, either. Temporal primary keys (`WITHOUT OVERLAPS`) were reverted in PG 17 and came back in PG 18—just a year late to the reunion. Of course, the reverse is also true: being reverted from PG 19 does not guarantee a spot in PG 20, so don't put these features on your roadmap yet.

## What Remains in PG 19

Even with five major cuts, several features DBAs have been waiting for are still in:

- **`REPACK` and `REPACK CONCURRENTLY`** are both still there. Note that concurrent execution still acquires strong locks during certain phases—don't market it as "completely lock-free."
- **`WAIT FOR LSN`** is in, allowing applications to implement read-your-writes consistency on standby servers, provided they follow the documented rules around transactions and snapshots.
- **Importing remote statistics in `postgres_fdw`** is in, with the option renamed from `restore_stats` to `import_stats`.
- Also still in: sequence synchronization in logical replication, on-demand activation of logical decoding when `wal_level = replica`, query plan advice (`pg_plan_advice`), the autovacuum scoring mechanism, and SIMD optimizations for `COPY FROM`.

Beta 4 also ships a long list of fixes, including:

- Crashes in `REPACK`.
- Deadlocks in `WAIT FOR`.
- Initial table synchronization during logical replication from older versions to v19.
- Logical replication conflict detection.
- Crashes when accessing partitions whose concurrent detach operation has not finished.

According to the schedule, the Release Candidate (RC) is due in early October, with general availability targeted for October if all goes smoothly. One rule to keep in mind if you are planning around PG 19: **a feature appearing in a beta does not mean it will ship in GA—always go by the final [Release Notes](https://www.postgresql.org/docs/19/release-19.html).**

## Five Reverted, One Merged

Beta 4 wasn't all deletions. On September 23, the [Simplified Chinese (`zh_CN`) native language message translations](/en/pg/pg-nls/) I submitted were merged upstream and shipped with Beta 4.

If you install PostgreSQL 19 now with your system locale set to `zh_CN`, the error messages and notices you see come from that translation. Give it a try, and if any phrasing looks off or awkward, feel free to send feedback.

Only the PG 19 Simplified Chinese strings made it into Beta 4. Traditional Chinese (`zh_TW`) and backports for PG 14 through 18 are already prepared and should land in the official releases.

## Also: 28 Years of PostgreSQL Manuals on pgsql.cc

[pgsql.cc](https://pgsql.cc/) is a full Chinese translation of the official postgresql.org documentation. Previously, it hosted the complete Chinese manuals for PG 10 through 19 (plus `devel`). Alongside syncing the Beta 4 documentation changes, I also built an archive of translated manuals for the 24 end-of-life releases from PG 6.3 through 13, available both online and as PDFs.

PostgreSQL 6.3 came out in 1998. Across 30 major releases spanning 28 years—from 6.3 to 19—every PostgreSQL manual can now be read in Chinese on pgsql.cc.

Why translate unmaintained legacy releases? Because I have been building a PostgreSQL knowledge-graph project that maps the complete historical evolution of every configuration parameter, server message, system catalog, and built-in function, and that requires an accurate Chinese documentation baseline across every release. The project still needs one more verification pass before launch—stay tuned.

## Aside: What Became of My GLM Subscription

There was also a more practical reason for taking on all that translation: I needed a way to burn through my remaining GLM subscription. After the [ZCode repository upload incident](/en/ai/zcode-upload/), I stopped using it for any actual development work. Still, GLM 5.3 is a reasonably capable model, and letting paid quota go to waste felt like a shame—using it to translate, cross-check, and proofread public documentation was a natural fit.

I have seen reports that newer releases of ZCode are still uploading user data, which is shady. Still, as long as Zhipu doesn't mind the indigestion, there is plenty of PostgreSQL documentation for its servers to chew on.

In practice, ZCode and GLM did the heavy lifting while Codex acted as the final reviewer. I set up Codex as a supervisor on a dedicated machine driving ZCode around the clock—continuously reviewing and proofreading the Chinese PG manuals for a full week straight (my legacy v1 plan only had a 5-hour rolling cap, with no weekly limit). Every manual went through seven or eight passes until none of the agents could find anything left to nitpick.
