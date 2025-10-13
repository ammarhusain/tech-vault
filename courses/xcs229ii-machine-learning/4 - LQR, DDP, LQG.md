---
created: 2022-09-23-Friday 11:33
modified: 2023-03-10-Friday 23:15
---

[[courses/xcs229ii-machine-learning/attachments/LQR_DDP_and_LQG.pdf]]

 [[courses/xcs229ii-machine-learning/attachments/Reinforcement_Learning_and_Control 1.pdf]]

# Finite Horizon Mdps

StateAction rewards: SxA → R

The reward also depends on the action you take in addition to the state you are in.

In the formulation of the lecture the reward depends on the current state and current action but not on the next state you get to.

Finite horizon MDP: 5-state tuple (S, A, P_sa, T, R) : T replaces discount factor gamma.

In finite horizon MDP the optimal policy is a non-stationary policy: this just means that the optimal action will now depend on how much time you have left on the clock. Before it just depended on the what state you are in.

Non-stationary state transitions

For solving finite horizon MDPs, value iteration becomes a dynamic programming algorithm.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923115515.png]]
For the final time step T
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923115524.png|300]]
This basically means that you can forward pass to obtain V_T_star and then keep back tracking to get V_T-1_star etc.. which makes it a dynamic programming algorithm.

# Linear Dynamical Systems

## Linear Quadratic Regulation (LQR)

It applies to only a few set of problems but is a great algorithm so use it whenever it applies.
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923115552.png]]
Two main assumptions of LQR:

- State transitions are a linear function of state and actions.
- Rewards (or costs) are a quadratic function of states and actions.

How do you get the matrices A & B for the state transitions? Different ways:

- Learn it
- Linearize a non-linear model
