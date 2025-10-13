---
alias: ["Wednesday, Oct 23, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595/journal 
	- Fairly productive today.
	- Generated synthetic data for objects for AttentionLLM. Also finetuned the SmolLM and TinyLlama models
	- Tried out Dave Krimsley PR for vocalization client to subscribe to ASR in AttentionKit. Running into some entitlements issues
		- Was able to get the device up & running pretty quickly - its more a mental block for me to play on the J310 - if everything works its actually not that painful at all

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-10-23 00:00 %%
%% TCT_TEMPLATED_END 2024-10-23 23:59 %%


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
