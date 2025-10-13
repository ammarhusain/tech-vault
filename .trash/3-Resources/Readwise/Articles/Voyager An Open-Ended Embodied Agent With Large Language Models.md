---
aliases: []
tags:
---
# Voyager: An Open-Ended Embodied Agent With Large Language Models

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)
### Metadata
Author: [[minedojo.org]]
Full Title: Voyager: An Open-Ended Embodied Agent With Large Language Models
Category: #readwise/articles
URL: https://voyager.minedojo.org/
Date Highlighted: [[2023-05-30-Tuesday]]

## Highlights
- We opt to use code as the action space instead of low-level motor commands because programs can naturally represent temporally extended and compositional actions, which are essential for many long-horizon tasks in Minecraft. Voyager interacts with a blackbox LLM (GPT-4) through prompting and in-context learning. Our approach bypasses the need for model parameter access and explicit gradient-based training or finetuning. ([View Highlight](https://read.readwise.io/read/01h1q1j4b23dmkgeqnbe9382ks))
- Skill library. **Top: Adding a new skill.** Each skill is indexed by the embedding of its description, which can be retrieved in similar situations in the future. **Bottom: Skill retrieval.** When faced with a new task proposed by the automatic curriculum, we perform querying to identify the top-5 relevant skills. Complex skills can be synthesized by composing simpler programs, which compounds Voyager's capabilities rapidly over time and alleviates catastrophic forgetting. ([View Highlight](https://read.readwise.io/read/01h1q1ge9v6g92a3a00r0jb0jh))
