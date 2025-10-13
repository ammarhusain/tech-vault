---
created: 2022-09-01-Thursday 11:16
modified: 2023-03-10-Friday 23:15
---

[[courses/xcs234 - reinforcement learning/attachments/Mod5_Slides.pdf]]

# 5.1 Introduction to Multi-armed Bandits

**Refresh you understanding**

- Policy Gradeints do gradient ascent on the value function.
- In tabular MDPs the number of deterministic policies is smaller than the number of value functions.
- Policy gradient algorithms are not very robust to step size choice.
- Baselines are only functions of state

Bandits: Like MDPs, make a single decision and then the world resets
Settings: Bandits (single decisions), MDPs
Frameworks: evaluation criteria for formally assessing the quality of a [[reinforcement learning|RL]] algorithm
Approaches: Classes of algorithms for achieving particular evaluation criteria in a certain set

Multi-armed bandit : Single state & multiple actions MDP, It is a tuple of $(A, R)$
	$A$ : known set of m actions (arms)
	$R^a(r) = P[r|a]$ is an unknown probability distribution over rewards (big challenge that we dont know)
	At each step t the agent selects an action $a_t \in A$
	The environment generates a reward $r_t \approx R^{a_t}$
	Goal: Maximize cumulative reward $\sum_{\tau=1}^t r_{\tau}$

## Evaluating Rl Algorithms

So far: computational complexity, convergence, convergence to a fixed point, & empirical performance
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220908140726.png|500]]

Informally an algorithm has linear regret if it takes a non-optimal action a constant fraction of the time
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220908142249.png|500]]
Types of regret bounds:
	Problem independent: Bound how regret grows as a function of T, the total number of time steps the algorithm operates for
	Problem dependent: Bound regret as a function of the number of times we pull each arm and the gap between the reward for the pulled arm a∗

## Optimism under Uncertainty

Choose actions that that might have a high value
Two outcomes:
	Getting high reward: if the arm really has a high mean reward
	Learn something: if the arm really has a lower mean reward, pulling it will (in expectation) reduce its average reward and the uncertainty over its value
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220908143304.png|500]]
We want to get the true action value $Q(a)$ as close as possible to the upper confidence bound $U_t(a)$ for that action. Hoeffdings Inequality allows you to compute that : estimate a bound on the true mean given several samples that compute the empirical mean.

This leads to the UCB1 algorithm $at = arg max_{a∈A} [Qˆ(a) + \sqrt {\frac{2 log t}{N_t(a)}}]$
Multi-armed bandits are a subcase of MDPs. Simpler settings to evaluate ideas around exploration. It makes the problem easier because we are only looking at sets of actions at a time to evaluate which set of actions is the best to take at this time. In MDPs conversely we are looking at sequential decision making, so evaluating after every state-action

## Bayesian Bandits

So far we have made no assumptions about the reward distribution R
	Except bounds on rewards
Bayesian bandits exploit prior knowledge of rewards, p[R]
They compute posterior distribution of rewards p[R | ht ], where $ht = (a_1,r_1, . . . , a_{t−1},r_{t−1})$
Use posterior to guide exploration
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220909101836.png]]

## Thompson Sampling

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220909150154.png]]

# Fast Rl in Mdps

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220909155753.png]]
Montezumas revenge is a particularly challenging game because the credit assignment problem is difficult. Aka the reward is received much much later after taking an action

**Model-Based Interval Estimation with Exploration Bonus (MBIE-EB)**
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220909160537.png]]
Dirichlet distribution is for multinomials just like bernoulli distribution is for binomials (0 or 1)
PAC based algorithms - Probably approximately correct

## From Assignment 4

Contextual multi armed bandits basically means that the learner sees a feature vector or "context" for each arm, timestep.
