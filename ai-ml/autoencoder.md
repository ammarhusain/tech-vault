---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

[[train_autoencoder.ipynb]]
[[autoencoder.py]]
[[autoencoder.ipynb]]

An autoencoder is basically a network that downsamples the input vector into a latent representation and then upsamples it back. The loss is usually a reconstruction loss w.r.t the original vector or a similarly high dimensional annotated vector (could be denoised, segmentation map etc.)
![[autoencoder_1.png]]
The encoder and decoder could be fully connected layers ([[neural networks]]) or convolutional layers ([[convolutional neural nets]]). Some uses of autoencoder in CV could be: denoising (removing watermarks, random noise etc.), semantic segmentation, neural inpainting (filling in missing patches).

# Variational Autoencoder

Instead of outputting a latent space, outputs a distribution over the latent space. We then sample over this distribution of this latent space and feed it in for decoding.
![[autoencoder_2.png]]
There is also an addition loss term that gets added in addition to the reconstruction loss. This term measures the [[KL divergence]] between the produced latent distribution and a unit Gaussian The idea here is to keep the latent space distribution as close to a unit Gaussian as possible.
![[autoencoder_3.png]]
