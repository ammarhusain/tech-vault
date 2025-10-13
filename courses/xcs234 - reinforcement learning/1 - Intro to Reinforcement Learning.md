---
aliases: []
created: 2022-08-08-Monday 08:27
modified: 2023-03-10-Friday 23:15
tags: 
---


---

Slides - [[courses/xcs234 - reinforcement learning/attachments/Mod1_Slides.pdf]]

Agents need to make good sequences of decisions

Fundamental challenge in AI &ML is learning to make good decisions under uncertainty

RL involves: Optimization; Delayed consequences; Exploration & Generalization

**Optimization**: Explicit notion of utility of decisions

**Delayed consequences**: Decisions now can impact things much later.

- When planning: decisions involve reasoning not only immediate benefit but also long term ramifications
- When learning: temporal credit assignment is hard

**Exploration**: Learning about the world by making decisions

- Censored data - only get reward for decision made. Dont know what would have happened if red pill chosen instead of blue pill

**Generalization:** Policy is mapping from past experience to action. It should generalize to a wide set of experiences

# Intro to Sequential Decision Making

![[courses/xcs234 - reinforcement learning/attachments/Untitled.png]]

Markov assumption: all of history is encoded in the current state. Future is independent of past given present. In practice we often assume most recent observation is sufficient statistic of history: s_t = o_t

State representation has big implications for:

- Computational complexity
- Data required
- Resulting performance

RL algorithm components: Model, Policy & Value Function![[courses/xcs234 - reinforcement learning/attachments/Untitled 1.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 2.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 3.png]]

![[courses/xcs234 - reinforcement learning/attachments/Untitled 4.png]]

Types of RL Agents:

- Model based
	 - Explicit: Model (dynamics and reward).
	 - May or may not have policy and/or value function
- Model-free
	 - Explicit: Value function and/or policy function
	 - No model

Evaluation: Estimate / predict the expected rewards from following a given policy

Control: Optimization - find the best policy
