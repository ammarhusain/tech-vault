---
created: 2023-09-12-Tuesday 11:08
modified: 2023-09-14-Thursday 11:31
---

# Models
## Minerva

[[2022-10-03-Monday]]
[Google AI Blog: Minerva: Solving Quantitative Reasoning Problems with Language Models](https://ai.googleblog.com/2022/06/minerva-solving-quantitative-reasoning.html)
		- it is [often believed](https://bounded-regret.ghost.io/ai-forecasting/) that solving quantitative reasoning problems using [[machine-learning|machine learning]] will [require](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html) [significant](https://arxiv.org/abs/2103.03874) [advancements](https://arxiv.org/abs/2110.14168) in model architecture and training techniques, granting models access to external tools such as [[python]] interpreters, or possibly a more profound paradigm shift.
		- In “[Solving Quantitative Reasoning Problems With Language Models](https://arxiv.org/abs/2206.14858)”, we present Minerva, a language model capable of solving mathematical and scientific questions using step-by-step reasoning.
		- Minerva solves such problems by generating solutions that include numerical calculations and symbolic manipulation without relying on external tools such as a calculator. The model parses and answers mathematical questions using a mix of natural language and mathematical notation. Minerva combines several techniques, including [few-shot prompting](https://arxiv.org/abs/2005.14165), [chain of thought](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html) or [scratchpad](https://arxiv.org/abs/2112.00114) prompting, and [majority voting](https://arxiv.org/abs/2203.11171), to achieve state-of-the-art performance on STEM reasoning tasks.
		- [interactive sample explorer](https://minerva-demo.github.io/)!
		- Minerva builds on the [Pathways Language Model](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html) (PaLM), with further training on a 118GB dataset of scientific papers from the [arXiv](https://arxiv.org/) preprint server and web pages that contain mathematical expressions using [LaTeX](https://www.latex-project.org/), [MathJax](https://www.mathjax.org/), or other mathematical typesetting formats.
		- Our approach to quantitative reasoning is not grounded in formal mathematics
		- This approach has an important limitation, in that the model’s answers cannot be automatically verified. Even when the final answer is known and can be verified, the model can arrive at a correct final answer using incorrect reasoning steps, which cannot be automatically detected. This limitation is not present in formal methods for theorem proving

## Muzero

[[2022-10-03-Monday]]
[MuZero: Mastering Go, chess, shogi and Atari without rules](https://www.deepmind.com/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules)
		- MuZero masters Go, chess, shogi and Atari without needing to be told the rules, thanks to its ability to plan winning strategies in unknown environments.
		- Systems that use lookahead search, such as AlphaZero, have achieved remarkable success in classic games such as checkers, chess and poker, but rely on being given knowledge of their environment’s dynamics, such as the rules of the game or an accurate simulator. This makes it difficult to apply them to messy real world problems, which are typically complex and hard to distill into simple rules.
		- Model-based systems aim to address this issue by learning an accurate model of an environment’s dynamics, and then using it to plan. However, the complexity of modelling every aspect of an environment has meant these algorithms are unable to compete in visually rich domains, such as Atari.  Until now, the best results on Atari are from model-free systems, such as [DQN](https://www.nature.com/articles/nature14236), [R2D2](https://openreview.net/forum?id=r1lyTjAqYX) and [Agent57](https://arxiv.org/abs/2003.13350). As the name suggests, model-free algorithms do not use a learned model and instead estimate what is the best action to take next.
		- MuZero models three elements of the environment that are critical to planning:
		- The value: how good is the current position?
		- The policy: which action is the best to take?
		- The reward: how good was the last action?
	![[62277f565ad61d23ae431c30_Fig 2.gif|500]]
Illustration of how Monte Carlo Tree Search can be used to plan with the MuZero [[courses/xcs224n - natural language processing/3-4 - Neural Networks and Backpropagation|neural networks]]. Starting at the current position in the game (schematic Go board at the top of the animation), MuZero uses the representation function (h) to map from the observation to an embedding used by the neural network (s0). Using the dynamics function (g) and the prediction function (f), MuZero can then consider possible future sequences of actions (a), and choose the best action.

## Cicero

First AI model that achieves human level performance in the strategy game Diplomacy. This model both cooperates and competes against human players through communicating in natural language and strategizing to make actions in games. Cicero combines a natural language dialogue model with strategic reasoning modules. It generates messages with a pre-trained Transformer-based model that was further finetuned on messages from human-only Diplomacy games. The dialogue generation is conditioned on the message history, game state, and predicted intents of other players. Generated messages are chosen with the help of several filters, which are designed to eliminate incomprehensible, inconsistent, toxic, or strategically poor messages. Cicero also has a strategic reasoning module, trained with self-play [[reinforcement learning]], which predicts policies of other players and selects actions for itself to execute. Cicero learns to cooperate, negotiate, and coordinate with humans through natural language in order to achieve its goals.

## ReAct

[[2023-10-10-Tuesday]]
Came out in March 2023
[Understanding ReACT with LangChain - YouTube](https://www.youtube.com/watch?v=Eug2clsLtFs)
Do the reasoning first within an LM
ReAct -> Reasoning + Act
Chain of thought is one shot reasoning - can we make it do more?
Need fairly long context lengths for this to work - thats why bigger models are better

[ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)
![[shiny-fm-reasoning-2023-10-10.png]]
While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces.

![[shiny-fm-reasoning-2023-10-10-1.png]]

*The format of Question-Thought-Action-Observation is something done within the paper but is not necessarily required in that way. One could hypothetically prompt the model in various different ways as long as there is room for "Reasoning" and " Acting" using tools. Prompt engineering LLMs are prone to hallucinations because the LM will produce an answer and then double down on it by providing evidence for it. This makes it even more confident in falsifying information. ReAct breaks that cycle by having the LM reason first thereby priming it to produce the right answer. It leverages these reasoning traces with in-context learning so the LM sees more & more of its own chain-of-thought.  This is different than CoT prompting because that is just a one-shot prompt breaking down a problem and might not be pertinent for the particular question - just general ways of thinking.
LLMS have also been increasingly employed in interactive and embodied environments for planning and decision making. Perhaps most relevant to ReAct in this respect are SayCan (Ahn et al., 2022) and Inner Monologue (Huang et al., 2022b), which use LLMs for robotic action planning and decision making. In SayCan, LLMs were prompted to directly predict possible actions a robot can take, which is then reranked by an affordance model grounded on the visual environments for final prediction. Inner Monologue made further improvements by adding the eponymous “inner monologue", which is implemented as injected feedback from the environment. To our knowledge, Inner Monologue is the first work that demonstrates such a closed-loop system, which ReAct builds on.* 

“inner monologue” (Google Brain robotics paper) is limited to observations of the environment state and what needs to be completed by the agent for the goal to be satisfied. In contrast, the reasoning traces in ReAct for decision making is flexible and sparse, allowing diverse reasoning types (see Section 2) to be induced for different tasks.

## Generative Agents: Interactive Simulacra of Human Behavior

[Paper - 2304.03442.pdf](https://arxiv.org/pdf/2304.03442.pdf)
To enable generative agents, we describe an architecture that extends a large language model to store a complete record of the agent’s experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior
Despite striking progress in large language models that can simulate human behavior at a single time point, fully general agents that ensure long-term coherence would be better suited by architectures that manage constantly-growing memories as new interactions, conflicts, and events arise and fade over time while handling cascading social dynamics that unfold between multiple agents. Success requires an approach that can retrieve relevant events and interactions over a long period, reflect on those memories to generalize and draw higher-level inferences, and apply that reasoning to create plans and reactions that make sense in the moment and in the longer-term arc of the agent’s behavior.
Our architecture comprises three main components. The first is the memory stream, a long-term memory module that records, in natural language, a comprehensive list of the agent’s experiences. A memory retrieval model combines relevance, recency, and importance to surface the records needed to inform the agent’s moment-to-moment behavior. The second is reflection, which synthesizes memories into higherlevel inferences over time, enabling the agent to draw conclusions about itself and others to better guide its behavior. The third is planning, which translates those conclusions and the current environment into high-level action plans and then recursively into detailed behaviors for action and reaction. These reflections and plans are fed back into the memory stream to influence the agent’s future behavior.
Across the technical and end-to-end evaluation, the most common errors arose when the agent failed to retrieve relevant memories, fabricated embellishments to the agent’s memory, or inherited overly formal speech or behavior from the language model.
The agents interact with the world by their actions, and with each other through natural language. At each time step of the sandbox engine, the agents output a natural language statement describing their current action
![[shiny new models-2023-08-24.png]]
Instead of summarizing, the memory stream described below surfaces relevant memories, resulting in a more informative and specific response
Memory retrieval for these generative agents is a combination of: Recency (timestamps), Importance (lang model scores the poignancy) and Relevance (cosine similarity of embedding vectors query & memory)

## DEMONSTRATE–SEARCH–PREDICT: Composing Retrieval and Language Models for Knowledge-intensive Nlp

[2212.14024.pdf](https://arxiv.org/pdf/2212.14024.pdf)
To begin to fully realize the potential of frozen LMs and RMs, we propose DEMONSTRATE– SEARCH–PREDICT (DSP), a framework that relies on passing natural language texts in sophisticated pipelines between an LM and an RM. DSP can express high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that the LM and RM can handle more reliably
LM - GPT 3.5
RM - ColBERTv2 (from 2020) for retrievals
[[2023-09-12-Tuesday]] - From Omar's talk: They are trying to build a PyTorch like framework that can be compiled to layer LM & RM models for Chain of Thought prompting etc. [GitHub - stanfordnlp/dspy: DSPy: The framework for programming with foundation models](https://github.com/stanfordnlp/dspy#4-documentation--tutorials)

## Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models

[Paper](https://arxiv.org/abs/2304.09842)
![[chameleon-2023-04-28.png]]
Remarkable plug-and-play compositional reasoning framework that leverages GPT-4 and seamlessly integrates vision models, web search, and even Python scripts.
Utilizes natural language planning to retrieve knowledge from the given question, plan for the necessary actions, and generate a coherent answer.
At its core, Chameleon comprises a natural language planner (P) and a set of possible usable modules (M). When presented with a query, P selects the appropriate modules from M, invokes them sequentially, and generates the final answer with the final module. Chameleon can be thought of as the generalized version of CoT, with a broader set of viable modules beyond the "Solution Generator" and the "Answer Generator."
With its seamless integration of diverse modules and impressive performance, Chameleon represents a significant advancement in the field of tool-augmented LLMs, holding the potential to unlock new frontiers in natural language processing and reasoning.


# Agents
[[2025-03-21-Friday]]
- [Agents | Blog posts Huyen Chip](https://huyenchip.com/2025/01/07/agents.html)
- [Google Agents Whitepaper](https://readwise-assets.s3.amazonaws.com/media/wisereads/articles/agents/Newwhitepaper_Agents2.pdf?__readwiseLocation=)
	- ![[2025-03-21-Friday-2025-03-21.png]]
	- At the heart of an agent’s operation is the orchestration layer, a cognitive architecture that structures reasoning, planning, decision-making and guides its actions. Various reasoning techniques such as ReAct, Chain-of-Thought, and Tree-of-Thoughts, provide a framework for the orchestration layer to take in information, perform internal reasoning, and generate informed decisions or responses. 


# Interesting Papers

## Human-level Prompt Engineering

 [[natural language program synthesis]] [[2022-10-12-Wednesday]] : **[paper](https://substack.com/redirect/fececd1d-777b-46f6-9ac1-5828544a52f3?r=f2u90)**
Large Language Models don’t always produce optimal results, but have to be prompted with carefully crafted queries to get them to respond correctly. While humans currently explore these prompts by trial and error, the authors explore training LLMs to generate meaningful prompts. In this paper, the authors train a secondary LLM on a set of input-output demonstrations for the target LLM. The secondary LLM then outputs a large number of candidate instructions, which are then scored and refined using a Monte Carlo Search method. In this method, the secondary LLM is asked to generate prompts that “have the same semantic meaning” as the candidates with the highest scores. The experiments reveal that the method achieves human-level performance on 19 out of 24 tasks.
*Very similar to an [[idea]] I had for using [[reinforcement learning]] to generate these prompts by modifying the prompt text embedding sequentially. Given the large action space (ie size of the text embedding) the agent would have been super hard to train. So in principle this approach is better.*

## Self-programming Ai

**[paper](https://substack.com/redirect/fc734b02-7e77-4e1b-b784-29161cd3b713?r=f2u90):** In what the authors assert to be the first practical implementation of a self-programming system, a T5-based [[autoencoder]] is trained on code samples for training [[convolutional neural nets|convolutional neural networks]]. A genetic algorithm then requests the model to generate *N* ‘refined’ code samples, and train them for one epoch, the losses from which are used to determine the best candidate for the next step of the algorithm. The model is mostly restricted to making hyperparameter changes - the number of layers, the number of neurons in a layer, and the number of attention heads. Note that this is different from simple hyperparameter tuning as a language model is rewriting code in this case instead of making numerical changes. Generated candidates with syntactic or compilation errors are discarded by the genetic algorithm.
[[2022-10-12-Wednesday]] [[archive/old-ideas#code generation]]

## Self-Instruct: Aligning LM with Self Generated Instructions

Self-Instruct is a framework that helps language models improve their ability to follow natural language instructions. It does this by using the model's own generations to create a large collection of instructional data. With Self-Instruct, it is possible to improve the instruction-following capabilities of language models without relying on extensive manual annotation.
The Self-Instruct process is an iterative bootstrapping algorithm that starts with a seed set of manually-written instructions and uses them to prompt the language model to generate new instructions and corresponding input-output instances. These generations are then filtered to remove low-quality or similar ones, and the resulting data is added back to the task pool. This process can be repeated multiple times, resulting in a large collection of instructional data that can be used to fine-tune the language model to follow instructions more effectively.
![[shiny new models-2023-07-25-1.png]]
It is pretty much using the prompt-completion pairs and using the OpenAI finetuning API.

## Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking
[[2024-04-15-Monday-W16|2024-04-17-Wednesday]]: Agatha sent this on palazzo-llm [2403.09629.pdf](https://arxiv.org/pdf/2403.09629.pdf)
Broadly, Quiet-STaR proceeds by generating rationales after every token to explain future text (think), mixing the future-text predictions with and without rationales (talk), and then learning to generate better rationales using REINFORCE (learn).
Quiet-STaR represents a step towards language models that can learn to reason in a general and scalable way. By training on the rich spectrum of reasoning tasks implicit in diverse web text, rather than narrowly specializing for particular datasets, Quiet-STaR points the way to more robust and adaptable language models.

> [!NOTE] I did not properly read this paper but it just seems like an incremental approach towards building reasoning agents. Not relevant to anything particular I am working on atm.

