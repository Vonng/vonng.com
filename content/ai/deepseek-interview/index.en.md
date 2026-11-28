---
title: "The Bojie Li–DeepSeek Interview Controversy"
date: 2026-07-07
authors: [vonng]
summary: >
  Today's biggest tech drama began when Bojie Li criticized DeepSeek's interview process on Twitter: he was asked to solve online-judge coding problems, then suspected of cheating. Add the DeepSeek name, and the story exploded.
tags: [AI, LLM, Career]
ai: true
---
Today's biggest tech drama began when Bojie Li criticized DeepSeek's interview process on Twitter. In short, he went in for an interview, was asked to solve online-judge coding problems, and was then suspected of cheating. Add the DeepSeek name, and the story exploded.

> [!SOCIAL] Bojie Li `@bojie_li`
>
> A rant about DeepSeek's interview process. First, after I passed the written test, they dragged their feet for half a month without scheduling an interview—by then I already had offers in hand from other companies. Only after repeated follow-ups did they finally schedule one. None of the other companies I interviewed with required coding rounds, yet DeepSeek still required a written test plus coding interviews in both of the first two rounds—something I had never encountered anywhere else. In the second round, the interviewer felt that all the problems I described were research problems and couldn't follow what I was saying; he kept pushing me to talk about engineering challenges instead. During the coding interview, I have two monitors, and the interviewer claimed I kept glancing at my left screen, suspected me of copying code, told me to stop cheating, and said the interview couldn't continue unless I proved I wasn't copying. I felt deeply insulted and terminated the interview on the spot. Based on the two interviewers in rounds one and two, DeepSeek is completely different from what I imagined. I've decided to end my interview process with DeepSeek and share this on social media. Please help spread the word—feel free to share.
{avatar="avatar-bojie-li.webp" date="2026-07-06" platform="x"}

The internet is full of wild speculation. I know a little about what happened, and my own judgment is that Li's account is probably accurate: DeepSeek's interview process really was... less than respectful to the candidate. DeepSeek is a good company, and Mr. Cui is a decent, sincere person. The charitable reading is that DeepSeek had previously recruited almost exclusively on campus and was only beginning to hire experienced people. It lacked experience and botched the process. That is understandable.

But interviews go both ways, and a bad interview is bad PR. This is especially true when hiring experienced people: if you want top talent, you cannot treat candidates like interchangeable new graduates waiting to be sorted. Their time is valuable too. Read the comments and you will find that quite a few people who actually interviewed there have complaints of their own.

From what I know, the process has problems, and that is not good for DeepSeek.

Then people piled on Li, often viciously. What followed was even harder to keep up with. One of Bojie Li's former investors came forward with accusations; Li fired back; and the whole affair turned into an ever-larger mud fight.

> [!SOCIAL] Du Jun `@DujunX`
>
> Bojie Li is the founder with the least respect for contracts we have ever worked with.
>
> In 2024, riding the halo of Huawei's "Genius Youth" title, Bojie Li founded Metagent and received investment from ABCDE Capital. Afterward, he refused to fulfill the basic obligations stipulated in the investment agreement—including updating investors on business progress and financials—and later went completely unreachable.
>
> Venture capital can accept all kinds of project failures, but it cannot accept the fraud of a founder taking the money and disappearing.
{avatar="avatar-dujunx.webp" date="2026-07-07" platform="x"}

> [!SOCIAL] Bojie Li `@bojie_li`
>
> Under the investment agreement, your firm committed $1.5 million, of which only $500,000 was ever wired; the remaining $1 million never arrived. Yet the company always recorded your firm's equity on the cap table at the full $1.5 million share. Because the funds kept failing to materialize, both my co-founder and I voluntarily cut our own salaries, and hiring and R&D ran into serious trouble. In October 2024, for personal family reasons I could not leave mainland China, where Web3 projects are non-compliant, so I resigned from Metagent with board approval. Up until my departure, as CTO and co-founder, I consistently fulfilled my duty to report the cap table and business status on schedule. And in accordance with the non-compete clause, I deliberately stayed away from Web3, AI infrastructure, and image generation in subsequent startups.
{avatar="avatar-bojie-li.webp" date="2026-07-07" platform="x"}

I do not know Li, and titles like Huawei's "Genius Youth" do nothing for me. But publicly pillorying someone for describing his own experience is wrong. I can understand why an expert with a proven body of work and reputation would feel insulted when a company subjects him to the same rote questions it uses for bulk résumé screening.

I also know that this was surely not DeepSeek's intention. DeepSeek is a good company, and I hope it does not become an untouchable "You-Know-Who" that nobody is allowed to criticize. That would be bad for DeepSeek itself. It cannot control every overzealous fan online, but it certainly can take candidates seriously and treat them with respect.

## How Should We Evaluate Talent in the AI Era?

Now that AI can reliably generate routine code of low to moderate complexity, I think evaluating people with LeetCode-style algorithm problems is pointless. Give those problems to Codex or Claude Code and they will knock out one every few minutes, better than almost anyone coding by hand.

Once the ability to write such code becomes universally available at nearly zero marginal cost, it is like calculating square roots by hand: no longer useful as an evaluation criterion. Nobody tests how quickly you can compute square roots or logarithms by hand—a cheap calculator will crush any human. What matters is the ability to discover, define, and decompose problems; technical taste and the judgment to validate results; and the basic competence to run the entire process end to end.

In my view, grinding online-judge problems is mostly for new grads. I used to do plenty of it myself and, at my peak, even won my company's coding contest. Ask me to do it now and I probably could not—rather like asking you to sit the chemistry section of China's college entrance exam today.

After all these years, databases, Postgres, and startups have long since filled my memory. That low-level coding material was swapped out ages ago. If forced, I could probably grind through a problem in an hour or two. But insisting on writing by hand what a single prompt can solve is simply a waste of time.

I do not think these useless OJ problems help identify talent. They are easy for people who know nothing but test prep to game, so the process ends up selecting a crowd of professional test takers. Just look at Shing-Tung Yau's mathematics program at Tsinghua: it too got reward-hacked.

> [!SOCIAL] 大漂亮| C Labs `@giantcutie666`
>
> Tsinghua's Shing-Tung Yau math program admitted a batch of students through its independent recruitment track. Yau gave them a surprise test using the Beijing Gaokao math paper, and the average score was 110 (out of 150).
>
> Yau was furious and wanted to expel everyone who failed and make them retake the Gaokao.
>
> The university leadership hasn't approved it yet out of fear of the parents' backlash 😅
>
> Word is this happened mainly because test-prep agencies reverse-engineered the admission playbook for Tsinghua's Leading Talent program.
>
> Personally I don't think it's that simple—at the very least, the exam questions leaked 😁
>
> ![Collage of screenshots discussing Tsinghua's Qiuzhen College admissions and parent group chats](reward-hacking-media.webp)
{avatar="avatar-giantcutie666.webp" date="2026-07-06" platform="x"}

A different evaluation would be far better. Give the candidate a terminal and have them figure out how to provision a virtual machine and configure Linux and Codex. Then give them a real task of moderate difficulty and watch how they direct Codex with prompts to get it done. Finally, have them submit the complete session and let an AI evaluate it.

When I interviewed at Apple eight years ago, the team lead gave me a problem drawn from the team's own work: they had a huge volume of data to load into Postgres. How fast could I make it? I thought that was a fascinating challenge. From parallel `COPY` and parallel `INSERT` to bulk loading and every trick in the book, I used quantitative analysis, profiling, and testing to choose the parameters. The entire process was interesting, challenging, and practical. It left an excellent impression.

There is another point. If someone already has public work and a reputation to vouch for them, making that person grind generic programmer puzzles while watching them like a suspected thief is not merely rude; it borders on humiliating. The canonical example is Google rejecting Homebrew's creator because he could not invert a binary tree by hand. Nobody thought, "Wow, Google's standards are impressively rigorous." They just laughed at how stupid the process was.

![The Homebrew interview anecdote](featured.webp)
