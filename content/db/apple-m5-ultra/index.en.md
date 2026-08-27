---
title: "Apple Skipped the Event and Quietly Launched a 512 GB Mac Studio"
linkTitle: "512 GB Mac Studio"
date: 2026-08-25
authors: [vonng]
summary: >
  No teaser, no rumors—the website simply changed. For local AI, this may be the most important machine of the year.
tags: [Apple, Mac Studio, Local AI]
---

> [Original article on WeChat](https://mp.weixin.qq.com/s/iIzW0B-FSO0Fi5eYQsyeCw)

There was no event today. No teaser campaign. Not even a credible rumor.

Apple simply updated its website and launched the new Mac mini and Mac Studio. The Mac mini now comes with the M6 or M5 Pro; the Mac Studio gets the M5 Max or M5 Ultra.

![Apple's website announcing the new Mac Studio with M5 Max or M5 Ultra](lineup.webp)

I have long been obsessed with self-hosted AI, especially machines like the Mac Studio with large pools of unified memory. I had spent almost a year searching every week for some sign of when the M5 Ultra would arrive.

Nothing appeared. Then today, without warning, it did.

Most important of all, **the 512 GB unified-memory option is back. The maxed-out [M5 Max MacBook Pro](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247491450&idx=1&sn=a2fd37dc58543aa1c333a7bd04066daf&scene=21#wechat_redirect) I bought for RMB 60,000 at the start of the year suddenly feels a lot less exciting.**

![The M5 Ultra Mac Studio offers up to 512 GB of unified memory](memory.webp)

That does not make the MacBook Pro a bad purchase. It is still a portable 128 GB workstation, which is a very different proposition from an aluminum box on a desk. But if your real goal is to run large models locally, the 512 GB Mac Studio is virtually the only machine in this generation worth serious consideration.

So far, we can see that the 256 GB / 16 TB configuration costs RMB 143,000. Based on Apple's pricing pattern, 512 GB / 16 TB will probably add another RMB 50,000–60,000, putting a fully loaded system close to RMB 200,000. Even a 512 GB / 2 TB configuration will likely cost around RMB 140,000–150,000. It is not cheap.

![Price of the Mac Studio configured with 256 GB of unified memory and 16 TB of storage](pricing.webp)

---

## 1. Why 512 GB Matters

After Apple discontinued the previous 512 GB M3 Ultra model, the market went berserk. A machine that originally cost less than RMB 100,000 was quoted by resellers at RMB 150,000, then RMB 180,000; some reportedly asked RMB 200,000.

![Reseller pricing for the discontinued 512 GB M3 Ultra Mac Studio](resale.webp)

People did not chase it because it was a Mac or because they liked the Apple logo. The machine filled a highly unusual gap in the market: **it may have been the cheapest high-memory, all-in-one local AI system that an ordinary buyer could purchase through official channels with a proper invoice.**

Expensive and cheap are relative. Next to a GB300 Station that costs $95,000—roughly RMB 640,000—it looks like a bargain.

![NVIDIA DGX Station listed at $94,930](dgx.webp)

The biggest problem with today's consumer GPUs is often not compute but memory capacity.

The RTX 5090 has 32 GB. The RTX PRO 6000 Blackwell has 96 GB. The DGX Spark has 128 GB. They can run a 27B model without breaking a sweat, but models such as DeepSeek-V4-Flash and GLM—mixture-of-experts models with hundreds of billions of parameters—hit the capacity wall immediately.

The Mac Studio's 512 GB of unified memory is accessible to both its CPU and GPU. That is not equivalent to 512 GB of HBM, of course, and it is nowhere near the speed of a true high-end NVIDIA system. But it avoids constantly shuttling a huge set of weights between VRAM and system memory.

**Its first job is not to answer “How fast can this run?” but “Can this fit at all?”**

### The Real Footprint of Several Models

![Weight sizes of Qwen3.8-27B, DeepSeek-V4-Flash, and GLM-5.3 compared with device memory capacity](models.webp)

The last figure is the one that matters.

Putting a 400–450 GB model into 512 GB leaves little headroom, but **there is at least a straightforward path to running it on one machine**. With consumer NVIDIA cards, you must start thinking about multiple GPUs, CPU offload, host memory, NUMA, PCIe topology, and distributed runtimes. Building a machine with enough slots, PCIe lanes, and high-bandwidth server memory just to run one model is a project in itself.

The GPUs are only the first line on the bill. Then come the case, power supply, motherboard, server CPU, cooling, noise, electrical requirements, and system tuning. The Mac Studio's value is that it packs all of that trouble into a 20-centimeter aluminum box that sits on a desk. Plug it in and get to work.

---

## 2. Capacity Is One Thing; Speed Is Another

Having 512 GB does not make the Mac Studio faster than an RTX 5090. It helps to separate inference into two stages.

**The first is prefill**, when the system reads and understands the entire prompt. This stage depends on compute, matrix-operation efficiency, and software optimization.

**The second is decode**, when the model emits one token after another. This stage is primarily constrained by memory bandwidth: generating each token requires reading the relevant weights again.

The new M5 Ultra delivers **1.2 TB/s** of unified-memory bandwidth, 50% more than its predecessor. Beyond capacity, this is the upgrade that matters most for local AI.

### What the Contenders Bring to the Table

![Memory capacity and bandwidth of the Mac Studio, Mac mini, DGX Spark, and NVIDIA GPUs](hardware.webp)

The table makes the tradeoff obvious. The RTX 5090 has 50% more bandwidth than the M5 Ultra, but only 32 GB of memory. **Bandwidth determines how quickly each token arrives; capacity determines whether the model runs at all.**

### A Conservative Estimate

Based on model architecture, weight footprint, memory bandwidth, and measurements from the previous generation, here is a conservative projection:

![Estimated generation speed and aggregate concurrent throughput for three large models on the M5 Ultra](estimates.webp)

**These are not benchmark results. The new machine has not shipped, and frameworks such as MLX and llama.cpp will need time to support the new GPU and Neural Accelerator. Quantization, context length, prompt caching, concurrency, and the inference engine can each change the result dramatically.**

Apple's website quotes **relative gains**, such as “up to 4× faster prompt processing in LM Studio,” rather than absolute numbers. Even so, the order of magnitude makes the conclusion clear: this machine may not merely load huge models, but run them at genuinely useful speeds.

Dozens of tokens per second already outpace normal human reading. Aggregate concurrent throughput of 50–100 tokens per second means the machine could support several coding agents, retrieval agents, document-analysis jobs, and background automation workflows at once. That is the threshold at which local AI becomes meaningfully productive.

Apple also specifically says that multiple Mac Studios can use Thunderbolt 5 + RDMA to form a shared memory pool, with a four-machine cluster delivering three times the distributed-inference performance of one system.

---

## 3. An Easy Upgrade to Miss: PCIe 6.0 Storage

The new Mac Studio's internal SSD uses a new architecture based on **PCIe Gen 6**. Apple says storage performance is up to twice that of the previous generation. **The theoretical link bandwidth of PCIe 6.0 x4 is 30 GB/s.**

But until independent benchmarks arrive, every real-world figure is speculation.

### What Does This Upgrade Actually Improve?

**Once a model is loaded, the SSD plays no part in steady-state generation.** Each decode step reads from 1.2 TB/s unified memory. A 13 GB/s SSD is nearly two orders of magnitude slower and irrelevant to that loop.

Where the SSD matters is model loading, model switching, cold starts, caches, data preprocessing, and large-scale local data analysis.

Take a 400 GB model. Loading it cold at 13 GB/s takes roughly half a minute; at the previous generation's 6.5 GB/s, it takes about a minute. If you switch models frequently, you will notice the difference.

### Building Your Own PCIe 6.0 System Is a Pain

**It is 2026, and consumer PC platforms are still largely on PCIe 5.0 or even 4.0.** PCIe 6.0 is only beginning to appear in servers and AI platforms. To build a Gen 6 machine yourself, the CPU platform, motherboard, and SSD controller all need to line up. Even before cost, selecting parts, validating compatibility, and wrestling with firmware is enough to ruin your week.

Apple solders the entire stack into the box. Unpack it, plug it in, and that performance is simply there.

**The soldering is also the catch**: a Mac's SSD cannot be replaced or upgraded. Apple Silicon storage has also appeared as “Apple Fabric,” not standard PCIe, in I/O Registry. “PCIe Gen 6” is therefore better understood as a **generational performance equivalent**—it does not mean you can insert a standard Gen 6 NVMe drive.

The top configuration combines a 16 TB SSD with 512 GB of unified memory. If independent testing really reaches 12–14 GB/s, loading models hundreds of gigabytes in size, scanning large Parquet datasets, and building vector indexes will all be remarkably fast.

I am only half joking: plenty of data-warehouse engineers may look at this configuration and feel a little inadequate.

In the real world, many companies' core analytical datasets would fit entirely in this machine's memory. Add DuckDB, PostgreSQL, Parquet, and local object storage, and one box could swallow many offline analytical workloads that once required a small cluster.

It will not replace a real data warehouse. High availability, concurrency, access control, disaster recovery, and horizontal scaling are different problems. But as a single-node analytical workstation, its performance is frankly absurd.

(I even caught myself wondering whether to build a macOS-based Pigsty appliance: databases, agents, and AI packaged as a ready-to-run distribution.)

---

## 4. It May Not Be Worth Buying Just for “Token Freedom”

Honestly, if your only goal is to save on subscription fees, I would not recommend a top-end Mac Studio.

I currently have ten AI subscriptions at $200 per month each. Together they cost $2,000 a month, or more than RMB 10,000. At that rate, the price of a top-end Mac Studio would buy me roughly a year of carefree access to cloud models.

And the cloud gives you leading proprietary models that are continuously updated. New reasoning, coding, and multimodal models keep arriving, and products such as Astra will push the race even harder. One quota had only reset two days ago; another reset just moments ago.

Local open-source models may not consistently keep pace in raw intelligence, tooling, or multimodal capability. You also take responsibility for model downloads, quantization, framework support, troubleshooting, upgrades, and hardware depreciation.

So if you mainly want to chat, write code, look things up, or simply finish the job with the strongest available model, **AI subscription services are usually easier and more economical.**

What you are really buying with this machine is not cheap tokens.

You are buying **a piece of computational territory that belongs entirely to you.**

---

## 5. The Real Keyword Is Data Sovereignty

If you work with ordinary public information, sending it to a cloud model is no great concern.

The situation changes completely when the material is a legal case file, a medical record, financial data, unreleased source code, a chip design, a trade secret, internal email, or client data covered by an NDA.

In those settings, **whether the data may leave your premises often matters more than whether the model tops a leaderboard.**

A 512 GB Mac Studio lets you keep the model, vector database, operational database, documents, and agent workflows on your own device. The entire inference pipeline can run without a network connection. The raw data need never go to a third party.

Local execution does not automatically make a system compliant. You still need to manage disk encryption, account permissions, audit logs, backups, model licenses, and data lifecycles.

But at least the technology finally lets you control where the data goes, who can access it, and how long it remains there.

That is why I believe this machine is far more valuable to teams in law, medicine, research, finance, manufacturing, and confidential development than it is to the average individual user.

---

## 6. This Is Not the Same Product as a DGX Station

NVIDIA's latest DGX Station uses Blackwell Ultra—the GB300—with HBM3e and LPDDR5X attached to the Grace CPU, for nearly 800 GB of tiered coherent memory in total. In raw AI compute and HBM bandwidth, it is obviously far more powerful than a Mac Studio.

It is also a professional system that costs nearly $100,000—more than RMB 600,000 at current exchange rates, enough for five or six top-end Mac Studios.

For buyers in China, procurement channels, export compliance, invoices, warranty coverage, and service can each become difficult. Gray-market channels can obtain the hardware, but a company that needs formal procurement and long-term support may not be willing to take that risk.

**The Mac Studio's advantage is not that it beats the DGX Station on every specification. It is that you can buy one through normal retail channels, receive a proper invoice, a warranty, and support, then take it back to the office and plug it in.**

Nor is it a data-center server. It has no redundant power supplies, remote management, or a full suite of enterprise operations features. If you need a strict SLA, a large multi-tenant service, or a rack-scale cluster, buy proper NVIDIA servers.

But as a personal AI workstation for an office, lab, or home, it has almost no direct competitor.

---

## 7. A Brief Note on the New Mac mini

The M6 Mac mini tops out at 32 GB of unified memory and 170 GB/s of bandwidth. It is not designed for enormous models.

It remains a compact, low-power host for local agents running 7B, 14B, and some quantized models.

The version local AI users should really watch is the **M5 Pro model**. It supports up to 64 GB of unified memory, 307 GB/s of bandwidth, and Thunderbolt 5.

![Mac mini with M5 Pro and 64 GB of unified memory](mini.webp)

It cannot run a full DeepSeek-V4, let alone a GLM model with hundreds of billions of parameters. But it is already quite practical for a quantized model in the Qwen 27B class. For a home AI service, coding agent, knowledge base, speech processing, or an always-on automation node, it may be the best-value small machine of this generation.

---

## Final Thoughts

The top-end 512 GB model will not officially ship until **late October**.

If pricing and availability in Hong Kong are reasonable, I will probably buy one. Before I pay, however, I want to see three things: **the final price, support from frameworks such as MLX, and independent sustained-inference benchmarks.**

If it performs as expected, I think this will be a machine worth keeping for many years.

It may not offer the cheapest tokens, and it will not outrun a true NVIDIA AI server. But for the first time, it lets an individual or small team use a device they can **buy through normal channels, get a proper invoice for, and put on an ordinary desk** to run cutting-edge open-source models hundreds of gigabytes in size.

RMB 100,000-plus is undeniably expensive. It is the price of a small car.

Look at it another way: a small car cannot give you a completely private local AI cluster that runs in your office 24×7.

As for whether it will sell out, remain useful through 2028, or be followed by an M7 Ultra with 1.5 TB of unified memory—

Those are questions for another visit to the wishing well.
