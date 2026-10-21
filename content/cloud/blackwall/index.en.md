---
title: "When AI Tears Through Cloud Security"
date: 2026-10-21
authors: [vonng]
summary: >
  TiDB Cloud breached, Zeabur shutting down, PostgreSQL 19 delayed: as AI accelerates vulnerability discovery and exploitation, how does the lag in deploying patches change the security calculus for cloud services? Local-first systems and physical isolation may be our last Blackwall.
tags: [Cloud, AI, Security, Local First]
images: []
---

The past two weeks in cloud computing and databases have felt like a disaster movie.

First came the **TiDB Cloud data breach** that has dominated the news over the past couple of days. The extortion group [FulcrumSec](https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting) put up a dedicated page for PingCAP on its leak site, *[The PingCAP TiDB Cloud Leaks](https://fulcrumsec.vg/pingcap/)*, claiming to have exfiltrated **10.6 TB** from TiDB Cloud. Alongside its public taunts, it released a **200 GB** first-stage sample for anyone to download and inspect.

This is no isolated incident. Step back, and the cloud infrastructure industry looks to be caught in a **cascade of systemic failures**:

- **Zeabur breached twice, then announces its shutdown.** Once a popular PaaS among developers, Zeabur suffered an environment-variable leak in late August. [A devastating second breach on October 14 reached its underlying dedicated servers. On October 17, it announced that the service would shut down completely at the end of December](https://zeabur.com/zh-CN/blogs/zeabur-is-shutting-down).
- **Regional clouds and major hosting providers hit in succession.** On October 7, ransomware struck the East Japan region of **IDCF Cloud**, a prominent Japanese cloud provider in the SoftBank group, [bringing 495 business and local-government customers to a halt](https://www.neuracybintel.com/articles/ransomware-attack-disrupts-japans-idcf-cloud-affecting-495-businesses-and-local-governments). Roughly 3.6 PB of data was encrypted. The provider went so far as to announce that [data in the affected availability zone would be difficult to recover, leaving customers dependent on their own external backups](https://hard2bit.com/en/blog/idcf-cloud-ransomware-snapshots-backups-outside-cloud-provider/). Meanwhile, even **Hetzner**, a European hosting heavyweight known for its technical chops, [suffered an attack against its Cloud API and console on October 14 that temporarily disrupted services](https://status.hetzner.com/incident/23397b40-e121-48d7-9c4e-0a6b4dcc4307).
- **16,000 Supabase databases left exposed.** Security firm UpGuard has just reported that, amid the boom in AI-assisted programming, or vibe coding, [more than 16,000 databases hosted on Supabase had publicly exposed endpoints and missing row-level security (RLS) configurations](https://www.upguard.com/blog/everything-everywhere-systemic-data-exposure-in-supabase-apps), leaving data open to bulk extraction. Set up like that, they are practically waiting to be harvested.

These headlines are only the tip of the iceberg. Behind them is a fundamental shift: **the rules of both attack and defense have changed.**

At the current pace of vulnerability disclosure and exploitation, I think almost every internet-connected cloud server and VM could soon be riddled with holes.

## 1. PostgreSQL 19's Rare Delay and the Vulnerability Wave

Why are vulnerabilities being disclosed, and cloud platforms falling, at such an unnerving pace?

Anyone following the PostgreSQL community may have noticed an unusual development. PostgreSQL, normally as dependable as clockwork in its release schedule, has delayed version 19, originally due this fall. [General availability has been pushed back to November 19](https://www.postgresql.org/about/news/postgresql-19-rc-1-released-3409/). [During beta, the project also removed 13 release-note entries](/pg/pg19b4-release/) covering **[11 features whose code had already been written](https://dev.to/devopsdaily/postgres-19-slipped-to-november-every-pulled-feature-and-why-3b4m)**, including the much-anticipated SQL/PGQ property graph queries, `FOR PORTION OF` temporal updates, `MERGE/SPLIT PARTITION`, and online data checksums.

The official reason for the delay is to incorporate the many fixes in the November minor releases into PostgreSQL 19 and issue another release candidate. There is also some interesting context: **people have been scanning the PostgreSQL source with Claude and other large language models, then flooding the community with bug reports and fixes.** Even core developer Robert Haas, when he launched the now-famous [“scary patch contest”](https://www.postgresql.org/message-id/CA%2BTgmob9NY6m0YNFTQ4nFH2d0iC9SQRruDYxfndGKKzh8OC80w%40mail.gmail.com) on `pgsql-hackers` in late August, asked Claude to assess which new features had the scariest bugs. I have found a few PostgreSQL bugs with AI myself recently.

PostgreSQL is a mountain of C code built up over more than three decades, with code quality among the best in open source. But AI code auditing has become absurdly capable. Memory boundary conditions, integer overflows, and type confusion that might once have taken a top security researcher months to unravel can now turn up in batches after an overnight run with a large language model.

Look at what has already been disclosed. In the routine security update on August 13, PostgreSQL [disclosed and fixed 28 CVEs in one release](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/), [a record total, including 14 high-severity remote code execution (RCE) vulnerabilities rated CVSS 8.8](https://blog.codercops.com/blog/postgresql-august-2026-security-release-cve-guide). The findings ranged from a [heap buffer overflow in the widely used `to_char()` function (`CVE-2026-14669`)](https://www.cve.org/CVERecord?id=CVE-2026-14669) and memory corruption in `pg_stat_statements` (`CVE-2026-14676`) to integer wraparound leading to memory writes in the full-text search type `tsvector` (`CVE-2026-14662`) and in `fuzzystrmatch` (`CVE-2026-15742`). The code was being turned inside out.

See [“A Flood of Fixes: PostgreSQL's Latest Minor Releases Address 28 CVEs and 110 Bugs”](/pg/pg-186-cve/).

The very next day, August 14, security researcher Mehmet Ince published a major piece with the blunt title [“Systemic Risks in the Managed PostgreSQL Industry”](https://mehmetince.net/part-1-6-systemic-risks-in-the-managed-postgresql-industry-extension-risks-are-real-exploiting-postgis-memory-corruption-bug-at-neondb-supabase-and-many-more/). His target was `address_standardizer`, an auxiliary extension distributed with PostGIS and allowlisted by default at almost every cloud provider.

![Mehmet Ince's report on security risks in managed PostgreSQL](pg-risks.webp)

He first used an out-of-bounds read in PostGIS ([`CVE-2026-73515`](https://www.strix.ai/cve/CVE-2026-73515)) to defeat address space layout randomization (ASLR), then an out-of-bounds write in `address_standardizer` (`CVE-2026-73514`) to corrupt memory. He even exploited how a C compiler handles Boolean values at the assembly level to create a “Shadow-Superuser” that bypassed some superuser-status checks. That chain of exploits cut straight through **NeonDB, Supabase, Xata**, and other popular serverless and managed PostgreSQL platforms.

Think the Linux containers and VMs underneath will save you once the database process is compromised?

Look at the recent crop of **Linux kernel exploits and container and VM escapes**.

**[“Copy Fail” (`CVE-2026-31431`)](https://www.suse.com/blog/suse-responds-to-the-copy-fail-vulnerability/)** is a vulnerability in the kernel's cryptographic subsystem. It requires no race condition, and public demonstrations claim to trigger it reliably. Affected kernels are used by major distributions including Ubuntu, RHEL, and Amazon Linux. It gives an unprivileged local user a way to tamper with the page cache and escalate privileges. In container environments that share a kernel, it can also threaten the host and other tenants when the conditions for exploitation are met. Because the cached data can be changed without altering the original file on disk, monitoring that checks only file hashes may miss it.

Then there is **[`PwnEscape` (`CVE-2026-99999`, CVSS 9.3)](https://socprime.com/blog/cve-2026-99999-analysis/)**, disclosed on October 15: an out-of-bounds write in `skb_checksum_help()` that had [lurked in the Linux kernel's IPv4 networking stack for 18 years](https://tuxcare.com/blog/pwnescape-kvm-guest-escape/). Distribution advisories spell out the risk: an untrusted guest VM can send packets with malformed checksum metadata through its virtual network interface, leaking or corrupting host kernel memory and potentially **escaping the VM to execute arbitrary code as root on the host**. [AlmaLinux's advisory](https://almalinux.org/blog/2026-10-16-pwnescape-cve-2026-99999/) confirms that risk. But the scope of the demonstrations matters: [Vercel's disclosure](https://vercel.com/blog/findings-from-the-1-million-dollar-vercel-sandbox-challenge#the-kernel-zero-day) describes host memory disclosure in production. The host crash and root code execution were demonstrated in a KVM / Firecracker environment the researchers set up with the same configuration.

![PwnEscape emergency maintenance notices shared by Paulos Yibelo](pwnescape.webp)

Memory corruption in application-layer extensions, RCE in the database engine, page-cache tampering in containers, escapes from KVM guests using network packets: the entire defensive stack is leaking, from top to bottom.

## 2. Why the Cloud Will Be Riddled with Holes

Back to the opening claim: why do I think that, at the current pace of AI-assisted vulnerability discovery, almost every public-cloud server and database will eventually be riddled with holes? This is not about any particular provider failing to try hard enough. It is an irreconcilable operational conflict between **how open-source software is developed** and **how multitenant public clouds are run**.

An attacker no longer even needs to point Claude at the code to hunt for zero-days. There is a simpler option: **watch the public `git commit log` for Linux and PostgreSQL.** Mainline commits and ordinary bug fixes are publicly visible. Some fixes expose enough clues to be useful to an attacker before anyone recognizes them as security issues. Suppose a PostgreSQL core developer commits a patch today for a bug that “causes an out-of-bounds memory write under certain boundary conditions,” with the details spelled out in the commit message.

An attacker—or an automated AI agent working for one—can start analyzing the conditions for exploitation as soon as that commit appears. For some vulnerabilities, a working prototype may take only minutes. What about the cloud provider? **Its deployment process simply cannot keep pace with upstream commits.**

PostgreSQL, for example, [normally issues minor releases quarterly, with additional releases for important bugs or security issues](https://www.postgresql.org/developer/roadmap/). Confirmed security vulnerabilities follow a [private coordination process](https://wiki.postgresql.org/wiki/UpdateReleaseDrafting#Security_Releases); patches are not invariably made public months before a release. But a gap still exists for ordinary fixes that are already public, and for instances that remain unpatched after a release. Once the community ships, each provider still has to pull the code, merge it into its customized fork, test control-plane compatibility, and schedule a staged rollout. By the time the fix reaches customer instances, the damage may already be done.

In all my years in the database industry, I have never seen a cloud provider dare to follow every `master` commit in a database or the Linux kernel and update thousands of running production instances every day. It is not realistic engineering. Try it, and you will not need an attacker: your own upgrades will take you down.

That creates a **dangerous lag** of weeks or even months. A fix or clues to an exploit are public, and anyone can study the loose brick in the wall. Meanwhile, unpatched cloud servers and multitenant databases remain exposed to the internet, or share a physical host with unknown neighboring tenants, waiting for a patch window months away.

The gap has always existed. AI changes what happens inside it. At the top of the stack, reckless vibe coding produces an avalanche of misconfigurations. At the bottom, automated vulnerability discovery and exploitation break through isolation.

Low-level exploitation was once largely the domain of a relatively restrained, discreet community of security professionals. Now a script kiddie using a version of GLM or Qwen with its safeguards stripped out—or another unrestricted LLM—does not even need to understand assembly or memory layouts. Feed it a public commit log, have it generate a proof of concept, and start shooting.

With internet exposure and multitenancy, that patch gap becomes a shooting gallery where attackers can see their targets and fire at will.

### An Aside: Would Commercial Software Be Safer?

At this point, someone selling proprietary software will inevitably jump in: “See? Open source gets attacked by AI because the code and commits are public. For security, you should buy commercial software with a secret codebase!” Believe that, and you are jumping out of the frying pan into the fire.

Security has a basic rule: **never rely on security through obscurity.** Thinking “if we hide the source, attackers cannot find the bugs” is self-deception. As attack costs fall by orders of magnitude, the flimsy proprietary systems that escaped scrutiny because they were badly built, rarely used, or simply not worth a close look may be swept away. The compromised, in-house cloud control planes mentioned above already offer examples.

First, strip away the branding from most commercial databases marketed as “sovereign technology” with “enterprise-grade security,” and you will usually find a heavily modified fork of an old PostgreSQL or MySQL release. The old vulnerabilities now surfacing upstream are still there in the inherited code. Worse, because these forks have diverged so far, they often take even longer than public-cloud providers to integrate security fixes. Some simply keep quiet, leave the bug unfixed, and pretend nothing happened.

Even a completely proprietary system written from scratch is not beyond AI's reach. Human-written C and C++ code, built with modern compilers, produces machine code with highly consistent **patterns** in memory allocation, bounds checking, and protocol parsing. AI can already work with decompilers such as IDA and Ghidra to reverse-engineer stripped binaries and perform targeted fuzzing.

More fundamentally, the argument gets cause and effect backward. Is it bad that people scrutinize open-source code, find bugs, and submit fixes? **By the basic principles of software engineering, that is an excellent thing.**

Start with a simple fact: **a mature system has a finite number of bugs, provided you do not keep piling on flashy features or recklessly changing its foundations.** Why would PostgreSQL 19 break with years of release discipline, accept a rare delay, and cut features already implemented? Part of the answer is that the community understands the tradeoff: put new features on hold and clear as many existing mines as possible.

On a stable branch with a settled feature set, assuming no new defects are introduced, bugs are a nonrenewable resource. **Every bug AI finds and developers correctly fix removes one more hidden mine, giving the branch a chance to become safer.** Linux and PostgreSQL are now undergoing one of the harshest, most intensive collective trials by fire in software history: the world's best security researchers, armed with the latest computing power, are sweeping open-source infrastructure for mines, free of charge.

And proprietary software? Its source stays hidden, without thousands of eyes auditing it or the hardening that comes from public attack and defense. It has far less experience under fire. That does not mean it has no vulnerabilities; it means no one has helped clear the mines. Inside the black box, fragile implementations often accumulate, including elementary mistakes that would not survive static analysis. Everything looks peaceful until the source leaks or an attacker points an AI binary-auditing tool at it. With no meaningful defense in depth, the whole thing is likely to fall in one go.

Do not confuse cause and effect: **the problem is not openness and transparency. It is exposure in a public, multitenant environment.** Open source's immediate pain lies in the **window between a public fix and its effective deployment**. How do we get the security of thoroughly tested open-source software without spending that window as a sitting duck on the internet?

The answer is simple: **use physical separation to cut off the remote paths through which attackers exploit the patching delay.**

## 3. The Days of Burning DVDs for the Server Room

I have long advocated **local-first computing and data autonomy**. Many **Pigsty** users know that it has supported offline installation from day one, with a basic operating assumption: **the internet does not exist**.

Why build that assumption into the design? Our first customer handled classified information. In its core server room, pulling a Docker image or running `yum install` against the public internet was out of the question. The network was physically isolated; not a single cable connected it to the outside world. To install a database, we had to collect the OS dependencies, database source packages, monitoring components, and every last RPM dependency into a completely self-contained offline installation repository. Then we burned it all onto DVDs, carried them into the server room, and installed from the servers' optical drives.

At the time, I found it terribly inconvenient. After years of cloud-security absurdities, and especially this latest wave of vulnerabilities, I have come to understand and respect that tradeoff: **physical isolation is the simplest, bluntest, and most effective last line of defense in information security.**

You can draw beautiful cloud architecture diagrams and talk about zero trust, fine-grained IAM, eBPF sandboxes, and SOC 2 certification. None of it changes a harsh fact: **if your machines face the public internet or share underlying infrastructure with other people's instances, one misconfiguration, one leaked support-system token, or one fix for a C buffer overflow just committed to GitHub can let a script kiddie on the other side of the planet take you down in seconds.**

What happens to the attacker's costs if you establish a real **air gap**? The scripts and AI on the far end of the network cable lose their route in. The attacker must find another way to bring malicious code into your network: through the supply chain, removable media, or an insider. Think of Stuxnet and Iran's Natanz uranium-enrichment facility. A target without a direct internet connection is not necessarily unreachable.

![CyberHoot infographic showing Stuxnet's attack on industrial control systems](stuxnet.webp)

Or the attacker has to attempt a physical intrusion: sneak into your office at night to access internal equipment, or steal a computer and try to decrypt it. Failing that, there is the cryptographer's dreaded [rubber-hose cryptanalysis](https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis), better known as the [five-dollar wrench attack](https://xkcd.com/538/): kidnap the DBA and beat the password out of them with a wrench.

An air gap does not make security absolute. But it raises the bar from **a script kiddie pressing Enter** to **a Hollywood spy plot and serious violent crime**. Over the years, I have seen many isolated internal networks running kernels and databases seven or eight years old, without an upgrade for three to five years. The operators slept soundly. In the environments I saw, those systems did indeed run without incident for long stretches.

Physical isolation and dedicated hardware keep strangers' malicious SQL, hostile containers, and rogue VMs outside. **Many remote attack paths are cut off at the physical network before they ever reach the software.** You still have to manage untrusted internal accounts, compromised applications, and supply-chain risks. Isolation does not mean you can skip patches forever. But reaching the vulnerable software becomes much harder.

Even if an air gap is impractical, a properly configured firewall and private-network boundary around your hosts and databases can sharply reduce the attack surface. Unfortunately, many cloud incidents start with an inability to get that configuration right. Those 16,000 exposed Supabase databases are a case in point.

## 4. Cyberpunk 2077's Prophecy: Back Behind the Blackwall

We may be witnessing a historic turning point.

For a decade, cloud providers have coaxed businesses into moving their core data onto multitenant public clouds with promises of economies of scale and professional teams handling security. Now the surge in AI computing power is turning vulnerability research from a craft workshop into an industrial production line. When discovery far outpaces patch deployment, the scale that cloud providers once boasted about becomes a vast shooting gallery: **one breach, consequences across the network**.

That will turn the balance between **cloud services** and **self-hosted, local-first systems** on its head.

As I write this, I keep thinking about the world of *Cyberpunk 2077*.

In its backstory, the legendary hacker Bartmoss unleashes the DataKrash virus. Countless rogue AIs rampage through the old public Net, turning a globally connected network into a death zone where connecting can get your neural interface fried. Humanity eventually retreats into protected networks behind the **Blackwall**, which keeps the out-of-control old Net at bay. The game's AI barrier is, of course, different from a physical air gap. But the image of walling off a dangerous outside world is strikingly apt.

Look at the scripts scanning internet ports around the clock, the AI models tirelessly auditing open-source C code, and the cloud providers being breached one after another. Is *Cyberpunk 2077* really just science fiction? It feels as though we are flooring the accelerator in that direction.

I am certainly not asking everyone to disconnect tomorrow. That would be unrealistic. The answer is **to separate systems by sensitivity**: take back control of your most critical, sensitive data, move it onto private networks, and physically isolate those systems. For everything else, at least configure the firewalls correctly and reduce the attack surface.

In a wasteland of rogue AI and automated exploits, the only truly safe territory may be the part you have disconnected.

![The Blackwall keeping the dangerous outside network at bay](blackwall.webp)
