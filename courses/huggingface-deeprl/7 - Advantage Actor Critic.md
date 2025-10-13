---
aliases: []
created: 2023-02-03-Friday 12:09
modified: 2023-03-10-Friday 23:15
tags: 
---
# Advantage Actor Critic

![rw-book-cover|450](https://huggingface.co/blog/assets/89_deep_rl_a2c/thumbnail.gif)

## Metadata

Author: [[Thomas Simonini]]
Full Title: Advantage Actor Critic
Category: #readwise/articles
URL: https://huggingface.co/blog/deep-rl-a2c
Date Highlighted: [[2023-02-03-Friday]]

Colab [link](https://colab.research.google.com/drive/1CDYLAq1_8loc-eRJH_av4a5nVKvD1ut9?authuser=1#scrollTo=4JmEVU6z1ZA-)

## Highlights
- We saw that Reinforce worked well. However, because we use Monte-Carlo sampling to estimate return (we use an entire episode to calculate the return), **we have significant variance in policy gradient estimation**. ([View Highlight](https://read.readwise.io/read/01grce6372yvr6h7q9dzn0wej2))
- Today we'll study **Actor-Critic methods**, a hybrid architecture combining a value-based and policy-based methods that help to stabilize the training by reducing the variance:
  - *An Actor* that controls **how our agent behaves** (policy-based method)
  - *A Critic* that measures **how good the action taken is** (value-based method) ([View Highlight](https://read.readwise.io/read/01grce6dtvw4wwqq98swwbm6eh))
- R(τ) is calculated using a *Monte-Carlo sampling*. Indeed, we collect a trajectory and calculate the discounted return, **and use this score to increase or decrease the probability of every action taken in that trajectory**. If the return is good, all actions will be “reinforced” by increasing their likelihood of being taken. R(τ)=Rt+1​+γRt+2​+γ2Rt+3​+...
  The advantage of this method is that **it’s unbiased. Since we’re not estimating the return**, we use only the true return we obtain.
  But the problem is that **the variance is high, since trajectories can lead to different returns** due to stochasticity of the environment (random events during episode) and stochasticity of the policy. Consequently, the same starting state can lead to very different returns. Because of this, **the return starting at the same state can vary significantly across episodes**.
  ![|175](https://huggingface.co/blog/assets/89_deep_rl_a2c/variance.jpg)
  The solution is to mitigate the variance by **using a large number of trajectories, hoping that the variance introduced in any one trajectory will be reduced in aggregate and provide a "true" estimation of the return.** ([View Highlight](https://read.readwise.io/read/01grce75e7974b58ddbnyxnyh3))
- idea behind Actor-Critic. We learn two function approximations:
  - *A policy* that **controls how our agent acts**: πθ​(s,a)
  - *A value function* to assist the policy update by measuring how good the action taken is: ​w​(s,a) ([View Highlight](https://read.readwise.io/read/01grce7yrk8v15v575ph5z99c5))
- Let's see the training process to understand how Actor and Critic are optimized:
  - At each timestep, t, we get the current state St​ from the environment and **pass it as input through our Actor and Critic**.
  ![|175](https://huggingface.co/blog/assets/89_deep_rl_a2c/step1.jpg)
  - The Critic takes that action also as input and, using St​ and At​, **computes the value of taking that action at that state: the Q-value**.
  ![|175](https://huggingface.co/blog/assets/89_deep_rl_a2c/step2.jpg)
  ![|175](https://huggingface.co/blog/assets/89_deep_rl_a2c/step3.jpg)
  - The Actor updates its policy parameters using the Q value.
  ![|175](https://huggingface.co/blog/assets/89_deep_rl_a2c/step4.jpg)
  - Thanks to its updated parameters, the Actor produces the next action to take at At+1​ given the new state St+1​.
  - The Critic then updates its value parameters. ([View Highlight](https://read.readwise.io/read/01grce0xwbgb6evkdhw36m3s7w))
- We can stabilize learning further by **using the Advantage function as Critic instead of the Action value function**.
  The idea is that the Advantage function calculates **how better taking that action at a state is compared to the average value of the state**. It’s subtracting the mean value of the state from the state action pair:
  ![|450](https://huggingface.co/blog/assets/89_deep_rl_a2c/advantage1.jpg)
  In other words, this function calculates **the extra reward we get if we take this action at that state compared to the mean reward we get at that state**. ([View Highlight](https://read.readwise.io/read/01grce94rfqw7hkvqjv8zf1svm))
- The problem with implementing this advantage function is that it requires two value functions — Q(s,a) and V(s). Fortunately, **we can use the TD error as a good estimator of the advantage function.**
  ![|450](https://huggingface.co/blog/assets/89_deep_rl_a2c/advantage2.jpg)
  Now that you've studied the theory behind Advantage Actor Critic (A2C), **you're ready to train your A2C agent** using Stable-Baselines3 in robotic environments. ([View Highlight](https://read.readwise.io/read/01grcea1rbh2599pz6s0s5hn9g))
