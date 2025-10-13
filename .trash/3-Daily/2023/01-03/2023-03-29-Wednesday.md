---
aliases: [2023-03-29]
created: 2023-03-29-Wednesday 09:57
modified: 2023-03-29-Wednesday 10:10
tags: 
---

---
# Top-of-mind

====- Migrated the hosted notes to my custom domain at notes.ammarh.io ====
	Followed this [guide](https://help.obsidian.md/Obsidian+Publish/Set+up+a+custom+domain)
- Moved to 117 Topaz way - supposed to start at 2 but movers came at 7pm. Extremely chaotic move. Was super exhausted after.

---
# Tasks
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
# Vault Updates
## Notes Created in the Last Week
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) AND file.ctime < date(substring(this.file.name,0,10))
SORT file.mtime ASCENDING
```

## Notes Modified in the Last Week
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
