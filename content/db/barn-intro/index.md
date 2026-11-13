---
title: "再见 Vagrant，你好 Barn"
date: 2026-11-12
authors: [vonng]
summary: >
  HCP Vagrant 与公共镜像仓库即将关停。老冯用 Go 写了一个 Apache-2.0 开源的本地虚拟机管理工具 Barn：用一份兼容 Ansible 的 YAML 清单拉起固定私网 IP 的多节点 Linux 集群，也能在 Apple Silicon 上按秒克隆原生 macOS 虚拟机，服务数据库研发测试与 AI Agent 沙箱隔离。
tags: [Pigsty, Agent, Linux, 开源]
---

11 月 2 日，HashiCorp 宣布停止维护 [HCP Vagrant 与公共镜像仓库（Vagrant Public Registry）](https://www.hashicorp.com/en/blog/hcp-vagrant-deprecation-important-dates-and-migration-guidance)，并定于今年 12 月 31 日关停服务器。

[![HashiCorp 官方宣布弃用并分阶段关停 HCP Vagrant 公共仓库](vagrant-sunset.webp)](https://www.hashicorp.com/en/blog/hcp-vagrant-deprecation-important-dates-and-migration-guidance)

看到这条消息还是有些感慨。Vagrant 曾经是最好用的本地虚拟机管理工具：写一份声明式清单，就能在 Mac、Linux、Windows 上拉起多台虚拟机。老冯断断续续用了七八年，[Pigsty](https://pigsty.cc/) 最早就是在 Vagrant 拉起的虚拟机里孵化和打磨出来的。

早些年 HashiCorp 那套工具链确实顺手：本地起虚机用 Vagrant，上云编排用 Terraform，服务发现用 Consul，调度用 Nomad，密钥管理用 Vault，不少工程师都是围着这套工具搭工作流的。

转折点在 2023 年。HashiCorp 把开源协议改成 BSL 1.1，随后又卖给 IBM，Vagrant 走下坡路其实是早晚的事：核心插件 [`vagrant-libvirt`](https://github.com/vagrant-libvirt/vagrant-libvirt) 陷入停滞，逼得 [`netlab`](https://blog.ipspace.net/2026/09/sunsetting-vagrant-libvirt/) 等项目在今年秋天放弃支持；Vagrant CLI 停在 [`2.4.9`](https://github.com/hashicorp/vagrant/releases/tag/v2.4.9) 之后**整整 14 个多月没发过新版**，仓库最近三个月只剩一人零星维持，连新版 macOS 上 `vagrant up` 报错的问题也一直拖着没发版。现在连放着大批 `generic/*`、`bento/*` 镜像的公共仓库也要拔网线了。

我和 Pigsty 社区受这件事影响很直接。

跑无状态服务用 Docker 很省心；但要研发、测试一套生产级数据库发行版——涉及多节点 `systemd` 服务编排、Patroni 高可用故障切换、VIP 漂移、Linux 内核参数调优、APT/YUM 仓库同步，以及 `ext4`/`XFS` 独立数据盘挂载——容器代替不了完整内核，手里必须有正经的 Linux 虚拟机。

但这几年每次带新用户或自己拉测试集群，Vagrant 都越来越难伺候：Ruby 环境依赖老出问题，VirtualBox 在 Apple Silicon 上一直别扭，`libvirt` 配置对新手也不友好，如今官方镜像源也要关了。

指望不上别人，干脆自己动手写一个。

HashiCorp 改协议后，Terraform 分叉出了 [OpenTofu](https://opentofu.org/)，Vault 分叉出了 [OpenBao](https://openbao.org/)，唯独 Vagrant 没人接。老冯起初动过直接 Fork 的念头，连名字都想好了，就叫 **OpenWonton**——豆腐、包子、馄饨，刚好凑一桌早点。结果翻开代码一看，十几年的 Ruby 历史包袱太重，修旧房不如直接盖新房。反正连 MinIO 都接过来做成 [Silo](/db/minio-silo-1year/) 了，按自己的实际需求用 Go 重写一个本地虚拟机管理器，反倒更痛快。借用 DHH 那句话：**["We can fix everything!"](/cloud/cloud-exit-2026/)**

## Barn：本地虚拟机的畜棚

于是就有了 **[Barn](https://github.com/pgsty/barn)**（**B**ootstrap **A**nd **R**un **N**odes）——Go 编写、Apache-2.0 协议开源的本地虚拟化管理工具，官网与中英文文档已经上线：**[barn.pgsty.com](https://barn.pgsty.com/zh/)**。

[![Barn 官网首页：多节点 Linux 实验环境与原生 macOS 虚拟机](barn-site.webp)](https://barn.pgsty.com/zh/)

熟悉 Pigsty 的朋友一看名字大概就乐了：**[Pigsty](https://pigsty.cc/)** 是猪圈，**[Silo](https://silo.pgsty.com/)** 是存粮的筒仓，**[PIG](/pg/pig/)** 是猪仔包管理器，**[Oink](/ai/oink-intro/)** 是文档框架，**Barn** 自然就是旁边的畜棚。云原生里常把随时可销毁重建的实例叫“牲畜”（Cattle），Barn 干的就是这活：在你的 MacBook 或 Linux 工作站上，低成本、确定性地养一群 Linux 与原生 macOS 虚拟机。

它的定位很直接：**拿一份兼容 Ansible 的标准 YAML 清单，在本地拉起带固定私网 IP 的多节点 Linux 集群（基于 QEMU + HVF/KVM 硬件加速）；或者在 Apple Silicon Mac 上按秒克隆独立的原生 macOS 虚拟机（基于 `Virtualization.framework`）。**

[![GitHub 开源仓库 pgsty/barn：Apache-2.0 协议、Go 实现与原生 mac-runner](barn-github.webp)](https://github.com/pgsty/barn)

不用装 VirtualBox，也不用折腾 Ruby 插件，装好就能上手：

```bash
# 1. 安装 Barn（macOS 自带签名公证过的原生 Barn.app）
brew install pgsty/infra/barn

# 2. 拉起默认 Linux 节点（或读取当前目录 barn.yml 多节点集群）并连入
barn up && barn ssh

# 3. 在 Apple Silicon 上按秒拉起一台挂载工作目录的独立 macOS 虚拟机
barn mac up dev --share ~/work
```

## 五个工程取舍

Barn 不是把 Vagrant 用 Go 照抄一遍。结合过去几年踩过的坑，我做了五个不一样的取舍：

### 1. 一份 YAML 清单，不再维护两套配置

以前用 Vagrant 跑 Pigsty 沙箱有件烦心事：得先用 Ruby 写一份 `Vagrantfile`，定义几台机器、几核几 G、什么 IP；再去维护一份 Ansible 的 `pigsty.yml` 主机清单，把同样的 IP 和主机名抄一遍。改一个节点，两边都得手动对齐。

在 Barn 里，**没有独立的虚拟机 DSL**。[`barn.yml`](https://barn.pgsty.com/zh/docs/reference/configuration/) 本身就是一份合法的 **Ansible 标准 YAML 主机清单**：

```yaml
all:
  vars:
    admin_ip: 10.10.10.10
    vm_image: d13          # 支持 u22/u24/u26, d12/d13, el8/el9 等别名
    vm_cpu: 4
    vm_mem: 8GiB
    vm_disk: 64
  children:
    pg_meta:
      hosts:
        10.10.10.10: { nodename: meta }
    pg_test:
      hosts:
        10.10.10.11:
          nodename: node-1
          vm_disks:
            - { path: /data, size: 128, fs: auto, persistent: true }
        10.10.10.12:
          nodename: node-2
```

Barn 只读取它关心的 `vm_*` 字段去创建机器（都有默认值，不写也行），Ansible 和 Pigsty 直接拿**同一个文件**去跑剧本（`ansible-playbook -i barn.yml`），不用再两边对账。刚发布的 `1.1.0` 还支持在命令行临时覆盖发行版与架构，直接敲 `barn up -I el9 -A amd64` 就能跑跨系统兼容性测试。

### 2. 全局单部署（`~/.barn`），不留幽灵虚拟机

用 Vagrant 久了，硬盘里很容易攒下十几个早忘了路径的 `.vagrant/` 目录，后台挂着一堆白占内存的虚机；更烦人的是，在 B 目录拉起一台 `10.10.10.10`，经常跟 A 目录忘了关的同 IP 虚机撞车，顺带把 SSH `known_hosts` 搞乱。

Barn 直接去掉了“按目录分项目”的概念——**[One Deployment, No Projects](https://barn.pgsty.com/zh/blog/design/one-deployment-no-projects/)**。所有状态、密钥、缓存镜像和虚拟机磁盘统一收口在 `~/.barn` 下。不管切到哪个目录敲 `barn status`，看到的都是同一套全局环境；真需要隔离第二套环境，显式指定环境变量 `BARN_HOME` 就行。

![Barn CLI 实机输出：全局受控的四节点 Linux 集群、双网卡诊断与双架构静态镜像目录](barn-cli-linux.webp)

### 3. 双网卡解耦：带外管理 + 固定私网 IP

做分布式系统和数据库实验，节点之间必须用固定私网 IP，动态 DHCP 只会添乱。Barn 给每个 Linux 节点配了[双网卡拓扑](https://barn.pgsty.com/zh/blog/design/fixed-ip-two-nics/)：

- **管理 / NAT 网卡**：负责出网访问，并在宿主机回环地址暴露独立的管理 SSH 端口。哪怕在虚机里把内网网卡配坏了，`barn ssh` 照样能像服务器带外管理口（IPMI）一样连进去处理。
- **固定私网网卡**：macOS 基于 `socket_vmnet`，Linux 基于宿主网桥，按清单分配固定私网 IP。

集群拉起时，免密 sudo 的默认管理员账号 `dba`、各节点 `/etc/hosts` 解析，以及**从控制节点（`admin_ip`）到所有工作节点的免密 SSH 互信**都会自动配好，登进控制节点就能直接跑 Ansible。

### 4. 写时复制与防误删保护

基础设施工具最忌讳自作聪明。在 Barn 里，基础镜像只下载缓存一次，新节点通过 `qcow2` 写时复制几秒钟就能拉起。如果不小心从 `barn.yml` 里删掉了一个节点，运行 `barn up` 甚至 `barn recreate` 时，Barn **[不会静默销毁那台机器](https://barn.pgsty.com/zh/blog/design/convergence-without-surprise/)**，而是直接报冲突停下来——删节点必须显式执行 `barn destroy NODE`。标记了 `persistent: true` 的独立数据盘在常规重建中也会保留，免得误删测试数据。

### 5. 静态镜像源：不被在线服务卡脖子

HCP Vagrant 关停提醒了一件事：**基础工具尽量别把命脉绑在一家商业公司的在线服务上。**

Barn 官方提供了涵盖 Ubuntu、Debian、Rocky Linux 等主流发行版在 `amd64` 与 `arm64` 双架构下的精简镜像，但整套镜像源不依赖任何动态后端，直接采用[**纯静态目录清单 + Ed25519 / minisign 签名 + SHA-256 校验**](https://barn.pgsty.com/zh/blog/design/repo-yaml-catalog-json/)。你可以随时把镜像源同步到自己的对象存储（比如 [Silo](https://silo.pgsty.com/)）、内网 Nginx 或任意 CDN 上，也可以用 `barn image import` 导入自制镜像，离线内网照样能转。

## 一台 Mac 劈成三台用：给 AI Agent 配个沙箱

如果你手里有台大内存的 Apple Silicon Mac（比如老冯日常干活的 128GB M5 Max MacBook Pro），Barn 还有一个很实用的功能：**[`barn mac`](https://barn.pgsty.com/zh/docs/start/macos/)**。

[![Barn 官方文档：在 Apple Silicon 上基于 Virtualization.framework 运行原生 macOS 虚拟机](barn-mac-docs.webp)](https://barn.pgsty.com/zh/docs/start/macos/)

发行包里内置了经过 Apple 签名公证的原生 **`Barn.app`**，底层调用苹果的 `Virtualization.framework` 与 **APFS 写时复制（Copy-on-Write）**：基础 `.ipsw` 恢复镜像只需装一次，后面敲一行 `barn mac up`，几秒钟就能克隆出一台干净的 macOS 客机，几乎不占额外磁盘——带原生桌面窗口和剪贴板同步，也自动配好了免密 SSH 与基于 **VirtioFS** 的高速目录共享（`--share ~/work`），用完一句 `barn mac destroy --yes` 直接清掉。

受苹果虚拟化协议限制，一台 Mac 宿主机最多同时运行两台 macOS 虚拟机；算上宿主机自己，**一台大内存 Mac 刚好能拆成 3 台相互隔离的独立 Mac 环境来用**。

有人可能会问：都 2026 年了，为什么还要费劲写一个本地虚拟机管理器？

除了研发测试数据库，老冯日常高强度跑 Coding Agent 时，很快撞上了另一个刚需：**[给 AI Agent 配本地沙箱](/ai/memory-vs-context/)。**

重度用 Claude Code、Codex 的朋友多半纠结过：不开全自动免确认（YOLO 模式），就得一直盯着终端敲回车；开了 YOLO 直接在宿主机上裸跑，万一哪天抽风敲错一行 `rm -rf` 或改乱了系统环境，主力机就得跟着遭殃。要是同时挂三个不同的 Claude 账号，或者跑多个要操作 GUI 的 Agent，它们还会互相污染环境变量、抢窗口焦点、抢鼠标指针。塞进 Docker 容器里也不够用，一碰到 `systemd`、内核模块、嵌套构建或 macOS 原生编译链，Agent 手脚就被捆住了。

算来算去，**按秒克隆、带完整内核、给足 root 权限又有独立桌面的本地虚拟机，反而是最省心的 [Agent 运行环境](/ai/agent-os/)。**

![Barn.app 原生 macOS 27 写时复制克隆与面向 AI Agent 的 --json 结构化输出契约](barn-cli-mac.webp)

所以 Barn 从一开始就把 **[CLI 结构化输出](https://barn.pgsty.com/zh/blog/design/cli-contracts/)** 做好了：主要命令都原生支持 `--json` 与 `--yaml` 输出，配合语义明确的退出码，人敲着顺手，Agent 调起来也省事。把 Agent 关进虚机里就能放心给满权限——让它自己调 `barn up` 拉起三台 Linux 节点跑数据库压测，或者 `barn mac up` 克隆一台干净的 Mac 跑完整构建验收。搞坏了销毁重来也就几秒钟，花的无非是本机闲置的算力与内存。

Vagrant 陪我们走过了基础设施自动化的头十年，是个好工具，但它的时代确实翻篇了。眼下云上机器越来越贵、本地硬件性能过剩，手底下又多了一群需要独立环境的 Coding Agent，本地虚拟化这件老兵器反而更有用武之地了。

Barn 采用 Apache-2.0 协议开源，欢迎拿去折腾：

- **项目官网与文档**：[https://barn.pgsty.com](https://barn.pgsty.com/)
- **GitHub 仓库**：[https://github.com/pgsty/barn](https://github.com/pgsty/barn)
- **快速安装（macOS）**：`brew install pgsty/infra/barn`
