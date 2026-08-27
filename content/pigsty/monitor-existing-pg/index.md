---
title: "如何用Pigsty监控现有PostgreSQL (RDS/PolarDB/自建)？"
date: 2023-09-17
authors: [vonng]
summary: >
  如何使用 Pigsty 监控云数据库服务，例如 PolarDB / RDS for PostgreSQL，或者自建的现有PG数据库？
tags: [Pigsty, 监控, RDS]
---

**Pigsty 是一个开箱即用的 PostgreSQL 发行版，与本地优先的 RDS 开源替代**。但它也可以单独作为一个 PostgreSQL/主机监控系统来使用。本文以阿里云为例，介绍了用一台 ECS 安装部署 Pigsty，并用于监控云上的 **PolarDB** 与 **RDS for PostgreSQL**，为现有数据库带来极致的观测能力。

[嵌入媒体](https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&action=mpvideo&auto=0&vid=wxv_3109126349086162945)

## 快速上手

使用 Pigsty 教程分为四个步骤：

1.申请用于部署 Pigsty 的 ECS 服务器2.在 ECS 服务器上完整单机安装 Pigsty3.配置 PolarDB / RDS 的监控用户、模式、视图、黑白名单4.将 RDS / PolarDB for PG 接入 Pigsty 监控系统中

只要您有阿里云账号，使用按量付费模式（需要账户余额¥100以上），费用大致为 ¥4 / 小时，一小时内收工。

## Why Pigsty

**在讲 How 之前先说 Why**。为什么要用一个额外的监控系统来做这件事？难道各家云厂商不是已经提供 RDS 监控了吗？没有错，只不过各家云厂商的 RDS PostgreSQL 的监控实在太简单了：这种程度的监控，对于回答数据库活着还是死了这件事也许足够了，但对于稍微高级一丁点儿的管理工作：性能优化，故障诊断都无能为力。

![图片](01.webp)

![图片](02.webp)

Pigsty 的监控系统便是为了解决这个问题而生的。Pigsty 提供了基于开源的 Grafana / Prometheus 现代可观测性技术栈做监控的最佳实践。整套系统同样被设计为一键拉起，开箱即用的 INFRA 模块。Pigsty 所管理的任何组件都会被自动纳入监控之中，包括主机节点，负载均衡 HAProxy，数据库 Postgres，连接池 Pgbouncer，元数据库 ETCD，KV缓存 Redis，对象存储 MinIO，……，以及整套监控基础设施本身。大量的 Grafana 监控面板与预置告警规则会让你的系统观测能力有质的提升。

![图片](03.webp)

Pigsty提供的监控面板概览\

无论是故障分析还是慢查询优化、无论是水位评估还是资源规划，Pigsty 为您提供全面的数据支撑，真正做到数据驱动。在 Pigsty 中，超过三千类监控指标被用于描述整个系统的方方面面，并被进一步加工、聚合、处理、分析、提炼并以符合直觉的可视化模式呈现在您的面前。从全局大盘总览，到某个数据库实例中单个对象（表，索引，函数）的增删改查详情都能一览无余。您可以随意上卷下钻横向跳转，浏览系统现状与历史趋势，并预测未来的演变。

![图片](04.webp)

对于现有的 PostgreSQL 数据库特别是 RDS 云数据库来说，虽然 Pigsty 拿不到主机监控数据，也没有高可用/连接池等组件的监控数据，也缺少原生的数据库日志。但能利用好 PostgreSQL 本身的监控指标，已经有着足够强大的力量了。

您可以查阅公开Demo：https://demo.pigsty.cc 来了解 Pigsty 监控系统提供的能力。

### 使用 Terraform 申请 ECS 服务器

单机安装 Pigsty 需要一台 x86_64 ECS 云服务器，EL 7-9操作系统（建议使用 Rocky 8.6/9.1），规格最小 1C2G 。您可以直接在控制台上申请资源，或者使用 Pigsty 提供的 Terraform 模板一键完成资源申请与置备。默认配置会使用固定的 `10.10.10.10` IP地址与密码 `PigstyDemo4`，并分配一个公网IP以供访问。

![图片](05.webp)

![图片](06.webp)

------------------------------------------------------------------------

### 在ECS上完整安装单机版 Pigsty

登陆 ECS 后，可以通过以下命令完成 Pigsty 的单机安装

    bash -c "$(curl -fsSL https://get.pigsty.cc/latest)"   # 下载 Pigsty
    cd ~/pigsty; ./bootstrap;                              # 提示下载离线软件包
    ./configure                                            # 配置 Pigsty
    vi pigsty.yml  # 定制一些配置，比如修改各种密码
    ./install.yml  # 完成完整的单机安装，使用离线包完整安装约10分钟

Pigsty的详细安装过程介绍：https://pigsty.cc/doc/#/zh/INSTALL，整个过程耗时约十几分钟。

安装完成后，您可以通过 ECS 公网 IP 地址上的 3000 端口访问监控系统 Grafana，监控界面中会显示出完整的自我监控。例如本例中：http://59.110.161.154:3000 ，默认用户名密码为：`admin` / `pigsty`。

![图片](07.webp)

我们建议您使用域名/https访问 Pigsty 的 Web 界面，注意在生产环境使用时，我们强烈建议您修改默认密码，并谨慎对公网暴露界面。

![图片](08.webp)

------------------------------------------------------------------------

### 配置 PolarDB / RDS PG 监控

PolarDB 的配置细节在此不再赘述，关键是要有一个给监控用户使用的连接串，可以从 ECS 上访问 PolarDB 主库 / 从库，并确保相关监控用户具有足够的读取权限，以及相关监控扩展已经完成安装。

•创建集群，确保 PolarDB 与ECS在同一个可用区/子网内，可以从ECS访问PolarDB。•创建集群账号：管理用户 `dbuser_dba`，高权限账号，用来对集群进行进一步的配置。•添加集群访问白名单：将 ECS 内网IP地址 `10.10.10.10` 添加到集群白名单中。•创建一个业务数据库，这里以 `test` 为例。

配置好数据库集群的账号、白名单、数据库之后，使用高权限管理用户连接至新创建的数据库

    $ psql postgres://dbuser_dba:DBUser_DBA@pc-2ze379wb1d4irc18x.polardbpg.rds.aliyuncs.com:1921/postgres

使用高权限用户创建专用监控用户，当然您也可以在控制台创建。

![图片](09.webp)

强烈建议安装 `pg_stat_statements` 扩展，它可以提供非常重要的关于查询的

------------------------------------------------------------------------

## 将现有PG数据库接入监控

为了将 RDS for PostgreSQL 实例与 PolarDB 实例纳入监控，您需要将这些目标实例的身份信息与连接信息告诉 Pigsty。编辑 `pigsty.yml` 配置文件，在 `all.children.infra.vars.pg_exporters` 定义这些待监控的远程数据库实例，这是一个字典，Key 为唯一分配的本地监控组件端口号，Value为目标实例的配置信息。

![图片](10.webp)

这里，我们接入了一个一主一从的 PolarDB 集群，并将其命名为 `pg-polar`，一个基础版（单节点）的 RDS for PostgreSQL 实例并命名为 `pg-rds`，以及一个高可用版本并带有一个只读节点的 RDS 集群 `pg-rdsha`。其配置如下所示，并不是所有参数都是必须的，通常来说，只有 `pg_cluster`，`pg_seq`，与 `pg_host` （`pg_port`，如果不是5432） 是需要修改的，其他参数可以按需指定覆盖。

定义好这些配置选项后，您可以使用以下命令，将其纳入到 Pigsty 的监控系统中：

        bin/pgmon-add pg-polar
        bin/pgmon-add pg-rds
        bin/pgmon-add pg-rdsha

然后，您就可以在 Pigsty 监控系统中看到这三个新集群了。

![图片](11.webp)

点击浅灰蓝色的集群名/实例名，即可跳转到对应集群/实例 PGRDS 监控面板上：

![图片](12.webp)

![图片](13.webp)

点击浅灰蓝色的集群名/实例名，即可跳转到对应集群/实例 PGRDS 监控面板上：

首屏包含了最为关键的信息，集群实例成员，存活状态，数据库列表与导航，13个核心监控指标。点击都可以展开更详细的信息。\

![图片](14.webp)

在 PGRDS Cluster 与 PGRDS Instance 之间，可以方便地在图表元素上点击跳转，快速上卷下钻。

![图片](15.webp)

同时，您依然可以复用 Overview / Database 层次的所有监控面板，查阅数据库内部的详细细节，比如每一类查询的 QPS / RT，或者每个表上的增删改查：

![图片](16.webp)

![图片](17.webp)

![图片](18.webp)

![图片](19.webp)

Pigsty的监控系统还允许您直接访问数据库的 Catalog （可选），从系统视图中查阅统计数据。例如锁等待 / TopSQL 等。

![图片](20.gif)

![图片](21.webp)

更多监控系统的细节就不在此展开了，欢迎访问 Pigsty 文档：  https://pigsty.cc ，或者访问 Demo 在线体验：https://demo.pigsty.cc 。点击“查看原文”，访问 Bilibili 视频版教程。

如果您对 Pigsty 与 PostgreSQL 感兴趣，也欢迎微信搜索 pigsty-cc 添加 Pigsty 小助手，加入 PGSQL x Pigsty 交流群中。
