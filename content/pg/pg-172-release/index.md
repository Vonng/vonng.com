---
title: "PostgreSQL 号外小版本发布：17.2, 16.6, 15.10, 14.15, 13.18, 12.22"
date: 2024-11-21
authors: [vonng]
summary: >
  不要在星期五发布代码，否则多忙一整周！PostgreSQL小版本发布当天，因ABI变化紧急回滚。
tags: [PostgreSQL, PG管理]
---

正如《[**号外：发布当日叫停，PG也躲不过翻车**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488669&idx=1&sn=9a31b12a3ea0aad6aa41135f6ed16120&scene=21#wechat_redirect "号外：发布当日叫停，PG也躲不过翻车")》一文所述，PostgreSQL 在上周四发布的 17.1 打破了 ABI 当天紧急叫停了发布，并于本周四，也就是几分钟前刚刚发布了新的号外小版本序列：17.2, 16.6, 15.10, 14.15, 13.18, 以及 12.22，修复了此问题。

如果你在过去一周中通过互联网上游直接从官方仓库或镜像安装或升级过 PostgreSQL， 那么你可能有概率会遇到一些扩展兼容性的问题，我们强烈建议你立即升级到最新的 PostgreSQL 小版本以解决此问题。

截止至发稿，PGDG YUM/APT 仓库中的二进制成品包均已可用。开箱即用的 PG 发行版 —— [**Pigsty**](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488249&idx=1&sn=6dba0cc29919850594f3379775b1aaec&chksm=fe4b2722c93cae34d59bbad0c0af1caa15fd769bfaa6f7ffe4acbbfa7aab9fb227f85004ab42&scene=21#wechat_redirect) 已经第一时间跟进了 PostgreSQL 最新小版本，并制作好了离线软件包。在确保340个扩展与 17.2 和其他版本的 ABI 兼容性后，将于本周正式发布 v3.1。

以下是 PostgreSQL 全球开发组的发布注记：https://www.postgresql.org/about/news/postgresql-172-166-1510-1415-1318-and-1222-released-2965/

## PostgreSQL 17.2, 16.6, 15.10, 14.15, 13.18, 12.22 发布

由 PostgreSQL 全球开发组发布于 **2024年11月21日**

PostgreSQL 全球开发组已发布所有受支持大版本的更新：包括17.2、16.6、15.10、14.15和13.18。此外，鉴于上一更新版本中某个问题的性质，PostgreSQL 全球开发组还为 PostgreSQL 12 发布了12.22版本。PostgreSQL 12 现已结束生命周期（EOL），将不再接收更多修复。

有关更改的完整列表，请查看发行说明<sup>[1]</sup>。

## PostgreSQL 12 生命周期结束通知

[**这是 PostgreSQL 12 的最终版本**](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488649&idx=1&sn=dedd945b1203606122f874053b8f828f&chksm=fe4b2152c93ca8447e349a8e2dc9d7bcd9193b48a22873cf014e048d6d8a7d499ac6dd33f37f&scene=21#wechat_redirect)。PostgreSQL 12 现已结束生命周期，将不再接收安全和错误修复。如果您在生产环境中运行 PostgreSQL 12，我们建议您计划升级到更新的、受支持的 PostgreSQL 版本。更多信息请参阅我们的版本政策<sup>[2]</sup>。

## 错误修复和改进

以下列出的问题影响 PostgreSQL 17。其中一些问题也可能影响其他受支持的 PostgreSQL 版本。

•恢复 `ALTER ROLE .. SET ROLE`<sup>[3]</sup> 和 `ALTER DATABASE .. SET ROLE`<sup>[4]</sup> 的功能。针对 CVE-2024-10978<sup>[5]</sup> 的修复意外导致如果角色设置来自非交互式来源（包括之前的 `ALTER {ROLE|DATABASE}` 命令和 `PGOPTIONS`<sup>[6]</sup> 环境变量），这些设置不会被应用。•恢复与在2024-11-14发布（17.0、16.4、15.8、14.13、13.16、12.20及更早版本）之前使用 PostgreSQL 构建的 `timescaledb` 和其他 PostgreSQL 扩展的兼容性。此修复将 `struct ResultRelInfo` 恢复到之前的大小，以便受影响的扩展无需重建。•修复逻辑复制槽的 `restart_lsn` 可能倒退的情况。•避免在执行 `pg_rewind`<sup>[7]</sup> 时删除仍需要的 WAL 文件。•修复与删除共享统计条目相关的竞争条件，避免统计数据丢失。•修复当表具有非默认操作类的索引时，在 `ALTER TABLE` 检查索引的操作类选项是否更改时发生的崩溃问题。

## 更新

所有 PostgreSQL 更新版本都是累积的。与其他小版本一样，用户无需转储和重新加载数据库或使用 `pg_upgrade`来应用此更新；您只需关闭 PostgreSQL 并更新其二进制文件即可。

跳过一个或多个更新版本的用户可能需要执行额外的更新后步骤；详情请参阅早期版本的发行说明。

更多详细信息，请参阅发行说明<sup>[8]</sup>。

## 链接

•下载<sup>[9]</sup>•发行说明<sup>[10]</sup>•安全<sup>[11]</sup>•版本政策<sup>[12]</sup>•在 X/Twitter 上关注 @postgresql<sup>[13]</sup>•捐赠<sup>[14]</sup>

如果您对本次发布公告有修改或建议，请发送至公共邮件列表 \*pgsql-www@lists.postgresql.org<sup>[15]</sup>\*。

### References

`[1]` 发行说明: *https://www.postgresql.org/docs/release/*\
`[2]` 版本政策: *https://www.postgresql.org/support/versioning/*\
`[3]` `ALTER ROLE .. SET ROLE`: *https://www.postgresql.org/docs/current/sql-alterrole.html*\
`[4]` `ALTER DATABASE .. SET ROLE`: *https://www.postgresql.org/docs/current/sql-alterdatabase.html*\
`[5]` CVE-2024-10978: *https://www.postgresql.org/support/security/CVE-2024-10978/*\
`[6]` `PGOPTIONS`: *https://www.postgresql.org/docs/current/libpq-envars.html*\
`[7]` `pg_rewind`: *https://www.postgresql.org/docs/current/app-pgrewind.html*\
`[8]` 发行说明: *https://www.postgresql.org/docs/release/*\
`[9]` 下载: *https://www.postgresql.org/download/*\
`[10]` 发行说明: *https://www.postgresql.org/docs/release/*\
`[11]` 安全: *https://www.postgresql.org/support/security/*\
`[12]` 版本政策: *https://www.postgresql.org/support/versioning/*\
`[13]` 在 X/Twitter 上关注 @postgresql: *https://twitter.com/postgresql*\
`[14]` 捐赠: *https://www.postgresql.org/about/donate/*\
`[15]` pgsql-www@lists.postgresql.org: *mailto:pgsql-www@lists.postgresql.org*
