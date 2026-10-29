---
title: "Apple’s Latest: 512 GB of Gold-Plated RAM, Touchscreen MacBooks, and the Same Old Pricing Games"
date: 2026-10-29
authors: [vonng]
summary: >
  Upgrading to 512 GB costs more than another Mac Studio. Touchscreen MacBooks, a 60 Hz iPad mini, and foldable-screen failures add to the disappointment. Apple remains a powerful ally for local AI, but how long can its memory and storage premiums last?
tags: [AI, Hardware, Cost, Commentary]
---

In the early hours of October 29, Beijing time, Apple held its [“Pro and Tell”](https://www.techradar.com/news/live/oled-touchscreen-macbook-pro-apple-pro-and-tell-live-october-2026) event in Los Angeles, without a livestream.

Apple staged three launches this week: the [OLED iPad mini](https://www.macrumors.com/2026/10/26/apple-announces-ipad-mini-with-oled-display/) on Monday, the M6 iMac and entry-level MacBook Pro on Tuesday, and the touchscreen MacBook Pro as Wednesday’s finale. None of that particularly interested me. I woke up sometime after 4 a.m., reached for my phone, and scrolled through the news. My eyes went straight to one line quietly added to the Mac Studio configurator: [512 GB of unified memory](https://www.macrumors.com/2026/10/28/mac-studio-m5-ultra-512gb-ram/).

When the M5 Ultra launched in late August, Apple had left the 512 GB option dangling with a promise of [“late October” availability](https://www.apple.com.cn/newsroom/2026/08/apple-introduces-mac-studio-with-m5-max-and-m5-ultra/). To its credit, it delivered on schedule, on October 28. Then I clicked through to the price, and my mood promptly soured.

## Memory Priced Like Gold: More Than a Whole Computer

You expect the marginal cost to fall as you buy more. That was how the M3 Ultra worked: higher memory tiers cost less per GB. On the M5 Ultra, the first upgrade, from 96 GB to 256 GB, had risen to $4,000. In [my August estimate](/en/db/apple-m5-ultra/), I assumed the next tier would follow the usual pattern and add another $6,000. A complete machine with a 2 TB SSD would land somewhere around RMB 140,000–150,000. Painful, but I could live with it.

Instead, Apple nearly doubled my estimate: [going from 256 GB to 512 GB costs $11,500 for the memory alone](https://9to5mac.com/2026/10/28/apple-reveals-pricing-for-mac-studio-with-512gb-of-ram/). In mainland China, the surcharge is RMB 86,250, and [a 512 GB machine starts at RMB 172,999](https://www.ithome.com/1/019/246.htm). Clearly, I had underestimated how much further Apple could push its pricing this generation.

| Memory Configuration (Apple’s U.S. Store) | M3 Ultra (2025) | M5 Ultra (2026) |
| --- | --- | --- |
| 96 GB → 256 GB | +$1,600 (about $10/GB) | +$4,000 ($25/GB) |
| 256 GB → 512 GB | +$2,400 (about $9.4/GB) | +$11,500 (about $45/GB) |
| Complete system, 512 GB + 1 TB | $9,499 | $22,299 |
| Maxed out, 512 GB + 16 TB | $14,099 | $29,799 |

To be fair, both GPU and system memory prices have soared across the industry over the past two years. Even NVIDIA’s 128 GB DGX Spark has [climbed from $3,999 to $6,950](https://runaihome.com/blog/dgx-spark-64gb-vs-128gb-vs-strix-halo-2026/), a 74% increase. But while everyone else is raising prices across the board, Apple has inverted the volume discount: the more you buy, the harder you get gouged. The second upgrade costs nearly twice as much per GB as the first.

Here is the calculation that makes you laugh through gritted teeth. A [complete M5 Ultra](https://www.engadget.com/2263184/apple-mac-studio-m5-ultra-review/) with a 36-core CPU, an 80-core GPU, 256 GB of memory, and a 1 TB SSD costs $10,799, or about $42 per GB of memory. Adding just 256 GB of memory costs $11,500, or about $45/GB. **The memory alone costs more than another entire computer, including the chip, motherboard, power supply, cooling, and a 1 TB SSD.**

The joke works in China, too: RMB 86,250 for the memory upgrade versus RMB 86,749 for [another 256 GB machine with the same configuration](https://www.nodeseek.com/post-895005-1). That is a difference of just RMB 499. In the U.S., two complete machines actually cost $701 less than one 512 GB machine.

If you are spending the same money, why not link two 256 GB machines? You get twice the GPU compute and twice the aggregate memory bandwidth, with each machine delivering 1.2 TB/s. In Apple’s own [Thunderbolt 5 RDMA benchmarks](https://machinelearning.apple.com/research/mlx-distributed-inference), two machines directly connected by two cables and running tensor parallelism, rather than pipeline parallelism merely to pool capacity, deliver a 1.7–1.8× speedup. Four fully interconnected machines reach 2.6–3.0×. Losing a little over 10% to overhead is more than I expected, but that is still a substantial performance gain for free.

There are limits. A monster such as Meta’s [Muse Spark Open](https://macrumors.com/2026/10/15/meta-muse-spark-open-mac-studio/), with 816 billion parameters and a roughly 493 GB footprint at 4-bit precision, will not fit on two 256 GB machines once you account for system overhead. But a single 512 GB machine will not run it comfortably either. For a frontier model like that, the right answer is **four 256 GB machines**: $43,196 in total, more than $1,000 cheaper than two 512 GB machines at $44,598, with generation speed jumping from 25.0 to 36.7 tokens/s.

After puzzling over this absurd pricing, my best guess is that the explanation lies in the memory chips: the 256 GB configuration uses standard 4 GB chips, while reaching 512 GB with the available channels requires expensive custom 8 GB chips. That could explain the hardware cost. For the buyer, though, 512 GB is a sucker’s deal unless you absolutely insist on having only one box on your desk, or need to tackle a money pit like [Kimi K3](https://www.superbash.ai/articles/mac-studio-m5-max-m5-ultra-local-ai-buying-guide/), which consumes 1.4 TB of memory even at 4-bit precision and needs at least four 512 GB machines. Two 256 GB machines are clearly better value. The catch is that delivery estimates now stretch into February next year.

## The Touchscreen MacBook Pro: Defying Jobs for a Screen Full of Fingerprints

Wednesday’s real headliner, the [“MacBook Ultra”](https://macrumors.com/2026/03/08/apple-planning-macbook-ultra) rumored for more than half a year, ended up being called the [MacBook Pro with PROLED XDR](https://www.macrumors.com/2026/10/28/apple-new-macbook-pro/). Perhaps Apple did not dare put “Ultra” on it because it still contains the same M5 Pro and M5 Max chips introduced in March, with no gain in compute performance. When I [bought my 128 GB M5 Max laptop](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng%3D%3D&mid=2247491450&idx=1&sn=a2fd37dc58543aa1c333a7bd04066daf&scene=21#wechat_redirect) early this year, I decided the year-end redesign would not be for me and bought before the price rise so I could enjoy it sooner. That call was right on the money.

The [extra $400](https://tidbits.com/2026/10/28/new-macbook-pro-gets-proled-xdr-display-touchscreen-dynamic-island/) buys a 2,000-nit tandem OLED display, Dynamic Island, a chassis 200–300 grams lighter but less than 1 mm thinner, and the headline feature: touch. Prices start at $2,899 for the 14-inch and $3,399 for the 16-inch. A fully loaded 16-inch reaches $14,549, enough to buy a Mac Studio.

Touch is precisely my complaint. I generally use my laptop with the lid closed as a portable server, so a touchscreen adds exactly zero value. Even with the lid open, holding your arm up to poke a vertical screen is terrible ergonomics. Steve Jobs [made the point back in 2010](https://www.techradar.com/pro/quote-of-the-day-by-apple-co-founder-steve-jobs-on-touchscreens-after-an-extended-period-of-time-your-arm-wants-to-fall-off-savaging-a-bitter-rivals-pc-pivot): use an upright touchscreen for a while and your arm feels ready to fall off.

Touchscreen laptops that get this right, such as the Lenovo Yoga with its 360-degree hinge, or the Surface Pro and ROG Flow Z13 with their detachable keyboards, share one essential feature: **the screen can become a tablet**. On a conventional clamshell that neither folds back nor detaches, the Mac’s best-in-class trackpad can do everything the touchscreen can, without covering the display in greasy fingerprints. The darkly funny part is that Apple stiffened the hinge specifically to stop the screen wobbling when you poke it. Clearly, it knows how awkward this is.

The software is not ready either. For now, macOS simply maps touches to mouse clicks. There is no Apple Pencil support, and useful gestures will have to wait for developers to adapt their apps. It feels uncomfortably like the Touch Bar, introduced in 2016 and quietly retired after seven years of trying to make it work.

Jobs’s doctrine held for 16 years. Then, barely two months after Tim Cook handed over on September 1, [John Ternus](https://newsonair.gov.in/apple-announces-john-ternus-as-successor-to-tim-cook-as-ceo-from-september-1/), nicknamed “Zhang Tieniu” (“Iron Ox Zhang”) in Chinese, broke the taboo. The product’s positioning is even harder to reconcile: users who need serious performance care about cooling, not touch. If reports from some overseas outlets are right and the old mini-LED models are being discontinued, anyone buying an M5 Max laptop will have to swallow that $400 “touchscreen tax.”

## A 60 Hz iPad mini and Cracking Foldables: Stingy Upgrades, Slipping Quality

Apple forces touch onto laptops that do not need it, then skimps on refresh rates for tablets whose entire purpose revolves around the screen.

I have always had a soft spot for the iPad mini. Outside the Pro lineup, it is the iPad I find most comfortable to use. Monday’s new model brings an 8.5-inch OLED display and an A20 Pro, trims the thickness to 5.4 mm, and gets the weight down to a mere [255 grams](https://9to5mac.com/2026/10/26/new-ipad-mini-vs-previous-model-heres-everything-new/). The starting price rises from $599 to $699. Yet after all that, [the refresh rate is still 60 Hz](https://www.pcguide.com/news/apples-new-ipad-mini-with-oled-display-looks-like-its-locked-to-60hz-with-no-promotion-technology/).

Even last year’s $799 [base iPhone 17 got 120 Hz](https://techcrunch.com/2025/09/09/apple-launches-iphone-17-with-a-120hz-display). Play a couple of rounds of Honor of Kings and the gap between 60 and 120 fps is obvious. When all your main devices have high-refresh-rate screens, a few sluggish swipes at 60 Hz can wipe out the goodwill earned by OLED. Some overseas communities even speculate that the panel physically supports 120 Hz and is capped in software. No teardown has confirmed that, but it would fit Apple’s habit of keeping the mini just short of what you want to maintain its price tiers. If true, it would be no different from disabling part of a 6 GB chip and selling it as 4 GB: the old trick of dumping milk to prop up prices.

Apple may be shrewd at carving up its product lineup, but quality control is slipping. Consider its first foldable, the $1,999 [iPhone Duo](https://fortune.com/2026/10/27/apple-iphone-duo-foldable-screen-cracking-hinge/), which went on sale last week. Preorders sold out within minutes, with delivery dates stretching into January next year. Yet within days of deliveries, reports began piling up of the 7.6-inch inner display cracking along the fold. One Australian user heard a snap and saw the screen break after opening and closing it fewer than 20 times. iFixit suspects a support bar that fails to retract fully and punctures the display, or dust getting inside. So far, Apple’s official response has simply been to direct people to AppleCare for replacements.

Whether this becomes another Antennagate or Bendgate will depend on the repair rates that follow. Still, Samsung’s foldables are already in their eighth generation. Apple arrived seven full years late and stumbled over the basic hinge. Add a $999 out-of-warranty inner-screen replacement, $200 more than a brand-new iPhone 17, and it is hard not to cringe.

## The Best Ally for Local AI, the Worst Gouger on Memory and Storage

Underneath the irritation, I am disappointed. I worked at Apple years ago. I have bought generation after generation of its hardware, spent hundreds of thousands of yuan, and been a fan for well over a decade. That attachment is real. What makes this harder is that, as someone who has long argued for leaving the cloud and keeping control of our own data, I also see Apple as the strongest hardware ally local AI has right now.

The M5 Ultra delivers a formidable 1.2 TB/s of memory bandwidth, [more than four times the DGX Spark’s](https://petronellatech.com/blog/mac-studio-m5-ultra-vs-nvidia-dgx-spark-for-local-ai/), and Thunderbolt 5 RDMA clustering is built into the operating system. A quiet little aluminum box on your desk can run models with hundreds of billions of parameters. Apple has done this beautifully. Nobody else in the industry does it.

Then the price comes up, and your best ally turns into a storage gouger. Upgrading an M5 Ultra to 16 TB costs $7,500, or $500 per additional TB. On the new Mac mini, moving to 1 TB costs $500 and 2 TB costs $1,000, while third-party modules for the previous generation sell for just $300 and $420 respectively. Worse, Apple is soldering shut the escape route. The M4 Mac mini finally offered removable storage, only for the new M6 and M5 Pro Mac minis to [solder the flash back onto the motherboard](https://9to5mac.com/2026/09/22/m6-mac-mini-upgrade-storage-change/). The Mac Studio still uses removable modules for now, but I would not bet on Apple sparing the next generation.

I am not worried about Apple’s business. At the end of June, it had roughly [$146.5 billion in cash and marketable securities](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm). The local AI boom and its existing hardware strengths alone can keep the profits rolling in. But I have a nagging feeling: **if Apple keeps calculating how much it can squeeze out of every customer, sooner or later someone will upend the whole business.**

People put up with Apple’s pricing because buying a Mac means paying two tolls. The first is “software rent” for **macOS**: a thriving commercial software ecosystem, strong support for both GUI and CLI workflows, and a full Unix developer ecosystem underneath. The second is “protection money” for access to **large pools of unified memory**: enough capacity to fit big models on a desk without buying absurdly expensive enterprise GPUs. But no moat is permanent. Four developments are already starting to erode Apple’s advantages in both software and hardware:

1. **Desktop Linux is getting better on its own merits.** DHH’s Omarchy brings tasteful polish to Arch and Hyprland, with the ambition to take on macOS using a free Linux desktop. I [gave it a serious try in August](/en/db/omarchy-desktop/) and went back to Ubuntu for the time being, but the gap is visibly closing.
2. **AI agents change who operates the computer.** The moat used to hold because humans cared deeply about interfaces and how they felt. As agents take on more of the work, a Windows or Linux environment that lets them operate the computer just as easily could quickly weaken the idea that getting work done requires a Mac.
3. **Coding agents can brute-force a macOS port.** I have recently seen an even wilder experiment: using coding agents to get macOS running smoothly on ordinary mini PCs and laptops. If this approach works out, it could pull the rug out from under Apple.
4. **Hybrid inference sidesteps expensive memory configurations.** Taking advantage of sparse mixture-of-experts (MoE) architectures, hybrid inference engines such as the recently open-sourced [Strata](https://github.com/Niko1221/Strata) can keep frequently activated experts resident in VRAM and dynamically offload less-used experts to cheap system RAM and SSDs. An old graphics card with just 12 GB of VRAM, paired with an ordinary PC with plenty of RAM, can run the 125B-parameter Qwen3.8-Flash-Next. Software scheduling breaks the grip of expensive high-capacity memory and gives affordable mini PCs paired with old GPUs a second life.

There is already a Strix Halo mini PC with 128 GB of unified memory on my desk. The whole machine costs [around $3,000](https://runaihome.com/blog/dgx-spark-64gb-vs-128gb-vs-strix-halo-2026/); I paid less than RMB 12,000 for mine. An M5 Max Mac Studio with the same amount of memory costs [$5,399](https://blog.invidelabs.com/m5-ultra-mac-studio-local-ai/). Once the open-source community and AI together eliminate the software rent and the need for huge memory pools, Apple’s carefully engineered memory and storage premiums will stop working.

## I’ll Still Buy. I’ll Just Wait for a Discount.

Look back at Apple’s week: staggering prices for 512 GB, a touchscreen MacBook selling me a feature I will not use, an iPad mini stuck at 60 Hz, and a foldable Duo tripping over its hinge. It is hard not to see an aging champion losing its touch.

The frustrating reality is that, for all my complaining, I will probably still pay for two 256 GB Mac Studios and link them up. Right now, if I want to run large models locally on my desk, quietly and without fuss, I cannot find another option that fits. But with deliveries already pushed into February next year, I am in no hurry. My six local computers and six cloud servers are still enough for now. I will wait for EPP discounts to become available, then see whether a friend can help.

Apple can make the gouging perfectly obvious and still expect you to pay. That is where its arrogance comes from. After well over a decade, though, this routine has become tiresome. Complaints from longtime fans will never make Apple ease up. That will happen when someone else catches up on software and upends the market.
