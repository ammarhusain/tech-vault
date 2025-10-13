---
aliases: [2023-01-25]
created: 2023-01-25-Wednesday 19:07
modified: 2023-03-10-Friday 23:15
tags: 
---

---

# Top-of-mind
- Another of those not so productive of days. I went to the SFO office then got massive FOMO so took a Lyft down to RLS and then just hung out there. I have this stress that I need to get a lot of tasks done before I lose Google access but dont feel like doing any or making those decisions
- Only real thing I got done that I have been thinking for a while was to create a self@ammarh.io account
- I really need to get back to clearing out my todo & reading / learning lists

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
