---
aliases: []
created: 2023-02-03-Friday 09:36
modified: 2023-03-10-Friday 23:15
tags: 
---

# Policy Gradient with Pytorch

![rw-book-cover](https://huggingface.co/blog/assets/85_policy_gradient/thumbnail.gif)

## Metadata

Author: [[Thomas Simonini]]
Full Title: Policy Gradient With PyTorch
Category: #readwise/articles
URL: https://huggingface.co/blog/deep-rl-pg
Date Highlighted: [[2023-02-03-Friday]]

[Colab link](https://colab.research.google.com/drive/1zBuOM2LaxoxgGaqeqjTxDDVSYw2YQFl1?usp=sharing)

## Highlights
- policy is a function that **given a state, outputs, a distribution over actions** (in our case using a stochastic policy).
  ![Stochastic Policy](https://huggingface.co/blog/assets/63_deep_rl_intro/pbm_2.jpg)
  Our goal with Policy-Gradients is to control the probability distribution of actions by tuning the policy such that **good actions (that maximize the return) are sampled more frequently in the future.** ([View Highlight](https://read.readwise.io/read/01grc5kvwz37kkxspthqz6gk2j))

## New Highlights: [[2023-02-03-Friday]] at 10:31 Am
- There are multiple advantages over Deep Q-Learning methods. Let's see some of them:
  1. The simplicity of the integration: **we can estimate the policy directly without storing additional data (action values).**
  2. Policy gradient methods can **learn a stochastic policy while value functions can't**.
  This has two consequences:
  a. We **don't need to implement an exploration/exploitation trade-off by hand**. Since we output a probability distribution over actions, the agent explores **the state space without always taking the same trajectory.**
  b. We also get rid of the problem of **perceptual aliasing**. Perceptual aliasing is when two states seem (or are) the same but need different actions. ([View Highlight](https://read.readwise.io/read/01grc5ysbvphn7qvv38dxdmv30))

- Policy gradients are **more effective in high-dimensional action spaces and continuous actions spaces** ([View Highlight](https://read.readwise.io/read/01grc61w8v6vpep7gw8y1aq4kp))
- the problem with Deep Q-learning is that their **predictions assign a score (maximum expected future reward) for each possible action**, at each time step, given the current state.
  But what if we have an infinite possibility of actions?
  For instance, with a self-driving car, at each state, you can have a (near) infinite choice of actions ... We'll need to output a Q-value for each possible action! And taking the max action of a continuous output is an optimization problem itself!
  Instead, with a policy gradient, we output a **probability distribution over actions.**
- Reinforce, also called Monte-Carlo Policy Gradient, **uses an estimated return from an entire episode to update the policy parameter** θ\thetaθ. ([View Highlight](https://read.readwise.io/read/01grc6ayqjwm6raa4246m9x8fz))
- The Policy Gradient algorithm (simplified) looks like this:
  ![](https://huggingface.co/blog/assets/85_policy_gradient/pg_bigpicture.jpg) ([View Highlight](https://read.readwise.io/read/01grc8vpk36ykqkr91wwngww9x))
- optimal stochastic policy will randomly move left or right in grey states. Consequently, **it will not be stuck and will reach the goal state with a high probability**.
  ![](https://huggingface.co/blog/assets/85_policy_gradient/hamster3.jpg) ([View Highlight](https://read.readwise.io/read/01grc8xhnxw9nxvnxx5mt0gm9y))
	 - Note: an example of perceptual aliasing where a policy gradient can output a 50/50 probability to go left or right in the red block. I guess you could bake that in to value based methods too by sampling from the output Q-values on what actions to take next (look at figure in unit 3 on deep Q-learning)
- We have our policy π which has a parameter θ. This π, given a state, **outputs a probability distribution of actions**.
  ![](https://huggingface.co/blog/assets/85_policy_gradient/policy.jpg)
  Where πθ​(at​∣st​) is the probability of the agent selecting action at from state st, given our policy. ([View Highlight](https://read.readwise.io/read/01grc90awnczcb6ctdgqyp0fjw))
- **But how do we know if our policy is good?** We need to have a way to measure it. To know that we define a score/objective function called J(θ).
  The score function J is the expected return:
  ![](https://huggingface.co/blog/assets/85_policy_gradient/objective.jpg)
  Remember that policy gradient can be seen as an optimization problem. So we must find the best parameters (θ) to maximize the score function, J(θ). ([View Highlight](https://read.readwise.io/read/01grc8zqec351w1hncfsqqgsxc))
