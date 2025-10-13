---
aliases: []
tags:
---
# Stable Diffusion With 🧨 Diffusers

![rw-book-cover](https://huggingface.co/blog/assets/98_stable_diffusion/thumbnail.png)
### Metadata
Author: [[huggingface.co]]
Full Title: Stable Diffusion With 🧨 Diffusers
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://huggingface.co/blog/stable_diffusion
Date Highlighted: [[2022-12-21-Wednesday]]

## Highlights
- Stable Diffusion is a text-to-image latent diffusion model ... It is trained on 512x512 images from a subset of the [LAION-5B](https://laion.ai/blog/laion-5b/) database. *LAION-5B* is the largest, freely accessible multi-modal dataset that currently exists.
- `guidance_scale` is a way to increase the adherence to the conditional signal that guides the generation (text, in this case) as well as overall sample quality. It is also known as [classifier-free guidance](https://arxiv.org/abs/2207.12598), which in simple terms forces the generation to better match the prompt potentially at the cost of image quality or diversity. Values between `7` and `8.5` are usually good choices for Stable Diffusion. ([View Highlight](https://read.readwise.io/read/01gmtn02fsddb6myq0cwtx7f2j))
- Latent diffusion can reduce the memory and compute complexity by applying the diffusion process over a lower dimensional *latent* space, instead of using the actual pixel space. This is the key difference between standard diffusion and latent diffusion models: **in latent diffusion the model is trained to generate latent (compressed) representations of the images.** ([View Highlight](https://read.readwise.io/read/01gmtnrsb1k37hdajw7r2kdcj1))
- There are three main components in latent diffusion.
  1. An autoencoder (VAE).
  2. A [U-Net](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb#scrollTo=wW8o1Wp0zRkq).
  3. A text-encoder, *e.g.* [CLIP's Text Encoder](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPTextModel). ([View Highlight](https://read.readwise.io/read/01gmtnwfn4m419c5cs4834t3q2))
- The VAE model has two parts, an encoder and a decoder. The encoder is used to convert the image into a low dimensional latent representation, which will serve as the input to the *U-Net* model. The decoder, conversely, transforms the latent representation back into an image. ([View Highlight](https://read.readwise.io/read/01gmtnz7a8c3f9jv0rfxyrf7kb))
    - Note: Why use a U-Net I wonder if the image is encoded by a VAE anyway? It could get encoded to a 1D or ND matrix instead of staying a 2D image too right?
- the stable diffusion U-Net is able to condition its output on text-embeddings via cross-attention layers. The cross-attention layers are added to both the encoder and decoder part of the U-Net usually between ResNet blocks. ([View Highlight](https://read.readwise.io/read/01gmtp4122ajftftgm3ts6w4fk))
    - Note: Why use a U-Net I wonder if the image is encoded by a VAE anyway? It could get encoded to a 1D or ND matrix instead of staying a 2D image too right?
- The text-encoder is responsible for transforming the input prompt ... into an embedding space that can be understood by the U-Net. It is usually a simple *transformer-based* encoder that maps a sequence of input tokens to a sequence of latent text-embeddings.
  Inspired by [Imagen](https://imagen.research.google/), Stable Diffusion does **not** train the text-encoder during training and simply uses an CLIP's already trained text encoder, [CLIPTextModel](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPTextModel).
- Since latent diffusion operates on a low dimensional space, it greatly reduces the memory and compute requirements compared to pixel-space diffusion models. For example, the autoencoder used in Stable Diffusion has a reduction factor of 8. This means that an image of shape `(3, 512, 512)` becomes `(3, 64, 64)` in latent space, which requires `8 × 8 = 64` times less memory. ([View Highlight](https://read.readwise.io/read/01gmtp7gtm8htz9dja9c78apxm))
- ![sd-pipeline](https://raw.githubusercontent.com/patrickvonplaten/scientific_images/master/stable_diffusion.png)
  The stable diffusion model takes both a latent seed and a text prompt as an input. The latent seed is then used to generate random latent image representations of size 64×64 64 \times 64 64×64 where as the text prompt is transformed to text embeddings of size 77×768 77 \times 768 77×768 via CLIP's text encoder. ([View Highlight](https://read.readwise.io/read/01gmtpctaxq64qcq9bn1bktbst))
- The [pre-trained model](https://huggingface.co/CompVis/stable-diffusion-v1-4/tree/main) includes all the components required to setup a complete diffusion pipeline. They are stored in the following folders:
  • `text_encoder`: Stable Diffusion uses CLIP, but other diffusion models may use other encoders such as `BERT`.
  • `tokenizer`. It must match the one used by the `text_encoder` model.
  • `scheduler`: The scheduling algorithm used to progressively add noise to the image during training.
  • `unet`: The model used to generate the latent representation of the input.
  • `vae`: Autoencoder module that we'll use to decode latent representations into real images. ([View Highlight](https://read.readwise.io/read/01gmtpm3qbrtn05d8jq49wdavb))
- For classifier-free guidance, we need to do two forward passes: one with the conditioned input (`text_embeddings`), and another with the unconditional embeddings (`uncond_embeddings`). In practice, we can concatenate both into a single batch to avoid doing two forward passes. ([View Highlight](https://read.readwise.io/read/01gmtq24jq6th5tny0pfcz0xq2))
    - Note: Simply a weighted average. See code below: Equation 2 of the Imagen paper here - https://arxiv.org/pdf/2205.11487.pdf
- noise_pred = noise_pred_uncond + guidance_scale * (noise_pred_text - noise_pred_uncond) ([View Highlight](https://read.readwise.io/read/01gmtpzx8mmsjx1pp4bvkszddh))
    - Note: Seems like the classifier guidance is just a weighted average between one image that is samples with the text prompt and the other that is sampled without any text prompt (unconditionally)
