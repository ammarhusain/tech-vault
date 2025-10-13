---
aliases: []
created: 2022-09-01-Thursday 15:40
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture17_Slides.pdf]]

---

- Broad categories of NLP tasks:
- Sequence tagging: Named Entity recognition, ...
- Text classification: sentiment analysis, ...
- Seq2seq: [[courses/xcs224n - natural language processing/8-9 - Machine Translation, Seq2Seq and Attention|machine translation]], summarization, question answering
- Multitask learning is using the same model to learn different tasks. In this case, the tasks don’t have specific heads. The output is a weighted combo of: Question pointer, Context pointer and a softmax over vocabulary.
- It turns out pointing is super important for most tasks other than [[courses/xcs224n - natural language processing/8-9 - Machine Translation, Seq2Seq and Attention|machine translation]]. Pointing is an output that points back to a word or phrase in the input (question or context).
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image47.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image40.png)
