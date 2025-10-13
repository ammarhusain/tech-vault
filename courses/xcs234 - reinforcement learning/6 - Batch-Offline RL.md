---
created: 2022-09-16-Friday 17:35
modified: 2023-03-10-Friday 23:15
---

[[courses/xcs234 - reinforcement learning/attachments/Mod6_Slides.pdf]]

# Introduction to Batch Rl

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220916174119.png]] ![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220916174144.png]]

Data Is Censored in that Only Observe Outcomes for Decisions Made

Why Can’t We Just Use Q-Learning?
	Q-learning is an off policy RL algorithm
		Can be used with data different than the state--action pairs would visit under the optimal Q state action values
	But deadly triad (Sutton & Barto) of bootstrapping, function approximation and off policy, and can fail

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220919084159.png|400]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220919101032.png|400]]

![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220919111256.png]]
![[courses/xcs234 - reinforcement learning/attachments/Pasted image 20220919131134.png]]
