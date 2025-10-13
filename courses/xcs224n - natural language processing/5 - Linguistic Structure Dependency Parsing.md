---
aliases: []
created: 2022-09-01-Thursday 14:31
modified: 2023-03-10-Friday 23:15
tags: aiml, aiml/nlp, courses/stanford
---


---

# 5 - Linguistic Structure: Dependency Parsing

[[courses/xcs224n - natural language processing/attachments/XCS224N_Lecture5_Slides.pdf]]
[[courses/xcs224n - natural language processing/attachments/cs224n-lecture_notes_iv.pdf]]
Suggested Readings:

1. [Incrementality in Deterministic Dependency Parsing](https://www.aclweb.org/anthology/W/W04/W04-0308.pdf)
2. [A Fast and Accurate Dependency Parser using Neural Networks](http://cs.stanford.edu/people/danqi/papers/emnlp2014.pdf)
3. [Dependency Parsing](http://www.morganclaypool.com/doi/abs/10.2200/S00169ED1V01Y200901HLT002)
4. [Globally Normalized Transition-Based Neural Networks](https://arxiv.org/pdf/1603.06042.pdf)
5. [Universal Stanford Dependencies: A cross-linguistic typology](http://nlp.stanford.edu/~manning/papers/USD_LREC14_UD_revision.pdf)
6. [Universal Dependencies](http://universaldependencies.org/)

---

- Some grammar terms:
	- Determiner/ articles: a, an, the;
	- Preposition: a word governing, and usually preceding, a noun or pronoun and expressing a relation to another word or element in the clause, as in “the man on the platform,” “she arrived after dinner,” “what did you do it for ?”
	- Predicate: state, affirm, or assert (something) about the subject of a sentence or an argument of a proposition. Eg: “John went home.”
	- Subject and Object: The subject is the person or thing doing something, and the object is having something done to it.
	- Modifier: Optional element in phrase structure or clause structure that modifies another element in the structure, on which it is dependent. Typically the modifier can be removed without affecting the grammar of the sentence. Eg: adjective (large, red), adverb (loudly, quite, then, there), determiners (a, the, no)
	- Infinitive: Basic form of a verb, without an inflection binding it to a particular subject or tense. Usually begins with the word “to”, eg: We came to see; let him see
	- Conjugation: give the different forms of (a verb in an inflected language) as they vary according to voice, mood, tense, number, and person. Eg: running, sang, mangoes (plural s).
	- Conjunct: word used to connect clauses or sentences or to coordinate words in the same clause (e.g. and, but, if ).
- Phrase structure grammars (= context free grammars):   You can build language sentences by starting with atomic word units & put them together with some simple rules.
- Noun Phrase-> Determiner  + (adjective) + Noun (a cat, the dog) + Prepositional Phrase (Eg: The black dog)
- Prepositional Phrase -> Preposition + Noun Phrase (Eg: in a large crate)
- This leads to recursive structure: ‘The black dog (NP)’ ‘in a large crate (PP)’
- Similarly one can write VerbPhrase: Verb + Prepositional Phrase (Eg: Talk to the cat)
- Dependency grammar & Dependency structures: We need to know what is connected to what.  
- Postulates that syntactic structure consists of relations between lexical items, normally binary asymmetric relations (“directional arrows”) called dependencies.
- You try and find what is the subject, object, of the verbs, nouns, modifiers etc . Figure out what depends on what or what modifies what. Though this can lead to prepositional phrase ambiguity.
- Leads to a large (exponential) number of dependencies that needs to be resolved within a sentence [Catalan numbers]. Exponentially growing series which arises in many tree like contexts: # of possible triangulations of a polygon with n+2 sides.

![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image11.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image53.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image25.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image65.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image10.png)![450](courses/xcs224n%20-%20natural%20language%20processing/attachments/image17.png)

- Neural Dependency Parsers basically get rid of the conventional feature representation above and build a neural network that just takes in word embedding with the state of the stack & buffer etc and to classify next action (shift, left arc, right arc).
- Tree banks are the NLP version of annotated data. Before people were witing their own grammars like NounPhrase=Det+(Adj)+Noun+PrepositionalPhrase and then writing parsers that parsed sentences based on that grammar that they defined. So there was no consistency or sharing. Also the parser might be wrong for certain sentences where you might need to have a different grammar+parser combo. Tree banks standardized all such annotations so it could be used for ML.
