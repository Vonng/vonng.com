---
title: "Catalog Bullshit: Take the Database Apart, Then Rent a PostgreSQL Table Back to You"
date: 2026-08-28
authors: [vonng]
summary: >
  Snowflake blames the lakehouse's governance gaps on multiple engines and turns the Catalog into a new billing layer. But the core of an Iceberg Catalog is just a metadata-pointer CAS; the real governance gap comes from separating the control plane from the data path.
tags: [PostgreSQL, OLAP, Object Storage, Commentary]
---

## Starting with Snowflake's Governance Checklist

A few days ago, Snowflake shared a poster with blue type on a black background in [an official tweet](https://x.com/Snowflake/status/2093073608851542204). Titled **THE ARCHITECT'S GOVERNANCE CHECKLIST**, it listed nine problems:

- Revocation gaps
- Policy drift
- Silent corruption
- Classification blind spots
- The "who" problem
- End-to-end lineage
- Identity standardization
- Right to be forgotten
- Logical consistency

The accompanying copy had only three sentences:

> Multi-engine lakehouses don't just fail at the data layer.\
> They fail when governance and security cannot be enforced consistently across every engine.\
> Data interoperability ≠ governance interoperability.

The third sentence is true, and it is the starting point of this essay: open data formats do not make governance mechanisms interoperable across engines. Many of the problems Snowflake describes in its longer piece on [governance interoperability](https://www.snowflake.com/en/blog/engineering/lakehouse-data-governance-interoperability/) are real.

The problem is the commercial conclusion smuggled in alongside that technical observation: multiple engines inevitably create governance gaps, so you should avoid multiple engines and put everything into a single engine. In plain English: "The standard is incomplete, so don't use standards."

That leap deserves a closer look. Rather than stop at vendor sparring, let us dig beneath the Catalog: what problem does it actually solve, and why is it becoming a new control point just as its technical necessity begins to fade?

## The Catalog's Real Job: Hold a Pointer for Object Storage

Start with how Iceberg commits a write. Under the Iceberg specification's definition of [optimistic concurrency](https://iceberg.apache.org/spec/#optimistic-concurrency), an update follows roughly four steps:

1. Write new Parquet data files.
2. Write a new manifest.
3. Write a new `metadata.json`.
4. Have the Catalog switch the table's current pointer from the old `metadata.json` to the new one.

The Catalog updates the pointer only if its current value still matches the old value the engine expects. That pointer swap is the transaction commit: readers before it see the old snapshot; readers after it see the new one. There is no third state in between.

In SQL, it is simply a single-row compare-and-swap:

```sql
UPDATE tables SET ptr = $new WHERE name = $t AND ptr = $old;
```

That atomic pointer swap is the Catalog's only irreplaceable responsibility. Everything else is built on top of it. This makes the question concrete: does one single-row CAS really require a distributed service that must be deployed, authorized, patched, and billed separately?

Now look at how the Catalogs themselves persist metadata:

- [Hive Metastore](https://hive.apache.org/docs/latest/admin/adminmanual-metastore-3-0-administration/) typically stores its state in a relational database such as MySQL and exposes it through Thrift.
- [Project Nessie](https://projectnessie.org/) can use JDBC/PostgreSQL and other backends.
- [Apache Polaris](https://polaris.apache.org/) provides a JDBC persistence path.
- [Lakekeeper](https://docs.lakekeeper.io/) is written in Rust and licensed under Apache 2.0, while its [configuration documentation](https://docs.lakekeeper.io/docs/nightly/configuration/#persistence-store) states that PostgreSQL 15 or later is currently its only supported persistence backend.

So while "the entire Catalog industry is a PostgreSQL table in a REST shell" is a caustic summary, it is not far from the truth. More interestingly, Snowflake has begun charging for this wrapper per REST request. From the user's perspective, the bill does look rather like rent on the table's `UPDATE`.

## As the Technical Need Recedes, the Tollbooth Arrives

A standalone Catalog once had strong technical reasons to exist. Early S3 had neither atomic rename nor a safe compare-and-swap. Object storage could not express "write the new value only if the old value still equals X," so the commit point had to be delegated to an external coordinator capable of a truly linearizable CAS.

Hive Metastore, Glue, Nessie, Polaris, Unity, Horizon, and Gravitino arrived in succession. The names changed; the core job did not: hold the current pointer on behalf of object storage. Delta took another route, atomically creating numbered log files directly on storage. But early S3 did not support `create-if-not-exists`, so Delta needed DynamoDB to supply that primitive.

The turning point came in 2024, when [S3 added conditional writes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html). Object storage could finally express both `create-if-absent` and ETag-based conditional updates directly. Once the commit primitive moved back into the storage layer, some workloads no longer needed a separate coordinator.

That creates a revealing timeline: **the technical need for a standalone Catalog is declining at exactly the moment it is being turned into a new control point and billing layer.**

Snowflake launched Polaris in 2024 and donated it to Apache. In April 2026, it looked back on that work under the title "[Apache Polaris and the End of Data Vendor Lock-In](https://www.snowflake.com/en/engineering-blog/apache-polaris-iceberg-rest-catalog/)," emphasizing that its Iceberg REST Catalog had no proprietary extensions, no hobbled features, and no fine print.

At the same time, [Snowflake Open Catalog has stopped accepting new registrations](https://docs.snowflake.com/en/user-guide/opencatalog/overview), directing new customers to Horizon Catalog, while the [Horizon Iceberg REST Catalog API](https://docs.snowflake.com/en/user-guide/tables-iceberg-access-using-external-query-engine-snowflake-horizon) is scheduled to begin charging 0.5 credits per million calls in the second half of 2026.

Put those facts together and the logic is clear. Once the format is open, the Catalog becomes the new gateway. Once the Catalog is open, governance becomes the gateway one layer above. **Governance is the wedge.** The poster at the beginning is the shortest possible manual for this commercial strategy.

## The Control Plane Is Not in the Data Path

That explains why the Catalog is becoming a business. Now we can get to why governance is hard.

Database permissions can form an enforceable boundary because the engine is the only gateway to the bytes. Reading a row requires passing through the same door, with the ACL mounted on it; every door is set into the same wall.

The lakehouse tore down that wall. The bytes sit in S3, and anyone with bucket credentials can read the objects directly. The Catalog can perform credential vending: identify the caller, then issue a time-limited STS token scoped to a particular prefix. But once the credential is issued, the Catalog drops out of the data path. It can no longer observe which rows or columns the engine actually reads.

### Row and Column Policies Depend on Engines Behaving Correctly

Object-storage tokens are scoped to objects and prefixes, while Parquet rows and columns live inside files. If a token permits access to a file, its holder can retrieve every row and column in that file. The Catalog layer therefore cannot directly enforce row-level security or column masking. It can only require every engine to apply the policy correctly during its scan.

This arrangement can work, but its boundary must be stated honestly: it is not a security boundary enforced by the storage layer. It is a protocol that depends on engine compliance.

### Revocation Has to Wait for Token Expiry

The same limitation explains the "revocation gap." Suppose the Catalog issues a token valid for one hour and an administrator then runs `REVOKE` in the control plane. The token already issued remains usable until it expires naturally.

Revocation in this architecture is therefore inherently asynchronous and eventually consistent. Reducing four engines to one does not close the window. As long as S3 remains the data plane and external tables read objects directly through short-lived credentials, the gap remains.

### Multiple Engines Take the Blame for the Real Problem

Revocation gaps, policy drift, the "who" problem, and logical consistency are first and foremost consequences of keeping the control plane out of the data path, not consequences of the number of engines. This is where Snowflake reverses cause and effect: it packages a structural constraint of the split architecture as a flaw unique to multiple engines, then offers a single engine as the cure.

[Lakekeeper's product documentation](https://docs.lakekeeper.io/) is more candid on this point. A Catalog that merely describes data cannot stop anything, so Lakekeeper places identity resolution, policy evaluation, short-lived credential issuance, and audit logging in the metadata request path. That can improve the control plane, but it cannot change one fact: the Catalog sits in the metadata request path, not the data path.

### The Right to Be Forgotten Is a Background Processing Chain

The "right to be forgotten" also needs to be understood against the actual data lifecycle. Under the Iceberg specification for [row-level deletes](https://iceberg.apache.org/spec/#row-level-deletes), v2 uses position deletes or equality deletes, while v3 introduces deletion vectors. These mechanisms first ensure that queries no longer return the target row; they do not immediately erase its bytes from the original Parquet file.

Physical deletion must still wait for a data rewrite, snapshot expiration, and orphan-file cleanup all to finish. In other words, GDPR deletion in a lakehouse is not one `DELETE` statement. It is an asynchronous background processing chain.

Snowflake's own micro-partitions are likewise immutable; deleted data may remain during the retention windows for [Time Travel and Fail-safe](https://docs.snowflake.com/en/user-guide/data-time-travel). There is nothing wrong with putting a constraint common to immutable storage on a governance checklist. The problem is implying that switching vendors makes it disappear.

**A database puts every door in the same wall. The lakehouse tears down the wall, then sells you a checklist for inspecting the doors.**

## Twenty Years of Reinventing the Database

Zoom out, and the past twenty years look like a long-running series called *Reinventing the Database*:

- In 2004, Google published the [MapReduce paper](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/).
- In early 2008, DeWitt and Stonebraker wrote "[MapReduce: A Major Step Backwards](https://dsf.berkeley.edu/cs286/papers/backwards-vertica2008.pdf)," criticizing its lack of schemas, indexes, and transactions. At the time, they were dismissed as hidebound dinosaurs.
- Around 2010, Hive brought SQL back.
- At roughly the same time, Hive Metastore brought the system catalog back, still backed by a relational database.
- From 2017 onward, Delta, Iceberg, and Hudi brought ACID back.
- Later, the [Puffin file](https://iceberg.apache.org/puffin-spec/) brought statistics files back.
- From 2024 onward, Polaris, Unity, Gravitino, and Horizon turned the Catalog into a service.
- In 2026, the industry began adding `GRANT`, `REVOKE`, row-level security, column masking, auditing, and lineage back in to address the nine problems on the poster.

Twenty years and tens of billions of dollars later, the industry has reimplemented System R on object storage. A database integrates these capabilities into one atomic, consistent whole, validated over forty years and packaged in a single process. After `initdb`, transactions, permissions, the catalog, and statistics are all there.

The lakehouse breaks the whole into more than a dozen components. A company stands behind each one, and each must be bought, licensed, patched, and operated separately. Pavlo and Stonebraker's 2024 paper, "[What Goes Around Comes Around... And Around](https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf)," examines exactly this cycle: after a decade of NoSQL churn, the industry returned to the relational model and SQL. The lakehouse is the same story on a new stage.

Even the script is similar. It used to be "we don't need schemas." Now it is "we don't need databases."

## The Catalog Should Have Been a Table All Along

Once you accept that the Catalog should be a database table, the design direction becomes straightforward: put the Catalog and its metadata back into a SQL database instead of continuing to scatter metadata across object storage as files.

[DuckLake v1.0](https://duckdb.org/2026/04/13/ducklake-10) takes exactly this route. The data remains Parquet, in the user's own bucket, in an open format. Only the metadata's home changes. Released in April 2026, v1.0 announced production readiness and committed to backward compatibility. Its metadata model consists of 28 tables, and it is licensed under MIT.

That decision enables two things Iceberg struggles to provide.

### Small Changes Do Not Have to Become Parquet Immediately

DuckLake supports [data inlining](https://ducklake.select/docs/stable/duckdb/advanced_features/data_inlining): inserts and deletes below a threshold do not immediately write Parquet. They first enter inline tables in the Catalog database, then flush into normal-sized files once enough changes accumulate. The default threshold in v1.0 is 10 rows.

[MotherDuck's architectural analysis](https://motherduck.com/blog/ducklake-architecture-deep-dive/) compares this with conventional lakehouses, where each small transaction creates three or four files across formats such as JSON, Avro, and Parquet. As the files accumulate, reads and compaction become more expensive, often constraining practical commit throughput to around one transaction per second. With inlining, DuckLake can sustain about 100 transactions per second.

Those are vendor numbers and should be discounted accordingly, but the direction is clear. Only when metadata lives in a real database can the system inline small changes there. If metadata is itself a pile of files, compaction will always be chasing the writes.

### Cross-Table Transactions Become a Built-In Capability

Table formats such as Iceberg can generally guarantee atomic commits only within a single table. DuckLake can use the underlying database transaction directly, letting multiple related tables share one `BEGIN` and one `COMMIT`. File-based metadata lacks a shared commit point, making this hard to express naturally. Put the metadata in a database and the capability comes almost for free.

Snowflake's open-source [`pg_lake`](https://pgext.cloud/ext/pg_lake) follows the same route. It introduces a new Iceberg table type and lets PostgreSQL itself serve as the Catalog. Snowflake's [official introduction](https://www.snowflake.com/en/blog/engineering/pg-lake-postgres-lakehouse-integration/) says so plainly: Postgres manages Iceberg tables directly instead of placing the Catalog in yet another system.

This is not some fringe heresy. Follow transaction consistency and metadata management far enough, and many implementations eventually arrive here.

### Four Rungs Cover 99% of Use Cases

From this perspective, the roadmap is short:

1. Use PostgreSQL directly.
2. Use DuckDB for single-node analytics.
3. Add object storage to DuckDB.
4. Use DuckDB with object storage and PostgreSQL metadata.

These four rungs cover 99% of use cases. The remaining 1% genuinely needs elastic distributed scans: 100 TB or more, 200 ephemeral workers running for five minutes and then disappearing so the bill drops to zero. That is Spark and Trino territory.

The problem was never that the 1% exists. The problem is that an architecture designed for the 1% was sold to 100% of users.

## DuckDB Dressed as PostgreSQL

We still need to face PostgreSQL's real weakness. Its executor uses a tuple-at-a-time Volcano model, with neither vectorized execution nor native columnar storage. It is no surprise that analytical scans run one or two orders of magnitude slower than in DuckDB or ClickHouse. Conventional extensions cannot fix that weakness, because an extension cannot replace the entire executor.

But today's extensions that "make PostgreSQL analytical" all solve the problem in similar ways:

- [`pg_lake`](https://pgext.cloud/ext/pg_lake) leaves planning and transactions to PostgreSQL, while a separate `pgduck_server` process runs DuckDB and communicates over the PostgreSQL wire protocol.
- [`pg_duckdb`](https://pgext.cloud/ext/pg_duckdb) embeds DuckDB's vectorized executor directly into PostgreSQL.
- [`pg_mooncake`](https://pgext.cloud/ext/pg_mooncake) follows the same route.

So "PostgreSQL will eat the data warehouse" needs a new subject:

**The thing actually eating the data warehouse is DuckDB in PostgreSQL clothing.**

That is not an insult. It is the architecture's real shape: the missing execution engine already exists; the only question is which system becomes the shell. CWI established the case for vectorized execution in its 2005 [MonetDB/X100 paper](https://ir.cwi.nl/pub/16497), and DuckDB came from the same lab. PostgreSQL did not absorb that work over the next twenty years, not because nobody knew about it, but because its executor is extremely hard to change and the community is not going to rewrite the entire kernel for OLAP.

Meanwhile, hardware continues to improve. A single machine with two 100 GbE links and a set of NVMe drives can already reach scan bandwidth in the tens of gigabytes per second. Most of what companies call "big data" fits on one machine and often runs faster there than on an eight-node cluster. Hardware advances every year while most companies' actual data volumes do not grow at the same pace, so this argument will only get stronger.

## Open One Layer, Move the Tollbooth Up One Layer

Put the relevant companies' moves side by side, and the picture becomes clearer:

- [`pg_lake`](https://pgext.cloud/ext/pg_lake) and [`pg_parquet`](https://pgext.cloud/ext/pg_parquet) both came from Crunchy Data. Snowflake completed its acquisition in June 2025, disclosed to the SEC that the [cash consideration was $164.5 million](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000187/snow-20250731.htm), and open-sourced `pg_lake` that November.
- The team behind [`pg_mooncake`](https://pgext.cloud/ext/pg_mooncake), Mooncake Labs, [was acquired by Databricks](https://www.linkedin.com/posts/databricks_were-excited-to-announce-that-databricks-activity-7379138538652696576-2pbr) in October 2025. Databricks had already [acquired Neon](https://neon.com/blog/neon-and-databricks) in May, in a [deal valued at about $1 billion](https://techcrunch.com/2025/05/14/databricks-to-buy-open-source-database-startup-neon-for-1b/). Both teams now work on Lakebase.
- [`pg_duckdb`](https://pgext.cloud/ext/pg_duckdb) is a collaboration among DuckDB Labs, Hydra, and MotherDuck.
- DuckLabs, the organization behind DuckDB and DuckLake, has [signed an acquisition agreement with AWS](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/).
- [Azure HorizonDB](https://azure.microsoft.com/en-us/blog/from-legacy-to-leadership-how-postgresql-on-azure-powers-enterprise-agility-and-innovation/) is Microsoft's in-house PostgreSQL-compatible engine, advertised to scale to 3,072 vCores and 128 TB.

Each rung of the four-level stack is backed by the very companies this architecture was meant to route around. They did not simply buy the projects to kill them. The more sophisticated strategy is to buy the road itself.

`pg_lake` is genuinely open source under Apache 2.0, and its code is excellent. There is no contradiction in Snowflake paying $164.5 million for the team and then releasing the core capability for free. It is not afraid that PostgreSQL will eat the data warehouse; it is afraid that PostgreSQL will do so without passing through Snowflake.

So `pg_lake` gives users exactly what they want: PostgreSQL manages Iceberg tables directly and serves as its own Catalog. At the same time, it cements Iceberg as the default format on disk. The easier the tool is to use, the stronger the Iceberg ecosystem becomes, while the governance gateway can remain one layer above.

The commercial strategy most worth studying in recent years is this upward migration of the tollbooth:

**If you cannot stop openness, fund it; then make sure the open layer is not the layer where you collect rent.**

Once the format is open, sell the Catalog. Once the Catalog is open, sell governance. If governance opens too, find another layer above it. Every time one layer opens, the tollbooth moves up. And every time it moves, the vendor tells you that the higher layer is too dangerous to manage yourself.

## Use the Checklist on the People Who Published It

Return to the original nine questions. The poster is worth saving because every item points to a real risk. But the checklist should not be used only against competitors. It should also be used on the people who published it:

- **Revocation gaps**—are external tables accessed through credential vending? After a token has been issued, when does `REVOKE` actually take effect?
- **Right to be forgotten**—during the Time Travel and Fail-safe retention windows, does the row the customer asked you to delete still exist?
- **Identity standardization**—in the 2024 attacks targeting Snowflake customer instances, Mandiant and Snowflake notified [roughly 165 potentially affected organizations](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion). That same year, AT&T disclosed that attackers had copied [records of calls and text-message interactions for nearly all of its wireless customers](https://www.sec.gov/Archives/edgar/data/732717/000073271724000046/t-20240506.htm) from a third-party cloud platform. Where was organization-wide mandatory MFA when those incidents occurred?

These nine items are not diseases unique to multi-engine systems. They are the governance costs you inevitably face after taking a database apart. Nor is the solution simply to reduce the number of engines from four to one. It is to put each separately sold capability back where it belongs:

**Put metadata back in the database. Put permissions back at the single gateway. Leave the remaining bytes in cheap object storage, in an open format anyone can read.**

This is not a new idea. It is a database.

We have spent twenty years and tens of billions of dollars going in a circle, and now we are picking the pieces back up one by one.

Even as we do, we still have to rent a PostgreSQL table from someone.
