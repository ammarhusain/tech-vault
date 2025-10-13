---
aliases: [2024-02-07]
tags: 
---
**[DayOne](dayone://open?date=2024-02-07)**

# TOP-OF-MIND
- #j595/journal 
	- Got Comet SAML SSO working (almost)
		- Turns out that the certificate in the vendor pdf was incorrect (fucking apple)
	- Can't get on device tool to query my mac studio LLM endpoint - even Andreas does not know what might be going on. Some weird networking issue
	- Redoing the streamlit appprompt with motif summarized emitted summaries

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
