---
aliases: []
tags:
---
# Making LLMs Even More Accessible With Bitsandbytes, 4-Bit Quantization and QLoRA

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_200658/Thumbnail_blue.png)
### Metadata
Author: [[huggingface.co]]
Full Title: Making LLMs Even More Accessible With Bitsandbytes, 4-Bit Quantization and QLoRA
Category: #readwise/articles
URL: https://huggingface.co/blog/4bit-transformers-bitsandbytes
Date Highlighted: [[2023-10-05-Thursday]]

## Highlights
- QLoRA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) double quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) paged optimizers to manage memory spikes. ([View Highlight](https://read.readwise.io/read/01hbycxktvd69g4kdf5bcyv6jb))
- Our results show that QLoRA finetuning on a small high-quality dataset leads to state-of-the-art results, even when using smaller models than the previous SoTA. ([View Highlight](https://read.readwise.io/read/01hbyd0xd3bpetmwqpevjz747j))
- In few words, QLoRA reduces the memory usage of LLM finetuning without performance tradeoffs compared to standard 16-bit model finetuning. This method enables 33B model finetuning on a single 24GB GPU and 65B model finetuning on a single 46GB GPU.
  More specifically, QLoRA uses 4-bit quantization to compress a pretrained language model. The LM parameters are then frozen and a relatively small number of trainable parameters are added to the model in the form of Low-Rank Adapters. During finetuning, QLoRA backpropagates gradients through the frozen 4-bit quantized pretrained language model into the Low-Rank Adapters. The LoRA layers are the only parameters being updated during training ([View Highlight](https://read.readwise.io/read/01hbykg75jqcwz44zeaf4ykfeq))
- QLoRA has one storage data type (usually 4-bit NormalFloat) for the base model weights and a computation data type (16-bit BrainFloat) used to perform computations. QLoRA dequantizes weights from the storage data type to the computation data type to perform the forward and backward passes, but only computes weight gradients for the LoRA parameters which use 16-bit bfloat. The weights are decompressed only when they are needed, therefore the memory usage stays low during training and inference. ([View Highlight](https://read.readwise.io/read/01hbykhhyhm1f1enqv2j9zhgmm))
- You can play with different variants of 4bit quantization such as NF4 (normalized float 4 (default)) or pure FP4 quantization. Based on theoretical considerations and empirical results from the paper, we recommend using NF4 quantization for better performance. ([View Highlight](https://read.readwise.io/read/01hbykx0esbgc8byjpxjwwgp0g))
- A rule of thumb is: use double quant if you have problems with memory, use NF4 for higher precision, and use a 16-bit dtype for faster finetuning. ([View Highlight](https://read.readwise.io/read/01hbym08rtbkzgd4v36z0m06wj))
