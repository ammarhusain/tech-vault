---
aliases: []
tags:
---
# Aligning Language Models to Follow Instructions

![rw-book-cover](https://openai.com/content/images/2021/08/openai-cover.png)
### Metadata
Author: [[OpenAI]]
Full Title: Aligning Language Models to Follow Instructions
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://openai.com/blog/instruction-following/
Date Highlighted: [[2022-12-20-Tuesday]]

## Highlights
- To make our models safer, more helpful, and more aligned, we use an existing technique called [reinforcement learning from human feedback (RLHF)](https://openai.com/blog/deep-reinforcement-learning-from-human-preferences/). ([View Highlight](https://read.readwise.io/read/01gmpjnxtjrf6er2s5qtcrgp3c))
- InstructGPT models are much better at following instructions than GPT-3. They also make up facts less often, and show small decreases in toxic output generation. Our labelers prefer outputs from our 1.3B InstructGPT model over outputs from a 175B GPT-3 model, despite having more than 100x fewer parameters. At the same time, we show that we don’t have to compromise on GPT-3’s capabilities, as measured by our model’s performance on academic NLP evaluations. ([View Highlight](https://read.readwise.io/read/01gmpjnpbh5z1xm06k40kzzt19))
- We first collect a dataset of human-written demonstrations on prompts submitted to our API, and use this to train our supervised learning baselines. Next, we collect a dataset of human-labeled comparisons between two model outputs on a larger set of API prompts. We then train a reward model (RM) on this dataset to predict which output our labelers would prefer. Finally, we use this RM as a reward function and fine-tune our GPT-3 policy to maximize this reward using the [PPO algorithm](https://openai.com/blog/openai-baselines-ppo/). ([View Highlight](https://read.readwise.io/read/01gmpk0vd5cnyvz1xja37qyzxh))
- One way of thinking about this process is that it “unlocks” capabilities that GPT-3 already had, but were difficult to elicit through prompt engineering alone: this is because our training procedure has a limited ability to teach the model new capabilities relative to what is learned during pretraining, since it uses less than 2% of the compute and data relative to model pretraining. ([View Highlight](https://read.readwise.io/read/01gmpk54nd6gt9b2ms0shbt710))

