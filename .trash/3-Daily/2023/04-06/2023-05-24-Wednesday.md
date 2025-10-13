---
aliases: [2023-05-24]
tags: 
---

---
# TOP-OF-MIND
- Spoke with Boston Dynamics recuiter (James?); call with Yang for interview prep
- Started migrating second brain search over to use StreamLit. It turned out to be quite straightforward porint the code over. The framework is surprisingly simple to use. I would say took 2-3 hours of focussed work to finish it up . [[second-brain-web-search]]
- Went over to Joe n the Juice on Montgomery after lunch (walked to Glen Park BART from home ~20ish mins). Continued StreamLit migration. Then went over to meet Ashish at 345 Spear. Took Muni to Verve after waiting for Sana to pick me up
- Queried ChatGPT for PointNet and ShapeMask
	- PointNet simply takes in an unordered set of vectors - so Nx3 for the xyz point coordinates. It is able to operate the neural network on top of those.
	- Pointnet (vanilla) has 0.8 parameters while full net has 3.5M parameters - pretty doable on robot
	- ShapeMask has anywhere from 0.02M to 1.44M parameters while Mask R-CNN has 2.64M so much fewer than that.
- Productive chat with Jose G about contract. Seems like he is willing & ready to execute. Goal is to unblock him with parts & decisions asap.
- Went over to Pranays to hang out - farewell as he moves to NY; ate butter chicken and brought back his standing desk.

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
