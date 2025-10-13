---
aliases: [2024-03-13]
tags: 
---
**[DayOne](dayone://open?date=2024-03-13)**

# TOP-OF-MIND
- #j595/journal 
	- Coffee with HP
	- The llama project in llama.cpp can be run as is within a swift workspace to get a model functioning on device. Worth an experiment with a phi model to see if finetuning it makes sense in general.
	- Got started building a LlamaCpp framework library that can be linked with AttentionKit

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
