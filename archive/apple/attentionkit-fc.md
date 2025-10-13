---
created: 2023-11-28-Tuesday 17:27
modified: 2023-11-28-Tuesday 17:27
publish: 
---

> [!info] Resources
> ![[archive/apple/attachments/attention-junk.ipynb]]
> ![[archive/apple/attachments/attention-st-ui.py]]
> AttentionKit [design doc](https://quip-apple.com/dY3wAYbZiDgV)
> HI [collaboration doc](https://quip-apple.com/ZXiyAabHNQNH)
> [Attention streamlit app](http://17.220.22.194:8501/)
> MICA animation prototype file from Marisa : /Users/ammarh/Documents/j595-docs/Attention/MarisaAttention-FaceTrack-FC2-20.ca
> 
> [[archive/apple/attachments/attention-internal-judgment-HI-illustration.png]]
 


### Fine-tuning

[[2025-03-04-Tuesday]]
Can we re architect the AttentionLM to be a SmolLM based reward model that takes in a state observation and then outputs a score per entity - so train a regression or classification head that emits an attention score. This would be different than a generation head with grammar that we finetune the shit out of right now

> [!info] [[LoRA]]



[[2024-06-03-Monday]]
- [ ] #j595/not-todo  Prepare for a demo within AttentionTestApp where you can say "Look at me", "Look at Manuel", "Look at pencil" and the device can give those corresponding entities high attention.


[[2024-05-13-Monday-W20|2024-05-14-Tuesday]]
Research on pretrained SLM Llama models smaller than <1.1B ie TinyLlama / ShearedLlama
[Felladrin (Victor Nogueira)](https://huggingface.co/Felladrin)
[JackFram/llama-160m · Hugging Face](https://huggingface.co/JackFram/llama-160m) - 160M model trained on wikipedia
[Felladrin/Llama-160M-Chat-v1 · Hugging Face](https://huggingface.co/Felladrin/Llama-160M-Chat-v1) - base model is the llama-160m above; just finetuned for chat
[Locutusque/TinyMistral-248M · Hugging Face](https://huggingface.co/Locutusque/TinyMistral-248M)


[[2024-03-25-Monday]]
[Learning how to fine-tune (first time), I've provided links to tutorials I found, but would anybody else recommend further material. : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1bkqxui/learning_how_to_finetune_first_time_ive_provided/) - found it in AI news - not sure how helpful it will be

[[2024-03-19-Tuesday]] - we could have a distilled base model and then LoRA adapters for various experiences 
Do we have a dataset of Siri utterances that could be used for model finetuning?
Good step by step article to get started with : [How to Fine-Tune LLMs in 2024 with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)

[[2024-03-15-Friday]]: [How to Fine-tune an LLM Part 3: The HuggingFace Trainer](https://wandb.ai/capecape/alpaca_ft/reports/How-to-Fine-tune-an-LLM-Part-3-The-HuggingFace-Trainer--Vmlldzo1OTEyNjMy)
Could be useful to refer to when I start the fine-tune process. Its a 3 part series though the second part is more PyTorchy vs the 3rd part using [[hugging face]] tools.

[[2024-03-13-Wednesday]]: [GitHub - openai/transformer-debugger](https://github.com/openai/transformer-debugger) - interesting library to debug and inspect transformer based models - worth a try

- [[2024-03-12-Tuesday]]
	- [Fine-tune a Mistral-7b model with Direct Preference Optimization | by Maxime Labonne | Towards Data Science](https://towardsdatascience.com/fine-tune-a-mistral-7b-model-with-direct-preference-optimization-708042745aac)
		- a popular preference dataset [Anthropic/hh-rlhf](https://huggingface.co/datasets/Anthropic/hh-rlhf/viewer/default/train), 
			- The structure of the dataset is straightforward: for each row, there is one chosen (preferred) answer, and one rejected answer. The goal of RLHF is to guide the model to output the preferred answer.
		- [Intel/orca_dpo_pairs](https://huggingface.co/datasets/Intel/orca_dpo_pairs)
			- Authors generated answers with GPT-4/3.5 to create the preferred answers, and with [Llama 2 13b chat](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) to create the rejected responses. It’s a smart way to bypass human feedback and only rely on models with different levels of performance.
		- Uses the HuggingFace DPO trainer
			```
			# Training arguments  
			training_args = TrainingArguments(  
			per_device_train_batch_size=4,  
			gradient_accumulation_steps=4,  
			gradient_checkpointing=True,  
			learning_rate=5e-5,  
			lr_scheduler_type="cosine",  
			max_steps=200,  
			save_strategy="no",  
			logging_steps=1,  
			output_dir=new_model,  
			optim="paged_adamw_32bit",  
			warmup_steps=100,  
			bf16=True,  
			report_to="wandb",  
			)  
			  
			# Create DPO trainer  
			dpo_trainer = DPOTrainer(  
			model,  
			ref_model,  
			args=training_args,  
			train_dataset=dataset,  
			tokenizer=tokenizer,  
			peft_config=peft_config,  
			beta=0.1,  
			max_prompt_length=1024,  
			max_length=1536,  
			)  
			  
			# Fine-tune model with DPO  
			dpo_trainer.train()
			```

	- [Fine-Tuning Llama-2: Tailoring Models to Unique Applications](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications) - Anyscale comprehensive overview article
		- Finetunes for 3 different tasks: structured data extraction; SQL generation; grade school math
		- Does better when the LLM needs to output structured data - can be done better than with supplying several few shot examples.
		- If you notice significant improvements with few shot prompting, fine-tuning could potentially offer even better results. This is because fine-tuning allows you to incorporate far more examples into the model's internal neural network weights, rather than being constrained by context length and consuming tokens for the prompt prefix.
		- If it is a completely new concept (or fact), the chances of the model learning it through small-scale fine-tuning are quite low.
	- Revisited [Finetuning LLMs with LoRA and QLoRA: Insights from Hundreds of Experiments - Lightning AI](https://lightning.ai/pages/community/lora-insights/#toc3)
		- Bunch of experiments on [[LoRA]] parameters to use for fine-tuning

[[2024-03-11-Monday]]
Read through [ML Blog - Fine-Tune Your Own Llama 2 Model in a Colab Notebook](https://mlabonne.github.io/blog/posts/Fine_Tune_Your_Own_Llama_2_Model_in_a_Colab_Notebook.html)
- simple straightforward read - trains a LoRA adapter on a 7B Llama model; uses huggingface and the PEFT library
- [colab](https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd?usp=sharing)

Pretrained LLMs are just next token predictors - they need to be finetuned to follow instructions and be helpful in answering questions.

Read through [ML Blog - A Beginner’s Guide to LLM Fine-Tuning](https://mlabonne.github.io/blog/posts/A_Beginners_Guide_to_LLM_Finetuning.html)
- same task just using the [GitHub - OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) wrapper.
- theres also flash attention which is a more memory efficient self-attention mechanism (not quadratic time ie)


### Logs

[[2024-07-12-Friday]]
#j595/perf 
- AttentionLLM fine-tuned model trained and ready to integrate
	- Experiment evaluations quip: [[FC3] AttentionLLM Finetuning](https://quip-apple.com/RavmAcc8KL2R)
- Will be a drop in replacement for the larger model to start with - ie invoked after every “final” token in AudioSpeechRecognitionObservation (without trigger word)
	- Later: Implement 1Hz sampling audio sampling
- Live demo: [http://17.220.22.194:8501/](http://17.220.22.194:8501/)
- Recorded demo: [[archive/apple/attachments/attentionkit-fc-2024-07-12.mp4]]
- Next steps:
	- Swap out the model and tune using the AttentionTestApp
	- Implement a corrections interface within the web UI - to quickly annotate and collect training data

[[2024-03-29-Friday]]
Finetuned a TinyLlama model with Shakespeare as reason
![[archive/apple/attachments/attentionkit-fc-2024-03-31.png]]

[[2024-02-16-Friday]]
#j595/perf 
Built an integrated Attention-LLM MVP:
Motif Audio + swift tool + Motif track summarizer + LLM w/ grammar + publish sigmon channel + MotifTools visualize  
This integration should be good for HI to test 
- integrate with CIKit and tracking next
![[archive/apple/attachments/attentionkit-fc-2024-02-16-1.png]]
![[archive/apple/attachments/attentionkit-fc-2024-02-16.png]]
[artifacts](https://www.icloud.com/attachment/?u=https%3A%2F%2Fcvws.icloud-content.com%2FB%2FAaRKJXHyzglxmuoQi8xmw13AvE0bAVwtmbBcJe-JbvvdAooX8gLrD3i2%2F%24%7Bf%7D%3Fo%3DAmUDwdYY2fW_xf4bCaeCebKbfP4HW9bJnDIxDa_5G40k%26v%3D1%26x%3D3%26a%3DCAog00XYHRsW88GJDn73dfqsjtybre040ncJbsuihkqvfvkSbRClroKh2zEYpb799OQxIgEAUgTAvE0bWgTrD3i2aiYSjj1ZMK2QTUuYOhUrBXmeFr1qBqW2hQwoACBk4bpy2GJc7icGWHImzh_OCg8UiEWw0SSHsgLiQcVuIDLQmbcq2QmooKK5NXBLnA8F6Ro%26e%3D1710716051%26fl%3D%26r%3D083E4E61-8235-42C8-B83A-BF7731B7C0DE-1%26k%3D%24%7Buk%7D%26ckc%3Dcom.apple.clouddocs%26ckz%3Dcom.apple.CloudDocs%26p%3D107%26s%3D93FsHkpzbV1g_Zhc0lTS6iFA67A&uk=_2GmgXOXtFC9re5h9y1Ocg&f=attn-llm-demo-3-1.mov&sz=82258601)

[[2024-02-05-Monday]]
Facing, Speaking work much better with NatVoc enabled:
login -f mobile defaults write com.apple.motif NatVocEnabled -bool true
login -f mobile defaults read com.apple.motif NatVocEnabled

Invoking is a command that shows up on Sunglasses but may not get serialized in the MotifTrackerState messaage - follow up with Paul
Continuous State in MotifTrackerState is: x, x', y, y', z, z' where x is coming out of the screen, y is sideways and z is up & down. Might just want to take a norm or just the x perhaps? 


[[2024-01-31-Wednesday]]
Wanted to setup a demo with Everest where I can set facing, gazing, speaking attributes for agents and then use my voice for LLM interactions. Though that might not be a feasible approach due to the following Everest bugs:
- Gazing, speaking, facing etc dont seem to get set correctly from Everest to MotifTrackerState
- UUIDs for agents dont set correctly. I can view the entity UUID via `MotifTools entity` however. 
Probably better for me to focus on getting the LLM prompts working instead 

[[2024-01-30-Tuesday]]
Wrapped up MotifTrackerState summarization (more or less)

[[2024-01-23-Tuesday]]
In order to visualize AttentionKit output just run on device:
sigmonctl stream --channels /Attention/State
Make sure there are Motif Tracks coming through 

To run Jordans stuff that gives audio output with final words:
1.  Install the root he sent ( [https://apple.box.com/s/2oo1rha7h90c61cmwouz2599jllh2lcm](https://apple.box.com/s/2oo1rha7h90c61cmwouz2599jllh2lcm))
2. On device run: MotifTools audio -s
To check if audio is being published: sigmonctl stream --channels /Audio/SpeechRecognition

[[2024-01-12-Friday]]
Things to try if AttentionLLM is greenlighted:
- [ ] Speeding up inference by prompt caching LLMLingua
- [ ] Summarizing entities and adding a notion of time in the environment - better ways to bake in historical context
- [ ] Parsing entities from a real mcap file
- [ ] Emit attention scores than just singular entities to attend to
- [ ] Figure out policies to fuse with "jumpscare" attention
- [ ] Add an ambient attention (look down etc) - for disengaging with either user.
- [ ] Reason for LLM output should come before the output entity in the demonstration to promote CoT reasoning

[[2024-01-03-Wednesday]]
- Jumpscare attention (quick responses to motion or novelty or someone suddenly starting to speak) should come from the heuristics based approach (fast / tighter response loop)
- More nuanced behavior where the device maintains long horizon context or semantic scene understanding into attention can leverage LLMs (slower more deliberate response loop)
- [x] #j595/todo How can I prompt cache a long prompt to warm up the LLM before passing it the entity list? ✅ 2024-01-12
- [x] #j595/todo How to encode historical context for attention? ✅ 2024-01-12
- [x] #j595/todo Sync with Reza on memory summarization and see how we can use it for attention summarization ie summarizing not only conversation but also device perception? ✅ 2024-01-23
Marisa Action Items:
- Populate natural language descriptions for device identity / self awareness, attention principles, different attention immersion modes, description of motif signals etc. 

[[2023-12-08-Friday]]
Xin's Dataset generation talk presentation:
Repo: [https://github.pie.apple.com/heavenly/datasets-generation](https://github.pie.apple.com/heavenly/datasets-generation) (Under construction, will add READMEs and comments soon.)
Photographer hand-made examples: [https://github.pie.apple.com/heavenly/datasets-generation/tree/main/examples/photographer](https://github.pie.apple.com/heavenly/datasets-generation/tree/main/examples/photographer)
Quip docs: [https://quip-apple.com/wVYOOkyOdk07](https://quip-apple.com/wVYOOkyOdk07)
Slides: [iCloud Keynote](https://www.icloud.com/keynote/091NK2v8duXJ0zojAZYb1dXNg#datasets_generation)

[[2023-12-04-Monday]]
[Large Language Models are Zero-Shot Rankers for Recommender Systems](https://arxiv.org/pdf/2305.08845.pdf)
Its good to randomize the order of entities passed into the prompt as LLMs can fall prey to sequential ordering
Also one additional steps in enforcing grammar is to ensure the LLM output is parsable and contains only entities that were passed in. Also the scores could be checked to make sure they normalize to one.
Some ways to prompt the model in the appendix

[LARGE LANGUAGE MODELS ARE EFFECTIVE TEXT RANKERS WITH PAIRWISE RANKING PROMPTING](https://arxiv.org/pdf/2306.17563.pdf)
 Empirically we find that listwise ranking prompts from existing work generate completely useless outputs on moderate-sized LLMs. Such observations show that existing popular LLMs do not fully understand ranking tasks, potentially due to the lack of ranking awareness during their pre-training and fine-tuning procedures.
 show pairwise ranking prompting is effective for zero-shot ranking with LLMs. It is able to produce state-of-the-art ranking performance with simple prompting and scoring mechanism.
 The key insights are the observation of the difficulties of LLMs handling ranking tasks in the existing pointwise and listwise formulations. Our designed pairwise ranking prompting (PRP) is effective in reducing the burden of LLMs.

![[archive/apple/attachments/attentionkit-fc-2023-12-05.png]]
![[archive/apple/attachments/attentionkit-fc-2023-12-05-1.png]]
![[archive/apple/attachments/attentionkit-fc-2023-12-05-2.png]]

> [!key idea] 
> Proposes using a sorting algorithm where the comparator function comes via an LLM

[LLMScore: Unveiling the Power of Large Language Models in Text-to-Image Synthesis Evaluation
](https://arxiv.org/pdf/2305.11116.pdf)
our approach leverages vision and language models to transform the image into multi-granularity (image-level and object-level) visual descriptions, which allows us to capture the compositional aspects of multiple objects in the language format. Then we concatenate these descriptions with text prompts and feed them into large language models to reason the alignment between text prompts and images.
![[archive/apple/attachments/attentionkit-fc-2023-12-05-3.png]]
![[archive/apple/attachments/attentionkit-fc-2023-12-05-4.png]]
The score generation process involves the LLMs’ understanding of various evaluation instructions, such as assessing the overall text-image alignment or precisely counting the number of errors in the image. Then the LLMs apply the understanding of the evaluation instruction to the concatenated visual description and text prompt, generating a score that reflects the alignment between the image and the text at multi-granularity compositionality (image-level and object-level). Each score is accompanied by a rationale

[Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/pdf/2306.05685.pdf)

Certain biases that can affect an attention scoring LLM:
- Position bias is when an LLM exhibits a propensity to favor certain positions over others.
- Verbosity bias is when an LLM judge favors longer, verbose responses, even if they are not as clear, high-quality, or accurate as shorter alternatives.
- Limited capability in grading math and reasoning questions. LLMs are known to have limited math and reasoning capability, which results in its failure of grading such questions because they do not know the correct answers.
Our results reveal that strong LLMs can achieve an agreement rate of over 80%, on par with the level of agreement among human experts, establishing a foundation for an LLM-based evaluation framework.


[[2023-11-28-Tuesday]]
Chatted with Jakub to get started on [[archive/apple/attentionkit-fc]]
[[archive/apple/attachments/simple_trackerstate_log.mcap]]
![[archive/apple/attachments/mcap_reader.ipynb]]

HI document on Attention: file://///Users/ammarh/Documents/J595/AttentionSytem.key
[link](file:////Users/ammarh/Documents/J595/scene%20&%20gaze.key)

![[archive/apple/attachments/attention-prompts.txt]]

[[../../attachments/attn-prompt.sh]]

[[../../attachments/attn-prompt-bundle.txt]]
### Evaluation
- [x] #j595/todo Run an evaluation python script on the synthetic data + local running mixtral model [completed:: [[2024-04-25-Thursday]]]
- [x] #j595/todo Evaluate a few different models: mixtral8x7b, mixtral8x22b, llama3-8b, phi-3 etc. [completed:: [[2024-05-08-Wednesday]]]


### Action model 

[[2024-04-15-Monday-W16|2024-04-19-Friday]] - This [guidance-ai/guidance: A guidance language for controlling large language models.](https://github.com/guidance-ai/guidance?tab=readme-ov-file#stateful-guidance-functions) would be very helpful in generating synthetic data for finetuning.It provides simple python functions like select and gen that can be hooked up with a language model. Additionally you can also define other LLM sampling functions with a @guidance decorator. I have played around with it a bit in the junkyard python notebook.

Another interesting library - [Scripted Prompting | LMQL](https://lmql.ai/docs/language/scripted-prompting.html) to work with prompt construction. Instead of trying to get the LLM to steer to some structured output using just grammars this could be a helpful way that can facilitate dynamic prompt construction and allows LMQL programs to respond dynamically to model output. 

We could just host a simple API server in python that uses LMQL to get model output and return relevant results rather than mucking around with complex grammars.

- [ ] Create an endpoint with LMQL or guidance that can produce a json with entities and their attention scores along with an action from a list of available actions that the device has. #j595/not-todo 
	- Would be interesting to try out Marisa's original immersion level descriptions in the prompt

[[2024-04-15-Monday-W16|2024-04-15-Monday]]
Need to build a function calling grammar with the track, lookAt, Nod etc actions that the AttentionLLM can call on entities
