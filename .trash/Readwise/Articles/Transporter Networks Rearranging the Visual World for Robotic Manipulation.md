---
aliases: []
tags:
---
# Transporter Networks: Rearranging the Visual World for Robotic Manipulation

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)
### Metadata
Author: [[Anonymous Submission]]
Full Title: Transporter Networks: Rearranging the Visual World for Robotic Manipulation
Category: #readwise/articles
Document Tags: [ [[aiml]],  [[AIML]],  [[robot]], ]
URL: https://arxiv.org/pdf/2010.14406.pdf
Date Highlighted: [[2023-01-11-Wednesday]]

## Highlights
- Transporter Network, a simple
  model architecture that rearranges deep features to infer spatial displacements from
  visual input – which can parameterize robot actions. It makes no assumptions of
  objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries ([View Highlight](https://read.readwise.io/read/01gpf4xwbsmdahtqaecee9kn7j))
- On
  10 unique tabletop manipulation tasks, Transporter Networks trained from scratch are capable of achieving
  greater than 90% success on most tasks with objects in new configurations using 100 expert demonstrations,
  while other end-to-end alternatives struggle to generalize with the same amount of data. ([View Highlight](https://read.readwise.io/read/01gpf4nhwqg4vhk4fr7ayhxx0t))
    - Note: the objects are not novel from training data. just in new configurations
- In this work, the goal of Transporter Networks is to transport our partial crop ot[Tpick] densely across a
  set of poses {τi} to search for its best placement, i.e. the ot[τi] with the highest feature correlation. This
  operation is analogous to the search function in visual tracking literature ([View Highlight](https://read.readwise.io/read/01gpf5aw8bmgq7byfe6g5zsvph))
- In our simulation framework, Ravens, each task comes with a scripted oracle that provides expert demon-
  strations by randomly sampling the distribution of successful picking and placing actions – samples of
  which are made available to the learner. Ravens also has several attributes that make it useful for studying
  different areas that are beyond the scope of this work, including: 1) active learning, since algorithms can
  query an oracle during specific moments of uncertainty to improve learning efficiency, 2) reinforcement
  learning, since we provide reward functions that provide partial credit for all tasks (used only for evaluation
  in this work), and 3) active perception, since camera parameters (e.g., extrinsics) are defined by an action
  (static in our experiments, but could be dynamic), which provides an opportunity to study algorithms that
  improve learning through active control of the camera position and orientation. ([View Highlight](https://read.readwise.io/read/01gph78r0b3rcxx3tadeasvb4k))
- k ([View Highlight](https://read.readwise.io/read/01gph7sp3p6929648e4jrsegdg))

