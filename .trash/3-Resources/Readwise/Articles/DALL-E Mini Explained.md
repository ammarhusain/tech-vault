---
aliases: []
tags:
---
# DALL-E Mini Explained

![rw-book-cover](https://wandb.ai/logo.png)
### Metadata
Author: [[W&B]]
Full Title: DALL-E Mini Explained
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mini-Explained--Vmlldzo4NjIxODA?galleryTag=intermediate
Date Highlighted: [[2023-05-30-Tuesday]]

## Highlights
- • Images are encoded through a [VQGAN](https://arxiv.org/abs/2012.09841) encoder, which turns images into a sequence of tokens.
  • Descriptions are encoded through a [BART](https://arxiv.org/abs/1910.13461) encoder.
  • The output of the BART encoder and encoded images are fed through the BART decoder, which is an auto-regressive model whose goal is to predict the next token.
  • Loss is the [softmax cross-entropy](https://wandb.ai/sauravm/Activation-Functions/reports/Activation-Functions-Softmax--VmlldzoxNDU1Njgy#📢-softmax-+-cross-entropy-loss-(caution:-math-alert)) between the model prediction logits and the actual image encodings from the VQGAN. ([View Highlight](https://read.readwise.io/read/01h1pzmgpqfrwan0xcfhx93cse))
- ![](https://api.wandb.ai/files/wandb/images/projects/370265/977fe530.png)
  Training pipeline of DALL·E mini ([View Highlight](https://read.readwise.io/read/01h1pzv9r4q9ffqq3ms3jcq8wd))
- ![](https://api.wandb.ai/files/dalle-mini/images/projects/383272/43cb2ac6.png)
  Inference pipeline of DALL·E mini ([View Highlight](https://read.readwise.io/read/01h1pzqrsk3v67kjdtt4rpp13j))
- The goal of the VQGAN is to encode an image into a sequence of discrete tokens that can be used in transformers model which have proved to be very efficient in [NLP](https://wandb.ai/fully-connected/NLP). ([View Highlight](https://read.readwise.io/read/01h1pzwryhpjnw0017fppr4jkj))
