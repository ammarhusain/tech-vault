---
aliases: []
created: 2023-04-22-Saturday 08:51
modified: 2023-06-22-Thursday 12:37
tags: 
---
# Pathways Language Model (PaLM): Scaling to 540 Billion Parameters for Breakthrough Performance

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)

## Metadata

Author: [[ai.googleblog.com]]
Full Title: Pathways Language Model (PaLM): Scaling to 540 Billion Parameters for Breakthrough Performance
Category: #readwise/articles
URL: http://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html
Date Highlighted: [[2022-04-08-Friday]]
[[ai-ml]]

## Highlights
- In “PaLM: Scaling Language Modeling with Pathways”, we introduce the Pathways Language Model (PaLM), a 540-billion parameter, dense decoder-only Transformer model trained with the Pathways system, which enabled us to efficiently train a single model across multiple TPU v4 Pods. We evaluated PaLM on hundreds of language understanding and generation tasks, and found that it achieves state-of-the-art few-shot performance across most tasks, by significant margins in many cases.
- PaLM 540B shows strong performance across coding tasks and natural language tasks in a single model, even though it has only 5% code in the pre-training dataset. Its few-shot performance is especially remarkable because it is on par with the fine-tuned Codex 12B while using 50 times less Python code for training. This result reinforces earlier findings that larger models can be more sample efficient than smaller models because they better transfer learning from other programming languages and natural language data.
- PaLM paves the way for even more capable models by combining the scaling capabilities with novel architectural choices and training schemes, and brings us closer to the Pathways vision:
  “Enable a single AI system to generalize across thousands or millions of tasks, to understand different types of data, and to do so with remarkable efficiency."

