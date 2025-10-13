---
aliases: []
tags:
---
# Helping Robots Learn From Each Other

![rw-book-cover](https://blog.google/static/blogv2/images/google-1000x1000.png)
### Metadata
Author: [[Vincent Vanhoucke]]
Full Title: Helping Robots Learn From Each Other
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robot, ]
URL: https://blog.google/technology/ai/helping-robots-learn-from-each-other/amp/
Date Highlighted: [[2023-01-13-Friday]]

## Highlights
- We’ve often relied on technology to supplement — and even superpower — our human capabilities. We developed the printing press to help share information, the abacus (and then the calculator) to help us do math, the airplane to help us get from one point to another. In recent years, and specifically in the field of machine learning, we’ve developed novel ways to process information to power helpful technologies like Search, Assistant, Maps and more. ([View Highlight](https://read.readwise.io/read/01gppqks8m0fmp94he0dtn2m2c))
    - Tags: #readwise/aiml 
- Underlying many of these technologies is a foundational breakthrough from 2017: the [Transformer](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html). Before the Transformer, machine learning systems struggled with determining which part of their input was relevant to arriving at the correct answer. Transformers introduced the notion of attention: by attending to the important part of its input, the model can dynamically choose what information matters and what doesn't, like applying a highlighter to the most relevant sentences in a book. Transformers proved so powerful that it’s become the mother of modern language models — powering much of the artificial intelligence we see today across the industry ([View Highlight](https://read.readwise.io/read/01gppq9y9pe750mr7f4d45cabb))
- Now, we’re using the same architectural foundation as PaLM’s – the Transformer – to help robots learn more generally from what they’ve already seen. So rather than merely understanding the language underpinning a request like “I’m hungry, bring me a snack,” it can learn — just like we do — from all of its collective experiences doing things like looking at and fetching snacks. ([View Highlight](https://read.readwise.io/read/01gppqcr7x0mm1q5wmmvfbpkw1))
- We did this by training a Transformer model on data collected from 130,000 demonstrations – when a person operates the robot to execute a task – of over 700 types of tasks, completed by 13 helper robots from Everyday Robots. The tasks include skills like picking and placing items, opening and closing drawers, getting items in and out drawers, placing elongated items up-right, knocking objects over, pulling napkins and opening jars ([View Highlight](https://read.readwise.io/read/01gppqk631c3qm4te5bkxtvqa3))
- Just like a Transformer-based language model predicts the next word based on trends and patterns it sees in text, RT-1 has been trained on robotic perception data – images – and corresponding actions so it can identify the next most likely behavior a robot should take. ([View Highlight](https://read.readwise.io/read/01gppqkm9kt5ktn2tz560wfvs1))
