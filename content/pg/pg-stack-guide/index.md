---
title: "开源PG全家桶上手指南"
date: 2021-05-21
authors: [vonng]
summary: >
  PostgreSQL中文社区又开始在线直播啦！本周日（5月23日晚7:30），由我带给大家来一段单口相声 —
tags: [PostgreSQL, PG管理]
---

PostgreSQL中文社区又开始在线直播啦！本周日（5月23日晚7:30），由我带给大家来一段单口相声 —— **《开源PG全家桶上手指南》**。

![图片](01.webp)

Pigsty是 **开源** 的PostgreSQL一条龙解决方案，主要有以下三个目标：

- **做最顶尖最专业的** **开源PostgreSQL** **监控系统**

- **做门槛最低最好用的** **开源PostgreSQL** **管控方案**

- **做开箱即用的数据分析可视化集成环境**

  \

  \

  **详情参考：https://pigsty.cc**

## 谁会感兴趣？

**PostgreSQL DBA，运维，DevOps**：Pigsty提供了一体化的生产级**监控系统**与**部署方案**，可以极大提高数据库的管理&使用水平下限。肯定比自己yum install & systemctl start 强大到不知道哪里去了。其监控系统指标覆盖率完爆市面上所有同类产品。

**PostgreSQL用户，后端开发者，数据研发工程师，内核研发**：Pigsty提供了**与生产环境完全一致**的本地沙箱，其中包含单节点的默认沙箱与4节点的集群沙箱。用户可以方便地在本地进行开发测试，并通过监控系统获得即时反馈。

**对**数据分析**，**数据可视化**感兴趣的人**：Pigsty提供了本地、单机即可运行，开箱即用的**集成数据分析环境**：包括分析功能强大的PostgreSQL（内嵌PostGIS，TimeScale地理空间时序数据等扩展），敏捷的数据库可视化平台Grafana，以及内建的Echarts可视化支持。

**学生，新手程序员，以及任何有兴趣尝试PostgreSQL数据库的用户**。Pigsty上手门槛极低：您只需要有一台虚拟机，或者一台笔记本即可运行。三行命令，一键安装，10分钟搞定。

## 相关分享

先前我在PostgreSQL中文社区做过三次相关的直播分享，分别关于监控系统，高可用架构，数据可视化：

- **PostgreSQL监控实战：集群监控**: https://www.bilibili.com/video/BV1tV411r7hy

- **PG高可用落地实践之Patroni**：https://www.bilibili.com/video/BV1fp4y1S7Hg

- **PostgreSQL与数据可视化**：https://www.bilibili.com/video/BV1Gh411o7FG

其实这些分享中已经可以看到Pigsty的三个核心抓手：**监控**，**管控**，**可视化**。这次分享将浓缩三者精华，直接以实例介绍这些功能。并现手把手演示如何用10分钟从上手到**交付**，**敬请期待**～

**主要内容**

![图片](02.webp)

![图片](03.webp)

![图片](04.webp)

![图片](05.webp)

![图片](06.webp)

![图片](07.webp)
