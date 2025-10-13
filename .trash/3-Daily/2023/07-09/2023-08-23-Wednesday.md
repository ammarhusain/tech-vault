---
aliases: [2023-08-23]
tags: 
---

---

**[DayOne](dayone://open?date=2023-08-23)**

# TOP-OF-MIND
- Spent most of the day doing house work
- Went to [[home#117 Topaz Way, Sf, Ca - 94131]] in the morning. Got Stas Russian painter guy for estimate. Chilled at Neighbors for a bit and then met with Jose to discuss a bunch of little details about the kitchen - where to put the shelves etc
- Home for a couple of [[j595 journal]] meetings
- Left again to check out doors at Caldwell. Went home to discuss kitchen countertop.
- Messaged Dan about the partition - he was being very fussy and behaving like a kid.
- Met up with Quinn & Kay - showed them around the work we're getting done. Dumped a few electronics over at theirs.
- Bikram Yoga in the evenings. I came out feeling very feverish.
- 

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
