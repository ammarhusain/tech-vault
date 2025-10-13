---
aliases: []
tags:
---
# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_200658/eLDWLurv7DfoNmz0cu73_yHfbgZfBEiFs8Fhbzr6P6s-cover_gXltUuN.png)
### Metadata
Author: [[Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Omar Cortes, Byron David, Chelsea Finn, Chuyuan Fu, Keerthana Gopalakrishnan, Karol Hausman, Alex Herzog, Daniel Ho, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Eric Jang, Rosario ...]]
Full Title: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/AIML,  #readwise/doc/robot, ]
URL: https://arxiv.org/pdf/2204.01691.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- We propose to provide real-world grounding by means of pretrained
  skills, which are used to constrain the model to propose natural language actions
  that are both feasible and contextually appropriate. The robot can act as the lan-
  guage model’s “hands and eyes,” while the language model supplies high-level
  semantic knowledge about the task. ([View Highlight](https://read.readwise.io/read/01gnzn32msjwj17vcjjbv9wnja))
- We show how low-level skills can be com-
  bined with large language models so that the language model provides high-level
  knowledge about the procedures for performing complex and temporally extended
  instructions, while value functions associated with these skills provide the ground-
  ing necessary to connect this knowledge to a particular physical environment. ([View Highlight](https://read.readwise.io/read/01gnzn3vhdk1ayj1d5nk3h4jtw))
- We also assume that we are given a set of skills Π, where each skill π ∈ Π performs a short task,
  such as picking up a particular object, and comes with a short language description π (e.g., “ﬁnd a
  sponge”) and an affordance function p(cπ|s, π), which indicates the probability of c-ompleting the
  skill with description π successfully from state s. ([View Highlight](https://read.readwise.io/read/01gnznspvfsk7f66zpm420nxt5))
- This corresponds
  to multiplying the probability of the language description of the skill given the instruction p(π|i),
  which we refer to as task-grounding, and the probability of the skill being possible in the current
  state of the world p(cπ|s, π), which we refer to as world-grounding. ([View Highlight](https://read.readwise.io/read/01gnznxwntmtc8qhsc8wgsbx3y))
- To instantiate SayCan, we must provide it with
  a set of skills, each of which has a policy, a value function, and a short language description (e.g.,
  “pick up the can”). These skills, value functions, and descriptions can be obtained in a variety
  of different ways. In our implementation, we train the individual skills either with image-based
  behavioral cloning, following the BC-Z method [13], or reinforcement learning, following MT-
  Opt [14]. ([View Highlight](https://read.readwise.io/read/01gnzp51hb7r90zedztnf82h0v))
- Inspired by common skills one might pose to a
  robot in a kitchen environment, we propose 551 skills that span seven skill families and 17 objects,
  which include picking, placing and rearranging objects, opening and closing drawers, navigating to
  various locations, and placing objects in a speciﬁc conﬁgurations. ([View Highlight](https://read.readwise.io/read/01gnzq0p0k2bjk3mygnnja74rk))
- The BC models use an architecture similar to BC-Z ... The language instruction is embedded by a universal sentence encoder [15], then used to FiLM
  condition a Resnet-18 based architecture. Unlike the RL model, we do not provide the previous
  action or gripper height, since this was not necessary to learn the policy. Multiple FC layers are
  applied to the ﬁnal visual features, to output each action component (arm position, arm orientation,
  gripper, and the termination action).
- Evaluations are divided by skill (pick up, knock over, place upright, open/close drawers, move object
  close to another one), and within each skill, 18-48 skills are sampled from a predetermined set of
  three objects. Object positions are randomized on each episode, with one or two objects serving as
  a distractor. ([View Highlight](https://read.readwise.io/read/01gnzztqxh6agnrsyn0978t1tj))
    - Note: interesting in terms of setting up [[capabilities benchmarking]]
- For the pick manipulation skills we use a single multi-task, language-conditioned policy,
  for the place manipulation skills we use a scripted policy with an affordance based on the gripper
  state, and for navigation policies we use a planning-based approach which is aware of the locations ... where speciﬁc objects can be found and a distance measure.
- Pick. For pick we use the learned policies in Appendix C and Section 4 with actions from
  BC and value functions from RL trained on the same skill. ([View Highlight](https://read.readwise.io/read/01gnzqp8ky49ezf41w54s6wnab))
- Go to. Since the focus of this work is mainly on planning, we assume the location of
  objects are known. ([View Highlight](https://read.readwise.io/read/01gnzqpgj0m1m3c45z37nyhjsm))
- Place. ... to have a
  consistent place policy across all objects we use a classical motion planning policy.
    - Note: aka this "place" skill is scripted
