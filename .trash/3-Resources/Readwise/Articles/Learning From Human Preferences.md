---
aliases: []
tags:
---
# Learning From Human Preferences

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)
### Metadata
Author: [[openai.com]]
Full Title: Learning From Human Preferences
Category: #readwise/articles
URL: https://openai.com/blog/deep-reinforcement-learning-from-human-preferences/
Date Highlighted: [[2022-07-05-Tuesday]]

## Highlights
- Our AI agent starts by acting randomly in the environment. Periodically, two video clips of its behavior are given to a human, and the human decides which of the two clips is closest to fulfilling its goal — in this case, a backflip. The AI gradually builds a model of the goal of the task by finding the reward function that best explains the human’s judgments. It then uses RL to learn how to achieve that goal. As its behavior improves, it continues to ask for human feedback on trajectory pairs where it’s most uncertain about which is better, and further refines its understanding of the goal.
- We’ve tested our method on a number of tasks in the simulated robotics and Atari domains (without being given access to the reward function: so in Atari, without having access to the game score). Our agents can learn from human feedback to achieve strong and sometimes superhuman performance in many of the environments we tested.
