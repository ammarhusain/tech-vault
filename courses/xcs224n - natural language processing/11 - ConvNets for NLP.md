---
aliases: []
created: 2022-09-01-Thursday 14:50
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture11_Slides.pdf]]
[[courses/xcs224n - natural language processing/attachments/cs224n-lecture_notes_viii.pdf]]

Suggested Readings:

1. [Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)
2. [A Convolutional Neural Network for Modelling Sentences](https://arxiv.org/pdf/1404.2188.pdf)
3. [CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/optimization-2/)

---

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image79.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image37.png)

- Interesting idea is to start with 2 copies of word embeddings. Backprop & update through one while keep the other copy of embeddings “static”.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image49.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image12.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image43.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image33.png)

- Interesting idea for Neural MAchine translation: Use a CNN for the encoder and a RNN for the decoder. (Seq2Seq uses RNN for both encoder & decoder).

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image24.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image87.png)
