---
aliases: []
created: 2023-02-01-Wednesday 13:52
modified: 2023-03-10-Friday 23:15
tags: 
---

# Deep Q-learning with Space Invaders

## Metadata

Author: [[Thomas Simonini]]
Full Title: Deep Q-Learning With Space Invaders
Category: #readwise/articles
URL: https://huggingface.co/blog/deep-rl-dqn
Date Highlighted: [[2023-02-01-Wednesday]]

[Hands-on Colab](https://colab.research.google.com/drive/1y9its0YnoWIrxQodmZF9qV6ClTbIoEHx?usp=sharing)

## Highlights
- Instead of using a Q-table, Deep Q-Learning uses a Neural Network that takes a state and approximates Q-values for each action based on that state. ([View Highlight](https://read.readwise.io/read/01gr7denrbwajpvn11sy3rq2ps))
- architecture of our Deep Q-Learning network:
	![[courses/huggingface-deeprl/attachments/Pasted image 20230201135544.png]]

- ![](https://huggingface.co/blog/assets/78_deep_rl_dqn/preprocessing.jpg)
  Why do we stack four frames together? We stack frames together because it helps us **handle the problem of temporal limitation**. ([View Highlight](https://read.readwise.io/read/01gr7emqm1da8a0sv9gg8dqsb7))
- the stacked frames are processed by three convolutional layers. These layers **allow us to capture and exploit spatial relationships in images**. But also, because frames are stacked together, **you can exploit some spatial properties across those frames**.
  Finally, we have a couple of fully connected layers that output a Q-value for each possible action at that state. ([View Highlight](https://read.readwise.io/read/01gr7eq65p2x0x89pmxyzqw744))
- Deep Q-Learning training **might suffer from instability**, mainly because of combining a non-linear Q-value function (Neural Network) and bootstrapping (when we update targets with existing estimates and not an actual complete return). ([View Highlight](https://read.readwise.io/read/01gr7etrexme9e9qyx6hns2vq7))
- To help us stabilize the training, we implement three different solutions:
  1. *Experience Replay*, to make more **efficient use of experiences**.
  2. *Fixed Q-Target* **to stabilize the training**.
  3. *Double Deep Q-Learning*, to **handle the problem of the overestimation of Q-values**. ([View Highlight](https://read.readwise.io/read/01gr7ev5285j9kxg3x6fhv79dz))
