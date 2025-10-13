---
aliases: []
created: 2022-09-01-Thursday 14:37
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

# 6 - Language Models & Recurrent Neural Networks

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture6_Slides.pdf]]
[[courses/xcs224n - natural language processing/attachments/cs224n-lecture_notes_v.pdf]]

Suggested Readings:

1. [N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf) (textbook chapter)
2. [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) (blog post overview)
3. [Sequence Modeling: Recurrent and Recursive Neural Nets](http://www.deeplearningbook.org/contents/rnn.html) (Sections 10.1 and 10.2)
4. [On Chomsky and the Two Cultures of Statistical Learning](http://norvig.com/chomsky.html)

---

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image85.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image6.png)

- N-grams: Major problems are sparsity (what if you never saw the n word combo) & storage (have to keep track of all diff n-word combos).

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image83.png) ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image3.png)

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image32.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image48.png)

- In addition to Language Modeling, RNNs can be used for tagging (part-of-speech: noun, pronoun; named entity recognition), sentiment classification, encoding sentences for question-answering, machine-translation, etc.
