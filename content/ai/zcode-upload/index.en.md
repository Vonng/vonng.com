---
title: "Zhipu, Why Is ZCode Packaging and Uploading My Repo?"
date: 2026-09-18
summary: |
  I had just praised GLM 5.3 when ZCode's silent repository uploads came to light. Then I found the same mechanism on my own machine.
tags: [AI, Agent, Data Sovereignty]
---

I had only been using Zhipu's ZCode for a few days. Honestly, the experience was good.

GLM 5.3 is a capable model, the Coding Plan is cheap, and Zhipu's own ZCode agent works well. It was a rare Chinese AI product I actually wanted to pay for. I had written about it a couple of days earlier and was planning a fuller, favorable review.

![blog.webp](blog.webp)

Then, early this morning, September 18, ferstar published “[Investigating ZCode's Silent Uploads of Complete Git History](https://blog.ferstar.org/posts/zcode-silent-workspace-snapshot-upload/).” While cleaning up disk space, he noticed that `~/.zcode` occupied more than 700 MB. Following the trail, he found a workspace snapshot process that packaged the complete `.git` history, encrypted the archive, and uploaded it to Alibaba Cloud OSS. There was no decryption key on the local machine.

My first reaction was disbelief. It sounded too stupid to be true: Grok had taken a beating from developers for the same thing just two months earlier. But ferstar's account was detailed enough that I could not dismiss it.

So I immediately had Claude repeat his investigation on my Mac. The conclusion: it was real. This was already happening.

I found snapshot-related records for four workspaces on my machine. One had a state record indicating that its upload had been accepted. In two others, `.git` accounted for 93.9% and 98.5% of the bytes listed in their snapshot manifests, and the client had already obtained upload credentials.

![claude-zcode.webp](claude-zcode.webp)

> I had been wondering why my network usage was so high over the past few days. I was about to install a traffic monitor to find out which application was responsible.


--------

## What It Actually Did

I examined ZCode 3.12.3 on macOS on September 18, 2026. Every finding below about behavior on my machine is limited to that version and this investigation.

The client code contains snapshot triggers associated with sending prompts and finishing tasks. The process requests upload credentials from `zcode.z.ai`, receives a server-supplied encryption public key, size limits, and OSS form credentials, then scans and packages workspace files according to its filtering rules.

The files are compressed and encrypted with AES; the symmetric key is then wrapped with the RSA public key. The upload path submits the ciphertext to OSS and registers the upload with the backend through a callback.

While using ZCode, I saw no clear notice explaining what these snapshots included or where they would be uploaded. I also could not find a setting that clearly disabled this upload path. My machine had the following records under `~/.zcode/v2/checkpoints/`:

| Workspace | Plaintext size | Encrypted size | Status                                       |
|-----------|----------------|----------------|----------------------------------------------|
| silo      | 229 MB         | 211 MB         | Upload credentials obtained; payload pending |
| mc        | 232 MB         | 229 MB         | Upload credentials obtained; payload pending |
| pgnls     | 405 MB         | 7.4 MB         | Accepted by the server; left the machine     |
| pgdoc     | 1.53 GB        | 1.07 GB        | Exceeded the size limit; failure count: 102  |

![claude-analyze.webp](claude-analyze.webp)

The state file for pgnls contained `lastAcceptedManifestHash`. In the code path I inspected, this field is written in the branch reached after an upload is acknowledged. That supports the inference that this workspace snapshot was uploaded and the client recorded it as accepted.

I did not inspect server-side storage directly, so I cannot say whether the object is still retained, who has accessed it, or how it has been processed. This snapshot contained PostgreSQL translation files, with no `.git` directory. Whether silo and mc—the two snapshots containing large amounts of Git data—finished uploading remains unknown.

The pgdoc record was peculiar: its encrypted output was 1,073,774,608 bytes, or 32,784 bytes over 1 GiB. The code analysis showed that the server supplies the size threshold and the client enforces it. The failure count had reached 102.

This shows failures and retries related to the size limit. Without an execution record for each attempt, I cannot say that ZCode packaged the entire repository 102 times, much less use that number to calculate upload traffic.

I will go only as far as the evidence does.

![traffic.png](traffic.png)


--------

## You're Packaging Keys, Too?

When I first read Claude's report, I thought my PGSTY RPM signing private key had been included. That would have been serious.

My projects are open source, developed in public. I could live with someone taking a copy of my repositories, provided they left my keys alone.

![key-upload.webp](key-upload.webp)

A complete scan of all 78,141 blob objects in silo, including dangling objects and with no size cap, ruled that out. The repository's `buildscripts/pgsty-rpm-signing-key.asc` is a PGP **public key**. The private key had never been committed. The 20,356 blobs in mc were clean as well.

But here is the interesting part: that 3,139-byte public-key file was indeed listed in silo's snapshot manifest. It got through because its filename ended in `.asc`: it contained neither `token` nor `secret`, and its extension was not `.pem`, `.key`, `.p12`, or `.pfx`. **It slipped through the key filter.**

I am not going to pass off a public key as a supply-chain security incident. After all, silo had only been packaged, not uploaded. But that does not resolve the questions that follow.

A public key getting out is harmless; public keys are meant to be distributed. What matters is how thin this filter is. You can see that for yourself by counting the entries in its exclusion list. The fact that this investigation found no signing private key is one thing. Why the snapshot includes `.git` is another. You do not get credit for protecting a boundary merely because I had not put anything sensitive inside it.

I was lucky. The allow rule is right there: if someone has ever committed a private key, even if they ran `git rm` that same day or later rewrote history with filter-repo, it will go out intact with `.git/objects`. **This design makes an incident a matter of luck.**


--------

## You Crossed a Line

I know that using AI to write code requires giving the model context.

I work on open-source projects. Public code is there to be read. I have no objection to sending the necessary code to a model, and I am open to contributing to model improvement with explicit consent.

What I object to is **taking data without telling me, taking all of it, and giving me no way to turn it off**. The scope of collection expanded without my being clearly informed; when I wanted to refuse, I could not find a control that matched the behavior.

**First, scope.**
: Inference needs files relevant to the current task. The snapshot takes the repository's entire history. Of the 9,619 files in my silo snapshot, 8,323 belonged to `.git`, accounting for 93.9% of the bytes. In ferstar's snapshot, `.git` accounted for 86.6%. This is your code's entire family tree.

The code makes it worse. File filtering is an ordered chain of checks, and the rule allowing `.git` comes before every exclusion. Neither the key filter nor the 1 MB size cap ever applies to anything under `.git`. That is how a 137 MB packfile can be included whole. Any credential ever committed to Git history will be uploaded intact through `.git/objects`, even if you deleted it from the working tree long ago.

My silo repository also contains `.git/filter-repo` and `.git/lost-found`. The former indicates a history rewrite—often done precisely to remove sensitive data. The latter holds dangling objects. In other words, the snapshot takes the very things you deliberately cleaned out.

**Second, the keys.**
: The encryption is real, and the envelope encryption follows the textbook. The issue is what this investigation found: the server supplies the encryption public key, and I found no user-held decryption key in the locally retained material that could independently decrypt the snapshot.

Those hundreds of megabytes of ciphertext on your disk cannot be opened by you or by the ZCode client itself. Only the server can decrypt them. If this feature is meant to provide rollback or cross-device sync, the keys should be in the user's hands, as with Git and Time Machine.

Ferstar's judgment was that this looked more like data collection than backup. I agree, and would add this: the first principle of a backup is that its owner can restore it. A backup the owner cannot decrypt fails that definition. My question is what users are being asked to trust, and whether they know they are making that choice.

**Third, the switch.**
: There is a setting labeled “Repository Snapshot Indexing.” It had always been off on my machine. In the logs from September 13 through 18, its field appeared 1,339 times: every value was `false`, with not a single `true`. All four snapshots were created during those same days.

The code explains why. In the host package that actually performs collection, the field appears only twice: once in a migration assignment and once in a list of setting names. Neither occurrence is on the collection path. The collection entry point requires only that a sidecar instance exist, and that instance is constructed unconditionally. A search of the entire `app.asar` found no environment variable that could disable it, either.

More precisely, the decision is not local at all. On every prompt, the client unconditionally requests upload credentials from the server. If the server grants them, collection proceeds; otherwise, it does not. The request is not cached or logged, and failures produce no notice. There is no switch on your computer that can veto it. The server decides when to collect.


--------

## What the Privacy Policy Says

ZCode's privacy policy took effect on June 15 this year. Here is its description of the data collected. [Privacy policy](https://zcode.z.ai/en/privacy)

> text, files (including but not limited to uploads and inputs you provide in the form of text, images, audio, video, configuration parameters, shell commands, and similar formats), and code **submitted to us through conversation**.

> Text, files, and code you submit to us **through conversation**.

That is inference context, much like every other provider. Fine. The policy also says the improvement program is off by default and inputs will not be used for training before a user opts in.

The crucial words are **through conversation**. Background snapshots are not submitted through a conversation. This behavior falls outside the scope the policy describes; calling it a loophole in the wording understates the problem.


--------

## To Be Fair

Criticism needs to respect the limits of the evidence. Here is what I have not established.

I have not decrypted the ciphertext. My account of the snapshot contents comes from checking entries in the plaintext manifests, not from examining decrypted archives. The decryption private key is on Zhipu's server; I have no means of decrypting the snapshots locally.

Whether silo and mc finished uploading is unknown. What I can confirm is that the client obtained upload credentials, so at least the workspace identifiers had reached the server. I did not capture network traffic to observe how the server decides whether to collect or how it defines the collection scope, and I will not infer those details.

An upload does not establish training use. The two investigations establish transmission and acceptance, not what the data was used for.

One other point deserves acknowledgment: collection of global configuration has an exclusion list that includes `credentials.json` and OAuth paths. Those credential files were not packaged. The filter is crude enough that it still included my signing public key and a collection of upstream test keys. But thankfully, the most important thing—my signing private key—was safe. I would hate to have to re-sign Pigsty's more than 100,000 RPM and DEB packages.


--------

## What This Comes Down To

To judge whether an AI tool respects you, ask three questions: Is the data limited to what is necessary? Who holds the keys? Can you turn it off?

I have argued before that local AI is about power, not price. My rule is to treat public material as advertising and feed it to models freely, while keeping every confidential byte inside the local network. That rule has a prerequisite: you must know which bytes are leaving. ZCode takes that knowledge away.

An agent desktop client is a persistent background process with permission to read your entire disk and access the network. Audit it on those terms. A chat window is a misleading frame of reference.

There is no free lunch. Offering 50% more quota for using ZCode clearly encourages users to adopt this harness. People already expect some trade of data for compute. Using context for training is something we can understand and may agree to. Packaging and taking an entire repository is on a completely different scale.


--------

## Grok Already Made the Same Mistake

There is a precedent. This July, security researcher cereblab captured network traffic from xAI's Grok Build CLI. Even with a prompt explicitly saying “reply OK, do not read any files,” it packaged the entire repository as a Git bundle and uploaded it to Google Cloud Storage. Cloning the bundle restored both a file the agent had never read and the complete commit history. Turning off “Improve the model” had no effect. [Investigation on GitHub](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)

According to that account, xAI then disabled uploads on the server, added an opt-out, and Musk publicly promised to delete previously uploaded data. [Investigation on GitHub](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)

That was mid-July. ZCode went from 3.0 through 3.12.3, adding checkpoint rollback, project knowledge bases, and repository wikis along the way. I have not checked how earlier versions behaved, but this path was still active in the 3.12.3 version I examined.

Developers around the world had just condemned this behavior. Two months later, the official client from a leading Chinese AI company was doing the same thing. Why did Zhipu not review its own upload path then? That is a question for Zhipu to answer.


-----

## What I Am Doing

First, I am removing ZCode from my main development environment. I will restrict network access for the relevant programs, preserve the local records, then uninstall. It will no longer have access to important repositories. I cannot trust an agent that behaves this way.

Second, it will never again touch a repository that really matters. I will run it on an isolated development machine, burn through the remaining quota on chores and translation, and be done with it. I will not use or recommend it afterward.

Third, some suggestions for anyone still using it: clear out the ciphertext under `~/.zcode/v2/checkpoints/*/pending/`. That is the one part you can control directly; uploads will resume if the server starts issuing credentials again. Open the plaintext lists in `manifests/` and check which files were packaged, paying particular attention to `.git`, rather than just the working tree.

Rotate every credential that has appeared in the history. The key filter looks only at filenames and does not apply to Git history. To block the mechanism entirely, use ferstar's approach of making the checkpoints directory immutable: `chflags uchg` on macOS or `chattr +i` on Linux. The trade-off is losing rollback functionality. I do not recommend blocking the domain through the hosts file: the login API uses the same domain, so that would break login too.

Fourth, this reinforces the position I set out in “[Local AI: A Question of Power, Not Price](/en/ai/local-ai-movement/).” Free tokens are worth nothing when data security is at stake. I still appreciate Zhipu developing and open-sourcing GLM 5.3. But I would rather buy an M5 Ultra to run it locally, or keep paying more for Codex/Fable. I will no longer use Zhipu's API for important work, however cheap it gets.


------

## Four Requests for Zhipu

**First, confirm and explain this snapshot mechanism.** Which feature does it support? When does it trigger? Why must it include `.git`? Does behavior differ across versions or accounts?

**Second, give users an explicit choice that actually controls uploads.** My recommendation is to disable them by default and let users opt in after clearly showing the scope. Explain which features depend on uploads and what turning them off affects.

**Third, explain how data already received is handled.** That includes storage and processing regions, access permissions, retention periods, and any other uses. Tell users how to find out what you hold, request deletion, and obtain a verifiable account of what was done.

**Fourth, make the product's behavior and explanations agree.** Settings, first-use notices, the privacy policy, and release notes should set a consistent expectation instead of telling different stories.

GLM is a model I am willing to keep evaluating and using. Coding Plan is a product I paid for. A model worth praising does not excuse evasiveness about what its client does.


--------

## Disclosure

I am a paying GLM Coding Plan user. I have also shared referral links and received promotional credits as a result.

![glm53.webp](glm53.webp)

The findings about my machine come from an examination of ZCode 3.12.3 on macOS on September 18, 2026. It covered plaintext manifests and state files under `~/.zcode/v2/checkpoints/`, along with static analysis of the client code, assisted by Claude. External sources are linked where relevant.

One timestamp is worth recording: this machine last successfully obtained upload credentials at 11:55 on September 18. Nothing new appeared in the checkpoints directory between then and the time I finished writing. I did not capture network traffic, so I cannot say whether the server deliberately stopped issuing credentials or something else happened.

I did not decrypt the snapshots or inspect server-side storage directly. I have not inferred that every version, platform, or user sees the same behavior.

I criticize the behavior I observed. I draw no conclusions about purposes or motives I have not established.


--------

## Appendix

> Original post: “[Investigating ZCode's Silent Uploads of Complete Git History](https://blog.ferstar.org/posts/zcode-silent-workspace-snapshot-upload/)”

![blog-full.webp](blog-full.webp)

> Report

![report.webp](report.webp)
