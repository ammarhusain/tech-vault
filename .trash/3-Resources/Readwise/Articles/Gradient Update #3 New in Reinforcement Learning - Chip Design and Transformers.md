---
aliases: []
tags:
---
# Gradient Update #3: New in Reinforcement Learning - Chip Design and Transformers

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)
### Metadata
Author: [[thegradientpub.substack.com]]
Full Title: Gradient Update #3: New in Reinforcement Learning - Chip Design and Transformers
Category: #readwise/articles
URL: https://thegradientpub.substack.com/p/update-3-new-in-reinforcement-learning
Date Highlighted: [[2021-12-07-Tuesday]]

## Highlights
- Instead of using standard reinforcement learning algorithms such as TD learning, Decision Transformer trains a language model to directly predict the sequence of experiences conditioned. Then, to generate the actual policy, they query the “language model” for a sequence with high rewards and play according to that.
- A key difference in our work is the shift of motivation to sequence modeling rather than supervised learning: while the practical methods differ primarily in the context length and architecture, sequence modeling enables behavior modeling even without access to the reward, in a similar style to language or images, and is known to scale well
