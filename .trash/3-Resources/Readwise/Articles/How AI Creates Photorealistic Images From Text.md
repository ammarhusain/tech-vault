---
aliases: []
tags:
---
# How AI Creates Photorealistic Images From Text

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
### Metadata
Author: [[blog.google]]
Full Title: How AI Creates Photorealistic Images From Text
Category: #readwise/articles
URL: https://blog.google/technology/research/how-ai-creates-photorealistic-images-from-text/
Date Highlighted: [[2022-09-03-Saturday]]

## Highlights
- Within Google Research, our scientists and engineers have been exploring text-to-image generation using a variety of AI techniques. After a lot of testing we recently announced two new text-to-image models — Imagen and Parti. Both have the ability to generate photorealistic images but use different approaches.
- Imagen is a Diffusion model, which learns to convert a pattern of random dots to images. These images first start as low resolution and then progressively increase in resolution. Recently, Diffusion models have seen success in both image and audio tasks like enhancing image resolution, recoloring black and white photos, editing regions of an image, uncropping images, and text-to-speech synthesis.
- Parti’s approach first converts a collection of images into a sequence of code entries, similar to puzzle pieces. A given text prompt is then translated into these code entries and a new image is created. This approach takes advantage of existing research and infrastructure for large language models such as PaLM and is critical for handling long, complex text prompts and producing high-quality images.
