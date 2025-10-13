---
aliases: []
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
tags: courses/xcs224u
---


[[courses/xcs224u - natural language understanding/xcs224u - natural language understanding]]
[[courses/xcs224u - natural language understanding/attachments/XCS224U_Mod1-distributed-word-representations.pdf]]

1. Notebook: [Designs, distances, basic reweighting](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/vsm_01_distributional.ipynb)
2. Notebook: [Dimensionality reduction and representation learning](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/vsm_02_dimreduce.ipynb)
3. Notebook: [Retrofitting](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/vsm_03_retrofitting.ipynb)
---

- Firth: "You shall know a word by the company it keeps" #readwise/qt 
- Context matters a lot in language as words take on different meanings in different contexts.

![[courses/xcs224u - natural language understanding/attachments/xcs224u-1-cooccurrence.png]]

- Just by looking at a word co-occurence matrix we can get a bunch of semantic information

![[courses/xcs224u - natural language understanding/attachments/xcs224u-1-word-dist.png]]

# Reweighting
- However there are a bunch of manual steps that you need to mix & match to get these co occurrence matrices rich. For ex: what word tokens to use, how to remove non useful words (like pronouns: he/she..., articles: a/an/the etc.). [[PMI]] is apparently common for re-weighting.
![[courses/xcs224u - natural language understanding/attachments/xcs224u-1-context-scaling.png]]

**Pointwise Mutual Information:** Probability of 2 words occuring together (jointly) divided by the probability of each word occuring by itself.
$\huge \frac{P(x,y)}{P(x)*P(y)}$

![[pmi.png]]

- [[GloVe]] & [[Word2Vec]] are sensible defaults that take away some of the need to mix & match.

![[courses/xcs224u - natural language understanding/attachments/xcs224u-1-matching-methods.png]]

- [[cosine distance]] is the workhorse of these vector similarity measures. If it has not been specified, this is usually the default.
- [[KL divergence]] measures similarity between a distribution w.r.t a reference distribution.(non-symmetric)

![[courses/xcs224u - natural language understanding/attachments/xcs224u-kl_divergence_variants.png]]

- Spearman's correlation
	Measures how correlated 2 sequences are.
	Ranges from +1 to -1
	+1 means there is a strong positive correlation, aka if one number increases the other number increases as well.
	-1 indicates strong negative correlation, aka if one number increases the other number decreases.
