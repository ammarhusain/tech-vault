---
created: 2022-08-23-Tuesday 14:11
modified: 2023-03-10-Friday 23:15
---

- [[courses/xcs234 - reinforcement learning/attachments/Mod4_Slides.pdf]]

# Refresh Your Understanding

Performance difference lemma
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220823143213.png]]
	We do not need data from both policies in order to compute the performance difference - just the immediate actions.

# 4.1 Introduction to Policy search Methods

## Policy search Methods Overview

Works for very large states or action spaces
In the last lecture we approximated the value or action-value function using parameters w,
$V_w(s) \approx V^{pi}(s)$ or $Q_w(s,a) \approx Q^{pi}(s,a)$
A policy was generated directly from the value function e.g. using $\epsilon$-greedy.
In this lecture we will directly parametrize the policy, and will typically use θ to show parameterization:
$\pi_\theta(s,a) = P[a|s;\theta]$
Goal is to find a policy π with the highest value function $V^\pi$. We will focus again on model-free reinforcement learning
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220829153820.png]]
So far have focused on deterministic policies (near deterministic like $\epsilon$-greedy). Now we are thinking about direct policy search in RL, will focus heavily on stochastic policies
Optimal policy for rock-paper-scissors is a stochastic policy. A deterministic policy can be exploited by the opponent.

**Policy optimization**: Policy based reinforcement learning is an optimization problem Find policy parameters θ that maximize $V(s_0, θ)$

# 4.2 Gradient-free Methods

Often a great simple baseline to try
Benefits: Can work with any policy parameterizations, including non-differentiable. Frequently very easy to parallelize
Limitations: Typically not very sample efficient because it ignores temporal structure

## 4.3 Policy Gradient Methods

Greater efficiency often possible using gradient: Gradient descent, Conjugate gradient, Quasi-newton
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830110826.png|500]]

### Finite Difference Methods

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830110934.png|500]]
Is guaranteed to converge to a local optima (not global), does not rely on the Markov assumption, uses a number of evaluations that scales linearly with the policy feature dimension (not state)

### Score Functions and Policy Gradient

We now compute the policy gradient analytically. Assume policy $\pi_\theta$ is differentiable whenever it is non-zero. Assume we can calculate gradient $∇_θπ_θ(s, a)$ analytically. What kinds of policy classes can we do this for?
	- Softmax
	- Gaussian
	- Neural networks
A score function is the derivative of the log of a parameterized probability / likelihood. Example: let p(s; θ) be the probability of state s under parameter θ. Then the score function would be $∇_θ log  p(s; θ)$

#### Softmax Policy

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830113206.png|500]]

#### Gaussian Policy

In continuous action spaces, a Gaussian policy is natural
Mean is a linear combination of state features $µ(s) = φ(s) ^ T θ$.
Variance may be fixed $σ ^2$ , or can also parametrised
Policy is Gaussian $a ∼ N (µ(s), σ^2 )$
The score function is $∇_θ log π_θ(s, a) = (a − µ(s))φ(s) / σ ^2$
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830120042.png|500]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830120434.png|400]] ![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830121214.png|400]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830122009.png|500]]

#### Reinforce

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830134032.png|500]]

#### Policy-based Rl Recap

General formulation : $∇_θV(θ) = E_{π_θ} [∇_θ log π_θ(s, a)Q^{π_θ} (s, a)]$
State-action pairs with higher estimated Q values will increase in probability on average

Policy search : directly parametrize the policy $\pi_\theta(s,a) = P[a|s;\theta]$
Goal is to find a policy $\pi$ with the highest value function $V^\pi$
(Pure) Policy based methods

- No value function
- Learned Policy
Actor-Critic methods
- Learned value function
- Learned Policy

Advantages

- Better convergence properties
- Effective in high-dimenstional or continuous action spaces
- Can learn stochastic policies
Disadvantages
- Typically converge to a local rather than global optimum
- Evaluating a policy is typically inefficient & has high variance

**Desired Properties of a Policy Gradient RL Algorithm**
Goal: Converge as quickly as possible to a local optima - Incurring reward / cost as execute policy, so want to minimize number of iterations / time steps until reach a good policy
During policy search alternating between evaluating policy and changing (improving) policy (just like in policy iteration)
Would like each policy update to be a monotonic improvement
	- Only guaranteed to reach a local optima with gradient descent
	- Monotonic improvement will achieve this
	- And in the real world, monotonic improvement is often beneficial

#### Better Gradient Estimation

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830135721.png|500]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830140627.png|500]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830140649.png|500]]

#### Policy Gradient Algorithms and Reducing variance

Actor-Critic Methods
Estimate of V/Q is done by a critic
Actor-critic methods maintain an explicit representation of policy and the value function, and update both
A3C (Mnih et al. ICML 2016) is a very popular actor-critic method
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830143417.png|500]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830143613.png|500]]
$A^{(1)}_t$ has low variance & high bias. $A^{(∞)}_t$ high variance but low bias.

#### Need for Automatic step Size Tuning

Step size is important in any problem involving finding the optima of a function
Supervised learning: Step too far → next updates will fix it
Reinforcement learning: Step too far → bad policy
	Next batch: collected under bad policy
	 Policy is determining data collection! Essentially controlling exploration and exploitation trade off due to particular policy parameters and the stochasticity of the policy
	 May not be able to recover from a bad choice, collapse in performance!

#### Trpo Algorithms

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830154659.png|500]]
**Common Template of Policy Gradient Algorithms**
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220830155106.png]]
