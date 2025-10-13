---
created: 2022-09-05-Monday 21:37
modified: 2023-03-10-Friday 23:15
---

[[courses/xcs224u - natural language understanding/attachments/XCS224U_Mod7_Slides 1.pdf]]

1. Notebook: [Overview of the Stanford Sentiment Treebank](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/sst_01_overview.ipynb)
2. Notebook: [Hand-built feature functions](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/sst_02_hand_built_features.ipynb)
3. Notebook: [Dense feature representations and neural networks](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/sst_03_neural_networks.ipynb)

---

- Tokenization is an important first step. Use a good domain specific tokenizer for your dataset. Eg: for social media text (aka tweets) a good start is `nltk.tokenize.casual.TweetTokenizer`
	 - There is also some sentiment aware tokenizer in nltk
- Though its unclear with sequence models (RNNs [[transformer|Transformers]] gaining more and more popularity, if just going character level (or word level) working about the same. In any case, decent tokenization is generally a good start.
- **Stemming**: is to heuristically collapse different word together by trimming off their ends. Egs: thinking, thinks → think. DON'T DO IT! It rarely helps

![attachments/Untitled%2010.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2010.png)

- Wordnet stemmer takes into account the part of speech (POS) tag of the word as well (verb, adjective, noun etc) to better collapse. Better but still loses a lot of good info.
- Simple negation marking: Append a _NEG suffix to every word to every word appearing between a negation and a clause-level punctuation mark.

![attachments/Untitled%2011.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2011.png)

- [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/): Sentence level corpus (10,662 sent), data from Rotten Tomatoes.
	 - Fully labeled trees with 5-way labels.

![attachments/Untitled%2012.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2012.png)

![attachments/Untitled%2013.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2013.png)

Bunch of stuff around how Potts' ML wrappers are structured. This would have been good to know before the first 4 homeworks so I didnt have to figure it out myself.

![attachments/Untitled%2014.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2014.png)

![attachments/Untitled%2015.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2015.png)

![attachments/Untitled%2016.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2016.png)

![attachments/Untitled%2017.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2017.png)

**Classifier comparison:** Is the difference between two models B & M really of significance?

- Demsar (2006) advises the Wilcoxon signed-rank test for situations in which you can afford to repeatedly assess B and M on different train/test splits.

![attachments/Untitled%2018.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2018.png)

- For situations where you can’t repeatedly assess B and M, McNemar’s test is a reasonable alternative. It operates on the confusion matrices produced by the two models, testing the null hypothesis that the two models have the same error rate.

![attachments/Untitled%2019.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2019.png)

A bunch of ideas around hand built features that exploit the tree structure.

![attachments/Untitled%2020.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2020.png)

It's good to combine multiple features together to build a linear model (sklearn.feature_selection offers functions to assess how much information your feature functions contain with respect to your labels.)

**Tree structured RNN**

![attachments/Untitled%2021.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2021.png)
