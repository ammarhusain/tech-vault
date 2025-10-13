---
aliases: []
tags:
---
# The Illustrated Stable Diffusion

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)
### Metadata
Author: [[Jay Alammar]]
Full Title: The Illustrated Stable Diffusion
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://jalammar.github.io/illustrated-stable-diffusion/
Date Highlighted: [[2022-12-15-Thursday]]

## Highlights
- Diffusion happens in multiple steps, each step operates on an input latents array, and produces another latents array that better resembles the input text and all the visual information the model picked up from all images the model was trained on.
  ![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-unet-steps.png)
  We can visualize a set of these latents to see what information gets added at each step.
  ![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-denoising-steps-latents.png) ([View Highlight](https://read.readwise.io/read/01gmb3xcevzwa95w74adsnsnx2))
- ![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-u-net-noise-training-examples-2.png)
  With this dataset, we can train the noise predictor and end up with a great noise predictor that actually creates images when run in a certain configuration. A training step should look familiar if you’ve had ML exposure:
  [![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-u-net-noise-training-step.png)](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-u-net-noise-training-step.png) ([View Highlight](https://read.readwise.io/read/01gmb426xg90ph1f05nck7ja1n))
- If the training dataset was of aesthetically pleasing images (e.g., [LAION Aesthetics](https://laion.ai/blog/laion-aesthetics/), which Stable Diffusion was trained on), then the resulting image would tend to be aesthetically pleasing. If the we train it on images of logos, we end up with a logo-generating model.
  [![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-image-generation-v2.png)](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-image-generation-v2.png) ([View Highlight](https://read.readwise.io/read/01gmb456dq7w7gb4zyktbjbg4e))
- To speed up the image generation process, the Stable Diffusion paper runs the diffusion process not on the pixel images themselves, but on a compressed version of the image. [The paper](https://arxiv.org/abs/2112.10752) calls this “Departure to Latent Space”.
  This compression (and later decompression/painting) is done via an autoencoder. The autoencoder compresses the image into the latent space using its encoder, then reconstructs it using only the compressed information using the decoder.
  ![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-autoencoder.png) ([View Highlight](https://read.readwise.io/read/01gmb48mk6dwsc0876d5ced683))
- The forward process (using the autoencoder’s encoder) is how we generate the data to train the noise predictor. Once it’s trained, we can generate images by running the reverse process (using the autoencoder’s decoder).
  [![](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-forward-and-reverse-process-v2.png)](https://jalammar.github.io/images/stable-diffusion/stable-diffusion-forward-and-reverse-process-v2.png)
  These two flows are what’s shown in Figure 3 of the LDM/Stable Diffusion paper:
  ![](https://jalammar.github.io/images/stable-diffusion/article-Figure3-1-1536x762.png) ([View Highlight](https://read.readwise.io/read/01gmb4ca4jvqkwf3hd69p52gvr))
- CLIP is trained on a dataset of images and their captions. Think of a dataset looking like this, only with 400 million images and their captions:
  ![](https://jalammar.github.io/images/stable-diffusion/images-and-captions-dataset.png)
  A dataset of images and their captions.
  In actuality, CLIP was trained on images crawled from the web along with their “alt” tags.
  CLIP is a combination of an image encoder and a text encoder. ([View Highlight](https://read.readwise.io/read/01gmb4gm1ecg9xp9ycd03j9wqy))
- We update the two models so that the next time we embed them, the resulting embeddings are similar.
  ![](https://jalammar.github.io/images/stable-diffusion/clip-training-step-3.png)
  By repeating this across the dataset and with large batch sizes, we end up with the encoders being able to produce embeddings where an image of a dog and the sentence “a picture of a dog” are similar. Just like in [word2vec](https://jalammar.github.io/illustrated-word2vec/), the training process also needs to include **negative examples** of images and captions that don’t match, and the model needs to assign them low similarity scores. ([View Highlight](https://read.readwise.io/read/01gmb4jzvtzgzpys3c0zm96cq5))
- Inside, we see that:
  • The Unet is a series of layers that work on transforming the latents array
  • Each layer operates on the output of the previous layer
  • Some of the outputs are fed (via residual connections) into the processing later in the network
  • The timestep is transformed into a time step embedding vector, and that’s what gets used in the layers
  ![](https://jalammar.github.io/images/stable-diffusion/unit-resnet-steps-v2.png) ([View Highlight](https://read.readwise.io/read/01gmb4s9bc0tyh8xnszh9dzenc))
- The main change to the system we need to add support for text inputs (technical term: text conditioning) is to add an attention layer between the ResNet blocks.
  ![](https://jalammar.github.io/images/stable-diffusion/unet-with-text-steps-v2.png)
  Note that the ResNet block doesn’t directly look at the text. But the attention layers merge those text representations in the latents. And now the next ResNet can utilize that incorporated text information in its processing. ([View Highlight](https://read.readwise.io/read/01gmb4tbrts40nrnsky1jf1j8g))
