---
alias: ["Wednesday, Jun 11, 2025"]
tags: 
---
##### TOP-OF-MIND
- #journal/daily 
	- Dropped Huzefa-Alifya family to SFO
	- Dinner at Stonestown with Adil-Maleehe [[social life]]
- #j595/journal 
	- [[memories-fc]]
		- Got the judges working well. Tried with Sri's barge in fix PR which makes the judge work pretty well overall

##### TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-06-11 00:00 %%
%% TCT_TEMPLATED_END 2025-06-11 23:59 %%



##### NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

##### NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
