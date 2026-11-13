---
title: "Ten Hours Without Exchange: Inside Microsoft's Cascading M365 Outage"
date: 2026-11-13
authors: [vonng]
summary: >
  A global Exchange Online outage dragged on for nearly ten hours, cascading across Microsoft 365 and third-party AI connectors. A look at how a network config change, aggressive health checks, and client retry storms locked Microsoft into a metastable failure—and why cloud customers still own the risk.
tags: [Cloud, Incident, Commentary]
---

Starting at 16:17 UTC on November 12, 2026 (00:17 Beijing time on November 13), Microsoft's core email infrastructure, **Exchange Online**, suffered a massive global outage (`EX1550543`) that quickly cascaded along internal shared dependencies across the broader **Microsoft 365** ecosystem (`MO1550821`). At the peak, Downdetector logged nearly 130,000 problem reports for Outlook alone, locking out enterprise users across the Americas, Europe, and Asia-Pacific.

![Microsoft's service health page listing degraded Microsoft 365 services and affected products](microsoft-service-health.webp)

This wasn't an external attack or an organic traffic spike. According to Microsoft's status updates, **the server-side process responsible for establishing secure connections overloaded and crashed**, and automated health checks compounded the damage by pulling degraded nodes out of rotation until the remaining capacity collapsed. Even after rolling back a **recent network configuration change** whose timing lined up closely with the start of the outage, Microsoft's public status page still listed the service as degraded nearly ten hours in. Exact per-tenant recovery times and the definitive root cause await the formal Post-Incident Review (PIR).

## Timeline and Blast Radius

Microsoft's backend telemetry first flagged Exchange Online access errors at 16:17 UTC on November 12 (00:17 Beijing time on November 13). Webmail (OWA), desktop Outlook (MAPI), mobile clients (EAS), and REST endpoints all dropped at once, leaving enterprise mailboxes stuck on "Disconnected" or an endless loading spinner. Error reports went vertical within two hours—Outlook alone neared **130,000 reports** on Downdetector—prompting Microsoft to open a cross-product umbrella incident (`MO1550821`) and widen its impact assessment from "portions of the Americas" to connections from any region worldwide.

It was a textbook **shared-substrate failure**. Core Teams chat and direct file reads in SharePoint mostly stayed up, whereas anything touching Exchange mail, calendar, or contact data went down by association: Microsoft Graph endpoints timed out across the board, Teams meeting scheduling broke, **Microsoft 365 Copilot** stalled out because it couldn't pull workplace context, and errors rippled through Defender Safe Links checks, Purview compliance components, and even a subset of Windows 365 Cloud PCs configured with Customer Key.

![Downdetector outage report spikes across Outlook, Microsoft 365, and related services](downdetector.webp)

The blast radius didn't stop at Microsoft's perimeter, either—the enterprise M365 connectors inside **OpenAI (ChatGPT)** and **Anthropic (Claude)** failed in lockstep. Worse, **the M365 Admin Center itself failed to load for stretches of the incident**. Locked out of the very console where Microsoft posts detailed outage advisories, sysadmins around the world ended up flocking to Reddit and other forums to read status updates copied and pasted by whoever still had a working session.

Incident response dragged on for nearly ten hours, complete with several diagnostic reversals. Microsoft initially blamed the disconnections on "elevated load across multiple regions." After 19:00 UTC (03:00 Beijing time), it instituted a global change freeze and dropped the traffic-surge hypothesis, conceding that high load was merely a symptom: **droves of servers had failed automated health checks and been evicted from the cluster**, dumping existing traffic onto the surviving pool and crushing it on the spot. On the perennial question of whether anything had changed, Microsoft first stated it had found no relevant recent changes, then walked that back an hour later to say it was reviewing a handful of configuration updates.

Between 22:00 and 00:00 UTC (06:00–08:00 Beijing time), mitigation hit a stubborn dead end. Engineers tried partitioning infrastructure and rebooting nodes in rolling batches. Pockets of traffic briefly recovered, only for Microsoft to discover that **freshly restarted servers locked up again the moment they took live production traffic**. Not until 01:06 UTC on November 13 (09:06 Beijing time) did they isolate the actual fault: **the core process responsible for establishing secure connections on affected servers was getting overwhelmed**. While throttling specific traffic patterns and rebuilding nodes on the previous baseline, Microsoft formally rolled back a **recent network configuration change closely correlated with the onset of the incident**. As of 02:01 UTC (10:01 Beijing time), its public service health page still showed "Service degradation."

## Technical Analysis

What follows is a failure-propagation model reconstructed from Microsoft's public advisories, rather than a confirmed full root cause. The exact health-check policies, internal connection-process behavior, and client retry volumes won't be clear until Microsoft publishes the formal PIR.

Piecing ten hours of status fragments together reveals a textbook case of failure amplification: a configuration change triggers a capacity collapse, kicking off a self-reinforcing feedback loop. The causal chain is straightforward:

```text
Recent network config change (prime suspect)
       ↓
Secure-connection process degrades & health probes fail
       ↓
Mass node eviction → Effective capacity falls off a cliff
       ↓
Client retry storm crushes surviving nodes (metastable feedback loop)
       ↓
Exchange goes dark → Cascading failures across M365 & external AI connectors
```

The deadliest mechanism here is **automated health checks working against recovery and locking the fleet into a metastable failure state**. Health probes exist to cull the occasional sick host. Faced with a fleet-wide common-mode fault, though, a load balancer without fail-open circuit breaking—a panic threshold capping the fraction of a backend pool probes are allowed to evict—will dutifully pull sluggish nodes out of rotation one after another, engineering a catastrophic capacity cliff all by itself.

Until the bad network configuration is reverted and the abnormal secure-handshake overhead disappears, rebooting machines accomplishes nothing. A freshly booted node comes online, immediately absorbs a wall of automated reconnects from millions of clients worldwide, and keels over again within minutes. That explains the hours of whac-a-mole where pockets of Exchange briefly showed a pulse before flatlining all over again.

The outage also stripped away the pretense that modern cloud office suites are loosely coupled. Cloud vendors love pitching SaaS as a modular, elastic mesh of cloud-native services. Under real stress, decades-old Exchange turns out to be the hidden single point of failure holding up enterprise collaboration, security auditing, and frontier AI agents alike.

One wobble in the mail connection layer, and all the compute behind Copilot and third-party LLM connectors can't keep them from flying blind. Meanwhile, Microsoft's official accounts on X kept robotically ending every status post by telling administrators to "sign in to the Admin Center for details"—while the Admin Center itself refused to load. Fate-sharing between the data plane and the control plane is one of the oldest traps in infrastructure architecture, and global cloud giants still walk right into it.

## My Take

Talk about impeccable timing. Barely a month ago, I migrated email for my own company domain (`pgsty.com`) off iCloud and onto Exchange Online. I woke up this morning, opened my mail client, and stared at zero new messages—walking face-first into Microsoft's blackout. Email is one of the very few workloads I actively advise *against* self-hosting, simply because poor IP reputation gets outbound mail rejected outright—which leaves you stuck picking your poison.

![Discussing the Microsoft email outage with other users on X](outage-reactions.webp)

![Mail client timing out while connecting to an Exchange server](exchange-timeout.webp)

**Buying a cloud giant's service gets you convenience—along with every ounce of its complexity and systemic risk.**

Step back for a second. Suppose you rack a few bare-metal servers in a conventional colocation facility and quietly run your own application or mail stack. You'd have to try pretty hard to invent a failure mode like *"the facility pushed a low-level network config tweak that sent my secure-connection daemon and health probes into a self-sustaining death spiral."*

On hyperscale public clouds, though, we watch the exact same script play out every few months: DNS meltdowns, circular dependencies between object storage and IAM, fat-fingered allowlists, or a control-plane push in one corner that drags global tenants into a ditch together. **Mega-scale comes with pathologies unique to mega-scale—failure modes that simply don't exist at your own scale.**

[**What Can We Learn from Tencent Cloud's Outage Postmortem?**](/en/cloud/qcloud/)

[**What Can We Learn from Alibaba Cloud's Epic Outage?**](/en/cloud/aliyun/)

[**Huawei Cloud International Outage: Suspected IAM Upgrade Gone Wrong**](/en/cloud/huawei-iam/)

[**Postmortem on Cloudflare's November 18 Global Outage**](/en/cloud/cf-ck-down/)

[**How One AWS DNS Failure Cascaded Across Half the Internet**](/en/cloud/aws-dns-failure/)

[**Taking Down Half the Web: Inside the Global Google Cloud & Cloudflare Outage**](/cloud/gcp-cf-outage/)

[**Wiped Clean: How Google Cloud Nuked a Major Fund's Entire Cloud Account**](/en/cloud/gcp-unisuper/)

Failures in modest, self-contained systems tend to be local, legible, and linear. A disk dies or a process crashes; you check the logs, restart the daemon, or fail over to a standby, and get on with your day. To keep a global multitenant substrate running, a hyperscale cloud has to stack hundreds of layers of software-defined networking, automated health probes, dynamic traffic orchestration, and multi-tier security gateways underneath it.

On a normal day, that contraption looks bulletproof. Jam a single gear with a bad config change, though, and the automated failover machinery it prides itself on flips into a brutally efficient failure amplifier. Individual tenants end up paying for the structural fragility of a distributed leviathan spanning hundreds of thousands of servers.

[**Stop Fetishizing Complexity: The Secret to High Availability Off the Cloud**](/en/cloud/uptime/)

Don't harbor any illusions about meaningful guarantees or payouts when a cloud giant goes down, either. Sure, Exchange Online comes with an SLA. Just don't confuse that with "service goes down for ten hours, Microsoft covers ten hours of losses." Uptime is calculated across eligible services, affected user counts, and contractual billing windows, and getting anything back means filing a claim for review under Microsoft's contract rules. Even if your claim clears every hurdle, the payout is a partial service credit against your subscription fee—a handful of billing credits that aren't even in the same order of magnitude as the real damage from missed critical emails and stalled operations.

[**Alibaba Cloud's CDN Went Down—Don't Forget to File Your SLA Claim**](/cloud/aliyun-cdn-sla/)

[**Are Cloud SLAs Just a Placebo?**](/en/cloud/sla/)

Put bluntly, moving to the cloud means signing a lopsided adhesion contract where your uptime sits in somebody else's hands. If you want turn-key convenience, you also sign up to swallow periodic bouts of hyperscale sickness. Think outsourcing infrastructure means you can pass the buck to the cloud vendor when production goes dark? Dream on. You're still the one left holding the bag.

![Screenshot of a discussion on accountability across public and private clouds](cloud-responsibility.webp)

## Series: Cloud Computing Trainwrecks

**Cloud Outages**

[**Someone Needs to Rein In Cloud Vendors: Cloudflare Is Down Again**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247490554&idx=1&sn=01636e81b9fe923e218fe814fe1b3d8d&scene=21#wechat_redirect)

[**Baidu Cloud: A ¥20 Million Bill for 261 KB of Traffic**](/en/cloud/baidu-cloud-bill/)

[**Alibaba Cloud "Borrows" Supabase: The Gray Zone Between Open Source and Cloud Vendors**](/en/cloud/aliyun-supabase/)

[**AWS's Official Outage Postmortem**](/en/cloud/aws-postmotem/)

[**How One AWS DNS Failure Cascaded Across Half the Internet**](/en/cloud/aws-dns-failure/)

[**Major Outage in AWS's Largest Region Takes Down Multiple Services**](/en/cloud/aws-dns-failure/)

[**Zhihu Goes Dark: Expired Certificate or Botched CDN?**](/cloud/zhihu-outage/)

[**Alibaba Cloud's CDN Went Down—Don't Forget to File Your SLA Claim**](/cloud/aliyun-cdn-sla/)

[**16 Billion Credentials Exposed Across Apple, Google, Facebook, and Telegram**](/cloud/16b-credentials-leak/)

[**Taking Down Half the Web: Inside the Global Google Cloud & Cloudflare Outage**](/cloud/gcp-cf-outage/)

[**Major Incident: Alibaba Cloud Had a Core Domain Seized**](/cloud/aliyun-domain-seized/)

[**Inside the Dior Data Breach: Another Cloud Misconfiguration?**](/cloud/dior-leak/)

[**Wiped Out Over an Unpaid ¥2 ($0.30) Tencent Cloud Bill: How a 100,000-User App Vanished**](/cloud/tencent-2yuan/)

[**AWS Tokyo Availability Zone Outage Hits 13 Services**](/cloud/aws-tokyo-outage/)

[**Shopify's April Fools' Outage Was No Prank**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247489406&idx=1&sn=f51aea1ea2148f7d281f1bded9de8888&scene=21#wechat_redirect)

[**Oracle Cloud Fiasco: 6 Million Authentication Records Leaked**](/cloud/oracle-cloud-leak/)

[**OpenAI's Global Outage Postmortem: Circular Dependencies in Kubernetes**](/en/cloud/openai-failure/)

[**Alipay Goes Down Right on Schedule for Singles' Day (11.11)**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488632&idx=1&sn=dba2c78f37bb4af2421677e842b57fdd&scene=21#wechat_redirect)

[**Amateur Hour Boomerang: An Expired Certificate Takes Down Apple Music**](/cloud/apple-music-cert/)

[**Alibaba Cloud and the Collapse of the High-Availability Myth**](/en/cloud/aliyun-ha/)

[**Alibaba Cloud Status Advisory: Estimated Recovery in 20 Years?**](/en/cloud/aliyun-ha/)

[**Catastrophic Bug in Alibaba Cloud Drive Exposed Other Users' Private Photos**](/cloud/aliyun-drive-bug/)

[**Alibaba Cloud Singapore AZ-C Goes Dark Amid Data Center Fire Reports**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488345&idx=1&sn=684398668bdddc05d4218c42f5a383b0&scene=21#wechat_redirect)

[**Now It's WPS Office's Turn to Go Down**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488215&idx=1&sn=34bedcf01169facd0207200b3e018989&scene=21#wechat_redirect)

[**Amateur Hour on Full Display: Inside Alibaba Cloud's RDS Outage**](/en/cloud/rds-failure/)

[**What Can We Learn from the NetEase Cloud Music Outage?**](/en/cloud/netease/)

[**GitHub Sitewide Outage: Did the Database Bite Them Again?**](/cloud/github-outage/)

[**Global Windows BSOD: Amateur Hour on Both Sides of the Contract**](/en/cloud/bsod-friday/)

[**Alibaba Cloud Is Down Again: A Severed Fiber Cable This Time?**](/cloud/aliyun-fiber-cut/)

[**Wiped Clean: How Google Cloud Nuked a Major Fund's Entire Cloud Account**](/en/cloud/gcp-unisuper/)

[**Dark Forest in the Cloud: All It Takes to Bankrupt Your S3 Bill Is a Bucket Name**](/en/cloud/s3-scam/)

[**Even taobao.com Let Its TLS Certificate Expire**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247487367&idx=1&sn=d6e4abd2b2249d27bd8b8146b591b026&scene=21#wechat_redirect)

[**What Can We Learn from Tencent Cloud's Outage Postmortem?**](/en/cloud/qcloud/)

[**Cloud SLAs: Placebo or Toilet-Paper Contract?**](/en/cloud/sla/)

[**Tencent Cloud: Amateur Hour in Plain Sight**](/cloud/tencent-disgrace/)

[**Tencent Cloud's Second Epic Meltdown**](/cloud/tencent-epic-fail-2/)

[**It's Amateur Hour All the Way Down: Behind Major Internet Outages**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247486590&idx=1&sn=d4d85de483fafb867487f024631a3e6c&scene=21#wechat_redirect)

[**From Cost-Cutting Punchline to Real Operational Efficiency**](/en/cloud/smile/)

[**Alibaba Cloud's Weekly Meltdown: The Managed Database Control Plane Is Down Again**](/cloud/aliyun-weekly-crash/)

[**What Can We Learn from Alibaba Cloud's Epic Outage?**](/en/cloud/aliyun/)

[**Alibaba Cloud's Epic Meltdown**](/en/cloud/aliyun/)

**Cloud Resources**

[**Paying to Get Fleeced: Escaping Cloud Lock-In's Hotel California**](/en/cloud/patsy/)

[**Are Managed Cloud Databases a Sucker's Tax?**](/en/cloud/rds/)

[**Is Cloud Block Storage a Bait-and-Switch?**](/en/cloud/ebs/)

[**Anatomy of the True Cost of Cloud Compute**](/en/cloud/ecs/)

[**Unmasking Object Storage: From Cost Savings to Bait-and-Switch**](/en/cloud/s3/)

[**Tencent Cloud's Awful CDN: From Onboarding to Rage-Quit**](/en/cloud/cdn/)

[**How 32 Seconds on Alibaba Cloud DCDN Left Me Owing ¥1,600**](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247488466&idx=1&sn=21a77c9076643f723038047b8c14ba59&scene=21#wechat_redirect)

[**Cloud SLAs: Placebo or Toilet-Paper Contract?**](/en/cloud/sla/)

[**The Endgame of FinOps Is Leaving the Cloud**](/en/cloud/finops/)

[**Why Do China's Cloud Providers Make Less Money Than Sand Quarries?**](/en/cloud/profit/)

[**Are Cloud SLAs Just a Placebo?**](/en/cloud/sla/)

[**Paradigm Shift: From Cloud-First to Local-First**](/en/cloud/paradigm/)

**Leaving the Cloud**

[**Paying to Get Fleeced: Escaping Cloud Lock-In's Hotel California**](/en/cloud/patsy/)

[**Amateur Hour on Full Display: Inside Alibaba Cloud's RDS Outage**](/en/cloud/rds-failure/)

[**DHH's Cloud Exit: Missing the S3 Deadline Costs $5,000 (¥40K) a Day**](/cloud/dhh-s3-migration/)

[**DHH's Cloud Exit Beat Expectations: Over $10M in Five-Year Savings**](/en/cloud/odyssey-done/)

[**Optimize Your Carbon-Based Bio-Cores Before Your Silicon CPU Cores**](/en/db/bio-core-cpu-core/)

[**The Single-Tenant Era: A SaaS Paradigm Shift**](/cloud/single-tenant-saas/)

[**Stop Fetishizing Complexity: Staying Reliable Off the Cloud**](/en/cloud/uptime/)

[**Six Months Out, ¥10M ($1.4M) Saved: DHH's Cloud Exit FAQ**](/cloud/cloud-exit-faq/)

[**Is It Time to Walk Away from the Cloud?**](/cloud/odyssey/)

[**The Cloud-Exit Odyssey**](/cloud/odyssey/)
