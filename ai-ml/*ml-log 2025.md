
- [[2025-09-14-Sunday]] - [Claude Memory: A Different Philosophy \| Shlok Khemani](https://www.shloked.com/writing/claude-memory)
	- [Writing effective tools for AI agents—using AI agents \\ Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents?__readwiseLocation=)
	- [Title Unavailable \| Site Unreachable](https://cookbook.openai.com/articles/gpt-oss/fine-tune-transfomers)
		- Finetunes gpt oss20b using LoRA adapter and TRL library from [[tools & tech/hugging face|hugging face]] - [[../code-junkyard/gpt-oss-finetune.ipynb|gpt-oss-finetune]]
		- 
- [[2025-09-12-Friday]] - [Claude Code: Behind-the-scenes of the master agent loop](https://blog.promptlayer.com/claude-code-behind-the-scenes-of-the-master-agent-loop/?__readwiseLocation=)
	- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus?__readwiseLocation=)
		- KV-cache hit rate is the single most important metric for a production-stage AI agent
		- Use the File System as Context
		- By constantly rewriting the todo list, Manus is reciting its objectives into the end of the context.
		- Dont remove the failed actions from the context
		- don't few-shot yourself into a rut. The more uniform your context, the more brittle your agent becomes.
	- [Understanding Multimodal LLMs - by Sebastian Raschka, PhD](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms?__readwiseLocation=)
		- ![[../attachments/*ml-log 2025-2025-09-12.png|400]]
		- ~={orange}great overview diagram of self attention and how Key Value Query KV & Q matrices work=~ 
- [2025-09-11-Thursday](2025-09-11-Thursday) - 
	- [[attachments/The Era of Experience.pdf]]
		- This era of experience will likely be characterised by agents and environments that, in addition to learning from vast quantities of experiential data, will break through the limitations of human-centric AI systems in several further dimensions:
			• Agents will inhabit streams of experience, rather than short snippets of interaction.
			• Their actions and observations will be richly grounded in the environment, rather than interacting via human dialogue alone.
			• Their rewards will be grounded in their experience of the environment, rather than coming from human prejudgement.
			• They will plan and/or reason about experience, rather than reasoning solely in human terms
		- What if experiential agents could learn from external events and signals, and not just human preferences?
			- Relying on human prejudgement in this manner usually leads to an impenetrable ceiling on the agent’s performance: the agent cannot discover better strategies that are underappreciated by the human rater. To discover new ideas that go far beyond existing human knowledge, it is instead necessary to use grounded rewards: signals that arise from the environment itself.
		- The reward function can adapt over time, to improve the way in which it selects or combines signals, and to identify and correct any misalignment. This can also be understood as a bi-level optimisation process that optimises user feedback as the top-level goal, and optimises grounded signals from the environment at the low level.4 In this way, a small amount of human data may facilitate a large amount of autonomous learning.
		- Conceptually, LLMs can act as a universal computer: an LLM can append tokens into its own context, allowing it to execute arbitrary algorithms before outputting a final result. In the era of human data, these reasoning methods have been explicitly designed to imitate human thought processes.
		- Techniques like RLHF (Reinforcement Learning from Human Feedback) and methods for aligning language models with human reasoning proved incredibly effective, driving rapid progress in AI capabilities. These approaches, while powerful, often bypassed core RL concepts: RLHF side-stepped the need for value functions by invoking human experts in place of machine-estimated values, strong priors from human data reduced the reliance on exploration, and reasoning in human-centric terms lessened the need for world models and temporal abstraction.
		- While human-centric RL has enabled an unprecedented breadth of behaviors, it has also imposed a new ceiling on the agent’s performance: agents cannot go beyond existing human knowledge. Furthermore, the era of human data has focused predominantly on RL methods that are designed for short episodes of ungrounded, human interaction, and are not suitable for long streams of grounded, autonomous interaction.
		- Finally, advancements relying on physical experience are inherently constrained by the time it takes to execute actions in the real world and observe their consequences. For example, the development of a new drug, even with AI-assisted design, still requires real-world trials that cannot be completed overnight. This may provide a natural brake on the pace of potential AI self-improvement.
		- ![[attachments/*ml-log 2025-2025-09-11.png|250]]
		- ==Authors talk about an "Era of Simulation"  followed by Era of Human Data that will now herald an Era of Experience. Though they also say that in order to get grounded signals from the environment the agent will have to build a "world model" -- how is this world model different than the simulations of the past?? Or are they arguing that leveraging human-centric AI ie AI systems that top out on human knowledge & capability we can build more faithful & general purpose world models than the narrow, hand coded and verifiiable simulators of the past -- in any case it sounds like the 'world model' is still a simulator. 
		- ==Another big difference between previous RL based methods and what the authors now prophesize is that the agents do not get complete trajectory rollouts  but instead have to compute rewards & adjust policy on partial rollouts -- so this will be a big change
	- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/pdf/2402.01030)
		- proposes to use executable Python code to consolidate LLM agents’ actions into a unified action space (CodeAct). Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions.
		~={yellow}	
		- simple idea - argue that LLMs are anyway trained for programming tasks so let them just write the pyhon code for building tools from provided or existing software packages rather than having them generate JSON or text and then translate that as a tool call. Following advantages:
				- use of existing software packages already have error logging so the LLM can self debug and regenerate tool code
				- code inherently supports control & data flow ie logic which text or json does not
				- dynamically adjust the tool through self debugging
				- build up on existing software packages rather than write your own tool for everything=~
		- Provides a dataset CodeActInstruct for SFT
		- 

- [[2025-08-26-Tuesday]] [Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet](https://simonwillison.net/2025/Aug/25/agentic-browser-security/?__readwiseLocation=)
	- [DeepSeek 3.1](https://simonwillison.net/2025/Aug/22/deepseek-31/?__readwiseLocation=)
	- [Running a gpt-oss eval suite against LM Studio on a Mac \| Simon Willison’s TILs](https://til.simonwillison.net/llms/gpt-oss-evals)
		- Downloading and running LM Studio - got a local model server hosted and running. I should just use LM studio for hosted the attention models too perhaps
	- [Why LLMs Can't Really Build Software — Zed's Blog](https://zed.dev/blog/why-llms-cant-build-software?__readwiseLocation=)
	- [The Illustrated GPT-OSS - by Jay Alammar](https://newsletter.languagemodels.co/p/the-illustrated-gpt-oss?asuniq=9589ff20&__readwiseLocation=)
	- ==[From GPT-2 to gpt-oss: Analyzing the Architectural Advances](https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the?publication_id=1174659&post_id=170506328&isFreemail=true&r=f2u90&triedRedirect=true&__readwiseLocation=)==
		- Most of the gains likely come from data and algorithm tweaks rather than from major architecture changes
		- Dropout is rarely used in modern LLMs 
			- This is likely because LLMs are typically trained for only a single epoch over massive datasets, which is in contrast to the multi-hundred-epoch training regimes for which dropout was first introduced. So, since LLMs see each token only once during training, there is little risk of overfitting.
		- RoPE (Rotary Position Embedding) introduced a different approach: instead of adding position information as separate embeddings, it encodes position by rotating the query and key vectors in a way that depends on each token's position.
			- While first introduced in 2021, RoPE became widely adopted with the release of the original Llama model in 2023 and has since become a staple in modern LLMs.
		- Swish/ SwiGLU activation function
			- Activation functions used to be a hot topic of debate until the deep learning community largely settled on ReLU more than a decade ago. Since then, researchers have proposed and tried many ReLU-like variants with smoother curves, and GELU and Swish (Figure 5) are the ones that stuck. Swish is used in most architectures today. However, GELU is not entirely forgotten; for example, Google's Gemma models still use GELU.
		- Last feedforward layer has been replaced by a GLU (gated linear unit)
			- ![[*ml-log 2025-2025-08-26.png]]
			- using the GLU variants results in fewer parameters, and they perform better as well. The reason for this better performance is that these GLU variants provide an additional multiplicative interaction, which improves expressivity (the same reason deep & slim neural nets perform better than shallow & wide neural nets)
		- Sliding window attention
			- gpt-oss alternates between GQA layers that attend to the full context and GQA layers with a sliding window limited to 128 tokens. Gemma 3 earlier this year went much further and shifted to a 5:1 ratio, which means only one full-attention layer for every five sliding-window (local) attention layers.
		- RMSNorm instead of LayerNorm
		- Deeper models are harder to train due to exploding & vanishing gradients. They are also slower in inference due to less parallelization but reduce memory consumption
		- 


- [[2025-08-18-Monday]] [Claude with the Anthropic API](https://anthropic.skilljar.com/claude-with-the-anthropic-api?asuniq=67deffb6) #tinker_short  - Course on building applications using Claude
- [[2025-08-07-Thursday]] - [GPT-5: Key characteristics, pricing and model card](https://simonwillison.net/2025/Aug/7/gpt-5/)
	- [GPT-5: It Just Does Stuff - by Ethan Mollick](https://www.oneusefulthing.org/p/gpt-5-it-just-does-stuff#media-062bc238-0852-49ba-b0d4-e625e47e3b65)
	- [Measuring AI Ability to Complete Long Tasks - METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
	- [OpenAI’s new open weight (Apache 2) models are really good](https://simonwillison.net/2025/Aug/5/gpt-oss/)
	- [GLM-4.5: Reasoning, Coding, and Agentic Abililties](https://simonwillison.net/2025/Jul/28/glm-45/)
	- [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony#built-in-tools)
	- [Project Vend: Can Claude run a small shop? (And why does that matter?) \\ Anthropic](https://www.anthropic.com/research/project-vend-1?asuniq=0e1b896b)
	- Walked through:
		- [Tiny Agents: an MCP-powered agent in 50 lines of code](https://huggingface.co/blog/tiny-agents)
		- [Building good agents](https://huggingface.co/docs/smolagents/en/tutorials/building_good_agents)
		- [What are agents? 🤔](https://huggingface.co/docs/smolagents/en/conceptual_guides/intro_agents)
			- Interesting note: It is better for LLM agents to write out their problem solving flow as python code (with embedded tool calls) than to sequentially call tools and then process out its results.
			- Might be the gist of [Paper page - Executable Code Actions Elicit Better LLM Agents](https://huggingface.co/papers/2402.01030) which is on my to read list
	- [How Attention Sinks Keep Language Models Stable](https://hanlab.mit.edu/blog/streamingllm?__readwiseLocation=)
		- We found models dump massive attention onto the first few tokens as "attention sinks"—places to park unused attention since softmax requires weights to sum to 1. Our solution, StreamingLLM, simply keeps these first 4 tokens permanently while sliding the window for everything else
		- The presence of a sink draws attention away from other tokens, limiting the spread of information (and noise) and resulting in more stable embeddings.
		- Sometimes an impactful discovery emerges not from grand theoretical breakthroughs, but from carefully investigating the curious details that others might overlook. In our case, questioning why a few seemingly meaningless tokens were so critical led us to uncover a mechanism that every Transformer model relies on—one that was hiding in plain sight.

- [[2025-07-28-Monday]] #tinker_short 
	- [\[Full Workshop\] Reinforcement Learning, Kernels, Reasoning, Quantization & Agents — Daniel Han - YouTube](https://www.youtube.com/watch?v=OkEGJ5G3foU)

[[2025-07-10-Thursday]] [CaMeL offers a promising new direction for mitigating prompt injection attacks](https://simonwillison.net/2025/Apr/11/camel/?__readwiseLocation=)
- [Highlights from the Claude 4 system prompt](https://simonwillison.net/2025/May/25/claude-4-system-prompt/?__readwiseLocation=)
- [ELEGNT: Expressive and Functional Movement Design for Non-anthropomorphic Robot - Apple ](https://arxiv.org/pdf/2501.12493)
	- Not sure what the big deal about this paper was - just seems like a user study discovering the obvious - yes expressive movements are better for robots
- [Scalable Long-Term Memory for Production AI Agents \| Mem0](https://mem0.ai/research) [Highlighted Mem0 paper in GoodNotes](https://readwise.io/reader/document_raw_content/298795472?__readwiseLocation=)

[[2025-06-27-Friday]] **Karpathy Software has change 3.0 talk at YC**
	- Part 1: LLM analogies
		- Compares LLMs to electricity/ water (utilities), semi conductor fabs and operating systems (circa 1960s).
		- The LLM OS does not have a GUI yet. Also its more centralized and endpoint driven which is analogous to how computers were used as mainframes in the past. The personal computing revolution has not really been invented where all models run locally but its getting there quickly.
		- Available via time-sharing and distributed like a utility.
		- Billions of people have sudden access to them! It is our time to program them.
	- Part 2 : LLM Psychology
		- LLMs are "people spirits" - stochatic simulator of people where the simulator is an autogressive transformer
		- Superpower: Have encyclopedic knowledge / memory
		- Deficit : Hallucinations
		- Jagged Intelligence : Famous examples 9.11 > 9.9 or two 'r' in strawberry
		- Anterograde amnesia : 
			- no continual learning, no equivalent of "sleep" to consolidate knowledge, insight or expertise into weights
			- they forget everything once it goes out of context
		- Gullibility => prompt injection risks, eg: can leak your private data
	- Part 3: Opportunities
		- Going to the chatgpt app is like going directly to the OS or typing commads into the terminal. We should expose this underlying LLM capabilities through various apps - Cursor is a prime example 
			- <TODO: insert image>
		- Lot of software & apps will become partially autonomous
			- Can an LLM "see" all things the human can?
			- Can an LLM "act" in all the ways a human can?
			- How can a human supervise and stay in the loop?
		- 
		- "AI assisted coding" workflow is a loop between Human Verification <-> AI Generation
			- we need to make the verification easy & fast since human is the bottleneck.
			- keep AI on a tight leash to increase probability of successful verification.
			- describe the next concrete incremental change
			- dont ask for code ask for approaches
				- pick an approach -> draft code -> review / learn, ask for explanations
			- test -> git commit -> ask for suggestions on what to do next
		- Spend a bit of time creating details in prompts to increase the probability of a successful verification
		
- [[2025-06-17-Tuesday]]
	- **[Language Models in Plato's Cave - by Sergey Levine](https://sergeylevine.substack.com/p/language-models-in-platos-cave)**
		- While the Human Connectome Project is busy reconstructing the human brain neuron by neuron, LLMs are trying to skip the neurons all together and reconstruct the mind from the shadow it casts on the Internet.
		- This explains why video prediction models that learn about the physical world have so far not yielded the same results as next-token prediction on language: while we might hope that models that learn from videos might acquire representations of the physical world in the same way that humans learn through experience, the LLMs have managed to skip this step and simply copy some aspects of human mental representations without having to figure out the learning algorithm that allowed humans to acquire those representations in the first place.
		- The bad news is that these AI systems live in Plato’s Cave. The cave is the Internet, and the light shines from human intelligence, casting shadows of real-world interactions on the cave wall for the LLM to observe.
	- [Building a fully local "deep researcher" with DeepSeek-R1 - YouTube](https://www.youtube.com/watch?v=sGUjmyfof4Q)
		- ![[*ml-log 2025-2025-06-18-1.png]]
	- [How we built our multi-agent research system \\ Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system)
		- The essence of search is compression: distilling insights from a vast corpus. Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent. Each subagent also provides separation of concerns—distinct tools, prompts, and exploration trajectories—which reduces path dependency and enables thorough, independent investigations.
		- We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval.
		- Some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time.
		- We found that the Claude 4 models can be excellent prompt engineers. When given a prompt and a failure mode, they are able to diagnose why the agent is failing and suggest improvements.
		- We experimented with multiple judges to evaluate each component, but found that a single LLM call with a single prompt outputting scores from 0.0-1.0 and a pass-fail grade was the most consistent and aligned with human judgements.
		- ![[*ml-log 2025-2025-06-18-2.png]]
	- [OpenAI : a-practical-guide-to-building-agents.pdf](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf?__readwiseLocation=)
		- Every orchestration approach needs the concept of a ‘run’, typically implemented as a loop that lets agents operate until an exit condition is reached. Common exit conditions include tool calls, a certain structured output, errors, or reaching a maximum number of turns. This concept of a while loop is central to the functioning of an agent. 
		- For many complex workflows, splitting up prompts and tools across multiple agents allows for improved performance and scalability. When your agents fail to follow complicated instructions  or consistently select incorrect tools, you may need to further divide your system and introduce more distinct agents
		- Guardrails are critical at every stage, from input filtering and tool use to [[archive/edr/humans-in-the-loop]] intervention, helping ensure agents operate safely and predictably in production. 
	- [Reinforcement Pre-Training](https://arxiv.org/pdf/2506.08007v1)
		- reinforcement pre-training (RPT), a novel paradigm that bridges the gap between scalable self-supervised pre-training and the power of reinforcement learning. RPT reframes the fundamental next-token prediction task as a next-token reasoning process. For any given context in a pre-training corpus, the model is incentivized to reason about the subsequent token before predicting it. It receives a verifiable, intrinsic reward based on the correctness of its prediction against the ground-truth next token from the corpus itself. This approach transforms the vast, unannotated text data typically used for next-token prediction into a massive dataset for general-purpose RL, without requiring external annotations or domain-specific reward functions.
		- Since many tokens are easily predictable even without reasoning, we perform token-level data filtering before reinforcement pre-training. Particularly, we use DeepseekR1-Distill-Qwen-1.5B as a small proxy model. For each token, we calculate the proxy model entropy on the top-16 next tokens. By applying an entropy threshold, we filter out low-entropy positions, prioritizing training on challenging tokens that require greater computational effort to predict.
		- *~={green}Interesting approach though I dont know how easily it can scale during pre-training if the corpora are humongous=~*
	- [Apple’s ‘AI Can’t Reason’ Claim Seen By 13M+, What You Need to Know - YouTube](https://www.youtube.com/watch?v=wPBD6wTap7g)

- [[2025-06-14-Saturday]] 
	- [Building software on top of Large Language Models - Blog post](https://simonwillison.net/2025/May/15/building-on-llms/?__readwiseLocation=)
		- Good walkthrough of the LLM CLI tool [Building software on top of LLMs](https://building-with-llms-pycon-2025.readthedocs.io/en/latest/)
	- [Claude’s System Prompt: Chatbots Are More Than Just Models \| Drew Breunig](https://www.dbreunig.com/2025/05/07/claude-s-system-prompt-chatbots-are-more-than-just-models.html?__readwiseLocation=) A couple days ago, Ásgeir Thor Johnson convinced Claude to give up its system prompt. The prompt is a good reminder that chatbots are more than just their model. They’re tools and instructions that accrue and are honed, through user feedback and design.
		- [system\_prompts\_leaks/Anthropic/claude-sonnet-4.txt at main · asgeirtj/system\_prompts\_leaks · GitHub](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-sonnet-4.txt)
	- [My AI Skeptic Friends Are All Nuts · The Fly Blog](https://fly.io/blog/youre-all-nuts/?__readwiseLocation=) - good article arguing for the 10X effects of LLM for coding

#### [[2025-05-29-Thursday]]
**DeepSeek R1-0528** new reasoning model update that competes with OpenAI O3. May be try it for [[*ongoing/action sequencing-m0]] instead of Gemini-2.5-pro

[The recent history of AI in 32 otters - by Ethan Mollick](https://www.oneusefulthing.org/p/the-recent-history-of-ai-in-32-otters#media-3ff4fd39-0a02-4545-8254-05962ed6b323)
two crucial trends with some big implications. First, there clearly continues to be rapid improvement across a wide range of AI capabilities from image generation to video to LLM code generation. Second, open weights models, while not generally as good as proprietary models, are often only months behind the state-of-the-art.
If you put these trends together, it becomes clear that we are heading towards a place where not only are image and video generations likely to be good enough to fool most people, but that those capabilities will be widely available and, thanks to open models, very hard to regulate or control.

#### [[2025-05-20-Tuesday]]
- [Introducing Codex \| OpenAI](https://openai.com/index/introducing-codex/)
	- Coding agent that runs in a virtul env on the cloud
- [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms - Google DeepMind](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
	- AlphaEvolve leverages an ensemble of state-of-the-art large language models: our fastest and most efficient model, Gemini Flash, maximizes the breadth of ideas explored, while our most powerful model, Gemini Pro, provides critical depth with insightful suggestions.
	- ![[*ml-log 2025-2025-05-20.png]]
	- *~={red}Can solve any problem whose solution can be described as an algorithm, that can be automatically evaluated/verified=~*

## [[2025-05-01-Thursday]]
- [Questions about the Future of AI - by Dwarkesh Patel](https://substack.com/home/post/p-161809078?__readwiseLocation=)
	- rebuttal to Morevac’s Paradox: the capabilities AIs are getting first have nothing to do with their recency in the evolutionary record and everything to do with how much relevant training data exists.
	- I keep hearing that the big bottleneck for RL is the amount of environments that we have built so far. I don't really understand what this means. What exactly does it take to build a new RL environment? Presumably building complex, realistic, hard to reward-hack challenges?
	- As horizon lengths increase, your rollout has to become longer. The AI needs to do two hours worth of agentic computer use tasks before we can even see if it did it right. And if this is correct, will the pace of AI progress slow down? 
		- ~={red}*Kind of like in robotics where data collect becomes challenging*=~
	- RL potentially just upweights 10 tokens worth of MCTS-like scaffolding in a model's thinking (words like “wait”, “let’s backtrack”). This explains why reasoning models can be easily distilled - finding these basic techniques in thought space might take a while, but their payload size is trivial.
		- ~={red}Would be an interesting experiment to try artificially boosting token probabilities for "wait", "aha" etc and see if that causes similar behavior without needing to run full blown RL=~
- [Personality and Persuasion - by Ethan Mollick](https://www.oneusefulthing.org/p/personality-and-persuasion?img=https://substack-post-media.s3.amazonaws.com/public/images/52d95c38-e328-444c-82d1-f3f40df40afe_2589x3461.png&open=false)
	- we're entering a world where AI personalities become persuaders. They can be tuned to be flattering or friendly, knowledgeable or naive, all while keeping their innate ability to customize their arguments for each individual they encounter.

## [[2025-04-30-Wednesday]]
- [Understanding Reasoning LLMs - by Sebastian Raschka, PhD](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms?__readwiseLocation=)
	- ![[*ml-log 2025-2025-04-30-2.png]]
	- DeepSeek-R1-Zero: "cold start" training because it did not include a supervised fine-tuning (SFT) step, which is typically part of reinforcement learning with human feedback (RLHF).
	- **DeepSeek-V3 base** (no SFT - only pretrained) -> 
		- (RL: accuracy + format rewards) -> 
		- **DeepSeek-R1-Zero** -> 
		- ***600k SFT data*** (from DeepSeek-R1-Zero)-> 
		- instruction finetuning (from DeepSeek-R1-Zero) -> 
		- **DeepSeek-R1-a** -> 
		- (RL: accuracy + format + language consistency rewards) ->
		- ***600k CoT data*** (from DeepSeek-R1-a) + ***200k SFT data*** (from DeepSeek-V3-base)
		- instruction finetuning (from DeepSeek-V3-base) ->
		- RL (accuracy + format + lang consistency + human preference) ->
		- **DeepSeek-R1**
		- ![[*ml-log 2025-2025-04-30-1.png]]
		- 
	- All in all, this is very similar to regular RLHF except that the SFT data contains (more) CoT examples. And the RL has verifiable rewards in addition to human preference-based rewards.
	- Interesting insight that could be applied to finetuning a small LM for behavior tree generation [[*ongoing/action sequencing-m0]]
		- Distillation is far more effective than pure RL for smaller models. This aligns with the idea that RL alone may not be sufficient to induce strong reasoning abilities in models of this scale, whereas SFT on high-quality reasoning data can be a more effective strategy when working with small models.
		- Pure RL is interesting for research purposes because it provides insights into reasoning as an emergent behavior. However, in practical model development, RL + SFT is the preferred approach as it leads to stronger reasoning models.
		
- [The State of Reinforcement Learning for LLM Reasoning](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training?__readwiseLocation=)
	- This reward model (RM) generally originates from the LLM created in the prior supervised fine-tuning (SFT) step. To turn the model from RLHF Step 1 into a reward model, its output layer (the next-token classification layer) is substituted with a regression layer, which features a single output node.
	- expected reward is computed by a so-called "critic" (sometimes also called "value model"), and a reward model computes the actual reward. I.e., the advantage computation involves 2 other models, typically the same size as the original model we are fine-tuning.
	- ![[*ml-log 2025-2025-04-30-3.png]]
	- By the way, you might wonder why we need both a reward model and a critic model. The reward model is usually trained before training the policy with PPO. It's to automate the preference labeling by human judges, and it gives the score for the complete responses generated by the policy LLM.
	- The critic, in contrast, judges partial responses. We use it to create the final response. While the reward model typically remains frozen, the critic model is updated during training to estimate the reward created by the reward model better.
	- So, in short, DeepSeek-R1 used RLVR with GRPO, which eliminates two expensive models in the training procedure: the reward model and the value model (critic)
	- *RLVR : RL with verifiable rewards such as using a calculator or compiler to provide reward signals is pretty much the idea I have been mulling over for more than a decade. I had initially thought about using a GAN as generator but transformers are so much more powerful. Interesting to see that my intuition was correct though and thats pretty much how reasoning models are being built. Also the application of generating code that leads to meta coding -> AGI is pretty much what is happening now*

## [[2025-04-23-Wednesday]]
- [LLMs and World Models, Part 2 - by Melanie Mitchell](https://aiguide.substack.com/p/llms-and-world-models-part-2)
	- *OthelloGPT is a pretty cool study where the transformer is trained on a sequence of moves and predicts the next action. Researches then took the activations of the transformer layers and trained a linear (& nonlinear) classifier to predict the state of the board. This would tell us where the transfomer is encoded the state of the board or is just learning arbitrary rules*
	- The claims of emergent abstract world models in LLMs are not yet supported by strong evidence. There is some evidence of such world models arising in transformers trained on narrow domains (Othello, chess, mazes, etc.) but also evidence that their abilities arise not from human-like internal models but from large “bags of heuristics”.
	- Humans probably use a mix of abstract world models and bags of heuristics for problem-solving as well, but I think it’s likely that humans don’t have the same capacity as today’s LLMs to learn enormous numbers of specific rules. I’d guess that it’s actually our human limitations—constraints on working memory, on processing speed, on available energy—as well as our continually changing and complex environments, that require us to form more abstract and generalizable internal models. Perhaps we will need to constrain and challenge our machines in similar ways to get them to “think” more abstractly and to be better at generalizing outside of their training data distributions
- [Announcing the Agent2Agent Protocol (A2A) - Google Developers Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
	- A2A is an open protocol that complements Anthropic's Model Context Protocol (MCP), which provides helpful tools and context to agents.
	- Full protocol: [A2A/specification/json/a2a.json at main · google/A2A · GitHub](https://github.com/google/A2A/blob/main/specification/json/a2a.json)

## [[2025-04-22-Tuesday]]
[GitHub - browser-use/web-ui: Run AI Agent in your browser.](https://github.com/browser-use/web-ui) - Run LLMs locally in your web browser
## [[2025-04-10-Thursday]]
[GitHub - huggingface/open-r1: Fully open reproduction of DeepSeek-R1](https://github.com/huggingface/open-r1) #tinker_short 
## [[2025-04-01-Tuesday]]
[Those MCP totally 10x my Cursor workflow… - YouTube](https://www.youtube.com/watch?v=oAoigBWLZgE)
MCP server repos - set this up successfully with Cursor - really awesome!
- [Sequential Thinking \| Smithery](https://smithery.ai/server/@smithery-ai/server-sequential-thinking)
- [Open-Source MCP servers \| Glama](https://glama.ai/mcp/servers)
[I gave Claude root access to my server... Model Context Protocol explained - YouTube](https://www.youtube.com/watch?v=HyzlYwjoXOQ)
- Many of the MCP servers are just APIs on top of existing APIs
- Gives me vibes of ChatGPT plugins
## [[2025-03-31-Monday]]
- [Tracing the thoughts of a large language model \ Anthropic](https://www.anthropic.com/research/tracing-thoughts-language-model?utm_source=alphasignal)  
  -   Claude sometimes thinks in a conceptual space that is shared between languages, suggesting it has a kind of universal “language of thought.” 
  -   Claude will plan what it will say many words ahead, and write to get to that destination. 
  - we find that Claude employs multiple computational paths that work in parallel. One path computes a rough approximation of the answer and the other focuses on precisely determining the last digit of the sum. These paths interact and combine with one another to produce the final answer.
  - When we ask Claude a question requiring multi-step reasoning, we can identify intermediate conceptual steps in Claude's thinking process
  - Why is this so confusing for the model? Why does it continue to write the sentence, producing bomb-making instructions?
  - We find that this is partially caused by a tension between grammatical coherence and safety mechanisms. Once Claude begins a sentence, many features “pressure” it to maintain grammatical and semantic coherence, and continue a sentence to its conclusion. This is even the case when it detects that it really should refuse.

## [[2025-03-26-Wednesday]]
- [Introducing 4o Image Generation \| OpenAI](https://openai.com/index/introducing-4o-image-generation/)
- [Gemini 2.5: Our newest Gemini model with thinking](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#building-on-best-gemini)
	- [Gemini 2.5 - The Thinking Family of Models - YouTube](https://www.youtube.com/watch?v=B3wLYDl2SmQ)
- [x] [Tutorials Overview - DSPy](https://dspy.ai/tutorials/) - create a simple py notebook with this (~2-3 hours)  [completion:: 2025-03-28]
- [x] Build an MCP server & client - [For Server Developers - Model Context Protocol](https://modelcontextprotocol.io/quickstart/server) (2-3 hours)  [completion:: 2025-04-03]
- Wrapped up [[code-junkyard/llm-api.ipynb]]
	- [courses/anthropic\_api\_fundamentals/01\_getting\_started.ipynb at master · anthropics/courses · GitHub](https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/01_getting_started.ipynb)
	- [courses/tool\_use/01\_tool\_use\_overview.ipynb at master · anthropics/courses · GitHub](https://github.com/anthropics/courses/blob/master/tool_use/01_tool_use_overview.ipynb)
- [Imperative vs Declarative Programming - YouTube](https://www.youtube.com/watch?v=E7Fbf7R3x6I)
	- Declarative programming is how the user thinks based on what it wants accomplished
	- Imperative programming is the step by step execution model of the machine
	- Declarative API is better and always has an imperative method underlying it
- [What is a REST API? - YouTube](https://www.youtube.com/watch?v=lsMQRaeKNDk)
	- REST -> Representational State Transfer
	- CRUD -> Create (POST), Read (GET), Update (PUT), Delete (DELETE) : HTTP methods in ()
- [DSPy Explained! - YouTube](https://www.youtube.com/watch?v=41EfOY0Ldkc), [CS 194/294-196 (LLM Agents) - Lecture 5, Omar Khattab - YouTube](https://www.youtube.com/watch?v=JEMYuzrKLUw)
	- DSPy is the PyTorch for LLM Programs 
	- Build compound AI systems
	- Provides a declarative framework to program LMs: just provide the inputs & outputs and let the framework fill in the underlying prompt stringiness

## [[2025-03-25-Tuesday]]
- [The "think" tool: Enabling Claude to stop and think \\ Anthropic](https://www.anthropic.com/engineering/claude-think-tool)
	- *Useful when the LLM needs to do multi step tool calling workflows. Helps it in reassessing the plan based on tool outputs rather than making incorrect tool calls. Apparently tool calling accuracy in multi step trajectories is super low.*
	- *Seems like a simple tool addition that just does CoT instead of adding CoT to the main system prompt.*
	- Extended thinking is all about what Claude does before it starts generating a response. With extended thinking, Claude deeply considers and iterates on its plan before taking action. The "think" tool is for Claude, once it starts generating a response, to add a step to stop and think about whether it has all the information it needs to move forward. This is particularly helpful when performing long chains of tool calls or in long multi-step conversations with the user.
- [Claude's extended thinking \\ Anthropic](https://www.anthropic.com/research/visible-extended-thinking)
	- When Claude 3.7 Sonnet is using its extended thinking capability, it could be described as benefiting from "serial test-time compute". That is, it uses multiple, sequential reasoning steps before producing its final output, adding more computational resources as it goes.
	- *Seems like Extended thinking mode models are finetuned on producing long CoT tokens before generating a response so they are not doing multiple function calls per se. That was the poit Sri & Chaitanya were making in the LLM breakout [[2025-03-24-Monday|yesterday]] which is interesting.*
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/pdf/2303.11366)
	- It remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials
	- *Has 3 LMs working alongside each other : Actor -> policy model; evaluator -> reward model; self-reflection -> update step but does not change the weights of the policy model - just influences it by changing the input prompt + memory*
	- ![[2025-03-25-Tuesday-2025-03-25.png]]
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/pdf/2309.07864)

## [[2025-03-19-Wednesday]]
- [How DeepSeek Rewrote the Transformer \[MLA\] - YouTube](https://www.youtube.com/watch?v=0VLAoVGf_74)
	- Really good overview of KV caching and Grouped Query Attention (GQA used in Llama), and multi head latent attention (used in DeepSeekR1)
	- ![[2025-03-19-Wednesday-2025-03-19.png]]
	- ![[2025-03-19-Wednesday-2025-03-19-1.png]]

## [[2025-03-14-Friday]]
- [How I think about LLM prompt engineering](https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering?__readwiseLocation=) (highlighted with [[Readwise]])
	- Very interesting article of thinking of LLMs as a continuous spaced database of fact & program vectors.
	- Out prompt is a key and input into the database and the output is the interpolated sequence of tokens that are in the data store closest to the key being queried.

## [[2025-02-24-Monday]]
-  [The Ultra-Scale Playbook - a Hugging Face Space by nanotron](https://huggingface.co/spaces/nanotron/ultrascale-playbook) #some-day 
	- Similar to the Deepmind mini book on training on TPUs
- #tinker_short [Welcome to the 🤗 AI Agents Course - Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)

## [[2025-02-08-Saturday]]
- [How To Scale Your Model](https://jax-ml.github.io/scaling-book/) - Deepmind TPU minibook 
- [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) documents a new reasoning model with 2 novel contributions:
	- [S1: The $6 R1 Competitor? - Tim Kellogg](https://timkellogg.me/blog/2025/02/03/s1) & [S1: The $6 R1 Competitor?](https://simonwillison.net/2025/Feb/5/s1-the-6-r1-competitor/)
	- finetuned from Qwen 2.5 32B on **just 1000 questions paired with reasoning traces** distilled from Gemini 2.0 Flash Thinking, filtered for difficulty, diversity, and quality (26 mins of training on 16 H100s)
	- controllable test-time compute by either forcefully terminating the model's thinking process or lengthening it by appending "Wait" multiple times to the model's generation when it tries to end.

## [[2025-01-18-Saturday]]
- [My AI/LLM predictions for the next 1, 3 and 6 years, for Oxide and Friends](https://simonwillison.net/2025/Jan/10/ai-predictions/?__readwiseLocation=)

## [[2025-01-11-Saturday]]
- [What do the gods of generative AI have in store for 2025? - Economist](https://read.readwise.io/new/read/01jh6r78hdkwbrygarrcdxdcfp) 
- [🌁#80: What's in 2025? From Elad Gil, François Chollet, Maxime Labonne, swyx and others](https://www.turingpost.com/p/fod80?__readwiseLocation=)
	- "It's going to be the year of inference-time search, and we will see many efforts to create an open source reproduction of O1. Also ARC-AGI will be solved."
	- Flow engineering/"guided chain of thought" will be deployed much more in production than o1/reasoning type models." 
	- "Edge LLMs will go from feasible to popular, thanks to progress with small language models and optimized inference."
- [OpenAI o3 Breakthrough High Score on ARC-AGI-Pub](https://arcprize.org/blog/oai-o3-pub-breakthrough?__readwiseLocation=)
	- ARC-AGI-1 took 4 years to go from 0% with GPT-3 in 2020 to 5% in 2024 with GPT-4o. All intuition about AI capabilities will need to get updated for o3.
	- o3's improvement over the GPT series proves that architecture is everything. You couldn't throw more compute at GPT-4 and get these results. Simply scaling up the things we were doing from 2019 to 2023 – take the same architecture, train a bigger version on more data – is not enough. Further progress is about new ideas.
	- early data points suggest that the upcoming ARC-AGI-2 benchmark will still pose a significant challenge to o3, potentially reducing its score to under 30% even at high compute (while a smart human would still be able to score over 95% with no training). This demonstrates the continued possibility of creating challenging, unsaturated benchmarks without having to rely on expert domain knowledge. You'll know AGI is here when the exercise of creating tasks that are easy for regular humans but hard for AI becomes simply impossible.
	- Effectively, o3 represents a form of deep learning-guided program search. The model does test-time search over a space of "programs" (in this case, natural language programs – the space of CoTs that describe the steps to solve the task at hand), guided by a deep learning prior (the base LLM). The reason why solving a single ARC-AGI task can end up taking up tens of millions of tokens and cost thousands of dollars is because this search process has to explore an enormous number of paths through program space – including backtracking.

## [[2025-01-07-Tuesday]]
- [Building effective agents \\ Anthropic](https://www.anthropic.com/research/building-effective-agents?__readwiseLocation=)
	- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
	- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.
	- When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.
	- The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.	
	- Our suggestions for deciding on tool formats are the following:
		- Give the model enough tokens to "think" before it writes itself into a corner.
		- Keep the format close to what the model has seen naturally occurring in text on the internet.
		- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.
	- ![[2025-01-07-Tuesday-2025-01-07-augmented-llm.png]]
	- ![[2025-01-07-Tuesday-2025-01-07-coding-agent.png]]

## [[2024-12-20-Friday]]
- [Finally, a Replacement for BERT: Introducing ModernBERT](https://huggingface.co/blog/modernbert)
	- The recent high-profile advances in LLMs have been in models like GPT, Llama, and Claude. These are decoder-only models, or generative models. What we've done, essentially, is port these advances back to an encoder-only model.
	- The output of an encoder-only model is a list of numerical values (an embedding vector). You might say that instead of answering with text, an encoder model literally encodes its "answer" into this compressed, numerical form. That vector is a compressed representation of the model's input, which is why encoder-only models are sometimes referred to as representational models.
	- #j595/idea - It might be worth finetuning a ModernBERT model for NotificationLM and even AttentionLLM. This would be the ultimate version that ships and run on device - might even run on the J310
	- ModernBERT's context length of 8,192 tokens is over **16x** larger than most existing encoders. This is critical, for instance, in RAG pipelines, where a small context often makes chunks too small for semantic understanding.
	- For code retrieval, ModernBERT is unique. There's nothing to really compare it to, since there's never been an encoder model like this trained on a large amount of code data before.
	- *Adds RoPE embeddings instead of the vanilla ones from OG Transformers*
	- One of ModernBERT's most impactful features is **Alternating** **Attention**, rather than full global attention. In technical terms, this means that our attention mechanism only attends to the full input every 3 layers (**global attention**), while all other layers use a sliding window where every token only attends to the 128 tokens nearest to itself (**local attention)**.
		- ![[2024-12-20-Friday-2025-01-13.png]]

## [[2024-12-17-Tuesday]]
- Wrapped up - [State of AI Report - 2024 ONLINE - Google Slides](https://docs.google.com/presentation/d/1GmZmoWOa2O92BPrncRcTKa15xvQGhq7g4I4hJSNlC0M/preview?slide=id.g24daeb7f4f0_0_5682) 
- Good blog post with an intuitive explanation of RoPE - [You could have designed state of the art positional encoding](https://fleetwood.dev/posts/you-could-have-designed-SOTA-positional-encoding?__readwiseLocation=)
- [Dev Day Holiday Edition—12 Days of OpenAI: Day 9 - YouTube](https://www.youtube.com/watch?v=14leJ1fg4Pw)
	- Vision inputs into the API
	- Will introduce WebRTC in addition to Websockets for Realtime API - would make it a lot easier to use compared to what I was prototyping with on [[2024-10-16-Wednesday]]
	- Preference finetuning - this approach just needs a prompt and two outputs (preferred and non preferred). It is different from the prompt-completion like Supervised API that I used before - [[2022-04-29-Friday#Openai Chatbot that I Finetuned on My Hangouts History]]]
- [Search—12 Days of OpenAI: Day 8 - YouTube](https://www.youtube.com/watch?v=OzgNJJ2ErEE&t=2s)
	- Bunch of additions to Search

## [[2024-11-05-Tuesday]]
- [Mixture of Parrots: Experts improve memorization more than reasoning](https://arxiv.org/abs/2410.19034#:~:text=Mixture%20of%20Parrots%3A%20Experts%20improve%20memorization%20more%20than%20reasoning,-Samy%20Jelassi%2C%20Clara&text=The%20Mixture%2Dof%2DExperts%20(,parameters%20with%20minimal%20computational%20overhead.) - follows the intuition that the parameters mostly contribute to storing information rather than doing much reasoning.

## [[2024-10-25-Friday]]
- [Introducing quantized Llama models with increased speed and a reduced memory footprint](https://ai.meta.com/blog/meta-llama-quantized-lightweight-models/)
	- Uses [GitHub - pytorch/executorch: On-device AI across mobile, embedded and edge for PyTorch](https://github.com/pytorch/executorch) as the inference engine (alternative to [[archive/apple/attachments/llama-cpp.ipynb]])
	- These models offer a reduced memory footprint, faster on-device inference, accuracy, and portability—all while maintaining quality and safety for developers to deploy on resource-constrained devices. Given the limited runtime memory available on mobile devices, we prioritized short-context applications up to 8K for these new quantized models. Our results show we can achieve superior accuracy by training with quantization as opposed to post-processing.
	- We developed these state-of-the-art models using Quantization-Aware Training with LoRA adaptors (QLoRA) to optimize performance in low-precision environments. We also used SpinQuant, a technique that enables us to determine the best possible combination for compression while retaining the most possible quality.
	- To initialize QAT, we utilize BF16 Llama 3.2 model checkpoints obtained after supervised fine-tuning (SFT) and perform an additional full round of SFT training with QAT. We then freeze the backbone of the QAT model and perform another round of SFT with low-rank adaptation (LoRA) adaptors applied to all layers within the transformer block. Meanwhile, the LoRA adaptors' weights and activations are maintained in BF16.
		- ====*This is the better quantization method because it is essentially using the original training dataset (data aware) in a low bit regime - which is better than blidly chopping off bits . It gives the network the opportunity to learn its way with limited memory*====
	- While the method is less accurate than QAT + LoRA, a key advantage of SpinQuant is its portability and ability to operate without requiring access to training datasets, which are often private. It's an attractive solution for applications where data availability or computational resources are limited

## [[2024-10-24-Thursday]]
- [Introducing Multimodal Embed 3: Powering AI Search](https://cohere.com/blog/multimodal-embed-3)
	- Like CLIP embedding but trained more broadly and outperforms it for retrievals - just a more updated version
- #tinker [Stanford CS229 I Machine Learning I Building Large Language Models (LLMs) - YouTube](https://www.youtube.com/watch?v=9vM4p9NN0Ts) 
	- [Slides](https://drive.google.com/file/d/1B46VFrqFAPAEj3kaCrBAtQqeh2_Ztawl/view)
	- Skips deep architecture details to focus on practical training aspects, data handling, and evaluation methods.

## [[2024-10-22-Tuesday]]
- [Merge Large Language Models with mergekit](https://huggingface.co/blog/mlabonne/merge-models) --- [GitHub - arcee-ai/mergekit: Tools for merging pretrained large language models.](https://github.com/arcee-ai/mergekit?tab=readme-ov-file#mixture-of-experts-merging)
	- Model merging is a technique that combines two or more LLMs into a single model. It's a relatively new and experimental method to create new models for cheap (no GPU required). Model merging works surprisingly well and produced many state-of-the-art models
	- Detailed how SLERP, TIES, DARE, and passthrough work and provided examples of configurations.

## [[2024-10-18-Friday]]
- [OpenAI Model Distillation: A Guide With Examples | DataCamp](https://www.datacamp.com/tutorial/model-distillation-openai)
	- Pretty straightforward - (i) just store=True for prompt completions, (ii) use Evals to measure results as graded by GPT4o and (iii) run distillation of some small base model and eval again
	- Not sure if it is just doing fintuning like [[*ongoing/tinkering#Openai Gpt-3 Chatbot]] or actually learning the output distribution of the teacher model from the softmax layer
- [GPT-4o Vision Fine-Tuning: A Guide With Examples | DataCamp](https://www.datacamp.com/tutorial/gpt-4o-vision-fine-tuning)
	- Similar API as what I had used to built the [[*ongoing/tinkering#Openai Gpt-3 Chatbot]] in mid 2022 - using the finetuning API and JSONL file for prompts and completions
- [Experimenting with audio input and output for the OpenAI Chat Completion API](https://simonwillison.net/2024/Oct/18/openai-audio/)
- [AI - 2024AD: 212-page Report (from this morning) Fully Read w/ Highlights - YouTube](https://www.youtube.com/watch?v=CyOL_4K2Nyo)
	- Highlights copyright issues and how creators are warming upto it with companies jumping into licensing monetization (Created by Humans, Calliope networks) - [[archive/Crawlspace]]
		- Zuckerberg claims content creators might overestimate how valuable that data is in model training
- [Llama 3.2: Revolutionizing edge AI and vision with open, customizable models](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)
- Probably have this in [[*shiny-fm-llm]]: 
	- Llama-1 was just a pretrained generation model, 
	- Alpaca was instruction finetuned on Llama-1 - its performance was matching OpenAIs text-davinci-003 (InstructGPT model),
	- Vicuna was finetuned Alpaca using ShareGPT (dataset collected from ChatGPT) and was a chatbot
	- Llava is simply a vision-encoder + projection-layer + Vicuna-LLM
		- Vision encoder is off the shelf pretrained. Llava training involved 2 stages
			- Stage 1: Pretraining for Feature alignment: Trains the projection layer weights to align text & vision
			- Stage 2: Fine-tuning End-to-end: Trains the projection layer + Vicuna LLM weights
- [GitHub - mlc-ai/mlc-llm: Universal LLM Deployment Engine with ML Compilation](https://github.com/mlc-ai/mlc-llm)
	- Helps you deploy LLMs across diverse hardware: GPUs (NVIDIA, AMD, Apple, Intel), CPUs, and web browsers. It uses ML compilation to optimize performance. You can run models like Llama 2 and Vicuna on your chosen device with OpenAI-compatible APIs.

## [[2024-10-14-Monday]]
- Liquid Foundation Models are a new architecture that seem to demonstrate the same scaling law as Transformers and State Space Models - not open source weights yet but is being created by Liquid AI
- [🍓 Ichigo: Llama learns to talk - Homebrew](https://homebrew.ltd/blog/llama-learns-to-talk) - early fusion speech models. Provides a recipe to convert any off the shelf LLM to take in speech tokens directly
	- [src](https://www.reddit.com/r/LocalLLaMA/comments/1g38e9s/ichigollama31_local_realtime_voice_ai/) (we put audio through whisper then quantize it using a vector quantizer). It's more like chameleon (but without the need of using a different activation function).
- [Apple DROPS AI BOMBSHELL: LLMS CANNOT Reason - YouTube](https://www.youtube.com/watch?v=tTG_a0KPJAc) 
- Super cool mathematical visualization library that 3Blue1Brown uses for his videos - [manim: A community-maintained Python framework for creating mathematical animations.](https://github.com/ManimCommunity/manim?tab=readme-ov-file)
	- Command: `manim -p -ql example.py SquareToCircle` ![[manim-example.py]] 

## [[2024-09-30-Monday]]
- Interesting comparison of various LLM inference engines: [Face-off of 6 maintream LLM inference engines : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1ff79bh/faceoff_of_6_maintream_llm_inference_engines/)
- **Larger quantized models** generally outperform smaller high-precision models, as shown in a [graph comparing quantization vs. perplexity](https://www.reddit.com/r/LocalLLaMA/comments/1441jnr/k_quantization_vs_perplexity/). A **70B model** at 4-bit quantization typically surpasses an **8B model** at full precision due to more internal token relationship representations.

## [[2024-09-29-Sunday]]
- Wow [NotebookLM](https://notebooklm.google.com/notebook/aadef398-76ba-4a59-b5f6-ab4c7bb8b935?pli=1) is pretty awesome - ![[Ammar resume.wav]]
	- The platform represents a shift in LLM interaction paradigms, moving beyond traditional chat interfaces. It aims to simplify complex information processing and presentation, catering to diverse user needs in research, study, and professional contexts.

## [[2024-09-19-Thursday]]
- Thoughts on [[hands on/hands on aiml]]-4o1 as inference time compute from a newsletter (the actual LLM might be smaller but it does more reasoning)
	- > What OpenAI did was get the o1 models to go through just this sort of "thinking" process, producing hidden thinking tokens before giving a final answer. In doing so they revealed another scaling law - the longer a model "thinks," the better its answer is. Just like the scaling law for training, this seems to have no limit, but also like the scaling law for training, it is exponential, so to continue to improve outputs, you need to let the AI "think" for ever longer periods of time.
- Do a small hands on tutorial in python to grasp concepts of DPO and PPO in RL 
- Good computer vision library to get up and running quickly [GitHub - roboflow/supervision: We write your reusable computer vision tools](https://github.com/roboflow/supervision)
	- [GitHub - autodistill/autodistill: Images to inference with no labeling (use foundation models to train supervised models).](https://github.com/autodistill/autodistill)
	- [Detect - Ultralytics YOLO Docs](https://docs.ultralytics.com/tasks/detect/#export)

## [[2024-09-13-Friday]]
- [LLMs develop their own understanding of reality as their language abilities improve | MIT News | Massachusetts Institute of Technology](https://news.mit.edu/2024/llms-develop-own-understanding-of-reality-as-language-abilities-improve-0814)
	- Why does it feel like I already read this article before and have a rough understanding of the experiments

## [[2024-09-12-Thursday]]
- Would be interesting to spend some time scoping out a project to do for the follow areas: #tinker_short 
	- [x] Model distillation -> Go step by step in training a small model (pretrained or from scratch) using the output distribution of a bigger 70b model perhaps  [completion:: 2024-12-12]
		- [ ] [Everything You Need to Know about Knowledge Distillation](https://huggingface.co/blog/Kseniase/kd)
		- [ ] [Knowledge Distillation](https://huggingface.co/docs/setfit/en/how_to/knowledge_distillation)
		- [[2024-12-12-Thursday]]: Went through a few articles for it - Mainly involved using some API to do this
	- Multimodal model -> Try out a model like [[*shiny-fm-vlm#Pixtral]]

## [[2024-09-09-Monday]]
- [PyTorch internals : ezyang's blog](http://blog.ezyang.com/2019/05/pytorch-internals/)
	- three parameters which uniquely determine what a tensor is
		- ![[2024-09-09-Monday-2024-09-09.png]]
	- The distinguishing characteristic of PyTorch when it was originally released was that it provided automatic differentiation on tensors
		- ![[2024-09-09-Monday-2024-09-13.png|300]] -> ![[2024-09-09-Monday-2024-09-13-1.png|300]]