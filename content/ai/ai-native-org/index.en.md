---
title: "Why Established Companies May Never Become AI-Native"
date: 2026-09-24
authors: [vonng]
summary: >
  What is happening is not transformation, but new species replacing old ones. Incentives and structure keep established companies from capturing AI's gains. AI-native companies will grow from scratch, with new forms of organization.
tags: [AI, Business, Commentary]
---

> What is happening is not transformation, but new species replacing old ones.

A few days ago, I joined a [roundtable](https://mp.weixin.qq.com/s/JMjX9A_5_L5fn3g5JGpC-A). The moderator asked how a company should calculate the ROI of deploying agents. Instead of answering directly, I offered a provocation: **the whole idea of enterprise AI transformation may rest on a false premise.**

He found the idea interesting and asked me on the spot to turn it into an essay. So here it is. One of his observations was especially good: learning to use a smartphone later in life does not make you a mobile native. Similarly, AI's real gains have trouble getting through the doors of established companies. Two walls stand in the way: incentives and structure.

Established companies will not disappear, but they cannot become AI-native companies. AI-native companies will emerge from scratch, as a new species.

## One Person, a Hundredfold Gain

I run a one-person company, or OPC. I have been doing it for four years, with consistent profits and a [valuation](https://mp.weixin.qq.com/s/Kia6uqomvmwW6eJ7xpvqaw) of RMB 120 million. By a conservative estimate, AI agents have made me more than 100 times as productive. I maintain Pigsty, a [database distribution](https://mp.weixin.qq.com/s/c6RtyrXpIfmutGfO8sVr-w), handle [more than 100 million](https://mp.weixin.qq.com/s/ILWUC5Sa4oCGZTfNfH7AQw) page views a month, and have also taken on [MinIO object storage](https://mp.weixin.qq.com/s/zq-rNfKNZHB_4Krb1hE9Mw). I am advancing on several fronts at once; I have described the actual output in [earlier writing](https://mp.weixin.qq.com/s/pcuxHzZBUSrGNZi___d4OQ).

Behind all this are 15 top-tier [subscriptions](https://mp.weixin.qq.com/s/Tfgvzs9sxyXmpsz4gNYDaw) at $200 each, mainly Codex and Claude. The monthly bill is under RMB 20,000—enough to hire just two or three interns. Yet the work these subscriptions produce is equivalent to having 10 experts working for me at 10 times their normal speed. AI agents have increased my productivity more than a hundredfold.

That figure is not plucked out of thin air. My commit count alone has grown more than tenfold over the past year. My [annual count](https://mp.weixin.qq.com/s/rx_J95zatr_7Z-DFk5YUiw) ranks in China's top 10 and the world's top 100. And that is only a lower bound: the amount of work in a single commit is already on a completely different scale. In the past few days, I single-handedly finished translating the [documentation](https://mp.weixin.qq.com/s/eTdhnt-sqNC4u7N2dOv-5A) for every PostgreSQL version from 10 through 20 into Chinese, and submitted [complete Chinese message translations](https://mp.weixin.qq.com/s/fJYjCSAfNqgFW1WJlqb46g) for versions 14 through 19 upstream. Any one of those jobs would once have taken a team months. Meanwhile, I have several times as much free time as before.

Yet the same AI seems to lose its magic inside an organization. From what I have seen, a team of a dozen or so can expect, at best, a severalfold productivity gain. At large companies, the public figures are much less impressive: even the best examples show gains of only 20–30%.

Take the industry leaders. [Google CEO Sundar Pichai said in mid-2025](https://www.aol.com/sundar-pichai-says-ai-making-141602216.html) that AI had increased the company's engineering velocity by about 10%, measured by the working hours AI tools saved engineers each week. On its [earnings call](https://www.fool.com/earnings/call-transcripts/2026/01/28/meta-meta-q4-2025-earnings-call-transcript/) early this year, Meta said output per engineer had risen 30% since the start of 2025. Even its most effective heavy users of AI coding tools had achieved only an 80% year-over-year gain.

A hundredfold gain for an individual, a 30% gain for a company. Where did those two orders of magnitude go?

## The First Wall: Incentives

As an OPC, I keep every bit of the benefit when AI makes me 100 times faster. I can use that speed to conquer new territory, or settle for a few dozen times my old output and spend the extra free time enjoying life.

Inside a company? If AI makes you 10 times faster, do you get 10 times the income or 10 times the free time? Probably neither. The most likely reward for being capable is more work: your boss assigns you 10 times as much, then adds a manipulative pep talk: "Today's best performance is tomorrow's minimum requirement."

So a rational employee uses AI quietly. Deliver the usual amount of work with one-tenth of the effort, and turn the rest into downtime, a side business, or an earlier finish. I am not just guessing: a [global survey by KPMG and the University of Melbourne](https://kpmg.com/xx/en/media/press-releases/2025/04/trust-of-ai-remains-a-critical-challenge.html), covering more than 48,000 people in 47 countries, found that 57% of employees admitted hiding their use of AI and presenting its output as their own. Employees can take this a step further, policing one another and collectively shunning "scabs" and relentless overachievers who raise the bar for everyone else.

There are enlightened companies, of course. I used to work at Tantan, which had a Nordic-style workplace culture: employees were allowed to enjoy the free time their own efficiency gains created. That was crucial to making Pigsty possible. I could keep the benefits of automating my own work, which gave me a reason to build it and then release it as open source. But this is unlikely to happen at the vast majority of Chinese companies.

Those of us from China know this story all too well. Same fields, same people, same hoes: replace collective farming with household contracts, and grain output jumps. [Justin Yifu Lin estimated](https://www.jstor.org/stable/2117601) that roughly half the growth in agricultural output from 1978 to 1984 was attributable to this reform. Fengyang's slogan for household contracting needs no revision today: **Meet the state's quota, set aside the collective's share, and keep everything else for yourself.**

What did household contracting actually do? It broke the production team back down into individual households as the units of production.

Put plainly, the collective did not transform itself. It dismantled itself.

## The Second Wall: Structure

Even if you fix the incentives and everyone eagerly pulls together to become more productive, established companies face a second wall: coordination costs.

One conclusion Geoffrey West draws in [Scale](https://kortina.nyc/notes/scale-the-universal-laws-of-growth-innovation-sustainability-and-the-pace-of-life-in-organisms/) is that companies scale like organisms, not cities: sublinearly. Ten times as many people do not produce ten times the output. The bigger the organization, the more unwieldy it becomes. [The Mythical Man-Month](https://en.wikipedia.org/wiki/Brooks%27s_law) gives us a formula: n people have \(n(n-1)/2\) communication paths between them. The number of paths grows with the square of the headcount: double the people, quadruple the paths.

Of course, no company actually connects every pair of employees. The point of a hierarchy is to compress that network into a tree, cutting coordination complexity from \(O(n^2)\) to \(O(n \log n)\). You report to your manager, who reports to theirs. The price? Communication that could have happened in parallel becomes a serial chain of approvals. Morning alignment meetings, evening status reports, reviews, approvals, waiting, handoffs, reporting, and arguments over responsibility. The taller the tree, the longer the chain.

And serial work is exactly the problem captured by [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law). How much faster a system can run depends on how much of its work can be accelerated. Make that portion infinitely fast, and the rest still takes as long as before. The serial portion puts a hard ceiling on the whole system. Suppose development becomes 100 times faster, but you spend 90% of your time on all those other steps. Overall, you gain only a little over 10%—roughly what Google reported.

Someone will object: AI can write meeting notes, review comments, and weekly reports too. Yes, it can speed up information processing. But the real bottleneck in that serial chain is responsibility: who makes the call, who signs off, and who takes the blame when things go wrong. AI cannot do those things for you, and the organization will not let it.

The [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) puts it more bluntly: speeding up a step that is not the bottleneck changes nothing except the pile of inventory waiting ahead of the bottleneck. [Faros's engineering data](https://www.faros.ai/blog/ai-software-engineering) shows exactly this pattern. Teams that used AI heavily merged 98% more pull requests, but PR review times also rose 91%. Code is written fast, then piles up in review.

One of an OPC's core advantages is eliminating the overhead that cannot be sped up.

## Productive Forces and Relations of Production

The previous two sections make the same point: AI's gains cannot get through the doors of established companies.

The wall of incentives makes people unwilling to hand over their gains. The wall of scale means the organization cannot absorb those gains even if it gets them.

Productive forces determine the relations of production—the way work and its rewards are organized. So what are the advanced productive forces of the AI era?

Compute? Tokens? I think neither. Anyone can buy compute and tokens, and they are not expensive. At $200 a subscription, buying 10 or 50 is pocket change compared with a company's payroll. A single deal is enough to pay for years of my subscriptions.

What is truly scarce is the ability to turn tokens into real output: revenue, code, evidence of reliability, traffic, trust, brand, reputation. Give different people the same stack of subscriptions, and one builds a company while another produces a pile of code no one reads. This ability resembles what economists call "entrepreneurship." You could also call it the "OPC spirit." This productive capacity resides in superpowered individuals, and AI can amplify it a hundredfold or more.

Now consider the relations of production. For most people today, the relationship with a company is employment: you get a monthly salary; the company keeps the surplus. You are a node in a hierarchy, and your output must pass through layer after layer of alignment and approval. The incentives deny you the benefit of the extra work; the structure limits the whole organization to a 10–20% speedup. Put someone with the OPC spirit inside Meta, and you get a cog that is 80% more productive.

When productive forces and the relations of production are this badly mismatched, resources flow to wherever they can earn their full return. For someone with the OPC spirit, the most rational choice is to leave and keep the full benefit of that acceleration. This is one reason OPCs are being so strongly encouraged today: they give these new productive forces room to grow.

Large companies see it too. [Zuckerberg said on an earnings call early this year](https://finance.yahoo.com/news/meta-boss-says-ai-letting-183328865.html) that a project that once needed a large team could now be done by one very talented person. He [wants as many of those people as possible to choose Meta](https://www.axios.com/2026/01/29/zuckerberg-ai-work-meta). But if AI really can make someone 100 times as productive, why would they choose Meta **instead of striking out on their own?**

Established companies face a dilemma. First, these people are hard to retain. Second, even if a company manages to keep them, they cannot deliver that kind of result inside it. Neither route leads to an AI-native company.

## Renewal Happens Across the Population

History offers an almost identical episode: electrification.

In 1990, economic historian Paul David published a famous essay, [The Dynamo and the Computer](https://www.aei.org/commentary/the-dynamo-the-computer-and-chatgpt-explaining-todays-productivity-paradox/). Electricity was commercialized in the 1880s, yet by the turn of the century, electric motors still supplied less than 5% of mechanical power in US factories. Early factories simply replaced a steam engine with one large electric motor, which drove the same [line shaft](https://en.wikipedia.org/wiki/Line_shaft) running through the building. The results were disappointing. From the mid-1890s until just before the 1920s, this "group drive" remained the dominant arrangement. Only in the 1920s did "unit drive"—one motor per machine—become widespread. US manufacturing productivity finally took off, forty years after electricity had become commercially available.

The change went beyond the power source to structure and incentives. Unit drive made lightweight, single-story factory buildings possible, with production lines arranged around the flow of materials instead of a line shaft. Workers could control their own machines, which also made them responsible for those machines. They needed better training and new employment contracts that gave them an incentive to take on that responsibility.

Why the forty-year delay? David's explanation was simple: the old factories still worked. Tearing them down and rebuilding did not pay.

Today's "AI subscription for every employee" is the electric motor replacing the steam engine in place, with the line shaft untouched. Today's line shaft is the corporate hierarchy and its approval chains. Today's factory is the organization itself.

That is why the closest things we have to AI-native companies today are frontier labs such as OpenAI and Anthropic. They, too, have thousands of employees and hold meetings. They may not yet have reached their final form, but they are the closest to the new species. Both grew from scratch. Neither is an established company transformed by handing AI tools to its employees.

Established companies can, of course, acquire the new thing. But that is acquisition, not transformation. Google bought [DeepMind](https://en.wikipedia.org/wiki/Google_DeepMind) in 2014 and let it operate as an independent unit for nearly a decade before integrating it into the parent organization. That is buying a new factory, not renovating the old one. My intuition is that future AI-native companies will follow a similar pattern: they will either emerge from scratch or grow out of superpowered OPCs.

This is normal in the corporate world. [West and his colleagues](https://royalsocietypublishing.org/doi/10.1098/rsif.2015.0120) studied more than 25,000 publicly traded North American companies from 1950 to 2009. The typical half-life was about ten years, and the mortality rate was independent of a company's age. The most common way to "die" was through a merger or acquisition. Individual companies come and go, while the economy as a whole keeps renewing itself. Renewal happens across the population, not within each individual.

That may sound cold. But the same story played out in the history of life long ago.

## The Skies of the Carboniferous

About 300 million years ago, from the late Carboniferous into the early Permian, insects reached their largest sizes. Giant dragonfly-like insects with wingspans of up to 70 centimeters flew through the skies. Atmospheric oxygen exceeded 30%, compared with just 21% today.

Insects have no lungs. They exchange gases almost entirely through a body-wide network of tubes called tracheae, with oxygen gradually diffusing inward. The traditional explanation is that the larger an insect gets, the harder it is to deliver oxygen deep inside its body. Only a high-oxygen world can support giant insects. One [study of beetles](https://pubmed.ncbi.nlm.nih.gov/17666530/) found that larger bodies devote a greater fraction of their volume to tracheae. Beyond a certain size, there is not even enough room in the legs for all the tubes they need. The [fossil record](https://news.ucsc.edu/2012/06/giant-insects/) fits: for roughly 200 million years, the maximum size of insects rose and fell with oxygen levels.

This looks a lot like today's superpowered individuals. **AI is the oxygen; the individual is the organism.** One person is like one insect: everything must be distributed by that person alone. The context is in their head, the judgment is in their head, and so is the final check on the work. When the "oxygen" was thin, one person could sustain only a small operation. AI sharply raises the concentration, changing the ceiling on how large one individual can grow. These superpowered individuals are the Meganeura of our time.

Companies are more like ant colonies. A single ant is weak; a colony relies on numbers and a strict division of labor. Workers, soldiers, and queens each have their place, passing messages along bit by bit through pheromones. The hierarchical company was the industrial age's answer to a constraint: individuals were too weak. **At its core, the division of labor is a survival strategy for weak individuals.** Once the ceiling on individual capacity rises dramatically, this division of labor designed for the weak loses much of its relative advantage.

The second half of the story is where things get interesting.

The age of giant insects did not last forever. Some research suggests that high oxygen in the Paleozoic enabled giant animals, and that falling oxygen levels later brought smaller bodies. What happened next is more intriguing. Around 150 million years ago, in the late Jurassic and early Cretaceous, oxygen levels were rising but insects were shrinking—just as birds appeared. Insects never returned to their Carboniferous size. The [researchers' explanation](https://pubmed.ncbi.nlm.nih.gov/22665762/) is that once birds were in the sky, agility mattered more than bulk. Evolution began to favor smaller bodies; the big ones became easy targets.

Birds took a different route from insects, with a different body plan. Vertebrates use the respiratory and circulatory systems in relay: lungs take in oxygen, then the heart and blood vessels actively deliver it to every cell. A bird has no less division of labor than an ant colony. The difference is that blood and nerves connect its organs in real time, rather than relying on the slow diffusion of pheromones. Birds can therefore be much larger than insects while remaining fast and agile.

Now bring the analogy back to the present.

The superpowered individual is the giant insect. It thrives under two conditions: plenty of oxygen, and no birds in the sky yet. Neither condition is permanent. Much of the "oxygen" these individuals breathe today comes from monthly subscriptions subsidized by model providers. Those subsidies may not last. And sooner or later, birds will appear.

The established company is the ant colony: it wins through numbers and division of labor, coordinating by passing messages through layers. As individuals grow stronger, this arrangement becomes increasingly cumbersome. The bird is a new species: an AI-native supercompany. Its skeleton—its core team—may well consist of today's superpowered individuals, but its body plan will be entirely different. An AI-native "circulatory system" will actively deliver context, judgment, and validation to everyone, instead of letting them diffuse through layer after layer of hierarchical meetings. The company can grow without slowing down. AI-native supercompanies, each held together by this new organizational structure and its relations of production—this "circulatory system"—will dominate the post-OPC era.

A bird is not a giant insect that grew bigger, much less an ant colony that transformed itself. No matter how many AI subscriptions an established company hands out, it cannot become one. An AI-native company can only emerge as a new species, growing from scratch.
