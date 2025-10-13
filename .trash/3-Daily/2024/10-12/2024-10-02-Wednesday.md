---
alias: ["Wednesday, Oct 2, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595 
	- Architecture review in the morning. Frustrating that Paul S & Hans do not include me for Attention
	- Met with memories working group to discuss FC4 use cases

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-10-02 00:00 %%
%% TCT_TEMPLATED_END 2024-10-02 23:59 %%


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
