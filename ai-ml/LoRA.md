---
created: 2023-11-05-Sunday 06:55
modified: 2023-11-07-Tuesday 13:18
publish: 
---

# Finetuning  Libraries

- Plain old HuggingFace - [example tutorial](https://wandb.ai/capecape/alpaca_ft/reports/How-to-Fine-tune-an-LLM-Part-3-The-HuggingFace-Trainer--Vmlldzo1OTEyNjMy)
Below are some other ones though not sure why I would want to use them - unnecessary abstractions or wrappers:
- [GitHub - Lightning-AI/lit-gpt: Hackable implementation of state-of-the-art open-source LLMs based on nanoGPT. Supports flash attention, 4-bit and 8-bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.](https://github.com/Lightning-AI/lit-gpt) and [GitHub - Lightning-AI/lit-llama: Implementation of the LLaMA language model based on nanoGPT. Supports flash attention, Int8 and GPTQ 4bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.](https://github.com/Lightning-AI/lit-llama)
- [GitHub - OpenAccess-AI-Collective/axolotl: Go ahead and axolotl questions](https://github.com/OpenAccess-AI-Collective/axolotl)
- [GitHub - hiyouga/LLaMA-Factory: Easy-to-use LLM fine-tuning framework (LLaMA, BLOOM, Mistral, Baichuan, Qwen, ChatGLM)](https://github.com/hiyouga/LLaMA-Factory)
- [GitHub - pytorch/torchtune: A Native-PyTorch Library for LLM Fine-tuning](https://github.com/pytorch/torchtune)
- [GitHub - unslothai/unsloth: Finetune Llama 3, Mistral & Gemma LLMs 2-5x faster with 80% less memory](https://github.com/unslothai/unsloth)
- [GitHub - hiyouga/LLaMA-Factory: Unify Efficient Fine-Tuning of 100+ LLMs](https://github.com/hiyouga/LLaMA-Factory)
- Good overview tutorial with a GPT head: [LLMs-from-scratch/ch06/01\_main-chapter-code/ch06.ipynb at main · rasbt/LLMs-from-scratch · GitHub](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch06/01_main-chapter-code/ch06.ipynb)
- [GitHub - mistralai/mistral-finetune](https://github.com/mistralai/mistral-finetune)
# Sources
[LORA: LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS | Microsoft](https://arxiv.org/pdf/2106.09685.pdf)
[[2012.13255] Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning](https://arxiv.org/abs/2012.13255)

[GitHub - microsoft/LoRA: Code for loralib, an implementation of "LoRA: Low-Rank Adaptation of Large Language Models"](https://github.com/microsoft/LoRA)
LoRA reduces the number of trainable parameters by learning pairs of rank-decompostion matrices while freezing the original weights. This vastly reduces the storage requirement for large language models adapted to specific tasks and enables efficient task-switching during deployment all without introducing inference latency. LoRA also outperforms several other adaptation methods including adapter, prefix-tuning, and fine-tuning.

# [Low-rank Adaption of Large Language Models: Explaining the Key Concepts Behind LoRA - YouTube](https://www.youtube.com/watch?v=dA-NhCtrrVE&t=44s)

Its a way of finetuning a large model by factorizing the delta weight updates in to some lower rank represenation - its a subset of PEFT (parameter efficient fine tuning )

![[LoRA-2023-08-11.png]]

Does a matrix decomposition
![[LoRA-2023-08-11-1.png]]
![[LoRA-2023-08-11-2.png]]

Mostly do this to attention weights - to the Q & V weight vectors
[Simple colab](https://colab.research.google.com/drive/1iERDk94Jp0UErsPf7vXyPKeiM4ZJUQ-a?usp=sharing#scrollTo=UQ-cH7ieCARh)
Finetuning is for structure not knowledge

# [PEFT LoRA Explained in Detail - Fine-Tune your LLM on your local GPU - YouTube](https://www.youtube.com/watch?v=YVU5wAA6Txo)

PEFT:Parameter-Efficient Fine-Tuning of Billion-Scale Models on Low-Resource Hardware

- HuggingFace Library freezing most parameters of a pre-trained LLM

LORA: Low-Rank Adaptation (a random projection to a smaller subspace)

- freezes pre-trained model weights and injects trainable rank decomposition matrices into each layer of Transformer

Adapter Transformers: adapter-transformers extend [[hugging face]] transformers

- AdapterHub: A Framework for Adapting Transformers

[[1902.00751] Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751)

- Fine-tuning involves copying the weights from a pre-trained network and tuning them on the downstream task (a new set of weights for each task).
- Multi-task learning requires simultaneous access to all tasks (mem intense).
- Adapters yield "parameter-efficient tuning" for NLP. It permits training on tasks sequentially!
- Tuning with adapter modules involves adding a small number of new parameters to a model, which are trained on the downstream task.
- In adapter-tuning, the parameters of the original network are frozen and therefore may be shared by many tasks.
![[LoRA-2023-08-15.png]]
These adapters are being injected within the [[transformer]] layers and not just as a couple of MLP layers on top of the network for classification/regression etc.

[[2007.07779] AdapterHub: A Framework for Adapting Transformers](https://arxiv.org/abs/2007.07779)
![[LoRA-2023-08-15-1.png]]
![[LoRA-2023-08-15-2.png]]
![[LoRA-2023-08-15-3.png]]

LoRA freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture.

[[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

We use Wa, Wk, Wv, and Wo to refer to the query/key/value/output projection matrices in the self-attention module.
During full fine-tuning, the model is initialized to pre-trained weights and all are updated to $\phi + \Delta \phi$ by repeatedly following the gradient.
One of the main drawbacks for full fine-tuning is that for each downstream task, we learn a different set of parameters $\Delta \phi$.
LORA adopts a more parameter-efficient approach, where the task-specific parameter increment $\Delta \phi = \Delta \phi(\theta)$ is further encoded by a much smaller-sized set of parameters $\theta$. LoRA proposes to use a Low-Rank representation to encode $\Delta \phi$.

[Quickstart — adapter-transformers documentation](https://docs.adapterhub.ml/quickstart.html) -> Same exists within PEFT library on [[hugging face]]

# Qlora

![[LoRA-2023-08-14-1.png]]

# [Understanding 4bit Quantization: QLoRA explained (w/ Colab) - YouTube](https://www.youtube.com/watch?v=TPcXVJ1VSRI)

[Colab for QLoRA](https://colab.research.google.com/drive/1BiQiw31DT7-cDp1-0ySXvvhzqomTdI-o?usp=sharing)

![[LoRA-2023-08-14-2.png]]

![[LoRA-2023-08-14-3.png]]
![[LoRA-2023-08-14-4.png]]

OLORA stands for Quantization and Low-Rank Adapters

In this method, the original pre-trained weights of the model are quantized to 4-bit and kept fixed during fine-tuning. Then, a small number of trainable parameters in the form of low-rank adapters are introduced during fine-tuning. These adapters are trained to adapt the pre-trained model to the specific task it is being fine-tuned for, in 32-bit floating-point format.

When it comes to computations (like forward and backward passes during training, or inference), the 4-bit quantized weights are dequantized back to 32-bit floating-point numbers.

After the fine-tuning process, the model consists of the original weights in 4-bit form, and the additional low-rank adapters in their higher precision format.

The additional low-rank adapters in the QLORA method are in a higher precision format, typically 32-bit floating-point (bfloat16), for a few reasons:

Higher precision allows the model to capture more subtle patterns in the data. This is particularly important for the low-rank adapters, as they are responsible for adapting the pre-trained model to the specific task it is being fine-tuned for.

Training neural networks involves a lot of incremental updates to the weights.

Weights in a higher precision format ensures that updates are accurately captured.

While quantizing all weights can save memory, the computational efficiency might not always improve. GPUs are optimized for 32-bit (bfloat16) operations.

Computations w/ 32-bit floating-point can be faster than with lower precision.

# [Fine-tune LLama2 w/ PEFT, LoRA, 4bit, TRL, SFT code - YouTube](https://www.youtube.com/watch?v=zcMQXID447s)

Pretty good notebook to follow along to ifnetune a LoRa model using [[hugging face]]. Relevant for [[archive/apple/j595 journal]]
![[ai-ml/attachments/gpt_llm_trainer.ipynb]]
