---
alias: ["Wednesday, Dec 4, 2024"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- bags took over an hour to become a Nagpur airport
	- got home around 4 AM. Tried to sleep for a few hours felt groggy and sleepy through the day.
	-  Went to the gym for a bit in the evening felt good.

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-12-04 00:00 %%
%% TCT_TEMPLATED_END 2024-12-04 23:59 %%


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
