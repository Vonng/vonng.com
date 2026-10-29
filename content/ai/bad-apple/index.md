---
title: "苹果新品：512 GB 金子内存、触屏 MacBook 与越来越无聊的刀法"
date: 2026-10-29
authors: [vonng]
summary: >
  512 GB 内存升级比再买一台 Mac Studio 还贵，触屏 MacBook、60 Hz iPad mini 与折叠屏故障也让人失望。苹果仍是本地 AI 的强力盟友，但存储溢价还能撑多久？
tags: [AI, 硬件, 成本, 技术评论]
---

北京时间 10 月 29 日凌晨，苹果在洛杉矶办了一场没有直播的[“Pro and Tell”](https://www.techradar.com/news/live/oled-touchscreen-macbook-pro-apple-pro-and-tell-live-october-2026)活动。

这周苹果搞的是“三连发”：周一上 [OLED 版 iPad mini](https://www.macrumors.com/2026/10/26/apple-announces-ipad-mini-with-oled-display/)，周二更 M6 iMac 和入门款 MacBook Pro，周三压轴触屏版 MacBook Pro。但这些热闹老冯都没往心里去，老冯四点多醒来，摸过手机刷了一圈，眼睛只盯着 Mac Studio 配置页上悄悄多出的那行字：[512 GB 统一内存](https://www.macrumors.com/2026/10/28/mac-studio-m5-ultra-512gb-ram/)。

8 月底 M5 Ultra 发布时，512 GB 只留了句[“10 月下旬发售”](https://www.apple.com.cn/newsroom/2026/08/apple-introduces-mac-studio-with-m5-max-and-m5-ultra/)的悬念。苹果倒是很守时，28 号准点上线。但点开价格那一秒，老冯整个人顿时就感觉不美丽了。

![studio-512.webp](studio-512.webp)

## 比整机还贵的“金子内存”：把老实人当冤大头

买东西讲究边际成本递减，上一代 M3 Ultra 就是越往上每 GB 越便宜。这代 M5 Ultra 第一档（96 GB 升 256 GB）涨到了 4,000 美元，老冯[8 月撰文估算](https://vonng.com/db/apple-m5-ultra/)时还按惯例推算第二档加个 6,000 美元，配 2 TB 硬盘整机落在十四五万也就认了。

结果苹果反手直接翻倍：[256 GB 升 512 GB 单加内存就要 11,500 美元](https://9to5mac.com/2026/10/28/apple-reveals-pricing-for-mac-studio-with-512gb-of-ram/)；国行加价高达 86,250 元，[512 GB 起步就是 172,999 元](https://www.ithome.com/1/019/246.htm)。只能说，老冯对苹果刀法的想象力，还是保守地停留在了上一代。

| 内存配置（美区官网） | M3 Ultra（2025）              | M5 Ultra（2026）              |
|----------------------|-------------------------------|-------------------------------|
| 96 GB → 256 GB       | +1,600 美元（约 10 美元/GB）  | +4,000 美元（25 美元/GB）     |
| 256 GB → 512 GB      | +2,400 美元（约 9.4 美元/GB） | +11,500 美元（约 45 美元/GB） |
| 512 GB + 1 TB 整机   | 9,499 美元                    | 22,299 美元                   |
| 512 GB + 16 TB 满配  | 14,099 美元                   | 29,799 美元                   |

平心而论，这两年全行业显存内存都在疯涨，英伟达 128 GB 的 DGX Spark 都从 3,999 美元一路[涨到了 6,950 美元](https://runaihome.com/blog/dgx-spark-64gb-vs-128gb-vs-strix-halo-2026/)（+74%）。但别人是水位整体抬高，苹果搞的却是“阶梯倒挂”：买得越多宰得越狠，第二档单价几乎是第一档的两倍。

最让人气笑的是这笔账：一台 36 核 CPU、80 核 GPU、256 GB + 1 TB 的 [M5 Ultra 整机](https://www.engadget.com/2263184/apple-mac-studio-m5-ultra-review/)卖 10,799 美元（约 42 美元/GB），单加 256 GB 内存却要 11,500 美元（约 45 美元/GB）。**单买内存，居然比连芯片、主板、电源、散热外加 1 TB 硬盘再买一整台机器还贵。**

国行也是同款幽默：加内存 86,250 元，直接买台[同配置 256 GB 整机](https://www.nodeseek.com/post-895005-1)只要 86,749 元，两边只差 499 块；美区买两台整机反而比一台 512 GB 便宜 701 美元。

既然钱花得一样，为什么不买两台 256 GB 并联？那可是翻倍的 GPU 算力外加翻倍的 1.2 TB/s 带宽。按苹果自家的[雷雳 5 RDMA 多机实测](https://machinelearning.apple.com/research/mlx-distributed-inference)，双线直连跑张量并行（而非只拼容量的流水线并行），两台提速可达 1.7–1.8 倍，四台全互连能到 2.6–3.0 倍。虽然一成多的折损比老冯预想略高，但依然是白捡的算力飞跃。

当然，遇到 Meta [Muse Spark Open](https://macrumors.com/2026/10/15/meta-muse-spark-open-mac-studio/)（8160 亿参数，4 bit 约 493 GB）这种卡脖子的巨物，两台 256 GB 扣掉系统开销确实塞不下——但单台 512 GB 同样跑不痛快。真要吃下这种前沿模型，正解是直接上**四台 256 GB**：总价 43,196 美元，比两台 512 GB（44,598 美元）还省一千多刀，生成速度直接从 25.0 拉到 36.7 token/s。

老冯琢磨了半天这套脑壳有包的定价，背后逻辑大概率出在颗粒上：256 GB 用的是标准 4 GB 颗粒，上 512 GB 通道数不够，必须换昂贵的定制 8 GB 颗粒。硬件成本上说得通，但对用户而言，除非有“桌面死活只能放一个盒子”的强迫症，或非要硬刚 [Kimi K3](https://www.superbash.ai/articles/mac-studio-m5-max-m5-ultra-local-ai-buying-guide/) 那种 4 bit 就要吃掉 1.4 TB 内存的吞金兽（得四台 512 GB 起步），否则 512 GB 纯属冤大头专供。两台 256 GB 明显更合算。只是现在的交货期都干到明年二月了。



## 触屏 MacBook Pro：违背“祖宗之法”，换一块满是指纹的屏

周三真正的主角——传了大半年的[“MacBook Ultra”](https://macrumors.com/2026/03/08/apple-planning-macbook-ultra)，最终定名 [MacBook Pro with PROLED XDR](https://www.macrumors.com/2026/10/28/apple-new-macbook-pro/)。没敢印上“Ultra”，大概因为肚子里装的还是今年 3 月同款的 M5 Pro 和 M5 Max，算力寸功未进。老冯年初[买 128 GB M5 Max 本子](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247491450&idx=1&sn=a2fd37dc58543aa1c333a7bd04066daf&scene=21#wechat_redirect)时就断定年底改款不是我的菜，趁涨价前先买先享受，这回精准命中。

![proled.webp](proled.webp)

多掏 [400 美元差价](https://tidbits.com/2026/10/28/new-macbook-pro-gets-proled-xdr-display-touchscreen-dynamic-island/)（14 寸 2,899 美元起，16 寸 3,399 美元起，16 寸拉满高达 14,549 美元，够买台 Mac Studio），换来的是 2000 尼特双层 OLED 屏、灵动岛、轻了两三百克的机身（厚度只薄了不到 1 毫米），以及最大卖点——触屏。

槽点恰恰就在“能摸”上。老冯平时把笔记本合盖当便携服务器用，触屏价值直接归零；就算开盖用，对着竖立屏幕悬空乱戳也极度反人类。乔布斯 2010 年在发布会上早就[把道理讲透了](https://www.techradar.com/pro/quote-of-the-day-by-apple-co-founder-steve-jobs-on-touchscreens-after-an-extended-period-of-time-your-arm-wants-to-fall-off-savaging-a-bitter-rivals-pc-pivot)：竖着的触摸屏点一会儿胳膊就要断了。

做对了的触屏本，像 360 度翻折的联想 Yoga，或是能拆键盘的 Surface Pro、ROG 幻X，大前提都是**屏幕能变成平板**。一台既不能翻又不能拆的传统翻盖本，触屏能干的事，行业天花板级的 Mac 触控板全能干，还不留满屏油印。黑色幽默的是，苹果怕你戳屏幕乱晃，专门调硬了铰链——可见有多别扭，自己心里门儿清。

软件同样没准备好。macOS 目前只是粗暴地把触控映射成鼠标点击，不支持 Apple Pencil，顺手的手势还得慢慢等开发者适配，开局神似 2016 年折腾七年黯然退场的 Touch Bar。

乔布斯守了 16 年的“祖宗之法”，库克 9 月 1 日刚交棒给“张铁牛”——[约翰·特努斯（John Ternus）](https://newsonair.gov.in/apple-announces-john-ternus-as-successor-to-tim-cook-as-ceo-from-september-1/)才俩月就破了戒。更拧巴的是定位：重度性能党要的是散热而非触屏；若真如部分外媒所言 mini-LED 老款就此停产，以后买 M5 Max 笔记本就只能捏着鼻子交这 400 美元“触屏税”了。




## 60 Hz 的 iPad mini 与裂开的折叠屏：挤牙膏与掉链子齐飞

不需要触屏的笔记本硬塞触屏，靠屏幕吃饭的平板却在死抠高刷。

老冯一直很偏爱 iPad mini，觉得它是除 Pro 外最称手的一款。周一发布的新款换了 8.5 寸 OLED 和 A20 Pro，厚度压到 5.4 毫米，重量降到极致的 [255 克](https://9to5mac.com/2026/10/26/new-ipad-mini-vs-previous-model-heres-everything-new/)，起售价也从 599 涨到了 699 美元；唯独翻遍规格表，[刷新率依然是 60 Hz](https://www.pcguide.com/news/apples-new-ipad-mini-with-oled-display-looks-like-its-locked-to-60hz-with-no-promotion-technology/)。

要知道去年 799 美元的 [iPhone 17 标准版都补齐了 120 Hz](https://techcrunch.com/2025/09/09/apple-launches-iphone-17-with-a-120hz-display)。随便打两把《王者荣耀》都懂 60 帧和 120 帧隔着次元壁；主力设备全是高刷，切回 60 Hz 划两下那种拖泥带水，一眼就能败光 OLED 的好感。海外社区甚至猜测这块面板物理支持 120 Hz，纯属被软件锁死。虽无拆机实锤，但实在太符合苹果“让 mini 永远差口气”的价格歧视刀法——若真如此，跟把 6 GB 颗粒屏蔽成 4 GB 卖毫无区别，活脱脱就是“倒牛奶”逻辑。

刀法精明，品控却掉了链子。另外值得一提的是上周刚开售的 1,999 美元首款折叠屏 [iPhone Duo](https://fortune.com/2026/10/27/apple-iphone-duo-foldable-screen-cracking-hinge/)，预购几分钟抢空、排期到明年 1 月，结果交货没几天就接连爆出 7.6 寸内屏沿折痕脆裂。有澳洲用户开合不到 20 次就“咔”一声干碎；iFixit 怀疑是支撑杆未完全缩回顶破屏幕或进灰，官方目前只推给 AppleCare 换新。

会不会演变成“天线门”“弯曲门”级别的翻车还得看后续返修率，但三星折叠屏都出到第八代了，苹果晚了整整七年进场还栽在基础铰链上，外加保外换内屏要价 999 美元（比全新 iPhone 17 还贵 200 刀），着实够尴尬。

![apple-cut.webp](apple-cut.webp)

> https://x.com/mylifcc/status/2115096683662942702
>
> https://www.tomshardware.com/tablets/ipads/m4-ipad-pros-with-8gb-of-ram-may-actually-have-12gb-teardowns-reveal-possible-apple-hijinks



## 最好的本地 AI 盟友，最狠的存储屠夫

老冯心底其实挺遗憾。俺早年在 Apple 待过，手里设备换了一茬又一茬，几十万砸进去，十几年老粉的感情不是假的。更纠结的是，站在老冯一贯提倡的“下云”与数据自主可控立场上，苹果偏偏又是当下最争气的本地 AI 硬件盟友。

M5 Ultra 给出了恐怖的 1.2 TB/s 内存带宽，是 [DGX Spark 的四倍有余](https://petronellatech.com/blog/mac-studio-m5-ultra-vs-nvidia-dgx-spark-for-local-ai/)，还把雷雳 5 RDMA 集群原生做进了系统底层。桌面上摆个安静的铝制小方盒，就能跑起几千亿参数的大模型——这件事苹果干得确实漂亮，业界独此一家。

可一谈钱，最佳盟友秒变“存储屠夫”。M5 Ultra 硬盘升到 16 TB 要加 7,500 美元（500 美元/TB）；新款 Mac mini 升 1 TB 加 500 美元、升 2 TB 加 1,000 美元，而上代第三方模块仅售 300 和 420 美元。更难受的是焊死退路：M4 Mac mini 好不容易做成可拆硬盘，新出的 M6 和 M5 Pro Mac mini 转头又把闪存[死死焊回了主板](https://9to5mac.com/2026/09/22/m6-mac-mini-upgrade-storage-change/)。Mac Studio 目前虽还是可拆模块，但老冯真不敢赌下一代不会下黑手。

我倒不替苹果操心生意。截至 6 月底苹果账上躺着约 [1,465 亿美元现金和有价证券](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm)，光吃本地 AI 红利和硬件老本就够满嘴流油。但老冯总有个预感：**照这种把用户当韭菜精算的节奏走下去，早晚有人会把苹果这张桌子掀了。**

大家今天忍着刀法买高溢价 Mac，核心是交两份买路钱：一份给 **macOS** 交“软件地租”——商业软件繁荣、GUI 与 CLI 兼顾，底下还打通了纯正的 Unix 开发者生态；另一份给**大统一内存**交“算力保护费”——不用买天价企业卡就能在桌面塞下大模型。但世上没有填不平的护城河，软硬两头松动的苗头，已经从四个方向冒出来了：

1. **桌面 Linux 自己在争气**：DHH 做的 Omarchy 把 Arch 和 Hyprland 打磨得颇有品味，有心气用免费 Linux 桌面硬刚 macOS。老冯 8 月[认真试玩一圈](https://vonng.com/db/omarchy-desktop/)后虽暂退回 Ubuntu，但差距肉眼可见在缩小。
2. **AI Agent 改变交互主体**：以前护城河稳固，是因为用电脑的“人”挑剔界面与手感；往后干活的主力变成 Agent，一旦 Windows 或 Linux 能提供同样顺手的 Computer Use 环境，“干活必买 Mac”瞬间松动。
3. **Coding Agent 暴力移植**：最近老冯还看到更野的尝试——直接利用 Coding Agent 把 macOS 移植到普通 MiniPC 和笔记本上丝滑运行。这条路一旦跑通，对苹果更是釜底抽薪。
4. **混合推理绕开天价大内存**：借着稀疏 MoE 架构的东风，像最近开源的 [Strata](https://github.com/Niko1221/Strata) 这类混合推理引擎，能把高频激活的热点专家常驻显存，冷门专家动态卸载到廉价的系统内存与 SSD 里——单靠一张 12 GB 显存的老显卡配上大内存普通主机，就能跑起 125B 规模的 Qwen3.8-Flash-Next。用软件调度拆解大内存垄断，直接让便宜大碗的 MiniPC + 老显卡焕发第二春。

老冯桌上就摆着一台 128 GB 统一内存的 Strix Halo 小主机，整机才 [3,000 美元上下](https://runaihome.com/blog/dgx-spark-64gb-vs-128gb-vs-strix-halo-2026/)，买的时候一万二不到。而同内存的 M5 Max Mac Studio 要卖 [5,399 美元](https://blog.invidelabs.com/m5-ultra-mac-studio-local-ai/)。一旦“软件地租”和“大内存刚需”这两道墙被开源社区与 AI 联手推平，苹果这套引以为傲的存储刀法就会失灵。



## 骂归骂，该买买

回头看苹果这一周：512 GB 的惊人刀法，触屏 MacBook 卖块用不上的屏，iPad mini 死守 60 Hz，Duo 折叠屏磕在了铰链上，真的是让人感慨廉颇老矣。

最无奈的现实是，吐槽归吐槽，老冯大概率还是得掏腰包弄两台 256 GB 的 Mac Studio 回来并联跑跑 —— 
谁让眼下想在桌面安静省心地跑本地大模型，确实挑不出第二个选择。
只不过既然已经排到了明年 2 月，老冯也没那么着急了，
手头六台本地电脑和六台云服务器都还够用，等 EPP 优惠上架再找朋友看看吧。

刀法哪怕明牌摆在脸上，你也只能乖乖付钱，这就是苹果傲慢的底气。
只是这套把戏玩了十几年，实在让人看腻了。
真正能让苹果把刀收起来的，从来不是老粉的吐槽，而是别人把软件追上来、把桌子掀掉的那一天。

