Repo here: /Users/ammarh/Library/Mobile Documents/com~apple~CloudDocs/code/smol-course/
#tinker_short [GitHub - huggingface/smol-course: A course on aligning smol models.](https://github.com/huggingface/smol-course/tree/main)

**DPO (Direct Preference Optimization)** is a simpler way to do preference learning without the complexity of running RL (like PPO) in RLHF. Llama uses DPO
- First step is to do supervised finetuning
- Second step is preference alignment where the model is trained on pairs of outputs - one preferred and one non-preferred. The preference pairs help the model understand which responses better align with human values and expectations.
	- Rather than training a separate reward model, DPO uses a binary cross-entropy loss to directly update the model weights based on preference data. This streamlined process makes training more stable and efficient while achieving comparable or better results than traditional RLHF.

[What is direct preference optimization (DPO)? \| SuperAnnotate](https://www.superannotate.com/blog/direct-preference-optimization-dpo)
- Instead, DPO uses a [binary cross-entropy objective](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a) to steer models toward producing the types of responses that people actually want to see. This approach cuts out the need for building and tweaking a separate reward model, making the training process more straightforward.
- ![[archive/apple/attachments/smol-course-2025-03-04.png]]
- Good overview of PPO updates in RLHF: [Illustrating Reinforcement Learning from Human Feedback (RLHF)](https://huggingface.co/blog/rlhf)
	- ![[archive/apple/attachments/smol-course-2025-03-04-1.png]]

**ORPO** merges SFT + DPO into one step using a novel odds ratio loss function