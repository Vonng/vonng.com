# PostgreSQL 小版本大地震：一次修掉 52 个安全漏洞

11 月 12 日，PostgreSQL 全球开发组一口气发了全线受支持分支的小版本更新：**18.7、17.12、16.16、15.20、14.25**（PG 14 就此寿终正寝，这是它的谢幕版），顺带端出了 **PostgreSQL 19 RC 2**。

熟悉 PG 社区节奏的老朋友一眼就能看出反常：往年年度大版本基本在 9 月或 10 月稳稳落地，今年 **PostgreSQL 19 拖到 11 月中旬才憋出 RC 2**。9 月底的 [Beta 4 先砍掉了一批大特性](https://mp.weixin.qq.com/s/qAt4LBJh1pWXprsK7bLSXg)，10 月中旬出 RC 1，现在正式版排到了 **11 月 19 日**。

为什么拖这么久？发布团队在 [10 月 10 日的邮件](https://www.postgresql.org/message-id/f161fbb7-e193-42eb-bec7-4cfc1af74a50@postgresql.org)里交了底：各维护分支攒下了大批修复，得先把这些活全塞进 PG 19 RC 2，才敢发正式版。看一眼今天的[发布公告](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)就知道这包袱有多沉——**单次修复 52 个安全漏洞（CVE），外加 140 多个 Bug**。

搁在往年，PostgreSQL 一个季度小版本也就修三五个 CVE；今年画风彻底变了。[8 月那一轮刚修了 28 个 CVE 和 110 多个 Bug](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492801&idx=1&sn=ca763a816cba8da0226f8613e0ee5a07&scene=21#wechat_redirect)，当时大家已经觉得够猛了，结果三个月后直接干到了 52 个和 140 多个。对一向稳如老狗的 PostgreSQL 来说，这算得上一场小版本级别的“大地震”了。

## 开源软件“渡劫”

为什么今年漏洞突然扎堆往外冒？答案一点也不神秘：AI 辅助代码审计上强度了。

老冯在《[当云被打成筛子](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493702&idx=1&sn=23231259ad592eb2f45e5a2f672298a8&scene=21#wechat_redirect)》《[当互联网真被打成筛子](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493712&idx=1&sn=2edd004cb0e18d0c7341f941127b9317&scene=21#wechat_redirect)》和《[渡劫期的 PostgreSQL 生态大更新](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493906&idx=1&sn=3abb155e393d823f1509a180b2f252fe&scene=21#wechat_redirect)》里聊过好几次，眼下所有核心开源基础软件都在集体“渡劫”。这回连猜都不用猜，翻开 [18.7 官方发布注记](https://www.postgresql.org/docs/release/18.7/)的致谢栏，OpenAI Security Research Team、OpenAI Codex Security、Anthropic OSS program，还有 Claude 与 Ada Logics 的名字排成了一串。

再看这 52 个 CVE 的成色，更是一股浓浓的自动化审计味：**32 个漏洞的 CVSS v3.1 评分齐刷刷顶在 8.8**，大片涉及任意代码执行。清一色的类型混淆（Type Confusion）、释放后使用（Use-After-Free）、堆缓冲区溢出和整数回绕；从复合类型、`plperl`/`pltcl`、`dblink`、刚进内核没多久的统计信息导入，一路犁到 `pg_dump`、`pg_restore`、`reindexdb`、`vacuumdb` 这些 DBA 天天顺手敲的家伙事儿，全被筛了个底朝天。哪怕是全世界最顶尖的一帮 C 语言老炮打磨了三十年的代码库，遇上这种不眠不休的犁地式审计，陈年暗伤也得排着队往外露。

这滋味老冯自己太熟了。不光 PostgreSQL，我自己维护的开源对象存储 [**Silo**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493772&idx=1&sn=976b2589aca159383ff5e0ed7686f72d&scene=21#wechat_redirect) 这阵子也天天在接安全报告、审代码、发补丁，刚放出的 [11 月 12 日版本](https://github.com/pgsty/silo/releases/tag/RELEASE.2026-11-12T00-00-00Z)就又修掉了一批安全与正确性问题。

除了这 52 个 CVE，顺手修掉的 140 多个常规 Bug 里也有几个真能让人后背发凉的坑：在备库上跑并行 `pg_dump`，可能把导出文件和备库自己的数据一块儿搞坏；增量备份可能打出坏备份；GIN 索引和 `pg_trgm` 的 GiST 索引可能损坏或漏数据；没限定长度的 `bpchar` 列，B-tree 索引去重能让仅索引扫描吐出错误结果。社区甚至趁这次小版本直接**推倒重写了查询优化器的连接消除（Join Removal）逻辑**——官方话说得很实在：小版本干这么大动作确实少见，但老代码实在补不动了，再打补丁还得接着漏。

## 该升还得升：有人管的叫补丁，没人管的叫后门

每次发小版本，总有朋友来问老冯：这次急不急着升？

老冯平时的口径一直是：只要数据库老老实实待在内网防火墙后面，连进来跑 SQL 的也都是自己人，那按常规维护窗口排期就行，犯不着自己吓自己。

但“不用慌”不等于“可以躺平装死”，尤其遇上今天这种分量的小版本。内网隔离防得住公网扫街，防不住应用被打穿之后的低权限账号提权——这批漏洞里有不少只要建对象这类普通权限就能动手（比如 [CVE-2026-6460](https://www.postgresql.org/support/security/CVE-2026-6460/)），连 `pg_dump`、`pg_restore` 都可能栽在恶意源库或来路不明的备份文件手里；至于备份打坏了、索引查错数了，防火墙更是爱莫能助。再加上 PostgreSQL 14 今天正式退役（EOL），这波升级真别往后拖了。

同一大版本内升级不用折腾 `pg_upgrade` 或逻辑导出导入，但**这回只换内核二进制可不算完活**。对照[官方升级说明](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)和[发布注记](https://www.postgresql.org/docs/release/18.7/)，有几件手尾得一块儿收拾掉：

- **C 语言扩展得重编**：想把 [CVE-2026-6460](https://www.postgresql.org/support/security/CVE-2026-6460/) 彻底堵上，C 扩展必须拿新版头文件重新编译，部分扩展还得改源码。用发行版软件源的，盯一眼扩展包跟上了没有；自己编译的，老老实实重编并测一遍兼容性，千万别为了图省事把 `composite_type_mismatch` 检查给关了。之前那次[小版本 ABI 翻车](https://mp.weixin.qq.com/s/l1BgfLaRKNNEqHyfx33E6A)早就敲过警钟：内核和扩展是一条绳上的蚂蚱。
- **问题索引得排查重建**：检查受影响的 GIN 索引；重建用了 `gist_trgm_ops` 的 GiST 索引；重建未限定长度 `bpchar` 列上的 B-tree 索引（定长 `char(n)` 没事）；要是撞上 `missing chunk number` 报错，按说明把对应表的索引重做一遍。
- **备份基线与分区表巡检**：开了增量备份的，升完级重打一次全量备份刷新基线；分区表顺手查一下有没有不该存在的 `NOT NULL NO INHERIT` 约束。
- **PG 14 准备搬家**：`14.25` 是最后一班车，还在跑 14 的同学该排大版本升级计划了。

企业客户直接找老冯就行，我们排个窗口，把内核、扩展升级和后面的索引约束巡检稳稳当当一条龙办了；自建团队老冯就只能隔空喊一嗓子了，对照上面那几条赶紧动起来。

说到底，最近这几个月就是开源基础软件维护能力的一场大考。一次爆出 52 个 CVE 看着唬人，但换个念头想，这反倒是件值得庆幸的事——说明这软件**有人管**，天塌下来还有人在前面顶着发补丁。真正要命的是那些没人管、半死不活的项目和孤儿分支：洞照样被人用 AI 一抓一把，但没人修，摆在那儿就是敞开的后门。之前 [pgBackRest 停更又续命的风波](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492056&idx=1&sn=575aa621f3eab9cc20eea0998bb8c099&scene=21#wechat_redirect)讲的也是同一个理：开源底座这摊活，总得有活人接着干。

## Pigsty 4.6 首日跟进

光催大家升级不够，做发行版的自己手脚得先利索。

PostgreSQL 发版当天，[**Pigsty v4.6.0**](https://github.com/pgsty/pigsty/tree/v4.6.0) 就同步跟进了，版本基线对齐到 **PostgreSQL 18.7** 与 **Pig 1.11.0**，配套的全平台扩展重编译、软件源同步和离线安装包也在连夜往外推。

这轮活儿远不止换个 PG 内核那么轻松。为了应付这波安全大考，老冯最近拉了张长单子，把仓库里的第三方依赖和几百个 PG 扩展挨个过了一遍筛子；自己手里维护的几个 Go 基础设施项目也集中发了一轮新版：

- 对象存储 [**Silo 20261112**](https://github.com/pgsty/silo/releases/tag/RELEASE.2026-11-12T00-00-00Z)
- 包管理器 [**Pig 1.11.0**](https://github.com/pgsty/pig/releases/tag/v1.11.0)
- 仓库管理器 [**SOW 0.7.1**](https://github.com/pgsty/sow/releases/tag/v0.7.1)
- 监控采集器 [**pg_exporter 1.6.1**](https://github.com/pgsty/pg_exporter/releases/tag/v1.6.1)
- 配套 Go 工具链与底层组件依赖更新

从数据库内核、扩展生态、包管理供应链到监控与备份存储底座，这一轮都得重新对齐。另外，老冯维护的 [**PostgreSQL 中文文档**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493128&idx=1&sn=d28faa447c8f9b527d872189ca3aed7b&scene=21#wechat_redirect) 也已经更新了这一批最新的小版本。

## 聊个高兴点的：汉化来了

前面聊了一堆修洞渡劫的糟心事，最后说点开心的。

**老冯前阵子系统重做并审校的简体中文消息（NLS `zh_CN`），已经正式进了 PostgreSQL 14 到 19 全部六个大版本。** 翻一翻这轮各版本的发布标签，连谢幕演出的 [**14.25 都带上了**](https://github.com/postgres/postgres/blob/REL_14_25/src/backend/po/zh_CN.po)，一个没落。

从现在起，PG 服务端和命令行工具吐出来的提示与报错，总算能说一口利索的中国话了。前因后果可以看《[PostgreSQL 中文版来了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493356&idx=1&sn=929cc3ef65ffaca809ae68e914eb9f18&scene=21#wechat_redirect)》和《[为什么要做 PostgreSQL 汉化？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493604&idx=1&sn=714ba4f204f51beaa691d035fb1e7f24&scene=21#wechat_redirect)》。

老冯的名字 Ruohang Feng，写进 PostgreSQL 19 发行说明的致谢名单（Acknowledgments）。11 月 11 日上游合入了 [Add translators to release notes credits](https://github.com/postgres/postgres/commit/8f8e68b62bd253b959ee3f47b5919bc4963dd005)，把包括老冯在内的一批译者加了进去。

目前[官方 Babel 状态表](https://babel.postgresql.org/)上，PG 19 简体中文各组件覆盖率在 99%–100%，PG 14–18 在 98%–100%；封版前临时变动的几条零星消息，老冯在 [`pgnls` 仓库](https://github.com/pgsty/pgnls/releases/tag/20261112)里也已经补齐到了 100%，后面会一直跟着上游走。

想来这事多少也带点黑色幽默。过去这么多年，到处都在喊“做中国人自己的数据库”；放眼一圈，国内多少徒子徒孙吃着 PostgreSQL 的红利，拿 PG 的代码包装出天花乱坠的商业故事，结果上游最基础的中文消息目录，自何伟平等前辈早年开荒之后，除了几本客户端目录偶有修补，服务端主干一晃七年没人动过。这种费工夫、又没法拿去融资讲故事的苦活，最后还是得有人挽起袖子自己干。

吐槽归吐槽，开源世界本就天下为公。老冯挺希望国内这些下游厂商顺手把上游这波汉化接过去——好事一桩，免得顶着“国产数据库”的招牌，真到报错的时候连句囫囵中国话都说不利索，白白让人看笑话。

写这篇文章的时候，老冯正猫在外地出差的酒店房间里，明天还要去中国企业 AI 大会讲一场。今晚就在一边对着上游公告核细节，一边远程指挥“家里的 Agent 小弟”跑全平台编译打包、同步软件源、发 Pigsty 4.6、编中文文档，争取让大伙儿睁眼就能用上验证妥当的新包。

外头风急，但也不用慌。别焦虑，别侥幸，把该升的版本升了，把自家的底座看住就行。

## 延伸阅读

- 2026-11-06：[渡劫期的 PostgreSQL 生态大更新](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493906&idx=1&sn=3abb155e393d823f1509a180b2f252fe&scene=21#wechat_redirect)
- 2026-11-05：[开源接盘侠又来了：昨天 vchord，今天吃月饼](https://mp.weixin.qq.com/s/hvOHVOmZqFozun6O5eIkDg)
- 2026-11-04：[老冯又接盘新开源项目了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493882&idx=1&sn=9733c0261e364d69fd0da74087d7804f&scene=21#wechat_redirect)
- 2026-10-31：[工业流水线：一天翻译完 30 本 PG 书籍](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493830&idx=1&sn=77588344c27203362f707b56f798960d&scene=21#wechat_redirect)
- 2026-10-22：[当互联网真被打成筛子](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493712&idx=1&sn=2edd004cb0e18d0c7341f941127b9317&scene=21#wechat_redirect)
- 2026-10-21：[当云被打成筛子](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493702&idx=1&sn=23231259ad592eb2f45e5a2f672298a8&scene=21#wechat_redirect)
- 2026-10-12：[复兴 PostgreSQL 中文社区](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493613&idx=1&sn=9a3a8a7e4ed09ab18b2420aa50dfb913&scene=21#wechat_redirect)
- 2026-10-10：[为什么要做 PostgreSQL 汉化？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493604&idx=1&sn=714ba4f204f51beaa691d035fb1e7f24&scene=21#wechat_redirect)
- 2026-09-25：[PostgreSQL 19 Beta 4 发布：特性大砍](https://mp.weixin.qq.com/s/qAt4LBJh1pWXprsK7bLSXg)
- 2026-09-19：[PostgreSQL 中文版来了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493356&idx=1&sn=929cc3ef65ffaca809ae68e914eb9f18&scene=21#wechat_redirect)
- 2026-09-10：[PG 中文文档发布：11 个大版本，一个不落](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493128&idx=1&sn=d28faa447c8f9b527d872189ca3aed7b&scene=21#wechat_redirect)
- 2026-08-14：[井喷：修了 28 个 CVE、110 个 BUG，PG 最新小版本发布](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492801&idx=1&sn=ca763a816cba8da0226f8613e0ee5a07&scene=21#wechat_redirect)
- 2026-05-15：[PostgreSQL 18.4、17.10、16.14、15.18 与 14.23 发布](https://mp.weixin.qq.com/s/NIyIvS9shAFBrU5m1NlWSA)
- 2026-05-05：[pgBackRest 续命战与开源世界的逼定价](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492056&idx=1&sn=575aa621f3eab9cc20eea0998bb8c099&scene=21#wechat_redirect)
- 2026-02-26：[PostgreSQL 号外紧急补丁版本发布！](https://mp.weixin.qq.com/s/whfw9Om3aGI7po1TpKJxtA)
- 2026-02-19：[号外：暂缓 PG 最新小版本安装与升级](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247491225&idx=1&sn=613f074625f09c3cadce75896309d5cc&scene=21#wechat_redirect)
