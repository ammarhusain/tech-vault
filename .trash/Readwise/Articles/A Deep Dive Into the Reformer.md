---
aliases: 
tags:
  - readwise/doc/aiml
---
# A Deep Dive Into the Reformer

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)
### Metadata
Author: [[pragmatic.ml]]
Full Title: A Deep Dive Into the Reformer
Category: #readwise/articles
URL: https://www.pragmatic.ml/reformer-deep-dive/
Date Highlighted: [[2021-09-27-Monday]]

## Highlights
- sharp contrast to the "bigger is better" trend of the past two years, and was accepted for a talk at ICLR 2020. The Reformer paper reads like a breath of fresh air – focusing primarily on how the self-attention operation scales with sequence length, and proposing an alternative attention mechanism to incorporate information from much longer contexts into language models.
- With the Reformer's changes to the Transformer, they're able to attend over sequences up to 64,000 tokens in length on a single accelerator – which is in sharp contrast to the 1024 token context size of MegatronLM and TuringNLP, both of which used pipeline model parallelism to cope with their massive parameter counts.
- Query - Key - Value ProjectionThe QKV projection. Although we've drawn this operation as three independent linear projections, it's typically implemented as a single matrix multiply for purposes of computational efficiency. In this stage the current hidden state for each token is broken up into three components via a linear projection.
- If your keys and queries are tensors of shape (batch, sequence_length, hidden_size), the output of the matrix multiply is a tensor of shape (batch, sequence_length, sequence_length).  This seemingly innocuous matrix multiply is the source of the self-attention operation's computational complexity issues.
- First, they observe that learning different projections for keys and queries are not strictly necessary.  They toss out the query projection and reframe the attention weights as a function of key agreement.
- If we want to find a value that corresponds to a given key, we typically don't iterate over a list of all keys and check each to see if we have a match. Instead, we use hash map data structures to do O(1) lookups rather than O(n) comparisons.  Conveniently, an analogue to hash maps for vector spaces does exist, and it's called "locality sensitive hashing" (LSH). It's to this method that the authors of the Reformer paper look to produce a transformer alternative that avoids the quadratic complexity of dot product attention.
- Locality sensitive hashing is a family of methods that map high dimensional vectors to a set of discrete values (buckets / clusters). It's most commonly used for as a method for approximate nearest neighbor search, for applications like near duplicate detection or visual search.Locality sensitive hashing methods try to assign vectors that are close in their high dimensional space to the same hash with high probability.
- Locality sensitive hashing-based attention and reversible layers form the basis of the Reformer's blueprint for a more efficient transformer

