---
aliases: []
tags:
---
# Introducing Apple’s on-Device and Server Foundation Models

![rw-book-cover](https://mlr.cdn-apple.com/media/Social_1200x630_97d5eae4c9.jpg)
### Metadata
Author: [[Apple Machine Learning Research]]
Full Title: Introducing Apple’s on-Device and Server Foundation Models
Category: #readwise/articles
URL: https://machinelearning.apple.com/research/introducing-apple-foundation-models
Date Highlighted: [[2024-06-13-Thursday]]

## Highlights
- We train our foundation models on licensed data, including data selected to enhance specific features, as well as publicly available data collected by our web-crawler, AppleBot. Web publishers have [the option to opt out](https://support.apple.com/en-us/119829) of the use of their web content for Apple Intelligence training with a data usage control. ([View Highlight](https://read.readwise.io/read/01j09v6v00836e5ww29hmd5x1w))
- Both the on-device and server models use grouped-query-attention. We use shared input and output vocab embedding tables to reduce memory requirements and inference cost. ([View Highlight](https://read.readwise.io/read/01j09vjfa4hr0fx0f1qkw911cf))
- The on-device model uses a vocab size of 49K, while the server model uses a vocab size of 100K, which includes additional language and technical tokens. ([View Highlight](https://read.readwise.io/read/01j09vjqhx6tv6gawg8tdg2485))
- To maintain model quality, we developed a new framework using LoRA adapters that incorporates a mixed 2-bit and 4-bit configuration strategy — averaging 3.5 bits-per-weight — to achieve the same accuracy as the uncompressed models. ([View Highlight](https://read.readwise.io/read/01j09vk7tbgwys726mhq352t2t))
- on iPhone 15 Pro we are able to reach time-to-first-token latency of about 0.6 millisecond per prompt token, and a generation rate of 30 tokens per second. ([View Highlight](https://read.readwise.io/read/01j09vn5er6n260152tk5g1bqr))
- We utilize adapters, small neural network modules that can be plugged into various layers of the pre-trained model, to fine-tune our models for specific tasks. For our models we adapt the attention matrices, the attention projection matrix, and the fully connected layers in the point-wise feedforward networks for a suitable set of the decoding layers of the transformer architecture.
  By fine-tuning only the adapter layers, the original parameters of the base pre-trained model remain unchanged, preserving the general knowledge of the model while tailoring the adapter layers to support specific tasks. ([View Highlight](https://read.readwise.io/read/01j09vwedmz4n042hnc8nd4ea2))
- We represent the values of the adapter parameters using 16 bits, and for the ~3 billion parameter on-device model, the parameters for a rank 16 adapter typically require 10s of megabytes. ([View Highlight](https://read.readwise.io/read/01j09vxq6mqq3tp0f685c3k2af))
- We find that our models with adapters generate better summaries than a comparable model. ([View Highlight](https://read.readwise.io/read/01j09y9dzxc9fxkgbvf8yevtbv))
---
aliases: []
tags:
---
# Introducing Apple’s on-Device and Server Foundation Models

![rw-book-cover](https://mlr.cdn-apple.com/media/Social_1200x630_97d5eae4c9.jpg)
### Metadata
Author: [[Apple Machine Learning Research]]
Full Title: Introducing Apple’s on-Device and Server Foundation Models
Category: #readwise/articles
URL: https://machinelearning.apple.com/research/introducing-apple-foundation-models
Date Highlighted: [[2024-06-13-Thursday]]

## Highlights
- We train our foundation models on licensed data, including data selected to enhance specific features, as well as publicly available data collected by our web-crawler, AppleBot. Web publishers have [the option to opt out](https://support.apple.com/en-us/119829) of the use of their web content for Apple Intelligence training with a data usage control. ([View Highlight](https://read.readwise.io/read/01j09v6v00836e5ww29hmd5x1w))
- Both the on-device and server models use grouped-query-attention. We use shared input and output vocab embedding tables to reduce memory requirements and inference cost. ([View Highlight](https://read.readwise.io/read/01j09vjfa4hr0fx0f1qkw911cf))
- The on-device model uses a vocab size of 49K, while the server model uses a vocab size of 100K, which includes additional language and technical tokens. ([View Highlight](https://read.readwise.io/read/01j09vjqhx6tv6gawg8tdg2485))
- To maintain model quality, we developed a new framework using LoRA adapters that incorporates a mixed 2-bit and 4-bit configuration strategy — averaging 3.5 bits-per-weight — to achieve the same accuracy as the uncompressed models. ([View Highlight](https://read.readwise.io/read/01j09vk7tbgwys726mhq352t2t))
- on iPhone 15 Pro we are able to reach time-to-first-token latency of about 0.6 millisecond per prompt token, and a generation rate of 30 tokens per second. ([View Highlight](https://read.readwise.io/read/01j09vn5er6n260152tk5g1bqr))
- We utilize adapters, small neural network modules that can be plugged into various layers of the pre-trained model, to fine-tune our models for specific tasks. For our models we adapt the attention matrices, the attention projection matrix, and the fully connected layers in the point-wise feedforward networks for a suitable set of the decoding layers of the transformer architecture.
  By fine-tuning only the adapter layers, the original parameters of the base pre-trained model remain unchanged, preserving the general knowledge of the model while tailoring the adapter layers to support specific tasks. ([View Highlight](https://read.readwise.io/read/01j09vwedmz4n042hnc8nd4ea2))
- We represent the values of the adapter parameters using 16 bits, and for the ~3 billion parameter on-device model, the parameters for a rank 16 adapter typically require 10s of megabytes. ([View Highlight](https://read.readwise.io/read/01j09vxq6mqq3tp0f685c3k2af))
- We find that our models with adapters generate better summaries than a comparable model. ([View Highlight](https://read.readwise.io/read/01j09y9dzxc9fxkgbvf8yevtbv))

