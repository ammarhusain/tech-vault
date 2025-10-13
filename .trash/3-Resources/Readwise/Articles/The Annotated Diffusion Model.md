---
aliases: []
tags:
---
# The Annotated Diffusion Model

![rw-book-cover](https://huggingface.co/blog/assets/78_annotated-diffusion/thumbnail.png)
### Metadata
Author: [[huggingface.co]]
Full Title: The Annotated Diffusion Model
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://huggingface.co/blog/annotated-diffusion
Date Highlighted: [[2022-12-20-Tuesday]]

## Highlights
- **Denoising Diffusion Probabilistic Models** (also known as DDPMs, diffusion models, score-based generative models or simply [autoencoders](https://benanne.github.io/2022/01/31/diffusion.html)) as researchers have been able to achieve remarkable results with them for (un)conditional image/audio/video generation. Popular examples (at the time of writing) include [GLIDE](https://arxiv.org/abs/2112.10741) and [DALL-E 2](https://openai.com/dall-e-2/) by OpenAI, [Latent Diffusion](https://github.com/CompVis/latent-diffusion) by the University of Heidelberg and [ImageGen](https://imagen.research.google/) by Google Brain. ([View Highlight](https://read.readwise.io/read/01gmrsx451ka7hwnqttzeagws4))
- A (denoising) diffusion model isn't that complex if you compare it to other generative models such as Normalizing Flows, GANs or VAEs: they all convert noise from some simple distribution to a data sample. This is also the case here where **a neural network learns to gradually denoise data** starting from pure noise. ([View Highlight](https://read.readwise.io/read/01gmrt0t6b6q4nvgdssn796452))
- set-up consists of 2 processes:
  • a fixed (or predefined) forward diffusion process qqq of our choosing, that gradually adds Gaussian noise to an image, until you end up with pure noise
  • a learned reverse denoising diffusion process pθp_\thetapθ​, where a neural network is trained to gradually denoise an image starting from pure noise, until you end up with an actual image.
  ![](https://huggingface.co/blog/annotated-diffusion/assets/78_annotated-diffusion/diffusion_figure.png) ([View Highlight](https://read.readwise.io/read/01gmrt1scrttnxgmk3679a92ym))
- Basically, each new (slightly noisier) image at time step ttt is drawn from a **conditional Gaussian distribution** with μt=1−βtxt−1\mathbf{\mu}_t = \sqrt{1 - \beta_t} \mathbf{x}_{t-1}μt​=1−βt​​xt−1​ and σt2=βt\sigma^2_t = \beta_tσt2​=βt​, which we can do by sampling ϵ∼N(0,I)\mathbf{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})ϵ∼N(0,I) and then setting xt=1−βtxt−1+βtϵ\mathbf{x}_t = \sqrt{1 - \beta_t} \mathbf{x}_{t-1} + \sqrt{\beta_t} \mathbf{\epsilon}xt​=1−βt​​xt−1​+βt​​ϵ.
  Note that the βt\beta_tβt​ aren't constant at each time step ttt (hence the subscript) --- in fact one defines a so-called **"variance schedule"**, which can be linear, quadratic, cosine, etc. as we will see further (a bit like a learning rate schedule). ([View Highlight](https://read.readwise.io/read/01gmrt82w10rk5x97x1ercrs9a))
- However, we don't know p(xt−1∣xt)p(\mathbf{x}_{t-1} | \mathbf{x}_t)p(xt−1​∣xt​). It's intractable since it requires knowing the distribution of all possible images in order to calculate this conditional probability. Hence, we're going to leverage a neural network to **approximate (learn) this conditional probability distribution**, let's call it pθ(xt−1∣xt)p_\theta (\mathbf{x}_{t-1} | \mathbf{x}_t)pθ​(xt−1​∣xt​), with θ\thetaθ being the parameters of the neural network, updated by gradient descent. ([View Highlight](https://read.readwise.io/read/01gmrtcw98hq7m2jtfgs7c7qbk))
- we can sample xt\mathbf{x}_txt​ at any arbitrary noise level conditioned on x0\mathbf{x}_0x0​ (since sums of Gaussians is also Gaussian). This is very convenient: we don't need to apply qqq repeatedly in order to sample xt\mathbf{x}_txt​. ([View Highlight](https://read.readwise.io/read/01gmryhjr9d4ysqzs0xeq1gndp))
- The neural network needs to take in a noised image at a particular time step and return the predicted noise. Note that the predicted noise is a tensor that has the same size/resolution as the input image. ([View Highlight](https://read.readwise.io/read/01gmrvte0pjzbpbczw9rw91g8w))
- In terms of architecture, the DDPM authors went for a **U-Net**, introduced by ([Ronneberger et al., 2015](https://arxiv.org/abs/1505.04597)) (which, at the time, achieved state-of-the-art results for medical image segmentation). This network, like any autoencoder, consists of a bottleneck in the middle that makes sure the network learns only the most important information. Importantly, it introduced residual connections between the encoder and decoder, greatly improving gradient flow ([View Highlight](https://read.readwise.io/read/01gmrvvbat8an05akeeg0cmnfa))
    - Note: This is interesting. U-Net is a convolutional architecture that can map images to segmentation masks for ex: by downsampling and then upsampling. In this case U-Net maps an input noisy image to its corresponding noise map. By constantly calling the U-Net noise gets gradually removed one step at a time (diffusion process).
- As the parameters of the neural network are shared across time (noise level), the authors employ sinusoidal position embeddings to encode ttt, inspired by the Transformer ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)). This makes the neural network "know" at which particular time step (noise level) it is operating, for every image in a batch. ([View Highlight](https://read.readwise.io/read/01gmrw6c1t8wa07mf333dj68yj))
- the network takes a batch of noisy images of shape `(batch_size, num_channels, height, width)` and a batch of noise levels of shape `(batch_size, 1)` as input, and returns a tensor of shape `(batch_size, num_channels, height, width)` ([View Highlight](https://read.readwise.io/read/01gmrxancq34r358zzj5s89fz6))
- The network is built up as follows:
  • first, a convolutional layer is applied on the batch of noisy images, and position embeddings are computed for the noise levels
  • next, a sequence of downsampling stages are applied. Each downsampling stage consists of 2 ResNet blocks + groupnorm + attention + residual connection + a downsample operation
  • at the middle of the network, again ResNet blocks are applied, interleaved with attention
  • next, a sequence of upsampling stages are applied. Each upsampling stage consists of 2 ResNet blocks + groupnorm + attention + residual connection + an upsample operation
  • finally, a ResNet block followed by a convolutional layer is applied. ([View Highlight](https://read.readwise.io/read/01gmrxbpczwve7jnytmrnm0jjh))
- The forward diffusion process gradually adds noise to an image from the real distribution, in a number of time steps TTT. This happens according to a **variance schedule**. The original DDPM authors employed a linear schedule ([View Highlight](https://read.readwise.io/read/01gmrxfc889bmjqxnrq03eqr21))
- Generating new images from a diffusion model happens by reversing the diffusion process: we start from TTT, where we sample pure noise from a Gaussian distribution, and then use our neural network to gradually denoise it (using the conditional probability it has learned), until we end up at time step t=0t = 0t=0. As shown above, we can derive a slighly less denoised image xt−1\mathbf{x}_{t-1 }xt−1​ by plugging in the reparametrization of the mean, using our noise predictor. Remember that the variance is known ahead of time.
  Ideally, we end up with an image that looks like it came from the real data distribution. ([View Highlight](https://read.readwise.io/read/01gmrz3htapxdphz3vf17fyn47))
