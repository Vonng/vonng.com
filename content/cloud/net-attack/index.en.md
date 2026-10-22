---
title: "The Internet Is Getting Shot Full of Holes"
date: 2026-10-22
authors: [vonng]
summary: >
  From PHP and GitLab to AI toolchains and certificate authorities, half the internet has been breached in a week. AI is accelerating vulnerability discovery and exploitation, making sustained maintenance, smooth upgrades, and security patches indispensable to infrastructure.
tags: [Cloud, AI, Security, Open Source]
---

Yesterday, I published [“When AI Tears Through Cloud Security”](/en/cloud/blackwall/), arguing that if AI keeps finding vulnerabilities at this pace, every cloud server and cloud database will eventually be shot full of holes.

That now looks too conservative. **In just the past couple of days, half the internet has already been shot full of holes.**

## A Week of Breaches Across the Board

The biggest shock was **PHP2Shell**[^1], the PHP remote code execution vulnerability that was everywhere last night (`CVE-2026-109618` / `CVE-2026-109619`, CVSS 9.2).

No login, no prior privileges: an attacker needs only one crafted request to execute arbitrary code, expose server memory, and take over the entire web server. Worse, with early exploit code already circulating widely, the community discovered to its dismay that the initial emergency patch might not even be complete.

How serious was it? Japan's prime minister, Sanae Takaichi, posted a warning on Twitter herself[^2]. One commenter wrote, “Never thought I'd live to see a head of state telling me to install a patch.” Quite a moment for the internet. Many people thought it was a joke. It wasn't: her own PHP site had been compromised.

![Sanae Takaichi warns website operators about a critical PHP vulnerability](php.webp)

But that was just one episode in this week's chain of breaches. Put the past few days' security advisories together, and the foundations of modern software engineering seem to be taking a beating from every direction:

First, **core infrastructure was breached**. A few days ago, a vulnerability designated `CVE-2026-99999`—yes, really, 99999—hit the major virtualization vendors. Node.js then issued emergency security patches[^3] for more than ten vulnerabilities, including RCE. Next, GitLab disclosed its **third** vulnerability in six weeks with a maximum CVSS score of 10.0 (`CVE-2026-110264`)[^4]. Again, an attacker could take over the server without logging in. The affected versions span **12 years**: every self-managed instance dating back to version 7.0 in 2014 needs an upgrade. Every last one.

![GitLab advisory for a CVSS 10.0 vulnerability allowing unauthenticated remote code execution](gitlab.webp)

Second, **the emerging AI toolchain is showing just how makeshift it is**. LiteLLM, widely used in LLM development, was poisoned in version `1.107.0`, with credential-stealing malware bundled into the release. Meanwhile, OpenCode Console was breached[^5], exposing users' OpenAI, Anthropic, and Google API keys.

Then came **a farce at the foundation of trust**. The private keys for eight intermediate CA certificates from **eMudhra**, a major Indian certificate authority, were compromised[^6] (see Cisco Talos's analysis[^7]). A certificate private key turned out to be, literally, the single digit **`4`**. This wasn't cryptography crumbling. The gatekeeper had put a paper lock on the front door.

From kernel virtualization and runtimes to code hosting, AI middleware, and certificate authorities, almost no piece of the stack made it through the week intact.

![A roundup of this week's internet vulnerabilities and security incidents, with a SpongeBob walking-away meme](chaos.webp)

These attacks aren't abstract advisories. There are already victims everywhere: **Zeabur**, which announced it was shutting down after repeated cyberattacks[^8]; [**TiDB Cloud**, breached by FulcrumSec, which hauled away 10.6 TB of data](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651295551&idx=1&sn=64b4e33bd21b374f8a213b5e11cdad6e&scene=21&poc_token=HKNN2WqjTX-s4VloE7UhlApBbnNgO-KqfUzn10VG#wechat_redirect)[^9]; **IDCF Cloud**, the prominent Japanese cloud provider where a ransomware attack brought nearly 500 businesses to a halt[^10]; and on and on.

## A Reckoning—and an Opening—for Legacy Systems

Looking at a screen full of red alerts, I see an opportunity.

**US cybersecurity stocks have already started rising, and demand for security engineers should rebound in the short term.** For the past two years, the whole industry has raced headlong after business growth and AI, cutting security budgets wherever possible. Now the bullets are flying past their heads, and there's no escaping the work they've neglected.

**This crisis will force a great many legacy systems to be updated and upgraded.**

Frankly, from the perspective of infrastructure evolution, **I think that's a very good thing.**

Anyone who works on infrastructure software knows how many systems out there operate on the rule “if it hasn't crashed, don't touch it.” It's 2026, yet plenty of production environments still run CentOS 7.9, or even 5.4—versions that belong in a museum. Inside, you might find PostgreSQL 9.1, released more than a decade ago.

Usually, when you talk to business teams about technical debt and end-of-life (EOL) risks, nobody takes you seriously. Upgrades carry risk and earn no credit; if something breaks, you take the blame. It often takes an industry-wide earthquake like this to force people to grit their teeth and rebuild the foundations of these tangled old systems.

**But here's the question: if today's relics are forced to upgrade, what happens two years from now?**

**Choose an unmaintained component, and in two years you could end up right back where last night's PHP vulnerability left people.**

Why are major PHP vulnerabilities so devastating every time? Because countless websites and legacy systems around the world run old PHP versions. They've long been left without maintainers or a workable upgrade path. When an RCE vulnerability surfaces underneath them, they can't even apply a patch. They can only line up and wait to be hit.

## Unmaintained Software: Online and Defenseless

I feel this acutely because I maintain two major pieces of infrastructure software myself: **an [open-source PostgreSQL distribution](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492498&idx=1&sn=ff2e6b477826c2fe899c62cdab7673f2&scene=21#wechat_redirect), Pigsty[^11], and [open-source object storage, Silo](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247492702&idx=1&sn=c45e85f69bb1f87aaebffc46dc49d90e&scene=21#wechat_redirect)**. It's been particularly busy lately. With AI now in use on both sides of the security battle, bug reports and vulnerabilities keep coming. Every day means intensive code review and patching.

Take the familiar open-source object store **MinIO**. Last October, [the vendor stopped regular releases of its open-source community edition](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247490694&idx=1&sn=d79444d4b55d6d42133f88db84fa5e18&scene=21#wechat_redirect), and I took over community maintenance with a fork called **Silo**. In just six months, **I've fixed more than 20 security vulnerabilities and dozens of bugs.**

![The Silo website shows project figures including downloads, GitHub stars, and security fixes](silo.webp)

Many teams don't take the end of software maintenance seriously enough. They think, “The binary I already have isn't going to break by itself. Why not just stay on the last free version?”

As I wrote yesterday, that can be reasonable in a physically isolated or network-isolated environment. But if you're still connected to the internet, what you might once have gotten away with no longer works.

**If you're still running the original MinIO, at its last release from October 2025 or earlier, and it's exposed to the public internet, you're effectively defenseless.**

The logic is brutal. Every security fix in an open-source project leaves a public commit and code diff. With today's LLMs, attackers don't need to discover zero-days from scratch. They can simply pull the 20-plus vulnerability fixes I've recently published, run patch diffing with AI, and generate a complete set of exploits in minutes. Then they can scan the internet for old instances that haven't upgraded and pick them off one by one, breaking straight into your MinIO server.

![Silo's security timeline documents ongoing vulnerability fixes and security advisories](patch.webp)

In an age of automated internet-wide scanning, **unmaintained software doesn't stand still. It visibly decays into a publicly documented backdoor.**

That's why this fork, essentially a personal project, has reached **4,000 GitHub stars** and **4 million downloads** in six months. It has no flashy new features to offer—just continuing security patches and updates. But with the internet being shot full of holes, **“someone is still looking after your infrastructure and shipping patches”** has become about as fundamental a need as there is.

## Closing Thoughts

For more than a decade, the tech industry has worshiped building new tools. People love grand concepts and disruptive features. The dirty work of fixing bugs and shipping patches is treated like air: free, ever-present, and taken for granted. Only this week, as PHP, GitLab, and Linux's virtualization foundations were breached one after another, did many people wake up: **when AI-driven attacks come down like torrential rain, what determines whether you make it through the night isn't a flashy new feature. It's whether there is still a real person behind that dull update command, keeping your system safe.**

But honestly, however fast maintainers fix things, this is still a reactive arms race. PHP2Shell and GitLab's maximum-severity vulnerability aren't freak spikes. They're the first rumble of a new normal. Don't assume that surviving this week means you're in the clear. The aging codebases we've accumulated over more than a decade are now being subjected, all at once, to the relentless scrutiny of AI. Logic flaws that once took a top security researcher months to tease out are now being churned out on an assembly line.

Against attacks on this scale, any static defense that stops evolving is paper-thin. Either give your infrastructure the ability to upgrade smoothly and apply patches at any time, or physically disconnect it from the public internet. The clock really is running out for legacy systems that never get upgraded.

![Gorillas firing amid broken network infrastructure](featured.webp)

## References

[^1]: [PHP2Shell](https://watchtowr.com/intelligence/php-cve-2026-109618-faq/)
[^2]: [Japan's prime minister Sanae Takaichi warns of a critical PHP vulnerability](https://abmedia.io/php-critical-rce-takaichi-warning)
[^3]: [Node.js October 2026 security releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)
[^4]: [GitLab vulnerability with a maximum CVSS score of 10.0 (CVE-2026-110264)](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html)
[^5]: [OpenCode Console breach may have exposed users' API keys](https://thehackernews.com/2026/10/opencode-console-breach-may-have.html)
[^6]: [eMudhra intermediate certificate private keys compromised](https://emudhra.we-have-a-problem.com/)
[^7]: [Cisco Talos: Analysis of compromised intermediate certificates](https://blog.talosintelligence.com/compromised-intermediate-certificates/)
[^8]: [Zeabur announces its shutdown](https://zeabur.com/zh-CN/blogs/zeabur-is-shutting-down)
[^9]: [TiDB Cloud data breach](https://www.techflowpost.com/article/34741)
[^10]: [IDCF Cloud official announcement](https://www.idcf.jp/news/topics/20261008001)
[^11]: [Pigsty](https://pigsty.io/)
