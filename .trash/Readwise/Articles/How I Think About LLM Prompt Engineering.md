---
aliases: []
tags:
---
# How I Think About LLM Prompt Engineering

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a9ca68f-6b32-4dbc-a266-cb1a5b62f236_1024x1024.png)
### Metadata
Author: [[François Chollet]]
Full Title: How I Think About LLM Prompt Engineering
Category: #readwise/articles
URL: https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering
Date Highlighted: [[2025-03-14-Friday]]

## Highlights
- On the surface, modern LLMs couldn’t seem any further from the primitive word2vec model. They generate perfectly fluent language — a feat word2vec was entirely incapable of — and seem knowledgeable about any topic. And yet, they actually have a lot in common with good old word2vec.
  Both are about embedding tokens (words or sub-words) in a vector space. Both rely on the same fundamental principle to learn this space: tokens that appear together end up close together in the embedding space. The distance function used to compare tokens is the same in both cases: cosine distance. Even the dimensionality of the embedding space is similar ([View Highlight](https://read.readwise.io/read/01jpb8j99rm4amb5m8n5w7zkaw))
- Just like with word2vec, LLMs end up learning useful semantic functions as a by-product of organizing tokens into a vector space. But thanks to this increased representation power and a much more refined autoregressive optimization objective, we’re no longer confined to linear transformations like a “gender vector” or a “plural vector”. LLMs can store arbitrarily complex vector functions — so complex, in fact, that it would be more accurate to refer to them as **vector programs** rather than functions.
  Word2vec enabled you to do basic things like **plural(cat) → cats** or **male_to_female(king) → queen**. Meanwhile LLMs can do pure magic — things like **write_this_in_style_of_shakespeare(“…your poem…”) → “…new poem…”**. And they contain millions of such programs. ([View Highlight](https://read.readwise.io/read/01jpb8thbxy5dcdykg2mc71skq))
- You can see a LLM as analogous to a database: it stores information, which you can retrieve via prompting. But there are two important differences between LLMs and databases.
  The first difference is that a LLM is a *continuous, interpolative* kind of database. Instead of being stored as a set of discrete entries, your data is stored as a vector space — a curve. You can move around on the curve (it’s semantically continuous, as we discussed) to explore nearby, related points. And you can interpolate on the curve between different data points to find their in-between. This means that you can retrieve from your database a lot more than you put into it — though not all of it is going to be accurate or even meaningful. Interpolation can lead to generalization, but it can also lead to hallucinations.
  The second difference is that a LLM doesn’t just contain data. It certainly does contain a lot of data — facts, places, people, dates, things, relationships. But it’s also — perhaps primarily — a database of *programs*. ([View Highlight](https://read.readwise.io/read/01jpb9n3rbkgsjnsfj4g0mxpwn))
- Consider the following example prompt: “*rewrite the following poem in the style of Shakespeare: …my poem…*”
  [
  ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff14bd38f-58be-4908-b2dd-ebcd50b73c24_1214x1060.png)
  ](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff14bd38f-58be-4908-b2dd-ebcd50b73c24_1214x1060.png)
  • **“rewrite this in the style of”** is the program key. It points to a particular location in program space.
  • “**Shakespeare**” and “**..my poem…**” are program inputs.
  • The LLM’s output in the result of the program execution. ([View Highlight](https://read.readwise.io/read/01jpb9nfd9vaqq0h30bnsvrtgc))
- Prompt engineering as a program search process
  Remember, this “program database” is continuous and interpolative — it’s not a discrete set of programs. This means that a slightly different prompt, like “*Lyrically rephrase this text in the style of x*” would still have pointed to a very similar location in program space, resulting in a program that would behave pretty closely but not quite identically. ([View Highlight](https://read.readwise.io/read/01jpb9h7jeczakx0fcev7de2ms))
