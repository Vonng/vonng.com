---
title: "Pigsty 2.0 展望"
date: 2022-11-11
authors: [vonng]
summary: >
  Pigsty v2: 安全性，兼容性，易用性的大幅改进，开箱即用PITR，开源RDS PG替代，“全盛状态的PostgreSQL”
tags: [Pigsty]
---

最近 PostgreSQL 15 发布了，Pigsty 也开始了紧锣密鼓地跟进，筹划第二个大版本：v2。

Pigsty 2.0 版本将引入一系列重大增强与改进。包括安全性，兼容性，易用性的大幅改进，并添加了开箱即用的 PITR 时间点恢复支持。此版本后，Pigsty 中 PostgreSQL 的架构状态将趋于完美，Pigsty 的缩写也相应修改为 "PostgreSQL in Great STYle"，即 “全盛状态的 PostgreSQL”。

Pigsty v2.0 旨在为用户提供一个开源的，更好的云数据库 RDS for PostgreSQL 上位替代。Pigsty v2.0 目前处于 ALPHA 状态，预计在 PG 15.1，以及 TimescaleDB 支持 PG15 后正式发布。

![图片](01.webp)

## 亮点

- 升级至 PG 15，PostGIS 3.3，Citus 11，TimescaleDB 2.8

- 支持 EL 7，8，9 及兼容发行版（RHEL，CentOS，Rocky，Oracle，Alma）

- 开箱即用的原地时间点恢复支持 （pgbackrest）

- 自适配的节点与数据库配置模板，根据机型规格自动调优

- 自签名 CA，全局 SSL 加密网络流量，更完善的安全机制

- 独立管理的 etcd 集群、部署剧本、监控面板

- 新的 MINIO 对象存储服务，部署、监控支持，允许作为备份中心。

- 开源协议由 Apache License 2.0 变更为 AGPLv3

<!-- -->

- 配置文件大幅精简，用户只需提供身份参数（ID，IP）即可使用。

### META

Pigsty v2 现在添加了新的 `meta_ip` 参数，在配置过程中配置为当前节点的首要 IP 地址，可以在其他变量中引用。例如，当您想使用 备份 Infra 节点时，可以直接通过修改此参数，一次性修改 DNS，NTP，Grafana，Loki 中的引用。

v2 在配置时自动检测环境并配置 `region` （也可以手工制定），Pigsty 会根据区域自动设置一些地理相关的变量，例如上游仓库的镜像地址，NTP 服务子区域等。这一功能主要用于在大陆地区避免 GFW 干扰，加快下载速度。

### CA

在 v2 中会默认创建一个自签名的 CA，为 etcd，PostgreSQL，以及其他所有需要 SSL 的服务签发证书。该 CA 会在所有节点被加入信任 CA 名单，以支持 SSL 流量加密。

### REPO

Repo 定义现在兼容不同的 EL 版本，将自动根据 EL 版本选择对应的 Repo。现在您可以通过 region 指定使用特定区域的上游仓库，例如 `china`, `europe`，加速下载并绕开 GFW。

Repo 将使用 TimescaleDB 与 Citus 官方的仓库下载插件。

对于 EL8，EL9，将直接使用 AppStream 仓库中的 Redis，与 PGDG 仓库中的 HAProxy。

将从 Minio 官方下载 minio 与 mcli 软件包。

### DCS

在 DCS 上，etcd，consul 服务将默认启用 SSL，只有管理节点才可以使用命令行访问 DCS。该特性可以确保 DCS 网络流量不受窃听影响，且将集群状态修改的权限收拢至管理节点上。

ETCD 将取代 Consul 成为 Pigsty 默认使用的 DCS 服务。因为它提供了轻量的实现，少了 Agent 这个额外失效点。且因为 Kubernetes 的存在变得更为流行，沉淀有更多运维经验。

V2 将提供专用的剧本 `etcd.yml` 以部署 ETCD 集群。并提供了专门的 ETCD 监控面板。

### Node

新增的 `node_id` 角色，将统一收集节点信息，并配置节点的身份参数。

所有 `nodes` 名称 现在统一收敛至 `node` 单数形式。

Chrony 将成为默认的 NTP 服务，替代 NTPD。

Tuned 模板中，将自动以 HugePage 的形式分配 26% 的内存专供 PostgreSQL 使用，提高性能。

一个专用的 `node_remove` 角色现在负责处理从 Pigsty 移除节点的工作。

主机节点默认使用的模板从 `tiny` 修改为 `oltp`。

### PostgreSQL

在 PostgreSQL 上，v2 将默认启用 SSL 支持，允许使用加密连接访问 PostgreSQL 服务，以加密数据库通信避免窃听。`/pg/cert` 目录用于盛放服务端证书，用于加密数据库与连接池的流量，访问 ETCD 服务。

修改用户密码的操作记录现在将从 PG 日志中移除，以避免意外泄漏。

新的 `scram-sha-256`  将取代 `md5`，成为 Pigsty 中 PG 默认的密码认证方式，以提高安全性。

新增的 `monitor.pgbouncer_auth` 函数用于连接池的 Auth Query，仅超级用户可本地访问。

默认模板中创建了`file_fdw`，并添加了一个名为 `fs` 的`foreign server`，基于此提供了几张外部表用于展示 Patroni 集群信息与配置，以及 Pgbackrest 备份信息，仅监控用户可以访问。

现在，`/pg/conf` 将收拢 Postgres，Patroni，Pgbouncer，pgbackrest，Haproxy，VipManager 的配置文件，创建快捷软链，便于集中访问与调整。

现在，`/pg/log` 将收拢 Postgres，Patroni，Pgbouncer，pgbackrest 的日志，便于集中访问与调整。

PostGIS，TimescaleDB，Citus 的软件包从 `pg_packages` 移动到 `pg_extensions`，这样当某个操作系统发行版（例如 EL9）缺少相关插件时，用户只需要修改 `pg_extensions` 变量即可。

### Patroni

Patroni 现在可以通过 `pg_rpo` 与 `pg_rto` 参数，控制 Failover 触发的条件，让用户有机会精确权衡可用性与一致性的具体阈值。当然，`crit.yml` 模板仍然会强制使用 `pg_rpo = 0` 确保数据 0 丢失。

Patroni 所有不安全的 API （例如重启集群，Failover）现在都限制了访问 IP 来源，您只能从管理节点执行此操作。但常规的信息查询，健康检查 API 仍然不受影响。此外，Patroni 现在拥有一组独立的管理用户名与密码参数，您必须使用 HTTP BASIC AUTH 指明用户名密码才可以调用不安全的 API。

Patroni 现在可以对 REST API 启用 SSL，默认不启用，因为健康检查是一个很频繁的操作。

现在，一个专用的 `pg_id` 角色将用于收集数据库节点的基本信息（CPU，内存，磁盘等），Patroni 标签中添加了机器配置规格的信息，可直观浏览集群规格。

现在 Patroni 的配置模板收敛至 `oltp` , `olap`, `crit`, `tiny` 四种，每一种根据经验调优规则，自动适配从 1 核到几百核几百 GB 内存的机型。

### Pgbouncer

在 Pgbouncer 连接池上，SSL 也得到了支持。

v2 允许用户通过 `auth_query` 的方式，对于 Pgbouncer 配置中不存在的用户，自动从 PostgreSQL 数据库中查询并进行认证。

提供了新的快捷命令 `pgb-route`，用于在故障或迁移时快速切换 Pgbouncer 的目标流量。

Pgbouncer 现在默认使用 session pooling 模式，以提高应用兼容性。

### Pgbackrest

v2 新增了 PGBACKREST 支持，默认在集群主节点本地创建一个备份仓库，用于存储归档与冷备份。

默认情况下，PGBACKREST 将在集群的所有实例上初始化一个仓库，但仅使用主库上的仓库用于 WAL 归档与基础备份。您可以通过 `pgbackrest_repo` 参数，使用专用的备份服务器或 S3 兼容服务作为集中的冷备份存储仓库。

Pigsty 添加了一系列开箱即用的配置与快捷命令，能让您自动回复到过去一段时间的任意时间点。

### Promtail

现在您可以指定 Postgres，Pgbouncer，Pgbackrest，Patroni 的日志位置，默认值收拢至 `/pg/log/<p*>`。Promtail 与其他日志相关的命令和快捷方式会自动适配这些日志位置。

### Makefile

添加了自动构建相关的快捷方式。

添加了写入心跳记录，健康检查的快捷方式，用于测试 PITR。

添加了 Vagrant 模板管理的快捷方式

### Deploy

添加了 AWS 的 Terraform 4 节点部署模板。

添加了几种新的 Vagrant 模板，可以测试 EL7，8，9 的部署，并自动构建对应平台的离线软件包。

添加了新的 `bootstrap` 脚本，替代原有的 `download` 与 `configure` 的部分功能。该脚本负责下载软件包，配置本地 Repo，并最终确保本机 Ansible 可用。现有 `configure` 脚本现在只负责监测当前环境，生成对应的 `pigsty.yml` 配置文件。

### Packages

现在 Pigsty 的源码包与离线软件包将带有版本号，离线软件包还将带有操作系统平台标识（el7.x86_64，el8.x86_64，el9.x86_64）。以便在未来兼容其他架构（arm）与操作系统发型版（ubuntu）。

- PostgreSQL 14.5 / PostgreSQL 15.0

- Patroni 2.1.4

- Pgbouncer 1.17

- HAProxy 2.6.6

- PostGIS 3.3

- Citus 11.1：彻底开源，带有完整的分片调整功能。

- TimescaleDB 2.8

- Prometheus 2.39

- Loki & Promtail 2.6.1

- Grafana 9.2.3

- Node Exporter 1.4

- Consul v13.3

- ETCD 3.5.5

### Misc

现在 Pigsty 将使用带有官方签名的 Echarts Grafana 面板，支持最新的 Echarts 5 与 Echarts GL。

如果您有任何想法，需求，功能建议，欢迎在 Github 提 <https://github.com/Vonng/pigsty/issues> 或加入 Pigsty 交流群讨论。

---

发布版本：[微信公众号](https://mp.weixin.qq.com/s/g-ZPWqBwjzaxZKxyjVmFig)
