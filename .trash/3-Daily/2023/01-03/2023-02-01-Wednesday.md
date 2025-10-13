---
aliases: [2023-02-01]
created: 2023-02-02-Thursday 10:47
modified: 2023-03-10-Friday 23:15
tags: 
---

---

# Top-of-mind
- This carbuncle boil is really bothering me. Not being able to work out is frustrating
- We went and saw 117 Topaz way today. Pretty excited about it. Though it will need a full interior refresh.
- Spoke with Stephan about it & other stuff. Also msged Vora about his remodel experience.
- Lets see hopefully we are able to get it at a reasonable price

---

## Tasks
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```

## Vault Updates

**Notes created in the last week:**

``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) AND file.ctime < date(substring(this.file.name,0,10))
SORT file.mtime ASCENDING
```

**Notes modified in the last week:**

``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
