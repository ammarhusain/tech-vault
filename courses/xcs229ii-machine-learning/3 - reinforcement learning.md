---
aliases: []
created: 2022-09-23-Friday 11:13
modified: 2023-03-10-Friday 23:15
tags: 
---


---

[[courses/xcs229ii-machine-learning/attachments/Reinforcement_Learning_and_Control 1.pdf]]

# Rl Intro

**Credit assignment problem**: When your algorithm gets a reward (positive or negative), how do you figure out what action you did or what you did poorly in the sequence of actions that caused you to get that reward.

When we develop algorithm we'll see how these algorithms will have to at least indirectly solve the credit assignment problem.

RL algorithms are modeled using the Markov Decision Process (MDP) formalism. It is a 5-tuple {States, Actions, Transition Probabilities P(s,a), Discount, Reward}

The goal of RL algorithms is to choose actions over time to maximize the expected total payoff. What most RL algorithms will come up with is a policy that maps states to actions.

**Simple Tabular MDP**
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111817.png]]
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111828.png]]
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111834.png]]

For finite state MDPs you can iteratively solve it in closed form. For example create a tabular representation as below.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111855.png]]
This is all pretty much like Dynamic Programming (solving Bellman Equation recursively)

# Value Function

Define: V_pi, V_star, Pi_star

- **V_pi** : Value function for policy *pi*

Maps States → Rewards, for a policy pi such that V_pi(s) is the expected total payoff for starting in state s and executing policy pi
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111916.png]]
**Bellman's Equation**
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111939.png]]
Action 'a' is drawn from some policy pi(s)

Bellman's Equation gives you a linear system of equations for a given policy pi to solve for. The number of equations (or the number of unknowns) equal the number of states.

- **V_star** : Optimal value function

For all possible policies pi, this is the most optimal value function.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923111958.png]]
We can augment the Bellman's equation above to solve this by:
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112017.png]]
Pi_star : Optimal policy
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112029.png]]

One strategy to obtain Pi_star:

1. Obtain V_star
2. Use argmax on actions to get Pi_star

# Value and Policy Iteration

For value iteration you could do synchronous or asynchronous updates: though synchronous updates are more common since they vectorize better.

Bellman backup operator: Use old estimate to compute new estimate. Ultimately it will converge and the estimate won't change.

There are some versions of value iteration that applies to continuous states as well.

In value iteration we wait and compute all the optimal values before figuring out the optimal policy.

In policy iteration we come up with a new policy on every iteration.

Value iteration is used a lot more in practice. You can use policy iteration if you have a small problem (it might converge a bit faster for those).

# Learning a Model for an Mdp

![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112058.png]]

A common algorithm to solve this would be to put together model learning followed by value iteration:

```jsx
Initialize policy Pi randomly ... then repeat till convergence:
	- Execute Pi in the MDP for some number of trials
	- Using the accumulated experience in the MDP, update our estimates for Transistion Probabilities (P_sa) and Rewards if applicable.
	- Apply value iteration with the estimated state transition probabilities and rewards to get a new estimated value function V.
	- Update Pi to be the greedy policy with respect to V
```

**Exploration vs Exploitation** :

- epsilon greedy algorithm (uniformly sample a random state with probability epsilon)
- Boltzmann exploration (bias your sampling of random states where you think the chance of rewards is higher)

Intrinsic Motivation: rewards the RL algorithm for reaching states it hadn't visited before (finding new things about the world)

## Models and Simulation

It is upto you the engineer to figure out and model the state space of the problem: [x, y, theta ...]

**Inverted Pendulum problem**
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112149.png]]
Curse of dimensionality: If you have a state space s in R^n and you discretize it into k buckets, you will end up with k^n discrete states. This will soon make the problem intractably hard to solve.

General rule of thumb: Discretization will work fine with 2-4 dimensional state spaces. With 4-6 dimenstional you can make it work by putting some effort into it, such as unevenly discretize based on what state (or range) is more important. Probably best not to bother with discretization for state spaces larger than 6.

**Fitted Value Iteration**

Tries to approximate V_star directly without resorting to discretization. It is used for working with MDPs that have an continuous valued state-space (actions are assumed discretized still)

Once we have the value function V_star we already know how to extract the best actions for policy Pi_star.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112224.png|300]]
In Fitted Value iteration we will try and learn a similar linear model for the value as a function of the states of the system.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112250.png|300]]
First we need to find the **model**:

One way to get model is using some physics simulator

Second way is to learn from data

Have a human operator fly the robot around P times to learn a model of the state transition probabilities.

![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112407.png]]

Apply supervised learning to estimate:
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112424.png|600]]
You now have two options: either use this model directly (deterministic) or add a bit off noise when sampling the next state from the model (stochastic).
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112454.png]]
This is called model-based RL. It is more common in robotics based application.

Model-free RL works better when playing video games (or chess or GO etc)

There is an interesting area of evolving research around a combination of model-based and model-free RL.

If you want your model to work on a real physical robot (not just in a simulator) always use the stochastic model, aka add random noise while sampling the next state.

Now that you have built a model of your robot or used a simulator, how do you apply fitted value iteration?

Figure out a bunch of features (Phi) of the state s that you can use to learn the value function.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112516.png]]
Good thing with model-based RL is that you can generate a lot of data using the learned model or the simulator to learn the parameters theta of the linear regression model of the value function.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112543.png]]
Learn this mapping and then constantly keep updating (similar to how we were doing it in the tabular case).
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112629.png]]
The assumption with these fitted value iteration algorithms is that the action is discretized. However you could even learn to quickly optimize a function (equivalent to doing argmax for discrete values) that spits out an action in continuous space. This is called Model Predictive Control (MPC).

When running the algorithm you remove the stochasticity of the model (by setting epsilon noise to 0) and deterministically sample the next state. It is generally not good to have a random number generator in the inner loop during inference time. Your value function must be robust given the noise added during training. This also makes the algorithm running a lot faster (real time) because you don't have to sample a whole bunch of states and then average over them during run time.

## Debugging Rl Algorithms

![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112648.png]]

## Policy search Algorithms

Goal is to find a good policy directly rather than finding a value function first and then doing an arg-max for the action.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112712.png]]

Let us assume that we train a logistic regression model that learns a model theta that maps states to actions.

In direct policy search we will use a "stochastic policy": A function PI:SxA → R where PI(s) is the probability of taking action a in state s.

In simple words the policy samples an action from some probability distribution function which is the policy.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112731.png]]
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923112740.png]]
Note: In direct policy search start state s_0 is a fixed state. It is either known or we have some initial state distribution. Compare this to value iteration where we are agnostic to start state.

**REINFORCE Algorithm**
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923113157.png]]
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923113202.png]]
This is a stochatic gradient ascent algorithm ^^

REINFORCE algorithm is pretty inefficient. The gradient updates are on expectation maximize the reward function but they have high variance. So you need to run many iterations with a low learning rate for it to converge.

Direct policy search would work better for 2 scenarios:

- POMDPs (partially observable MDP)
	 - At every step you only get a partial (and potentially noisy) measurement of the state. Have to choose action "a" using that.
	![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923113222.png]]
	- If Pi_star is simpler than V_star, use direct policy search. In other words if it is a low level control task (needs fast & high update rates) such as controlling a motor etc then policy search would work better. If your task requires higher level reasoning (more complex or multi step reasoning) like playing Chess or Go then value function approximation works better. That is why DeepMind uses DQN.

RL is a sequential decision making process. It is becoming common in robotic applications, controlling large machine, chatbots etc. Also increasingly being used for healthcare, stock trading
