---
created: 2022-08-10-Wednesday 08:46
modified: 2023-03-10-Friday 23:15
---

# A1

[[courses/xcs234 - reinforcement learning/attachments/A1.pdf]]

My solution:
source code - [XCS234/A1 at main · ammarhusain/XCS234 · GitHub](https://github.com/ammarhusain/XCS234/tree/main/A1)
[[courses/xcs234 - reinforcement learning/attachments/XCS234_A1.pdf]]

# A2

[[courses/xcs234 - reinforcement learning/attachments/A2.pdf]]

**Required readings:**

[[courses/xcs234 - reinforcement learning/attachments/DQNNaturePaper_DeepMind.pdf|DeepMind DQN Nature Paper]] Human-level control through deep [[reinforcement learning]]
To improve the data efficiency and stability of the training process, DeepMind's [paper](https://www.datascienceassn.org/sites/default/files/Human-level%20Control%20Through%20Deep%20Reinforcement%20Learning.pdf) employed two strategies:

**(1) replay buffer:** to store transitions observed during training. When updating the QQ function, transitions are drawn from this replay buffer. This improves data efficiency by allowing each transition to be used in multiple updates.

**(2) target network**: with parameters \bar{\theta}θˉ to compute the target value of the next state, $\max_{a'} Q(s',a')$. The update becomes:

$$
\theta \leftarrow \theta + \alpha\left(r+\gamma \max_{a' \in \mathcal{A}}Q_{\bar{\theta}}\left(s', a'\right) - Q_{\theta}(s, a)\right) \nabla_{\theta} Q_{\theta}(s, a)
$$

![[courses/xcs234 - reinforcement learning/attachments/Playing Atari with Deep RL.pdf]]

**Question 7 result - Nature DQN on Pong**
![[courses/xcs234 - reinforcement learning/attachments/rl-video-step-0.mp4]]

**Submission**
![[courses/xcs234 - reinforcement learning/attachments/XCS234_A2.pdf]]

![[courses/xcs234 - reinforcement learning/attachments/submission.zip]]

# A3

[[courses/xcs234 - reinforcement learning/attachments/A3.pdf]]

Submission: ![[courses/xcs234 - reinforcement learning/attachments/submission_A3.zip]]

# A4

[[courses/xcs234 - reinforcement learning/attachments/A4.pdf]]
[[courses/xcs234 - reinforcement learning/attachments/Thompson Sampling for Contextual Bandits with Linear Payoffs.pdf]]
[[courses/xcs234 - reinforcement learning/attachments/A Contextual-Bandit Approach to Personalized News Article Recommendation.pdf]]

Solution: [[courses/xcs234 - reinforcement learning/attachments/A4.zip]]
