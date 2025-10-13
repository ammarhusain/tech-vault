---
publish: 
created: 2024-04-09-Tuesday 18:24
modified: 2024-04-09-Tuesday 18:26
---

#hands-on ![[llama-from-scratch.ipynb]]
# Llama.cpp

[GitHub - karpathy/llama2.c: Inference Llama 2 in one file of pure C](https://github.com/karpathy/llama2.c/tree/master?tab=readme-ov-file)
Simple notebook that loads and runs llama-cpp with python bindings: [[archive/apple/attachments/llama-cpp.ipynb]]
Simple streamlit app that puts a frontend on top of llama-cpp python: [[archive/apple/attachments/st-llama.py]]

[[archive/apple/attentionkit-fc]] streamlit app that calls llama.cpp as subprocess [[archive/apple/attachments/attention-st-ui.py]]

- [x] #j595/todo walk through and run this: Notebook to finetune Llama-2: [[ai-ml/attachments/gpt_llm_trainer.ipynb]]  [completion:: 2024-11-08]
- [x] setup streamlit app to measure llama cpp token inference time locally - 13B model: ✅ 2024-01-09
	- [x] Measure time & memory usage ✅ 2024-01-09
- [x] #j595/todo finetune Llama (simply jupyter notebook) [Fine-Tuning Llama-2: A Comprehensive Case Study for Tailoring Models to Unique Applications](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications) ✅ 2024-03-12

# Llama Architecture

> [!tldr] Llama-1 vs Transformer
> - Pre-normalization and using RMSNorm (from GPT3)
> - SwiGLU activation function (from PaLM)
> - Rotary positional embeddings rather than absolute positional embedding (from GPTNeo)

> [!tldr] Llama-2 vs Llama-1
> - Increased context length from 2k to 4k
> - Grouped-query attention (GQA)

[LLaMA explained: KV-Cache, Rotary Positional Embedding, RMS Norm, Grouped Query Attention, SwiGLU - YouTube](https://www.youtube.com/watch?v=Mn_9W1nCFLo)
![[nanoGPT-2024-04-07.png]]
![[nanoGPT-2024-04-07-1.png]]
![[nanoGPT-2024-04-07-2.png]]
![[nanoGPT-2024-04-07-3.png]]
Root mean square layer norm does not require the mean & variance to be computed like in layer norm so its faster; also works better
RoPE is a relative positional encoding - so instead of an embedding vector that represents a fixed position in a sequence a rotary position embedding represents the distance between two tokens
![[nanoGPT-2024-04-07-4.png]]
Also in Llama the position embedding is added at each layer of the transformer block during attention computation vs in vanilla [[transformer]] where the embedding was added once to the input.
Rotary position embedding are only applied to the Q & K vectors but not the V vectors. They are also applied after those vectors have been multiplied by their corresponding W matrices.
![[nanoGPT-2024-04-07-5.png]]
**KV cache**
![[nanoGPT-2024-04-07-6.png]]

![[nanoGPT-2024-04-07-7.png]]
![[nanoGPT-2024-04-07-8.png]]
Good computation complexity overview of the attention computation:

> [!NOTE] Attention is squared complexity in the size of the embedding dimension

![[nanoGPT-2024-04-07-10.png]]
Memory access becomes the bottleneck of the attention computation when we start using a KV cache - which is not ideal given GPU architecture
![[nanoGPT-2024-04-07-13.png]]

Multi query attention is simply splitting only the Query matrix into multiple heads while leaving the Key & Value matrices as a single headed matrix.
![[nanoGPT-2024-04-07-14.png]]
Halway between multi headed attention and multi-query
![[nanoGPT-2024-04-07-15.png]]
Original Transformer used ReLU, Llama uses SwiGLU for activation function

- [ ] #j595/not-todo  train a TinyLlama model on the shakespeare dataset by loading a checkpoint as well as from scratch using karpathy/llama2.c repo
