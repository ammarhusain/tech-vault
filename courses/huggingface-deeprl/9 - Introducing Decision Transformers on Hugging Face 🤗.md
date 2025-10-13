---
aliases: []
created: 2023-02-07-Tuesday 18:12
modified: 2023-03-10-Friday 23:15
tags: 
---
# Introducing Decision Transformers on Hugging Face 🤗

![rw-book-cover](https://huggingface.co/blog/assets/58_decision-transformers/thumbnail.jpg)

## Metadata

Author: [[huggingface.co]]
Full Title: Introducing Decision Transformers on Hugging Face 🤗
Category: #readwise/articles
URL: https://huggingface.co/blog/decision-transformers
Date Highlighted: [[2023-02-08-Wednesday]]

[Decision Transformer](https://huggingface.co/docs/transformers/model_doc/decision_transformer) - HuggingFace library
Colab [link](https://colab.research.google.com/drive/1fC2oXYpHr1qv5yLcnRsoEyfgrdxPb84B?authuser=1)

## Highlights
- in offline reinforcement learning, the agent only uses data collected from other agents or human demonstrations. **It does not interact with the environment**.
  The process is as follows:
  1. Create a dataset using one or more policies and/or human interactions.
  2. Run offline RL on this dataset to learn a policy ([View Highlight](https://read.readwise.io/read/01grqb3dps7dx0855pvvjeyx72))
- The main idea is that instead of training a policy using RL methods, such as fitting a value function, that will tell us what action to take to maximize the return (cumulative reward), we use a sequence modeling algorithm (Transformer) that, given a desired return, past states, and actions, will generate future actions to achieve this desired return. It’s an autoregressive model conditioned on the desired return, past states, and actions to generate future actions that achieve the desired return. ([View Highlight](https://read.readwise.io/read/01grqb6rejfksfv67cbh36f3g8))
- [![](https://huggingface.co/blog/assets/58_decision-transformers/offlinevsonlinerl.gif)](https://huggingface.co/blog/assets/58_decision-transformers/offlinevsonlinerl.gif)
  *A comparison between Reinforcement Learning in an Online and Offline setting* ([View Highlight](https://read.readwise.io/read/01grqb1ff9bhz8tpd3565ws6vw))
- This is a complete shift in the Reinforcement Learning paradigm since we use generative trajectory modeling (modeling the joint distribution of the sequence of states, actions, and rewards) to replace conventional RL algorithms. It means that in Decision Transformers, we don’t maximize the return but rather generate a series of future actions that achieve the desired return. ([View Highlight](https://read.readwise.io/read/01grqb7eympjk0b37ts7eb1p20))
- 1. We feed the last K timesteps into the Decision Transformer with 3 inputs:
  - Return-to-go
  - State
  - Action
  3. The tokens are embedded either with a linear layer if the state is a vector or CNN encoder if it’s frames.
  4. The inputs are processed by a GPT-2 model which predicts future actions via autoregressive modeling.
  [![](https://huggingface.co/blog/assets/58_decision-transformers/dt-architecture.gif)](https://huggingface.co/blog/assets/58_decision-transformers/dt-architecture.gif)
  *Decision Transformer architecture. States, actions, and returns are fed into modality specific linear embeddings and a positional episodic timestep encoding is added. Tokens are fed into a GPT architecture which predicts actions autoregressively using a causal self-attention mask.* ([View Highlight](https://read.readwise.io/read/01grqbjtn5m4q3cee0awgvexyg))
