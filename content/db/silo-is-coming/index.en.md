---
title: "MinIO Nuked Its Docker Hub Repos—Your Object Storage Doesn't Have to Go Down With It"
date: 2026-09-18T00:00:00+08:00
authors: [vonng]
summary: >
  On September 11, MinIO deleted the minio/minio and minio/mc repositories from Docker Hub outright, finishing its walk out the door. Over the past month or so I put two mutually adversarial AI agents to work on Silo, the MinIO community fork I maintain, and ran a full cleanup: four releases, 210 commits, 8 CVEs, plus compatibility hardening and a zero-cost migration path. One person with a pile of top-tier subscriptions can now genuinely carry the security maintenance of a mid-sized Go project.
tags: [MinIO, Silo, Object Storage, Open Source, AI]
---

Let me nail a date to the wall first: **September 11, 2026**, sometime between 18:31 and 19:36 UTC, MinIO **flat-out deleted** the `minio/minio` and `minio/mc` repositories on Docker Hub.

Not rate-limited. Not retagged. The whole repository returns 404—"repository does not exist."

CI pipelines quietly went red all over the world that day. I poked around GitHub and found projects [filing issues the same day](https://github.com/shellhub-io/shellhub/issues/7117): `docker compose up` wouldn't come up, and what it reported was
`pull access denied for minio/minio, repository does not exist or may require 'docker login'`. A lot of people's first instinct was that their own login had expired, and they went digging through their credentials—which had nothing to do with it.
Docker Hub returns the same sentence for "repository does not exist" and "private repository, please log in," and an anonymous user cannot tell the two apart. Some spent a long while debugging before it clicked: nothing on my side is broken, upstream is just gone.

A Dutch developer put it most bluntly in an [issue](https://github.com/cloudmarktplaats/cloudmarktplaats/issues/48) on their own project:
in May and June 2025, MinIO hacked the free community edition's entire admin console into a cripple; in October it stopped publishing community images and binaries and hung "no longer maintained" on the repo;
this February the repo was formally archived; on September 11, `minio/minio` and `minio/mc` were wiped off Docker Hub entirely—not throttled, just gone.

I'm Vonng, the author of Pigsty. **Silo is the MinIO community fork I maintain.**

This is not the release notes. I wrote those separately, change by change, for people who need to read them against an upgrade. This is the retrospective—what actually happened over the past month or so,
why I picked the moment two frontier models had just landed to run a vulnerability cleanup with two AIs, and why I think it was worth it.

## How MinIO Skipped Town, One Step at a Time

To explain why Silo exists, I have to lay out the timeline of how MinIO spent the last few years killing itself. This isn't a grudge; it's a documented string of dates:

**2021.** MinIO relicensed the core server code from the permissive Apache 2.0 to the very restrictive AGPLv3
(the [groundwork was laid back in 2019](https://bizety.com/2025/12/06/minio-in-maintenance-mode-open-source-alternatives/)). The community had one round of arguing about it at the time,
but most users didn't care—I run it myself, I don't offer it as a service, so AGPL and Apache are the same to me. The real problem was buried further down the road.

**May–June 2025.** MinIO did the thing that made the community angriest: it gutted the full admin Console in the free community edition, leaving a crippled object browser. User management, bucket policies, access control,
lifecycle management—**gone overnight**. Want them back? Sure: buy the enterprise edition, starting somewhere around $100k a year.

The funniest part is that when I [brought the Console back](/en/db/minio-resurrect/) later, **no reverse engineering was required at all**. All they had done was roll the `minio/console` submodule back a version—swap one dependency version,
and the full Console turned into the neutered one. I rolled that dependency version back, and the Console returned.

**October 2025.** MinIO stopped publishing prebuilt binaries and container images for the community edition. Source only. Want to use it? Compile it yourself.

**December 3, 2025.** MinIO announced on GitHub that the community edition was entering "maintenance mode." The README said security fixes would be "evaluated case by case." I wrote [MinIO Is Dead](/en/db/minio-is-dead/) and let them have it.

**February 12, 2026.** The repository went from "maintenance mode" to "no longer maintained," then got formally archived. Read-only. A project with 60k stars and a billion-plus Docker pulls became a digital tombstone. And inside that very archived repository,
`SECURITY.md` still carries one line: "we will always provide security updates for the latest release."

**September 11, 2026.** Delete the Docker Hub repositories. This is the last step out the door, and the meanest one—every earlier step at least left you something to hold on to: the image was stale, but you could still pull it. This one takes that away too.

Join the dots and you get a very clean piece of commercial design: **archive the repo so there's no obligation to patch; keep publishing CVE advisories for visibility; then funnel everyone who reads them into the commercial product, AIStor.**
AIStor bills by capacity at $0.02/GB/month, with the enterprise self-service support tier covering up to 400 TiB—third-party evaluations put the entry price around $96,000 a year. Yes, that is the "tidy" arrangement.

Someone still has to patch the abandoned old version. That someone is me.

## Why Me, and Why AI

I had actually built my own CVE-patched binaries and switched over to them back in December 2025, when MinIO announced maintenance mode.
**Because Pigsty itself runs MinIO in production as the backup repository for PostgreSQL.** This was never "I'd like to start an open-source project." It was "the thing I depend on broke, and I have to fix it."

I started out lazy. Click Fork, build the packages, don't even bother renaming anything—the repo was just `pgsty/minio`. That was fine while I was the only user. It stopped being fine once the image had been pulled more than half a million times
and a pile of well-known open-source projects started pointing their default image at me. MinIO® is a registered trademark, an open-source license does not grant trademark rights, and I wasn't going to dump that latent risk into someone else's supply chain. So in August I did something about it: the project, the repository,
the binary, every brand-facing surface got renamed from MinIO to **[PGSTY SILO](/en/db/long-live-silo/)**, Silo for short. In the data world, *silo* is normally an insult—a data silo is the thing everybody is trying to eliminate. I took it as a name anyway.
A grain silo sits nicely next to the Pigsty pig pen, and with the pig package manager and the sow repository tool alongside it, the family is complete.

So: how does one person maintain a mid-sized Go codebase while high-severity CVEs keep landing on it? The answer is AI. But it is **absolutely not** as simple as telling an AI to "go fix everything."

In April's [Two Months Into Maintaining a MinIO Fork](/en/db/minio-promise-kept/) I described the process at the time: Codex drafts, Claude Code does an adversarial review. For this August–September cleanup the setup got an upgrade,
but the core is unchanged—**two heterogeneous AI agents fighting each other, with me refereeing from above.**

For this past month specifically: Anthropic shipped Claude Fable 5.1 on September 1, and OpenAI shipped GPT-6 Astra on September 3. Two frontier models landing back to back
is what triggered my decision to run a full cleanup—the tools were finally sharp enough that a lot of deep water I had previously marked "I know there's a problem here, but changing it is too risky" became touchable.

The division of labor went like this: **before Astra 6 shipped, Fable mostly did the design and Sol (GPT-5.6 Sol, driven through Codex) did the implementation; after Astra 6 shipped, Astra handled both design and implementation,
and Fable moved over to verification and adversarial review.** You can see the fingerprints in [Silo's commit history](https://github.com/pgsty/silo/commits/main): PR co-authors reading `Claude Opus 4.8` and
`Claude Fable 5.1`, PR descriptions carrying lines like "Codex Astra 6 (Max) adversarial review: VERDICT PASS,"
branch names with a `codex/` prefix—the branch that fixed SN-2026-011, the unsigned-header flaw, was called `codex/unsigned-amz-header-copy-20260909`. **Every AI commit ends with a line reading
`Signed-off-by: Feng Ruohang`.** That's me.

Why insist on two agents clawing at each other? Because I've found that a single agent fixing a security bug will very happily hand you a patch that sounds entirely reasonable and quietly misses one boundary condition. It is too confident.
Put a second model from a different vendor in the attacker's seat with a mandate to find fault, and most of those confident holes get filtered out. Adversarial review also forces them to write the tradeoffs down—when two implementations diverge,
one side has to spell out why A and not B. That argument happens to be the only thing I, as the person who makes the final call, can actually judge on. If the two of them agree instantly and neither explains, that's when I get nervous.

My job is **direction, arbitration, and resource allocation**. I don't read the implementation line by line—there's no way one person carries that. I define the problem, set the constraints, pick between two proposals, read the diff, run the tests, and decide whether it merges or goes back.
Real maintenance is never one clean kill; it's patches stacked on patches. The LDAP STS rate-limiting fix is the classic case: only after the first version landed did we realize that successful requests shouldn't count against the limit, that `X-Forwarded-For` can't be trusted by default,
and that the rate-limit key has to be "source IP + normalized username" rather than a single dimension—three follow-up commits before it was solid. Grinding through work like that by hand, round after round, costs an absurd amount of time.

<!-- TODO: a concrete, vivid anecdote from this cleanup where Astra and Fable deadlocked on a specific fix and I had to step in and arbitrate. -->

## What Actually Got Fixed This Past Month

All right, let's get concrete.

From early August through September 17 I shipped **four server releases**: 08-04, 08-06, 09-03, 09-16. The last one, [09-16](https://silo.pgsty.com/blog/release/silo-20260916/),
swallowed **210 commits (140 of them non-merge) in a single release**.

On security, counting the books all the way back to April: **8 CVEs plus a dozen or so project-local SN entries**; the official site's phrasing is "14 security fixes, 17 security notes." All of them are **inherited from the archived upstream MinIO**—which means
these holes will **never** be fixed in the MinIO community edition, and the official answer is to go buy AIStor. A few are worth spelling out, just to show how bad they are:

- **CVE-2026-33322, OIDC JWT algorithm confusion, CVSS 9.8.** Under certain identity-provider configurations, an attacker who knows the OIDC ClientSecret
  can mint a token claiming any identity—including the `consoleAdmin` superuser—and MinIO will accept it. The vulnerable window ran from November 2022 to March 2026. **About three and a half years.**
- **CVE-2026-34204, replication-header metadata injection.** An ordinary PUT or COPY carrying certain `X-Minio-Replication-*` headers
  can write an object into a **permanently unreadable** state. The data is still on disk; you just can't read it back out.
- **Two signature-verification bypasses (CVE-2026-40344 / CVE-2026-41145).** Anonymous or forged-signature requests on the unsigned-trailer path can successfully write objects on certain routes. These two only have GHSA identifiers,
  with no published CVSS numbers, but they're critical in nature.
- **CVE-2026-42600, ReadMultiple path traversal in the storage layer.** This one deserves more words. We started by deleting the unused internal endpoint and declaring it fixed. The audit afterward found that the endpoint was indeed gone,
  but **the underlying disease was still alive on three other protocol surfaces**: request bodies and grid frames never pass through the validation middleware, and the storage layer has no fence of its own.
  That produced [SN-2026-002](https://github.com/pgsty/silo/blob/main/docs/security/advisories.md), which settled the rest of the bill: traversal in both the path and volume dimensions, a divide-by-zero panic that crashes a node with a single frame,
  metadata that reports a truncated shard as complete, three places that allocate memory from a caller-declared value... **12 defects, every one inherited from upstream, and our diff against the affected files is pure deletion with zero added lines.**
  I wrote [a full postmortem](https://silo.pgsty.com/blog/security/cve-2026-42600/) on that lesson: fixing one endpoint is not the same as closing a whole class of vulnerability, and when you decide to leave the layer below alone, write it down where the next person will trip over it.

The September round also landed some harder work: **durable IAM revocation** (retaining delete revisions and parent revocation boundaries so old credentials can't resurrect themselves past revocation history), **multi-pool object consistency** (conditional PUT,
multipart completion, and conditional DELETE all evaluating the same logical object under a shared namespace lock), and **a full set of fixes for encryption and federated replication** (storing SSE-C ciphertext copies verbatim, preserving per-part plaintext lengths, handling Object Lock headers correctly).

A few of these holes were **reported to us by users**, and I want to name them. SN-2026-011, the unsigned `x-amz-*` header issue,
was privately reported by Oren Yomtov (@orenyomtov)—it blocks a signed PUT from being swapped into a CopyObject running with the signer's privileges. The anonymous Console share proxy issue came from jiri-pejchal;
the slow-HTTP denial of service came from @AEGEGE (issue #183); the concurrent-read crash in the CPU metrics came from @aschyolkin (issue #210).

Beyond security, a large pile of non-security defects inherited from upstream got cleaned up along the way. Many of them are **tradeoffs about compatibility and default behavior**, and that is where you can see how I draw the line:

- **Trusting the client's source address** I shipped as hardening you have to **turn on explicitly**. The upstream problem is real: `X-Forwarded-For`, `X-Real-IP`, and RFC 7239 `Forwarded` can all be spoofed.
  But the new explicit trust configuration I added, `MINIO_API_TRUSTED_PROXIES`, **leaves upstream behavior completely intact if you don't set it**. Why? Because the moment you change the default, every existing deployment running behind a reverse proxy can break.
  With hardening like this, I would rather you turn it on yourself than make the decision for you.
- **A distroless image variant**: single file, 128MB (the classic image is 199MB), with a built-in HEALTHCHECK and a writable `/data` layer. But I did **not** go and slim down the classic image—the contents of the classic image are themselves a compatibility surface,
  and upstream is exactly who burned everyone by quietly changing things underneath it. So distroless is **a new name with a new contract**; nobody's existing healthcheck or
  `docker exec mc` habit [gets broken](https://silo.pgsty.com/compatibility/feature/healthcheck/).
- **A native `silo healthcheck` subcommand**: no more needing a shell, curl, or mc inside the container just to run a probe.
- Plus regression fixes for streaming flushes in `mc watch`, bucket notifications, and S3 Select keep-alive; per-bucket CORS; serialized bucket metadata (one `metadata.lock` so concurrent writes stop clobbering each other); a proper `NoSuchBucket` when the bucket isn't there...

There's one more tradeoff I want to stress: **I don't merge every PR from outside contributors.** Take that CPU metrics race. @mrjavadseydi filed [PR #215](https://github.com/pgsty/silo/pull/215); the locking change was correct
and the regression test did reproduce the problem, but I had already implemented the same fix my own way on mainline in #214, so I closed their PR as superseded—and credited them in the contributor acknowledgments. **Closing a PR is not rejecting a contribution;
which implementation ships is a technical judgment the maintainer has to own.** Over this past month, **50 community contributors** (49 human issue/PR authors, plus separately acknowledged security reporter Oren Yomtov) took part,
and externally merged code PRs covered the go-jose and OpenTelemetry dependency CVEs, the bucket notification stream, per-bucket CORS, federated CopyObject legalhold, multipart ChecksumType, and more. **This stopped being a one-man project a long time ago.**

On compatibility, the [official compatibility page](https://silo.pgsty.com/compatibility/) sorts Silo's differences from MinIO into **12 compatibility improvements, 4 subtle differences, and 8 conditional checks**—24 categories in all,
benchmarked against the upstream 2025-12-03 source. Let me be honest about one thing: those 24 categories are **grouped by user scenario; they are not a compatibility percentage**. I'm not going to hand you a pretty "99.x% compatible" number and then let you fall into a hole.
The hard evidence I can offer is internal acceptance testing: `make verify` covers FS, erasure coding, distributed erasure coding, multi-pool, and IPv6 multi-pool, at **174 PASS / 0 FAIL**;
a [four-node TLS cluster](https://silo.pgsty.com/blog/release/silo-20260903/) went through upload/download checksum comparison on 1,004 object pairs one by one, two-site replication, single-drive rebuild, and a full rollback drill.

## What It Cost, and Whether It Was Worth It

Honestly: quite a lot.

This is **absolutely not** a matter of yelling "go and fetch all the problems and fix them" at an AI. It involves an enormous amount of weighing: which holes get fixed now and which wait; whether to change a default and whether changing it breaks existing deployments; where to draw the compatibility line;
whether an outside PR gets merged or replaced with my own implementation. AI can't make those calls for me. Only I can.

I currently hold **15 AI subscriptions**. This past month of Silo cleanup **burned through the entire quota of three of the $200 ones**, plus a substantial chunk of my own time.
(I've quoted numbers on different bases in [other posts](/en/ai/yield-with-agents/)—"running seven $200 subscriptions and burning north of 100 billion tokens," "burned four 20x subscriptions in a single day," that sort of thing. Different windows, different arithmetic;
don't hold me to the exact figures, just get a feel for the order of magnitude: **one person, a pile of top-tier AI subscriptions, and a lot of nights.**)

But I do think this was genuinely worth doing.

Why? Because in 2026, the cost of saying "I'll fix it" has changed. A year or two ago, one person carrying the security maintenance of a mid-sized Go codebase—chasing CVEs, writing patches, running adversarial audits,
keeping the supply chain alive—was basically a fantasy. Now, with two coding agents willing to tear each other's work apart, plus one person willing to referee in the middle and make the tradeoffs, it **has become feasible**.
This isn't some grand theory about open-source resilience. It's a very concrete operational fact about right now.

And it holds up a lot of real deployments. [Pigsty v4.5](https://pigsty.io/blog/pigsty/v4.5/) has moved its entire object storage module to Silo; `minio_type` now accepts exactly one value, `silo`.
Out in the world: RAGFlow's default Compose stack, Dokploy's product templates, the Helm chart for Grafana Loki, Dell's Omnia HPC platform, nixpkgs, DaoCloud's image mirror... dozens of projects already point their default image at me.
In a certain sense, this emergency fork has become **the most active and most visible MinIO fork there is**.

## If You're Still Running MinIO

The conclusion is simple: **MinIO has walked away, and deleting the Docker Hub repositories on September 11 is the latest and most final step. And you can switch to Silo.**

Silo's position hasn't changed since day one, and it comes down to one rule: **rename every product and delivery surface; don't touch a single byte of the protocol or your data.** The `silo` binary, the packages, the systemd service, the Helm chart, and the container image got new names.
But the S3 and Admin APIs, `MINIO_*` environment variables, `minio_*` metrics, `x-minio-*` headers, `/minio/*` routes, and the `.minio.sys` on-disk format are all preserved verbatim—and nailed down by CI compatibility checks.

That is my promise to existing MinIO deployments: **don't touch your data, keep fixing vulnerabilities, keep shipping images, keep the interfaces compatible.** I've always liked the tagline on the [website](https://silo.pgsty.com/):

> **S3 Interface, Libre Object Store. Keep the interface. Own the objects.**

[Migration](https://silo.pgsty.com/compatibility/migration/) is cheap. Docker users swap `minio/minio` for `pgsty/silo` and that's it: volumes untouched, data untouched, no API to relearn.
The container entrypoint even translates legacy `minio` arguments ([someone actually does this](https://github.com/ShyME/Pictogram/pull/245)), so even `command: minio server /data` keeps working.
RPM and DEB packages are on [GitHub Releases](https://github.com/pgsty/silo/releases), or install with `pig`. If you want a turnkey HA production deployment, [Pigsty](https://pigsty.io/) gives you one for free.

Something I use broke, and I'm fixing it. That's all this is. When the next CVE lands, I'll still be here.
