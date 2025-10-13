---
alias: ["Wednesday, Dec 11, 2024"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Alifiya's Nana funeral in the morning got done by 1 PM and then went for Danyal's concert
	- went to the office for a little bit.

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-12-11 00:00 %%
%% TCT_TEMPLATED_END 2024-12-11 23:59 %%


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
