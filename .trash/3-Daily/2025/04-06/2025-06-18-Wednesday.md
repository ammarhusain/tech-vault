---
alias: ["Wednesday, Jun 18, 2025"]
tags: 
---
##### TOP-OF-MIND
- #journal/daily 
	- Cruise total that Huzefa owes me came out to 4840 +375 + 750 + 815 = 6780 (we should be all squared up since he transfered 7k already)
- #j595/journal 
	- Caught up with some papers & articles
	- Trying to get the behavior tree engine refactored to scale up from

##### TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-06-18 00:00 %%
%% TCT_TEMPLATED_END 2025-06-18 23:59 %%



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
