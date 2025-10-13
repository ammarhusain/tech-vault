---
aliases: [2023-11-29]
tags: 
---
**[DayOne](dayone://open?date=2023-11-29)**

# TOP-OF-MIND
- #j595/journal 
	- Chatted with Humphrey about generic object tracking (per Martins request)
		- They are assuming a function call that has the entity of interest provided. Use VI-SAM model under the hood developed by the Beijing team.
		- Mostly plumbing work that they need to do to put it under Motif
		- I mentioned that there probably needs to be an intermediate LLM stage that extracts the entity of interest - maybe thats part of Xins planner or a separate small model
	- CometML office hours meeting - met their CEO. Still blocked on them to resolve some stability issues.
	- Mark Pauley showed me a cool tool `nsd` to get the latest macOS build

# TASKS
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date) OR (has created date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `) OR (created on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
# CROSS-REFERENCED 
```dataviewjs
// Loop through pages 
for (let p of dv.pages()) {
	for (let ol of p.file.outlinks) {
		// find all the cross references of this file
		if (dv.current().file.path == ol.path) {
			// get all the lists in this file
			for (let ls of p.file.lists) {
				if (ls.text.includes(dv.current().file.name)) {
					dv.header(3, p.file.link + "  ...  " + ls.line)
					dv.paragraph(ls.text)
					dv.paragraph("---")
				}
			}
		}
	}
}
```

# VAULT UPDATES
## NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

## NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
