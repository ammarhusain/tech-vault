---
aliases: [2024-01-24]
tags: 
---
**[DayOne](dayone://open?date=2024-01-24)**

# TOP-OF-MIND
- #j595/journal 
	- Was trying to write a simple tool that subscribes to TrackerState messages and prints them on screen
	- Struggled to get it to work. Turns out the TrackerBridge in AttentionKit that I was using as a template does not work either. I should really make sure that the thing I am copying from works in the first place since the tech stack here is very janky - #j595/meditation 
	- Seeked help from Jakub & Paul and both weren't able to figure out either - Jakub sent me a patch but that patch does not work.

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
