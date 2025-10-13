---
aliases: []
tags:
---
# CLIPORT: What and Where Pathways for Robotic Manipulation

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
### Metadata
Author: [[Mohit Shridhar, Lucas Manuelli, Dieter Fox]]
Full Title: CLIPORT: What and Where Pathways for Robotic Manipulation
Category: #readwise/articles
Document Tags: [ #readwise/doc/shortlist, ]
URL: https://arxiv.org/pdf/2109.12098.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- In realistic human-robot interaction settings,
  collecting additional demonstrations or providing goal-images is often infeasible and unscalable. A
  natural solution to both these problems is to condition policies with natural language. Language pro-
  vides an intuitive interface for specifying goals and also for implicitly transferring concepts across
  tasks. ([View Highlight](https://read.readwise.io/read/01gph57t5sa8aan76z04b7vray))
- The key
  insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance
  predictions, where the objective is to detect actions rather than detect objects and then learn a policy.
  This action-centric approach to perception [19] is data efﬁcient and effective at circumventing the
  need for explicit “objectness” in learnt representations. ([View Highlight](https://read.readwise.io/read/01gph5g41bwy8hgqnv0qkwbe8n))
    - Note: Transporter Nets
- CLIPORT is an imitation-learning agent based on four key principles: (1) Manipulation through a
  two-step primitive where each action involves a start and ﬁnal end-effector pose. (2) Visual rep-
  resentations of actions that are equivariant to translations and rotations [56, 57]. (3) Two separate
  pathways for semantic and spatial information. (4) Language-conditioned policies for specifying
  goals and also transferring concepts across tasks. C ([View Highlight](https://read.readwise.io/read/01gph5rn3xq2n7t8s6svz57t3r))
- we extend these networks to two-stream architectures that can handle language input. ([View Highlight](https://read.readwise.io/read/01gph67ddetkxc799q192bs18t))
- We extend the Ravens benchmark [2] to 10 language-conditioned. 8 out of 10 tasks have two eval-
  uation variants, denoted by seen and unseen in their names. ([View Highlight](https://read.readwise.io/read/01gph6kf9zew1rzfmmy4ja0p8r))
