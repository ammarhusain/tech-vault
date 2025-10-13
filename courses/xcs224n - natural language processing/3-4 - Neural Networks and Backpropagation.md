---
aliases: []
created: 2022-09-01-Thursday 14:25
modified: 2023-03-10-Friday 23:15
tags: courses/xcs224n, aiml, aiml/nlp, courses/stanford
---


---

# 3 - Word Window Classification, Neural Networks, and Matrix Calculus

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture3_Slides.pdf]]

Suggested Readings:

1. [CS231n notes on backprop](http://cs231n.github.io/optimization-2/)
2. [Review of differential calculus](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/readings/review-differential-calculus.pdf)

Additional Readings:

1. [Natural Language Processing (Almost) from Scratch](http://www.jmlr.org/papers/volume12/collobert11a/collobert11a.pdf)

# 4 - Backpropagation and Computation Graphs

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture4_Slides.pdf]]
[[courses/xcs224n - natural language processing/attachments/cs224n-lecture_notes_iii.pdf]]
Suggested Readings:

1. [CS231n notes on network architectures](http://cs231n.github.io/neural-networks-1/)
2. [Learning Representations by Backpropagating Errors](http://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf)
3. [Derivatives, Backpropagation, and Vectorization](http://cs231n.stanford.edu/handouts/derivatives.pdf)
4. [Yes you should understand backprop](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b)
---

![[courses/xcs224n - natural language processing/attachments/Pasted image 20220901142853.png|500]] ![[courses/xcs224n - natural language processing/attachments/Pasted image 20220901142904.png|500]]
![[courses/xcs224n - natural language processing/attachments/Pasted image 20220901142916.png|500]]![[courses/xcs224n - natural language processing/attachments/Pasted image 20220901142925.png|500]]

## Restricted Boltzmann Machine

A boltzmann machine comes from a boltzmann (or Gibbs) distribution. It is a mishmash of hidden and visible nodes connected with each other. An RBM imposes the restriction that hidden & visible nodes aren't connected among each other (so only visible <-> hidden).

It tries to produce an energy function which is a way of saying it tries to learn a joint prob dist: `p(x,h)` where x is visible and h is hidden node. Its used in generative learning. I think a simple intuition here is that a pair of layers in a network can be modeled as an RBM. Perhaps more a theoretical construct.

[Tutorial](https://www.youtube.com/watch?v=p4Vh_zMw-HQ)

Also related to [Factor Graphs](http://deepdive.stanford.edu/inference#factor-graphs)
