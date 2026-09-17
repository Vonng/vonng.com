---
title: "5 TB Deleted"
date: 2026-09-15
authors: [vonng]
summary: >
  A PolarDB for PostgreSQL instance running in Docker on a single production host lost 5 TB of data. There were no backups. Watching the recovery unfold, I have a few thoughts on the value of prevention—and making timely decisions when things go wrong.
tags: [PostgreSQL, Database, Backup, Incident]
images: [featured.webp]
---

A couple of days ago, a friend from the community got in touch about a spectacular database wipe. Their production database was PolarDB for PostgreSQL, running in Docker on a single host. Several terabytes of data were gone. It supported an important business system. There were no backups. The damage was severe.

Two or three years ago, I [recovered a PostgreSQL database](/en/pg/pg-filedump/) for a company in the MiraclePlus alumni network. That was a GitLab database on a machine using bcache. A power outage corrupted its files, and running `pg_resetwal` several times made things worse. I also helped look into companies offering PostgreSQL data recovery. None inspired much confidence. With my friend out of options, I rolled up my sleeves and took it on myself.

I used `pg_filedump` for page carving: picking through data pages on disk, identifying which table they might belong to, then extracting tuples one by one and piecing the data back together. It sounds cool. In practice, it is exhausting manual work that leaves your eyes aching. I got the data back, but that database was only 1 GB. This one is 5 TB.

Five thousand times larger. At 1 GB, page carving is hard labor. At 5 TB, it is moving a mountain by hand. And you cannot take your time: the client is breathing down your neck, the business is at a standstill, and you are working around the clock for days.

I've been going flat out on AI work lately and simply couldn't spare the time. I even asked a few friends at Alibaba Cloud whether the vendor offered a data recovery service for its PolarDB for PG engine. Nope. No such service there, either.

## Calling in Help

As it happened, I knew someone who specializes in PostgreSQL data recovery: Zhang Chen, the author of PDU. Very few people in China tackle this particularly hard problem, and he is among the best. I brought him in. Recovery is still in progress, with more than 70% of the data already recovered. Given the combination of no backups, several terabytes, and a niche database engine, that is an impressive result.

I won't go into how he did it. This is his livelihood, and those methods aren't mine to turn into a tutorial. All I can say is that watching it unfold was more gripping than a TV drama. As for the client's identity or business, I won't say a word.

The incident itself, though, left me with two observations worth discussing.

## Bian Que's Eldest Brother Doesn't Get Paid

There is a famous story in the ancient Chinese text *Heguanzi*.

King Wen of Wei asks the physician Bian Que which of the three brothers is the best doctor. “My eldest brother is the best, my second brother comes next, and I am the worst,” Bian Que replies. The king is puzzled. “Then why is yours the only name everyone knows?”

Bian Que explains: his eldest brother recognizes illness before it takes shape and eliminates it, so his reputation never travels beyond the family. His second brother treats illness at its first, slightest sign, so his reputation never travels beyond the neighborhood. Bian Que himself uses needles, powerful medicines, and surgery, intervening only when the patient is nearly dead. That is why rulers across the land know his name.

The database business works exactly the same way.

I've [seen several database wipes over the years](/db/database-really-exploded/), and the script is remarkably consistent: launch a single PostgreSQL instance in Docker, get it working, put it into production. It runs beautifully. Years go by without a problem. It reminds me of a line from the Chinese band Omnipotent Youth Society's “Kill the One from Shijiazhuang”: “Thirty years of living like this, until the building collapses.”

Three incident-free years do not validate the architecture. They mean you got lucky for three years. For a production business system, even if you don't set up a standby for high availability, periodically taking a `dump` and putting it on another machine is the bare minimum of professional responsibility. The cost is a `cron` job and a few dozen lines of script. When disaster strikes, that may be the only thin barrier between you and the abyss.

And honestly, if you're already running a niche engine like PolarDB for PostgreSQL, you're clearly willing to tinker. Why not try Pigsty while you're at it? [Pigsty can manage PolarDB for PG](/db/domestic-db-any-good/). Alibaba Cloud once asked me to add support, saying it would bring some business my way. Not a single deal materialized. I added the support anyway. The code is right there, free.

Pigsty's high availability, monitoring, and point-in-time recovery (PITR) support for upstream PostgreSQL also works with PolarDB for PG, at no charge. Deploy PolarDB with Pigsty, and you have an enterprise-grade database service with high availability and PITR out of the box. Personally, I think the vast majority of people should just use upstream PostgreSQL. Why go looking for trouble with these forks? But if you insist, I have a ready-made, free option for that too.

Don't know how to set it up? Spend 2,000 yuan on a consultation, and I can at least explain exactly what you need to do. With a subscription at 50,000 yuan a year, I can help you avoid most of these pitfalls before they happen. You don't need to hire a dedicated person. Most failures resolve automatically, and backups, including off-site backups, largely take care of themselves. Fifty thousand yuan a year won't even hire an intern in one of China's major cities.

The other option is to cobble something together yourself, save that 2,000 or 50,000 yuan, and then spend hundreds of thousands of yuan on data recovery after it blows up, losing contracts worth millions or tens of millions along the way. Here is the catch: most people only start taking databases seriously after a disaster. In all these years, I've seen very few companies that understood their importance from day one. That understanding isn't something you pick up off a shelf for free. People earn it by running headfirst into a wall—and usually only after they've bloodied themselves.

Preventing trouble is therefore a thankless business. Fix a problem before it happens, and there is no drama and little money in it. The rescuer brings a dying patient back to life. You prevent countless incidents that, in the client's mind, “would never have happened anyway.” To them, those two things differ in value by two orders of magnitude.

Bian Que's eldest brother doesn't get paid.

## Don't Haggle over Bandages While You're Bleeding

My second point: when a decision is needed, make it. Stop dragging your feet. The first two days after an incident are often spent debating whether to pay for recovery, rather than recovering anything. I'm not singling anyone out. I've seen the same sequence many times: Can you take a look for free first? Can you assess how much is recoverable? Could you get the data out before we discuss the price? We need to discuss this internally and go through our approval process—

And there go two days.

Throughout all this back-and-forth, the disk isn't waiting for you. New writes can overwrite deleted blocks at any moment. Every extra minute the business keeps running reduces the amount of data that could, in principle, be recovered. That's physics. It doesn't negotiate. Suppose a contract worth tens of millions of yuan is on the line, your database is gone, and recovery costs hundreds of thousands. What would I do? Pay the damn money, right now. The sooner, the better.

Sign the contract and pay immediately, and the specialist can work through the night, 24/7. Why should someone pull three all-nighters for you without a signed contract? The delay creates further damage that might otherwise have been avoided. Downtime, lost data: how do those costs compare with the recovery fee? The arithmetic is simple. Under stress, though, people tend to focus on a different question: “Am I being ripped off?”

It's like being rushed to the emergency room in the middle of the night and haggling with the ambulance driver from your stretcher.

What most companies lack is not money but a sense of when to escalate. They have no plan that says: for an incident of this severity, this person can authorize this much spending within this many minutes. When something goes wrong, the report crawls up the hierarchy and everyone waits for an answer. By the time the person with authority understands what happened, the best recovery window has already closed.

## I'd Rather Have Less of This Business

Data recovery requires deep expertise and substantial effort, with no certainty about the outcome. People who can actually do it deserve to be paid accordingly.

Two thousand yuan for a consultation. Fifty thousand yuan a year for a subscription. Hundreds of thousands for recovery. Business worth millions or tens of millions. Anyone can do that arithmetic. Most people simply refuse to pick up a pencil until the building collapses. What saddens me is how much of this business should never have existed.

What could have been a planned restore from backup becomes an expert doing archaeology on surviving data files. What could have been an agreed response channel becomes a desperate search for help in an incident chat. It looks like a heroic rescue. Behind it lies a pile of avoidable trouble.

So don't make “we can always find an expert to salvage it” your disaster recovery plan. An expert should be your last resort, not your only backup. I'd much rather help people put the missing pieces in place while their systems are still healthy. Fewer legends, more routine. Fewer overnight rescues, more people going home on time.

I hope the next friend who gets in touch tells me their business has grown and they need a few more databases. Not that the database is gone again, there are still no backups, and I need to find someone fast.

As for “spectacular database wipe” stories, **I'd rather never have another one to write about.**
