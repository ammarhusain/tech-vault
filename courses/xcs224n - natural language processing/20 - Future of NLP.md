---
aliases: []
created: 2022-09-01-Thursday 15:44
modified: 2023-03-10-Friday 23:15
tags: courses/xcs224n, aiml, aiml/nlp, courses/stanford
---


---

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture20_Slides.pdf]]

---

- (i) Harnessing unlabeled data: Backtranslation and Unsupervised Machine Translation,
- (ii) Scaling up pre-training and models.
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image16.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image36.png)
- Here step 1 uses unlabeled language data while step 2 uses the labeled translations (bilingual) dataset.
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image78.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image57.png)
- This is a neat idea for learning totally unsupervised translations. Basically you learn two sets of word embeddings for each language. Then try and learn an orthogonal mapping matrix W that can map embeddings from one space /language to another. The assumption here is that embedding structure should be similar across languages (like the horse shoe). What is unclear to me is if this technique expects word to word translations or not even that.
- Anyway once you have learned the embeddings, then you can use adversarial techniques (similar to discriminator of a GAN) to say which language a given embedding belongs to. Keep training W & discriminator iteratively until it gets fooled.
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image70.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image56.png)
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image74.png)
- This works decently for cases where we don’t have too many parallel translations (< 10^5). However it also seems to work for languages that have more similar structure (Eng, Fr, German etc) but doesn’t do well translating English to Turkish for ex.
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image76.png) ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image88.png)
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image31.png)
- GLUE benchmark is a compendium of 10 NLU tasks, sQuAD: Stanford question answering dataset.
