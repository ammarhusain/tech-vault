---
aliases: []
tags:
---
# Towards a Conversational Agent That Can Chat About…Anything

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)
### Metadata
Author: [[ai.googleblog.com]]
Full Title: Towards a Conversational Agent That Can Chat About…Anything
Category: #readwise/articles
URL: http://ai.googleblog.com/2020/01/towards-conversational-agent-that-can.html
Date Highlighted: [[2021-09-30-Thursday]]

## Highlights
- The Meena model has 2.6 billion parameters and is trained on 341 GB of text, filtered from public domain social media conversations. Compared to an existing state-of-the-art generative model, OpenAI GPT-2, Meena has 1.7x greater model capacity and was trained on 8.5x more data.
- Researchers have long sought for an automatic evaluation metric that correlates with more accurate, human evaluation. Doing so would enable faster development of dialogue models, but to date, finding such an automatic metric has been challenging. Surprisingly, in our work, we discover that perplexity, an automatic metric that is readily available to any neural seq2seq model, exhibits a strong correlation with human evaluation, such as the SSA value. Perplexity measures the uncertainty of a language model. The lower the perplexity, the more confident the model is in generating the next token (character, subword, or word). Conceptually, perplexity represents the number of choices the model is trying to choose from when producing the next token.
