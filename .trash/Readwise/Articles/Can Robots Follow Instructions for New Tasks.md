---
aliases: []
tags:
---
# Can Robots Follow Instructions for New Tasks?

![rw-book-cover](https://blogger.googleusercontent.com/img/a/AVvXsEh18FvGNYPAA8EixR3uGpEp8bJRGYSi5mEQEVEfDzRrV2O0BBqUnXumes0NrNsBU0oQvbgvzGIsrND3Tfw8Wt6TvrzFSwW7Jz0bda6eJdVxDIMJs_4pdTmo_BtPZazyOb2ix035q_a3s9tAqs7PFD2TFq5JiTTxATT0JzuUvr-KLhcisii9dleRYVURKg=s72-w640-c-h406)
### Metadata
Author: [[googleblog.com]]
Full Title: Can Robots Follow Instructions for New Tasks?
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://ai.googleblog.com/2022/02/can-robots-follow-instructions-for-new.html
Date Highlighted: [[2022-12-19-Monday]]

## Highlights
- The system, called BC-Z, comprises two key components: (*i*) the collection of a large-scale demonstration dataset covering 100 different tasks and (*ii*) a neural network policy conditioned on a language or video instruction of the task. The resulting system can perform at least 24 novel tasks, including ones that require interaction with pairs of objects that were not previously seen together. ([View Highlight](https://read.readwise.io/read/01gmp7195ez6zevqm39p5mrcb6))
- [![](https://blogger.googleusercontent.com/img/a/AVvXsEh18FvGNYPAA8EixR3uGpEp8bJRGYSi5mEQEVEfDzRrV2O0BBqUnXumes0NrNsBU0oQvbgvzGIsrND3Tfw8Wt6TvrzFSwW7Jz0bda6eJdVxDIMJs_4pdTmo_BtPZazyOb2ix035q_a3s9tAqs7PFD2TFq5JiTTxATT0JzuUvr-KLhcisii9dleRYVURKg=w640-h406)](https://blogger.googleusercontent.com/img/a/AVvXsEh18FvGNYPAA8EixR3uGpEp8bJRGYSi5mEQEVEfDzRrV2O0BBqUnXumes0NrNsBU0oQvbgvzGIsrND3Tfw8Wt6TvrzFSwW7Jz0bda6eJdVxDIMJs_4pdTmo_BtPZazyOb2ix035q_a3s9tAqs7PFD2TFq5JiTTxATT0JzuUvr-KLhcisii9dleRYVURKg=s1500) ([View Highlight](https://read.readwise.io/read/01gmp904hsbj3ceqt546xr9xd2))
- In language models, it is well known that sentence embeddings generalize on compositions of concepts encountered in training data. For instance, if you train a translation model on sentences like “pick up a cup” and “push a bowl”, the model should also translate “push a cup” correctly.
  We study the question of whether the compositional generalization capabilities found in language encoders can be transferred to real robots, i.e., being able to compose unseen object-object and task-object pairs. ([View Highlight](https://read.readwise.io/read/01gmp8v15tkj70c0ag7nmsw7v9))
- The results of this research show that simple imitation learning approaches can be scaled in a way that enables zero-shot generalization to new tasks. That is, it shows one of the first indications of robots being able to successfully carry out behaviors that were not in the training data. ([View Highlight](https://read.readwise.io/read/01gmp8xgb1e29g06gnbbhr5sp1))
- Interestingly, language embeddings pre-trained on ungrounded language corpora make for excellent task conditioners. We demonstrated that natural language models can not only provide a flexible input interface to robots, but that pretrained language representations actually confer new generalization capabilities to the downstream policy, such as composing unseen object pairs together. ([View Highlight](https://read.readwise.io/read/01gmp8y7rj48v17k0kp0e2bfaj))
---
aliases: []
tags:
---
# Can Robots Follow Instructions for New Tasks?

![rw-book-cover](https://blogger.googleusercontent.com/img/a/AVvXsEh18FvGNYPAA8EixR3uGpEp8bJRGYSi5mEQEVEfDzRrV2O0BBqUnXumes0NrNsBU0oQvbgvzGIsrND3Tfw8Wt6TvrzFSwW7Jz0bda6eJdVxDIMJs_4pdTmo_BtPZazyOb2ix035q_a3s9tAqs7PFD2TFq5JiTTxATT0JzuUvr-KLhcisii9dleRYVURKg=s72-w640-c-h406)
### Metadata
Author: [[googleblog.com]]
Full Title: Can Robots Follow Instructions for New Tasks?
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://ai.googleblog.com/2022/02/can-robots-follow-instructions-for-new.html
Date Highlighted: [[2023-08-09-Wednesday]]

## Highlights
- The system, called BC-Z, comprises two key components: (*i*) the collection of a large-scale demonstration dataset covering 100 different tasks and (*ii*) a neural network policy conditioned on a language or video instruction of the task. The resulting system can perform at least 24 novel tasks, including ones that require interaction with pairs of objects that were not previously seen together. ([View Highlight](https://read.readwise.io/read/01gmp7195ez6zevqm39p5mrcb6))
- [![](https://blogger.googleusercontent.com/img/a/AVvXsEh18FvGNYPAA8EixR3uGpEp8bJRGYSi5mEQEVEfDzRrV2O0BBqUnXumes0NrNsBU0oQvbgvzGIsrND3Tfw8Wt6TvrzFSwW7Jz0bda6eJdVxDIMJs_4pdTmo_BtPZazyOb2ix035q_a3s9tAqs7PFD2TFq5JiTTxATT0JzuUvr-KLhcisii9dleRYVURKg=w640-h406)](https://blogger.googleusercontent.com/img/a/AVvXsEh18FvGNYPAA8EixR3uGpEp8bJRGYSi5mEQEVEfDzRrV2O0BBqUnXumes0NrNsBU0oQvbgvzGIsrND3Tfw8Wt6TvrzFSwW7Jz0bda6eJdVxDIMJs_4pdTmo_BtPZazyOb2ix035q_a3s9tAqs7PFD2TFq5JiTTxATT0JzuUvr-KLhcisii9dleRYVURKg=s1500) ([View Highlight](https://read.readwise.io/read/01gmp904hsbj3ceqt546xr9xd2))
- In language models, it is well known that sentence embeddings generalize on compositions of concepts encountered in training data. For instance, if you train a translation model on sentences like “pick up a cup” and “push a bowl”, the model should also translate “push a cup” correctly.
  We study the question of whether the compositional generalization capabilities found in language encoders can be transferred to real robots, i.e., being able to compose unseen object-object and task-object pairs. ([View Highlight](https://read.readwise.io/read/01gmp8v15tkj70c0ag7nmsw7v9))
- The results of this research show that simple imitation learning approaches can be scaled in a way that enables zero-shot generalization to new tasks. That is, it shows one of the first indications of robots being able to successfully carry out behaviors that were not in the training data. ([View Highlight](https://read.readwise.io/read/01gmp8xgb1e29g06gnbbhr5sp1))
- Interestingly, language embeddings pre-trained on ungrounded language corpora make for excellent task conditioners. We demonstrated that natural language models can not only provide a flexible input interface to robots, but that pretrained language representations actually confer new generalization capabilities to the downstream policy, such as composing unseen object pairs together. ([View Highlight](https://read.readwise.io/read/01gmp8y7rj48v17k0kp0e2bfaj))

