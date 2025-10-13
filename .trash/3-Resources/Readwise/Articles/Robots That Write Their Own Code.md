---
aliases: []
tags:
---
# Robots That Write Their Own Code

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJs5xuCtPfu7bzm4c7-5osumFCp5bvKmguRmt_y3fgQbbUoc_37a-ezjjAEH0u1Nb4Am6-zDJi4-z5ZWOn1Io174DEYDNCjYnBQX_2izJloFoO3pbJI7ibYSz2q4_gDMmasq8YFTFdb-4UcObIZykvLviCh3TNIiAw5umN5dRg8V0ZblRQ4ibBvW2gKw/s72-c/CodeAsPolicies-2.png)
### Metadata
Author: [[googleblog.com]]
Full Title: Robots That Write Their Own Code
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/robots, ]
URL: https://ai.googleblog.com/2022/11/robots-that-write-their-own-code.html
Date Highlighted: [[2022-12-19-Monday]]

## Highlights
- When provided with several example instructions (formatted as comments) paired with corresponding code (via [in-context learning](http://ai.stanford.edu/blog/understanding-incontext/)), language models can take in new instructions and autonomously generate new code that re-composes API calls, synthesizes new functions, and expresses feedback loops to assemble new behaviors at runtime. More broadly, this suggests an alternative approach to using machine learning for robots that (i) pursues generalization through modularity and (ii) leverages the abundance of open-source code and data available on the Internet. ([View Highlight](https://read.readwise.io/read/01gmnjrm75hgj61dbxq5q46j6a))
- [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE55-x4Nq_pV-hdSw8M45MlYZFoyX9Q0nv7b0LgZ5V-0HBiBw-s_SvcIkKJ4tWoVxu0QgmPxO792fsZ0vg6qSU42ps8clbdCHzJoH_3dZRc8dZ9HtF6a1P3kjr0gKGfb581san33sLFuXlsrCYSk2_6l-1UssiePuUZny0LmIEd8WX1if6CShyYcEsHw/s16000/image4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE55-x4Nq_pV-hdSw8M45MlYZFoyX9Q0nv7b0LgZ5V-0HBiBw-s_SvcIkKJ4tWoVxu0QgmPxO792fsZ0vg6qSU42ps8clbdCHzJoH_3dZRc8dZ9HtF6a1P3kjr0gKGfb581san33sLFuXlsrCYSk2_6l-1UssiePuUZny0LmIEd8WX1if6CShyYcEsHw/s1276/image4.png)
  Given code for an example task (left), language models can re-compose API calls to assemble new robot behaviors for new tasks (right) that use the same functions but in different ways. ([View Highlight](https://read.readwise.io/read/01gmnk0yk59czjk25kw1xj4afh))
    - Note: Example of "capabilities" that the LLM can learn to compose skills from.
- [Code as Policies](https://code-as-policies.github.io/) (CaP), a robot-centric formulation of language model-generated programs executed on physical systems. CaP extends our [prior work](https://ai.googleblog.com/2022/08/towards-helpful-robots-grounding.html), [PaLM-SayCan](https://sites.research.google/palm-saycan), by enabling language models to complete even more complex robotic tasks with the full expression of general-purpose Python code. With CaP, we propose using language models to directly write robot code through few-shot prompting. Our experiments demonstrate that outputting code led to improved generalization and task performance over directly learning robot tasks and outputting natural language actions. CaP allows a single system to perform a variety of complex and varied robotic tasks without task-specific training. ([View Highlight](https://read.readwise.io/read/01gmnjwj7e76h6gdwhgx37atgz))
    - Note: The code that the "Code as Policies" sytem outputs should map to individual capabilities on the EDR robot. So in essense CaP can build "skills" by synthesizing/composing a set of capabilities (in python code) using a LLM. This fits pretty well with chat with Kendra on her Research strawman -> defining capabilities, skills, tasks & services.
- Central to this approach is *hierarchical code generation*, which prompts language models to recursively define new functions, accumulate their own libraries over time, and self-architect a dynamic codebase. Hierarchical code generation improves state-of-the-art on both robotics as well as standard code-gen benchmarks in natural language processing (NLP) subfields ([View Highlight](https://read.readwise.io/read/01gmnk4zt104pa35pfs7h59afy))
- CaP generalizes at a specific layer in the robot: interpreting natural language instructions, processing perception outputs (e.g., from off-the-shelf object detectors), and then parameterizing control primitives. This fits into systems with factorized perception and control, and imparts a degree of generalization (acquired from pre-trained language models) without the magnitude of data collection needed for [end-to-end robot learning](https://ai.googleblog.com/2021/11/decisiveness-in-imitation-learning-for.html). ([View Highlight](https://read.readwise.io/read/01gmnkad2v59hsr9cxj7qhpkta))
    - Note: This is great for still applying ML in a hybrid approach. Not sure if its necessarily better than a human at this point but could be a worthwhile investment for spinning up new services quickly (assuming we have a decently well defined set of capabilities in the Robot API)
