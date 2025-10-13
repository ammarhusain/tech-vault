---
aliases: []
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
tags: courses/xcs224u
---


[[courses/xcs224u - natural language understanding/xcs224u - natural language understanding]]

[[courses/xcs224u - natural language understanding/attachments/XCS224U_Mod2-relation-extraction.pdf]]

1. Notebook: [Relation extraction with distant supervision: Task definition](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/rel_ext_01_task.ipynb)
2. Notebook: [Relation extraction with distant supervision: Experiments](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/rel_ext_02_experiments.ipynb)
---

Goal is to create a knowledge triple that contains: a "relation" and then 2 "entities" one being the subject and the other object.

Eg: ("founder", "Elon_Musk", "SpaceX")

# Distant Supervision

The idea is quite simple. It is very hard to hand annotate these "relation triples" in a large corpus of data. Instead we can take an existing knowledge base (KB) that already has a set of relation triples and a corpus of text that has all the entities extracted.

We then take all relation triples from the KB and for each find the sentences in the corpus that those entities are mentioned. We take the context around those entities and mark them as describing the given relation. This way we can create a massive dataset context sentences to learn other relations from.

There are 2 drawbacks to this approach:

1. Not all sentences where the 2 entities are mentioned will describe their relationship. However the benefit of having a huge dataset far outweighs the noise that might be introduced by these false labels.
2. We can only annotate relations that already exist in our knowledge base. There we might be able to discover new entities that share some relationship. But we cannot discover new relationships with this method. Given a decently large KB this problem can also be mitigated because we mostly want to discover more entities & their relation instead.

![[courses/xcs224u - natural language understanding/attachments/xcs224u-relations-generalizations.png]]
