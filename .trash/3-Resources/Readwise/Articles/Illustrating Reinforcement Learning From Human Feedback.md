---
aliases: []
tags:
---
# Illustrating Reinforcement Learning From Human Feedback

![rw-book-cover](https://huggingface.co/blog/assets/120_rlhf/thumbnail.png)
### Metadata
Author: [[Nathan Lambert]]
Full Title: Illustrating Reinforcement Learning From Human Feedback
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://huggingface.co/blog/rlhf
Date Highlighted: [[2022-12-20-Tuesday]]

## Highlights
- three core steps:
  1. Pretraining a language model (LM),
  2. gathering data and training a reward model, and
  3. fine-tuning the LM with reinforcement learning. ([View Highlight](https://read.readwise.io/read/01gmpg41a2pv3gttme3t2kcwd3))
- OpenAI used a smaller version of GPT-3 for its first popular RLHF model, [InstructGPT](https://openai.com/blog/instruction-following/). ([View Highlight](https://read.readwise.io/read/01gmpg36vshdde59fwdt2smdgh))
- Generating a reward model (RM, also referred to as a preference model) calibrated with human preferences is where the relatively new research in RLHF begins. The underlying goal is to get a model or system that takes in a sequence of text, and returns a scalar reward which should numerically represent the human preference. ([View Highlight](https://read.readwise.io/read/01gmpg92exawxrkkdhqmzet941))
- These LMs for reward modeling can be both another fine-tuned LM or a LM trained from scratch on the preference data. ([View Highlight](https://read.readwise.io/read/01gmpgg5djmk5f37b1cd03kr02))
    - Note: Its almost like a GAN. You have the main LLM (generator) and the RM (discriminator) that helps in finetuning the LLM output
- Human annotators are used to rank the generated text outputs from the LM. One may initially think that humans should apply a scalar score directly to each piece of text in order to generate a reward model, but this is difficult to do in practice. The differing values of humans cause these scores to uncalibrated and noisy. Instead, rankings are used to compare the outputs of multiple models and create a much better regularized dataset. ([View Highlight](https://read.readwise.io/read/01gmpgj13n5m8qs9shys7mtw11))
- An interesting artifact of this process is that the successful RLHF systems to date have all used reward language models of similar sizes to the text generation. An intuition would be that these preference models need to have similar capacity to understand the text given to them as a model would need in order to generate said text. ([View Highlight](https://read.readwise.io/read/01gmpgmf00qr262m5134hkyy7x))
- At this point in the RLHF system, we have an initial language model that can be used to generate text and a preference model that takes in any text and assigns it a score of how well humans perceive it. Next, we use **reinforcement learning (RL)** to optimize the original language model with respect to the reward model.
  ![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/rlhf/reward-model.png) ([View Highlight](https://read.readwise.io/read/01gmpgn8x9twy6te7mwx793a5h))
- Let's first formulate this fine-tuning task as a RL problem. First, the **policy** is a language model that takes in a prompt and returns a sequence of text (or just probability distributions over text). The **action space** of this policy is all the tokens corresponding to the vocabulary of the language model (often on the order of 50k tokens) and the **observation space** is the possible input token sequences, which is also quite large (size of vocabulary x number of input tokens). The **reward function** is a combination of the preference model and a constraint on policy shift. ([View Highlight](https://read.readwise.io/read/01gmpgtremmyps82nrtrefypn9))
- Given a prompt, *x*, from the dataset, two texts, *y1*, *y2*, are generated – one from the initial language model and one from the current iteration of the fine-tuned policy. The text from the current policy is passed to the preference model, which returns a scalar notion of “preferability”, rθ​. This text is compared to the text from the initial model to compute a penalty on the difference between them. ([View Highlight](https://read.readwise.io/read/01gmpgygn730h15r2vd12tf2fz))
- Finally, the **update rule** is the parameter update from PPO that maximizes the reward metrics in the current batch of data (PPO is on-policy, which means the parameters are only updated with the current batch of prompt-generation pairs) ([View Highlight](https://read.readwise.io/read/01gmph2xj1wamtgcr3e6ajhx8z))
- ![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/rlhf/rlhf.png) ([View Highlight](https://read.readwise.io/read/01gmph216crmmkbjk452yf7mz4))
- there are already a few active repositories for RLHF in PyTorch that grew out of this. The primary repositories are Transformers Reinforcement Learning ([TRL](https://github.com/lvwerra/trl)), [TRLX](https://github.com/CarperAI/trlx) which originated as a fork of TRL, and Reinforcement Learning for Language models ([RL4LMs](https://github.com/allenai/RL4LMs)). ([View Highlight](https://read.readwise.io/read/01gmphfjrtgb99w41k98mcfhb9))
- One large cost of the feedback portion of fine-tuning the LM policy is that every generated piece of text from the policy needs to be evaluated on the reward model (as it acts like part of the environment in the standard RL framework). To avoid these costly forward passes of a large model, offline RL could be used as a policy optimizer. ([View Highlight](https://read.readwise.io/read/01gmphwe7v854nra44hjrbk4h9))
