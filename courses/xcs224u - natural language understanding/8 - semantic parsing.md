---
created: 2022-09-05-Monday 21:41
modified: 2023-03-10-Friday 23:15
---

[[courses/xcs224u - natural language understanding/attachments/XCS224U_Mod8_Slides.pdf]]
[https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-0.ipynb](https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-0.ipynb) [https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-1.ipynb](https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-1.ipynb) [https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-2.ipynb](https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-2.ipynb) [https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-3.ipynb](https://nbviewer.jupyter.org/github/wcmac/sippycup/blob/master/sippycup-unit-3.ipynb)

![attachments/Untitled%2022.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2022.png)

**Goal of semantic parsing** is to do a precise, complete interpretation of linguistic inputs and to map those inputs into structures machine-readable representations of meaning.

![attachments/Untitled%2023.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2023.png)

Outline of approach:

- Define possible syntactic structures using a context-free grammar
- Construct semantics bottom-up, following syntactic structure
- Leverage annotators for names, numbers, places, times, ...
- Score parses with a log-linear model learned from training data
- Use grammar induction to avoid manual grammar engineering

![attachments/Untitled%2024.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2024.png)

![attachments/Untitled%2025.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2025.png)

Try to map natural language to some other machine understandable language like SQL or other querying systems that can then be executed as a program.

![attachments/Untitled%2026.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2026.png)

Run some kind of an entity recognition annotator that goes through the text and annotates words/phrases that it recognizes and tags them with their corresponding entities. It could be a combination of [Freebase](https://en.wikipedia.org/wiki/Freebase_(database)) + personalized things like contact info etc.

![attachments/Untitled%2027.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2027.png)

Ambiguity: could be both syntactic and semantic ambiguity.

Since these context free grammars (CFG) will be rich they would most likely yield multiple derivations (natural language → query).

You can try and come up with a bunch of hand engineered features and then learn a weight vector $\theta$ (linear in this case). Once you have good learned weights you could use simple softmax (logistic regression) to figure out which is the best derivation.

![attachments/Untitled%2028.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2028.png)

EM algorithms are good at estimating latent variables (z in our case, since we only have y annotations).

![attachments/Untitled%2029.png](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%2029.png)

Learning from denotation (kind of ties closely with my idea of tying in reinforcement learning):

Basic idea is to not have human annotators annotate parses (ie queries that should be generated given natural language sentence). But have them annotate answers to those queries. Then you should generate your own parses and run those generated queries through your system and compare the answer with what the human annotator provided.

- Problem: examples annotated with semantics are expensive
  - Solution: learn from **indirect supervision**, using the results of evaluating the semantics (e.g., **learning from denotations**)
