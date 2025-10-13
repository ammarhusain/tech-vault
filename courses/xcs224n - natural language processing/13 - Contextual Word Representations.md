---
aliases: []
created: 2022-09-01-Thursday 14:59
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

# 13 - Contextual Word Representations

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture13_Slides.pdf]]

Suggested readings:

1. Smith, Noah A. [Contextual Word Representations: A Contextual Introduction](https://arxiv.org/abs/1902.06006). (Published just in time for this lecture!)
2. [The Illustrated BERT, ELMo, and co.](http://jalammar.github.io/illustrated-bert/)

---
- Up until now we said we have just one representation for a word: Word2Vec, GloVe.
- We can just start with random word vectors and train them on our task of interest. But in most cases, use of pre-trained word vectors helps, because we can train them for more words on much more data
- Map all rare words (<5 times occur) to "UNK" token. No way to distinguish different UNK tokens, either for identity or meaning.
- Few things to try in dealing with UNK tokens:
- If the UNK word at test time appears in your unsupervised word embeddings, use that vector as is at test time. (helps a lot). I.e. if you are using pre trained embeddings.
- For other words, just assign them a random vector, adding them to your vocabulary (may help)
- Collapse things to word classes (like unknown number, capitalized thing, etc. and having an UNK for each.
- Problems with just one word embedding: (a) Always same representation for work token regardless of context in which word token occurs, (b) Words can have different aspects like syntactic semantic, connotations.
- In Neural Language Models we took word vectors and stuck them through LSTM layers and trained them to predict the next word. The LSTM hidden states are already producing context specific word representations at each position.
- TagLM key idea:  Want meaning of word in context, but standardly learn task RNN only on small task-labeled data (e.g., NER). Why don’t we do semi-supervised approach where we train NLM on large unlabeled corpus, rather than just word vectors?
![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image81.png)

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image21.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image51.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image39.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image20.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image27.png)

- GPT, BERT and GPT-2 are all [[transformer]] based architectures.
- BERT (Bidirectional Encoder Representations from [[transformer|Transformers]]): Language Models are inherently unidirectional. They predict the probability of the next word given previously seen words. You could train a bidirectional encoder but then this would cause “cross-talk” as in words can see themselves.
- BERT uses the idea that instead of learning a language model, they mask out k% of the input words, and then predict the masked words. They always use k = 15% since there is a tradeoff between masking out too many words (lose context) and masking out too little (too expensive to train).
- They also use the “Next sentence prediction” in their training objective. That is they take two sentences and try to learn whether the second sentence is the next logical sentence or just a random one from the training data. That is the segment embedding E_A & E_B in the figure below. The positional embedding is for the [[transformer]] architecture and the token embedding is the word embedding we’ve seen before.
- GPT-2 uses only decoder [[transformer]] blocks.
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image69.png)
- ![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image5.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image60.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image35.png)
