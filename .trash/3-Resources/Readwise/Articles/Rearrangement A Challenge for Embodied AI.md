---
aliases: []
tags:
---
# Rearrangement: A Challenge for Embodied AI

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)
### Metadata
Author: [[Dhruv Batra, Angel X. Chang, Sonia Chernova, Andrew J. Davison, Jia Deng, Vladlen Koltun, Sergey Levine, Jitendra Malik, Igor Mordatch, Roozbeh Mottaghi, Manolis Savva, Hao Su]]
Full Title: Rearrangement: A Challenge for Embodied AI
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robot, ]
URL: https://arxiv.org/pdf/2011.01975.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- In the rearrange-
  ment task, the goal is to bring a given physical environ-
  ment into a speciﬁed state. The goal state can be speciﬁed
  by object poses, by images, by a description in language,
  or by letting the agent experience the environment in the
  goal state. ([View Highlight](https://read.readwise.io/read/01gpkrsd5e4hrpbn7xs674bj4s))
- Rearrangement is thus a compre-
  hensive framework for research and evaluation in Embodied
  AI that subsumes component skills such as navigation and
  manipulation and integrates them into a broader roadmap
  towards embodied intelligence. ([View Highlight](https://read.readwise.io/read/01gpksffs44z4b0rtxptc1yfky))
- We propose rearrangement as a canonical task for Em-
  bodied AI because it naturally uniﬁes instances that are of
  clear practical interest: setting the table, cleaning the bed-
  room, loading the dishwasher, picking and placing orders
  in a fulﬁllment center, rearranging the furniture, and many
  more. Rearrangement scenarios can be deﬁned with station-
  ary manipulators that operate locally or with mobile sys-
  tems that traverse complex scenes such as houses and apart-
  ments ([View Highlight](https://read.readwise.io/read/01gpksa50m2njs2w568rma43mf))
- we delib-
  erately exclude within-object transformations, such as melt-
  ing (spot welding, soldering), destruction (cutting, drilling,
  sanding), and non-rigid dynamics (liquids, ﬁlms, cloths,
  or ropes). Thus boiling water, chopping onions, stomping
  grapes, pouring coffee, making a smoothie, folding towels,
  ironing clothes, or making a bed are considered beyond the
  scope of the presented framework. ([View Highlight](https://read.readwise.io/read/01gpksbb5t1hvbqt8kwzdzhgn1))
- A PredicateGoal can be pre-
  cisely speciﬁed and evaluated by deﬁning the predi-
  cates (e.g. supported by, inside, is on), the sym-
  bols on which they act (e.g. plate, pizza, table,
  microwave), and their grounding to objects and rela-
  tions. ([View Highlight](https://read.readwise.io/read/01gpkvg39jaby7gw4wexdv5waa))
- On one extreme
  of the spectrum (‘weak generalization’) a system is evalu-
  ated with known objects in known environments, with only
  the arrangements of the objects being novel (i.e., there is
  a closed set of objects and environments shared between
  training and evaluation). On the other side of the spectrum
  (‘strong generalization’), the agent is tasked with rearrang-
  ing new objects in new environments, never encountered
  during training. ([View Highlight](https://read.readwise.io/read/01gpktka0wpf0rwe0wryrkmwzs))
- A rearrangement task requires an agent (or agents) to ac-
  complish a many-to-many transformation of a scene, and
  evaluation of success will necessarily therefore require the
  design of composite metrics which capture the quality of an
  overall performance. ([View Highlight](https://read.readwise.io/read/01gpkv71v3smjxxkxj6hxjg86d))
- The most obvious use for more general predicates is to
  allow for tests of the relative poses of objects. For instance,
  if a saucer must be placed on a table, and a cup on the
  saucer, one predicate would set a threshold on the relative
  pose of the saucer and the table, and another on the relative
  pose of the cup and saucer. ([View Highlight](https://read.readwise.io/read/01gpkvndvkn3tz3c4bzrq6pes8))
