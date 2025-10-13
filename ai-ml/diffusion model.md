---
aliases:
  - diffusion models
created: 2022-09-19-Monday 15:59
modified: 2023-04-19-Wednesday 10:10
tags:
---

**Linked by:**

**Related To:**
- [[*shiny-fm-diffusion]]
- [[2-Focus-Areas/Readwise/Articles/The Illustrated Stable Diffusion]]
	- Does the noise diffusion in a latent encoded space that needs to be decoder by an image decoder, rather than diffusing in the image space.
- [[2-Focus-Areas/Readwise/Articles/Stable Diffusion With 🧨 Diffusers]] - [[stable_diffusion.ipynb]]


> [!tip]- Colab notebooks
![[annotated diffusion model.ipynb]]
![[code-junkyard/diffusion/diffusers_training_example.ipynb]]
![[code-junkyard/diffusion/Diffusers.ipynb]]
![[diffusers-junkyard.ipynb]]
![[stable diffusion with diffusers.ipynb]]
![[stable_diffusion_my_notebook.ipynb]]
![[stable_diffusion 1.ipynb]]

---

[[2025-04-03-Thursday]]
- Variance of the noise added to the image increases with each timestep: variance schedule a bit like the learning rate schedule
- However, we don't know $p(x_{t−1} ∣ x_t)$. It's intractable since it requires knowing the distribution of all possible images in order to calculate this conditional probability. Hence, we're going to leverage a neural network to approximate (learn) this conditional probability distribution, let's call it $p_θ(x_{t−1} ∣ x_t)$ with $θ$ being the parameters of the neural network, updated by gradient descent. so we need a neural network to represent a (conditional) probability distribution of the backward process.
- Model is usually not trained to directly predict a slightly less noisy image, but rather to predict the "noise residual" which is the difference between a less noisy image and the input image (for a diffusion model called "DDPM")

---
Good step by step walk through the paper math + code: [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion)
	My notes: [[2-Focus-Areas/Readwise/Articles/The Annotated Diffusion Model]]
	Colab: [annotated diffusion model.ipynb - Colaboratory](https://colab.research.google.com/drive/1cIX1xKMpgX-pY-IcRv_Xd_vv3yKRJ2Zd?authuser=1#scrollTo=r-66oBOL-9DW)

Tinker with Stable Diffusion : [stabilityai/stable-diffusion-2-1 · Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-2-1)
Old library - perhaps deprecated by [[diffusion model#HuggingFace Diffusers]]
	- [GitHub - lucidrains/denoising-diffusion-pytorch: Implementation of Denoising Diffusion Probabilistic Model in Pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch)

# Fast Ai Course part 2

Main notebook - [diffusion-nbs/stable\_diffusion.ipynb at master · fastai/diffusion-nbs · GitHub](https://github.com/fastai/diffusion-nbs/blob/master/stable_diffusion.ipynb)

## Lecture 9

Textual Inversion & Dreambooth are two methods of doing finetuning or more like style transfer.
Interesting example of finetuning - here [How to fine tune stable diffusion: how we made the text-to-pokemon model at Lambda](https://lambdalabs.com/blog/how-to-fine-tune-stable-diffusion-how-we-made-the-text-to-pokemon-model-at-lambda)
This is relevant to my idea of synthetic data generation for perception model training ^^
CL in [[*shiny-fm-datasets#Clip : Connecting Text & Images|CLIP]] stands for Contrastive loss which means maximize the embedding similarity for matching image & text pairs and minimize the similarity for non matching image & test pairs.
![[Pasted image 20230418104058.png]]
Components we need to build up a diffusion model:
![[Pasted image 20230418104245.png]]
**U-Net** : give it some noise and it applies a U-Net architecture to predict noise which can then be subtracted (like in semantic segmentation)
**VAE Decoder** : take the latents and upsample them into an image
**CLIP Text encoder** : condition the diffusion model based on the text embedding

## Lecture 10

Diffusion model math is formulated as "differential equations", though it could very well have been formulated as a "optimization scheduling" problem.

**Classifier free guided diffusion models** - For these models the diffusion U-net is given a prompt embedding and an empty embedding. It produces two outputs. The outputs are then averaged together for the next step over and over again.

Progressive Distillation - These algorithms are interesting. It basically has a teacher diffusion net and a student diffusion net. The teacher denoising in multiple steps. The student then tries to learn denoising that same sequence in one step. The student net then become the teacher net for the next denoising stage and a new student net is initialized. This process keeps going and makes denoising progressively faster.



# Huggingface Diffusers

**Library :** [🧨 Diffusers](https://huggingface.co/docs/diffusers/index)
State-of-the-art diffusion pipelines that can be run in inference with just a couple of lines of code (see [**Using Diffusers**](https://huggingface.co/docs/diffusers/using-diffusers/conditional_image_generation)) or have a look at [**Pipelines**](https://huggingface.co/docs/diffusers/index#pipelines) to get an overview of all supported pipelines

## Introduction

[Diffusers.ipynb - Colaboratory](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb?authuser=1)
`diffusers` - divided into three components:

1. **Pipelines**: high-level classes designed to rapidly generate samples from popular trained diffusion models in a user-friendly fashion.
2. **Models**: popular architectures for training new diffusion models, *e.g.* [UNet](https://arxiv.org/abs/1505.04597).
3. **Schedulers**: various techniques for generating images from noise during *inference* as well as to generate noisy images for *training*.
Common architecture for diffusion models is [[convolutional neural nets#U-Net|U-Nets]]
 The model is usually not trained to directly predict a slightly less noisy image, but rather to predict the "noise residual" which is the difference between a less noisy image and the input image
To do the denoising process, a specific noise scheduling algorithm is thus necessary and "wrap" the model to define how many diffusion steps are needed for inference as well as how to *compute* a less noisy image from the model's output. Here is where the different **schedulers** of the diffusers library come into play.
Finally, a **pipeline** groups together a **model** and a **scheduler** and make it easy for an end-user to run a full denoising loop process.
**Schedulers** are algorithms wrapped into a Python class. They define the noise schedule which is used to add noise to the model during training, and also define the algorithm to *compute* the slightly less noisy sample given the model output. Schedulers are *parameter-free* (no trainable weights)
All schedulers provide one or multiple `step()` methods that can be used to compute the slightly less noisy image. The `step()` method normally expects at least the model output, the `timestep` and the current `noisy_sample`. It is somewhat of a black box function that "just works".
we very much *deliberately* try to keep *models* and *schedulers* as independent from each other as possible. This means a `scheduler` should never accept a `model` as an input and vice-versa. The model *predict* the noise residual or slightly less noisy image with its trained weights, while the scheduler *computes* the previous sample given the model's output.

## Training Diffusers

[diffusers_training_example.ipynb - Colaboratory](https://colab.research.google.com/drive/1tG0klyE5SJYql3OxV_F7wZ5IYqZ3hlVm?authuser=1#scrollTo=34cac24c-df25-49a7-9828-5518a31df8bc)

## Stable Diffusion with Diffusers

[[2-Focus-Areas/Readwise/Articles/Stable Diffusion With 🧨 Diffusers]]
[stable_diffusion_my_notebook.ipynb - Colaboratory](https://colab.research.google.com/drive/1zGX2rVVI_yt2G0DvTY98aVOGos72HZFP?authuser=1#scrollTo=8640wQ9DUldd)

## [Understanding Diffusion Models: A Unified Perspective](https://substack.com/redirect/1d1cc816-f902-4464-b01c-877117f64006?r=f2u90)

A really nice tutorial starting at simple probability and progressing through variational approximations and the ELBO, VAEs, hierarchical Markovian VAEs, variational diffusion models, score-based generative modeling, and conditional diffusion.

[![](https://ci5.googleusercontent.com/proxy/nusSaAHOKiuHE3m_9BKRTPiFZFlvK-DV6_eupsIAO26IkskKRHxKesvyLAjLTaBnIhOr3OT2VJYTOStVtYciwOmHsEiIryio_gdzpGT7noNuxlPADr5ZM_SXgsQNZ0NuPc4D41f-efPhL7yXKwEb3S-dVeqvNrEs18V5Nly6FwLiZk3v7-GwmyZLThFEL8jfn5N15anS3t3YBuo2iKL9kZQ5pTl4wYJ_LNMFOzneaZoCYxdiDMJ_mVUCY0N4jmCF_FSD926TAIAZSoyckJPnIOC_jmmwrefTyPksNRUfSqkPny2c5LyRVgwgkmwLjOuKH5I1S6Y7kLkendYvvUNLPxuPpg=s0-d-e1-ft#https://substackcdn.com/image/fetch/w_1398,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9df83890-46d9-4962-9f16-8bbadff13fba_2034x1070.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9df83890-46d9-4962-9f16-8bbadff13fba_2034x1070.png)


## Papers
[[Diffusion models beat GAN on Image synthesis (annotated).pdf]]