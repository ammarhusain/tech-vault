---
aliases: []
tags:
---
# A Visual History of Interpretation for Image Recognition

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
### Metadata
Author: [[thegradient.pub]]
Full Title: A Visual History of Interpretation for Image Recognition
Category: #readwise/articles
URL: https://thegradient.pub/a-visual-history-of-interpretation-for-image-recognition/
Date Highlighted: [[2022-04-10-Sunday]]

## Highlights
- LOO is an easy method to understand; it’s the first algorithm you might come up with if you were to design an interpretation method from scratch. The idea is to first segment the input image into a bunch of smaller subregions. Then, you run a series of predictions, each time masking (i.e. setting the pixel values to zero of) one of the subregions. Each region is assigned an importance score based on how much its “being masked” affected the prediction relative to the original image. Intuitively, these scores quantify which regions are most responsible for the prediction.
- With standard back-propagation, we compute the gradient of the model’s loss with respect to the weights. The gradient is a vector that contains a value for each weight, reflecting how much a small change in that weight will affect the output, essentially telling us which weights are most important for the loss. By taking the negative of this gradient, we minimize the loss during training. For gradient ascent, we instead take the gradient of the class score with respect to the input pixels, telling us which input pixels are most important in classifying the image. This single step through the network gives us an importance value for each pixel, which we display in the form of a heatmap
