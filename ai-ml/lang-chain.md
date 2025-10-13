---
created: 2023-05-08-Monday 08:02
modified: 2023-05-08-Monday 08:02
---

[[lang-chain-2023-05-08.ipynb]]

[[2023-05-30-Tuesday]]
A lot of the magic is being hid in this `VectorstoreIndexCreator`. What is this doing?
There are three main steps going on after the documents are loaded:
1. Splitting documents into chunks
2. Creating embeddings for each document
3. Storing documents and embeddings in a vectorstore
My [[code-junkyard/second-brain-web-search/second-brain-web-search]] could be built much simpler using these langchain indexes. I end up doing the same stuff with custom python code - [Obsidian — 🦜🔗 LangChain 0.0.186](https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/obsidian.html)

[[2023-05-23-Tuesday]]:
Very good intro: [LangChain Crash Course: Build a AutoGPT app in 25 minutes! - YouTube](https://www.youtube.com/watch?v=MlK6SIjcjE8)
- Introduces Streamlit as well for the frontend

[LangChain Crash Course - Build apps with language models - YouTube](https://www.youtube.com/watch?v=LbT1yp6quS8)
![[lang-chain-2023-05-23.png]]

Core concepts:
- Models
	OpenAI, HuggingFace etc
- Prompt Templates
	Prompt engineering and syntactic sugar
- Tools & Agents
	Calls to external APIs
- Chains
- Memory 
- Indexes
	Pinecone Chroma etc