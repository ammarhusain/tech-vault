---
alias: ["Wednesday, Dec 18, 2024"]
tags: 
---
# TOP-OF-MIND
-  #journal/daily 
	- went to corridor seven to get a couple of hours of work in the morning while mom had gone to the jewelers.
	- went to the hospital late afternoon around 3 PM to get Huzefa discharged took a few hours in the entire process. We got back around 8 PM.

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-12-18 00:00 %%
%% TCT_TEMPLATED_END 2024-12-18 23:59 %%


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
