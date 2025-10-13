---
aliases: []
tags:
---
# Gradient Update #26: Facial Recognition in the Real World and Large Language Model Advances

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)
### Metadata
Author: [[thegradientpub.substack.com]]
Full Title: Gradient Update #26: Facial Recognition in the Real World and Large Language Model Advances
Category: #readwise/articles
URL: https://thegradientpub.substack.com/p/gradient-update-26-facial-recognition
Date Highlighted: [[2022-06-16-Thursday]]

## Highlights
- Imagen is a text-to-image diffusion model that leverages text embeddings from a generic LLM (T5 XXL). The LLM is frozen, meaning that it is not updated during training. The rest of the model is a diffusion model that is conditioned on the LLM text embeddings and generates images. In contrast, DALL-E 2 encodes text using CLIP, which was trained in a multimodal fashion to embed text and images in a shared latent space. Imagen outperforms DALL-E 2 on MS-COCO and several human evaluation metrics, thus showing the power of an LLM that was only trained on text, and no images. Moreover, experiments show that increasing the size of the LLM significantly improves performance, and is more impactful than increasing the size of the diffusion model.
- researchers affiliated with the University of Tokyo and Google Brain demonstrate that a simple change can significantly improve the zero-shot reasoning capabilities of LLMs.

