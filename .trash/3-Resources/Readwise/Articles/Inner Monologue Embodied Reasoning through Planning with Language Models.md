---
aliases: []
tags:
---
# Inner Monologue: Embodied Reasoning through Planning with Language Models

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_200658/VZCrxa-_jEJFsHaIvP40IHxZPdxeTze3X6g01Dw97b8-cover_7ERh5B7.png)
### Metadata
Author: [[Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, Pierre Sermanet, Noah Brown, Tomas Jackson, Linda Luu, Sergey Levine, Karol Hausman, Brian Ichter]]
Full Title: Inner Monologue: Embodied Reasoning through Planning with Language Models
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/AIML,  #readwise/doc/robot, ]
URL: https://arxiv.org/pdf/2207.05608.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- we combine multiple perception models that perform various tasks such as
  language-conditioned semantic classification or language-based scene description, together with feedback
  provided by a human user that the robot is cooperating with. ([View Highlight](https://read.readwise.io/read/01gnzx6h0596cgpqw38fan2ycv))
- To execute the commands given by a user, the
  actions are chosen from a set of pre-trained robotic manipulation skills together with their textual descriptions
  that can be invoked by a language model. Our proposed system Inner Monologue chains together these
  various components (perception models, robotic skills, and human feedback) in a shared language prompt,
  enabling it to successfully perform user instructions. ([View Highlight](https://read.readwise.io/read/01gnzx72101wvmkjmk4y52s7pz))
- we show that Inner Monologue, without requiring additional training beyond a frozen language model
  and pre-trained robotic skills, can accomplish complex, long-horizon, and unseen tasks in simulation as well
  as on two real-world robotic platforms. ([View Highlight](https://read.readwise.io/read/01gnzx850z4pqxqmmvjm0h2m5t))
- This robotic agent is only capable of executing short-horizon skills from a library of previously
  trained policies πk∈Πwith short language descriptions k, which may be trained with reinforcement learning
  or behavioral cloning. ([View Highlight](https://read.readwise.io/read/01gnzx95c0mnm7k8bqv6cndncd))
- The “planner,” which is a pretrained LLM [20, 21], attempts to find a sequence of
  skills to accomplish the instruction. To observe the environment, the planner has access to textual feedback
  o from the environment that can be appended to the instruction or requested by the planner. The observation
  o may be success detection, object detection, scene description, visual-question answering, or even human
  feedback. ([View Highlight](https://read.readwise.io/read/01gnzxa4bgnpy60cp2m2t4jqa8))
- As the proactive counterpart to Passive SceneDescription, Active SceneDescrip-
  tion encompasses sources of feedback that are provided directly in response to active queries by the LLM plan-
  ner. In this case, the LLM can directly ask a question about the scene, and this question can be answered either
  by a person, or by another pretrained model, such as a Visual Question Answering (VQA) model ([View Highlight](https://read.readwise.io/read/01gnzxg1acfxw7bsfrff2e57ay))
- The learned manipulation policies
  responsible for counter picking, drawer opening and closing, drawer picking, and countertop object
  manipulation are Behavior Cloning (BC) policies trained on 68000 teleoperated demonstrations and 12000
  autonomous successes that were collected over the course of 11 months using a fleet of 10 robots. ([View Highlight](https://read.readwise.io/read/01gnzypcfxwbpmse5k0dbst8b3))
- The scripted navigation policies utilize a ground-truth map along with a learned
  perception module to navigate between different points in the environment. The scripted manipulation policy
  is solely responsible for countertop placing when preceded by a navigation policy, and follows pre-computed
  motions. The Value Functions used by SayCan for affordance grounding are provided by the Q-networks
  of trained RL agents; ([View Highlight](https://read.readwise.io/read/01gnzypkwvjbnv44mbrwk4hr8f))
- The model uses image encoders from
  CLIP [65] to embed o0 and of, concatenate them, and fuse these representations with a fusion MLP. This
  image embedding is concatenated with the text embedding obtained by the CLIP text encoder, then passed
  through another MLP. The output of the model is a scalar denoting the probability of the agent succeeding
  at the specified task ([View Highlight](https://read.readwise.io/read/01gnzyw544k3av37f8qezpz70p))
