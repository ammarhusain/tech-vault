---
aliases: [2023-10-11]
tags: 
---

---

**[DayOne](dayone://open?date=2023-10-11)**

# TOP-OF-MIND
- #j595/journal 
	- Got a bit pissed off at Andreas in the LLM standup - he keeps trying to solve problems that we already agreed upon. Just presents them as "awwweesome" novel problems that only he discovered and is thinking about but they are actually super basic ones.
	 - For the VQA task where the scene descriptors need to be supplied to Photographer LLM - I could use a tagging model like [RAM](https://arxiv.org/pdf/2306.03514.pdf) if object localization is not super important. It is a multi-label classification model that could just spit out all the labels of objects that are present in the image.
		 - Apparently Swin is a visual transformer backbone just like ViT for image encoding [[*shiny-fm-vlm#Vision Models]]
	- Reading through the [[*shiny-fm-llm#TinyStories How Small Can Language Models Be and Still Speak Coherent English?]] paper it occurs to me that it would be worhtwhile for us to train our own SLM that is photographer specific. We could take one of the synthetic datasets that Xin is trying to produce and train an SLM from scratch to see how it performs - rather than depending on a 7B or 13B model. This falls in line with Chris' goal of model distillation. Talk to Xin about it?
		- [x] #j595/todo Follow Karpathy GPT-mini tutorial - [[*shiny-fm-llm#[Let's build GPT from scratch, in code, spelled out. - YouTube](https //www.youtube.com/watch?v=kCc8FmEb1nY)]] ✅ 2023-10-20
			- Train your own SLM with a TinyStories like dataset
		- This could be a task I tackle while in India, Need to go through Karpathys mini-GPT tutorial
		- Work to get a very small dataset - browse through the TinyStories dataset on HuggingFace
		- Attempt to train a very simple 2 ish layer Transformer model
		- How do we run inference on it - using llamacpp or just pytorch?
		- Xin: finetuned a 1B model for photographer already and it seems to work decently well. *I did it on TinyLLama [https://huggingface.co/PY007/TinyLlama-1.1B-step-50K-105b](https://huggingface.co/PY007/TinyLlama-1.1B-step-50K-105b) with [https://github.com/artidoro/qlora](https://github.com/artidoro/qlora)*

---
# TASKS
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
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
