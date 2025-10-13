
[Architecture Doc](https://github.pie.apple.com/heavenly/EmbodiedReasoning/pull/10)

# Task
- [x] Build a behavior tree engine + simulator to demonstrate an LLM generating small BTs  [completion:: 2025-08-14]
- [ ] Create a behavior tree synthetic dataset to finetune a smaller model
- [ ] Attempt to do RLVR with [[hugging face]] on your dummy simulator
	- [unsloth/DeepSeek-R1-Distill-Llama-8B · Hugging Face](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-8B) or Qwen-7B perhaps?
		- Start with these distilled models, then -> SFT  -> RL post training
	- 
# Log

- [2025-05-13-Tuesday](2025-05-13-Tuesday) 
- [[2025-08-14-Thursday]] Chat with Arto, Martin
	- Just build a simple vibe coding tool using BehaviorKit, Motion API + EntityKit API
		- Command could be as simple as: PlayAnimation when someone enters view
- [[2025-05-13-Tuesday]] Chat with Josh
	- Event driven BT: Rearchitect the behavior tree to go from a tick based system that executes the full behavior tree to nodes that get retriggered when an event changes them.
		- Expand action space to 10-20 actions and 10-20 conditions.
			- How will conditions get broken down? Do we add a bunch of entity kit actions & conditions and then have a fallback VLM condition that is a catch all for answering generic questions: "is Chris wearing the funny hat?"
- [[2025-05-09-Friday]] Vibe coded a Behavior Tree Engine, Nisualizer and LLM Generator
	- ![[archive/apple/attachments/action sequencing-m0-2025-05-09.gif]]
	- ![[archive/apple/attachments/action sequencing-m0-2025-05-09.png]]
- [[2025-05-06-Tuesday]] Chat with Greg
	- Would be super useful to have a local LLM generate a behavior tree -> "Hey look at the paper"
	- Have a way for user to verbally command the device point in different spots
		- Roadshow was also hardcoded locations
	- Certain function calls -> map to fixed behavior trees "look at the homework"
		- We should also have facility for dynamic behavior trees that may be slightly modify one or more existing ones: "look at the paper on the left"
	- Supergoals example: "User wants casper to play podcast", "Is what I am wearing today appropriate for dinner tonight"
	- ~={green}This could be a "behavior_planner('goal')" function call and we can restrain it to be timebound and completed within a certain tick count or interrupt it after some time=~


- [[2025-04-30-Wednesday]]
	- Is it possible to serialize and deserialize behavior trees to/from XML?
	- How can I dynamically generate a new BT and run it say within Microcosm?