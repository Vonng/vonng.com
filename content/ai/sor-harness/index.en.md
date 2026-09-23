---
title: "The Application Layer Is Collapsing: The Moat Moves to the Database"
date: 2026-09-22
authors: [vonng]
summary: >
  As agents take over software interfaces and execution logic, where does the application layer go? Future software will consist of a lasting system of record and harnesses that are continually replaced and recombined. The operator can change. The books must stay straight. The rules must stay put.
tags: [AI, Agent, Database, Commentary]
---

> This is the script for a talk at the AI-Native Technology Innovation Forum of the 2026 Shanghai AI Application Ecosystem Conference, September 22, 2026.
>
> Speaker: Ruohang Feng (Vonng), creator of the PostgreSQL distribution Pigsty.

Good afternoon. I'm Ruohang Feng, creator of the PostgreSQL distribution Pigsty.

One disclosure before we start: I sell a Postgres distribution. Today's conclusion happens to favor my business, so apply whatever discount you think it deserves.

## Opening: Who Is Building Databases, and Who Is Reading the Docs?

PostgreSQL was hot property for investors last year, with several acquisitions. The most conspicuous was Databricks buying Neon for roughly a billion dollars. Neon also disclosed a striking number: **more than 80% of the databases on its platform were created by agents, not people.**

Supabase disclosed two more numbers this June: database creation on its platform had **grown 600% over the past year**, and **more than 60% of those databases were created by AI tools**. It also raised $500 million in that funding round, at a $10.5 billion valuation—double its valuation eight months earlier.

Both companies offer serverless Postgres. Their numbers tell the same story: **backend databases are increasingly being set up by agents rather than people.**

I believe it, because I've run into this myself.

I maintain a PostgreSQL distribution with 6,000 GitHub stars. Among open-source projects working on the Postgres ecosystem and distributions, it is one of the strongest contenders in China and internationally. As an infrastructure project, we have a documentation site.

How much traffic would you expect a database distribution's documentation site to get? **We used to get one or two million page views a year, at most.**

After one change we made this year, traffic exploded. **Monthly page views went from one million to 100 million—a hundredfold increase.**

What happened?

We compared our Cloudflare and Google Analytics data: **roughly 200,000 human users over the year, with monthly active users on the order of 100,000.**

How could 100,000 people possibly generate 100 million page views?

Then we dug into the access logs. **More than 90% of the traffic came from agents.** A smaller share came from AI companies' training-data crawlers, but the bulk came from agents of all kinds reading the docs and learning how to use the software.

We have observed this trend firsthand: **agents now come to read the docs and learn how things work far more often than humans do.**

## 1. AI Replaces UI

Of course, this isn't confined to developer tools.

In 2024, Microsoft CEO Satya Nadella said something few people took seriously at the time: **enterprise applications are essentially wrappers around databases. A database plus create, read, update, and delete—that is what an enterprise application is.**

Follow that argument and the next step is obvious: **if your backend application can perform those CRUD operations, why can't an agent?**

People shrugged it off. But the tsunami was already on the horizon.

Now everyone says, “The frontend is dead.” Is it? I think it's pretty close.

And the backend? **I think that's pretty close to dead, too.** Why? Look at Supabase. Its proposition is Backend as a Service. **Supabase's popularity is itself a sign of the backend's decline.**

If that is only a sign, the strongest evidence came last week. At Dreamforce, industry heavyweight Salesforce announced **AIforce**, connecting CRM workflows with Claude and Slack. From a chat window, inside your agent's cockpit, you can look up customers, edit records, and trigger workflows, **without ever opening Salesforce.**

Its own slogan? **“AI replaces UI.”**

The industry leader is telling you that you no longer need to look at its interface.

So I think “the application layer is collapsing” is already common ground. I don't need to spend this talk proving it.

**The real question is: where does that layer end up?**

Users may never open Salesforce, but the application's capabilities are still being called. Where will those capabilities live?

Here is my prediction: **the software endgame is Database plus Harness.**

## 2. Two Terms: System of Record and Harness

It isn't just Nadella saying this, or just me.

The latest example came a week ago, when Y Combinator CEO Garry Tan said:

> Either you die a system of record, or you live long enough to become a domain-specific harness.

It's a riff on the line from *The Dark Knight* about dying a hero or living long enough to become the villain.

I think he is restating the same proposition more precisely. **Two things really matter: the System of Record and the Harness.**

There is no settled Chinese translation of “harness” yet. Some translations refer literally to horse tack. I find **“cockpit”** a more useful metaphor. For today, think of the two as **a system of record and a cockpit.**

That leaves two questions:

- **How does a system of record relate to a database?**
- **How does a harness relate to an agent?**

Let's look at concrete examples. **For the system of record, Supabase. For the harness, Codex, Jev, and DSH.**

## 3. The System of Record: What Supabase Got Right

If you ask who in China knows Supabase best, I'll happily claim the top spot. **We supported complete, enterprise-grade, self-hosted Supabase back in 2023**, building and packaging its custom extensions and database kernel. Even today, few open-source projects can do that.

So why has Supabase succeeded?

Because it put a pretty admin interface on PostgreSQL? Because it's free?

Neither.

It got two things right: **row-level security and automatically generated APIs.**

The core component behind automatic API generation is another open-source project, **PostgREST**. It generates a REST API directly from the database schema. **You no longer have to write a CRUD backend.**

But here's the question: **PostgREST has been around for over a decade. I've been using it for over a decade. Why did it suddenly become magic?**

Because Supabase also took care of **authentication** on the way in and **permissions** behind the API.

Expose an automatically generated API without proper authentication and authorization, and you have a toy. Nobody will trust it in production. **Adding authentication and permissions is what makes it a foundation for enterprise applications.** That's why Supabase is no longer just for startups. I've seen people using it even in Chinese state-owned enterprises.

Take a SaaS application. Each user maps to an identity in the database. Combine that with Postgres privileges and row-level security policies:

One user sees these tables; another sees those tables. **Even within the same table, one user can see only these rows, while another sees a different set.**

One schema, different views of the data for different people. **What used to be one of the biggest headaches in multitenant application development suddenly becomes simple.**

So what is Supabase? Is it a database?

No. **It is PostgreSQL plus authentication, automatic API generation, and RLS access control, built around PostgREST and GoTrue—a general-purpose backend harness.**

It calls itself **Backend as a Service**: I'm not providing a database; I'm providing a backend.

**That is why it can call itself infrastructure for the agent era, rather than just another serverless PostgreSQL.** Many people miss this distinction, including many of the people cloning Supabase in China.

**What it really got right was bringing authentication and permissions into the database.**

## 4. The Harness: Codex, Jev, and DSH

### Codex: From Coding Assistant to General-Purpose Agent

How many of you use Codex or Claude Code? If you do, you know what I'm talking about.

What Codex can do now is absurdly powerful. Give it a laptop and ask it to do 3D modeling, play games, edit video, configure Cloudflare DNS, or sign up for an AWS account. **You still have to handle payments and enter passwords yourself, but it can now do pretty much anything else you can do on a computer.**

Seriously: **apart from entering your passwords and serving your prison sentence, it can do anything you can do on a computer.**

I've become so lazy that I hand everything to Codex, including today's slides. **I dictated the script. Codex made the entire presentation.**

Don't let the “coding agent” label fool you into thinking it only writes code. **It is already a general-purpose agent.**

**Isn't this a glimpse of what software will become?**

If I can just tell Codex what I want and have it do the work, why would I open a dedicated application and learn how to use it? **Why not have it read the database directly?**

Here's an example from my own work. I maintain several sites, including the Chinese PostgreSQL documentation and the Postgres extension catalog. They're simple static sites; all the data comes from databases. Maintenance, updates, proofreading, hunting down whatever new extensions appeared today, then building everything and publishing it to the repository—**agents do all of that now.**

**If something as complex and intellectually demanding as software development can be handled this smoothly, how hard can a little CRUD be?**

There were only two reasons people didn't do this before: **too slow, too expensive.**

Who wants to wait ten or twenty seconds for an LLM to spit out text, or pay a few yuan per call?

### Jev: The Kind of Model Programs Need

But doesn't **Jev**, released just last week, solve that problem?

You no longer need the model to produce paragraphs of waffle. **Give it a defined question and a set of options, and in tens of milliseconds it tells you which option to pick and with what probability.**

**Isn't that exactly the kind of model a program needs?**

People used to think letting agents read and write databases directly was fantasy. That has changed, because things like Jev now exist.

Jev may not be the eventual winner, but it has opened up a new approach: **at very low cost, with performance on the order of an OLTP index lookup, you can do work that used to take an LLM seconds or even minutes.** It opens up a new possibility for the harness.

### DSH: An Execution Layer That Can Replace Itself

Then there is **DSH, DeepSeek Harness.**

“Software that evolves itself” used to sound like science fiction. **Isn't that what DSH is?**

Its slogan is “Everything is a Plugin.” **Even the agent loop itself is a plugin that can be replaced while the system is running.** The loops in Codex, Cursor, and Claude Code are hardwired into their cores. DSH pulls the loop out and makes it a replaceable part.

To do this, it built three things: **a side-effect undo stack, dependency reactivity, and transactional hot updates.**

Listen to those three words: **undo, dependencies, transactions.**

**To make its execution layer safe to hot-swap, DSH has reimplemented, inside a process, guarantees that databases had thirty years ago.** That's not a sneer. It's the project's most concrete contribution: the engineering work demonstrates **exactly what guarantees a replaceable execution layer needs.**

Ask it for a feature, and it writes a few plugins for itself, becoming an agent tailored to your domain.

## 5. From One-Off Tasks to Fixed Code

So here is how I see future software: **a spectrum, with progressively more of the work crystallized into a fixed form.**

Software used to be rigid. You wrote the program in advance, and it could perform only its prescribed CRUD operations. Future software will be much more flexible.

### Level One: Direct Programming, Disposable Software

I want to book a flight, but I don't know how. An agent figures out Ctrip's API, writes a working script, finds the best flight, and gets the job done. **Just this once.**

### Level Two: Crystallizing the Workflow

Then a colleague needs to book a flight, too. So we crystallize that task. The first time is the hard part: the agent has to deal with enormous complexity and uncertainty. The second time, it only needs to make decisions at a few key points. **What once required a large model like Astra or Fable can now be handled by Jev.**

### Level Three: Fixed Entirely in Code

Go one step further. Once the whole process is understood and the business logic can be fully expressed, write it as a script or a function. Next time you need a flight, call the function. **No intelligent judgment required.**

**Aren't we back to the old CRUD application?**

Except this CRUD application **has grown around the flight-booking company's services.**

For people using coding agents, none of this is fantasy. It's already happening.

Enterprises may adopt it more slowly. Their harnesses may contain more CRUD, or even consist entirely of CRUD with an LLM as a finishing touch. Startups may embrace it faster and hand everything to the model.

**Finding the right balance of intelligence, cost, speed, and throughput for your niche—that is the problem the harness has to solve.**

Which raises the next question: **once harnesses look like this, what will they demand of the database underneath?**

## 6. The Last Fortress

At the heart of a Turing machine are state transitions.

My point is this: **you can replace the transitions. You cannot lose the state.**

Where does that state live? **In the System of Record.**

As the harnesses above become more numerous, more flexible, and more inventive, **the system of record below has to do more.**

The database's job goes beyond storing data. It must also enforce **the boundaries of what can be done to that data**: authentication, permissions, access control, and consistency.

**Business invariants will move down into the database.**

Why? Because **you never know what another harness you work with will do to your system.** What can all parties rely on? The underlying source of truth, the system of record.

It's the old warning from microservices: **you design an exquisite authentication and access-control system in the application layer, then someone connects directly to your database with a connection string, and your controls turn out to be made of tissue paper.**

That arrangement used to work because the only thing with the connection string was a vetted application server.

**Now the thing holding the connection string is a probabilistic agent, vulnerable to prompt injection, whose next action you cannot guarantee.**

I expect the database to absorb these responsibilities, **just as Supabase has already done.**

## Closing: Change the Operator, Keep the Books Straight

Let's return to those two examples.

**Salesforce** shows one path from an existing application: keep the business capabilities and open up every way of accessing them.

**Supabase** shows another way to organize things: build composable infrastructure for authentication, authorization, and access around the database.

My prediction goes one step further:

> More and more transactional business software will **cease to be an application you must buy, use, and replace as a single unit**. It will be a lasting system of record, plus harnesses that are continually replaced and recombined.

That still sounds a little abstract, so here is **a test you can apply yourselves**:

> **When you replace the agent, the interface, or the orchestration workflow, do you still have to rebuild the ledger, rewrite the permissions, and migrate the core business constraints?**
>
> **The less you have to do that, the closer you are to System of Record plus Harness.**

You don't have to take my word for it, or wait ten years. Ask that question about the system you work with, and you can have an answer today.

Software isn't disappearing. Its boundaries are changing.

The things that understand intent, choose a path, and organize execution belong in the harness. The things that must endure, be respected by everyone, and remain reliably traceable belong in the system of record.

**The operator can change. The books must stay straight. The rules must stay put.**

Thank you.
