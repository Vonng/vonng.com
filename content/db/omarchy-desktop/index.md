---
title: "Omarchy：桌面 Linux 发行版有救了吗？"
date: 2026-08-24
authors: [vonng]
summary: >
  装了 Omarchy，然后又卸载了。Why？谁适合？谁不适合？Linux 桌面发行版还有出路吗？
tags: [Linux, Omarchy, 操作系统]
---

> [微信公众号](https://mp.weixin.qq.com/s/eRa3tnzV9WBuGEBgtbCDVQ)

最近 X 时间线上铺天盖地都是 Omarchy 的消息——这是 DHH 搞的一个 Linux 桌面发行版。这两天也传到中文世界里了，漫山遍野，到处都是。

老冯之前翻译过 DHH 的整个[下云流程](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247485760&idx=1&sn=97096da1077a4fbb4c43452a3c4983c7&scene=21#wechat_redirect)，也经常看他的博客，算是见证了 Omarchy 的诞生。但我确实没想到，这次 4.0 版本发布能产生这么大的反响。

正好手头有一台老笔记本——2018 年的 Intel MacBook Pro，于是装了 Omarchy 玩了几天。

结论先放这儿：**这是一个品味在线、很不错的操作系统，但我最后还是把它换回了 Ubuntu 26。原因也简单：桌面体验难以替代 macOS，服务器的便利程度又难以取代 Ubuntu 的位置。两头不靠，这就有点尴尬了。**

**但实话说，我是举双手支持生态里多出这样一个玩家与选项。**

![装有 Omarchy 的 2018 款 Intel MacBook Pro](featured.webp)

本文 AI 含量：**10%**

## Omarchy 好在哪

老冯觉得 Omarchy 有一个特别好的点：**它可以在老的 Intel MacBook 上跑起来**。而且这个安装流程非常丝滑，不会有以前用 T2 Linux 安装时遇到的各种键盘失灵、USB Wi-Fi 驱动失灵、USB 网卡失灵之类的烂事烂活。

这一下子就盘活了大量老旧 Mac，简直是让它们焕发新生。因为这些老的 Intel Mac 已经脱离 macOS 的支持生命周期了——你要么将就着用老系统，很多新软件都不支持了；要么就只能让它吃灰，很尴尬。

以前 T2 Linux 项目可以在 Intel Mac 上面跑 Debian、Ubuntu 这样的系统，反正也能用，用得也还可以。但你总觉得这个桌面离 macOS 的体验差了很多意思。Omarchy 虽然也达不到 macOS 的水准，但至少比 Ubuntu 的桌面要好多了。

![T2 Linux 为配备 T2 芯片的 Apple 设备提供 Linux 支持](t2-linux.webp)

![T2 Linux 支持的 Ubuntu、Fedora 与 Arch Linux 发行版](distro-support.webp)

当然，也少不了一些人的刻薄讽刺嘲笑，说这就是「DHH 的 dotfiles 配置文件大合集」。这话还是有点太贬低人家了——里面确实有不少定制的匠心在。

但反过来，有些粉丝把它吹成「为 AI 而生的 Agent 原生操作系统」，那也太离谱了——把 Codex、Claude Code、OpenCode 打个包这种事儿（也没预装），老冯[年前就干了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247490846&idx=1&sn=1083f1f55a22ac88e3aab24e0907b102&scene=21#wechat_redirect)。打个包装个包就管自己叫 AI 优先的操作系统，那实在是 Bullshit。

![Omarchy 的默认桌面与壁纸](wallpaper.webp)

抛开这些噪音看，Omarchy 的桌面使用体验跟 macOS 确实还有不小的差距，但这可能已经是 Linux 发行版里面的品味巅峰了。它至少是我看到的，**Linux 生态里唯一一个有精气神去追平 macOS 体验的项目**。这真的很不得了，非常有志气。DHH 直接对各路 Linux 伪君子口吐芬芳，老冯是打心底里欣赏和佩服的。

![DHH 回应对 Omarchy 的嘲讽](dhh-tweet.webp)

正所谓，知之者不如好之者，好之者不如乐之者。也就是 DHH 这种已经财富自由、又真心热爱计算机的中登，才能搞出这种事情来。想做好 Linux 桌面，需要的正是这种集品味、技术、资源、影响力于一身，并且**真的热爱它**的人，才能成事。

## 关于各种 Linux

作为一个 PostgreSQL 发行版的作者，老冯对 Linux 发行版可以说是如数家珍。

因为我自己就要提供 16 个 Linux 发行版上 PostgreSQL 和 400 多个扩展的打包构建与分发，维护着将近十几万个包。虽说做的是 PG 发行版，某种意义上也算半个 Linux 发行版作者了。

![Pigsty 支持的 Linux 发行版与 PostgreSQL 版本矩阵](distro-matrix.webp)

各种各样的发行版我基本都尝试过：Red Hat 系（CentOS、Rocky、Alma、Oracle Linux）、Debian、Ubuntu 全家桶、Fedora、Arch、NixOS、Mint、Kali，还有麒麟、统信、欧拉……

但折腾了这么多操作系统之后，老冯现在已经返璞归真了——主力基本就是 Debian 和 Ubuntu，偶尔用用 EL。

简单、可靠、好用，这就是硬道理。跑在服务器上就挺好，带一个凑合能用的 UI 就行了。因为你再怎么折腾桌面，也折腾不过 macOS。至少我觉得这几年是折腾不过的——但 Omarchy 至少带来了一个希望。你要问我用什么，那就看世界上用得最多的 Linux 是哪个——不就是 Ubuntu 吗？那还折腾什么劲儿呢。

![Ubuntu 26.04 LTS Resolute Raccoon](ubuntu-raccoon.webp)

## 关于 Ubuntu

Ubuntu 在海外有着压倒性的主导地位。这一点国内的开发者可能没有太大感触，但看一眼 Stack Overflow 的开发者调查就明白了，它是很明显的绝对主力。

Ubuntu 是衍生自 Debian 的。Debian 也是我很喜欢的一个操作系统，因为它跟 PostgreSQL 一样，都是那种开源原教旨的、很纯粹的开源项目。如果你要跑 Proxmox 虚拟机，Debian 就很合适；但如果你要跑 AI 相关的东西，装个 NVIDIA 显卡驱动之类的，那可能就只能选择 Ubuntu。

至于 Enterprise Linux（EL 系列），国内 CentOS 系列用得实在太多了，所以这块确实也比较普遍，我接触得也很多。但你要让我自己用的话，我可能还是更喜欢 Ubuntu 多一点——**因为它可能是唯一一个桌面和服务端都做得还不错的系统**，而且普及率、使用率又很高。

桌面市场终究没打赢 Windows，但 Ubuntu 在服务器和云上赢得非常彻底：AWS、Azure 上的 Linux 实例大量跑的是它，WSL 的默认发行版也是它。

## 关于 Debian

另一个我比较喜欢的操作系统就是 Debian，也就是 Ubuntu 的上游，很多东西都是共通的。

我觉得它没有 Ubuntu 那样开箱即用，但是它足够纯粹。如果你是做分发或者开源项目的，大概率基础镜像都会优先选择 Debian。

一个很扎实的操作系统，稳如老狗。

## 所以，到底该用什么

马上要开学了，很多朋友要买电脑。听老冯一句劝：**别折腾什么桌面 Linux 了，桌面直接 macOS 一把梭就完了。**它起码提供了一个 BSD-style 的终端环境，大部分东西跟 Linux 也是共通的，而且做到了极致的桌面体验，加上相当不错的命令行体验。

想要极致的桌面 AI 原生体验，选 macOS 没有错，因为这些开发者也几乎都是自己用 macOS，并将 macOS 作为第一桌面优先级来对待的。想折腾，弄台 Linux 服务器就行——云服务器，或者一台小型迷你 PC，你想怎么折腾都行。但折腾桌面这种事，说实话我已经过了那个年纪了。

而且肌肉记忆是很不容易迁移的。举个具体的例子，我在 macOS 上有一个改键软件，把 Caps Lock 改成了一个非常强大的 Hyper 键。有了这个键，我可以手指不离键盘完成几乎所有操作——模拟鼠标、滚动、滑动、切换窗口、快捷启动应用，操作效率基本比正常翻了十倍。

到 Linux 上，我知道应该也有类似的改键工具，但我实在懒得去折腾。一换到 Linux，我的输入和操作效率立刻大幅下降；而且我真不想记两套快捷键体系，肌肉记忆已经长在那儿了，实在不想去换。折腾来折腾去，没有实际产出。

工作上也是同样的道理。老冯做 Pigsty，跑数据库和可观测性全家桶这一套东西，Ubuntu 至少能用 `.deb` 包整个跑起来；要是换成 Arch Linux，难道还要我专门去打一套 `pacman` 包？我是真懒得折腾。

## 它让我想起了当年的 Ubuntu

其实 DHH 的 Omarchy，和当初的 Ubuntu 有点像。Ubuntu 当年也是一个很好的开源社区操作系统，背后同样站着一个大富翁——南非人 Mark Shuttleworth（马克·沙特尔沃思）。

![Ubuntu 创始人 Mark Shuttleworth](shuttleworth.webp)

他当时觉得 Debian 技术上很扎实，但对普通人太不友好：安装难，发布周期还不固定，有时候隔好几年才出一版。他的想法很简单：拿 Debian 当底子，把它打磨成普通人装完就能用的桌面系统，**固定每 6 个月发一版，而且永远免费**。

他甚至还免费给人邮寄安装光盘——那个项目叫 **ShipIt**，全球包邮，一分钱不收，你去申请他就给你寄一张。很多人当年就是这样第一次摸到 Linux 的，很有意思。

当然，现在 Ubuntu 有了商业公司 Canonical，用户也开始有些微词了，比如强推自己的包管理器 Snap 之类的，确实感觉没以前那么纯粹了。所以如果 Omarchy 能做得足够好，那真的是一件大好事，老冯非常支持。但你要说让我现在就换过去，我肯定还是选 Ubuntu。

不过话说回来——如果哪天 Omarchy 真的能在 Linux 上实现媲美 macOS 的同等体验和生态，那老冯肯定二话不说，直接就换了。

## 附录：Stack Overflow 开发者调研

老冯昨天让 Codex 去把 Stack Overflow 过去十几年的开发者调研数据爬了下来，主要是分析数据库的变迁。我们正好也让它做了一个操作系统变迁的分析报告，顺便就发在这里了，有兴趣可以看一看。

![Stack Overflow Linux 桌面调研报告概览](survey-report.webp)

![桌面操作系统的早期分流](os-evolution.webp)

![原生 Linux、WSL 与重叠使用情况](linux-wsl.webp)

![Ubuntu 的主导地位与后期分化](ubuntu-split.webp)

![工作环境与个人环境中的操作系统](work-profile.webp)

![各国的 Linux 与 WSL 使用情况](country-usage.webp)

![操作系统家族与 Linux 发行版的关联](os-correlation.webp)
