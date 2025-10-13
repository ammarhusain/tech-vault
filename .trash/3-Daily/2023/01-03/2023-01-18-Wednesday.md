---
aliases: [2023-01-18]
created: 2023-01-18-Wednesday 16:42
modified: 2023-03-10-Friday 23:15
tags: 
---

---

# Top-of-mind
- Went for a swim in the morning which felt great. Then read through a couple papers (GLUE & Interactive language) at work. Singing lesson in the afternoon which is fun but breaks the flow of my workday.
- Gelt:
	- tax tool "platform", strategy & analysis looking through previous year tax returns.
	- have dedicated cpa assigned; annual fee not billed per hours; proactively engage with tax optimization suggestions
	- most cpas usually come handy during tax seasoned platform is like personal capital/ mint integrated with all transactions
	- overall this girl didnt really know too much other than kept saying we have a"platform" for everything
- Jai Ho; tried chilling at Center SF but it was packed so drove over to Voras to drop off box and chill at homes
- Started reading Making of Prince of Persia journal entries

---

## Tasks
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has start date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (starts on ` + date + `)`
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
