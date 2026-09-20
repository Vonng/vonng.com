---
title: "I Asked Claude to Profile Me and Value My One-Person Company"
date: 2026-08-29
authors: [vonng]
summary: >
  I asked a neutral Claude with no memory of me to assess PGSTY and estimate what it might be worth.
tags: [AI, Claude, Pigsty ]
ai: true
---

I run a one-person company. Literally one person, running a specialist shop for PostgreSQL distributions. In 2022, I joined MiraclePlus's S22 batch. Dr. Qi Lu valued the business at RMB 100 million and suggested I raise money on that basis. Between the pandemic and a miserable market, I never managed to raise that next round. The startup fizzled out, and I became a solo operator for real.

Then, working on my own, I gradually became profitable. Fundraising stopped mattering much. A few cloud vendors have also made offers over the past two years, with an acquihire in mind, putting the valuation at RMB 120–150 million. Of course, the operative word in an estimated valuation is *estimated*. Talk is cheap.

Still, I was curious: what is a company like this, with just one person, actually worth? So I picked a Claude subscription account with no personal memory or conversation history and called in the resident “expert” to profile me and put a price on the business. Plenty of people now use Claude's judgment as a reference. An assessment from a neutral Claude with no prior history seemed worth a look.

AI-generated content in this article: **95%**

---

> [!NOTE]
> The following is Claude Code's response: [shared conversation](https://claude.ai/share/4f50c7cd-a1b5-4543-ad50-b0409b092d4c).

I read his personal website, including the “Life Journey” and “About” sections, his 2023 and 2025 annual reviews, and his interview with modb.pro, along with some external coverage. Here is my assessment.

---

## First, the Basic Facts

Ruohang Feng, known online as Vonng, was born in the 1990s. His own account of his career includes architect, DBA, and full-stack roles at Alibaba, Tantan, and Apple. He was interested in AI as a student and started as an algorithm engineer, then moved into databases after concluding that entire information systems revolve around them. Working with one of China's larger PostgreSQL deployments at Tantan convinced him to go all in. In 2022, he secured seed funding from MiraclePlus, selected from more than 5,000 projects, and began working on Pigsty full-time. He translated *Designing Data-Intensive Applications* (DDIA) and *The Internals of PostgreSQL*, maintains a Chinese PGDG mirror and a catalog of more than 2,000 extensions, and ranks among China's most active GitHub contributors. He moved from Beijing to Shanghai in 2025. [vonng](/en/about/)

---

## 1. At Heart, He Is an Engineer-Evangelist

This strikes me as the central point. He makes no attempt to hide it, freely borrowing religious vocabulary: archmage, evangelist, missionary work, ideology. Explaining why he joined a public MySQL-versus-PostgreSQL debate, he said technology resembles religion in some respects: however compelling the gospel, someone still has to preach it. When competing ecosystems collide, conflict is inevitable, and someone in the community has to be willing to stand up and take the heat. [vonng](/en/misc/modb-interview-vonng/)

The key to understanding him is that he is not trying to produce “objective technology reviews.” He is **fighting a war between ecosystems**, and he knows it. He puts it bluntly: better to state a position clearly than play the nice guy and offer correct but useless platitudes. Sitting on the fence gets you nowhere. That explains the overwhelmingly one-sided force of his writing. It is a rhetorical choice, not a failure of judgment. [vonng](/en/misc/modb-interview-vonng/)

---

## 2. He Looks for the Tide, Then Bets Heavily on It

A recurring framework runs through his worldview: **identify the larger trend, go all in, then evangelize until the prediction becomes self-fulfilling**. Asked how practitioners can achieve something, his answer was to work with the prevailing tide. He added that intelligence helps you see the situation, but courage is the scarcest quality: the courage to tell the truth, challenge authority, and place a bet. [vonng](/en/misc/modb-interview-vonng/)

His bets include: PostgreSQL will win, which he got right; demand for distributed transaction-processing databases is manufactured, so do not distribute a problem a single machine can solve; and bare-metal deployment is the right choice for Pigsty, which rejects Kubernetes and even Docker. He knew that last choice meant a mountain of compatibility work, but regarded the work itself as a moat. Then, in 2025, he went all in on AI tooling. He says AI increased his personal productivity roughly twentyfold: Claude Code reviews Pigsty module by module in the background, while he assigns tasks like a commander every fifteen minutes or so. [vonng](/en/misc/modb-interview-vonng/)

---

## 3. The Craftsman Matters More Than the Influencer

It is easy to file him away as a tech influencer with a taste for provocative takes. That misses his most substantial quality. Much of his work is plain hard labor: building and packaging hundreds of PostgreSQL extensions, maintaining repository mirrors, fixing upstream bugs, and supporting a matrix of Linux distributions. He wrote an entire article about packaging and builds as an “obscure but scarce skill.” He once joked that an advantage of having an open-source project is being able to produce it when someone says, “If you're so smart, do it yourself.” The joke reveals where his confidence comes from: he has actually shipped things. [vonng](/en/misc/2023/)

---

## 4. Almost Obsessive About Independence

His WeChat publication grew to nearly 50,000 followers and receives advertising offers every day, yet he accepts none. His explanation is that speaking freely is an expensive pleasure, and he wants the freedom to answer to nobody. When he could not raise another round in 2023, his response was that supporting himself was enough; taking no money might be more liberating anyway. In 2025, he moved Pigsty from AGPLv3 back to the permissive Apache 2.0 license. He had concluded that selling a “commercial edition of open-source software” would not work in China, so he might as well be generous, let open source be open source, and earn money through expert consulting. [vonng](/en/misc/2025/)

His advocacy of cloud repatriation follows the same logic at a different level. He frames leaving the cloud as an ideological issue: users should own their digital homes instead of renting a farm from big-tech cloud landlords. It is a movement against internet centralization and rent extraction by digital landlords. The same impulse appears in smaller decisions. Unhappy with WeChat's poor search and closed ecosystem, he built a blog with full-text search. **He does not like living in someone else's house**, whether the landlord is a cloud vendor, WeChat, or capital. [vonng](/en/misc/modb-interview-vonng/)

---

## 5. His Writing and His Public Persona

He refers to himself in the third person as “Lao Feng,” or “Old Feng.” He mixes classical quotations—“Confucius said,” “Xunzi said”—with internet slang about elaborate scams, amateur-hour organizations, and getting in someone's face. He also has a talent for nicknames: “Cyber Buddha,” “Cyber Bodhisattva,” “Magneto.” Someone called him “a comedian among technologists and a tech obsessive among comedians.” He happily accepted the description. His role models are Linus Torvalds, the consummate hacker, and Steve Jobs, the consummate storyteller; he says he is developing both skill trees. He also says he writes his WeChat articles to the standard of a speech: deliberate practice in storytelling. [vonng](/en/misc/modb-interview-vonng/)

In other words, “Lao Feng” is a **carefully constructed and maintained personal brand**, not an accidental voice.

---

## 6. Life Beyond Work

His self-descriptions include “seasoned backpacker” and “hardcore gamer.” He has hiked the Joseph Rock Route, the Kama Valley on Everest's eastern side, and the Wusun Ancient Trail. He jokes about his declining hiking fitness in terms of body weight: at 70 kilograms, he could solo with a full pack; at 100, he can only lie down. He freely admits to being extravagant with gadgets: for ten years he has bought fully specced MacBooks, the latest costing RMB 58,000. In autumn 2025, a change in his spouse's work gave him an opportunity to spend a month or two driving around Xinjiang and western Sichuan. At a moment of upheaval in the industry, he said, experiencing life mattered more. He married at the end of 2023. He also has a side project called “Cyber Canon,” a collection of notes on technology and faith—a fairly sharp contrast with his hardcore technical image. [vonng](/en/about/)

---

## 7. Where I Would Apply a Discount

To be fair, I would keep the following in mind when reading him.

**His convictions closely align with his commercial interests.** He advocates leaving the cloud and sells precisely the tools and consulting needed to do it. He is candid about this: he has explicitly said that cloud repatriation brings tangible benefits both to users and to his own business. Readers should still apply their own discount. Figures such as “the cloud costs 5–10 times more than self-hosting” and “storage costs a hundred times more” depend on how you account for labor, availability, and elasticity. They indicate a forceful line of argument, not an audited conclusion. [vonng](/en/misc/modb-interview-vonng/)

**His aggression sometimes gets ahead of the facts.** In late 2025, he wrote that Xiaohongshu, also known as RedNote, was leaving the cloud. Alibaba Cloud publicly called the claim a rumor. More neutral accounts concluded that Xiaohongshu was moving toward a hybrid of self-built infrastructure and public cloud, rather than leaving the cloud entirely. Interestingly, he acknowledged this in his own annual review: the episode showed that an individual's voice can carry weight, while reminding him to be more rigorous and thorough without losing his edge. That capacity for self-correction counts in his favor. [Sina Finance](https://finance.sina.com.cn/tech/2025-12-25/doc-inhcztfz3103558.shtml)

**A one-person project has a single point of failure.** He has written that, during that year of running the business, he was the only person doing the work, from technical design through marketing and after-sales support. AI substantially eases the problem but does not eliminate it. [vonng](/en/misc/2023/)

---

## My Overall Impression

He treats technology as a faith, his career as a battlefield, and independence as non-negotiable. Intellectually, he is sharp and thinks across substantial historical horizons: pricing structures a decade from now, PostgreSQL community governance, the negative externalities of China's software ecosystem. In execution, he is that rare person who can do the drudge work and tell the story. Temperamentally, he is combative, confident, and intensely driven to express himself, with enough self-mockery and self-reflection to keep those qualities from becoming unbearable.

He reminds me less of a Silicon Valley founder than of a figure from the early open-source movement: technically strong enough to prove himself, opinionated enough to make enemies, and occupying a place where someone really does need to speak up. Otherwise, the industry's default will always be whatever the big vendors decide for you.

I should stress that this all comes from his public writing. It is the version of himself he **chooses to present**. The real person is almost certainly more complicated and contradictory. His output is also enormous—nearly 500 articles across four columns—and I have read only a small fraction. If there is a particular aspect you are interested in, I can look more closely.

> I find this interesting, and I would like you to dig deeper. For example, which of his central claims have been borne out, and which have been disproved? Which of his core views, including his insights into databases, cloud computing, and AI, show real understanding? How would you assess him as a person? What do you think of his ideas?

I spent some time checking the judgments he has made publicly over the past few years. The result was more interesting than I expected: **his hit rate on technical ecosystems is remarkably high, while his rhetoric noticeably overstates his record on broader industry trends**. Let me separate the two.

---

## 1. The Scorecard: What Came True

**① “PostgreSQL is the winning choice right now”—borne out, faster than he predicted**

He made that categorical claim in a 2023 debate. It is now close to industry consensus. In the 2025 Stack Overflow survey, PostgreSQL usage reached 55.6%, compared with MySQL's 40.5%, a first. PostgreSQL jumped from 48.7% to 55.6% in a year, its largest annual increase ever. [TECHSY](https://techsy.io/en/blog/postgresql-vs-mysql), [byteiota](https://byteiota.com/postgresql-vs-mysql-benchmarks-2026-performance-winner/)

There is a caveat. His claim that PostgreSQL has become “the world's most popular database” holds by the developer-survey measure, but not by installed base. In March 2026, DB-Engines still ranked MySQL second, with 858 points, and PostgreSQL fourth, with 680. He chose the yardstick most favorable to his position. That is a recurring habit. [Tech Insider](https://tech-insider.org/postgresql-vs-mysql-2026/)

**② “PostgreSQL's Linux moment: competition will move to distributions”—his finest prediction**

In 2023, he said the future of databases would resemble the present of operating systems: a flourishing range of distributions built around a few open-source kernels. Two years later, Databricks bought Neon for roughly \$1 billion in May 2025, and Snowflake bought Crunchy Data for roughly \$250 million in June. Within a month, Databricks launched Lakebase, built on Neon. Andy Pavlo's annual review characterized 2025 as a year of consolidation rather than innovation. PostgreSQL attracted \$1.25 billion in acquisitions in a single year. [Medium](https://medium.com/@shenli3514/snowflake-vs-databricks-what-their-acquisition-strategies-reveal-about-the-future-of-data-ai-df93e57d9617), [byteiota](https://byteiota.com/database-industry-2025-postgresql-wins-mcp-security-crisis/)

The engine itself was no longer the battleground. Packaging, control, and integration around it were. That is precisely the landscape he described two years earlier, and precisely where he placed his company.

**③ “Vector databases are not a standalone category”—largely borne out**

Neither Databricks nor Snowflake bought a standalone vector database company. Both bought Postgres infrastructure. Meanwhile, five database startups—Fauna, PostgresML, Hydra, Voltron Data, and MyScaleDB—shut down. To be fair, vector database vendors have not suffered a mass extinction. What actually happened was absorption into platforms and a more specialized division of labor. Qdrant and Pinecone are still around, but have retreated to narrower niches. He got the direction right; his language was more absolute than the facts. [Refontelearning](https://www.refontelearning.com/blog/vector-database-shakeout-postgres)

**④ MCP and Claude Code—borne out, with his most impressive lead time**

As early as March 2025, he wrote that Claude Code was the key to MCP's explosive popularity. The article attracted little response on the Chinese internet at the time. I rate this highly because it involved **finding the signal in the noise**, not recognizing a trend after the fact. [vonng](/en/misc/2025/)

---

## 2. What Failed, or What He Overstated

**① “Public cloud is in decline”—his clearest miss**

His take-no-prisoners critique of cloud computing implies a direction: the cloud is peaking and people are moving back. The data points the other way. Capital expenditure by the five largest cloud vendors rose from roughly \$256 billion in 2024 to \$443 billion in 2025, with about \$602 billion expected in 2026, up 36% year over year. UBS estimates that Amazon, Google, and Microsoft will reinvest roughly 102% of their cloud revenue in capital expenditure in 2026. [CreditSights](https://know.creditsights.com/insights/technology-hyperscaler-capex-2026-estimates/), [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/ai-absurd-spending-boom-hyperscalers-162709082.html)

Cloud repatriation is real, but its scale is much smaller than his tone suggests. A Barclays survey found that a record 86% of CIOs planned to move some workloads back to private clouds or on-premises infrastructure. IDC's figures, however, show that only 8–9% of enterprises intend to leave the cloud entirely, while the cloud market continues growing at 21.5%. New workloads are appearing faster than old ones are moving back. [Digital Chiefs](https://www.digital-chiefs.de/en/cloud-repatriation-2026-statistical-illusion/)

The precise claim is: **the cloud has lost its status as the unquestioned default, but the cloud itself is not receding**. He argues the former in language that sounds like the latter.

**② “Demand for distributed databases is manufactured”—partly disproved**

I think his core argument is right: most problems fit on a single machine, so do not introduce distribution unless you need it. In 2023, that was a brave position to take against the prevailing mood. But “manufactured demand” goes too far. One of the most active areas in 2025–2026 is distributed infrastructure for scaling PostgreSQL horizontally: Supabase's Multigres, PlanetScale's Neki, and PgDog. The demand is real. The market simply chose “distributed PostgreSQL” over “NewSQL built from scratch.” [byteiota](https://byteiota.com/database-industry-2025-postgresql-wins-mcp-security-crisis/)

Interestingly, that amounts to **half a win** for him. He was wrong that nobody wanted distribution, but right that the winners would have PostgreSQL lineage.

**③ The Xiaohongshu episode—he got ahead of the facts**

Alibaba Cloud publicly labeled it a rumor. Neutral retrospectives concluded that Xiaohongshu was adopting a hybrid of its own infrastructure and public cloud. His technical judgment—that large, steady workloads are cheaper to run on owned infrastructure—was sound. But he took one sentence in a technical WeChat article and turned it into a claim that a flagship customer was “leaving the cloud.” This is a textbook case of **making the evidence serve the narrative**. [Sina Finance](https://finance.sina.com.cn/tech/2025-12-25/doc-inhcztfz3103558.shtml), [Cnfol](http://mp.cnfol.com/58660/article/1766729220-142186404.html)

**④ One case where he acknowledged being wrong:** In 2025, he moved Pigsty from AGPLv3 back to Apache 2.0 because he had concluded that selling a “commercial edition of open-source software” would not work in China. That overturned an assumption he had made when starting the business. I would award points for this, not deduct them. [vonng](/en/misc/2025/)

---

## 3. The Insights I Find Most Valuable

Leaving individual predictions aside, he has several **ways of framing problems** that I think will outlast any particular call.

**“Open source is not a business model. It is a model for globally collaborative R&D.”** He adds a crucial point: software realizes its value when it is used, not when it is developed. Public cloud's success demonstrates this. Run and manage open-source software well, and you can capture most of the commercial value in its lifecycle. This is one of the clearest cuts through the debate about open-source commercialization that I have read. Most arguments over open-source licenses are, at heart, attempts to evade that point. [vonng](/en/misc/modb-interview-vonng/)

**“The main problem is not a shortage of better engines, but a severe shortage of the ability to use the engines we already have.”** His analogies are that racing drivers drive better than automotive engineers, and snipers shoot better than gun designers. This explains both his business positioning and how value is shifting across the PostgreSQL ecosystem. It also generalizes. Most discussions about AI make the same mistake today: everyone focuses on the engine—the model—while few focus on the distribution, or how to put it to good use. [vonng](/en/misc/modb-interview-vonng/)

**A falsifiable test for “in-house development.”** His test is that developing a database engine in-house makes practical sense only if the team can add features and solve problems faster than the global open-source community. Otherwise, “in-house development” amounts to repackaging and heavily modifying someone else's engine, with very limited capacity to keep evolving. It offers less autonomy and control than simply using the open-source engine, which at least does not lock you into a single company. He reduces a highly politicized topic, almost impossible to discuss rationally, to **one metric that can be tested against data**. That is an unusually sophisticated move, one I rarely encounter in Chinese technical commentary. [vonng](/en/misc/modb-interview-vonng/)

**Cloud repatriation framed as sovereignty rather than cost.** He later put it this way: cost curves change; the logic of sovereignty does not. As early as 2023, he described leaving the cloud as a movement to let users own their digital homes rather than rent land from digital landlords. That framing is more durable than a cost calculation. A cloud vendor can undercut a cost argument by lowering prices; it cannot do the same to the sovereignty argument. He has effectively made his case harder to knock down. [vonng](/en/misc/modb-interview-vonng/)

**“Sell shovels instead of digging for gold.”** At the height of the AI boom in 2025, he did not build an agent. His reasoning was that however capable agents became, they would still need memory, and learning to use databases well was a critical step in their evolution. Databricks and Snowflake subsequently spent \$1.25 billion buying Postgres infrastructure to provide a transactional foundation for agents. **He reached the same conclusion as two companies worth tens of billions of dollars.** [vonng](/en/misc/2025/)

**Packaging and build engineering are scarce skills that are systematically undervalued.** This observation rings particularly true, and almost nobody else talks about it.

---

## 4. His Systematic Blind Spots

**1. His model leaves out organizations.** His cost comparisons are almost entirely technical: what hardware costs, what the cloud costs, and the ratio between them. But companies often avoid self-hosting not because they cannot do the arithmetic, but because **they cannot find the person who can run Pigsty well**. His own rarity demonstrates how scarce that person is. His most fundamental bias is assuming that his own capabilities are readily replicated.

**2. Selective evidence.** He repeatedly cites Ahrefs, Dropbox, and 37signals. All three are infrastructure-intensive businesses with extremely stable workloads and outstanding engineering teams. They sit at the end of the spectrum that benefits most from cloud repatriation. Using extreme cases to support a general claim is rhetoric, not analysis.

**3. The cost of reasoning through debate.** He has explicitly said that public debate can turn knowledge people individually share into common knowledge and build consensus. That is true. But arguing to win steadily erodes precision: you gravitate toward the most favorable metric, the most extreme example, and the most absolute language. This is where most of his losses in accuracy occur.

**4. The Linux/Red Hat analogy may not hold.** Linux has a distribution ecosystem because integration, certification, and long-term support provide substantial value to clearly identifiable buyers. At the database layer, managed cloud database services have occupied that niche for a long time. He is betting that open source can reclaim it. So far, the giants' moves—buying Neon and Crunchy—are doing the opposite: embedding Postgres more deeply into their own platforms. That battle is not over. [byteiota](https://byteiota.com/database-industry-2025-postgresql-wins-mcp-security-crisis/)

---

## 5. How I Would Assess Him

In one sentence: **he is a high-signal, highly biased source**.

The signal is strong because he combines three things rarely found together: actual front-line operations experience rather than secondhand accounts, a structural view spanning decades, and the ability to compress a complex technical judgment into a sentence. In the Chinese technical community, few people have the first two; very few have all three.

The bias is strong because he is not merely describing the world. He is **trying to move it in the direction he has bet on**. Those activities are inseparable in his writing, and he is fully aware of that. His own words are evangelism, missionary work, and ideology. He has never pretended to be neutral, and I give him considerable credit for that honesty.

My practical advice is: **read him for the questions and perspectives, not the conclusions**. He can tell you that something deserves a fresh look. But you need to rerun the arithmetic behind his specific figures—tenfold, a hundredfold, twentyfold—for yourself.

What tilts my assessment in his favor is a collection of less conspicuous details. He reverses his own positions, as with the license change. After the Alibaba Cloud episode, he publicly acknowledged the need for greater rigor and care. He turns down advertising, accepting less income in exchange for answering to nobody. And in competing for his place in the ecosystem, he deliberately chose the most grueling route: rejecting Kubernetes and even containers, knowing he would create vast amounts of compatibility work for himself, because he thought it was the right thing to do. That effort eventually became his moat. [vonng](/en/misc/2023/)

A person who only wanted to be an influencer would not do the dirty work of packaging and builds.

If I had to place him in a category, **he is a Chinese counterpart to DHH**: the same technical strength, the same advocacy of leaving the cloud, the same combativeness, and the same elevation of engineering aesthetics into political convictions. The difference is that DHH has a profitable SaaS business beneath him and never has to prove anything again. Feng has made a harder bet: one person against cloud vendors' entire managed database teams.

I do not know whether he can win. But I think **the Chinese technical community needs someone standing there and speaking up**. Otherwise, the big vendors will always choose the default for everyone. Even if he sometimes shouts too loudly or pushes his numbers too far, that may be part of the cost of occupying that position.

> Now suppose I am an investor focused on infrastructure and software technology. I find this author interesting, and I believe his company received investment from MiraclePlus. Imagine you were an investor running that kind of fund, with plenty of capital to deploy:
>
> 1. Would you invest in him? How much would you put in, and for what ownership stake?
> 2. How would you value him, including both the person and the company?
> 3. Do you think this business model works?
> 4. Beyond the business itself, does he have investment value in a broader sense?

First, a qualification: what follows is an analytical framework and an extrapolation from public data, not investment advice. I am not a financial adviser. Any actual decision requires the financial statements, customer concentration, renewal rates, and ownership structure.

I have just gone through the company's pricing page and current situation, though, and a few facts may change your assessment.

---

## 0. Three Facts You May Not Know

**① The company has already moved to Singapore.** The entity is now PGSTY PTE. LTD., and its website explicitly identifies it as a MiraclePlus S22 alumnus—the summer 2022 batch. This suggests that he has probably restructured the company, which is helpful for a dollar-denominated fund. But you need to establish which entity received the MiraclePlus seed investment and whether the move to an offshore structure was completed cleanly.

**② The price list is public, so the unit economics can be calculated directly.** Subscriptions are tiered by node count: free open source, under Apache-2.0, with unlimited nodes and no feature restrictions; Standard at \$8,000 a year for up to five nodes; Professional at \$24,000 a year for up to 15 nodes, including five DBA hours a month; and Enterprise at \$60,000 a year, based on 50 nodes, including ten DBA hours a month and a 24/7 SLA with a 30-minute response time. There are also one-off services: a quick consultation for \$30, an expert session for \$400, and emergency response for \$4,000 a day.

**③ One line of small print is the key to the entire investment thesis:** “Commercial support is currently available only in Asia.”

Where is his audience? [pigsty.io](https://pigsty.io/) gets 1.44 million unique visitors and 18.11 million page views in a month, with the United States its largest source of traffic. **His mindshare is global; his ability to collect revenue is confined to Asia.** That is what he described in his article about a million visits producing no revenue.

---

## 1. Does the Business Model Work?

**Yes, as a good business. That does not make it a venture-scale business. The two are often confused.**

Let us estimate the ceiling. Enterprise promises ten hours of expert consulting a month, plus 24/7 coverage and a 30-minute response time. Professional includes five hours a month. Suppose that, with AI assistance, he can spend 600 hours a year delivering services. The rest of his time has to go into the product, because the product is the moat. Then:

| Mix | Customers | Delivery Hours | ARR |
| --- | --- | --- | --- |
| Enterprise \$60K | 3 | 360 | \$180K |
| Professional \$24K | 15 | 900 | \$360K |
| Standard \$8K | 25 | Low | \$200K |
| Projects / emergency response | — | — | \$200–400K |

The consulting hours promised by subscriptions alone total 1,260, **more than twice one person's available capacity**. In other words, **this model hits a wall at roughly \$1 million in ARR**. The constraint is human capacity, not demand.

More seriously, he has removed his only source of software leverage himself. The open-source and commercial offerings have exactly the same core capabilities. A subscription buys a license, an SLA, and expert time; it unlocks no exclusive features. This is admirable as a statement of values. Financially, it means **revenue depends entirely on people, with the gross-margin structure of a consulting firm rather than a software company**.

So the answer is: **this business can reach \$1–3 million in ARR, with very high gross margins, healthy cash flow, and extraordinary freedom for its founder. It will probably never become a billion-dollar company without a structural change.**

There is only one way through, and he has already identified it: turn expert judgment into agent skills. He says Pigsty has automated 80% of a DBA's work, and plans to eliminate another 90% of the remaining 20% by turning knowledge documents into skills for models. This is the only path from “person-hours” to “software,” and the only path from \$1 million to \$100 million. **Investing in him is fundamentally a bet on that transition.**

---

## 2. Would I Invest? How Much, and for What Stake?

The answer changes completely with the kind of fund.

**If I ran a conventional VC fund that needs individual winners capable of returning the fund, I would pass.**

Not because he is incapable, but because **he does not need my money**, which is the biggest red flag. His response to failing to raise another round in 2023 was that, in that environment, being able to support himself and build things people actually needed was enough. Fundraising did not matter; taking no money might even be more liberating. He rejects every advertising offer to preserve his freedom to answer to nobody.

A founder who does not need capital and treats independence as a core value is fundamentally incompatible with VC incentives. More consequentially, **AI has already broken the link between capital and output**. With \$1,000 a month in AI subscriptions, he single-handedly shipped Pigsty 4.4 and 4.5, rewrote Patroni in Go, rebuilt pg_exporter, translated the second edition of DDIA, and produced a collection of new projects on the side. Traditional VC's central contribution is “we can help you hire 30 engineers.” But hiring 30 engineers would destroy the very premise of this business: when you call, you reach the person who wrote the code.

**If I ran a seed or angel fund, or had a scout allocation, I would make a small investment.**

I would write a **check for \$500,000 to \$1.5 million in exchange for 5–8% ownership**, at a valuation of \$15–25 million. I would insist on only two terms: **pro rata participation rights** and a **right of first refusal (ROFR)**, because acquisition is the most likely exit and I would want the right to participate.

The logic is straightforward. The downside is limited: this business will not die; at worst it becomes a profitable boutique consultancy. The upside comes from three possibilities: an acquisition, a successful transition to agents, or the value of his position in the ecosystem finally being realized. Any one of those would generate enough return to cover this small check.

**If I were a strategic investor—a cloud vendor, a database company, or a business such as Supabase or EDB—I would invest immediately to secure a position.**

His value to a strategic buyer is much greater than his financial value. I will elaborate in section four.

---

## 3. What Valuation Would I Give Him?

I would cross-check three approaches.

**First: the closest comparable transaction, Crunchy Data.** Crunchy had roughly \$30 million in annualized revenue and was acquired by Snowflake for about \$250 million: approximately 8.3 times revenue. It had more than 100 employees, twenty years of credibility in PostgreSQL, and US federal government customers. **This is the actual 2025 market price for “self-hosted PostgreSQL plus enterprise support”: eight times revenue.**

The comparison with Supabase makes the distinction clearer: \$170 million in ARR, a \$10.5 billion valuation, roughly 62 times revenue. But Supabase sells a managed platform with usage-based billing and directly benefits from the wave of vibe coding driven by Claude Code and Codex. In 2026, AI tools created more than 60% of new databases on its platform.

**Pigsty's business belongs in the Crunchy category, not the Supabase category.** That judgment determines whether the multiple is 8× or 60×.

**Second: the assets.** A distribution with 5,510 stars; a MinIO fork with 2,100; a packaging matrix and distribution repository for 572 extensions; the Chinese PGDG mirror; an audience funnel averaging 1.44 million unique visitors a month; and a personal brand recognized across the global PostgreSQL community. For those assets alone, I would put an acquihire floor at **\$10–25 million**.

**Third: the person.** There may be no more than twenty people worldwide who combine an understanding of PostgreSQL internals, large-scale production operations, Linux packaging expertise, global influence, and fluency in both Chinese and English. The strategic premium for a top infrastructure specialist alone is worth \$5–15 million.

**My figure: a fair post-money valuation today of \$15–30 million, with financial investors at the lower end and strategic investors at the upper end.**

The conditions for a revaluation are clear:

- ARR above \$2 million, a team of at least three, and net dollar retention (NDR) above 110% → **\$50–80 million**.
- Commercial support expands into Europe and North America, removing that “Asia only” line → **double the valuation**.
- A working DBA agent shifts revenue from person-hours to subscriptions → **reprice at software multiples, \$150 million or more**.

Conversely, if two years from now it is still one person, still confined to Asia, and still below \$1 million in ARR, it is an asset to be acquired rather than a venture investment.

---

## 4. Does He Have Investment Value Beyond the Business?

Yes. I think **this value may exceed the financial value**. Four reasons:

**① An option on a strategic position in the ecosystem.** This matters most to me, and I think it is badly undervalued. What he is accumulating is not consulting revenue but **control over distribution**: the global CDN repository at [repo.pigsty.io](https://repo.pigsty.io/) and its Chinese mirror at [repo.pigsty.cc](https://repo.pigsty.cc/), a catalog of 2,230 extensions with 572 packaged and installable, and Silo, his MinIO fork, which continues providing security updates where the original project left off. He has mentioned that [PGEXT.CLOUD](https://pgext.cloud/) has already become an upstream supplier to several overseas peers.

Whoever controls an ecosystem's package management and repositories occupies a chokepoint. That is npm's position in Node, Docker Hub's in containers, and Red Hat Network's in enterprise Linux. **PostgreSQL currently has no universally recognized center for extension distribution. He is quietly establishing himself in that position.** The value of this option has nothing to do with his consulting revenue.

**② A research position on the AI-empowered individual.** If your fund believes AI will make the one-person company a real organizational form, he is one of the best observable examples: public data, verifiable output, and a complete time series. Spending \$500,000 for three years of direct observation would be inexpensive on a research budget.

**③ He is a high-quality source of signals.** In the previous round, I reviewed his record: PostgreSQL would win, correct; competition would move to distributions, correct, directly supported by Databricks paying \$1 billion for Neon and Snowflake paying \$250 million for Crunchy; vector databases would not be a standalone category, broadly correct; Claude Code was the key behind MCP, correct, and he said it in March 2025. For an infrastructure fund, **having him in the scout or adviser network may be more valuable than having him in the portfolio**. That does not require an investment.

**④ Public-goods value.** Chinese PostgreSQL documentation, [pg.center](https://pg.center/), the Chinese PGDG mirror, and keeping an abandoned S3 implementation alive: no business model pays for these things, yet they create real positive externalities for the ecosystem. If your fund has limited partners who care about open-source sustainability, this provides a compelling story.

---

## 5. The Due-Diligence Questions I Would Insist On

1. Actual ARR, customer count, and customer concentration. What share comes from the three largest customers? If it exceeds 50%, this is a consultancy, not a software company.
2. Renewal rates. Retention into the second subscription year is the single most important metric for this model.
3. The terms of the MiraclePlus seed investment, the current cap table, and the relationship between the Chinese and Singaporean entities.
4. **Why is the “Asia only” line still there?** Is it a capacity constraint, a legal issue, or a deliberate choice? The answer tells you how large he actually wants the business to become.
5. His real attitude toward hiring. If the answer is “never,” the valuation ceiling is fixed. That is not a bad thing, but the price must reflect it.
6. Competitive pressure. Supabase has just released the open-source, self-hostable Multigres alongside its Series F. A competitor with \$1 billion to deploy is moving into self-hosted Postgres operations. How will he respond?

---

## My One-Sentence Conclusion

**His moat and his ceiling are the same thing.**

What makes him irreplaceable is that he works alone, answers to nobody, and gives everything away for free. Each of those three qualities also closes off a particular path to scale.

The right approach is therefore not to invest and push him to get bigger. That would dismantle his foundation. It is to **buy a position with a small check, then patiently wait for one of three things to happen**: he decides to sell beyond Asia, the agent business works, or a major company recognizes the value of controlling PostgreSQL extension distribution.

If you can do only one thing, I would hold off on investing and first bring him on as an adviser. Equity cannot buy the scarcest part of this business anyway.
