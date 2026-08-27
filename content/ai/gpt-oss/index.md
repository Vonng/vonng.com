---
title: "一夜变天，OpenAI又开源GPT模型了？"
date: 2025-08-06
authors: [vonng]
summary: >
  OpenAI开源GPT 20B/120B模型，水平与 o4-mini 相当，带有思维链可微调，支持函数调用等Agent功能，原生 MXFP4 量化，120b可以跑在高端笔记本或者单…
tags: [大模型, 开源]
---

OpenAI 开源 gpt-oss-20b 与 gpt-oss-120b 两款模型，Apache 2.0 许可证，水平与 o4-mini 相当，MoE 架构，带有思维链，可微调，本地 Agent 函数调用等功能，原生 MXFP4 量化，120b可以跑在高端笔记本或者单块 H100 上，20b版本可以跑在手机上。

![图片](01.webp)

一觉醒来，AI 世界又要变天了。这下 OpenAI 真的成 OpenAI 了。

OpenAI: 隆重推出 gpt-oss<sup>[1]</sup>

gpt-oss-120b & gpt-oss-20b 模型卡<sup>[2]</sup>

Hugging Face: gpt-oss-120b<sup>[3]</sup>

早晨起来一看，Sam Altman 发了个推说 GPT 又双叒叕开源了，这是 OpenAI 首次提供开放权重模型，而且上次开源已经是 GPT-2 时代了。\

![图片](02.webp)

在 OpenAI 的网站上也发布了公告与模型卡，而且很贴心的提供了部署运行，微调，提示词设计教程。\

![图片](03.webp)

![图片](04.webp)\

同时发布公告上还有一篇详细介绍的文章。

![图片](05.webp)

让 GPT 自己总结一下自己家的新模型：

![图片](06.webp)

![图片](07.webp)

顺便一体，Ollama, Lamma.cpp, 还有 LM Studio 等都第一时间提供了对这两个新模型的支持，你可以很方便的在自己的笔记本电脑上测试这两个模型。

![图片](08.webp)

![图片](09.webp)

### \

### References

`[1]` OpenAI: 隆重推出 gpt-oss: *https://openai.com/zh-Hans-CN/index/introducing-gpt-oss/*\
`[2]` gpt-oss-120b & gpt-oss-20b 模型卡: *https://openai.com/zh-Hans-CN/index/gpt-oss-model-card/*\
`[3]` Hugging Face: gpt-oss-120b: *https://huggingface.co/openai/gpt-oss-120b*\
