---
aliases: []
created: 2023-02-07-Tuesday 17:35
modified: 2023-03-10-Friday 23:15
tags: 
---
# Proximal Policy Optimization

![rw-book-cover](https://huggingface.co/blog/assets/93_deep_rl_ppo/thumbnail.png)

## Metadata

Author: [[Thomas Simonini]]
Full Title: Proximal Policy Optimization
Category: #readwise/articles
URL: https://huggingface.co/blog/deep-rl-ppo
Date Highlighted: [[2023-02-08-Wednesday]]

Colab [link](https://colab.research.google.com/drive/1lk1nEU_T9OZMs9U4fXADNYQF8lCpTWQ3?authuser=1#scrollTo=oDkUufewmq6v)

## Highlights
- idea with Proximal Policy Optimization (PPO) is that we want to improve the training stability of the policy by limiting the change you make to the policy at each training epoch: **we want to avoid having too large policy updates.** ([View Highlight](https://read.readwise.io/read/01grq7wm2j6thxd9z5129k6y63))
- ![](https://huggingface.co/blog/assets/93_deep_rl_ppo/cliff.jpg)
  Taking smaller policy updates improve the training stability ([View Highlight](https://read.readwise.io/read/01grq8n55j70d3td072gznyqb1))
- **with PPO, we update the policy conservatively**. To do so, we need to measure how much the current policy changed compared to the former one using a ratio calculation between the current and former policy. And we clip this ratio in a range [1−ϵ,1+ϵ], meaning that we **remove the incentive for the current policy to go too far from the old one (hence the proximal policy term).** ([View Highlight](https://read.readwise.io/read/01grq8nh54bny8d3tmbn1j30ar))
- *Clipped surrogate objective function* that **will constrain the policy change in a small range using a clip.**
  This new function **is designed to avoid destructive large weights updates** :
  ![](https://huggingface.co/blog/assets/93_deep_rl_ppo/ppo-surrogate.jpg)
  Let’s study each part to understand how it works.
  ![](https://huggingface.co/blog/assets/93_deep_rl_ppo/ratio1.jpg)
  This ratio is calculated this way:
  ![](https://huggingface.co/blog/assets/93_deep_rl_ppo/ratio2.jpg)
  As we can see, rt​(θ) denotes the probability ratio between the current and old policy:
  So this probability ratio is an **easy way to estimate the divergence between old and current policy.** ([View Highlight](https://read.readwise.io/read/01grq8rjwpr446mmwzv465eg0f))
- **By clipping the ratio, we ensure that we do not have a too large policy update because the current policy can't be too different from the older one.**
  To do that, we have two solutions:
  - *TRPO (Trust Region Policy Optimization)* uses KL divergence constraints outside the objective function to constrain the policy update. But this method **is complicated to implement and takes more computation time.**
  - *PPO* clip probability ratio directly in the objective function with its **Clipped surrogate objective function.** ([View Highlight](https://read.readwise.io/read/01grq8yn411wyyhqxmvagxet1r))
