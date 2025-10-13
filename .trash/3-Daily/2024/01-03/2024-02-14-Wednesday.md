---
aliases: [2024-02-14]
tags: 
---
**[DayOne](dayone://open?date=2024-02-14)**

# TOP-OF-MIND
- #j595/journal 
	- Create Prod app for Comet SAML SSO
	- Walked Reza through streamlit app to help out on [[attentionkit-fc]]. Some ideas
		- Experiment with entity ranking
		- Numeric vs bucketized scores for inputs and outputs
	- Learned how to create and deploy root from Sylvain - tested with a simple AttentionLLM root
	- Started working on setting up sigmon publisher channel

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
