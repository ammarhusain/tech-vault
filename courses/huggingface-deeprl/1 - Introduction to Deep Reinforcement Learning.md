---
created: 2022-10-18-Tuesday 03:55
modified: 2023-03-10-Friday 23:15
---

[An Introduction to Deep Reinforcement Learning](https://huggingface.co/blog/deep-rl-intro)

[Exercise Colab](https://colab.research.google.com/drive/1Pqld3Hv2q0_Yh6HutEyVnAUIMVV6Jh96?authuser=1#scrollTo=xcQYx9ynaFMD)

[Quiz](https://github.com/huggingface/deep-rl-class/blob/main/unit1/quiz.md)

# Framework
- idea behind Reinforcement Learning is that an agent (an AI) will learn from the environment by interacting with it (through trial and error) and receiving rewards (negative or positive) as feedback for performing actions.

![[courses/huggingface-deeprl/attachments/Pasted image 20221018163803.png|400]]

- RL is based on the reward hypothesis, which is that all goals can be described as the maximization of the expected return (expected cumulative reward).
- Markov Property implies that our agent needs only the current state to decide what action to take and not the history of all the states and actions they took before.

# Observation Space

![[courses/huggingface-deeprl/attachments/Pasted image 20221018164232.png|500]]

# Action Space
- Action space is the set of all possible actions in an environment. The actions can come from a discrete or continuous space:
![[courses/huggingface-deeprl/attachments/Pasted image 20221018164316.png|500]]

# Reward Space

Our discounted cumulative expected rewards is:
![[courses/huggingface-deeprl/attachments/Pasted image 20221018164754.png|500]]

# Task
- A task is an instance of a Reinforcement Learning problem. We can have two types of tasks: episodic and continuing.
- **Episodic task** : In this case, we have a starting point and an ending point (a terminal state). This creates an episode: a list of States, Actions, Rewards, and new States. For instance, think about Super Mario Bros
- **Continuing task** : These are tasks that continue forever (no terminal state). In this case, the agent must learn how to choose the best actions and simultaneously interact with the environment. For instance, an agent that does automated stock trading.
![[courses/huggingface-deeprl/attachments/Pasted image 20221018165109.png|500]]

# Exploration / Exploitation

**- Exploration/exploitation trade-off.**

- Exploration is exploring the environment by trying random actions in order to find more information about the environment.
- Exploitation is exploiting known information to maximize the reward.
![[courses/huggingface-deeprl/attachments/Pasted image 20221018165246.png|500]]

# Policy
  - The Policy π is the brain of our Agent, it’s the function that tell us what action to take given the state we are. So it defines the agent’s behavior at a given time.
  - There are two approaches to train our agent to find this optimal policy π\*:
  -       Directly, by teaching the agent to learn which action to take, given the state is in: Policy-Based Methods. 
  -       Indirectly, teach the agent to learn which state is more valuable and then take the action that leads to the more valuable states: Value-Based Methods.

![[courses/huggingface-deeprl/attachments/Pasted image 20221018165833.png|400]]

## Policy Based Methods
- In Policy-Based Methods, we learn a policy function directly. This function will map from each state to the best corresponding action at that state. Or a probability distribution over the set of possible actions at that state.
-       **Deterministic**: a policy at a given state will always return the same action. 
-       **Stochastic**: output a probability distribution over actions.

![[courses/huggingface-deeprl/attachments/Pasted image 20221018170338.png|500]]![[courses/huggingface-deeprl/attachments/Pasted image 20221018170403.png|500]]

## Value Based Methods
- In Value-based methods, instead of training a policy function, we train a value function that maps a state to the expected value of being at that state.
- The value of a state is the expected discounted return the agent can get if it starts in that state, and then act according to our policy.
![[courses/huggingface-deeprl/attachments/Pasted image 20221018170640.png|500]]

# "DEEP" In Deep Reinforcement Learning

![[courses/huggingface-deeprl/attachments/Pasted image 20221018171242.png|500]]

## Additional Readings 📚
- [Reinforcement Learning: An Introduction, Richard Sutton and Andrew G. Barto Chapter 1, 2 and 3](http://incompleteideas.net/book/RLbook2020.pdf)
- [Foundations of Deep RL Series, L1 MDPs, Exact Solution Methods, Max-ent RL by Pieter Abbeel](https://youtu.be/2GwBez0D20A)
- [Spinning Up RL by OpenAI Part 1: Key concepts of RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
- [Getting Started With OpenAI Gym: The Basic Building Blocks](https://blog.paperspace.com/getting-started-with-openai-gym/)
- [Lunar Lander - Gym Documentation](https://www.gymlibrary.dev/environments/box2d/lunar_lander/)
