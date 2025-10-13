---
alias: ["Wednesday, Jul 24, 2024"]
tags: 
---


# TOP-OF-MIND
- #j595/journal 
	- Worked with Josh to understand how the behavior works in the AttentionTestApp. He helped me implement a behavior that plays an animation when the number of entities goes down to zero.
		- Met with Hans about it but was useful
	- Chatted with Stephan about my "gazing" feature request for Everest
- #journal/daily 
	- Woke up a bit groggy this morning - mostly due to a sense of overwhelm perhaps
	- Chatted with the fam for a while as mom & dad were about to fly out here
	- Spent a bunch of time in Webflow get the website done for #crawlspace - made good progress, just formatting left to do now. Felt productive and got some closure after the overwhelm over the last several days

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-07-24 00:00 %%
%% TCT_TEMPLATED_END 2024-07-24 23:59 %%


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
