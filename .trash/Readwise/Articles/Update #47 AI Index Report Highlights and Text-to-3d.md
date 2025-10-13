---
aliases: []
tags:
---
# Update #47: AI Index Report Highlights and Text-to-3d

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_limit,f_jpg,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb47e3754-7506-4199-bc28-8b31774a885b_1600x850.png)
### Metadata
Author: [[daniel bashir]]
Full Title: Update #47: AI Index Report Highlights and Text-to-3d
Category: #readwise/articles
URL: https://thegradientpub.substack.com/p/update-47-ai-index-report-highlights?utm_source=post-email-title&publication_id=265424&post_id=113762164&isFreemail=false&utm_medium=email
Date Highlighted: [[2023-04-21-Friday]]

## Highlights
- researchers and engineers have been working towards text-to-3D data generation as well. This problem is harder than text-to-2D for several reasons; for one, there are many fewer available pairs of 3D data and text descriptions than there are image-text pairs. ([View Highlight](https://read.readwise.io/read/01gyjav4an6x059kc3vbjbs39b))
- Both of these works use Neural Radiance Fields (NeRFs) to represent 3D scenes. In other words, both methods generate a neural network that represents a scene fitting a text description, and this neural network can be used to view the scene from any position and any viewing angle. ([View Highlight](https://read.readwise.io/read/01gyjavme8gnv556yq4e698eyp))
- Instruct-NeRF2NeRF is built off of [InstructPix2Pix](https://www.timothybrooks.com/instruct-pix2pix/), a text-to-2D diffusion model that takes in an image and text instruction, and edits the image based on the text instruction. Instruct-NeRF2NeRF takes in a text instruction, a NeRF, and the training set of images, positions, and viewing angles used to train the NeRF. To get an output NeRF that edits the scene based on the text instruction, the authors use a particular training process starting from the input NeRF. First, the NeRF is used to render an image from the current scene at a training viewpoint. Then this image is edited to follow the text instruction using InstructPix2Pix, and the training dataset image is replaced with this edited image. This process continues iteratively. ([View Highlight](https://read.readwise.io/read/01gyjd4gt4600rk0bmm5q7pswn))
    - Note: Something like this could be used to generate different hand meshes for WearScape too
---
aliases: []
tags:
---
# Update #47: AI Index Report Highlights and Text-to-3d

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_limit,f_jpg,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb47e3754-7506-4199-bc28-8b31774a885b_1600x850.png)
### Metadata
Author: [[daniel bashir]]
Full Title: Update #47: AI Index Report Highlights and Text-to-3d
Category: #readwise/articles
URL: https://thegradientpub.substack.com/p/update-47-ai-index-report-highlights?utm_source=post-email-title&publication_id=265424&post_id=113762164&isFreemail=false&utm_medium=email
Date Highlighted: [[2023-04-21-Friday]]

## Highlights
- researchers and engineers have been working towards text-to-3D data generation as well. This problem is harder than text-to-2D for several reasons; for one, there are many fewer available pairs of 3D data and text descriptions than there are image-text pairs. ([View Highlight](https://read.readwise.io/read/01gyjav4an6x059kc3vbjbs39b))
- Both of these works use Neural Radiance Fields (NeRFs) to represent 3D scenes. In other words, both methods generate a neural network that represents a scene fitting a text description, and this neural network can be used to view the scene from any position and any viewing angle. ([View Highlight](https://read.readwise.io/read/01gyjavme8gnv556yq4e698eyp))
- Instruct-NeRF2NeRF is built off of [InstructPix2Pix](https://www.timothybrooks.com/instruct-pix2pix/), a text-to-2D diffusion model that takes in an image and text instruction, and edits the image based on the text instruction. Instruct-NeRF2NeRF takes in a text instruction, a NeRF, and the training set of images, positions, and viewing angles used to train the NeRF. To get an output NeRF that edits the scene based on the text instruction, the authors use a particular training process starting from the input NeRF. First, the NeRF is used to render an image from the current scene at a training viewpoint. Then this image is edited to follow the text instruction using InstructPix2Pix, and the training dataset image is replaced with this edited image. This process continues iteratively. ([View Highlight](https://read.readwise.io/read/01gyjd4gt4600rk0bmm5q7pswn))
    - Note: Something like this could be used to generate different hand meshes for WearScape too

