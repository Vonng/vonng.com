---
title: "Codex Edited My Video in One Shot for About 8 Yuan"
date: 2026-09-23
authors: [vonng]
summary: >
  I gave Codex three panel recordings and a casually dictated prompt. Forty-eight minutes later, it delivered a finished edit with subtitles, at an estimated amortized subscription cost of about 8 yuan. Coding agents are finding their way into everyday life.
tags: [AI, Codex, Tools]
---

> [WeChat article](https://mp.weixin.qq.com/s/JMjX9A_5_L5fn3g5JGpC-A)

When GPT-6 Astra came out a little while ago, I heard that people were using it with Codex to edit videos, with pretty good results. With another update out, I finally had to try it myself.

Yesterday, I took part in a [panel discussion at an AI conference](https://mp.weixin.qq.com/s?__biz=MzU5ODAyNTM5Ng==&mid=2247493372&idx=2&sn=9915f2dc25ac30114b326e64b6760eba&scene=21#wechat_redirect) and recorded the whole thing on my Pocket 4. Usually, footage like this goes straight onto a hard drive to gather dust. I never get around to editing or posting it.

There was a row of guests on stage, and the moderator asked each of us in turn. Just thinking about digging out my parts and adding subtitles sentence by sentence felt exhausting. But if Astra is so damn good, why not let it do the job? The finished video is already on WeChat Channels, edited in one shot.

## The Prompt

Here is my original prompt. One shot, with no adjustments or corrections:

> I don't know whether you can edit videos. This directory contains three recordings of a panel discussion, in chronological order. I'm the fat guy dressed in black, fifth from the left and second from the right.
>
> I'd like you to do a few things to turn them into a finished video I can publish:
>
> 1. Edit the footage: Use Final Cut Pro and keep only the parts where the moderator and I are speaking. The moderator asks each guest in turn. Cut out everything the other guests say, keeping just the moderator's questions and my answers.
> 2. Create and add subtitles: Extract the audio from these videos. Find a speech-to-text tool, whatever works, to produce a complete plain-text transcript, then turn it into subtitles and add them to the video.
> 3. Export settings: Edit these three videos into a single video. It doesn't need to be 1080p; 720p is fine.
>
> Can you give this a try and edit the panel video for me?

As you can see, this is a pretty casual prompt. I simply handed over an everyday request in plain language. In fact, I dictated it. The entire input process was three button presses: Start Dictation, Stop Dictation, Enter. My only preparation was to create a new directory and put the three video files copied from the Pocket 4 into it. That was it.

Forty-eight minutes later, the result was ready, and I was very happy with it. It had picked out exactly the exchanges between the moderator and me.

![Codex's delivery report after editing the panel video](01.webp)

## The Result

I've already posted the finished video on WeChat Channels. Honestly, it exceeded my expectations.

What surprised me most was how it went about the work. It didn't have a speech recognition tool available, so it downloaded a Qwen ASR model, ran it locally, and transcribed everything I said. It drove the whole process itself: sampling video frames to inspect the footage, extracting audio, transcribing speech, checking and correcting the text, creating subtitles, aligning them with the timeline, then cutting, assembling, and exporting the video.

![Codex operating Final Cut Pro to edit, subtitle, and export the video](02.webp)

![Video, subtitles, transcripts, and project files produced by the editing task](03.webp)

I kept working on the same computer while it operated Final Cut Pro in the background, smoothly handling the job on its own. All I did was copy the videos over and give Codex that prompt.

In the past, that workflow would have taken a good part of a day, even for someone who knew ffmpeg, understood a bit of speech recognition, and was comfortable with video editing software. Existing AI video editing tools would still involve a learning curve and some manual work. Now it takes a few words.

Having seen what it can do, I'm now asking it to go through my video archive—several terabytes of footage accumulated over the years—and see what could make a decent video worth posting.

## The Cost

I used Codex's most powerful configuration: GPT-6 Astra in Fast mode, with reasoning effort set to Max. This task consumed about 29.1 million tokens, with a cache hit rate of 98.6% for input tokens. At API rates, the estimated cost would have been under 500 yuan. Of course, you'd be a fool to pay metered API rates for this. Everyone uses subscriptions.

![Token usage statistics for the Codex video editing task](04.webp)

The Codex 20x Pro subscription costs $200 a month. With an average of 4.33 weeks per month, plus the 10 complimentary resets handed out over the past month, that adds up to the equivalent of 14.33 weekly allowances if fully used. During this task, my account's remaining weekly quota fell by about 8 percentage points. Using that change as a rough basis for allocating the subscription cost, and assuming all the quota replenished by resets was fully used, the task consumed about 0.56% of the monthly budget. At an assumed exchange rate of 6.7 yuan to the dollar, that comes to 7.5 yuan.

![Estimated amortized subscription cost with and without complimentary resets](05.webp)

Without the resets, it would be roughly 1.9% of the monthly allowance, or 25 yuan. Elapsed time: 48 minutes. Since I didn't have to watch it, the cost in my own time was close to zero.

That is a startlingly low cost. Including that month's complimentary resets and amortizing the subscription on the assumption that the available quota was fully used, this edit worked out to about 8 yuan. For a finished video, that's a bargain.

## A Jevons Paradox

I think this is an excellent use case, and it could produce a very interesting instance of the Jevons paradox.

The Jevons paradox says that when something becomes more efficient and cheaper to use, total consumption can rise rather than fall. Steam engines became more efficient at burning coal, and total coal consumption soared. Video editing follows the same logic: when the cost of editing a video drops from "an afternoon and a set of specialized skills" to "a few words," we won't just be editing the same videos as before. There will be orders of magnitude more of them.

This is something ordinary people encounter every day. Anyone can shoot video on a phone, and everyone's phone holds hundreds or thousands of "dead" clips: recorded with enthusiasm, then never opened again. People don't lack the desire to edit them. They lack the capacity. They would have to learn the software, find the time, and patiently sift through footage frame by frame. If those clips could easily become something decent enough to share, that would be enormously appealing.

A friend of mine has been struggling with exactly this. His child is three, and he has shot piles of video over the years without ever finding time to edit it. Until now, Codex had nothing to do with his life. A coding tool—what use would he have for that? In the future, this could be a reason for him to pay for a subscription.

That's the part I find really interesting. People have treated Codex and Claude Code as tools exclusively for programmers, but fundamentally, an agent like this can do things on your computer. Coding was simply the first use case that worked. The bigger market is in editing videos, organizing photos, filing documents: everyday chores people have always been left to handle themselves. When the audience expands from tens of millions of programmers to everyone who has ever shot a video on a phone, you can do your own arithmetic on what happens to token consumption.

I was honestly amazed that I could just hand over raw footage and get a well-edited video back. All those clips gathering dust on my hard drive finally have a chance to see the light of day.
