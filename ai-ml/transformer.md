---
aliases: [Transformer, Transformers, transformers]
created: 2022-11-08-Tuesday 10:51
modified: 2023-03-10-Friday 23:15
tags: 
---


---

# Notes
- [[2023-10-10-Tuesday]]
	- There are several knobs available for transformer like architectures
		- What positional embedding to use: Learned (original Vaswani paper), RoPE (rotational), AliBi
		- Group attention, what kind of attention masking
		- Tokenizers

# 3blue1brown
[A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html#architecture-attn-independent)
![[nanoGPT-2024-04-08.png]]

# [[hugging face|Hugging Face]]

Doc : [🤗 Transformers](https://huggingface.co/docs/transformers/v4.23.1/en/index), [GitHub - huggingface/transformers: 🤗 Transformers](https://github.com/huggingface/transformers)

[Quickstart colab](https://colab.research.google.com/drive/1OFf_lMBXGr52j9bN5HaONRqEFavKQsoV?authuser=1#scrollTo=szmo-rHI_dBi) , Doc : [Quick tour](https://huggingface.co/docs/transformers/v4.23.1/en/quicktour)

- Configuration of the model is the blueprint that contains all the information of the model architecture
- Transformers provides a simple and unified way to load pretrained instances. This means you can load an [AutoModel](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModel) like you would load an [AutoTokenizer](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoTokenizer). The only difference is selecting the correct [AutoModel](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModel) for the task. For example: to do text - or sequence - classification, load [AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModelForSequenceClassification)
- See the [task summary](https://huggingface.co/docs/transformers/main/en/task_summary) for which [AutoModel](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModel) class to use for which task.
- Using [Trainer - PyTorch optimized training loop](https://huggingface.co/docs/transformers/v4.23.1/en/quicktour#trainer-a-pytorch-optimized-training-loop). Transformers provides a [Trainer](https://huggingface.co/docs/transformers/v4.23.1/en/main_classes/trainer#transformers.Trainer) class optimized for training 🤗 Transformers models, making it easier to start training without manually writing your own training loop. The [Trainer](https://huggingface.co/docs/transformers/v4.23.1/en/main_classes/trainer#transformers.Trainer) API supports a wide range of training options and features such as logging, gradient accumulation, and mixed precision.
- Architecture refers to the skeleton of the model and checkpoints are the weights for a given architecture. For example, [BERT](https://huggingface.co/bert-base-uncased) is an architecture, while `bert-base-uncased` is a checkpoint. Model is a general term that can mean either architecture or checkpoint.
- `AutoModelFor*` classes let you load a pretrained model for a given task (see [here](https://huggingface.co/docs/transformers/v4.23.1/en/model_doc/auto) for a complete list of available tasks). For example, load a model for sequence classification with [AutoModelForSequenceClassification.from_pretrained()](https://huggingface.co/docs/transformers/v4.23.1/en/model_doc/auto#transformers.FlaxAutoModelForVision2Seq.from_pretrained):
- For tasks involving multimodal inputs, you’ll need a [processor](https://huggingface.co/docs/transformers/v4.23.1/en/main_classes/processors) to prepare your dataset for the model. A processor couples a tokenizer and feature extractor.
- All Transformers models return logits.

Vision Transformer [sandbox](https://colab.research.google.com/drive/1l-dxOClI8pxXUR8_izb0M0z-zSzTmQZT?authuser=1#scrollTo=GDbPVJjOsBML)

[Fine-tune a pretrained model](https://huggingface.co/docs/transformers/v4.23.1/en/training) - Also contains a barebone [[pytorch]] training loop

Great notebook from Harvard that annotates the Transformers paper with code - [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)

[[2-Focus-Areas/Readwise/Articles/The Illustrated Transformer]]

### Local Notebooks
![[finetuning_transformer.ipynb]]
![[quicktour.ipynb]]
![[vision_transformers.ipynb]]
