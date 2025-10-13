---
aliases: [2024-01-31]
tags: 
---
**[DayOne](dayone://open?date=2024-01-31)**

# TOP-OF-MIND
- #j595/journal 
	- Check Turi cofigs - giving Blanca access
	- Updated Comet license token - valid till [[2024-02-29-Thursday]]
	- Hans helped me out with CIKit code to track one or more entities using their name or UUIDs
	- [[attentionkit-fc]] - struggling to set a demo with Everest
	- Added passwordless ssh access to my mac studio
	- setup uuid persona names with suncore - sunctl insertPersona identifier=1234 firstName=joe lastName=shmoe

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
