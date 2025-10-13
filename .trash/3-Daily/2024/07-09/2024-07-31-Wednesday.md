---
alias: ["Wednesday, Jul 31, 2024"]
tags: 
---


# TOP-OF-MIND
-  #j595/journal 
	- Not much done workwise
	- Booked parents tickets to Vegas & LA
	- Booked my tickets to London
	- Tried to get the callbacks written for a periodic 1Hz and sample audio transcripts with it
		- Could not test because AttentionTestApp started failing due to Protobuf versioning issues in the new SDK :(

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-07-31 00:00 %%
%% TCT_TEMPLATED_END 2024-07-31 23:59 %%


#### PHOTOS
```photos
notedate
```

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
