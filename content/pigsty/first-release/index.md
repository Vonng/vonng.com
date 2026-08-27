---
title: "Pigsty正式发布"
date: 2021-01-13
authors: [vonng]
summary: >
  一个比较正式的上线发布通知：Pigsty —— 世界上最先进的开源关系型数据库PostgreSQL的监控系统与供给方案。
tags: [Pigsty, 监控]
---

今天我很荣幸的宣布，**Pigsty正式发布了！**

![图片](01.webp)

**官方网站：https://pigsty.cc**

## Pigsty是什么？

- Pigsty是针对大规模PostgreSQL集群的监控系统

- Pigsty是高可用PostgreSQL集群的供给方案

- Pigsty基于开源生态构建，是免费的开源软件

![图片](02.webp)

Pigsty 针对大规模数据库集群监控与管理而设计，提供业界顶尖的PostgreSQL监控系统与开箱即用的高可用数据库供给方案。Pigsty基于开源生态构建，旨在降低PostgreSQL使用管理的门槛，为用户带来极致的可观测性与丝滑的数据库使用体验。\

## Pigsty是监控系统

PostgreSQL是世界上最好的开源关系型数据库，但在其生态中却缺少一个足够好的监控系统。Pigsty即旨在解决这一问题：提供世界上最好的PostgreSQL监控系统，

开发Pigsty的初衷是：作者需要对一个大规模PostgreSQL集群进行管理，但找遍所有市面上的开源与商业监控系统方案后，发现没有一个是“足够好用”的。本着“**我行我上**”的精神，开发设计了本系统。

Pigsty的界面基于Grafana深度定制，由30+监控面板，上千+仪表盘，18万行JSON定制而成，涵盖数据库与基础设施的方方面面。

![图片](03.webp)

![图片](04.webp)

Pigsty提供近1200个监控指标，一骑绝尘，远超市面上现有的相关产品。提供从全局大盘汇总到某一个数据对象增删改查的全域数据支持。\

![图片](05.webp)

## Pigsty是供给方案

Pigsty同时还是一个高可用数据库集群供给方案。

监控系统要想发行与演示，必须要先有被监控的对象。可许多用户自建的数据库实在是千奇百怪。所以这里，Pigsty项目决定将数据库供给方案作为项目的一部分发布。

将主从复制，故障切换，流量代理，连接池，服务发现，基本权限系统等成熟的生产级部署方案打包至本项目中，真正让用户做到**立等可取**，**开箱即用**。

![图片](06.webp)

数据库供给方案所做的事情一言以蔽之：**您填写一张表单，然后系统会自动根据表单的内容创建出对应的数据库集群**。真正做到傻瓜式数据库管理。

![图片](07.webp)

Pigsty通过130+配置项定义了数据库与基础设施的方方面面，采用声明式的语法与幂等的执行机制，使用代码定义基础设施，在物理机与虚拟机上达到了与Kubernetes类似的舒爽体验，简单易用。

## Pigsty是开源软件

Pigsty依托开源，回馈社区，是免费的开源软件。Pigsty基于**Apache 2.0**协议开源，但也提供**专业版**与**可选的商业支持服务**。欢迎各位贡献ISSUE与PR，也欢迎捐赠与赞助。

![图片](08.webp)

Pigsty的监控系统基于开源组件Prometheus，Grafana，Alertmanager, Exporter进行深度定制开发。同时还包括Nginx, Dnsmasq/CoreDNS, NTP/Chrony, Consul/Etcd等基础设施。遵循业界监控最佳实践，可以方便地与已有监控基础设施集成。

Pigsty的供给方案基于流行的DevOps工具Ansible进行开发，部署涉及的组件包括：Postgres, Pgbouncer, Patroni, HAProxy, Keepalived。所有部署逻辑都以Ansible Role的方式编写，可以方便地进行集成、定制与二次开发。

PostgreSQL是世界上最先进的开源关系型数据库，而Pigsty旨在成为世界上最先进的开源关系型数据库的监控系统与供给方案。希望Pigsty能在各位使用PostgreSQL的过程中起到帮助。

## Pigsty可以开箱即用

Pigsty提供了详实的中英文档供您参考。

更重要的是，Pigsty既提供了可公开访问的演示Demo，也自带了基于Vagrant的本地沙箱。您可以使用以下命令简单的在自己的笔记本上一键拉起带有数据库集群与监控基础设施的沙箱环境。

    make up          # 拉起vagrant虚拟机
    make ssh         # 配置虚拟机ssh访问
    make init        # 初始化Pigsty
    sudo make dns    # 写入Pigsty静态DNS域名（需要sudo,可选）
    make mon-view    # 打开Pigsty首页（默认用户密码：admin:admin）

也可以在修改极少量配置后，使用完全相同的工作流初始化生产环境。

Pigsty的相关站点\
-----------------

Pigsty提供了详实的中英文档供您参考。

中文站点：https://pigsty.cc

英文站点：https://pigsty.cc/en/

官方演示：http://demo.pigsty.cc

Github仓库：https://github.com/Vonng/pigsty

![图片](09.webp)
