---
alias: ["Wednesday, Nov 6, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595/journal MLR Openhouse
	- WRAP- Web Rephraed Augmented Pretraining (synthetic datagen)
		- Rephrasing (using an LLM) pipeline of web data to use for pretraining another LLM
	- CRISP - importance sampling from a large dataset to create specialist dataset for small LM
	- Passive vs Active LLM Personalization
		- Casper needs active personalization (per the papers definition)
		- Passive: observe key info, memory creation, preference inference
		- Active: Feedback & expectations, Human+Synthetic data, RLHF
		- [Poster](https://apple.ent.box.com/s/nh21rr1g2th7ww2wrn30d3xxbo6bjepc)
	- Denoising LM - improves ASR somehow
	- dMel - Discretized Mel Spectral for audio tokenization
		- encoder free speech tokenization, unified autoregressive ASR & TTS
	- SiliconChat - all the voice model demos
	- Multi-Year Continual Evaluation and Training of Foundation Models
	- Autoregressive Model Meets Diffusion - like [[*shiny-fm-vlm#Transfusion]]?
		- Kaleido Diffusion - Have an auto regressive model generate latent tokens then run diffusion on them
		- DART - Denoising AutoRegressive Transformer: Diffusion is a step by step Markovian denoising process - this approach tries to make it like a transformer - so you have access to all previous denoised versions
		- DDLM - Distilled Diffusion Language Models - generates text tokens using a diffusion model
- #journal/daily Sold FujiFilm X100F camera [[photography]]

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-11-06 00:00 %%
%% TCT_TEMPLATED_END 2024-11-06 23:59 %%


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
