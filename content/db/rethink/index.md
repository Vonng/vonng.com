---
title: "正本清源：技术反思录"
date: 2023-05-29
authors: [vonng]
summary: >
  降本增效的主旋律触发了所有技术的价值重估，当然也包括数据库。本系列将评述数据库领域热点技术，并对其在当下的利弊权衡发出灵魂拷问：云数据库、分布式数据库、微服务、K8S容器化等技术，究竟是真需求还是伪需求？
series: ["正本清源"]
tags: [云计算, 数据库, 架构, 技术评论]
---

最近在技术圈有一些热议的话题，[云数据库是不是智商税？](/cloud/rds/)？[公有云是不是杀猪盘](/cloud/ebs/)？[分布式数据库是不是伪需求](/db/distributive-bullshit/)？[微服务是不是蠢主意](/db/microservice-bad-idea/)？[你还需要运维和 DBA 吗](https://mp.weixin.qq.com/s/Gk9bG_EOIv0IAkim41XRHg)？[中台是不是一场彻头彻尾的自欺欺人](https://mp.weixin.qq.com/s/VgTU7NcOwmrX-nbrBBeH_w)？在 Twitter 与 HackerNews 上也有大量关于这类话题的讨论与争辩。

在这些议题的背后的脉络是大环境的改变：**降本增效压倒其他一切，成为绝对的主旋律**。开发者体验，架构可演化性，研发效率这些属性依然重要，但在 **ROI** 面前都要让路 —— **社会思潮与根本价值观的变化会触发所有技术的重新估值。**

有人说，互联网公司砍掉一半人依然可以正常运作，只不过老板不知道是哪一半。现在收购推特的马斯克刷新了这个记录：截止到 2023 年 5 月份，推特已经从 8000 人一路裁员 **90%** 到现在的不足千人，而依然不影响其平稳运行。**这个结果彻底撕下大公司病冗员问题的遮羞布，其余互联网大厂早晚会跟进，掀起新一轮大规模裁员的血雨腥风**。

在经济繁荣期，大家可以有余闲冗员去自由探索，也可以使劲儿吹牛造害铺张浪费炒作。但在经济萧条下行阶段，所有务实的企业与组织都会开始重新审视过往的利弊权衡。同样的事情不仅会发生在人上，也会发生在技术上，这是实体世界的危机传导到技术界的表现：**泡沫总会在某个时刻需要出清，而这件事已正在发生中。**

公有云，Kubernetes，微服务，云数据库，分布式数据库，大数据全家桶，Serverless，HTAP，Microservice，等等等等，所有这些技术与理念都将面临拷问：**有些事不上秤没有四两，上了秤一千斤也打不住**。这个过程必然伴随着怀疑、痛苦，伤害与毁灭，但也孕育着希望，喜悦，发展与新生。花里胡哨华而不实的东西会消失在历史长河里，大浪淘沙能存留下来的才是真正的好技术。

在这场技术界的惊涛骇浪中，需要有人透过现象看本质，脚踏实地的把各项技术的好与坏，适用场景与利弊权衡讲清楚。而我本人愿意作为一个亲历者，见证者，评叙者，参与者躬身入局，加入其中。这里拟定了一个议题列表集，名为《**正本清源：技术反思录**》，将依次撰文讨论评论业界关心的热点与技术：

- [国产数据库是大炼钢铁吗？](/db/great-leap-db/)
- [中国对 PostgreSQL 的贡献约等于零吗？](/pg/china-pg-contribution/)
- [MySQL 的正确性为何如此拉垮？](/db/bad-mysql/)
- [没错，数据库确实应该放入 K8s 里！](/db/database-in-k8s-counterpoint/)（转载 SealOS）
- [数据库应该放入 K8S 里吗？](/db/db-in-k8s/)
- [把数据库放入 Docker 是一个好主意吗？](/db/db-in-k8s/)
- [向量数据库凉了吗？](/db/svdb-is-dead/)
- [阿里云的羊毛抓紧薅，五千的云服务器三百拿](/cloud/cheap-ecs/)
- [数据库真被卡脖子了吗？](/db/db-choke/)
- [EL 系操作系统发行版哪家强？](/db/rhel-compatibility/)
- [基础软件到底需要什么样的自主可控？](/db/sovereign-dbos/)
- [如何看待 MySQL vs PGSQL 直播闹剧](/pg/mysql-pg-live-drama/)
- [驳《MySQL：这个星球最成功的数据库》](/pg/rebut-mysql-best/)
- [向量是新的 JSON](/pg/vector-json-pg/) 【译评】
- [【译】微服务是不是个蠢主意？](/db/microservice-bad-idea/)
- [分布式数据库是伪需求吗？](/db/distributive-bullshit/)
- [数据库需求层次金字塔](/db/demand-pyramid/)
- [StackOverflow 2022 数据库年度调查](/db/so2022-db/)
- [DBA 还是一份好工作吗？](/cloud/is-dba-good-job/)
- [PostgreSQL 会修改开源许可证吗？](/pg/pg-license/)
- [Redis 不开源是“开源”之耻，更是公有云之耻](/db/redis-oss/)
- [PostgreSQL 正在吞噬数据库世界](/pg/pg-eat-db-world/)
- [RDS 阉掉了 PostgreSQL 的灵魂](/cloud/rds-castrates-pg/)
- [技术极简主义：一切皆用 Postgres](/pg/just-use-pg/)

[![rethink](rethink.jpg)](https://mp.weixin.qq.com/s/Q0OtrpEhF24XN7gwMjbSRA)

---

## 写作计划

《[云数据库是不是智商税](/cloud/rds/)》

《[云盘是不是杀猪盘？](/cloud/ebs/)》

《[分布式数据库是不是伪需求](/db/distributive-bullshit/)？》

《国产数据库是不是大跃进？》

《TPC-C 打榜是不是放卫星？》

《信创数据库是不是恰烂钱？》

《谁卡住了中国数据库的脖子？》

《[微服务是不是蠢主意](/db/microservice-bad-idea/)？》

《Serverless 是不是榨钱术？》

《RCU/WCU 计费是不是阳谋杀猪？》

《数据库到底要不要放入 K8S?》

《HTAP 是不是纸上谈兵？》

《单机分布式一体化是不是脱裤放屁？》

《你真的需要专用向量数据库吗？》

《你真的需要专用时序数据库吗？》

《你真的需要专用地理数据库吗？》

《APM 时序数据库选型姿势指北》

《202x 数据库选型指南白皮书》

《开源崛起：商业数据库还能走多远？》

《[范式转移：云原生能否干翻公有云？](/cloud/paradigm/)》

《[本地优先：你是否真的需要 XaaS？](/misc/goodbye-gpl/)》

《云厂商的 SLA 到底靠不靠得住？》

《大厂技术管理思想真的先进吗？》

《卷数据库内核还有没有出路？》

《用户到底需要什么样的数据库？》

《再搞 MySQL 还有没有前途？》

《 [炮打 RDS —— 我的一张大字报](/pigsty/v2.0-launch/) 》

《[为什么 PostgreSQL 是最成功的数据库？](/pg/pg-is-best/)》

如果您有任何认为值得讨论的话题，也欢迎在评论区中留言提出，我将视情况加入列表中。

---

发布版本：[微信公众号](https://mp.weixin.qq.com/s/Q0OtrpEhF24XN7gwMjbSRA)
