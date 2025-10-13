---
aliases: 
tags:
  - readwise/doc/aiml
---
# ALFRED A Benchmark for Interpreting Grounded Instructions for Everyday Tasks

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)
### Metadata
Author: [[arxiv.org]]
Full Title: ALFRED A Benchmark for Interpreting Grounded Instructions for Everyday Tasks
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://arxiv.org/pdf/1912.01734.pdf
Date Highlighted: [[2023-01-12-Thursday]]

## Highlights
- We present ALFRED (Action Learning From Realistic
  Environments and Directives), a benchmark for learning
  a mapping from natural language instructions and ego-
  centric vision to sequences of actions for household tasks. ([View Highlight](https://read.readwise.io/read/01gphap7ver5vp8rwme81z3010))
- ALFRED con-
  sists ofexpert demonstrations in interactive visual environ-
  ments for 25k natural language directives. These direc-
  tives contain both high-level goals like “Rinse off a mug
  and place it in the coffee maker.” and low-level language
  instructions like “Walk to the coffee maker on the right.”
  ALFRED tasks are more complex in terms of sequence
  length, action space, and language than existing vision-
  and-language task datasets. ([View Highlight](https://read.readwise.io/read/01gpharx0qqvg6v4zk4hb23r0r))
- ALFRED includes 25,743 English language directives
  describing 8,055 expert demonstrations averaging 50 steps
  each, resulting in 428,322 image-action pairs. ([View Highlight](https://read.readwise.io/read/01gphbhyjmajfdvxv7qm84jvm2))
- Motivated
  by work in robotics on segmentation-based grasping [37],
  agents in ALFRED interact with objects visually, specify-
  ing a pixelwise interaction mask of the target object. This
  inference is more realistic than simple object class pre-
  diction, where localization is treated as a solved problem. ([View Highlight](https://read.readwise.io/read/01gphbjmep740m05sbx5y3g8q8))
- ALFRED facilitates learning models that
  translate from language to sequences of actions and interac-
  tions in a visually and physically realistic simulation envi-
  ronment. This benchmark captures many challenges present
  in real-world settings for translating human language to
  robot actions for accomplishing household tasks. ([View Highlight](https://read.readwise.io/read/01gphbp909cqjd3ecd3tyd7czt))
- Each expert demonstration can be de-
  terministically replayed in the AI2-THOR 2.0 simulator. ([View Highlight](https://read.readwise.io/read/01gphbrjcbxsfbr7g1hy11h4hr))
- Expert demonstrations are composed of an agent’s ego-
  centric visual observations of the environment and what ac-
  tion is taken at each timestep as well as ground-truth in-
  teraction masks. ([View Highlight](https://read.readwise.io/read/01gphbrymtr0g1pdrc63yp31dt))
- Navigation actions move the agent or change
  its camera orientation, while manipulation actions include
  picking and placing objects, opening and closing cabinets
  and drawers, and turning appliances on and off. ([View Highlight](https://read.readwise.io/read/01gphbsh9vxe09w8y15n274p7a))
- An agent trained for ALFRED tasks needs to jointly rea-
  son over vision and language input and produce a sequence
  of low-level actions to interact with the environment. ([View Highlight](https://read.readwise.io/read/01gphnyadwtb65dtex7zar35gh))
- AMT workers are told to write instructions to tell a
  “smart robot” how to accomplish what is shown in a video. ([View Highlight](https://read.readwise.io/read/01gphnvvyq1gwwvts2b96ebkpm))
- We model the interactive agent with a CNN-LSTM
  sequence-to-sequence (SEQ2SEQ) architecture. ACNN en-
  odes the visual input, a bidirectional-LSTM generates a rep-
  resentation of the language input, and a decoder LSTM in-
  fers a sequence of low-level actions while attending over
  the encoded language. ([View Highlight](https://read.readwise.io/read/01gphnyv5bckw2nkj26j33w0dr))
- The agent chooses from among 13 actions. There
  are 5 navigation actions: MoveAhead, RotateRight,
  RotateLeft, LookUp, and LookDown together with
  7 interaction actions: Pickup, Put, Open, Close,
  ToggleOn, ToggleOff, and Slice. Interaction actions
  require a pixelwise mask to denote the object of interest.1
  Finally, the agent predicts a Stop action to end the episode. ([View Highlight](https://read.readwise.io/read/01gphp6zrerse8xyv9adx6hzrh))
- The goal-condition success of
  a model is the ratio of goal-conditions completed at the end
  of an episode to those necessary to have ﬁnished a task. For
  example, in the previous Heat & Place example, there are
  four goal-conditions. First, a potato must be sliced. Sec-
  ond, a potato slice should become heated. Third, a potato
  slice should come to rest on a counter top. Fourth, the same
  potato slice that is heated should be on the counter top. ([View Highlight](https://read.readwise.io/read/01gphceczbxeppcccf8v9v3r5s))
    - Note: this could also be used in "skills" benchmarking - did the arm reach a graspable pose?, did the gripper open?, did it pick object up?, was it vertical?

