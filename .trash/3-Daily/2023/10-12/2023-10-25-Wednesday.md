---
aliases: [2023-10-25]
tags: 
---

---

**[DayOne](dayone://open?date=2023-10-25)**

# TOP-OF-MIND
- #journal/daily
	- Had breakfast at Mango Inn - this also took forever. I left to pack up in between to get to class at 9am. Quickly ate and bounded 
	- Rescue Diver course started this morning. Watched another video with an attached knowledge review that we had to complete while watching it. It was more or less obvious stuff. Went through all the answers with Georgi after. 
	- Had a break for lunch. Went by myself to La Casita for lunch and had the tortilla chicken soup. Was very good in the pouring rain but took >30 mins to come.
	- Gave the final exam and wrapped up 3.30pm ish for the day.
	- Bumped into Tamara at Mango who mentioned that she is making plans for dinner at Pelican thai resturant because they have some ongoing specials on wednesdays. Took a tuktuk over - had the panang curry & drunked chicken noodles. Food was good - ran out of cash though so had to borrow 700LMP from Tobi
	- On the walk to Mango withdrew some money.

---
# TASKS
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
# CROSS-REFERENCED 
```dataviewjs
// Loop through pages 
for (let p of dv.pages('"vault-management"')) {
	for (let ol of p.file.outlinks) {
		// find all the cross references of this file
		if (dv.current().file.path == ol.path) {
			// get all the lists in this file
			for (let ls of p.file.lists) {
				if (ls.text.includes(dv.current().file.name)) {
					dv.header(3, p.file.link)
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
