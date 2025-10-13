---
aliases: [machine translation]
created: 2022-09-01-Thursday 14:47
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

# 8 - Machine Translation, SEQ2SEQ and Attention

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture8_Slides.pdf]]
[[courses/xcs224n - natural language processing/attachments/cs224n-lecture_notes_vi.pdf]]

Suggested Readings:

1. [Statistical Machine Translation slides, CS224n 2015](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1162/syllabus.shtml) (lectures 2/3/4)
2. [Statistical Machine Translation](https://www.cambridge.org/core/books/statistical-machine-translation/94EADF9F680558E13BE759997553CDE5) (book by Philipp Koehn)
3. [BLEU](https://www.aclweb.org/anthology/P02-1040.pdf) (original paper)
4. [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf) (original seq2seq NMT paper)
5. [Sequence Transduction with Recurrent Neural Networks](https://arxiv.org/pdf/1211.3711.pdf) (early seq2seq speech recognition paper)
6. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf) (original seq2seq+attention paper)
7. [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/) (blog post overview)
8. [Massive Exploration of Neural Machine Translation Architectures](https://arxiv.org/pdf/1703.03906.pdf) (practical advice for hyperparameter choices)
---

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image41.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image62.png)

- We actually try and learn P(x,a | y) where a is the alignment that is word level correspondence. It depends on position in sentence, word mapping etc.
- Get a bit more clarity on decoding for SMT (or is that even needed?)

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image77.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image28.png)

- Many NLP tasks can be framed as Seq2seq: Summarization, Dialogue, Parsing, Code Generation.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image2.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image22.png)

- Greedy decoding is when you take the argmax word at every decoder hidden state. Though it's not that good because there is no way to undo decisions or backtrack.
- In beam search just pick the final hypothesis from a set that was created by picking the one with the highest sum of log likelihood. Make sure to normalize by length of sentence otw the shorter sentences will always win.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image44.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image52.png)

- Existing issues with NMT: less interpretable, difficult to control by specifying rules/guidelines.
- Can't deal with out of vocabulary words; Domain mismatch between train & test; maintaining context over longer texts; low resource language pairs.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image7.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image34.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image64.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image58.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image50.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image84.png)

- In general terms: Given a set of vector values, and a vector query, Attention is a technique to compute a weighted sum of the values, dependent on the query.
- Weighted sum is a selective summary of the information contained in the values, where the query determines which value to focus on.
- Attention is a way to obtain a fixed size representation of an arbitrary set of representations (values), dependent on some other representation (query).
- Second attention variant is a form of bilinear function (W) applied to encoder & decoder hidden state. Third one is a linear function applied to each (W1, W2).

---

# 9 - More on Grus and Nmt

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture9_Slides.pdf]]

- Adaptive adding as in [alpha*h_t + (1-alpha)*h_t-1] is a powerful idea that is used even in ResNets. That is take alpha times current quantity and the rest of the previous quantity. This gets rid of some of the vanishing gradients type problems.
- GRUs have 2 gates: update & reset. Update gate determines how much to keep off the current activation vs how much to keep from older activations. Reset gate determines how much of the previous activation should we just discard/zero out.
- Reset gate is helpful for periods (full stop) in sentences. After that's been encountered we can reset a lot of the stored hidden state.
