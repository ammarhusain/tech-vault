---
aliases: []
tags:
---
# Introducing Model Search: An Open Source Platform for Finding Optimal ML Models

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)
### Metadata
Author: [[ai.googleblog.com]]
Full Title: Introducing Model Search: An Open Source Platform for Finding Optimal ML Models
Category: #readwise/articles
URL: http://ai.googleblog.com/2021/02/introducing-model-search-open-source.html
Date Highlighted: [[2022-02-23-Wednesday]]

## Highlights
- The system builds a neural network model from a set of predefined blocks, each of which represents a known micro-architecture, like LSTM, ResNet or Transformer layers. By using blocks of pre-existing architectural components, Model Search is able to leverage existing best knowledge from NAS research across domains. This approach is also more efficient, because it explores structures, not their more fundamental and detailed components, therefore reducing the scale of the search space.
- The search algorithms implemented in Model Search are adaptive, greedy and incremental, which makes them converge faster than RL algorithms. They do however imitate the “explore & exploit” nature of RL algorithms by separating the search for a good candidate (explore step), and boosting accuracy by ensembling good candidates that were discovered (exploit step). The main search algorithm adaptively modifies one of the top k performing experiments (where k can be specified by the user) after applying random changes to the architecture or the training technique (e.g., making the architecture deeper).

