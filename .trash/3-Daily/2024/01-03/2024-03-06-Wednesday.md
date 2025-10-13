---
aliases: [2024-03-06]
tags: 
---
**[DayOne](dayone://open?date=2024-03-06)**

# TOP-OF-MIND
- #j595/journal 
	- Read through [[*shiny-fm-llm#Can Generalist Foundation Models Outcompete Special-Purpose Tuning? - MedPrompt]]
	- [Proximal Policy Optimization (PPO): The Key to LLM Alignment](https://cameronrwolfe.substack.com/p/proximal-policy-optimization-ppo) - meh article
		- main difference between TRPO and vanilla policy gradient is that TRPO scales the policy updates by the KL divergence between the old & new policy
		- PPO is an extension of TRPO that clips the updates further thereby preventing policy updates to wildly fluctuate.
		- should refer back to my notes for [[reinforcement learning]]
	- Interesting read on decision making: [Reversible and Irreversible Decisions](https://fs.blog/reversible-irreversible-decisions/)
	- Kept hammering at getting the interactive llama.cpp chat working
	- [[comet-ml]] office hours & a useless weekly llm standup - might just need to bite the bullet and write my own comet logging code from superserver.

# NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

# NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
