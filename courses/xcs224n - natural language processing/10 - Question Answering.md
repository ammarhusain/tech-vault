---
aliases: []
created: 2022-09-01-Thursday 14:54
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture10_Slides.pdf]]
[[courses/xcs224n - natural language processing/attachments/cs224n-lecture_notes_vii.pdf]]

---

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image19.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image59.png)- p_i is each word in the passage. Basic idea is to find 2 high attention tokens for the start and end word. Everything in between those 2 words becomes your answer. It assumes that the answer is a substring of the text, which is the case for the SquAD dataset.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image42.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image1.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image18.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image14.png)

- BiDAF is another Question Answering system. Didn't really get the details but the main idea is : attention should flow both ways – from the context to the question and from the question to the context.
- Basically a lot of work in applying the “attention” concept in different and novel ways. For ex: instead of BiLinear attention the learns a weight matrix between 2 vectors (query & target), you could train another neural net (single or deep) to do that mapping.
