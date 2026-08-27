---
title: "某平台CVV泄露：你的信用卡被盗刷了吗？"
date: 2024-10-02
authors: [vonng]
summary: >
  草台班子新高度：某平台曝外卡CVV泄露，出现批量外卡信用卡被盗刷。
tags: [云计算, 安全]
---

这个十一不太平，最近某头部互联网平台曝出特大丑闻，信用卡数据库被人拖库，卡号，有效期，CVV 泄露。有许多信用卡被盗刷的苦主发现共性是都在该平台上绑了 MASTERCARD / VISA 等外卡。

这会给卡主带来重大风险和巨大的麻烦：这玩意泄漏了信用卡能轻易被盗刷，只能联系发卡机构换卡。十一长假很多人都在外面，用卡换卡都很不方便，真的是会给人整活。

![图片](01.webp)

这种离谱的事让人难以置信，让草台班子理论达到了新的高度。与之相比，最近《[阿里云盘灾难级BUG：能看别人照片？](/cloud/aliyun-drive-bug/)》只能算不痛不痒的毛毛雨了。“如果”这是真的，这已经不只是草台班子的问题了，而是违法犯罪了。

国内普通银联信用卡用户可能不太熟悉，刷 VISA / MASTERCARD 信用卡的时候，很多时候是没有 “密码” 的，而是靠卡背面3位 CVV 做校验，类似于密码，一般拿到卡都要记牢并直接遮蔽这个数字的。

同理，支付平台一般是严禁存储 CVV 的 —— 只能在支付的时候用一次，但不允许存储下来。因为按照外卡的玩法是能直接用卡号+有效期+CVV 刷你的卡，所以一旦这三要素同时泄漏，别人就能刷你的钱了。

我听业内人士说过，国内有些相当头部的平台，“快捷支付” 服务CVV 明文是直接存数据库里的。仔细想一下，凭啥快捷支付时在平台上输入个自定义密码就能直接再次用你的信用卡支付了？（注意这里都特指 VISA / MasterCard 等外卡） 。

这次是其中一个爆了，也许还有没爆的，比这个体量还大。像这种事，估计会引发监管铁拳，说不定还会拔出萝卜带出泥，牵动其他这么搞但还没爆雷曝光的平台。

![图片](02.webp)

![图片](03.webp)

[**阿里云盘灾难级BUG：能看别人照片？**](/cloud/aliyun-drive-bug/)

[删库：Google云爆破了大基金的整个云账户](/cloud/gcp-unisuper/)

[全球Windows蓝屏：甲乙双方都是草台班子](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488036&idx=1&sn=7bbcc3e8979a5f97a519a7a1684caa06&scene=21#wechat_redirect "全球Windows蓝屏：甲乙双方都是草台班子")[](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488215&idx=1&sn=34bedcf01169facd0207200b3e018989&scene=21#wechat_redirect "这次轮到WPS崩了")

[我们能从阿里云史诗级故障中学到什么](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486468&idx=1&sn=7fead2b49f12bc2a2a94aae942403c22&scene=21#wechat_redirect "我们能从阿里云史诗级故障中学到什么")

[腾讯云：颜面尽失的草台班子](/cloud/tencent-disgrace/)

[黑暗森林：打爆AWS云账单，只需要S3桶名](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487536&idx=1&sn=0cd598f426de0b617c7f3318aed9bd95&scene=21#wechat_redirect "黑暗森林：打爆AWS云账单，只需要S3桶名")

[我们能从网易云音乐故障中学到什么？](/cloud/netease/)

[GitHub全站故障，又是数据库上翻的车？](/cloud/github-outage/)

[这次轮到WPS崩了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488215&idx=1&sn=34bedcf01169facd0207200b3e018989&scene=21#wechat_redirect "这次轮到WPS崩了")

## [**数据库老司机**](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488417&idx=1&sn=11ac37347fd159a1949da015b2cf57c7&chksm=fe4b267ac93caf6c5a8e1c716642426421007ceb6518553816e13054245edc6cbaed3207a0d0&scene=21#wechat_redirect)，[**云计算泥石流**](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488410&idx=1&sn=e44705fce4221458244e7705258ca254&chksm=fe4b2641c93caf57cc46069b82827da873af95b3e157e7e8d2943977bdd1cbb547d79bc16373&scene=21#wechat_redirect)

![图片](04.webp)

**（这个小助手很懒，请使劲拍打他）**
