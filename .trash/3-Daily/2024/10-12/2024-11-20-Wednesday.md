---
alias: ["Wednesday, Nov 20, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595/journal 
	- Moderately produtive day: got the AttentionLLM physical object intrinsics piped through swift code
	- Figured out bug in the NotificationLM demo app that I built - The chat tokens were misaligned which was causing the LLM to freak out. Had to replace the `<endoftext>` tag with `<assistant>`. Another remined how brittle these LLMs can be at times.
- #journal/daily 
	- Chatted with Melissa @ Lyra about my feeling of being lost and lacking self confidence
		- She asked me to practice mindful awareness: take note of thoughts, feelings & behaviors

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-11-20 00:00 %%
%% TCT_TEMPLATED_END 2024-11-20 23:59 %%


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
