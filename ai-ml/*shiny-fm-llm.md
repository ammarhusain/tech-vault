---
created: 2023-09-12-Tuesday 11:07
modified: 2023-09-12-Tuesday 11:21
publish: 
---

# Models
## Text-to-text Transfer Transformer - T5

11B parameters, [Colab](https://colab.sandbox.google.com/github/google-research/text-to-text-transfer-transformer/blob/main/notebooks/t5-trivia.ipynb), [Blog](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html), [code](https://goo.gle/t5), and [pre-trained models](https://github.com/google-research/text-to-text-transfer-transformer#released-model-checkpoints), Live app for T5 text generation: [Demo – InferKit](https://app.inferkit.com/demo) #sandbox

- Transfer learning's effectiveness comes from pre-training a model on abundantly-available unlabeled text data with a self-supervised task, such as language modeling or filling in missing words. After that, the model can be fine-tuned on smaller labeled datasets, often resulting in (far) better performance than training on the labeled data alone. The recent success of transfer learning was ignited in 2018 by [GPT](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf), [ULMFiT](https://arxiv.org/abs/1801.06146), [ELMo](https://arxiv.org/abs/1802.05365), and [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) and 2019 saw the development of a huge diversity of new methods like [XLNet](https://arxiv.org/abs/1906.08237), [RoBERTa](https://arxiv.org/abs/1907.11692) [ALBERT](https://ai.googleblog.com/2019/12/albert-lite-bert-for-self-supervised.html) [Reformer](https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html), and [MT-DNN](https://arxiv.org/abs/1901.11504).
- With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the input and output are always text strings, in contrast to BERT-style models that can only output either a class label or a span of the input. Our text-to-text framework allows us to use the same model, [[loss function]], and hyperparameters on *any* NLP task, including [[courses/xcs224n - natural language processing/8-9 - Machine Translation, Seq2Seq and Attention|machine translation]], document summarization, question answering, and classification tasks (e.g., sentiment analysis). We can even apply T5 to regression tasks by training it to predict the string representation of a number instead of the number itself.
- ![[Pasted image 20220825083213.png|800]]
- Colossal Clean Crawled Corpus (C4), a cleaned version of Common Crawl that is *two orders of magnitude larger than Wikipedia*. C4 is available through [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/c4)
- model architectures: where we found that encoder-decoder models generally outperformed "decoder-only" language models;
- Numerous creative applications like [Talk To Transformer](https://talktotransformer.com/) and the text-based game [AI Dungeon](https://aidungeon.io/).

## Gopher

[[2-Focus-Areas/Readwise/Articles/Language Modelling at Scale Gopher, Ethical Considerations, and Retrieval]]
Deepmind's large language model - 280 billion parameters
RETRO is an interesting architecture that they present on how LLM generated text can be sent through a retrieval database that maps back to the closest train data examples that might have contributed in producing that result (like an efficient nearest neighbor search). This could be used for dataset curation and removing harmful examples in internet scale datasets.

## Chinchilla

[[2-Focus-Areas/Readwise/Articles/An Empirical Analysis of Compute-Optimal Large Language Model Training]]
Large language model - 70-billion parameter model trained for 1.3 trillion tokens
Outperforms Gopher which has 4X more parameters but 4X fewer training data tokens, though the compute cost of both are the same.

## GPT series

Decoder only [[transformer|Transformer]] architecture
Very good simple walk through of implementing a GPT architecture in PyTorch - [Let's build GPT: from scratch, in code, spelled out. - YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY)
[GitHub - karpathy/nanoGPT: The simplest, fastest repository for training/finetuning medium-sized GPTs.](https://github.com/karpathy/nanoGPT)

### ChatGPT

#sandbox [https://chat.openai.com](https://chat.openai.com/)
Is there anything more to say?

### InstructGPT

Its GPT-3 finetuned using RLHF on a instruction dataset. To train InstructGPT models, our core technique is [reinforcement learning from human feedback (RLHF)](https://openai.com/blog/deep-reinforcement-learning-from-human-preferences/). This technique uses human preferences as a reward signal to fine-tune our models, which is important as the safety and alignment problems we are aiming to solve are complex and subjective, and aren’t fully captured by simple automatic metrics.
![[shiny new models-2023-07-25-2.png]]
The resulting InstructGPT models are much better at following instructions than GPT-3. They also make up facts less often, and show small decreases in toxic output generation. Our labelers prefer outputs from our 1.3B InstructGPT model over outputs from a 175B GPT-3 model, despite having more than 100x fewer parameters.


### Gpt4-o1 (Strawberry)
[[2024-09-13-Friday]] - GPT4o augmented with capabilities to solve complex reasoning tasks. creates CoT tokens before trying to solve the input problem
[Something New: On OpenAI's "Strawberry" and Reasoning](https://www.oneusefulthing.org/p/something-new-on-openais-strawberry?publication_id=1180644&post_id=148742683&isFreemail=true&r=qjq2&triedRedirect=true)
o1 represents a paradigm shift from "memorize the answers" to "memorize the reasoning" but is not a departure from the broader paradigm of fitting a curve to a distribution in order to boost performance by making everything in-distribution.

### o3 and o4-mini
Reasoning model with further train and test time scaling. Also trained to use ~600 tools as part of the reasoning training. Before the specific tools were not directly part of the training itself.

### GPT-5
input limit of 272,000 tokens and an output limit (which includes invisible reasoning tokens) of 128,000 tokens. They support text and image for input, text only for output.

### gpt-oss 20b and 120b
[Introducing gpt-oss \| OpenAI](https://openai.com/index/introducing-gpt-oss/)
[OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony#built-in-tools)

gpt-oss-120b ; 36 layers | 117B total params | 5.1B active params per token | 128 total experts | 4 active experts per token | 128k context length
gpt-oss-20b; 24; 21B; 3.6B; 32; 4; 128k
![[*shiny-fm-llm-2025-08-26.png]]
## Vicuna

We introduce Vicuna-13B, an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT. Preliminary evaluation using GPT-4 as a judge shows Vicuna-13B achieves more than 90%* quality of OpenAI ChatGPT and Google Bard while outperforming other models like LLaMA and Stanford Alpaca in more than 90%* of cases. The cost of training Vicuna-13B is around $300. The [code](https://github.com/lm-sys/FastChat) and [weights](https://github.com/lm-sys/FastChat#vicuna-weights), along with an online [demo](https://chat.lmsys.org/), are publicly available for non-commercial use.
*Cool thing about this is that it can be run locally using llama-cpp*

## Llama

Foundation models train on a large set of unlabeled data, which makes them ideal for fine-tuning for a variety of tasks. We are making LLaMA available at several sizes (7B, 13B, 33B, and 65B parameters)
Smaller models trained on more tokens — which are pieces of words — are easier to retrain and fine-tune for specific potential product use cases. We trained LLaMA 65B and LLaMA 33B on 1.4 trillion tokens. Our smallest model, LLaMA 7B, is trained on one trillion tokens.
As a foundation model, LLaMA is designed to be versatile and can be applied to many different use cases, versus a fine-tuned model that is designed for a specific task

### Llama2
[Paper](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.2365-6/10000000_662098952474184_2584067087619170692_n.pdf?_nc_cat=105&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=KT6T4Ke4w-AAX-Y9cu1&_nc_ht=scontent-sjc3-1.xx&oh=00_AfAIsIQkqDIwnTlrkTPpAuUD649yQdfI78KAPAd-A-UfNA&oe=651B58BF)
Karpathy's [simple implementation](https://github.com/karpathy/llama2.c) for small models
Pretained on 2 trillion tokens and has double the context length of LLama. The models are available with 7B, 13B and 70B parameters.
![[shiny new models-2023-07-26-2.png]]

Llama-2-chat uses reinforcement learning from human feedback to ensure safety and helpfulness. **Training Llama-2-chat:** Llama 2 is pretrained using publicly available online data. An initial version of Llama-2-chat is then created through the use of supervised fine-tuning. Next, Llama-2-chat is iteratively refined using Reinforcement Learning from Human Feedback (RLHF), which includes rejection sampling and proximal policy optimization (PPO).
![[shiny new models-2023-07-26-3.png]]

There have been public releases of pretrained LLMs (such as BLOOM (Scao et al., 2022), LLaMa-1 (Touvron et al., 2023), and Falcon (Penedo et al., 2023)) that match the performance of closed pretrained competitors like GPT-3 (Brown et al., 2020) and Chinchilla (Hoffmann et al., 2022), but none of these models are suitable substitutes for closed “product” LLMs, such as ChatGPT, BARD, and Claude. These closed product LLMs are heavily fine-tuned to align with human preferences, which greatly enhances their usability and safety

The primary architectural differences from Llama 1 include increased context length and grouped-query attention (GQA).
Ouyang et al. (2022) demonstrates that a combination of instruction fine-tuning and RLHF can help fix issues with factuality, toxicity, and helpfulness that cannot be remedied by simply scaling up LLMs.

### Llama-3
Released the 404B model [[2024-07-23-Tuesday]] - [Introducing Llama 3.1: Our most capable models to date](https://ai.meta.com/blog/meta-llama-3-1/)
Other variants: 8B & 70B
- We opted for a standard decoder-only transformer model architecture with minor adaptations rather than a mixture-of-experts model to maximize training stability.
- We adopted an iterative post-training procedure, where each round uses supervised fine-tuning and direct preference optimization. This enabled us to create the highest quality synthetic data for each round and improve each capability’s performance.
- Compared to previous versions of Llama, we improved both the quantity and quality of the data we use for pre- and post-training. These improvements include the development of more careful pre-processing and curation pipelines for pre-training data, the development of more rigorous quality assurance, and filtering approaches for post-training data.
- *Seems like they used a lot of synthetic data to train this model and emphasized on data cleaning and curation. Definitely areas to consider with [[archive/Crawlspace]] to provide as services*
Interesting Llama agent library - [GitHub - meta-llama/llama-agentic-system: Agentic components of the Llama Stack APIs](https://github.com/meta-llama/llama-agentic-system)**128k context length**

### Llama 3.2
Release includes: 11B & 90B models (with vision encoders) and 1B & 3B models (text) for edge inference
Multi-modal model that adds a vision encoder and also a cross attention layer after every 4 self attention layers between the vision encoder output and the decoded output. Cross attention layers also use grouped query attention (GQA)
To add image input support, we trained a set of adapter weights that integrate the pre-trained image encoder into the pre-trained language model. The adapter consists of a series of cross-attention layers that feed image encoder representations into the language model.
During adapter training, we also updated the parameters of the image encoder, but intentionally did not update the language-model parameters. By doing that, we keep all the text-only capabilities intact, providing developers a drop-in replacement for Llama 3.1 models.

Launched Llama Stack API
![[llama-stack-api.png]]
Trained on 9 trillion tokens
[Llama 3.2: Revolutionizing edge AI and vision with open, customizable models](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)
Molmo 72B & 7B are supposed to be a stronger open weight alternative

![[shiny-fm-llm-2024-10-15.png]]

### Llama 4
[Title Unavailable \| Site Unreachable](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?__readwiseLocation=)
We use alternating dense and mixture-of-experts (MoE) layers for inference efficiency. MoE layers use 128 routed experts and a shared expert. Each token is sent to the shared expert and also to one of the 128 routed experts.
**Llama 4 Scout**
- **Active parameters**: 17 B (with 16 experts; total parameter count ~109 B)
- **Context window**: **10 million tokens** — ultra-long context capability
- **Training traits**: Trained from scratch  
**Llama 4 Maverick**
- **Active parameters**: 17 B (with 128 experts; total ~400 B)
- **Context window**: **1 million tokens** — still massive context
- **Training traits**: “Co-distilled” from the larger Behemoth model  
**Llama 4 Behemoth** (In Training)
- **Planned size**: 288 B active parameters (16 experts; ~2 trillion total parameters)
- Intelligent model built for distillation
Supports both **text and image input**, with outputs in text form
Scout handles 10M tokens, while Maverick supports 1M
## Falcon-180B

[[2023-09-07-Thursday]]
Falcon 180B, **the largest open-source language model ever with 180 billion parameters**, developed by Technology Innovation Institute from UAE.

Trained on 3.5 trillion tokens from RefinedWeb dataset and using more about 7 million GPU hours (about 4096 GPUs), the model represents the longest single-epoch pretraining for an open model. 

Falcon 180B not only tops the leaderboard for open-access models but also **rivals proprietary ones like PaLM-2 Large**. Its performance metrics span a range of NLP tasks, placing it between GPT-3.5 and GPT-4 depending on the evaluation benchmark.

- **Advanced multiquery attention architecture**, scaled up from Falcon 40B

## Claude Series
### Claude2

Introduces a new concept called constitutional AI to train the LLM for alignment.

### Claude 4
[Introducing Claude 4 \\ Anthropic](https://www.anthropic.com/news/claude-4) - Much better than claude-3.7 sonnet apparently
Keeps long running memory

## Alpaca

***Alpaca 7B**, a model fine-tuned from the LLaMA 7B model on 52K instruction-following demonstrations. On our preliminary evaluation of single-turn instruction following, Alpaca behaves qualitatively similarly to OpenAI’s text-davinci-003, while being surprisingly small and easy/cheap to reproduce*
![[shiny new models-2023-07-25.png]]
We started with the 175 human-written instruction-output pairs from the [self-instruct seed set](https://github.com/yizhongw/self-instruct). We then prompted text-davinci-003 to generate more instructions using the seed set as in-context examples. We improved over the self-instruct method by simplifying the generation pipeline (see details in [GitHub](https://github.com/tatsu-lab/stanford_alpaca#data-generation-process)) and significantly reduced the cost. Our data generation process results in 52K unique instructions and the corresponding outputs,
Equipped with this instruction-following dataset, we then fine-tuned the LLaMA models using Hugging Face’s training framework. For our initial run, fine-tuning a 7B LLaMA model took 3 hours on 8 80GB A100s,

- **Data**: [52K demonstrations](https://github.com/tatsu-lab/stanford_alpaca#data-release) used to fine-tune Alpaca.

## OpenAssistant - LAOIN

Open source [[#ChatGPT]]
#sandbox [HuggingChat](https://huggingface.co/chat/) - [[hugging face]] has built a UI on it

## StarCoder

#sandbox [BigCode - Playground - a Hugging Face Space by bigcode](https://huggingface.co/spaces/bigcode/bigcode-playground)
[StarCoder: A State-of-the-Art LLM for Code](https://huggingface.co/blog/starcoder?utm_source=alphasignalai.beehiiv.com&utm_medium=newsletter&utm_campaign=is-this-the-end-of-regulation-free-ai)

## Persimmon-8B
[[2023-09-19-Tuesday]]
Adept AI Labs introduces **Persimmon-8B, an open-source, fully permissively licensed language model with 8 billion parameters**. Despite training on less data, the model rivals or outperforms its peers like LLama 2 and MPT 7B Instruct and offers a much larger context size of 16k tokens.

## NuPIC
**NuPIC (developed by Jeff Hawkins' Numenta) aims to make AI processing up to 100 times more efficient.** **NuPIC's architecture allows Large Language Models (LLMs) to run efficiently on CPUs**, offering substantial cost savings and enhanced privacy. This shifts the AI landscape, which has largely depended on GPUs, towards more accessible and flexible CPU-based solutions.

## BLOOM - 176B

[[2023-10-10-Tuesday]] - [2211.05100.pdf](https://arxiv.org/pdf/2211.05100.pdf)
BigScience Large Open-science Open-access Multilingual Language Model 
Open source LLM released by HuggingFace.  BLOOM, a 176B-parameter open-access language model designed and built thanks to a collaboration of hundreds of researchers. BLOOM is a decoder-only Transformer language model that was trained on the ROOTS corpus: (Lauren¸con et al., 2022), a composite collection of 498 Hugging Face datasets (Lhoest et al., 2021) amounting to 1.61 terabytes of text that span 46 natural languages and 13 programming languages (59 total).
Although ALiBi was initially motivated by its ability to extrapolate to longer sequences, we found it also led to smoother training and better downstream performance even at the original sequence length – outperforming both learned (Vaswani et al., 2017) and rotary (Su et al., 2021) embeddings.
Although most modern language models are based on the Transformer architecture, there are significant deviations between architectural implementations. Notably, while the original Transformer is based on an encoder-decoder architecture, many popular models have opted for encoder-only (e.g. BERT, (Devlin et al., 2019)) or decoder-only (e.g. GPT, (Radford et al., 2018)) approaches. Currently, all state-of-the-art language models over 100 billion parameters are causal decoder-only models (Brown et al., 2020; Rae et al., 2021; Chowdhery et al., 2022). This is in opposition to the findings of Raffel et al. (2020), in which encoderdecoder models significantly outperform decoder-only models for transfer learning 
## Orca - 13B
[[2023-09-26-Tuesday]]
From Microsoft Research - [2306.02707.pdf](https://arxiv.org/pdf/2306.02707.pdf)
Fine-tuned Vicuna-13B (which was instruction finetuned on top of Lllama with ShareGPT - dataset collected from ChatGPT)

Orca, a 13-billion parameter model that learns to imitate the reasoning process of LFMs. Orca learns from rich signals from GPT-4 including explanation traces; step-by-step thought processes; and other complex instructions, guided by teacher assistance from ChatGPT. To promote this progressive learning, we tap into large-scale and diverse imitation data with judicious sampling and selection. Orca surpasses conventional state-of-the-art instruction-tuned models such as Vicuna-13B by more than 100% in complex zero-shot reasoning benchmarks.

Orca reaches parity with ChatGPT on the BBH benchmark and shows competitive performance (4 pts gap with optimized system message) in professional and academic examinations like the SAT, LSAT, GRE, and GMAT, both in zero-shot settings without CoT; while trailing behind GPT-4

![[orca-13b.png]]
We augment ⟨query, response⟩ pairs with detailed responses from GPT-4 that explain the reasoning process of the teacher as it generates the response. These provide the student with additional signals for learning. We leverage system instructions (e.g.., explain like I’m five, think step-by-step and justify your response, etc.) to elicit such explanations. This is in contrast to vanilla instruction tuning, which only uses the prompt and the LFM response for learning, providing little opportunity for mimicking the LFM’s “thought” process.

we use FLANv2, supplemented with high-quality templates, advanced formatting patterns, and data augmentations. Even though FLAN holds tens of millions of instructions, we selectively sample from the task collection to form a diverse mixture of tasks, which we then further sub-sample to generate complex prompts. These prompts are used to query LFMs like ChatGPT and GPT-4, thus creating a rich and diverse training set.

Instruction tuning [22] is a technique that allows pre-trained language models to learn from input (natural language descriptions of the task) and response pairs, for example, 
{"instruction": "Arrange the words in the given sentence to form a grammatically correct sentence.", "input": "the quickly brown fox jumped", "output": "the brown
fox jumped quickly"}. 
Instruction tuning has been applied to both language-only and multimodal tasks. 


## FLAN
[[2023-09-26-Tuesday]] -Stands for **F**inetuned **LA**nguage **N**et.

This is the paper that first introduced Instruction-Finetuning of LLMs : [Finetuned language models are zero-shot learners](https://arxiv.org/pdf/2109.01652.pdf)
This paper explores a simple method for improving the zero-shot learning abilities of language models. We show that instruction tuning—finetuning language models on a collection of datasets described via instructions—substantially improves zeroshot performance on unseen tasks.
We take a 137B parameter pretrained language model and instruction tune it on over 60 NLP datasets verbalized via natural language instruction templates. We evaluate this instruction-tuned model, which we call FLAN, on unseen task types. FLAN substantially improves the performance of its unmodified counterpart and surpasses zero-shot 175B GPT-3 on 20 of 25 datasets that we evaluate. FLAN even outperforms few-shot GPT-3 by a large margin on ANLI, RTE, BoolQ, AI2-ARC, OpenbookQA, and StoryCloze.

![[flan.png]]
![[flan-1.png]]

![[flan-2.png]]

To balance the different sizes of datasets, we limit the number of training examples per dataset to 30k
Because FLAN prompts are formulated as responding to an instruction, they do not work well for pretrained language models without finetuning. Performance was near zero for most generation tasks. For instance, given the input “‘The dog runs.’ Translate this sentence to French.”, LaMDA-PT continues with ”The dog runs after the cat” instead of actually translating the sentence. Hence, we used the established GPT-3 prompts for our LaMDA-PT baselines.

## Platypus
[[2023-09-26-Tuesday]] - [Platypus: Quick, Cheap, and Powerful Refinement of LLMs](https://arxiv.org/pdf/2308.07317.pdf)
Provides a good overview of the history & development of [[*shiny-fm-llm]] thus far.
13B Platypus model can be trained on a single A100 GPU using 25k questions in 5 hours. This is a testament of the quality of our Open-Platypus
dataset.
Our work centers around improving the performance of base Large Language Models (LLMs) by fine-tuning models using parameter efficient tuning (PEFT) on a small, yet powerful, curated dataset Open-Platypus.
Chinchillia [16] was introduced along with a novel scaling law approach that shifts the emphasis from model size to the number of processed tokens.
Shortly after the initial release of the 70B parameter [[*shiny-fm-llm#Llama2]] model was fine-tuned by StabilityAI to create StableBeluga2 [26] using an [[#Orca - 13B|Orca]]-style dataset [29].

Different from full fine-tuning methods, LoRA freezes pre-trained model weights and adds rank decomposition matrices into each layer of the transformer. This reduces the number of trainable parameters for downstream tasks and by extension, the time and cost of training. For example, our 13B model was fine-tuned using 1 A100 80GB for 5 hours and our 70B model using 4 A100s 80GB for 22 hours. As a benchmark for comparison, Stanford notes that their full fine-tune of Alpaca-7B took 3 hours on 8 A100s 80GB.

[GitHub - arielnlee/Platypus: Code for fine-tuning Platypus fam LLMs using LoRA](https://github.com/arielnlee/Platypus)
The Platypus models are a series of fine-tuned and merged variants based on the LLaMA and LLaMa-2 transformer architectures. Platypus takes advantage of [LoRA](https://arxiv.org/pdf/2106.09685.pdf) and [PEFT](https://github.com/huggingface/peft).
## llama-2-70b-dolphin 🦙🐬
[[2023-09-26-Tuesday]]
This instruction model was built via parameter-efficient QLoRA finetuning of [llama-2-70b](https://huggingface.co/meta-llama/Llama-2-70b-hf) on the first 25k rows of [ehartford/dolphin](https://huggingface.co/datasets/ehartford/dolphin) (an open-source implementation of [Microsoft's Orca](https://www.microsoft.com/en-us/research/publication/orca-progressive-learning-from-complex-explanation-traces-of-gpt-4/)). Finetuning was executed on a single H100 (80 GB PCIe) for roughly 17 hours on the [Lambda Labs](https://cloud.lambdalabs.com/instances) platform.

## Phi series
### phi-1_5
[[2023-09-27-Wednesday]] - [microsoft/phi-1\_5 · Hugging Face](https://huggingface.co/microsoft/phi-1_5) 
The language model phi-1.5 is a Transformer with **1.3 billion** parameters. It was trained using the same data sources as [phi-1](https://huggingface.co/microsoft/phi-1), augmented with a new data source that consists of various NLP synthetic texts. When assessed against benchmarks testing common sense, language understanding, and logical reasoning, phi-1.5 demonstrates a nearly state-of-the-art performance among models with less than 10 billion parameters.
One of the few models that is trained only on synthetic data.

### phi-3
- We introduce phi-3-mini, a 3.8 billion parameter language model trained on 3.3 trillion tokens - performance rivals that of models such as Mixtral 8x7B and GPT-3.5
- The innovation lies entirely in our dataset for training, a scaled-up version of the one used for phi-2, composed of heavily filtered web data and synthetic data. The model is also further aligned for robustness, safety, and chat format.
- We also provide some initial parameter-scaling results with a 7B and 14B models trained for 4.8T tokens, called phi-3-small and phi-3-medium, both significantly more capable than phi-3-mini
- **phi-3-small:** Standard decoder architecture; 7B; 32 layers and a hidden size of 4096. To minimize KV cache footprint, the model also leverages a grouped-query attention, with 4 queries sharing 1 key; leverages the tiktoken tokenizer (for better multilingual tokenization) with a vocabulary size of 100352 and has default context length 8K
- **phi-3-mini:** 3.8B parameters; 4K context length; vocab size = 320064; 3072 hidden dimension, 32 heads and 32 layers. We trained using bfloat16 for a total of 3.3T tokens.
- The model simply does not have the capacity to store too much “factual knowledge”, which can be seen for example with low performance on TriviaQA.
## OpenOrca-Platypus2-13B
[[2023-10-03-Tuesday]]
[Open-Orca/OpenOrca-Platypus2-13B · Hugging Face](https://huggingface.co/Open-Orca/OpenOrca-Platypus2-13B)
OpenOrca-Platypus2-13B is a merge of [`garage-bAInd/Platypus2-13B`](https://huggingface.co/garage-bAInd/Platypus2-13B) and [`Open-Orca/OpenOrcaxOpenChat-Preview2-13B`](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B)
first 13B model to score higher than LLaMA1-65B on the HuggingFace Leaderboard
Trained on the following two datasets:
- `garage-bAInd/Platypus2-13B` : STEM and logic based dataset [`garage-bAInd/Open-Platypus`](https://huggingface.co/datasets/garage-bAInd/Open-Platypus). Please see our [paper](https://arxiv.org/abs/2308.07317) and [project webpage](https://platypus-llm.github.io/) for additional information.
- `Open-Orca/OpenOrcaxOpenChat-Preview2-13B` : Refined subset of most of the GPT-4 data from the [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca).

## Mistral AI
### Mistral-7B
[[2023-10-11-Wednesday]] 
[2310.06825.pdf](https://arxiv.org/pdf/2310.06825.pdf)
Mistral 7B, a 7–billion-parameter language model engineered for
superior performance and efficiency. Mistral 7B outperforms the best open 13B
model (Llama 2) across all evaluated benchmarks, and the best released 34B
model (Llama 1) in reasoning, mathematics, and code generation. 
Mistral 7B leverages grouped-query attention (GQA) [1], and sliding window attention (SWA) [6, 3]. GQA significantly accelerates the inference speed, and also reduces the memory requirement during decoding, allowing for higher batch sizes hence higher throughput, a crucial factor for real-time applications. In addition, SWA is designed to handle longer sequences more effectively at a reduced computational cost, thereby alleviating a common limitation in LLMs. 
![[shiny-fm-llm-2023-10-11.png]]
Sliding Window Attention. The number of operations in vanilla attention is quadratic in the sequence length, and the memory increases linearly with the number of tokens. At inference time, this incurs higher latency and smaller throughput due to reduced cache availability. To alleviate this issue, we use sliding window attention: each token can attend to at most W tokens from the previous layer (here, W = 3). Note that tokens outside the sliding window still influence next word prediction. At each attention layer, information can move forward by W tokens. Hence, after k attention layers, information can move forward by up to k × W tokens.

*From Xin: I think their message is that "We trained a better foundation model. You can do whatever (Orca/Platypus/UC) you did on LLaMA-2 now on Mistral instead."*

### Mixtral-7B
[[2023-12-12-Tuesday]] - New hotness
![[shiny-fm-llm-2023-12-12.png]]
Good video describing it: [Mistral 8x7B Part 2- Mixtral Updates - YouTube](https://www.youtube.com/watch?v=gCD8bsI6Du4)
We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model. Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts). For every token, at each layer, a router network selects two experts to process the current state and combine their outputs. Even though each token only sees two experts, the selected experts can be different at each timestep. As a result, each token has access to 47B parameters, but only uses 13B active parameters during inference. Mixtral was trained with a context size of 32k tokens and it outperforms or matches Llama 2 70B and GPT-3.5 across all evaluated benchmarks. In particular, Mixtral vastly outperforms Llama 2 70B on mathematics, code generation, and multilingual benchmarks. We also provide a model finetuned to follow instructions, Mixtral 8x7B – Instruct, that surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B – chat model on human benchmarks.
The memory costs for serving Mixtral are proportional to its sparse parameter count, 47B, which is still smaller than Llama 2 70B.
As a sparse Mixtureof-Experts model, Mixtral only uses 13B active parameters for each token. With 5x lower active parameters, Mixtral is able to outperform Llama 2 70B across most categories.

### Magistral 
[Magistral ](https://mistral.ai/news/magistral) - the first reasoning model by Mistral AI

### Voxtral 
new transcription model that "comprehensively outperforms Whisper large-v3" and "beats GPT-4o mini Transcribe and Gemini 2.5 Flash across all tasks":
Built-in Q&A and summarization: Supports asking questions directly about the audio content or generating structured summaries, without the need to chain separate ASR and language models
Long context: with a 32k token context length, Voxtral handles audios up to 30 minutes for transcription, or 40 minutes for understanding
Highly capable at text: Retains the text understanding capabilities of its language model backbone, Mistral Small 3.1

## Phi-2
[[2023-12-18-Monday]] - From Microsoft. 3B and trained on textbooks data. Apparently very powerful SLM
[TheBloke/phi-2-GGUF · Hugging Face](https://huggingface.co/TheBloke/phi-2-GGUF)

## Code Llama 70B
Code Llama 70B, a leap in open-source code generation models, surpassing GPT-4 with a HumanEval score of 67.8. Building on Llama 2's architecture, Code Llama 70B, a large language model (LLM), specializes in code-related tasks, offering enhanced code generation and natural language understanding of code.
Trained on 1TB tokens of code and code-related data, setting a new standard in the field. It's designed to generate code from text prompts, supporting popular programming languages like Python, C++, and Java, and is especially proficient in Python, owing to additional fine-tuning on 100B tokens of Python code.
This model offers three versions: a foundational code model, a Python-specific model, and an Instruct model fine-tuned for natural language instructions.
Available in 7B and 13B variants.

## Gemini series
### Gemini Ultra
[[2024-02-15-Thursday]] - 
### Gemini 1.5
[[2024-02-15-Thursday]] - [Introducing Gemini 1.5, Google's next-generation AI model](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#gemini-15)
1M tokens context window - largest ever so far. Previous was Claude with 200k tokens.

### Gemini 2
[[2024-12-12-Thursday]] - made a big buzz: [Google introduces Gemini 2.0: A new AI model for the agentic era](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/#project-astra)
Playground: [Site Unreachable](https://aistudio.google.com/prompts/new_chat)
![[gemini_2_api.ipynb]]

## xAI
### Grok-1
[[2024-03-18-Monday]]: With 314-billion parameters, the Mixture of Experts (MoE) model utilizes 86 billion active parameters at any given time, enhancing its processing capabilities - largest open LLM ever built

Key Specifications:
- **Parameters**: 314 billion, with 25% of weights active per token.
- **Architecture**: Mixture of 8 Experts, using 2 per token.
- **Layers**: 64 transformer layers, integrating multihead attention and dense blocks.
- **Tokenization**: Utilizes a SentencePiece tokenizer, vocab size of 131,072.
- **Embedding and Positional Encoding**: 6,144 embedding size, matching rotary positional embeddings.
- **Attention**: 48 heads for queries, 8 for keys/values, each with a size of 128.
- **Context Length**: Capable of processing 8,192 tokens with bf16 precision.
Performance Metrics:
- Outperforms LLaMa 2 70B and Mixtral 8x7B with a MMLU score of 73%, showcasing its efficiency and accuracy in various tests.

### Grok-4
[[2025-07-10-Thursday]] - Rumored to be [2.4T params](https://41598e5c38d3cd55e335e985614d0883.us-east-1.resend-links.com/CL0/https:%2F%2Fx.com%2Fkalomaze%2Fstatus%2F1942996555088134592%3Fs=46/1/01000197f6bb16e1-ba4790eb-ab2e-4436-b674-04cdff982e59-000000/I35v9rBz6IZK9VyFE7xHxz33NxDvXoE5KXpunuuSAdY=413) (the second released >2T model after 4 Opus?)
## Cohere
### Command-R and Command-R+
[[2024-04-10-Wednesday]]
[Introducing Command R+: A Scalable LLM Built for Business](https://txt.cohere.com/command-r-plus-microsoft-azure/)
Just another llm that works well with long context windows 128k and especially for RAG applications. Targeted towards Enterprise customers and can be paired with their Embed and Rank models for even better RAG.

### Command A Reasoning
[[2025-08-22-Friday]] Apparently better than [[#gpt-oss 20b and 120b]]

## Mixtral 8x22B
[[2024-04-15-Monday-W16|2024-04-17-Wednesday]] - [Blog post](https://mistral.ai/news/mixtral-8x22b/)
Mixtral 8x22B is a natural continuation of our open model family. Its sparse activation patterns make it faster than any dense 70B model, while being more capable than any other open-weight model

> [!NOTE] Apparently pretty good at function calling natively - would be interesting to use it for synthetic datagen in [[archive/apple/attentionkit-fc]]

![[shiny-fm-llm-2024-04-17.png]]

## Llama-3
[[2024-04-15-Monday-W16|2024-04-18-Thursday]]
[Meta Llama 3](https://llama.meta.com/llama3/)
15T token of data – a training dataset 7x larger than that used for Llama 2, including 4x more code.
7B and 80B versions
Compared to Llama 2, we made several key improvements. Llama 3 uses a tokenizer with a vocabulary of 128K tokens that encodes language much more efficiently, which leads to substantially improved model performance. To improve the inference efficiency of Llama 3 models, we’ve adopted grouped query attention (GQA) across both the 8B and 70B sizes. We trained the models on sequences of 8,192 tokens, using a mask to ensure self-attention does not cross document boundaries.

## Phi-3
[[2024-04-24-Wednesday]] - [\[2404.14219\] Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219)
- Designed to run on mobile devices
- The mini model is particularly optimized for mobile use, requiring only about 1.8GB when compressed to 4-bits and efficiently processing over 12 tokens per second on mobile devices like the iPhone 14.
- three sizes: mini (3.8 billion parameters), small (7 billion parameters), and medium (14 billion parameters).
- Each model uses the same tokenizer as the Llama-2, ensuring compatibility with existing packages.
- ![[shiny-fm-llm-2024-04-24.png]]


## OpenELM - Apple 
[[2024-04-29-Monday-W18|2024-04-29-Monday]]
- OpenELM models were trained on 1.8T tokens from datasets like RefinedWeb, deduplicated PILE, RedPajama subset, and Dolma v1.6 subset.
- Both pre-trained and instruction-tuned checkpoints are available for all four model sizes (270M, 450M, 1.1B, 3B).
- On ARC-C, MMLU, and HellaSwag benchmarks, the largest 3B model scored 42.24%, 26.76%, and 73.28% respectively.

## DeepSeek
### DeepSeek-V2
[[2024-05-06-Monday-W19|2024-05-09-Thursday]] - Open-source MoE model that places top 3 in AlignBench, surpassing GPT-4. It has 236B parameters with 21B activated during generation.

### DeepSeek-V3 & R1
- [DeepSeek-V3](https://api-docs.deepseek.com/news/news1226) : their answer to GPT-4o and Claude3.5 Sonnet 
	- 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities
- [DeepSeek-R1](https://api-docs.deepseek.com/news/news250120) : their answer to OpenAI's O1 model
Key innovations: (pulled from [here](https://youtubetranscriptoptimizer.com/blog/05_the_short_case_for_nvda))
- sophisticated **mixed-precision training framework** that lets them use 8-bit floating point numbers (FP8) throughout the entire training process
- **multi-token prediction system** - Most Transformer based LLM models do inference by predicting the next token— one token at a time. DeepSeek figured out how to predict multiple tokens while maintaining the quality you'd get from single-token prediction.
- **Multi-head Latent Attention (MLA**) - finds a way to store a compressed version of KV indices that captures the essential information while using far less memory. entire compression mechanism is "differentiable" and able to be trained directly using the standard optimizers.
- major advances in **GPU communication efficiency** through their DualPipe algorithm and custom communication kernels.
- **Mixture-of-Experts (MOE)** Transformer architecture, but with key innovations around load balancing
	- DeepSeek-V3 - absolutely massive MOE model with 671B parameters but only 37B of these parameters are active at any given time— enough to fit in the VRAM of two consumer-grade Nvidia 4090 GPUs (under $2,000 total cost)
- novel approach to **reward modeling**. Rather than using complex neural reward models that can lead to "reward hacking" (where the model finds bogus ways to boost their rewards that don't actually lead to better real-world model performance), they developed a clever rule-based system that combines accuracy rewards (verifying final answers) with format rewards (encouraging structured thinking).
~45x efficiency improvement in training
their 14B parameter version outperforms many models several times its size, suggesting that reasoning ability isn't just about raw parameter count but about how you train the model to process information.

### DeepSeek-R1 paper
**Post-Training: Large-Scale Reinforcement Learning on the Base Model**
- We directly apply RL to the base model without relying on supervised fine-tuning (SFT) as a preliminary step. This approach allows the model to explore chain-of-thought (CoT) for solving complex problems, resulting in the development of DeepSeek-R1-Zero. DeepSeekR1-Zero demonstrates capabilities such as self-verification, reflection, and generating long CoTs
- We introduce our pipeline to develop DeepSeek-R1. The pipeline incorporates two RL stages aimed at discovering improved reasoning patterns and aligning with human preferences, as well as two SFT stages that serve as the seed for the model’s reasoning and non-reasoning capabilities.
*DeepSeek-R1-Zero is just RL finetuned without any supervised finetuning step because collecting SFT data is labor intensive.*
*DeepSeek-R1 is first RL finetuned with some CoT cold start data before going full RL on it*
For distilled models, we apply only SFT and do not include an RL stage, even though incorporating RL could substantially boost model performance.

### DeepSeek V3.1(Think/Non-Think hybrid)**
Unified model that can toggle between “reasoning” and “non-reasoning” via <think></think> tokens, with an explicit push toward agentic use cases and coding workflows. Unlike earlier versions focused on raw reasoning benchmarks, V3.1 is designed to power autonomous workflows, enabling agents that can plan, call tools, and execute long multi-step tasks.   
The launch reflects a broader industry move away from static chatbots toward **general-purpose reasoning systems** built to act, not just answer.
128k context window; Anthropic compatible API
671B parameters (37B active per token).
## Qwen
[[2024-09-30-Monday]] - [Qwen2.5: A Party of Foundation Models! | Qwen](https://qwenlm.github.io/blog/qwen2.5/)
**131,072 context** size.
**Qwen-2.5-Coder** : - The final training dataset comprises 70% code, 20% text, and 10% math data, totaling 5.2 trillion tokens.
### Qwen 2.5 Omni 7B
First omni model from Qwen
[Qwen2.5-Omni-7B: Voice Chat + Video Chat! Powerful New Opensource end-to-end multimodal model - YouTube](https://www.youtube.com/watch?v=yKcANdkRuNI)
![[shiny-fm-llm-2025-03-28.png]]
## Gemma Series
### Gemma-2
[[2024-06-30-Sunday]] : Gemma 2 in 9B and 27B parameter sizes, trained on 13T tokens (27B) and 8T tokens (9B). Uses **SFT, Distillation, RLHF & Model Merging**. Trained on Google TPUv5e. Apparently beats Llama-70B in LMSYS

### Gemma3
[[2025-03-13-Thursday]] - Creating a lot of buzz today - just behind DeepSeek-R1 in ELO scores - [paper](https://arxiv.org/pdf/2503.19786)
Gemma 3 introduces a SigLIP vision encoder for image processing, extends context size to 128K tokens, and optimizes memory usage by interleaving local and global attention layers. It also incorporates a novel post-training approach to enhance performance in math, reasoning, coding, and multilingual abilities. Knowledge distillation is used to improve efficiency.
- 1B, 4B, 12B, and 27B parameters for different deployment needs.  
- 2T, 4T, 12T, and 14T training tokens, depending on model size.
Support RoPE embedding upto 1M context window size


## Nemotron family

### Nemotron-4-340B-Base
[nvidia/Nemotron-4-340B-Reward · Hugging Face](https://huggingface.co/nvidia/Nemotron-4-340B-Reward), [Technical Report](https://arxiv.org/pdf/2406.11704)
Release Nemotron-4-340B-Base, Nemotron-4- 340B-Instruct and Nemotron-4-340B-Reward (used in RLHF for alignment and can be used for synthetic datagen)
Nemotron-4-340B-Reward consists of the Nemotron-4-340B-Base model and a linear layer that converts the final layer representation of the end-of-response token into five scalar values, each corresponding to a HelpSteer2 attribute.
Similar in architecture to Nemotron-4-15B-Base. It is a standard decoder-only Transformer architecture, with causal attention masks, uses Rotary Position Embeddings (RoPE), SentencePiece tokenizer, and squared ReLU activations in the MLP layers. It has no bias terms, has dropout rate of zero, and untied input-output embeddings. We also use grouped query attention (GQA)
![[shiny-fm-llm-2024-09-19.png]]

### Nemotron 70B

Nvidia Nemotron 70B - beats Llama 3.1 405B, GPT4o & Claude 3.5 Sonnet on Arena Hard, AlpacaEval and MT Bench. They release the Instruct model, reward model and the dataset all on Hugging Face

## Moshi
From Kyutai Labs - [paper](https://kyutai.org/assets/pdfs/Moshi.pdf)
Try it on [https://moshi.chat](https://t.co/5QaFspEMkj) or even locally on your Apple Silicon Mac with just: 
$ pip install moshi_mlx 
$ python -m moshi_mlx.local_web -q 4

Trained on **3,000 hours** of speech data, can perform **voice conversion** and **speech enhancement** tasks

- Helium, a 7B-parameter text LLM that we pretrain on 2.1T tokens of public English data.
- Mimi, a neural audio codec that converts audio into the discrete tokens predicted by Moshi and back, using residual vector quantization (RVQ)
- Moshi, a new architecture for audio language modeling, which combines Helium with a smaller Transformer  model to predict audio tokens in a hierarchical and streaming fashion

*Neural audio codecs usually have semantic (words & meanings) and acoustic (emotions, expressivity, intonation) tokens*
Mimi’s encoder projects a 24kHz waveform to a latent representation of 12.5 frames per second and dimension D = 512. Symmetrically, the decoder adopts a similar structure but with transposed convolutions rather than strided ones, to project the latent representation back to 24kHz audio.
![[shiny-fm-llm-2025-03-05.png]]
*Mimi is trained like an autoencoder with reconstruction loss. WavLM helps align it in the semantic sense by making sure the audio tokens make sense in terms of the words they capture. The ConvNet + Transformer seems like a streaming model that takes in a 512 dimensional token and outputs a VQ (vector quantizer). The RVQ is like a history vector that this model outputs*

## Amazon Nova
### [Introducing Amazon Nova Act \| Amazon AGI Labs](https://labs.amazon.science/blog/nova-act) 
[[2025-04-01-Tuesday]] Computer use model that is apparently better than Claude. OpenAI also has one they launched

## HuggingFace
### SmolLM-2

![[*shiny-fm-llm-2025-04-08.png]]

We trained 1.7B parameter Transformers based on the Llama architecture, with a sequence length of 2048, a global batch size of approximately 2 million tokens, the GPT-2 tokenizer, and a cosine learning rate schedule with a learning rate of 3.0 × 10−4

SmolLM2-360M (360M parameters, trained on 4T tokens) and SmolLM2-135M (135M parameters, trained on 2T tokens), which are similarly state-of-the-art in their
size class.

Introduces 3 new datasets: FineMath, Stack-Edu, and SmolTalk (for mathematics, code, and instruction-following respectively).
-  FineMath, a collection of up to 54B tokens of math data focusing on mathematical deduction and reasoning through classifier-based filtering
- FineWeb-Edu consists of 1.3T tokens that were deemed “educational” by a classifier trained on annotations generated by Llama3-70B-Instruct
-  SmolTalk2, a new instruction-following dataset that carefully combines selected existing datasets with new synthetic datasets we developed, including the Magpie-Ultra conversational dataset as well as other specialized datasets that address specific capabilities like Smol-Constraint, Smol-Rewrite, and Smol-Summarization.
- 

Uses DPO for finetuning [[*ongoing/smol-course]]

![[*shiny-fm-llm-2025-04-08-1.png]]

### SmolLM3
[SmolLM3: smol, multilingual, long-context reasoner](https://huggingface.co/blog/smollm3)

- GQA matches the performance of multi-head attention while significantly reducing the KV cache size during inference
- After the main pretraining, we trained SmolLM3 on an additional 100B tokens to extend its context length.

![[*shiny-fm-llm-smol-lm3-2025-07-14.png]]

---

## Moonshot AI
**Kimi K2 (1T MoE) Open-Weights Release**: **Moonshot AI** has released **Kimi K2**, a **1 trillion** parameter (**32B** active) Mixture-of-Experts model with an **MIT license**. The model was trained on **15.5 trillion tokens** with zero training instability using the **MuonClip** optimizer
Better base model than [[#DeepSeek-V3 & R1]]


## Genie series
World Models for simulations
[Genie 3: A new frontier for world models - Google DeepMind](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)


## Apple Foundation Models
 (i) a∼3B-parameter on-device model optimized for Apple silicon through architectural innovations such as KV-cache sharing and 2-bit quantization-aware training; and (ii) a scalable server model built on a novel Parallel-Track Mixture-of-Experts (PT-MoE) transformer that combines track parallelism, mixture-of-experts sparse computation, and interleaved global–local attention to deliver high quality with competitive cost on Apple’s Private Cloud Compute platform.
 
Nothing too novel other than the Parallel Track MoE model. which runs several little transformers in parallel and then synchronizes their results. Within each block are MoE layers.
![400](attachments/*shiny-fm-llm-2025-09-11-1.png)
Follow the same recipe of Pre-Training -> SFT -> RLHF using REINFORCE -> Tool use RL
The RL pipeline looks very much like a robotics on-policy pipeline where trajectories are rolled out and reward is computed for it and then stored in a replay buffer. Different than the DPO & PPO like RL I have been seeing lately that just picks or ranks different generations. Honestly I dont quite fully understand it either.

![500](attachments/*shiny-fm-llm-2025-09-11.png)

On device 3B model is trained with quantization aware training and compressed down to 2 bit. The server side model also has some weird adaptive quantization.

Provides a @Generable macro in swift that is fed in to the model prompt for structured contrained generation. It makes sure that the model produces an output that can translate into the datastruct in swift that has been annotated with the macro. Some post training is done for constrained data structure generation.

# Interesting Papers

## RoPE
[[2023-09-20-Wednesday]]
[RoPE (Rotary positional embeddings) explained: The positional workhorse of modern LLMs - YouTube](https://www.youtube.com/watch?v=GQPOtyITy54)
Alternative to sinusoidal positional embeddings (from the original transformers paper). It provides a much better behaved positional embedding because it does not smash the token embedding with the position embedding into one thing. Instead it multiples the token embeddings with a rotational position embedding using a 2D block rotation matrix. This enables the sequence length for LLMs to be longer than their training lengths. Another approach is AliBi

## AliBi
[[2023-09-20-Wednesday]]
[ALiBi - Train Short, Test Long: Attention with linear biases enables input length extrapolation - YouTube](https://www.youtube.com/watch?v=-Kgxv64aG3o)
Another way to compute positional embeddings
![[shiny-fm-llm-2023-09-20.png]]

## Are Emergent Abilities in Large Language Models just In-Context Learning?
[[2023-10-04-Wednesday]] - [2309.01809.pdf](https://arxiv.org/pdf/2309.01809.pdf)

## TinyStories : How Small Can Language Models Be and Still Speak Coherent English?
[[2023-10-11-Wednesday]] - [2305.07759.pdf](https://arxiv.org/pdf/2305.07759.pdf)
TinyStories , a synthetic dataset of short stories that are intended to contain only words that most 3 to 4-year-old children would typically understand, generated by GPT-3.5 and GPT-4. TinyStories is designed to capture the essence of natural language, while reducing its breadth and diversity. Each story consists of 2-3 paragraphs that follow a simple plot and a consistent theme, while the whole dataset aims to span the vocabulary and the factual knowledge base of a 3-4 year old child

We also introduce a new paradigm for the evaluation of language models: We suggest a framework which uses GPT-4 to grade the content generated by these models as if those were stories written by students and graded by a (human) teacher. This new paradigm overcomes the flaws of standard benchmarks which often require the model’s output to be very structured, and moreover it provides a multidimensional score for the model, providing scores for different capabilities such as grammar, creativity and instruction-following.

We hope that TinyStories can facilitate the development, analysis and research of LMs, especially for low resource or specialized domains, and shed light on the emergence of language capabilities in LMs.
Ó
Our main contribution is that we show TinyStories can be used to train and evaluate SLMs2 that are much smaller than the state-of-the-art models (below 10 million parameters with an embedding dimension of 256), or have much simpler architectures (with only one transformer block), yet still produce a diverse set of fluent and consistent stories that are comparable or superior to those generated by larger and more complex models. Moreover, despite of the small size of the models, we still observe an emergence of reasoning capabilities, knowledge of general facts and ability to follow certain instructions.

We show that the trained SLMs appear to be substantially more interpretable than larger ones. When models have a small number of neurons and/or a small number of layers, we observe that both attention heads and MLP neurons have a meaningful function: Attention heads produce very clear attention patterns, with a clear separation between local and semantic heads, and MLP neurons typically activated on tokens that have a clear common role in the sentence. 

We also see that the largest model that we have trained on TinyStories (with roughly 80M parameters) reaches almost perfect scores in terms of grammar and consistency. However, it falls short of GPT-4’s abilities in terms of creativity quite significantly, suggesting that creativity continues to improve more substantially with the sizes of the model and dataset, compared to grammar and consistency

## Soft Prompts / Prompt Tuning
[Guiding Frozen Language Models with Learned Soft Prompts – Google Research Blog](https://blog.research.google/2022/02/guiding-frozen-language-models-with.html)
To create a soft prompt for a given task, we first initialize the prompt as a fixed-length sequence of vectors (e.g., 20 tokens long). We attach these vectors to the beginning of each embedded input and feed the combined sequence into the model. The model’s prediction is compared to the target to calculate a loss, and the error is back-propagated to calculate gradients, however we only apply these gradient updates to our new learnable vectors — keeping the core model frozen. While soft prompts learned in this way are not immediately interpretable, at an intuitive level, the soft prompt is extracting evidence about how to perform a task from the labeled dataset, performing the same role as a manually written text prompt, but without the need to be constrained to discrete language.
![[shiny-fm-llm-2024-01-20.png]]


## ASPIRE
After sampling high-likelihood outputs for each query, ASPIRE adds adaptable parameters (θs) and only fine-tunes θs for learning self-evaluation. Since the output sequence generation only depends on θ and θp, freezing θ and the learned θp can avoid changing the prediction behaviors of the LLM when learning self-evaluation. We optimize θs such that the adapted LLM can distinguish between correct and incorrect answers on their own.
Uses [[#Soft Prompts / Prompt Tuning]] to fine tune the model.
Our experimental journey with ASPIRE underscores a pivotal shift in the landscape of LLMs: The capacity of a language model is not the be-all and end-all of its performance. Instead, the effectiveness of models can be drastically improved through strategic adaptations, allowing for more precise, confident predictions even in smaller models. As a result, ASPIRE stands as a testament to the potential of LLMs that can judiciously ascertain their own certainty and decisively outperform larger counterparts in selective prediction tasks.
![[shiny-fm-llm-2024-01-20-2.png]]
![[shiny-fm-llm-2024-01-20.gif]]

## Can Generalist Foundation Models Outcompete Special-Purpose Tuning? - MedPrompt
[[2024-03-06-Wednesday]] - [2311.16452.pdf](https://readwise-assets.s3.amazonaws.com/media/wisereads/articles/can-generalist-foundation-mode/2311.16452.pdf)
We find that prompting innovation can unlock deeper specialist capabilities and show that GPT-4 easily tops prior leading results for medical question-answering datasets.
We introduce Medprompt, based on a composition of several prompting strategies. Medprompt greatly enhances GPT-4’s performance and achieves state of the art results on all nine of the benchmark datasets in the MultiMedQA suite. The method outperforms state-ofthe-art specialist models such as Med-PaLM 2 by a large margin with an order of magnitude fewer calls to the model.
 We discover that a combination of methods, including in-context learning and chain-of-thought, can yield synergistic effects. We find that GPT-4 benefits significantly from being allowed to design its prompt, specifically with coming up with its own chain-of-thought to be used for in-context learning. This observation echoes other reports that GPT-4 has an emergent self-improving capability via introspection, such as self-verification
 
 Key prompting strategies they applied:
 - Dynamic few-shot:  Given a test example, we choose k training examples that are semantically similar using a k-NN clustering in the embedding space to pass as few shot examples
 - Self-generated chain of thought: Simply ask GPT-4 to generate a rationale before answering the question. “Let’s think step by step,”  - this approach has been found to significantly improve the ability of foundation models to perform complex reasoning.
 - Choice shuffling ensemble: takes care of position bias in LLMs by shuffling choices and then select the consistent answer - ie the one least sensitive to the relative order. Choice shuffling has an additional benefit of increasing the diversity of each reasoning path beyond temperature sampling, thereby also improving the quality of the final ensemble

> [!Tldr] 
> interesting approach when runtime inference latency is not a concern because the prompt generation is an intensive step. Finetuning & distilling would be better for quick generation if the use case is constrained to specific domains

## LLMLingua
Presenting at [[j595 tasks]] literature review [[J595 Literature Review - LLMLingua.key]]

[(Long)LLMLingua | Designing a Language for LLMs via Prompt Compression](https://llmlingua.com/#rag)

[LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models](https://arxiv.org/pdf/2310.05736.pdf)
 LLMLingua, a coarse-to-fine prompt compression method that involves a budget controller to maintain semantic integrity under high compression ratios, a token-level iterative compression algorithm to better model the interdependence between compressed contents, and an instruction tuning based method for distribution alignment between language models.
 up to 20x compression with little performance loss.
grounded in the concept that natural language is inherently redundant (Shannon, 1951) and thus can be compressed.
 validate the effectiveness of our approach on four datasets from different domains, i.e., GSM8K and BBH for reasoning and ICL, ShareGPT for conversation, and Arxiv-March23 for summarization.
 ![[shiny-fm-llm-2024-01-17.png]]
 Split the prompt into: instruction, demonstrations and question
 3 components: budget controller, iterative token-level prompt compression & distribution alignment between compressor llm and blackbox llm.
 In this paper, we employ the GPT-3.5-Turbo-0301 and the Claude-v1.3 as the target LLMs, which can be accessed via OpenAI2 and Claude API3 . To improve the stability of outputs produced by LLMs we apply greedy decoding with a temperature of 0 across all experiments. The Alpaca dataset (Taori et al., 2023) is exclusively employed for aligning small language models with black-box LLMs, and is not utilized in the evaluation process. In our experiments, we utilize either Alpaca-7B4 or GPT2-Alpaca as the small pre-trained language model M𝑠 for compression
 Experiments with recovering the prompt using GPT-4
 Pretty badly written paper overall
 
[LongLLMLingua: Accelerating and Enhancing Llms in Long Context Scenarios via Prompt Compression](https://arxiv.org/pdf/2310.06839.pdf)

Builds on top of LLMLingua and makes the compression question-aware.
main contributions are five-fold: (1) We propose a question-aware coarse-to-fine compression method to improve the key information density in the prompt (Sec. 4.1); (2) We introduce a document reordering mechanism to reduce information loss in the middle. (Sec. 4.2); (3) We present dynamic compression ratios to bridge the coarse-grained compression and fine-grained compression for adaptive granular control (Sec. 4.3); (4) We propose a post-compression subsequence recovery strategy to improve the integrity of the key information (4.4). (5) We evaluate LongLLMLingua on three benchmarks, i.e., NaturalQuestions (Liu et al., 2023), LongBench (Bai et al., 2023), and ZeroSCROLLS (Shaham et al., 2023). 

![[shiny-fm-llm-2024-01-17-1.png]]

## HuggingGPT / JARVIS
[GitHub - microsoft/JARVIS: JARVIS, a system to connect LLMs with ML community. Paper: https://arxiv.org/pdf/2303.17580.pdf](https://github.com/microsoft/JARVIS?tab=readme-ov-file) [Paper](https://arxiv.org/pdf/2303.17580.pdf) 
![[shiny-fm-llm-2024-03-22.png]]
Interesting approach: pretty much LLMs with function calling into HuggingFace models
The principle of our system is that an LLM can be viewed as a controller to manage AI models, and can utilize models from ML communities like Hugging Face to automatically solve different requests of users.

## 1-bit LLMs

### [BitNet: Scaling 1-bit Transformers for Large Language Models](https://arxiv.org/pdf/2310.11453.pdf)
Goodnotes: [[BitNet.pdf]]

In this work, we introduce BitNet, a scalable and stable 1-bit Transformer architecture designed for large language models. Specifically, we introduce BitLinear as a drop-in replacement of the nn.Linear layer in order to train 1-bit weights from scratch. Experimental results on language modeling show that BitNet achieves competitive performance while substantially reducing memory footprint and energy consumption, compared to state-of-the-art 8-bit quantization methods and FP16 Transformer baselines. Furthermore, BitNet exhibits a scaling law akin to full-precision Transformers, suggesting its potential for effective scaling to even larger language models while maintaining efficiency and performance benefits.

Recently, there has been some research on binarized Transformers. However, these studies have focused on machine translation or BERT pretraining, which is quite different from large language models. For example, machine translation employs an encoder-decoder architecture, BERT pretraining utilizes a bidirectional encoder, and large language models use a unidirectional decoder. Furthermore, large language models are typically scaled up to a much larger model size, while BERT and machine translation models do not undergo such extensive scaling.

Most existing quantization approaches for large language models are post-training. They are simple and easy to apply since it does not require any changes to the training pipeline or retraining the model. However, it will result in a more significant loss of accuracy especially when the precision goes lower, because the model is not optimized for the quantized representation during training. 

We propose BitNet, a 1-bit Transformer architecture for large language models, which aims to scale efficiently in terms of both memory and computation. BitNet employs low-precision binary weights and quantized activations, while maintaining high precision for the optimizer states and gradients during training. Our approach is designed to be scalable and stable, with the ability to handle large language models efficiently.

### [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits](https://arxiv.org/pdf/2402.17764.pdf)
[Goodnotes](https://share.goodnotes.com/s/ZTTqtKOjzpjDLXbfjlZhTy) : [[Era Of 1-bit LLMs.pdf]] 

Nous Research replicated these results: [NousResearch/OLMo-Bitnet-1B · Hugging Face](https://huggingface.co/NousResearch/OLMo-Bitnet-1B) 70B model with 24GB VRAM

## Mixture of Depth (MoD) Deepmind
[[2024-04-10-Wednesday]] - [2404.02258.pdf](https://arxiv.org/pdf/2404.02258.pdf)
	Not all problems require the same amount of time or effort to solve. Analogously, in language modeling not all tokens and sequences require the same time or effort to accurately make a prediction. And yet, transformer models expend the same amount of compute per token in a forward pass. Ideally, transformers would use smaller total compute budgets by not spending compute unnecessarily.

> [!NOTE] Pretty neat idea  - might start getting combined with Mixture of Experts in SoTA LLMs

![[shiny-fm-llm-2024-04-10.png]]
	We leverage an approach akin to Mixture of Experts (MoE) transformers, in which dynamic token-level routing decisions are made across the network depth. Departing from MoE, we choose to either apply a computation to a token (as would be the case for a standard transformer), or pass it through a residual connection (remaining unchanged and saving compute). Also in contrast to MoE, we apply this routing to both forward MLPs and multi-head attention. Since this therefore also impacts the keys and queries we process, the routing makes decisions not only about which tokens to update, but also which tokens are made available to attend to. We refer to this strategy as Mixture-of-Depths (MoD) to emphasize how individual tokens pass through different numbers of layers, or blocks, through the depth of the transformer
Authors also make an observation that the cost of attention for those layers decreases quadratically, so this could be an interesting way of making ultra long context length much faster. There's no impact at training time, but can be "upwards of 50% faster" per forward pass. The authors also demonstrate how MoD can be combined with MoE (eg by having a no-op expert) to decouple the routing for queries, keys, and values:
![[shiny-fm-llm-2024-04-10-1.png]]

## ReALM: Reference Resolution As Language Modeling
[[2024-04-15-Monday-W16|2024-04-17-Wednesday]] - [2403.20329.pdf](https://arxiv.org/pdf/2403.20329.pdf)
There thus continues to be utility in exploring "traditional" NLP tasks such as reference resolution, despite some of the larger language models being able to handle them implicitly. In this work, we thus advocate the use of (relatively) smaller language models, but fine-tuned for specifically and explicitly for the task of reference resolution.
In this work, we propose reconstructing the screen using parsed entities and their locations to generate a purely textual representation of the screen that is visually representative of the screen content. The parts of the screen that are entities are then tagged, so that the LM has context around where entities appear, and what the text surrounding them is (Eg: call the business number).
We pose the task of reference resolution as a multiple choice task for the LLM, where the intended output is a single option (or multiple options) from the entities shown on the user’s screen.

> [!NOTE] This LLM task formulation seems very similar to how [[archive/apple/attentionkit-fc]] is formulated
> 

While our approach is effective in encoding the position of entities on the screen, we find that it results in loss of information that may not be able to resolve complex user queries that rely on nuanced positional understanding. We thus believe that exploring more complex approaches such as splitting the screen into a grid and encoding these relative spatial positions into text, while challenging, is a promising avenue of future exploration.

> [!tldr] Finetuned a FLAN-T5 of different sizes for the reference resolution task
> This also potentially indicates that finetuning [[archive/apple/attentionkit-fc]] models is a good idea rather than always relying on a big model

## Karpathy - [\[1hr Talk\] Intro to Large Language Models - YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g)
Great over view tutorial.
There could also be a 3rd RLHF stage. Pre-training just produces a document auto completer. Finetuning makes it a helpful assistant. RLHF makes sure it is aligned with human values.
![[shiny-fm-llm-2024-05-07.png]]

![[shiny-fm-llm-2024-05-07-1.png]]

## Mapping the Mind of a Large Language Model - Anthropic
[Blog](https://www.anthropic.com/research/mapping-mind-language-model), [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#assessing-features-v-neurons)
Interesting approach to interpreting feature activation maps with sparse autoencoders.

Related from OpenAI: [Extracting-concepts-from-gpt-4/](https://openai.com/index/extracting-concepts-from-gpt-4/)

## Fine-Tuning Language Models from Human Preferences
[paper](https://arxiv.org/pdf/1909.08593)
- we combine the pretraining advances in natural language processing with human preference learning. We fine-tune pretrained language models with reinforcement learning rather than supervised learning, using a reward model trained from human preferences on text continuations.
- we use a KL constraint to prevent the fine-tuned model from drifting too far from the pretrained model.
- Since the reward model needs to understand language, we initialize it as a random linear function of the final embedding output of the language model policy
- To keep the scale of the reward model consistent across training, we normalize it so that it has mean 0 and variance 1
- Now we fine-tune π to optimize the reward model r. To keep π from moving too far from ρ, we add a penalty  with expectation β KL(π, ρ) - KL divergence between the new policy and the pre trained language model policy
- Our overall training process is: 
	1. Gather samples (x, y0, y1, y2, y3) via x ∼ D, yi ∼ ρ(·|x). Ask humans to pick the best yi from each. 
	2. Initialize r to ρ, using random initialization for the final linear layer of r. Train r on the human samples using loss (1). 
	3. Train π via Proximal Policy Optimization (PPO) with reward R from (2) on x ∼ D. 
	4. In the online data collection case, continue to collect additional samples, and periodically retrain the reward model r.
- We believe the application of human reward learning to natural language tasks is important both from a capability and safety perspective. On the capability side, purely supervised training is insufficient to correct mistakes that arise when sampling from trained policies, and RL training to programmatic reward functions such as BLEU or ROUGE is insufficient.

