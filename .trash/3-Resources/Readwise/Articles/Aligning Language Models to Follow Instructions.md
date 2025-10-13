---
aliases: []
tags:
---
# Aligning Language Models to Follow Instructions

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
### Metadata
Author: [[openai.com]]
Full Title: Aligning Language Models to Follow Instructions
Category: #readwise/articles
URL: https://openai.com/blog/instruction-following/
Date Highlighted: [[2022-05-21-Saturday]]

## Highlights
- We first collect a dataset of human-written demonstrations on prompts submitted to our API, and use this to train our supervised learning baselines. Next, we collect a dataset of human-labeled comparisons between two model outputs on a larger set of API prompts. We then train a reward model (RM) on this dataset to predict which output our labelers would prefer. Finally, we use this RM as a reward function and fine-tune our GPT-3 policy to maximize this reward using the PPO algorithm.
