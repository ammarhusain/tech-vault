---
aliases: []
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
tags: aiml 
---


---

[[ensemble learning]] algorithms or methods can be divided into two groups:

# Sequential Ensemble Methods

where the base learners are generated sequentially (e.g. AdaBoost).
The basic motivation of sequential methods is to exploit the dependence between the base learners. The overall performance can be boosted by weighing previously mislabeled examples with higher weight.

# Parallel Ensemble Methods

where the base learners are generated in parallel (e.g. Random Forest).
The basic motivation of parallel methods is to exploit independence between the base learners since the error can be reduced dramatically by averaging.

[[Random Forests]] are parallel ensemble methods where [[Decision Trees]] are the base learners. A large number of relatively uncorrelated models (trees) operating as a committee will outperform any of the individual constituent models. (wisdom of crowds).
Two key concepts that give it the name random:

- A random sampling of training data set when building trees,
- Random subsets of features considered when splitting nodes.

[[Decision Trees]] are simply a hierarchical set of if/else nodes that are learned to split on a given feature/attribute in order to maximize some criterion (like Gini index). Goal is to somehow lower entropy (similar to loss functions in NN or logistic regression etc).

Articles: [decision trees](https://towardsdatascience.com/decision-tree-algorithm-explained-83beb6e78ef4), [random forests](https://towardsdatascience.com/random-forest-a-powerful-ensemble-learning-algorithm-2bf132ba639d)
