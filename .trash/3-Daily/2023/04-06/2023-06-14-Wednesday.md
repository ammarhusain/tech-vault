---
aliases: [2023-06-14]
tags: 
---

---
# TOP-OF-MIND
- Morning dives today- went to the northsude of the island so a long boat ride. Thankfully I popped a dramamime since I felt quite sick on Monday during the surface interval. Dramamime really helped and felt more in control.
- Divemaster was Melanie - saw a turtle which was spectacular.
- Got back to Trudys around 12.45pm. Chilled & logged dives, cleaned up and took a nap
- Had a late lunch at Trudys (delicious fish & chips).
- Hung out at the hostel. Went for a swim in the water during sunset.
- Chilled on the hammocks reacding. Ate chicken fingers and fries before hitting the bed.

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
