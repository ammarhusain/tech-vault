---
aliases: [2023-11-08]
tags: 
---
**[DayOne](dayone://open?date=2023-11-08)**

# TOP-OF-MIND
-  #j595/journal 
	- [x] #j595/todo Finetune a model with Lit-GPT [GitHub - Lightning-AI/lit-gpt: Hackable implementation of state-of-the-art open-source LLMs based on nanoGPT. Supports flash attention, 4-bit and 8-bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.](https://github.com/Lightning-AI/lit-gpt) ✅ 2024-03-12
	- [ ] #j595/not-todo  Try and run  TinyLlama model through Llama-cpp and karpathy's llama repo
	- Playing around with [Lit-GPT for training LoRA adapters](https://lightning.ai/pages/community/lora-insights/#toc3) 
	- Long call with Leo pitching him to join team
	- Chat with Martin: Marching ahead with ComeML
- #journal/daily 
	- Mostly home all day. 
	- Pallak had a diwali party at her place but they did not know that we are in town. Would have been great to meet up with everyone there together. I really should let folks know in advance before visiting rather than randomly drop in as a surprise. People dont like it and feel uninformed. It would be a lot better to give everyone a heads up next time. #journal/meditations 
# TASKS
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date) OR (has created date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `) OR (created on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
# CROSS-REFERENCED 
```dataviewjs
// Loop through pages 
for (let p of dv.pages()) {
	for (let ol of p.file.outlinks) {
		// find all the cross references of this file
		if (dv.current().file.path == ol.path) {
			// get all the lists in this file
			for (let ls of p.file.lists) {
				if (ls.text.includes(dv.current().file.name)) {
					dv.header(3, p.file.link + "  ...  " + ls.line)
					dv.paragraph(ls.text)
					dv.paragraph("---")
				}
			}
		}
	}
}
```

# VAULT UPDATES
## NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) AND file.ctime < date(substring(this.file.name,0,10))
SORT file.mtime ASCENDING
```

## NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
