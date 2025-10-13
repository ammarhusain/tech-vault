---
alias: ["Wednesday, Mar 26, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Melissa shared this [Feelings Wheel](https://feelingswheel.com/) to identify emotions
- #j595/journal 

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-03-26 00:00 %%
%% TCT_TEMPLATED_END 2025-03-26 23:59 %%



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
