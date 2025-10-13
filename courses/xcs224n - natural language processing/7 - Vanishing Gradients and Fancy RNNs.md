---
aliases: []
created: 2022-09-01-Thursday 14:42
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

# 7 - Vanishing Gradients and Fancy Rnns

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture7_Slides.pdf]]

Suggested Readings:

1. [Sequence Modeling: Recurrent and Recursive Neural Nets](http://www.deeplearningbook.org/contents/rnn.html) (Sections 10.3, 10.5, 10.7-10.12)
2. [Learning long-term dependencies with gradient descent is difficult](http://ai.dinfo.unifi.it/paolo//ps/tnn-94-gradient.pdf) (one of the original vanishing gradient papers)
3. [On the difficulty of training Recurrent Neural Networks](https://arxiv.org/pdf/1211.5063.pdf) (proof of vanishing gradient problem)
4. [Vanishing Gradients Jupyter Notebook](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/lectures/vanishing_grad_example.html) (demo for feedforward networks)
5. [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) (blog post overview)

---

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image38.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image46.png)

- Vanishing gradients is bad because we aren’t able to capture further away context dependencies between t and t+n. End up with more recency bias which defeats the point of having a sequence model to capture these contextual relations.
- Opposite problem is exploding gradients if W>1. This is also bad and may result in Nan or Inf parameter values. Could also make SGD take large update steps into bad regions.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image30.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image45.png)

- LSTM doesn’t guarantee that there is no vanishing or exploding gradients, but it provides an internal representation/memory closer to the hidden state that can control how much of the context to remember. Rather than depending only on the hidden state for that.
- Use LSTM as default choice since it usually works better. Switch to GRU if you want it to be more efficient/faster.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image86.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image68.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image54.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image8.png)

- Multi-layer RNNs = Stacked RNNs

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image26.png)
