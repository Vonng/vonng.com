---
title: "AWS 东京可用区故障：影响13项服务"
date: 2025-04-15
authors: [vonng]
summary: >
  AWS 东京可用区断电故障：影响13项服务。
tags: [云计算, AWS, 故障复盘]
---

## AWS 东京可用区故障：影响13项服务

就在刚刚，AWS 东京可用区出现故障，开始于 4 月 15 日 16:15 分（北京时间），宣告结束于 16:51 分，EC2 实例断电，主备电源同时断电。影响13项服务。目前已经通告解决：剩余的少数实例托管在受断电不利影响的硬件上。

![图片](01.webp)

## 故障通知

**4月15日凌晨1:51（太平洋** 夏令时间）凌晨12:40至凌晨1:43之间，我们在AP-NORTHEAST-1区域的单个可用区 (apne1-az4) 中遇到了与部分 EC2 实例的连接问题。这是由于受影响 EC2 实例的主电源和备用电源中断造成的。在此期间，客户在受影响区域启动的实例以及使用受影响 EC2 实例的其他 AWS API 的错误率和延迟可能增加。工程师在几分钟内就自动介入，并立即开始研究缓解措施。我们预计此问题不会再次发生。剩余的少数实例托管在受断电不利影响的硬件上。虽然我们将继续努力恢复所有受影响的实例和卷，但为了立即恢复，我们建议尽可能替换任何剩余的受影响实例或卷。该问题已解决，服务正常运行。

**4月15日凌晨1:21（太平洋夏令时）** 我们已看到初步恢复迹象，但仍在持续监控并努力实现全面恢复。其他AWS服务也受到此问题的影响，目前仍在观察恢复情况。我们将在接下来的30-60分钟内再次发布更新。

**4 月 15 日凌晨 1:15 太平洋夏令时间** 我们正在调查影响 AP-NORTHEAST-1 区域内单个可用区 (apne1-az4) 中的实例的连接问题。

[云计算泥石流](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488410&idx=1&sn=e44705fce4221458244e7705258ca254&scene=21#wechat_redirect)点一个关注 ⭐️，精彩不迷路\

**DHH**

[先优化碳基BIO核，再优化硅基CPU核](/db/bio-core-cpu-core/)

[单租户时代：SaaS范式转移](/cloud/single-tenant-saas/)

[拒绝用复杂度自慰，下云也保稳定运行](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486772&idx=1&sn=88783a2b7982f9db9e0b9ea4843fc2cb&scene=21#wechat_redirect "拒绝用复杂度自慰，下云也保稳定运行")

[是时候放弃云计算了吗？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486366&idx=1&sn=c28407399af8b1ddeadf93e902ed23cc&scene=21#wechat_redirect "是时候放弃云计算了吗？")

[下云奥德赛](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247485760&idx=1&sn=97096da1077a4fbb4c43452a3c4983c7&scene=21#wechat_redirect "下云奥德赛")

### 亚马逊

[Ahrefs不上云，省下四亿美元](/cloud/ahrefs-saving/)

[云上黑暗森林：打爆云账单，只需要S3桶名](/cloud/s3-scam/)

[Redis不开源是“开源”之耻，更是公有云之耻](/db/redis-oss/)

[RDS阉掉了PostgreSQL的灵魂](/cloud/rds-castrates-pg/)

[扒皮对象存储：从降本到杀猪](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486688&idx=1&sn=bbdee063b65994cb5e15d3e3b7d87523&scene=21#wechat_redirect "扒皮对象存储：从降本到杀猪")

[重新拿回计算机硬件的红利](/cloud/bonus/)

[是时候放弃云计算了吗？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486366&idx=1&sn=c28407399af8b1ddeadf93e902ed23cc&scene=21#wechat_redirect "是时候放弃云计算了吗？")

[下云奥德赛](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247485760&idx=1&sn=97096da1077a4fbb4c43452a3c4983c7&scene=21#wechat_redirect "下云奥德赛")

### 阿里云

[阿里云：高可用容灾神话的破灭](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488376&idx=1&sn=3c403495f5282f469a50e4fbe09ae0c7&scene=21#wechat_redirect "阿里云：高可用容灾神话的破灭")

[阿里云故障预报：本次事故将持续至20年后？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488361&idx=1&sn=c84e7f9ff09f9f5042d990ee2ea9a105&scene=21#wechat_redirect "阿里云故障预报：本次事故将持续至20年后？")

[阿里云新加坡可用区C故障，网传机房着火](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488345&idx=1&sn=684398668bdddc05d4218c42f5a383b0&scene=21#wechat_redirect "阿里云新加坡可用区C故障，网传机房着火")

[草台班子唱大戏，阿里云RDS翻车记](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488205&idx=1&sn=2c45a521d50a60e9644b95c974bb2949&scene=21#wechat_redirect "草台班子唱大戏，阿里云RDS翻车记")

[阿里云又挂了，这次是光缆被挖断了？](/cloud/aliyun-fiber-cut/)

[云计算：菜就是一种原罪](/cloud/cloud-incompetence/)

[taobao.com 证书过期](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487367&idx=1&sn=d6e4abd2b2249d27bd8b8146b591b026&scene=21#wechat_redirect "taobao.com 证书过期")

[牙膏云？您可别吹捧云厂商了](/cloud/toothpaste-cloud/)

[罗永浩救不了牙膏云](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487223&idx=1&sn=da885170d5d65a3c646d8b3d9da3aed3&scene=21#wechat_redirect "罗永浩救不了牙膏云")

[迷失在阿里云的年轻人](/cloud/lost-youth-at-aliyun/)

[剖析云算力成本，阿里云真的降价了吗？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487089&idx=1&sn=ca16c2e7e534380eadcb3a3870d8e3b4&scene=21#wechat_redirect "剖析云算力成本，阿里云真的降价了吗？")

[从降本增笑到真的降本增效](/cloud/smile/)

[阿里云周爆：云数据库管控又挂了](/cloud/aliyun-weekly-crash/)

[我们能从阿里云史诗级故障中学到什么](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486468&idx=1&sn=7fead2b49f12bc2a2a94aae942403c22&scene=21#wechat_redirect "我们能从阿里云史诗级故障中学到什么")

[【阿里】云计算史诗级大翻车来了](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486452&idx=1&sn=29cff4ee30b90483bd0a4f0963876f28&scene=21#wechat_redirect "【阿里】云计算史诗级大翻车来了")

[阿里云的羊毛抓紧薅，五千的云服务器三百拿](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486438&idx=1&sn=b2c489675134d4e84fbc249089777cb4&scene=21#wechat_redirect "阿里云的羊毛抓紧薅，五千的云服务器三百拿")

[云厂商眼中的客户：又穷又闲又缺爱](/cloud/cloud-customers-poor-bored-lonely/)

### 腾讯云

[腾讯真的走通云原生之路了吗？](/cloud/tencent-cloud-native/)

[我们能从腾讯云故障复盘中学到什么？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487348&idx=1&sn=412cf2afcd93c3f0a83d65219c4a28e8&scene=21#wechat_redirect "我们能从腾讯云故障复盘中学到什么？")

[云SLA是安慰剂还是厕纸合同？](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487339&idx=1&sn=fce4c0d415d87026013169c737faeacb&scene=21#wechat_redirect "云SLA是安慰剂还是厕纸合同？")

[腾讯云：颜面尽失的草台班子](/cloud/tencent-disgrace/)

[【腾讯】云计算史诗级二翻车来了](/cloud/tencent-epic-fail-2/)

[垃圾腾讯云CDN：从入门到放弃](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247485363&idx=1&sn=8622b25fd2309d4fc969d22964a04129&scene=21#wechat_redirect "垃圾腾讯云CDN：从入门到放弃")

### 其他云

[删库：Google云爆破了大基金的整个云账户](/cloud/gcp-unisuper/)

[\
](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487552&idx=1&sn=799ae77dda3b80d2296070826142adea&scene=21#wechat_redirect "删库：Google云爆破了大基金的整个云账户")[云计算不能做成云算计之一：云行贿必须清理](/cloud/cloud-bribery/)\
