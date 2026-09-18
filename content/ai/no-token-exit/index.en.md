---
title: "No Tokens? Drop Out. And That's Putting It Politely"
date: 2026-09-02
authors: [vonng]
summary: >
  A slide from a Nanjing University course said CS students without tokens should drop out immediately, and the Chinese internet split down the middle over it. What the fight is actually about: the junior jobs AI is erasing, an education system that cannot supply what students need, and why young people now have to build their own ladder.
tags: [AI, Agent, Education, Programmers]
ai: true
---

First day of the new school year, and here's the news. A screenshot of a lecture slide from a new course at Nanjing University, one of China's top schools, with one line in red: **CS students without tokens should drop out immediately**. The screenshot went from Bilibili, the Chinese YouTube, to Weibo, to Zhihu, China's Quora, to Tieba, Baidu's sprawling forum network. It hit the trending lists, and the Zhihu thread piled up more than four hundred answers. People in tech mostly said he was right. People outside it mostly said: let them eat cake. Reviews were split.

It took me until now to write this, because I spent the week pedaling all ten of my subscriptions until they were dry. What I want to say is simple. You can tell at a glance that this professor has the goods and knows the territory. And he's right. Not just right: I think he was being polite.

---

## What the Screenshot Left Out

The screenshot comes from the slides for a new course at Nanjing University. The red line reads: "**CS students without tokens should drop out immediately**." It spread across Bilibili, Weibo, Zhihu, and Tieba, and [the Zhihu thread about it](https://www.zhihu.com/question/2075868388124004913) collected hundreds of answers and climbed the trending list. Support and pushback both. The question nobody could get around: is telling students to buy their own tokens a "let them eat cake" move?

![](screen.webp)

The course at the center of this is called Generative Software Engineering, offered for the first time in fall 2026, ungraded, pass/fail only. I fast-forwarded through the two lectures he has posted publicly, a bit over three hours of video. The class has exactly three rules:

1. No artisanal coding;
2. You pay for your own tokens;
3. But no Tokenmaxxing required.

He had originally planned to line up a vendor sponsorship, because making students pay out of pocket felt wrong to him. Then he looked at the enrollment numbers, decided the sum was too small to go asking for, and simply wrote "you pay" into the rules. The whole course runs on `deepseek-v4-flash`. He suggests students top up ¥100 (about $14) for the semester, and joked that the class would be outsourcing its homework to DeepSeek's founder. Then he added one more line: **if money is genuinely a problem, come talk to me.**

That line got cleanly amputated on its way around the internet. The "drop out" line wasn't an opener either; it came at the end of a long windup. He starts with three anxieties CS students share: the professor uses Doubao, ByteDance's ChatGPT, to write the assignment and the student uses Doubao to do it, so the only party in the loop getting no training is the student; you study hard for four years and discover the AI already knows everything you learned; and every résumé in fall recruiting season looks exactly like every other one.

He once received a "perfect résumé"—papers in CCF-ranked journals (the China Computer Federation's tier list is the coin of the realm in Chinese academia), accepted, under review, the full set. He gave it a zero. No GitHub. No personal site. Not even a preprint.

Only then does he say it:

> Personal opinion, but any student without paid tokens in hand should drop out immediately.

What he actually means is: **tokens are the lab consumables of the AI era**. If you want to make a living in computing, you treat them the way a chemistry student treats reagents—an obvious cost of doing the work, not something you sit around waiting to be issued.

---

## Why Should Students Pay?

The objection: chemistry students don't buy their own reagents, the lab does. Physics students don't buy their own equipment, the school does. So why, in CS, do tokens come out of the student's pocket? Nanjing University is not poor. It can't cover a few dozen yuan of tokens?

That punch lands. My answer is this: **because the university has no idea how much to hand out, to whom, or how to teach with it.** Compute at Chinese universities has long been locked up in the big-name research groups; an undergraduate has essentially no path to a large-scale training environment, and the budget line "undergraduate consumables" does not exist. This isn't Nanjing being cheap. The entire higher-education system simply hasn't gotten around to funding this yet.

If a course makes a paid tool a hard requirement, the school owes students basic access to it. Educational opportunity shouldn't reduce to who can afford the bill. A professor covering the gap out of his own pocket deserves credit, but it is no substitute for a stable course budget.

Some places have already worked out that putting AI in the hands of the next generation matters. On July 29, Taipei's Department of Youth Affairs announced an [AI tool subsidy for young people](https://youth.gov.taipei/announcement/news/53606034-2305-44ea-bb00-82a40719c1d1): residents aged 18 to 35 who meet the residency, enrollment, and coursework criteria can claim up to NT$4,000 a year (about $125) against a personal AI subscription, and up to NT$8,000 for low-income and lower-middle-income households. Hsinchu City started [a similar program](https://dgservice.hccg.gov.tw/serviceNotice.do?id=1323&rule=guest) back in April.

The vendors are running student offers too. On August 19, Google announced that eligible US college students get [a free year of Google AI Pro](https://blog.google/innovation-and-ai/products/gemini-app/student-offer-google-ai/), with students in 140-plus other supported markets getting a free year of AI Plus. OpenAI's [2026 back-to-school offer](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) gives eligible US college students four free billing months of ChatGPT Plus.

On the mainland, Alibaba Cloud runs a student program that hands you ¥300 in credit once you verify your enrollment. Barely anything, but half a loaf beats none. Getting tokens out to the schools is going to be a long march.

Honestly, he isn't asking for much. ¥100 for a semester. But none of this is the student's problem to solve. **What nobody issues you, you bring yourself.** Nobody owes anybody anything here.

---

## Pulling Up the Ladder

Back in February I wrote [*New Programmers in the AI Era: Where Do You Go?*](/en/ai/ai-survival/), arguing that AI had knocked out the bottom rung of the programmer's career ladder. Six months on, I need to revise that. It isn't the bottom rung. It's the whole ladder.

The ladder CS students used to climb was called **the junior job**. Internship, campus hire, three years to mid-level, five to senior. You climbed it writing bad code, stepping on rakes, and getting chewed out, and your judgment grew one rung at a time. That path held for decades. Everyone in my generation came up it.

The ladder is gone.

A year or two ago, if you were starting a small company, what was the optimal play in that patch? Hire ten interns and give each one an AI subscription, right? In the July 2026 patch, the optimal play changed: **skip the interns; one person drives ten subscriptions.**

This isn't a forecast. It has already happened. A study from the Stanford Digital Economy Lab, updated in 2026, analyzed US payroll data from ADP and found that employment among 22-to-25-year-olds in occupations with high AI exposure sits about 19% below where it would be had it tracked their peers in low-exposure occupations, **and the gap comes mostly from reduced hiring rather than mass layoffs**. The entry door is taking more pressure than the senior ranks.

I'm running ten subscriptions myself and pedaling hard. [Pigsty](/en/pigsty/v4.5/) and [Silo](/en/db/long-live-silo/) are the kind of work that would have needed a hundred-person team a few years ago; [one person handles them now without breaking a sweat](/en/ai/yield-with-agents/). DHH runs a company and still turned out Omarchy essentially single-handedly. I covered all of this in [*AGI Machine Guns Are Now Standard Issue*](/en/ai/ai-machinegun-for-everyone/), so I won't rehash it.

And the patch may change again in a few days. OpenAI is supposedly shipping Astra the day after tomorrow, which is said to dispatch a swarm of smaller agents on its own initiative. If that holds up, the leverage available to a solo operator goes up another order of magnitude.

The old stratagem—lure them onto the roof, then take the ladder away—assumes somebody did it on purpose. Nobody is tricking anybody here. The people who got up first simply turned around and noticed the ladder wasn't there anymore. For everyone still on the ground, one option remains: **build your own.**

---

## Five Percent

Here's a statistic I collected with my own eyes. In June I gave a PostgreSQL talk at Xidian University, one of China's serious engineering schools for computing and electronics. I asked the room two questions.

First: raise your hand if you can chat with an AI. More than half the room went up.

Second: raise your hand if you have used Codex or Claude Code to do actual work. A scattering of hands. Eyeballing it, under 5%.

That's the funnel. People who can chat with an AI: by OpenAI's own accounting, ChatGPT is past a billion weekly actives, one-eighth of the human race. People who can direct an AI to do work? Codex just celebrated crossing 25 million daily actives, but that is the count after it was folded into the ChatGPT desktop app; a few months ago, on its own, it was around two million. My estimate for the number of people who can genuinely put an AI to work is in the low millions.

Narrower still: the people who can actually drain a subscription's quota. Look at the follower count of Tibo, the patron saint of Codex resets—under 500,000, and plenty of those are on Plus only. My guess for people who can run a 20× Pro plan to empty is no more than 200,000. Animals like me, running ten plans and blowing out all ten, billions of tokens a day: at the outside, tens of thousands of us.

**At a school like Xidian, dedicated to this field, only 5% of the room has ever touched the ladder.** **The other 95% are still on the ground waiting for the school to issue one.** The school can't. That is the entire context behind Jiang Yanyan's line.

---

## Nobody Is Going to Hand You a Ladder

It isn't only schools that can't issue one. Your employer may not either. When an AI rollout stalls inside a company, the reason is often laughably simple: management won't expense the API, so employees buy their own subscriptions. Better companies reimburse; worse ones don't. My view: **buy your own tokens even if your boss won't pay.** That is the variable that opens the gap. AI isn't going to take your job. Someone else holding AI is going to out-compete you for it.

Employees won't volunteer either. If AI makes you ten times more productive, what's waiting for you is not ten times the pay; it's ten times the work. So everyone is better off standing still together. That's a Nash equilibrium. The price of the equilibrium, of course, is that the whole company gets displaced by companies outside it that did embrace AI—metabolism at the corporate level. Big firms die slowly and can coast a while longer, but not forever.

The school won't issue it, the boss won't expense it, the colleagues won't move. All three layers of the organization are standing still. So stop waiting. **Nobody in this era is going to hand you a ladder. You bring your own.**

---

## What Four Years of College Are For

So what should you actually study for four years? I've thought about it for a long time, and the answer is still the boring one: **math, English, computer science fundamentals, plus firsthand experience on AI projects**. For anything else on the transcript, I struggle to make the case.

Fundamentals matter more than they used to, not less. Operating systems, architecture, networking, databases: the point isn't to reimplement each one by hand. The point is to know what a correct result looks like, which designs will be slow, and where something is eventually going to break. Without those concepts, you can't tell whether the AI is saving you time or just dressing an error up to look more like an answer.

The ability to hand-write a red-black tree or a dynamic programming solution is heading toward zero value. Understanding its invariants, its complexity, and the boundary where it stops applying is still the basis for judging whether an implementation is any good. You learn C not for the interview, but to see memory, concurrency, and system calls—the things high-level abstractions usually hide from you.

When Jiang brought up that zero-score résumé in class, I don't read it as a dismissal of papers. Papers, competitions, and open-source projects each prove different things. What actually bothered him was a résumé full of impressive nouns with almost nothing anyone could click into, run, and verify. GitHub, a personal site, technical writing, and reproducible projects are becoming a second credential alongside the transcript. Work that anyone can check in public is worth more every year.

This summer I helped a relative's kid sort through his college choices; he ended up doing CS at BUPT, Beijing's telecom-and-computing university. What I told him then is close to what I'm writing now. Junior programmers are badly oversupplied. Once you're in, what matters is finding a mentor, finding opportunities, and learning to teach yourself; the coursework itself isn't worth much. Buy a MacBook. Subscribe to ChatGPT and Claude. Ask a lot of questions, talk to the professors and upperclassmen who are actually good, and never hesitate to skip a blow-off class you can get away with skipping.

---

## Waiting Tables at Laoxiangji

If you can use AI, this is a window with gold lying on the ground. It is a rare historical opening: the chance to grow up alongside a revolutionary technology that is rewriting the world. If you can't use it well, or you reject it outright, the same window is a sword of Damocles over your head.

The polarization in the next few graduating classes is going to be frightening. The sharpest ones will graduate already able to command an army of agents and ship something that makes people's jaws drop. The ones who coasted through four years reading off the slides and doing nothing else—right now there's still Laoxiangji, the home-style fast-food chain on every corner, where they can wait tables. Four years from now, there may not even be tables to wait.

The industry genuinely does not need this many beginners. Brutal as that is, computing still leaves one exit that other fields don't: if you can't grind your way up inside it, take the AI toolkit into another domain and work the seam, where you'll be bringing a gun to a knife fight. Don't expect an easy ride there either. People in those fields are learning AI too.

So for young people just entering the field, my read is the old Dickens line: it is the best of times, it is the worst of times. For those at the top, a golden age. For the average and the below average, a painful one. Jiang Yanyan says no tokens, drop out. I think he was being polite. **No tokens, no initiative: if you don't drop out now, you'll hit the market in four years and get the same outcome, or a worse one.**
