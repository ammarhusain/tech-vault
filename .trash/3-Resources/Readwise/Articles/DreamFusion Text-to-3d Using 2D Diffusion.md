---
aliases: []
tags:
---
# DreamFusion: Text-to-3d Using 2D Diffusion

![rw-book-cover](https://dreamfusion3d.github.io/assets/images/dreamfusion_samples.png)
### Metadata
Author: [[Ben Poole]]
Full Title: DreamFusion: Text-to-3d Using 2D Diffusion
Category: #readwise/articles
URL: https://dreamfusion3d.github.io/
Date Highlighted: [[2023-06-01-Thursday]]

## Highlights
- In this work, we circumvent these limitations by using a pretrained 2D text-to-image diffusion model to perform text-to-3D synthesis. We introduce a loss based on probability density distillation that enables the use of a 2D diffusion model as a prior for optimization of a parametric image generator. Using this loss in a DeepDream-like procedure, we optimize a randomly-initialized 3D model (a Neural Radiance Field, or NeRF) via gradient descent such that its 2D renderings from random angles achieve a low loss. The resulting 3D model of the given text can be viewed from any angle, relit by arbitrary illumination, or composited into any 3D environment. ([View Highlight](https://read.readwise.io/read/01h1t810qwgxwbpdg01f7s7spj))
- Our generated NeRF models can be exported to meshes using the marching cubes algorithm for easy integration into 3D renderers or modeling software. ([View Highlight](https://read.readwise.io/read/01h1t824g99sx0nsm834q513by))
- We propose **Score Distillation Sampling (SDS)**, a way to generate samples from a diffusion model by optimizing a loss function. SDS allows us to optimize samples in an arbitrary parameter space, such as a 3D space, as long as we can map back to images differentiably. We use a 3D scene parameterization similar to Neural Radiance Fields, or NeRFs, to define this differentiable mapping. ([View Highlight](https://read.readwise.io/read/01h1t8darc0wmvzp09atap34vp))
