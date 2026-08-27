---
title: "Dify 被重复骑脸羞辱：我太难了！"
date: 2025-03-27
authors: [vonng]
summary: >
  丽珠医药的换 Logo PR 从天而降。被 DeepSeek 一体机厂商白嫖还没完，又有人飞龙骑脸开大羞辱，Dify 真的太难了！
tags: [AI, 开源, 技术评论]
---

今天 Dify 的 GitHub 仓库上演了一出魔幻现实大戏。Dify 开源社区好好地维护着自己的仓库，没想到忽然收到了一个疑似来自丽珠医药的 PR（而且不止一个，接连两个！），手起刀落就把 Dify 的 Logo 给换了。

为什么要换别人的 Logo 呢？《[警惕，Dify 成为 DeepSeek 开源最大受害主体](https://mp.weixin.qq.com/s?__biz=MzU2NjY1ODk1Ng==&mid=2247484447&idx=1&sn=d59104d3c20e7666d988393a268616c3&scene=21#wechat_redirect)》这篇文章里就提醒了大家：有些「国产 DeepSeek 一体机」悄悄地把 Dify 拿回去改 UI、藏版权、抹 Logo，最后打个包装就说自己「自研」。这种「借壳上市」的花招在国内并不罕见（比如几百款「国产数据库」有很多都改自 PG），只不过 Dify 这波被白嫖得有点太狠了。

![Deng Gao 展示丽珠医药替换 Dify Logo 的 PR](logo-pr.webp)

但白嫖归白嫖，自己偷偷装个逼、吹牛说自研也就算了，给人上来飞龙骑脸，一个 PR 就要把人家的 Logo 换掉，这么赤裸裸的当面羞辱是不是有点太过分了？这就跟一个人抄了别人的作品说是自己的，然后还给原作者发邮件要求他把署名改成自己一样无耻啊。

![PR #16640 同时修改 Logo、上传证书和私钥并把默认语言改为中文](pr-16640-changes.webp)

不仅换 Logo，还要上传证书、私钥，又把默认语言改成中文，哈哈。

让人哭笑不得的是，这个 PR #16640[^1] 里还直接把证书和私钥都提交上了！这种操作一看就是妥妥的草台班子。

![PR 提交者的 GitHub 主页与仓库列表](submitter-profile.webp)

按照最善意的解释，可能是对 GitHub 不熟练，傻傻分不清「同步上游」和「贡献上游」——本来想拉取最新的上游更新，结果点成了把自己的魔改发布提交给上游。

![Dify 官方在 PR #16640 下提醒商业授权要求](license-warning.webp)

面对三天前的这个 PR，还可以理解为不小心与失误，Dify 官方留言也只是提醒警告了一下。结果昨天，这帮人又提交了一次 PR #16819[^2]。

![PR #16819 再次替换 Dify Logo](pr-16819-logo.webp)

天天飞龙骑脸，到底是故意的还是不小心，可就不好说了。

![「你逝故意的还逝不小心」熊猫头表情包](intentional-or-accidental.webp)

这下可给 Dify 恶心坏了，直接发律师函了。

律师函里说得很清楚：Dify 的开源协议在 Apache License 2.0 基础上附加了限制。未经书面授权，不得用 Dify 源码运营类似 Dify 服务版的多租户 SaaS，也不得移除或修改 Dify 控制台中的 Logo 与版权信息。律师函据此要求赔礼道歉与赔偿。

![GitHub 评论区附上的 Dify 律师函](legal-notice.webp)

![Dify 律师函第一页](legal-letter-1.webp)

![Dify 律师函第二页](legal-letter-2.webp)

当然，Dify 的开源许可证里写得很清楚。至少从 [2023 年 7 月 28 日的变更](https://github.com/langgenius/dify/commit/c98311b325a4)开始，Dify 就在 `LICENSE` 文件中显式声明了两条限制：未经书面授权，不得用 Dify 源码运营类似 Dify 服务版的多租户 SaaS；不得移除或修改 Dify 控制台中的 Logo 与版权信息。

![Dify 开源许可证中的 SaaS 与 Logo 限制条款](license-terms.webp)

那么，收函的是谁呢？用 Google 搜一下这个 Logo，或者直接打开 PR 里证书目录的域名，就能看到丽珠集团的大名。公开的律师函里也直接写明，涉嫌侵权的是「丽珠医药集团股份有限公司」。

![丽珠医药官网及其 Logo](livzon-website.webp)

像这种其他领域的公司，自己修改 Logo 内部用用可能也就是偷个名；更可恶的其实是那些「DeepSeek 一体机」厂商，直接把人家的开源项目改名换皮，当成自己的去卖。在《[警惕，Dify 成为 DeepSeek 开源最大受害主体](https://mp.weixin.qq.com/s?__biz=MzU2NjY1ODk1Ng==&mid=2247484447&idx=1&sn=d59104d3c20e7666d988393a268616c3&scene=21#wechat_redirect)》这篇文章里已经有人说过了。

---

那么，正确的姿势是什么？当然就是大大方方地直接用 Dify 原版呗！广告时间：开源免费「企业级」Dify 自建，请认准 Pigsty。

![Dify Docker Compose 的服务与存储拓扑](dify-architecture.webp)

一套可靠的 Dify 部署，核心是它使用的 PostgreSQL 数据库。向量数据库可以选择装了 pgvector 的 PG，从而省掉一个组件；Redis 纯粹是缓存。只要解决好 PG 的备份、恢复、PITR、高可用与监控，就能解决绝大多数 Dify 的问题。

![Pigsty 的 Dify 自建部署文档](pigsty-dify.webp)

而 Pigsty 能为你解决 PG、Redis、对象存储、Nginx，甚至 HTTPS 和域名的问题。一台服务器，几行命令，就可以在本地拉起一套不要钱、同时又足够可靠的 Dify，详情请参考 [Pigsty 的 Dify 部署文档](https://pigsty.cc/docs/app/dify/)。

当然，这是原汁原味的纯种开源 Dify，除了使用更可靠的外部 PostgreSQL 数据库之外，没有任何魔改，绝对没有修改 Logo 当自研的把戏——这才是开源应该有的样子。

最后，我要对 Dify 愿意开源这么好的 AI 工作流编排软件表示敬意，同时对换皮魔改 Dify（以及其他开源项目，比如 PG）的小偷们表示鄙视与唾弃。

[^1]: [langgenius/dify PR #16640](https://github.com/langgenius/dify/pull/16640/files)
[^2]: [langgenius/dify PR #16819](https://github.com/langgenius/dify/pull/16819/files)
