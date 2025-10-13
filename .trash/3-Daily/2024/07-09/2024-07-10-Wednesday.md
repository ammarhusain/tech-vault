---
alias: ["Wednesday, Jul 10, 2024"]
tags: 
---


# TOP-OF-MIND
- #j595/journal 
	- evaluated the 3 finetuned models trained yesterday
	- obsidian workflow: integrated google photos, todoist link for tasks
- #journal/daily
	- purchased webflow template for [[Crawlspace]]
	- finding it hard to get in the zone

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-07-10 00:00 %%
* Inbox
    - [x] move all only #j595 tags in Daily to #j595/journal 
    - [x] modify todoist uri in ultimate todoist sync to use the todoist app instead of https 

%% TCT_TEMPLATED_END 2024-07-10 23:59 %%


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
