---
title: 为什么拒绝生产 Docker 跑库与 K8s 大辩论
linkTitle: 拒绝生产容器跑库
description: 生产数据库禁用容器七宗罪、数据库进 K8s 正反交锋及 Linux 原生编排最短故障域。
weight: 160
icon: fa-solid fa-ban
---

容器与 Kubernetes 天生为无状态的“牲畜”进程设计，而生产关系数据库是最忌讳抽象泄漏的有状态“宠物”。剥离云原生营销滤镜，贴近裸 Linux 与本地 NVMe 配合声明式 IaC，才是兼顾性能与可靠性的最短故障链路。

## 一、为什么拒绝用 Docker 跑生产数据库 {#no-docker-for-db}

### 为何 Docker 小版本升级会让索引报废？ {#docker-glibc-index-corruption}

Docker 官方 Postgres 镜像仅维护最近两个 Debian 版本，未锁死系统后缀的 `postgres:17.6` 升至 `17.7` 会被静默切到 `glibc 2.41` 新底座，原地拉起旧库将直接击穿 B-Tree 排序不变量，引发索引报废与静默损坏。所谓下载十亿次的“官方镜像”并非 PG 社区出品，只是缺位 DBA 常识的简陋脚本封装，仅适合开发测试。

- [原地报废：不要在生产环境用Docker跑PostgreSQL！ · 到底是怎么回事](/db/no-docker-pg/#到底是怎么回事)
- [原地报废：不要在生产环境用Docker跑PostgreSQL！ · 官方不等于靠谱](/db/no-docker-pg/#官方不等于靠谱)

### 如何从根源斩断 glibc 升级毁索引的祸根？ {#pg17-builtin-locale}

传统 PostgreSQL 默认耦合宿主系统的 `glibc` 执行字符串比较，发行版升级带来的排序规则漂移令跨系统物理流复制与原地升级如同拆盲盒。自 PG 17 起，生产初始化应强制指定 `--locale-provider=builtin --builtin-locale=C.UTF-8` 彻底斩断系统库依赖；确需自然语种排序时，在列或 SQL 级按需显式调用 `ICU` 即可永久免疫。

- [原地报废：不要在生产环境用Docker跑PostgreSQL！ · 为什么排序规则很重要](/db/no-docker-pg/#为什么排序规则很重要)

### 容器化跑生产库会引入哪些致命可靠性陷阱？ {#docker-stateful-mismatch}

容器专为随用随毁的无状态进程而生，有状态库打洞挂载本地卷后既丢掉了迁移弹性，又凭空背上 `dockerd` 崩溃、默认 64MB 共享内存上限与误写 OverlayFS 等复合故障点。更致命的是 PID 命名空间隔离屏蔽了实例互斥锁检测，若缺乏严密外部 Fencing，极易在宿主机与容器间对同一目录拉起双实例，瞬间将底层数据文件彻底烤糊。

- [容器化数据库是个好主意吗？ · Docker解决什么问题？](/db/pg-in-docker/#docker解决什么问题)
- [容器化数据库是个好主意吗？ · 隔离性](/db/pg-in-docker/#隔离性)
- [原地报废：不要在生产环境用Docker跑PostgreSQL！ · 生产数据库不宜使用容器](/db/no-docker-pg/#生产数据库不宜使用容器)

### 为何贪图初始化便利会毁掉数据库日常运维？ {#container-day2-operations}

生产数据库初始化极低频而连续服役长达数年，真实成本全在 Day2 日常运维。容器粗暴割裂了包管理与监控语义：裸机一条命令无感装扩展，容器却逼你重打镜像重启实例，切主后动态扩展还会凭空丢失；流式 `COPY` 与物理备份被迫套上繁琐的 `docker exec`，原地大版本升级与多阶段拉起 TB 级从库更会遭遇剧烈的单进程抽象泄漏。

- [容器化数据库是个好主意吗？ · Day2 Operation](/db/pg-in-docker/#day2-operation)

### “容器跑库几年没出事”为何只是幸存者偏差？ {#container-survivor-bias}

草台班子凭运气裸奔几年不出事很常见，拿顺风局在线时长当安全证据纯属幸存者偏差——严肃基建只认极端故障下的 RTO 与 RPO 兜底指标。锁死旧镜像不升级只是苟且，保持常规小版本更新并借逻辑复制蓝绿演进才是正道。除开发沙箱、可重建缓存或公有云超卖混部外，丢数即要命的核心 OLTP 库离裸 Linux 硬件越近越可靠。

- [原地报废：不要在生产环境用Docker跑PostgreSQL！ · FAQ](/db/no-docker-pg/#faq)
- [容器化数据库是个好主意吗？ · 总结](/db/pg-in-docker/#总结)

## 二、数据库该不该进 K8s：架构祛魅与正反交锋 {#db-in-k8s-debate}

### OLTP 库进 K8s 为何陷入存储双输？ {#k8s-pet-vs-cattle}

K8s 的灵魂是把无状态应用当可随时销毁的“牲畜”调度，而重度吃 IO 的 OLTP 库却是需精心呵护的“宠物”，强扭必然双输：挂网络云盘搞存算分离，延迟与吞吐较本地 NVMe 差出数量级；用 `LocalhostPV` 绑死本地盘，又彻底废掉跨机编排弹性，反让有状态包袱拖垮集群恢复（如滴滴故障因有状态组件拖延 12 小时才恢复）。

- [数据库应该放入K8S里吗？ · 双输的选择](/db/db-in-k8s/#双输的选择)

### 数据库进 K8s 为何违背分层并引爆排障复杂度？ {#k8s-layer-inversion-complexity}

数据库是比 PaaS 层 K8s 更底层的状态基石，交由 K8s 自举托管极易引发循环依赖雪崩（阿里云与滴滴大宕机皆是明证），多租户还扩大了攻击面——BrokenSesame 漏洞便从 PG 容器逃逸接管了整个 K8s API。更致命的是“智力功率不可累加定律”：单科 DBA 加单科 K8s 运维也解不开叠加 CNI、CSI 后的状态空间爆炸。

- [数据库应该放入K8S里吗？ · 利弊的权衡](/db/db-in-k8s/#利弊的权衡)

### 支持数据库进 K8s 的正方有哪些核心技术论据？ {#k8s-counterpoint-operator}

在本站正方争鸣文中，Sealos 创始人 fanux 主张 K8s Operator（如 KubeBlocks）能以 24 小时状态调谐取代“穿孔纸带式”的 Ansible 脚本，借云操作系统发行版两条命令屏蔽拼装门槛，并用 `OpenEBS` 本地裸盘配多副本控制器兼顾性能与自愈。但我的判断不变：封装只能藏住复杂度却无法消灭它，凌晨三点抽象泄漏时终归要连本带利偿还。

- [没错，数据库确实应该放入 K8s 里！ · 数据库 on k8s：专业能力的普及化](/db/database-in-k8s-counterpoint/#数据库-on-k8s专业能力的普及化)
- [没错，数据库确实应该放入 K8s 里！ · 第一：建设这套系统的复杂度](/db/database-in-k8s-counterpoint/#第一建设这套系统的复杂度)
- [没错，数据库确实应该放入 K8s 里！ · 性能](/db/database-in-k8s-counterpoint/#性能)

### 万物皆上 K8s 是分工演进还是简历驱动杂耍？ {#k8s-resume-driven-vs-economics}

正方 fanux 认为控制器研发能以高固定成本换极低边际人力（半人管 30 机 3000 容器），阻力源于传统运维保饭碗。但我看到的真相恰恰相反：连 K8s 联合创始人 Tim Hockin 都警告复杂性反噬，DHH 下云更果断弃用 K8s；现代裸机 PG 足以撑大多数公司干到上市，所谓云原生狂热多是老板攀比叠加工程师堆 YAML 刷简历，声望归个人、账单归雇主。

- [没错，数据库确实应该放入 K8s 里！ · 不脱离实际场景去否定和肯定](/db/database-in-k8s-counterpoint/#不脱离实际场景去否定和肯定)
- [数据库应该放入K8S里吗？ · 云原生狂热](/db/db-in-k8s/#云原生狂热)

### 普通企业该用什么方案替代 K8s 管好数据库？ {#bare-metal-iac-alternative}

公有云把数据库塞进 K8s 是为了超卖碎片资源，跌破 SLA 也只赔 25% 代金券；普通企业则应压低水位换 Day2 稳定。在网络存储超越本地 NVMe 前，裸 Linux 或虚拟机配 Ansible 声明式 IaC（如开源本地 RDS 发行版 Pigsty）才是正道——影视飓风龚锐团队弃用 Docker 与云 RDS 后，靠本地双机虚拟化加 Pigsty 无专职 DBA 便跑出了 99.99% 可用性与零丢数。

- [数据库应该放入K8S里吗？ · 明智地决策](/db/db-in-k8s/#明智地决策)
- [影视飓风达芬奇千万级数据库演化及实践 · 2024 年 1 月 - 高可用集群](/db/davinci-database/#2024-年-1-月---高可用集群)
