---
aliases:
  - 2023-10-18
tags: []
---

---

**[DayOne](dayone://open?date=2023-10-18)**

# TOP-OF-MIND
- #j595/journal 
	- Chat with Yi about W&B:
		- Yi recommends having our own W&B instance because network configuration is very complicated.
		- W&B says that they can help bring up instance - but they dont really do that
		- Yi willing to help - it wont take too much effort. W&B can help support in the long run
		- We would need more licenses for ISPG. Can link me to EPM eho helped negotiate licenses. 
		- Enterprise plans come with several options - # seats or unlimited. $3k for AWS, kubernetes accounts
		- Can help bring w&b run locally 
		- [x] #j595/todo Get Yi disclosed on J595, get him access to SC01 ✅ 2023-10-31
		- [x] #j595/todo Work with Yi Qin to get W&B hosted locally on one of the mac studios ✅ 2023-10-31
		- [x] #j595/todo Setup Jakubs Linux box in the office ✅ 2023-11-01
	- Meeting with Humphrey, Jakub, Victor, Anton on AttentionKit - lot of interesting IL/RL work there on designing attention policies
	- Setup second-brain with git lfs - good step that I have been meaning to explore for a while. Limit now is 2GB per file though.
	- [x] #j595/todo Reading through [[State of AI Report 2023 - ONLINE.pdf]] - interesting report on [[ai-ml|aiml]] ✅ 2023-10-20

---
# TASKS
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
# VAULT UPDATES
## NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) AND file.ctime < date(substring(this.file.name,0,10))
SORT file.mtime ASCENDING
```

## NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
