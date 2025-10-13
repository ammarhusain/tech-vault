---
aliases: [aiml, ml, machine learning]
created: 2022-08-27-Saturday 22:22
modified: 2023-06-23-Friday 15:59
tags: aiml
---

**Linked by:**
[[career/career]]
[[2-Focus-Areas/Readwise/Articles/Competitive Programming With AlphaCode]]
[[courses/xcs224u - natural language understanding/4 - grounded language understanding]]
[[courses/xcs229ii-machine-learning/1 - learning theory|bias-variance tradeoff]]
[[courses/xcs229ii-machine-learning/2 - debugging ml algorithms]]
[[landing]]

**Related To:**

---

[[machine learning overview.canvas|machine learning overview]]
[[State of AI Report 2023 - ONLINE.pdf]]

# Core Concepts

![[ai-ml-2023-05-01.png|350]]
[[backpropagation]]
[[linear classification]]
[[optimization]]
[[loss function]]
[[neural networks]]
[[metrics]]
[[data preprocessing]]

[[visual language models]]
[[convolutional neural nets]]
[[autoencoder]]
[[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation|neural networks]]
[[bias & variance]]
[[neural network debugging]]
[[courses/xcs224n - natural language processing/xcs224n - natural language processing|natural language processing]]
[[diffusion model]]
[[*shiny-fm-datasets]]
[[transformer]]
[[recurrent neural networks]] - good note in [old evernote](https://www.evernote.com/shard/s518/nl/91738801/915aa774-e5e4-46f4-bf51-9f1a3ad21673?title=Learnings%3A%20Deep%20Learning)

# Model Architectures

[[convolutional neural nets]]
[[transformer]]

# Model Types
## Visual Language Models (VLM)

[[*shiny-fm-datasets#CLIP Connecting Text Images|CLIP]], [[*shiny-fm-datasets#Flamingo https www deepmind com blog tackling-multiple-tasks-with-a-single-visual-language-model Demo https dm-vlm-applied corp google com 80B parameter|Flamingo]]

## Image Generation

[[*shiny-fm-datasets#DALL·E 2]]; [[*shiny-fm-datasets#ImageGen https imagen research google|ImageGen]]; [[*shiny-fm-datasets#Parti]]

## Large Language Models (LLM)

GPT-3, RoBERT, [GLaM](https://ai.googleblog.com/2021/12/more-efficient-in-context-learning-with.html), [LaMDA](https://ai.googleblog.com/2022/01/lamda-towards-safe-grounded-and-high.html), [Gopher](https://arxiv.org/abs/2112.11446), [Megatron-Turing NLG](https://arxiv.org/abs/2201.11990), [[*shiny-fm-datasets#Text-To-Text Transfer Transformer - T5|T5]]

## Multi-modal Llm

GPT-4, Palm-E

## Denoising Diffusion Probabilistic Models (aka Ddpm, [Diffusion models):](https://github.com/openai/guided-diffusion)
- Generative models that are apparently better than GANs.
- Can be conditioned on various inputs - text captions, inpainting etc
- Similar to Variational Auto encoders (VAEs)
	![[ai-ml/attachments/Untitled 3.png|500]]

[High Fidelity Image Generation Using Diffusion Models](https://ai.googleblog.com/2021/07/high-fidelity-image-generation-using.html)

## Audio Language Models (ALM)

Wav2CLIP, Speech2Text


# Logs
```dataviewjs 
let pages_foo = dv.pages('"Daily"').sort(p => p.file.name, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#aiml"))))
}
```

# Frameworks
- **Zero-shot Learning (ZSL)**
	- is a problem setup in [[machine-learning|machine learning]] where at test time, a learner observes samples from classes, which were not observed during training and needs to predict the class that they belong to.
- **[Socratic Models](https://socraticmodels.github.io/) (SMs)**
	- a framework that uses structured dialogue between pre-existing foundation models, each of which can exhibit unique (but complementary) capabilities
- **Chain of Thought Prompting**
	- Technique in large language models to break down the prompt step by step that helps the model reason in a similar way to how a human would ([paper](https://arxiv.org/pdf/2205.11916v1.pdf))

# Tools & Resources
- [[pytorch]] tutorials & sandbox
- Weights & Biases for results tracking
- GradIO, Flask, Streamlit for creating Web apps
	- [GitHub - Lightning-AI/LitServe: Lightning-fast serving engine for AI models. Flexible. Easy. Enterprise-scale.](https://github.com/Lightning-AI/LitServe?tab=readme-ov-file#define-a-server)
- Repl.it, Vercel
- Tensorflow datasets
- [Comet ML - Build better models faster](https://www.comet.com/site/)

[[machine-learning-cheat-sheet.pdf]]

# Someday /Maybe
- [ ] XCS221 (AI techniques)

# Books
- [Deep Learning - Goodfellow et al](https://www.deeplearningbook.org/)

