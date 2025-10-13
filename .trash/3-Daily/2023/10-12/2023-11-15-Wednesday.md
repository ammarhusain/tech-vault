---
aliases: [2023-11-15]
tags: 
---
**[DayOne](dayone://open?date=2023-11-15)**

# TOP-OF-MIND
- #j595/journal 
	- [Arithmetic Coding - mathematicalmonk](https://www.youtube.com/watch?v=ouYV3rBtrTI)
		- Current sota in lossless compression
		- ![[2023-11-14-Tuesday-2023-11-15.png]]

- #journal/daily 
	- Dropped Sana to the airport at 2.30am. Came back and passed out.
	- Long nap in the afternoon.
	- Went to Premals for Diwali in the evening.
	- Watched the WC semi finals India-NZ match there and through the evening.

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
