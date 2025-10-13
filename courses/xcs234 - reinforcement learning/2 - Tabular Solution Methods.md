---
created: 2022-08-10-Wednesday 08:28
modified: 2023-03-10-Friday 23:15
publish: true
---

Slides - [[courses/xcs234 - reinforcement learning/attachments/Mod2_Slides.pdf]]

---

# 2.1 Markon Decision Process Planning

## Policy Evaluation

![[courses/xcs234 - reinforcement learning/attachments/Untitled 23.png]]

**Model**: Mathematical models of dynamics & reward (transition)

**Policy**: Function mapping agent’s states to actions

**Value function**: future rewards from being in a state and/or action when following a particular policy

![[courses/xcs234 - reinforcement learning/attachments/Untitled 1 1.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 2 1.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 3 1.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 4 1.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 5.png]]
Can solve for a Markov Reward Process in 2 ways:

- closed form (by a matrix inversion)
- Iterative algorithm (dynamic programming)

![[courses/xcs234 - reinforcement learning/attachments/Untitled 6.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 7.png]]
MDP = MRP + actions

![[courses/xcs234 - reinforcement learning/attachments/Untitled 8.png]]
Policy specifies what action to take in each state: can be deterministic or stochastic

For generality, consider policy as a conditional distribution - given a state specifies a distribution over actions

![[courses/xcs234 - reinforcement learning/attachments/Untitled 9.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 10.png]]

---

## Policy Iteration

![[courses/xcs234 - reinforcement learning/attachments/Untitled 11.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 12.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 13.png]]

New definition of State-Action Value Q: Value functions are conditioned only on the state while Q functions are conditioned on state & action pair

There is a bunch of math proof that this actually improves the policy by making the value estimates better (I skipped that here)

Policy search is just enumerating all possible policies given the finite number of states and actions (tabular case) and walking through them all to compute the value function.

---

## Value Iteration

Similar to the Policy evaluation dynamic programming algorithm. Need to be able to compute an argmax over all actions - Bellman backup operator. I think this works well when the action space is discrete.

A bunch of theory around the Bellman Backup Operator

![[courses/xcs234 - reinforcement learning/attachments/Untitled 14.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 15.png]]

Policy evaluation amounts to computing the fixed point of B (bellman backup operator)

## Bellman Contraction Operator & Finite Horizon Problems

A bunch of proof that bellman operator is a contraction operator, aka minimizes distance between value functions.

Finite Horizon H : means your policy only gets H timesteps/decisions to make

Infinite Horizon : policy can keep going forever

For finite horizon problems the optimal policy is not necessarily stationary (independent of timestep)

- Value iteration:
	 - Compute optimal value for horizon = k
		  - Note this can be used to compute optimal policy if horizon = k
	 - Increment k
- Policy iteration
	 - Compute infinite horizon value of a policy
	 - Use to select another (better) policy
	 - Closely related to a very popular method in RL: policy gradient

## 2.2 Model-free Policy Evaluation

### Refresh Your Understanding

![[courses/xcs234 - reinforcement learning/attachments/Untitled 16.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 17.png]]

### Monte Carlo Policy Evaluation
- Estimating the expected return of a particular policy if don’t have access to true MDP models (expected discounted sum of rewards)
- Monte Carlo policy evaluation
	 - Policy evaluation when don’t have a model of how the world work
		  - Given on-policy samples
- Temporal Difference (TD)
- Certainty Equivalence with dynamic programming
- Metrics to evaluate and compare algorithms
![[courses/xcs234 - reinforcement learning/attachments/Untitled 18.png]]
- If trajectories are all finite, sample set of trajectories & average returns
- Does not require MDP dynamics/rewards
- Does not assume state is Markov
- Can only be applied to episodic MDPs
	 - Averaging over returns from a complete episode
	 - Requires each episode to terminate
- Generally high variance estimator
	 - Reducing variance can require a lot of data
	 - In cases where data is very hard or expensive to acquire, or the stakes are high, MC may be impractical
- Requires episodic settings
	 - Episode must end before data from episode can be used to update V

### Temporal Difference Learning
- TD Learning is one of the most central & novel ideas in RL - Sutton & Barto
- Combination of Monte Carlo & dynamic programming methods
- Model free
- Bootstraps and samples value function
- Can be used in episodic or infinite-horizon non-episodic settings
- Immediately updates estimate of V after each (s, a, r, s’) tuple
- Key insight: You can update the value function of the current state by taking an action and looking at the value of the next state you end up in.
	 - This does not require the agent to finish the entire episode before getting any value estimate.
		  - I.e dont need to compute G as the discounted sum of reward first before updating value

![[courses/xcs234 - reinforcement learning/attachments/Untitled 19.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 20.png]]

---

## 2.3 Model-based Policy Evaluation

### Dynamic Programming with Uncertainty Equivalence

![[courses/xcs234 - reinforcement learning/attachments/Untitled 21.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 22.png]]

## 2.4 Policy Evaluation Algorithm Comparison

### Comparing Algorithms for Policy Evaluations

TODO

## 2.5 Model-free Control

### Generalized Policy Iteration and E-greedy

### Mc Control with E-greedy Policies (TABULAR)

### Td Methods, Sarsa & Q-learning

SARSA is on policy vs Q-learning is off policy

Off policy enables us to mine from all possible experiences and decisions to create an optimal policy.

SARSA & Q-learning are pretty much the same. In Q-learning you just pick the action with the max Q rather than a according to the policy. Therefore you just need a (s,a,r,s’) tuple rather than a (s,a,r,s’,a’)

### Maximization Bias

We may overestimate Q-values

Double Q-learning: use two Q functions one for picking best action a (for control) and the other for evaluating the value of that action (for evaluation)
