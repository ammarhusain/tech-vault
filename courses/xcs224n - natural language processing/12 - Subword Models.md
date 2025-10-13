---
aliases: []
created: 2022-09-01-Thursday 14:59
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture12_Slides.pdf]]

Suggested readings:

1. Minh-Thang Luong and Christopher Manning. [Achieving Open Vocabulary Neural Machine Translation with Hybrid Word-Character Models](https://arxiv.org/abs/1604.00788)

---
- Easier lecture… No new deep networks context.
- Phonemes: Phonology posits a small set or sets of distinctive, categorical units, aka basic sounds.
- Morphemes: “smallest” semantic unit of a word [un][fortun(e)][ate][ly] . Which basically means one or more inflections is added to the “root” to modify meaning/grammar.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image13.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image71.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image67.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image15.png)

- Byte Pair Encoding: Originally a compression algorithm. Its like a bottom up clustering to do word segmentation.
- Start with a unigram vocabulary of all characters (unicode) in your data.
- Most frequent ngram pairs -> becomes a new ngram in your vocabulary.
- Continue clustering this way until a max vocabulary size is reached (8-20k).
- Do deterministic segmentation of words. Vocabulary is now automatically decided for the system (frequency based).
- Wordpiece model tokenizes inside words. Sentencepiece model tokenizes entire sentences. Whitespace is retained as just another special token and clustered normally.
- You dont necessarily need word embeddings to build language models. You can compose “building blocks” to obtain nuanced and powerful models!
