---
publish: 
alias: ["Tuesday, Jul 9, 2024"]
tags: 
created: 2024-07-09-Tuesday 14:40
modified: 2024-07-09-Tuesday 17:14
---

# TOP-OF-MIND
- #j595/journal
	- evaluated the 2 finetuned models that i trained before july 4th break last week: f-2024-07-02_19-12-36-synth-30k-with-medium-engagement-level-largecorpus-nopunctuation.json.gguf and f-2024-07-02_19-40-06-synth-30k-no-medium-engagement-level-largecorpus-sampled.json.gguf
	- updated xcode & j310

%% COMPLETED_TODOIST_TASKS_START %%

%% COMPLETED_TODOIST_TASKS_END %%

%% TCT_TEMPLATED_START 2024-07-09 00:00 %%

- Inbox
	 - Run roomba
	 - https://www.reddit.com/r/ObsidianMD/s/3a8oVD8B7Y
	 - generate new dataset & train a model with the input & out entities in the same order
- Organize
	 - @downtime Review Monarch Financials
	 - change readwise template to make tags nested: readwise/pink /typo etc
	 - update macos
	 - remove day tags from daily notes: wednesday, Monday etc with some grep & sed magic
	 - get the natural language date as alias in daily note
- J595
	 - Download new Xcode and build@on device
	 - eval 2 new trained models: with-medium, with sampled sentences
%% TCT_TEMPLATED_END 2024-07-09 23:59 %%
#### NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

#### NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
