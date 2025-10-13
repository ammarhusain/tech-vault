---
aliases: []
tags:
---
# Talking to Robots in Real Time

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbFdyJRWeJfiREcvw26XS6tK0xPD_v7opYB9M9Ku8x5-X2SAHxFvuE1KlL8RPqc0aUPYqDVPC9MYmJpW6GgVuDY0sHIBlk1JyOfXAGg47HeWDDGmsKor3w_2XkkLt5GR-rVPst9m2neg1KUO5AbeyUQjrYa0redbk18FBgmqhO70yJnkRFJH03BNcPww/s72-c/interactive%20language%20hero%20image.gif)
### Metadata
Author: [[Google AI (noreply@blogger.com)]]
Full Title: Talking to Robots in Real Time
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robot, ]
URL: http://ai.googleblog.com/2022/12/talking-to-robots-in-real-time.html
Date Highlighted: [[2022-12-15-Thursday]]

## Highlights
- [Palm-SayCan](https://sites.research.google/palm-saycan) work has produced robots that leverage language models to plan long-horizon behaviors and reason about abstract goals. [Code as Policies](https://ai.googleblog.com/2022/11/robots-that-write-their-own-code.html) has shown that code-generating language models combined with pre-trained perception systems can produce language conditioned policies for zero shot robot manipulation. Despite this progress, an important missing property of current "language in, actions out" robot learning systems is *real time* interaction with humans. ([View Highlight](https://read.readwise.io/read/01gmb5j6bp5hkm1a050at2r1xh))
- Ideally, robots of the future would react in real time to any relevant task a user could describe in natural language. Particularly in open human environments, it may be important for end users to customize robot behavior as it is happening, offering quick corrections ("stop, move your arm up a bit") or specifying constraints ("nudge that *slowly* to the right"). Furthermore, real-time language could make it easier for people and robots to collaborate on complex, long-horizon tasks, with people iteratively and interactively guiding robot manipulation with occasional language feedback. ([View Highlight](https://read.readwise.io/read/01gmb5m1dysa42v0597yd024a2))
    - Note: This is a bit like the vision towards humans in the loop for EDR (HiTL)
- Interactive Language shows initial evidence that large scale imitation learning can indeed produce real time interactable robots that follow freeform end user commands. We open source [Language-Table](https://github.com/google-research/language-table), the largest language conditioned real-world robot demonstration dataset of its kind and an associated simulated benchmark, to spur progress in real time language control of physical robots. We believe the utility of this dataset may not only be limited to robot control, but may provide an interesting starting point for studying language- and action-conditioned video prediction, robot video-conditioned language modeling ([View Highlight](https://read.readwise.io/read/01gmb6bkmqr8z9rgd3k635hvt6))
