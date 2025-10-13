---
alias: ["Wednesday, Mar 12, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Spoke to Stacy about [[side-hustle ideas#Crater Lake Airbnb]] at Shady Cove City Hall about 20655 Hwy 62 - she thinks the neighbors disagreed on doing a short term rental there and because its a shared well & driveway they couldn't make it work. Joe is the planner who will confirm and can give me full details of that.
- #j595/journal 
	- Discussed NotificationsLM proposal with Luke Selina Martin Victor - I made my case pretty clearly. Selina suggests we wait till Vera greenlights all feature development and kick off meetings with HI.
	- [GitHub - mem0ai/mem0: The Memory layer for AI Agents](https://github.com/mem0ai/mem0?tab=readme-ov-file)  - Mem0 potentially relevant for [[memories-fc]]

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-03-12 00:00 %%
%% TCT_TEMPLATED_END 2025-03-12 23:59 %%



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
