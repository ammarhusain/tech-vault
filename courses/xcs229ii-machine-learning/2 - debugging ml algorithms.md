---
created: 2022-09-23-Friday 09:27
modified: 2023-03-10-Friday 23:15
---

Related: [[neural network debugging]]

[[courses/xcs229ii-machine-learning/attachments/ML-advice-slides.pdf]]
ML algorithms almost never work the first time around. A lot of [[machine-learning]] is about knowing how to debug in a principled way.

# Debugging Ml Algorithms

Common things people end up trying:

- Try getting more training examples.
- Try a smaller set of features.
- Try a larger set of features.
- Try changing the features: Email header vs. email body features.
- Run gradient descent for more iterations.
- Try Newton’s method.
- Use a different value for lambda
- Try using an SVM

Andrew Ng recommends doing a Bias-Variance tradeoff analysis
Remember a high bias model most likely underfits while a high-variance model most likely overfits on training data while might not do well on test set.

![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923092940.png]]

High bias problem
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923092956.png]]
![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923093004.png]]

Common questions to ask:

- Is the algorithm converging?
- Are you optimizing the right function?

Bias and variance are the single most powerful tool to analyse ML algorithms. Andrew Ng does it on every application.

# Debugging Rl Algorithms

![[courses/xcs229ii-machine-learning/attachments/Pasted image 20220923093034.png]]

- If theta_RL flies well in simulation, but not in real life then the problem is in the simulator.
- Let theta_human be the human control policy. If J(theta_human) < J(theta_RL), then the problem is in the reinforcement learning algorithm. (It is failing to minimize the cost function J)
- If J(theta_human) > J(theta_RL) then the problem is in the cost function (maximizes it does not correspond to good autonomous flight)

In reality you keep shifting between these because once one of them becomes good enough the other one degrades.

# Error Analysis Tools

Error analysis tries to explain the difference between current performance and perfect performance.
Ablative analysis tries to explain the difference between some baseline (much poorer) performance and current performance.

# Projects
- Start with something quick and dirty. Do something simple and get results rather than building some very complicated algorithm. Do error analysis and get some results.
- Build it up step by step and test along the way. Same way you shouldn't just write 10k lines of code and then compile, figure out how you can compile & test incrementally.
- Start with logistic regression or Naive Bayes ... not a neural network.
