---
aliases: []
tags:
---
# Improving Vision Transformer Efficiency and Accuracy by Learning to Tokenize

![rw-book-cover](https://blogger.googleusercontent.com/img/a/AVvXsEiylT3_nmd9-tzTnz3g3Vb4eTn-L5sOwtGJOad6t2we7FsjXSpbLDpuPrlInAhtE5hGCA_PfYTJtrIOKfLYLYGcYXVh1Ksfh_C1ZC-C8gw6GKtvrQesKoMrEA_LU_Gd5srl5-3iZDgJc1iyCELoXtfuIXKJ2ADDHOBaUjhU8lXTVdr2E7bCVaFgVHHkmA=s72-w640-c-h208)
### Metadata
Author: [[googleblog.com]]
Full Title: Improving Vision Transformer Efficiency and Accuracy by Learning to Tokenize
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://ai.googleblog.com/2021/12/improving-vision-transformer-efficiency.html
Date Highlighted: [[2022-12-19-Monday]]

## Highlights
- at every layer, a ViT model recombines and processes patch tokens based on relations between each pair of tokens, using [multi-head self-attention](https://arxiv.org/abs/1706.03762). In doing so, ViT models have the capability to construct a global representation of the entire image. ([View Highlight](https://read.readwise.io/read/01gmpcwty6n4kprxaeeffgzjgh))
- At the input-level, the tokens are formed by uniformly splitting the image into multiple segments, e.g., splitting an image that is 512 by 512 pixels into patches that are 16 by 16 pixels. At the intermediate levels, the outputs from the previous layer become the tokens for the next layer. In the case of videos, video ‘tubelets’ such as 16x16x2 video segments (16x16 images over 2 frames) become tokens. The quality and quantity of the visual tokens decide the overall quality of the Vision Transformer. ([View Highlight](https://read.readwise.io/read/01gmpcxj8fvefejhc3xz8cqmjb))
- In “[TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?](https://arxiv.org/pdf/2106.11297.pdf)” ... we show that *adaptively* generating a smaller number of tokens, rather than always relying on tokens formed by uniform splitting, enables Vision Transformers to run much faster and perform better. TokenLearner is a learnable module that takes an image-like tensor (i.e., input) and generates a small set of tokens.

