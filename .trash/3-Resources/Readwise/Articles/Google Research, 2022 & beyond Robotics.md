---
aliases: []
tags:
---
# Google Research, 2022 & beyond: Robotics

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKgvim8bYA_R-eVrpL1COlP3xBSNuRZ7Sk7mlZWX_xJVWU-51lfp7445l4DLahZAI2PGSCS9f0xUvQF2oYKXLxmfHGKFMaXIUh7TTjZsw5K715Le005qnlHkTbFP784EC-kdliQSvWHRMeq85cXLhgGAyUa4-pnysF_SXoT_L0U3DeR5OzP3pYbZxnEg/w1200-h630-p-k-no-nu/CodeAsPolicies-hero.jpg)
### Metadata
Author: [[googleblog.com]]
Full Title: Google Research, 2022 & beyond: Robotics
Category: #readwise/articles
URL: https://ai.googleblog.com/2023/02/google-research-2022-beyond-robotics.html
Date Highlighted: [[2023-05-31-Wednesday]]

## Highlights
- One of the underlying concepts is using LLMs to prompt other pretrained models for information that can build context about what is happening in a scene and make predictions about multimodal tasks. This is similar to the socratic method in teaching, where a teacher asks students questions to lead them through a rational thought process. In “[Socratic Models](https://arxiv.org/abs/2204.00598)”, we showed that this approach can achieve state-of-the-art performance in zero-shot image captioning and video-to-text retrieval tasks. ([View Highlight](https://read.readwise.io/read/01h1shcyks2qj1fs2rwbpsks7t))
- one needs to have both an LLM that can predict the sequence of steps to complete long horizon tasks *and* an affordance model representing the skills a robot can actually do in a given situation. In “[Extracting Skill-Centric State Abstractions from Value Functions](https://ai.googleblog.com/2022/04/extracting-skill-centric-state.html)”, we showed that the [value function](https://en.wikipedia.org/wiki/Value_function) in reinforcement learning (RL) models can be used to build the affordance model — an abstract representation of the actions a robot can perform under different states. ([View Highlight](https://read.readwise.io/read/01h1shem0evemgryh4wyjvcbp7))
- Inspired by the recent success of LLMs, which shows that the generalization and performance of large Transformer-based models scale with the amount of data, we are taking a data-driven approach, turning the problem of learning low-level physical skills into a scalable data problem. With [Robotics Transformer-1](https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html) (RT-1), we trained a robot manipulation policy on a large-scale, real-world robotics dataset of 130k episodes that cover 700+ tasks using a fleet of 13 robots ([View Highlight](https://read.readwise.io/read/01h1sj01654aq6x2kabrx3z6re))
- Advances in large models across the field of AI have spurred a leap in capabilities for robot learning. This past year, we’ve seen the sense of context and sequencing of events captured in LLMs help solve long-horizon planning for robotics and make robots easier for people to interact with and task. We’ve also seen a scalable path to learning robust and generalizable robot behaviors by applying a transformer model architecture to robot learning. ([View Highlight](https://read.readwise.io/read/01h1shyjgertzf0kstnr1ztdzk))
