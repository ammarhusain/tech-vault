---
aliases: []
tags:
---
# Human Preferences

![rw-book-cover](https://openai.com/content/images/2022/05/twitter-1.png)
### Metadata
Author: [[OpenAI]]
Full Title: Human Preferences
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://openai.com/blog/deep-reinforcement-learning-from-human-preferences/
Date Highlighted: [[2022-12-17-Saturday]]

## Highlights
- Our AI agent starts by acting randomly in the environment. Periodically, two video clips of its behavior are given to a human, and the human decides which of the two clips is closest to fulfilling its goal — in this case, a backflip. The AI gradually builds a model of the goal of the task by finding the reward function that best explains the human’s judgments. It then uses RL to learn how to achieve that goal. As its behavior improves, it continues to ask for human feedback on trajectory pairs where it’s most uncertain about which is better, and further refines its understanding of the goal. ([View Highlight](https://read.readwise.io/read/01gmgbematmc9e0b95m77metep))
- Our approach demonstrates promising sample efficiency — as stated previously, the backflip video required under 1000 bits of human feedback. It took less than an hour of a human evaluator’s time, while in the background the policy accumulated about 70 hours of overall experience (simulated at a much faster rate than real-time.) ([View Highlight](https://read.readwise.io/read/01gmgbh4kjtjaknb5mthmdcxg3))
- We’ve tested our method on a number of tasks in the simulated robotics and Atari domains (without being given access to the reward function: so in Atari, without having access to the game score). Our agents can learn from human feedback to achieve strong and sometimes superhuman performance in many of the environments we tested. ([View Highlight](https://read.readwise.io/read/01gmgbk5jsxc595q1tyjvjvzzq))
- We also sometimes find that learning from feedback does better than reinforcement learning with the normal reward function, because the human shapes the reward better than whoever wrote the environment’s reward. ([View Highlight](https://read.readwise.io/read/01gmgbmkh4tb6jmyvevdvq8z2q))
---
aliases: []
tags:
---
# Human Preferences

![rw-book-cover](https://openai.com/assets/images/favicon.svg?v=cdd1ea0542)
### Metadata
Author: [[OpenAI]]
Full Title: Human Preferences
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://openai.com/blog/deep-reinforcement-learning-from-human-preferences/
Date Highlighted: [[2023-08-09-Wednesday]]

## Highlights
- Our AI agent starts by acting randomly in the environment. Periodically, two video clips of its behavior are given to a human, and the human decides which of the two clips is closest to fulfilling its goal — in this case, a backflip. The AI gradually builds a model of the goal of the task by finding the reward function that best explains the human’s judgments. It then uses RL to learn how to achieve that goal. As its behavior improves, it continues to ask for human feedback on trajectory pairs where it’s most uncertain about which is better, and further refines its understanding of the goal. ([View Highlight](https://read.readwise.io/read/01gmgbematmc9e0b95m77metep))
- Our approach demonstrates promising sample efficiency — as stated previously, the backflip video required under 1000 bits of human feedback. It took less than an hour of a human evaluator’s time, while in the background the policy accumulated about 70 hours of overall experience (simulated at a much faster rate than real-time.) ([View Highlight](https://read.readwise.io/read/01gmgbh4kjtjaknb5mthmdcxg3))
- We’ve tested our method on a number of tasks in the simulated robotics and Atari domains (without being given access to the reward function: so in Atari, without having access to the game score). Our agents can learn from human feedback to achieve strong and sometimes superhuman performance in many of the environments we tested. ([View Highlight](https://read.readwise.io/read/01gmgbk5jsxc595q1tyjvjvzzq))
- We also sometimes find that learning from feedback does better than reinforcement learning with the normal reward function, because the human shapes the reward better than whoever wrote the environment’s reward. ([View Highlight](https://read.readwise.io/read/01gmgbmkh4tb6jmyvevdvq8z2q))

