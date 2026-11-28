---
title: "Did T3 Code Hurt Chinese Developers’ Feelings?"
date: 2026-11-25
authors: [vonng]
summary: >
  Someone mistook a T3 Code fork for the real thing, and Xiaoxin renamed it within 19 minutes of Theo asking him to. The two talked it out, but Chinese Twitter kept fighting over “Temu3 Code.”
tags: [AI, Open Source, Commentary]
images: [featured.jpg]
---

Theo’s team built T3 Code, an MIT-licensed control plane for coding agent harnesses. It lets you run Claude Code, Codex, OpenCode, and Antigravity from a single chat interface. I’ve been using it myself. There are plenty of agent harnesses around, and T3 Code is about the best third-party open-source chat interface I’ve tried. Gemini has been on a tear lately, but Antigravity still sucks. You can use Gemini directly in T3 Code, so users came flooding in.

Over the past couple of days, this project got into a fight with Chinese-speaking Twitter. I watched the whole thing. The people involved sorted it out in 19 minutes. The bystanders were the ones who got their feelings hurt.

## What happened

The sequence is pretty simple.

1. **November 20.** A developer who goes by Xiaoxin (@DDdxx666) announced “T3 Stardust Edition” on Twitter. It was his first public open-source release. He’d made extensive changes to T3 Code and said so in the description. The repository and the app still had T3 in the name, and the icon was still T3’s.
2. **On the afternoon of November 23,** a blogger named Suyuan (@suyuan1711) mistook the fork for the official release and tweeted about the mess on his screen. There were two “Ask” boxes crammed into one view, and the same pending sessions showed up at both the top and the bottom.
3. **A little after 7 p.m. that evening,** Theo quote-tweeted the complaint. He thought there was a “Chinese knockoff”[^1] going around, because that definitely wasn’t his team’s app. Ten or so minutes later he added, “Temu3 Code.”[^2]
4. **Right after that,** Xiaoxin replied that he’d consider a less confusing name. “Not consider. Do it right now,” Theo shot back.[^3] He threatened to have GitHub take down Xiaoxin’s account if he didn’t rename the fork.
5. **Nineteen minutes later,** Xiaoxin had renamed the repository “Stardust Agent,” removed the T3 name, logos, and icons, and clearly labeled it an unofficial fork. Suyuan downloaded the official app, tried it, and publicly apologized for blaming the upstream team.[^4] Xiaoxin and Theo talked at length in private. Xiaoxin later tweeted, “I can take being told it sucks. I can take criticism.”[^5] He also made a point of saying, “Theo and I have been talking since yesterday. There’s no beef between us.”[^6]

That should have been the end of it. The misunderstanding was cleared up, the fork had a new name, and the two developers were on good terms.

The next day, Chinese Twitter blew up. Screenshots of “Chinese knockoff” and “Temu3” made the rounds, accompanied by accusations of racism. Someone dug up a line from the README, `If you don't like something, fork it`, and accused Theo of hypocrisy.

Theo has never been known for his patience. After a day of people piling on, he lost his temper and fired off a string of replies.[^7] He stood by what he’d said and started taking shots of his own. Around noon that day, the team added `TRADEMARK.md` to the T3 Code repo and changed the README to say `fork it under your own branding`.

## Does the name come with the fork?

Underneath all the outrage is a basic rule of open source. **You can take the code. You’ll need your own name.**

The MIT license lets you use the code, modify it, redistribute it, even sell it. Those permissions come from copyright law. Forking a project doesn’t give you the right to use its trademarks, any more than it gives you its reputation.

That’s been the custom in open source long enough that plenty of small projects never bother writing a trademark policy. They assume everyone knows the drill. Debian packaged Firefox as Iceweasel. When Redis changed its license, the community called its fork Valkey. The Terraform fork is OpenTofu. The Elasticsearch fork is OpenSearch. Any self-respecting fork goes out under its own name.

It’s easy to see why. Suppose you take my project, vibe-code it into a piece of shit, and keep the original name. Your users can’t tell which version they have. Who do you think they come to yell at? I’d be pissed too. That’s exactly what happened here. The amateur-hour bugs in the screenshot came from the fork. The T3 team got chewed out in front of tens of thousands of people.

I follow the same rule in my own open-source work. When I forked MinIO, the object store, I really didn’t want to rename it. Think of the repos, package names, container images, docs, and users’ scripts. Changing the whole lot is a pain in the ass. But MinIO is a registered trademark. I did the work and called the fork **Silo**.

[Silo: A Maintained, MinIO-Compatible Object Store](/en/db/long-live-silo/)

I’ve taken the easy way out too. I recently [took on a fork of VectorChord](/en/pg/maintain-vchord/), a PostgreSQL vector extension, and kept the extension name, `vchord`. I checked three things first. The original author was fine with it and wasn’t going to sue. They hadn’t registered a trademark. And by calling the fork `vchord`, I was already dropping the VectorChord brand in favor of the extension’s name. With all three settled, I could spare everyone the trouble.

People brought up Anthropic. When Claude Code borrowed T3’s sidebar design, Theo was happy to let a trillion-dollar company use it. Here was a Chinese developer working on his own, and Theo threatened to get his account suspended. A double standard? Anthropic borrowed an interaction design. The app was still called Claude Code. You’re welcome to copy the feature. Passing your work off under someone else’s name crosses a line. The same rule covers both cases.

As for Xiaoxin, I thought he handled it well. It was his first open-source release. I can understand how he missed the trademark issue. Once someone pointed it out, he had everything cleaned up and renamed in 19 minutes. He took the criticism on the chin and talked it through with the upstream author. Someone spotted a problem, and the person who could fix it did. That’s a pretty healthy open-source interaction.

## When a free user becomes a liability

Theo has a foul mouth and a short fuse. Xiaoxin made an honest mistake. Of everyone in this mess, the outraged spectators left the worst impression on me. I’ll spare you the screenshots of the abuse they hurled.

Open source runs on **prosumers**, people who both make the software and use it. We’re building tools for ourselves. The people who write code, fix bugs, and keep projects running are at the center of it. Even if you only use the software, you can sponsor the project, tell other people about it, or file a few good issues. All of that helps.

But suppose you haven’t paid a penny for the software and can’t even tell the official release from a heavily modified fork. If you still show up in the author’s replies to lecture him and demand an apology, you’re a **net liability** to open source. Nobody’s begging you to use the thing. The T3 Code website even has a button that says `Steal our code (legally)`. Go ahead and take it. All they ask is that you give your version its own name so they don’t have to take the blame for it. Is that really too much to ask?

## It was a good Temu joke

Back to the joke that set everyone off. “Temu3 Code.”[^8]

Temu is Pinduoduo’s overseas brand. On the English-speaking internet, “the Temu version” is shorthand for a cheap imitation. Here was a fork with two input boxes on the same screen and double vision in the session list. I laughed. Two words and you knew exactly what he meant. On the Chinese internet we do this to each other every day. We call things “the *Pinxixi* version,” using our own mocking nickname for Pinduoduo. We say much nastier things without anyone taking it as a personal insult. When your UI really is that shoddy, you can laugh and go fix it.

> [!SOCIAL] Theo - t3.gg `@theo`
>
> Temu3 Code
>
> > [!SOCIAL] Theo - t3.gg `@theo`
> >
> > I think there's a Chinese knockoff of T3 Code going around because this definitely is NOT our app x.com/suyuan1711/sta...
> {avatar="avatar-theo.webp" date="2026-11-23" url="https://x.com/theo/status/2124823227570745504"}
{avatar="avatar-theo.webp" date="2026-11-23" url="https://x.com/theo/status/2124825920808829077" platform="x"}

As the fight went on, people on Chinese Twitter worked Theo into a genuine rage. Yes, he led with the nationality in “Chinese knockoff,” and he was brusque about changing the name immediately. It started as a dig at the fork from someone in a hurry to protect his brand. Then people swarmed his replies to tell him how serious this was and call him a racist. By the next day he was fighting back in earnest. “What a sensitive fucking community,” he wrote.[^9] He also asked, “‘Temu3 Code’ is a racist joke?”[^10] Then he went after a whole group, sneering that apparently Chinese developers were allowed to steal trademarks. He started taking potshots at what he called “Chinese style.”

I didn’t enjoy reading those later tweets. Who wants to see their fellow developers written off in one go? I can also see how he got there. He started out responding to a screenshot of someone else’s bug with his project’s name on it. We all got to watch him get goaded, step by step, into lashing out at Chinese developers in general. Make every technical dispute a matter of national pride and call someone a racist for good measure, and look what you get. A fresh round of ugly comments about Chinese developers, and one more reason for people to think the Chinese-speaking community can’t take a joke.

Some of this comes down to being comfortable in your own skin. A confident developer can hear “the Temu version,” have a laugh, and go back to writing better code. Getting defensive over a single wisecrack gives the opposite impression.

> [!SOCIAL] Theo - t3.gg `@theo`
>
> They're writing essays about a 2 word joke tweet. What a sensitive fucking community
>
> > [!SOCIAL] 独立开发者William `@DLKFZWilliam2`
> >
> > For those who missed the drama, here's the full story behind today's Theo and T3 Code incident. I couldn't stand it anymore, so I went straight to posting a callout.
> >
> > It's simple: a blogger in the Chinese community posted a complaint about the UI of a Chinese version of T3 Code—two Ask input boxes on the same screen, and pending conversations duplicated above and below. Then the original author, Theo, saw it and retweeted it, immediately declaring: "There's definitely a Chinese knockoff of T3 Code going around, because this is absolutely not our app."
> >
> > And that wasn't the end of it. Forty-eight minutes later, he retweeted his own tweet and added a snide "Temu3 Code."
> >
> > For those who don't spend much time in English-speaking circles: Temu is Pinduoduo's overseas version. On Twitter in Europe and the US, calling something the "Temu version" is basically outright contempt—the subtext is "cheap, shoddy, slapdash Chinese knockoff." First he slaps on the label "Chinese knockoff," then follows up with the mockery of "Temu3 Code." The condescending arrogance and prejudice practically ooze out of it.
> >
> > T3 Code is an open-source project under the MIT license, and your own GitHub repo's README spells it out in black and white: "Open. MIT licensed. If you don't like something, fork it." When someone takes the MIT license you yourself signed and openly forks the code, localizes it into Chinese, and tweaks the interface, that's called a…
> {avatar="avatar-dlkfzwilliam2.webp"}
{avatar="avatar-theo.webp" date="2026-11-24" url="https://x.com/theo/status/2125067761806434581" platform="x"}

## Chinese developers have a reputation to protect

Let’s be honest. Chinese developers have had a reputation problem in international open source for a while. Some of that comes from our history and some from how things work back home. Think of Pinduoduo, or Tencent’s legal team, nicknamed “the Nanshan Invincibles,” or any number of past run-ins over open source and intellectual property. We all know Chinese developers start with a negative score.

Take Alibaba Cloud RDS. A while back it launched a product called “RDS Supabase.” Supabase is open source. It’s also a registered trademark. Selling your own commercial cloud product under someone else’s trademark is a lousy way to do business. The CEO of Supabase took a public dig at us over it, questioning whether hacker ethics even existed in that part of the world.[^11] I wrote about it in [Alicloud “Borrowed” Supabase, the giant free loader](/en/cloud/aliyun-supabase/).

> [!SOCIAL] Paul Copplestone - e/postgres `@kiwicopple`
>
> \>hacker ethics
>
> I think you are assuming this exists in that part of the world 😅
{avatar="img/paul-copplestone.png" platform="x"}

Then there are the homegrown operating systems and databases. China has two or three hundred supposedly homegrown databases on the market. Pop the hood and about half are descendants of PostgreSQL. It’s one thing to fork Postgres and hack it to pieces. It’s another to turn around and advertise the result as “100% developed in-house.” Try explaining that to the rest of the world with a straight face. It’s embarrassing.

That’s been changing over the past few years. Just look at the open models coming out of China. One after another, they’ve been hits around the world. Chinese developers have taken the lead in open-weight models and earned real goodwill for it.

Plenty of Chinese open-source infrastructure projects are finding users abroad too. More than half the users of my own projects, the Silo object store and the Pigsty distribution, are outside China. It’s taken a lot to shake those old stereotypes. For once, we’re getting somewhere.

## How you earn a reputation

Open source has always been a place to argue the merits and let people judge your work. I’d rather we stopped making enemies over pointless Twitter fights. Ganging up on people and calling them names won’t scare anyone into respecting Chinese developers. You earn that respect one commit, one patch, one release at a time.

Take the community I know best, PostgreSQL. I work on extension distribution, packaging hundreds of extensions as native RPMs and DEBs. I helped bring the Simplified and Traditional Chinese translations of PostgreSQL’s messages to 100% coverage. Both went into PostgreSQL 19. I maintain docs, run mirrors, and report bugs upstream. None of that is going to trend on social media. Do it long enough and people get to know you. Look at Chao Li. He spent two years quietly working on PostgreSQL internals and earned his place in the core development community. Nobody kept him out for being Chinese. Nobody waved him through for it either. Code is code.

The people involved have moved on. Xiaoxin changed the name. Suyuan apologized. Theo and Xiaoxin talked it out privately, and the rules are in `TRADEMARK.md`. The bystanders who are still dragging their hurt feelings into international forums are, to put it bluntly, taking a shit in a space we all share. Every bit of respect Chinese developers enjoy today was earned by colleagues and people who came before us doing the actual work. It gets old watching someone who hasn’t written a line of code stand on the sidelines all day and piss that goodwill away.

Barking on Twitter doesn’t accomplish much. In tech, what counts in the end is whether the product delivers. If you think T3 Code is bad, or you just can’t stand Theo, the best comeback is to fork it. Give it your own name, fix the things that drive people nuts, and build a better damn product. Pull that off and you’ll have the world’s respect without having to chant a single slogan.

Theo can run his mouth on Twitter all he likes. People will keep using T3 Code because it’s good. What can you do? I’d say Anthropic is about as hostile to China as a company can get. I can’t stand the company myself. I still use Claude because right now it’s the best at writing code.

Besides, take my $200 Claude Ultra subscription. I can squeeze $10,000 worth of compute out of it in a month. Even at an 85% gross margin, Anthropic loses more than $1,000 on me. And all the work I do with it is on public open-source projects, so they get no private data out of me either. The more I use it, the more they lose. That’s how you actually draw blood. As the old Chinese saying goes, learn what your rival does best and use it against them.

If you’re really that pissed off, build something better and beat them head to head, or find a way to make it actually cost them something. You can bark from behind a screen all day. It won’t cost them a dime. If all you’ve done is damage the reputation other Chinese developers worked so hard to earn, what was the point?

[^1]: [“Chinese knockoff”](https://x.com/theo/status/2124823227570745504)

[^2]: [“Temu3 Code”](https://x.com/theo/status/2124825920808829077)

[^3]: [“Not consider. Do it right now”](https://x.com/theo/status/2124829315657576890)

[^4]: [Suyuan’s public apology](https://x.com/suyuan1711/status/2124842065158959273)

[^5]: [“I can take being told it sucks. I can take criticism.”](https://x.com/DDdxx666/status/2125200657816998014)

[^6]: [“Theo and I have been talking since yesterday. There’s no beef between us.”](https://x.com/DDdxx666/status/2125244948635377950)

[^7]: [Theo pushes back](https://x.com/theo/status/2125070353663967644)

[^8]: [“Temu3 Code”](https://x.com/theo/status/2124825920808829077)

[^9]: [“What a sensitive fucking community”](https://x.com/theo/status/2125067761806434581)

[^10]: [Theo on the accusation of racism](https://x.com/theo/status/2125084297048780888)

[^11]: [What does Supabase think?](/en/cloud/aliyun-supabase/#what-does-supabase-think)
