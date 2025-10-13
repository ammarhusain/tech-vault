---
aliases: []
created: 2022-09-22-Thursday 23:32
modified: 2023-06-22-Thursday 21:44
tags: 
---

**Linked by:**

**Related To:**
[[machine-learning]]
[[career/career]]

---

[[courses/xcs229ii-machine-learning/attachments/XCS229ii Project Milestones.pdf]]

[[courses/xcs229ii-machine-learning/attachments/XCS229ii_Syllabus.pdf]]

Goodnotes: [[courses/xcs229ii-machine-learning/attachments/Machine Learning strategy and reinforcement learning (my notes).pdf]]

Assignment #1 - [[courses/xcs229ii-machine-learning/attachments/PS1_answers.pdf]]

Assignment #2 - [[courses/xcs229ii-machine-learning/attachments/PS2.pdf]]
	- This exercise was a pain in the butt
	- I really need to be extra cautious when I read through instructions. Also need to slow down and look over every single detail of the course rather than rushing to finish it off ASAP. There were a lot of nuances such as in the reward function etc that if I actually paid attention I would be able to have spotted them
	- Also shouldn't over index on one part of the problem. I kept debugging one function whereas the bug was in a totally separate piece of code.
	- The issue was that I was not updating my transition_probabilities MDP model correctly. It was not zeroing out the terminal state probabilities and left them to some small constant. Therefore in the value update it kept skimming off more & more value in the terminal state because it thought it could keep going further. I fixed the problem in the update_mdp_transition function when reading through it very very carefully.
	![[courses/xcs229ii-machine-learning/attachments/ski.gif]]
	[[courses/xcs229ii-machine-learning/attachments/XCS229ii-PS2.zip]]

%% Begin Waypoint %%
- **[[courses/xcs229ii-machine-learning/xcs229ii - machine learning]]**
	- [[courses/xcs229ii-machine-learning/1 - learning theory]]
	- [[courses/xcs229ii-machine-learning/2 - debugging ml algorithms]]
	- [[courses/xcs229ii-machine-learning/3 - reinforcement learning]]
	- [[courses/xcs229ii-machine-learning/4 - LQR, DDP, LQG]]
	- **attachments**

	- [[courses/xcs229ii-machine-learning/project - hyperparameter tuning using rl]]

%% End Waypoint %%

---

**Raindrop bookmarks:**

- [XCS229ii-project/rl_env_sandbox.ipynb at main · ammarhusain/XCS229ii-project](https://github.com/ammarhusain/XCS229ii-project) : XCS229ii project repo hyperparameter optimization [[reinforcement learning|RL]]
- [XCS229ii Final Paper](https://docs.google.com/document/d/1yOirIKVzVlGLTRHSC51dIkGUbd2Btj8u3oqDZUMUdgk/edit)
- [DLR-RM/stable-baselines3: PyTorch version of Stable Baselines, reliable implementations of reinforcement learning algorithms.](https://github.com/DLR-RM/stable-baselines3) : [[pytorch]] version of Stable Baselines, reliable implementations of [[reinforcement learning]] algorithms
- [ammarhusain/XCS229ii-project](https://github.com/ammarhusain/XCS229ii-project/tree/main)
- [Auto-Tuning Hyperparameters with Optuna and PyTorch](https://www.youtube.com/watch?v=P6NwZVl8ttc)
- [Deep Deterministic Policy Gradient — Spinning Up documentation](https://spinningup.openai.com/en/latest/algorithms/ddpg.html)
- [quantopian/pyfolio: Portfolio and risk analytics in Python](https://github.com/quantopian/pyfolio)
- [Hyp-RL paper](https://arxiv.org/pdf/1906.11527.pdf)
- [optuna.study.Study — Optuna 2.10.0 documentation](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html?highlight=optimize#optuna.study.Study.optimize)
- [Deep Reinforcement Learning and Hyperparameter Tuning](https://towardsdatascience.com/deep-reinforcement-learning-and-hyperparameter-tuning-df9bf48e4bd2) : Using Ray’s Tune to Optimize your Models
- [2016-Apr-26-AAPL.txt - Department of Management](https://dataverse.nl/file.xhtml?fileId=47772&version=1.0)
- [(PDF) Stock Values and Earnings Call Transcripts: a Dataset Suitable for Sentiment Analysis](https://www.researchgate.net/publication/349435078_Stock_Values_and_Earnings_Call_Transcripts_a_Dataset_Suitable_for_Sentiment_Analysis) : dataset reports a collection of earnings call transcripts, the related stock prices, and the related sector index
- [Extracting text from HTML file using Python](https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python)
- [Jupyter notebook support | PyCharm](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html)
- [GitHub - openai/baselines: OpenAI Baselines: high-quality implementations of reinforcement learning algorithms](https://github.com/openai/baselines) : OpenAI Baselines: high-quality implementations of [[reinforcement learning]] algorithms
- [r/reinforcementlearning - Is hyperparameter tuning legitimate in reinforcement learning?](https://www.reddit.com/r/reinforcementlearning/comments/fzj9k1/is_hyperparameter_tuning_legitimate_in/)
- [Reinforce](http://www.cs.toronto.edu/~tingwuwang/REINFORCE.pdf)
- [XCS229ii Shared Projects | Powered by Box](https://stanford.app.box.com/s/9sokp36e7ygcyril7xciyavefe0730h3)
- [mystanfordconnection | Stanford Center for Professional Development](https://mystanfordconnection.stanford.edu/portal/logon.do?method=logonAuthenticatedExternally)
- [Lecture 1 - Stanford CS229: Machine Learning - Andrew Ng (Autumn 2018)](https://www.youtube.com/watch?v=jGwO_UgTS7I&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
