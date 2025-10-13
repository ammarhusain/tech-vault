---
aliases: [2024-01-10]
tags: 
---
**[DayOne](dayone://open?date=2024-01-10)**

# TOP-OF-MIND
- #j595/journal 
	- [[attentionkit-fc]] meeting with Jakub & Marisa
		- Marisa excited about using it with speech
		- We might not have provenance - who said what. Or even isolate speech coming from one person.
		- Overall she wants to get it soon. Need her to define granularity of Motif signals to use
	- Minor tweaks on getting attention streamlit app
	- Spent a large chunk of the day listening in on system design meetings


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
