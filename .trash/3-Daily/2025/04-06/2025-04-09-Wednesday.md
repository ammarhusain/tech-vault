---
alias: ["Wednesday, Apr 9, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- 
- #j595/journal 
	- #travel/egypt 
		- Wifi on Turkish airlines sucked - reached Cairo around 10.30pm and by 11.30pm we were already in our room in Le Meridien - super convenient location by just walking across the bridge in T3

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-04-09 00:00 %%
%% TCT_TEMPLATED_END 2025-04-09 23:59 %%



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
