---
aliases: []
tags:
---
# RT-1: Robotics Transformer for Real-World Control at Scale

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8KHWWax1Ls5GmtYjLCtGd6Bq_K9syONqDrjrcZJLwS8q3hKtXTijt6sQylxDwZbt5Rlqc5DCkwDdcaI8wW3Pg8Xwe1A0z3UzMcpmN_kwttugQA_YvF4iumezRUrZyxiNflapGhRp5lokaK22UqMxVwqhn03hqikMJ2Yl4b7WyQs24lgm56qhX0eL9dQ/s72-c/RT-1%20H.png)
### Metadata
Author: [[googleblog.com]]
Full Title: RT-1: Robotics Transformer for Real-World Control at Scale
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robots, ]
URL: https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html
Date Highlighted: [[2022-12-14-Wednesday]]

## Highlights
- RT-1 is built on a [transformer architecture](https://arxiv.org/abs/1706.03762) that takes a short history of images from a robot’s camera along with task descriptions expressed in natural language as inputs and directly outputs tokenized actions.
  RT-1’s architecture is similar to that of a contemporary decoder-only sequence model trained against a standard categorical [cross-entropy](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_loss_function_and_logistic_regression) objective with [causal masking](https://arxiv.org/abs/2106.01345). Its key features include: image tokenization, action tokenization, and token compression ([View Highlight](https://read.readwise.io/read/01gm8nby48fhjvnyw3yjyty9j2))
- **Image tokenization:** We pass images through an [EfficientNet-B3](https://ai.googleblog.com/2019/05/efficientnet-improving-accuracy-and.html) model that is pre-trained on [ImageNet](https://image-net.org/index.php), and then flatten the resulting 9×9×512 spatial feature map to 81 tokens. The image tokenizer is conditioned on natural language task instructions, and uses [FiLM layers](https://arxiv.org/pdf/1709.07871.pdf) initialized to identity to extract task-relevant image features early on. ([View Highlight](https://read.readwise.io/read/01gm8ndbfvy9ra2fzaqthmwv1v))
- **Action tokenization:** The robot’s action dimensions are 7 variables for arm movement (x, y, z, roll, pitch, yaw, gripper opening), 3 variables for base movement (x, y, yaw), and an extra discrete variable to switch between three modes: controlling arm, controlling base, or terminating the episode. Each action dimension is discretized into 256 bins. ([View Highlight](https://read.readwise.io/read/01gm8ndsemf17tx2qthkkhrad0))
- [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj11ho9tm4Td7ByTigAgDxFWsxbsZ6tQsAng3AtwuufHRuoLaLOV9YN7FUMyyAhefzuFOVCrbwTLsEaRYidOOToS__KRrotot-6aBxTliZxYz-B2jiJG-4myq5NB3vRKaY86nr5y1-13dBv_H_XyfnDijphCM3UBalczim0PeGJ63Z0Ok6k9zvKQ2D55A/s16000/image1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj11ho9tm4Td7ByTigAgDxFWsxbsZ6tQsAng3AtwuufHRuoLaLOV9YN7FUMyyAhefzuFOVCrbwTLsEaRYidOOToS__KRrotot-6aBxTliZxYz-B2jiJG-4myq5NB3vRKaY86nr5y1-13dBv_H_XyfnDijphCM3UBalczim0PeGJ63Z0Ok6k9zvKQ2D55A/s1999/image1.png)
  RT-1’s architecture: The model takes a text instruction and set of images as inputs, encodes them as tokens via a pre-trained FiLM EfficientNet model and compresses them via TokenLearner. These are then fed into the Transformer, which outputs action tokens. ([View Highlight](https://read.readwise.io/read/01gm8ngcd7skqyrtwkzacjvw5q))
- SayCan works by grounding language models in robotic affordances, and leveraging few-shot prompting to break down a long-horizon task expressed in natural language into a sequence of low-level skills. ([View Highlight](https://read.readwise.io/read/01gm8nszbx4b6sdxy3c4hfr4pc))
