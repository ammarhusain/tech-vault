---
aliases: []
tags:
---
# Feature Visualization

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)
### Metadata
Author: [[distill.pub]]
Full Title: Feature Visualization
Category: #readwise/articles
URL: https://distill.pub/2017/feature-visualization
Date Highlighted: [[2022-04-10-Sunday]]

## Highlights
- Neural networks are, generally speaking, differentiable with respect to their inputs.
  If we want to find out what kind of input would cause a certain behavior — whether that’s an internal neuron firing or the final output behavior — we can use derivatives to iteratively tweak the input
  towards that goal
- It turns out that optimization approach can be a powerful way to understand what a model is really looking for,
  because it separates the things causing behavior from things that merely correlate with the causes.
- Optimization also has the advantage of flexibility.
  For example, if we want to study how neurons jointly represent information,
  we can easily ask how a particular example would need to be different for an additional neuron to activate.
  This flexibility can also be helpful in visualizing how features evolve as the network trains.
  If we were limited to understanding the model on the fixed examples in our dataset, topics like these ones would be much harder to explore.
