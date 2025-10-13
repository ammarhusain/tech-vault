---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

Entropy is a measure of the randomness in the information being processed. The higher the entropy, the harder it is to draw any conclusions from that information.

$$
E(s) = -\sum_i -p_i\log_2(p_i)
$$

**Multi-class classification** we want to assign a single class to an input, so we apply a [[softmax]] function to the raw output of our neural network. The output is a probability distribution (losely) and sums to 1. **Multi-label classification** we want to assign multiple classes to an input, so we apply an element-wise [[sigmoid]] function to the raw output of our neural network. Each node in the raw output is independent (not related to each other) and represents a probability between 0 & 1.

[[Negative log likelihood]] loss is used for the multi-class problem with the ground truth as a one hot vector. It computes the likelihood that the [[softmax]] output was sampled from this one hot vector.

[[Binary cross entropy]] uses the same idea but each node is a 2 element distributions (yes or no) and the loss is computed individually for each label output.

Several implementations for cross entropy in PyTorch:

In [[pytorch]], there are several implementations for cross-entropy:

**MultiLabel problems:**

- `torch.nn.BCELoss`: Input values to this function have already had a [[sigmoid]] applied.
- `torch.nn.BCEWithLogitsLoss`: Combines a [[sigmoid]] layer and the BCELoss in one single class. This version is more numerically stable than using a plain sigmoid followed by a BCELoss.

**MultiClass problems:**

- `torch.nn.NLLLoss` : Input given through a forward call is expected to contain log-probabilities of each class.
- `torch.nn.CrossEntropyLoss`: Combines `nn.LogSoftmax()` and `nn.NLLLoss()` in one single class. The input is expected to contain raw, unnormalized scores for each class.

[Good article](https://glassboxmedicine.com/2019/12/07/connections-log-likelihood-cross-entropy-kl-divergence-logistic-regression-and-neural-networks/)
