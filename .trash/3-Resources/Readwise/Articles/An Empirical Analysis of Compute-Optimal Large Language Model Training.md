---
aliases: []
tags:
---
# An Empirical Analysis of Compute-Optimal Large Language Model Training

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)
### Metadata
Author: [[deepmind.com]]
Full Title: An Empirical Analysis of Compute-Optimal Large Language Model Training
Category: #readwise/articles
URL: https://www.deepmind.com/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training
Date Highlighted: [[2022-12-04-Sunday]]

## Highlights
- the training compute cost for transformers is determined by two factors: the model size and the number of training tokens.
  The current generation of large language models has allocated increased computational resources to increasing the parameter count of large models and keeping the training data size fixed at around 300 billion tokens. ([View Highlight](https://read.readwise.io/read/01gkf0hc3c81vdh2ap2ch3v225))
- Our main finding is that the current large language models are far too large for their compute budget and are not being trained on enough data. In fact, we find that for the number of training FLOPs used to train *Gopher*, a 4x smaller model trained on 4x more data would have been preferable.
  ![](https://assets-global.website-files.com/621e749a546b7592125f38ed/62557f7626b9e103db549c7b_tokens_vs_flops%20(1).png) ([View Highlight](https://read.readwise.io/read/01gkf0ttj2ktkc4jxmdkpaj9rf))
- 70-billion parameter model trained for 1.3 trillion tokens ([View Highlight](https://read.readwise.io/read/01gkf0vp54n82twnpzzecwb80h))
