---
created: 2022-10-20-Thursday 00:10
modified: 2023-03-10-Friday 23:15
---

[Exercise colab](https://colab.research.google.com/drive/1WUEQv7ycBnItZraNSqXxLp0Nwc7i11GT?authuser=1#scrollTo=Y-mo_6rXIjRi)

[An Introduction to Q-Learning Part 1](https://huggingface.co/blog/deep-rl-q-part1)
[deep-rl-class/quiz1.md at main · huggingface/deep-rl-class · GitHub](https://github.com/huggingface/deep-rl-class/blob/main/unit2/quiz1.md)

[An Introduction to Q-Learning Part 2/2](https://huggingface.co/blog/deep-rl-q-part2)
[deep-rl-class/quiz2.md at main · huggingface/deep-rl-class · GitHub](https://github.com/huggingface/deep-rl-class/blob/main/unit2/quiz2.md)

# Part 1

two types of value-based functions:

## The State-value Function

For each state, the state-value function outputs the expected return if the agent **starts at that state,** and then follow the policy forever.
![[courses/huggingface-deeprl/attachments/PNG image 1.png]]

## The Action-value Function

action-value function **outputs the expected return** if the agent starts in that state and takes action, and then follows the policy forever after.

![[courses/huggingface-deeprl/attachments/PNG image 2.png]]

The Bellman equation **simplifies our state value or state-action value calculation.**
The idea of the Bellman equation is that instead of calculating each value as the sum of the expected return, **which is a long process.** This is equivalent **to the sum of immediate reward + the discounted value of the state that follows.**

## Monte Carlo Vs Temporal Difference Learning

Monte Carlo and Temporal Difference Learning are two different **strategies on how to train our value function or our policy function.** Both of them **use experience to solve the RL problem.**

On one hand, Monte Carlo uses **an entire episode of experience before learning.** On the other hand, Temporal Difference uses **only a step ( St,At,Rt+1,St+1St​,At​,Rt+1​,St+1​ ) to learn.**

![[courses/huggingface-deeprl/attachments/PNG image 3.png]]

Temporal difference, on the other hand, waits for only one interaction (one step) St+1St+1​- to form a TD target and update V(St)V(St​) using Rt+1Rt+1​ and gamma∗V(St+1)gamma∗V(St+1​).

The idea with **TD is to update the V(St)V(St​) at each step.**

But because we didn't play during an entire episode, we don't have GtGt​ (expected return). Instead, **we estimate GtGt​ by adding Rt+1Rt+1​ and the discounted value of the next state.**

This is called bootstrapping. It's called this **because TD bases its update part on an existing estimate V(St+1)V(St+1​) and not a complete sample GtGt​.**
![[courses/huggingface-deeprl/attachments/PNG image 4.png]]

This method is called TD(0) or **one-step TD (update the value function after any individual step).**

## Part 2
- Q-Learning is an off-policy value-based method that uses a TD approach to train its action-value function.
- If we have an optimal Q-function, we have an optimal policy since we know for each state what is the best action to take.
- Policy is an argmax policy $\pi^\star(s) = \arg\max_a Q^\star(s,a)$
  ![[courses/huggingface-deeprl/attachments/Pasted image 20221026160640.png|500]]
	 - At the beginning of the training, the probability of doing exploration will be huge since ɛ is very high, so most of the time, we'll explore. But as the training goes on, and consequently our Q-Table gets better and better in its estimations, we progressively reduce the epsilon value since we will need less and less exploration and more exploitation.
![[courses/huggingface-deeprl/attachments/Pasted image 20221026162548.png|500]]
-       Off-policy: using a different policy for acting and updating. 
-       On-policy: using the same policy for acting and updating. 
  - For instance, with Sarsa, another value-based algorithm, the Epsilon-Greedy Policy selects the next\_state-action pair, not a greedy policy.
  - Q-learning is off-policy while SARSA in on-policy
![[courses/huggingface-deeprl/attachments/Pasted image 20221027220037.png|500]]

## Additional Readings 📚
- [Reinforcement Learning: An Introduction, Richard Sutton and Andrew G. Barto Chapter 5, 6 and 7](http://incompleteideas.net/book/RLbook2020.pdf)
- [Foundations of Deep RL Series, L2 Deep Q-Learning by Pieter Abbeel](https://youtu.be/Psrhxy88zww)
- To dive deeper on Monte Carlo and Temporal Difference Learning:
	 - [Why do temporal difference (TD) methods have lower variance than Monte Carlo methods?](https://stats.stackexchange.com/questions/355820/why-do-temporal-difference-td-methods-have-lower-variance-than-monte-carlo-met)
	 - [When are Monte Carlo methods preferred over temporal difference ones?](https://stats.stackexchange.com/questions/336974/when-are-monte-carlo-methods-preferred-over-temporal-difference-ones)
