---
aliases: [2023-01-11]
created: 2023-01-11-Wednesday 12:15
modified: 2023-03-10-Friday 23:15
tags: 
---


---

# Top-of-mind
- Spent the day at the SF office reading through papers related to robotics task benchmarking Spent the morning tweaking and tuning Obsidian. Creates [[vault management]] to store snippets of various query code. Installed Various Complements plugin
- Singing lesson today was fun as always. Got to work on modulating pitch and beat.

# Tasks
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has start date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (starts on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```

## Quote
> It is never too late to be what you might have been.
> — <cite>George Eliot</cite>

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
