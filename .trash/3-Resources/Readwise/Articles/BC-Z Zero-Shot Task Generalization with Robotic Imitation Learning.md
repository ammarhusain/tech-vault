---
aliases: []
tags:
---
# BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)
### Metadata
Author: [[Eric Jang, Alex Irpan, Mohi Khansari, Daniel Kappler, Frederik Ebert, Corey Lynch, Sergey Levine, Chelsea Finn]]
Full Title: BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robot, ]
URL: https://arxiv.org/pdf/2202.02005.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- we develop an interactive and ﬂexible imitation learn-
  ing system that can learn from both demonstrations and interventions and can be
  conditioned on different forms of information that convey the task, including pre-
  trained embeddings of natural language or videos of humans performing the task. ([View Highlight](https://read.readwise.io/read/01gpeyffyw6dj35pyxzfc0qytb))
- The policy architecture is divided into an encoder q(z|w), which processes the command w into
  an embedding z ∈ Z, and a control layer π, which processes (s, z) to produce the action a, ([View Highlight](https://read.readwise.io/read/01gpf0p0edekkn5em1tgfgv9r2))
- . For each task i, this dataset
  contains expert data (s, a) ∈ Di
  e, human video data wh ∈ Di
  h, and one language command wi
  . We
  now discuss how we use this data to train the encoder q(z|w) and the control layer π(a|s, z). ([View Highlight](https://read.readwise.io/read/01gpf0bx5fsr7x7cs30nhsdvyw))
