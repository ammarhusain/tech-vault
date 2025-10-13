---
aliases: []
tags:
---
# ChatGPT: Optimizing Language Models for Dialogue

![rw-book-cover](https://openai.com/content/images/2022/11/ChatGPT.jpg)
### Metadata
Author: [[OpenAI]]
Full Title: ChatGPT: Optimizing Language Models for Dialogue
Category: #readwise/articles
URL: https://openai.com/blog/chatgpt/
Date Highlighted: [[2023-03-12-Sunday]]

## Highlights
- ChatGPT sometimes writes plausible-sounding but incorrect or nonsensical answers. Fixing this issue is challenging, as: (1) during RL training, there’s currently no source of truth; (2) training the model to be more cautious causes it to decline questions that it can answer correctly; and (3) supervised training misleads the model because the ideal answer [depends on what the model knows](https://www.alignmentforum.org/posts/BgoKdAzogxmgkuuAt/behavior-cloning-is-miscalibrated), rather than what the human demonstrator knows. ([View Highlight](https://read.readwise.io/read/01gvba6e8zgcxyjs5qtf9sws99))
    - Note: For 1 it would be interesting to plug in various source of truth generators into the sampled output. So rather than operating in language space for a mathematical expression one could extract a mathematical expression from language and plug it into a calculator. Or extract a code snippet and plug it into an interpreter or compiler
