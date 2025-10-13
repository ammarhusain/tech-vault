---
aliases: []
tags:
---
# OpenAI and the Road to Text-Guided Image Generation: DALL·E, CLIP, GLIDE, DALL·E 2

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)
### Metadata
Author: [[blog.inten.to]]
Full Title: OpenAI and the Road to Text-Guided Image Generation: DALL·E, CLIP, GLIDE, DALL·E 2
Category: #readwise/articles
URL: https://blog.inten.to/openai-and-the-road-to-text-guided-image-generation-dall-e-clip-glide-dall-e-2-unclip-c6e28f7194ea
Date Highlighted: [[2022-08-19-Friday]]

## Highlights
- The trained model generated several samples (up to 512!) based on the text provided, then all these samples were ranked by a special model called CLIP, and the top-ranked one was chosen as the result of the model.
- CLIP was originally a separate auxiliary model to rank the results from DALL·E. Its name is an abbreviation for Contrastive Language-Image Pre-Training.
- CLIPDraw generation procedure: Starting from a random set of Bezier´s curves, the curves' position and colors are optimized so that the generated drawings best match the given description prompt.
- GLIDE could be called DALL·E 2 at the moment it was published. Now when a separate DALL·E 2 system is announced (which is really called unCLIP inside the paper and heavily uses GLIDE itself), we may call GLIDE as DALL·E 1.5 :)
- The CLIP model is trained separately. Then the CLIP text encoder generates an embedding for the input text (caption). Then a special prior model generates an image embedding based on the text embedding. Then a diffusion decoder generates an image based on the image embedding. The decoder essentially inverts image embeddings back into images.
