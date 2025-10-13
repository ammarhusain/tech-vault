---
aliases: [2024-01-17]
tags: 
---
**[DayOne](dayone://open?date=2024-01-17)**

# TOP-OF-MIND
- #j595/journal 
	- Got Everest working with device - Peopleawarenessd signals getting detected now
		- I had just gotten stuck between some bad build version of SapphirePalazzo and the Xcode SDK - just needed to update
	- Prepared slides for literature review with [[*shiny-fm-llm#LLMLingua]] papers: [[J595 Literature Review - LLMLingua.key]]
	- Spent an hour trying to get Comet SAML SSO working - its been cumbersome & painful.
	- 

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
