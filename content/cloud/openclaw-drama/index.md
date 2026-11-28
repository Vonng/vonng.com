---
title: 'OpenClaw 小龙虾翻车：不测就发的后果'
date: 2026-03-25
authors: [vonng]
summary: >
  OpenClaw v2026.3.22 发布到 npm 时漏掉了控制台前端和相关构建资源。
  这次翻车暴露出的，不只是一个打包事故，而是发布流程里缺少最基本的安装后验证。
tags: [AI, Agent, 开源]
ai: true
aliases: ["/ai/openclaw-drama/"]
---
昨晚，OpenClaw 发布了新版本 `v2026.3.22`。结果 npm 包里把控制台前端漏掉了，全球用户升级完打开浏览器，直接 `503`。

> [!SOCIAL] 小众软件
>
> 注意草台班子 OpenClaw 在发布 npm 包时遗漏了 `dist/control-ui/` 目录，导致升级后没有控制台了。
>
> 太离谱了。临时修复方式：*（附图为从源码克隆并手动构建 UI 的临时步骤，见下文 GitHub Issue）*
{avatar="avatar-appinn.webp" date="2026-03-23 22:03" platform="weibo"}

> [!SOCIAL] 小众软件
>
> 别自己修了！它大概要下载好几百MB的文件（也可能上GB），我放弃了。等更新吧。别用控制台了。
{avatar="avatar-appinn.webp" date="2026-03-23 22:39" platform="weibo"}

> [!SOCIAL] 夹头推土机
>
> 这有啥离谱的🐶全是ai写的代码，人都看不懂，出点问题只能怪ai🐶。也提醒一下想开了程序员的老板们，以后出了问题你们只能和ai掰扯了
{avatar="avatar-jiatoutuituji.webp" date="2026-03-23 23:38" platform="weibo"}

> [!SOCIAL] 睿爸201211
>
> 可以发布个修复skill😁😁
{avatar="avatar-ruiba.webp" date="2026-03-23 22:23" platform="weibo"}

> [!SOCIAL] 你就是猴子请来的救兵吗
>
> 那些发openclaw新版介绍的看来是连安装都没有😂
{avatar="avatar-houzi.webp" date="2026-03-24 00:35" platform="weibo"}

> [!SOCIAL] 千问
>
> 太惨了，升级完发现没界面，这波确实离谱。好在有你给的这个手动构建复制的方案，不然真不知道怎么修，辛苦辛苦！
{avatar="avatar-qwen.webp" date="2026-03-23 22:12" platform="weibo"}

> [!SOCIAL] Longw长木
>
> MLGB我折腾几个晚上怎么都访问不了控制台，我一度怀疑是我哪里配置错了，来回卸载安装。
{avatar="avatar-longw.webp" date="2026-03-24 08:10" platform="weibo"}

## 一、怎么回事

`v2026.3.22` 是个大版本。插件市场 ClawHub 上线，浏览器工具链重构，一堆安全加固，Release Notes 里几十条 changelog，看起来挺热闹。然后用户一升级，控制台没了。

![npm 包里缺失控制台前端目录](missing-control-ui.webp)

发到 npm 的包里，`dist/control-ui/` 整个目录都不见了。上个版本 `v2026.3.13` 还是好的，这个版本直接丢了。

更骚的是，报错信息让你跑 `pnpm ui:build` 自己编译前端，但 `scripts/` 目录也没打进包里。官方给你指了条死路。

同一个版本里，WhatsApp 集成也一起炸了。模块已经拆到独立包 `@openclaw/whatsapp`，但这个包压根还没发到 npm 上。两个打包事故叠在一起，npm 用户当场团灭。Docker 没事，Git 没事，npm 全军覆没。

## 二、不是第一次了

翻 GitHub Issues 会发现，OpenClaw 在 npm 这条路上翻车已经不是头一回了。

一月的 `v2026.1.29`，UI 资源文件其实在包里，但路径解析逻辑默认 `process.argv[1]` 指向 `dist/` 内部；而 npm 全局安装的入口文件在包根目录，于是照样找不到。资源明明在那里，代码却看不见，等于没有。

二月，有人报 `scripts/ui.js` 不在 npm 包里，`pnpm ui:build` 根本跑不起来。

三月，直接把整个前端产物丢了。

三个月，同一条路，三个坑。说明什么？

**npm publish 之后，没有任何自动化验证。**

没人，也没有 CI，去检查一句最关键的话：**“装完以后，到底能不能跑起来？”**

哪怕只是下面这四行脚本，都能把昨晚这次事故拦在门外：

```bash
npm pack
npm install -g ./openclaw-2026.3.22.tgz
openclaw doctor --non-interactive
curl -s http://127.0.0.1:18789 | grep -q '<!DOCTYPE html>'
```

但显然，没人写。

## 三、AI 写代码，但不管发布

微博评论区有条评论很扎眼：

> “这全是 AI 写的代码，人都看不懂，出点问题只能修 AI。也提醒一下想开了程序员的老板们，以后出了问题你们只能和 AI 扯皮了。”

GitHub 上有些 Issue 标着 “Generated via Claude Code agent”，有些 PR 是 Codex 生成的。这件事本身不是问题。我自己 Pigsty `v4.x` 百分之九十九以上的代码，也是 Claude 和 Codex 写的。

但 AI 能帮你写代码，不会替你建流程。

AI 不会主动说“我们该在 publish 前加个冒烟测试”，不会在你拆包的时候提醒你“新包还没发 npm”。**代码层面的 Bug，AI 能写也能修；流程层面的缺失，AI 看不到。**

看到这个事故，我特别有感触。因为就在昨天，我刚发了一个 Pigsty 小版本。这个版本里有个看起来很不起眼的升级：ETCD 从 `3.6.8` 升到 `3.6.9`。Patch 版本，按语义化版本约定，理论上只有 bugfix，不该有兼容问题。结果冒烟测试一跑，集群炸了。

ETCD `3.6.9` 悄悄给 Member List API 加了认证。之前普通用户能直接调的接口，现在要身份验证了。Pigsty 的健康检查和成员管理全部失败。

**这种东西，你看 changelog 看不出来，看 diff 也未必反应得过来。** 只有真装一遍、跑一遍，让所有组件在真实环境里交互一轮，才能把它逮出来。

发现之后，我做了三件事：

- 把 ETCD 回滚到 `3.6.8`
- 在发布版里锁死这个版本
- 在更新说明里写清楚为什么没跟进最新版

之前升级 MinIO 时，我也碰到过类似的坑，处理方式一样：回滚、锁定、记录。

有多高深吗？其实没什么。就是在干净环境里安装、启动、验证；发现问题就回滚；确认无误才放行。很慢，也挺麻烦，一个小版本有时候要折腾好几轮。

但用你软件的人，是拿它跑生产的。你得对得起这份信任。

OpenClaw 这次，如果发布前有人真装一下、启动一下、打开控制台看一眼，整件事就不会发生。

**做基础设施的，装完跑一圈，测试一下，很难吗？**
