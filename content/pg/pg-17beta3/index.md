---
title: "PostgreSQL小版本更新，17beta3，12将EOL"
date: 2024-08-09
authors: [vonng]
summary: >
  PostgreSQL全球开发组发布了例行小版本更新，包括16.4、15.8、14.13、13.16， 12.20 以及 17 beta3，此外，PG 12 即将 EOL。
tags: [PostgreSQL, PG管理]
---

## PostgreSQL全球开发组发布了所有受支持PG大版本的更新，包括16.4、15.8、14.13、13.16 和 12.20 版本，以及PostgreSQL 17 的第三个 beta 测试版。此次发布修复了1个安全漏洞和过去几个月报告的 55 个 BUG。

## 欲了解更多变更详情，请查阅发布说明<sup>[1]</sup>。

------------------------------------------------------------------------

## PostgreSQL 12 终止支持通知

PostgreSQL 12将于2024年11月14日停止发布修复补丁。如果您在生产环境中运行PostgreSQL 12，我们建议您计划升级到更新的、受支持的 PostgreSQL 大版本。更多信息请参阅我们的版本政策<sup>[2]</sup>。

------------------------------------------------------------------------

## 安全问题

### CVE-2024-7348<sup>[3]</sup>：在 pg_dump 期间替换PostgreSQL关系执行任意SQL

CVSS v3.1基础分值：8.8<sup>[4]</sup>

受影响的大版本范围：12 - 16。

能够创建和删除非临时对象的攻击者，在超级用户并发执行的 `pg_dump` 过程中有可能注入 SQL 代码，并由超级用执行。攻击涉及用视图或外部表替换序列或类似对象，这些对象将执行恶意代码。为防止此类攻击，引入了一个新的服务器参数 `restrict_nonsystem_relation_kind`，可以禁用非内置视图的展开以及访问外部表，并教授pg_dump在可用时设置它。请注意，只有当 pg_dump 和导出数据的 Server 版本都足够新，才能阻止此攻击。

PostgreSQL 项目感谢 Noah Misch 报告此问题。

------------------------------------------------------------------------

## 错误修复和改进

此更新修复了过去几个月报告的55多个错误。以下列出的问题影响PostgreSQL 16。这些问题中的一些也可能影响其他受支持的PostgreSQL版本。

•修复了“合并右反连接”计划的错误结果，其中如果内部关系被知道具有唯一的连接键，当外部关系中存在重复的连接键时，合并可能会表现异常。•防止在`VACUUM`<sup>[5]</sup>中无限循环。•在`ALTER TABLE DETACH ... PARTITION CONCURRENTLY`<sup>[6]</sup>期间修复分区修剪设置。•修复在`CALL`<sup>[7]</sup>语句中用作参数的稳定函数的行为。•当在备用服务器上或在其他会话的临时序列上调用时，`pg_sequence_last_value()`现在返回`NULL`，而不是抛出错误。•修正`websearch_to_tsquery()`中忽略的操作符的解析。•在`INSERT ... DEFAULT`<sup>[8]</sup>中正确检查视图列的可更新性。•在`ALTER TABLE ... SET LOGGED|UNLOGGED`<sup>[9]</sup>期间锁定所拥有的序列。•如果排队的`AFTER`触发器不再存在，则不抛出错误。•当所需索引具有表达式或谓词时，例如通过可更新视图，修正`INSERT ... ON CONFLICT`<sup>[10]</sup>选择仲裁索引的问题。•拒绝修改另一个会话的临时表`ALTER TABLE`<sup>[11]</sup>。•修正在`CREATE TABLE ... LIKE STATISTICS`<sup>[12]</sup>中对表达式的扩展统计信息的处理。•修正无法重新计算从`MIN()`或`MAX()`聚合生成的子查询的问题。•禁止在位置参数中使用下划线。•避免在JIT内联的后端函数抛出错误时崩溃。•修正启动热备服务器时准备事务的子事务的处理。•防止逻辑复制槽的错误初始化。•修正逻辑复制WAL发送器在发布对行类型与表物理不同的分区表的更改时的内存泄漏。•禁止OpenSSL创建有状态的TLS会话票证。•修正PL/pgSQL<sup>[13]</sup>处理包含下划线的整数范围（例如，`FOR i IN 1_001..1_002`）的方式。•修正PL/Perl<sup>[14]</sup>与Perl 5.40之间的不兼容。•修正与递归PL/Python<sup>[15]</sup>函数和触发器相关的几个问题。•确保`pg_restore -l`<sup>[16]</sup>正确报告目录项的依赖关系。•`pg_stat_statements`<sup>[17]</sup>现在为出现在SQL语言函数中的非`SELECT`/`INSERT`/`UPDATE`（实用）语句传递查询ID。•修正`postgres_fdw`<sup>[18]</sup>在将外部表映射到复杂远程视图时的问题。•`postgres_fdw`<sup>[19]</sup>不再向远程服务器发送`FETCH FIRST WITH TIES`子句

------------------------------------------------------------------------

更新

所有PostgreSQL更新版本都是累积的。与其他小版本一样，用户无需转储和重新加载数据库或使用`pg_upgrade`来应用此更新版本；您可以简单地关闭PostgreSQL并更新其二进制文件。

跳过一个或多个更新版本的用户可能需要执行额外的更新后步骤；请查阅早期版本的发布说明了解详细信息。

更多详情，请查阅发布说明<sup>[20]</sup>。

------------------------------------------------------------------------

## 关于PostgreSQL 17测试版的说明

此版本标志着PostgreSQL 17的第三个测试版本，并使社区更接近预计在第三季度末的正式发布。

本着开源PostgreSQL社区的精神，我们强烈鼓励您在您的系统上测试PostgreSQL 17的新功能，以帮助我们消除可能存在的错误或其他问题。虽然我们不建议您在生产环境中运行PostgreSQL 17 Beta 3，但我们鼓励您找到方法在此测试版上运行您的典型应用工作负载。

您的测试和反馈将帮助社区确保PostgreSQL 17版本符合我们交付世界上最先进的开源关系数据库的稳定、可靠版本的标准。请阅读有关我们的测试版测试过程<sup>[21]</sup>的更多信息以及您如何贡献：

https://www.postgresql.org/developer/beta/

------------------------------------------------------------------------

## 升级到PostgreSQL 17 Beta 3

要从PostgreSQL的早期版本升级到PostgreSQL 17 Beta 3，您将需要使用类似于在PostgreSQL的主要版本之间升级的策略（例如`pg_upgrade`或`pg_dump` / `pg_restore`）。有关更多信息，请访问升级<sup>[22]</sup>文档部分。

------------------------------------------------------------------------

## 自Beta 2以来的更改

PostgreSQL 17 Beta 3的修复和变更包括：

•将`standby_slot_names`参数重命名为`synchronized_standby_slots`。•几项SQL/JSON修复。•修复`pg_combinebackup --clone`。•修复`pg_createsubscriber`以适用于包含空格的数据库名称。•`pg_createsubscriber`现在在目标数据库上运行时删除预先存在的订阅。•在`pg_upgrade`期间检索订阅信息的效率提高。•在`sslmode=prefer`中修复TLS回退行为，当服务器在启动过程中发送错误时出错。•文档记录了在备用服务器上立即执行上一个备份后使用`pg_basebackup`增量备份时的错误案例。•修正`pg_upgrade --transaction-size`可能导致后端使用比预期多一个数量级的RAM的问题。

请参阅发布说明<sup>[23]</sup>以获取新功能和更改功能的完整列表，并查看PostgreSQL 17未决问题<sup>[24]</sup>以了解更多修复和变更详情。

------------------------------------------------------------------------

## 测试错误和兼容性

每个PostgreSQL版本的稳定性很大程度上取决于您，社区，通过您的工作负载和测试工具测试即将发布的版本，以便在正式发布PostgreSQL 17之前发现错误和回归。由于这是一个测试版，数据库行为、功能详情和API的细微更改仍然是可能的。您的反馈和测试将帮助确定新功能的最终调整，因此请在近期进行测试。用户测试的质量有助于确定我们何时可以进行最终发布。

未决问题<sup>[25]</sup>的列表在PostgreSQL wiki中公开可见。您可以使用PostgreSQL网站上的此表格报告错误<sup>[26]</sup>：

https://www.postgresql.org/account/submitbug/

------------------------------------------------------------------------

### References

`[1]` 发布说明: *https://www.postgresql.org/docs/release/*\
`[2]` 版本政策: *https://www.postgresql.org/support/versioning/*\
`[3]` CVE-2024-7348: *https://www.postgresql.org/support/security/CVE-2024-7348/*\
`[4]` 8.8: *https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H*\
`[5]` `VACUUM`: *https://www.postgresql.org/docs/current/sql-vacuum.html*\
`[6]` `ALTER TABLE DETACH ... PARTITION CONCURRENTLY`: *https://www.postgresql.org/docs/current/sql-altertable.html*\
`[7]` `CALL`: *https://www.postgresql.org/docs/current/sql-call.html*\
`[8]` `INSERT ... DEFAULT`: *https://www.postgresql.org/docs/current/sql-insert.html*\
`[9]` `ALTER TABLE ... SET LOGGED|UNLOGGED`: *https://www.postgresql.org/docs/current/sql-altertable.html*\
`[10]` `INSERT ... ON CONFLICT`: *https://www.postgresql.org/docs/current/sql-insert.html*\
`[11]` `ALTER TABLE`: *https://www.postgresql.org/docs/current/sql-altertable.html*\
`[12]` `CREATE TABLE ... LIKE STATISTICS`: *https://www.postgresql.org/docs/current/sql-createtable.html*\
`[13]` PL/pgSQL: *https://www.postgresql.org/docs/current/plpgsql.html*\
`[14]` PL/Perl: *https://www.postgresql.org/docs/current/plperl.html*\
`[15]` PL/Python: *https://www.postgresql.org/docs/current/plpython.html*\
`[16]` `pg_restore -l`: *https://www.postgresql.org/docs/current/app-pgrestore.html*\
`[17]` `pg_stat_statements`: *https://www.postgresql.org/docs/current/pgstatstatements.html*\
`[18]` `postgres_fdw`: *https://www.postgresql.org/docs/current/postgres-fdw.html*\
`[19]` `postgres_fdw`: *https://www.postgresql.org/docs/current/postgres-fdw.html*\
`[20]` 发布说明: *https://www.postgresql.org/docs/release/*\
`[21]` 测试版测试过程: *https://www.postgresql.org/developer/beta/*\
`[22]` 升级: *https://www.postgresql.org/docs/17/static/upgrading.html*\
`[23]` 发布说明: *https://www.postgresql.org/docs/17/release-17.html*\
`[24]` PostgreSQL 17未决问题: *https://wiki.postgresql.org/wiki/PostgreSQL_17_Open_Items*\
`[25]` 未决问题: *https://wiki.postgresql.org/wiki/PostgreSQL_17_Open_Items*\
`[26]` 报告错误: *https://www.postgresql.org/account/submitbug/*\
`[27]` 下载: *https://www.postgresql.org/download/*\
`[28]` 发布说明: *https://www.postgresql.org/docs/release/*\
`[29]` 安全: *https://www.postgresql.org/support/security/*\
`[30]` 版本政策: *https://www.postgresql.org/support/versioning/*\
`[31]` 测试版测试信息: *https://www.postgresql.org/developer/beta/*\
`[32]` PostgreSQL 17测试版发布说明: *https://www.postgresql.org/docs/17/release-17.html*\
`[33]` PostgreSQL 17未决问题: *https://wiki.postgresql.org/wiki/PostgreSQL_17_Open_Items*\
`[34]` 功能矩阵: *https://www.postgresql.org/about/featurematrix/*\
`[35]` 提交错误: *https://www.postgresql.org/account/submitbug/*\
`[36]` 在X/Twitter上关注@postgresql: *https://twitter.com/postgresql*\
`[37]` 捐赠: *https://www.postgresql.org/about/donate/*\
`[38]` pgsql-www@lists.postgresql.org: *mailto:pgsql-www@lists.postgresql.org*\
`[39]` 邮件列表: *https://www.postgresql.org/list/*

------------------------------------------------------------------------

## 数据库老司机

**欢迎微信搜索 pigsty-cc加入 PGSQL 交流群**
