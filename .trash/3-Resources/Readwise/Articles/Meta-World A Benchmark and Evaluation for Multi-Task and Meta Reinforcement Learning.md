---
aliases: []
tags:
---
# Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)
### Metadata
Author: [[Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Avnish Narayan, Hayden Shively, Adithya Bellathur, Karol Hausman, Chelsea Finn, Sergey Levine]]
Full Title: Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robot, ]
URL: https://arxiv.org/pdf/1910.10897.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- we propose
  an open-source simulated benchmark for meta-reinforcement learning and multi-
  task learning consisting of 50 distinct robotic manipulation tasks. ([View Highlight](https://read.readwise.io/read/01gpkyza5d558859c8s8pd7skd))
- state-of-the-art methods require substantially
  more experience than humans to acquire only one narrowly-deﬁned skill. If we want robots to be
  broadly useful in realistic environments, we instead need algorithms that can learn a wide variety of
  skills reliably and efﬁciently. ([View Highlight](https://read.readwise.io/read/01gpkyt1pk0p1bmj37r2b793d7))
- Multi-task RL methods aim to learn a single policy that can solve multiple tasks
  more efﬁciently than learning the tasks individually, while meta-learning methods train on many
  tasks, and optimize for fast adaptation to a new task. ([View Highlight](https://read.readwise.io/read/01gpkywtecnca4jf607c2swt9b))
- On one hand, multi-task RL methods have
  largely been evaluated on disjoint and overly diverse tasks such as the Atari suite [8], where there
  is little efﬁciency to be gained by learning across games [9]. On the other hand, meta-RL methods
  have been evaluated on very narrow task distributions. For example, one popular evaluation of meta-
  learning involves choosing different running directions for simulated legged robots [10], which then
  enables fast adaptation to new directions. ([View Highlight](https://read.readwise.io/read/01gpkyy3qyc8ar1pp5tj94xyb6))
- Our empirical evaluation of existing methods on this benchmark
  reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over
  the past few years, current methods are generally not able to learn diverse task sets, much less gen-
  eralize successfully to entirely new tasks. We provide an evaluation protocol with evaluation modes
  of varying difﬁculty, and observe that current methods show varying amounts of success on these
  modes ([View Highlight](https://read.readwise.io/read/01gpkz1ztf8wqmb339p6n628bk))
- The goal of multi-task RL is to learn a single, task-
  conditioned policy π(a|s, z), where z indicates an encoding of the task ID. ([View Highlight](https://read.readwise.io/read/01gpkzdtvwfcgcxg01wdtvsxc7))
- Our full task distribution is therefore substantially broader, since it includes this parametric variabil-
  ity for each ofthe 50 tasks. ([View Highlight](https://read.readwise.io/read/01gpm1ewjb1r4072rffrh2d43r))
- The tasks themselves require the
  robot to execute a combination of reaching, pushing, and grasping, depending on the task. By
  recombining these basic behavioral building blocks with a variety of objects with different shapes
  and articulation properties, we can create a wide range of manipulation tasks. ([View Highlight](https://read.readwise.io/read/01gpm1fwcbrcywy0p6gwd8h3dw))
- For example, the
  open door task involves pushing or grasping an object with a revolute joint, while the open drawer
  task requires pushing or grasping an object with a sliding joint. More complex tasks require a
  combination of these building blocks, which must be executed in the right order. ([View Highlight](https://read.readwise.io/read/01gpm1gpf5qwqbgs48h29nb9rf))
