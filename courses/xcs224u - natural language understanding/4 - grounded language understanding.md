---
created: 2022-09-05-Monday 21:25
modified: 2023-03-10-Friday 23:15
---

[[courses/xcs224u - natural language understanding/attachments/XCS224U_Mod4_Slides.pdf]]

1. Notebook: [Pragmatic color describers](https://nbviewer.jupyter.org/github/cgpotts/cs224u/blob/2020-spring/colors_overview.ipynb)

Grounding here means getting the broader context of the world/environment beyonf just the spoken words.

Linguistic insights:

Indexicality: relating to or denoting a word or expression whose meaning is dependent on the context in which it is used (such as here, you, me, that one there)

Modality: phenomenon whereby language is used to discuss possible situations. For instance, a modal expression may convey that something is likely, desirable, or permissible. Egs: must, could , should, probably

Epistemic: relating to knowledge or to the degree of its validation (epistemology)

Deontic reasoning: thinking about whether actions are forbidden or allowed, obligatory or not obligatory

Anaphora: word or phrase that takes its reference from a preceding word/phrase

Cataphora: word or phrase that takes its reference from a succeeding word/phrase

Interesting take on [pragmatics & Grice](https://plato.stanford.edu/entries/pragmatics/#Far1.2)

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled.png)

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%201.png)

These work because they are grounded in that small simulated world. It is difficult to achieve this level of performance with purely [[machine-learning]] systems that just do pattern matching.

Though deep learning systems are a promising toolkit, because just like you have vectors for words, you could have vectors for other agents in your environment to ground your system, like vectors for people, vectors for images, vectors for videos etc. Then a DL could take these sentence representations/vectors & the grounding vectors, smoosh them together and produce something meaningful.

**Speaker:**

Something that maps from real world phenomena/attribute to language.

Model for describing a color from the XKCD color dataset. Simple idea (surprised it works)

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%202.png)

This one just includes an attention like mechanism:

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%203.png)

**Listener:**

Maps language to some real world phenomena/attribute, like creating some rich 3d scenes from just its description.

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%204.png)

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%205.png)

There was also a bit about chatbots from FAIR that were negotiating with each other to reach some goal deal state. Didn’t really catch all details, but I think it would be interesting to train these through some RL objectives.

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%206.png)

![450](courses/xcs224u%20-%20natural%20language%20understanding/attachments/Untitled%207.png)
