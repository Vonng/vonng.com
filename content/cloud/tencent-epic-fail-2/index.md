---
title: "【腾讯】云计算史诗级二翻车来了"
date: 2024-04-08
authors: [vonng]
summary: >
  腾讯云管控面大故障，阿里云双十一大故障翻版。疑似 Auth 问题 —— 云计算史诗级二故障来了
tags: [云计算, 故障复盘]
---

就在现在，腾讯云管控面挂了。症状几乎和 **[去年双十一阿里云史诗级大故障](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486452&idx=1&sn=29cff4ee30b90483bd0a4f0963876f28&chksm=fe4b3e2fc93cb739af6ce49cffa4fa3d010781190d99d3052b4dbfa87d28c0386f44667e4908&scene=21#wechat_redirect) **一毛一样：CVM 虚拟机，RDS 数据库还可以正常运行，但是管控面，特别是和 Auth 有关的无一幸免。[**堪称阿里云故障翻版**](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486468&idx=1&sn=7fead2b49f12bc2a2a94aae942403c22&chksm=fe4b39dfc93cb0c92e5d4c67241de0519ae6a23ce6f07fe5411b95041accb69e5efb86a38150&scene=21#wechat_redirect)**。**

这篇给阿里云做的的非官方复盘文章《**[我们能从阿里云史诗级故障中学到什么](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486468&idx=1&sn=7fead2b49f12bc2a2a94aae942403c22&chksm=fe4b39dfc93cb0c92e5d4c67241de0519ae6a23ce6f07fe5411b95041accb69e5efb86a38150&scene=21#wechat_redirect)**》，把阿里云三个字改成腾讯云，读起来丝毫没有一点儿违和感。也许是**[降本增笑](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486527&idx=1&sn=8e26f644f2b908fd21c83b81d329155d&chksm=fe4b39e4c93cb0f22271127a154a6ac5c45947b2051b06b7667ee5c203d136b5d2e8f6577b10&scene=21#wechat_redirect)**太狠了，SRE 今年的年终奖又要泡汤了。

**![图片](01.webp)**

我自己还有几台 CVM 虚拟机跑 Demo，也用了[**腾讯云的 CDN**](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247485363&idx=1&sn=8622b25fd2309d4fc969d22964a04129&chksm=fe4b3268c93cbb7efb8757e876574bebf5d615bdd3c4ceb76e48b2bd907d78faeb450ca1e825&scene=21#wechat_redirect) 服务，登陆到控制台上，也访问不了了。看来确实要抓紧**[彻底迁移到 Cloudflare](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487240&idx=1&sn=ba535fd0c1026bc2482ea6ad1e1fb8bf&chksm=fe4b3ad3c93cb3c50bfeaed64963cce25c49bee80364d3a8ca78b87d7c9f19fd4d79d3c62ddc&scene=21#wechat_redirect)** 上去了。

查看了一下腾讯云健康状态页（https://status.cloud.tencent.com/）发现服务还都是“正常的”，也没有公开通告。不过一些群里已经传出了消息，希望能够尽快恢复吧。

![图片](02.webp)

![图片](03.webp)

------------------------------------------------------------------------

今天晚上八点，我在微信直播《[云数据库是不是杀猪盘](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487249&idx=1&sn=9003873f73089ae603ae1cadd734d3f6&chksm=fe4b3acac93cb3dcabe45ac0965b231f0b6f88dcf85c2ac898ad169bfdc4a23b85c5f69b7aff&scene=21#wechat_redirect)》，嘲讽云服务的质量安全效率成本并不过关，没想到腾讯这么赶趟儿送个大人头。还好，看起来微信还可以正常直播，，不知道是不是没有用自家的云哈哈……欢迎大家预约收看，吐槽云厂商。

[云计算泥石流](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486813&idx=1&sn=ffb126fdd061c1e27626dd558f6fa26a&chksm=fe4b3886c93cb190e2acf7af6cfd25f298199f6ee73da566bed050c066b96753b913e3453d4f&scene=21#wechat_redirect)曾几何时，“上云“近乎成为技术圈的政治正确，整整一代应用开发者的视野被云遮蔽。就让我们用实打实的数据分析与亲身经历，讲清楚公有云租赁模式的价值与陷阱 —— 在这个降本增效的时代中，供您借鉴与参考。

### [云数据库是不是智商税](/cloud/rds/)

### [牙膏云？您可别吹捧云厂商了](/cloud/toothpaste-cloud/)\

[罗永浩救不了牙膏云](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487223&idx=1&sn=da885170d5d65a3c646d8b3d9da3aed3&chksm=fe4b3b2cc93cb23a5625e8c183860a9e1528eca0a1311439f1ec308a74d53f10cf5dbbb9a1d0&scene=21#wechat_redirect)[吊打公有云的赛博佛祖 Cloudflare](/cloud/cloudflare/)\
[云计算为啥还没挖沙子赚钱？](/cloud/profit/)[FinOps终点是下云](/cloud/finops/)[卡在政企客户门口的阿里云](/cloud/aliyun-enterprise-market/)[云厂商眼中的客户：又穷又闲又缺爱](/cloud/cloud-customers-poor-bored-lonely/) [阿里云降价背后折射出的绝望](/cloud/aliyun-price-cut-despair/)迷失在阿里云的年轻人[互联网故障背后的草台班子们](/cloud/amateur-internet-outages/) [门内的国企如何看门外的云厂商](/cloud/state-owned-enterprise-cloud-view/)[剖析云算力成本，阿里云真的降价了吗？](http://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487089&idx=1&sn=ca16c2e7e534380eadcb3a3870d8e3b4&chksm=fe4b3baac93cb2bc8c4b68c468acf3e8ac5ee124080a3e738262fe99dd1765c3adf9c56ea650&scene=21#wechat_redirect)\
