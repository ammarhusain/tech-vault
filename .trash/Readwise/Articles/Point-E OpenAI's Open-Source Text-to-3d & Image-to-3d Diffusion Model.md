---
aliases: []
tags:
---
# Point-E: OpenAI's Open-Source Text-to-3d & Image-to-3d Diffusion Model

![rw-book-cover](https://wandb.ai/logo.png)
### Metadata
Author: [[W&B]]
Full Title: Point-E: OpenAI's Open-Source Text-to-3d & Image-to-3d Diffusion Model
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://wandb.ai/telidavies/ml-news/reports/Point-E-OpenAI-s-Open-Source-Text-To-3D-Image-To-3D-Diffusion-Model--VmlldzozMTkwMzU3
Date Highlighted: [[2023-04-01-Saturday]]

## Highlights
- How does Point-E work?
  Where many text-to-3D models convert text prompts to 3D objects directly, Point-E opts to split the process into two steps for text-to-image and image-to-3D. This split architecture was chosen because it is more scalable, less reliant on hard-to-come-by 3D object datasets, and takes advantage of the already-established flexibility of cheap-but-powerful text-to-image generation models. ([View Highlight](https://read.readwise.io/read/01gwyn248vsfnjhkg4q24xw4ke))
- The text-to-image portion of Point-E is a fine-tuned [GLIDE](https://arxiv.org/abs/2112.10741) model. ([View Highlight](https://read.readwise.io/read/01gwyne4vrr33gsmb978z1y4mt))
- The image output from the text-to-image portion is embedded through a pre-trained CLIP model before insertion. ([View Highlight](https://read.readwise.io/read/01gwynbssg5vvw3gwd7bwgar2e))
- like other diffusion models, Point-E first constructs a low-resolution, or in this case, low-point count, the output which is subsequently upscaled by a smaller upscaler model of similar architecture. The base model produces 1,000 points, which the upscaler increases to 4,000 points. ([View Highlight](https://read.readwise.io/read/01gwyncyjpvwc6hwcnffhvg2f9))
---
aliases: []
tags:
---
# Point-E: OpenAI's Open-Source Text-to-3d & Image-to-3d Diffusion Model

![rw-book-cover](https://wandb.ai/logo.png)
### Metadata
Author: [[W&B]]
Full Title: Point-E: OpenAI's Open-Source Text-to-3d & Image-to-3d Diffusion Model
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://wandb.ai/telidavies/ml-news/reports/Point-E-OpenAI-s-Open-Source-Text-To-3D-Image-To-3D-Diffusion-Model--VmlldzozMTkwMzU3
Date Highlighted: [[2023-04-01-Saturday]]

## Highlights
- How does Point-E work?
  Where many text-to-3D models convert text prompts to 3D objects directly, Point-E opts to split the process into two steps for text-to-image and image-to-3D. This split architecture was chosen because it is more scalable, less reliant on hard-to-come-by 3D object datasets, and takes advantage of the already-established flexibility of cheap-but-powerful text-to-image generation models. ([View Highlight](https://read.readwise.io/read/01gwyn248vsfnjhkg4q24xw4ke))
- The text-to-image portion of Point-E is a fine-tuned [GLIDE](https://arxiv.org/abs/2112.10741) model. ([View Highlight](https://read.readwise.io/read/01gwyne4vrr33gsmb978z1y4mt))
- The image output from the text-to-image portion is embedded through a pre-trained CLIP model before insertion. ([View Highlight](https://read.readwise.io/read/01gwynbssg5vvw3gwd7bwgar2e))
- like other diffusion models, Point-E first constructs a low-resolution, or in this case, low-point count, the output which is subsequently upscaled by a smaller upscaler model of similar architecture. The base model produces 1,000 points, which the upscaler increases to 4,000 points. ([View Highlight](https://read.readwise.io/read/01gwyncyjpvwc6hwcnffhvg2f9))

