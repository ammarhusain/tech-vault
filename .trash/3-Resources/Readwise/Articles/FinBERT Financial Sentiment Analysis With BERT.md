---
aliases: []
tags:
---
# FinBERT: Financial Sentiment Analysis With BERT

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
### Metadata
Author: [[medium.com]]
Full Title: FinBERT: Financial Sentiment Analysis With BERT
Category: #readwise/articles
URL: https://medium.com/prosus-ai-tech-blog/finbert-financial-sentiment-analysis-with-bert-b277a3607101
Date Highlighted: [[2021-11-11-Thursday]]

## Highlights
- The current state-of-the-art approach to natural language understanding is using pre-trained language models by fine-tuning them for specific (downstream) tasks such as question answering or sentiment analysis.We followed that recipe and developed FinBERT as a BERT-based language model with a deeper understanding of financial language and fine-tuned it for sentiment classification.
- BERT brought two core innovations to language modelling: (1) It borrowed the transformer (T of BERT) architecture from machine translation, which does a better job of modelling long-term dependencies than RNN-based ones (excellent overview here). (2) It introduced the Masked Language Modelling (MLM) task, where a random 15% of all tokens are masked and the model predicts them, enabling true bi-directionality (B of BERT).
