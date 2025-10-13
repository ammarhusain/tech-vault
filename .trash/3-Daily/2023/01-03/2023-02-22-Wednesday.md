---
aliases: [2023-02-22]
created: 2023-03-08-Wednesday 21:57
modified: 2023-03-10-Friday 23:15
tags: 
---

---
# Top-of-mind
- Chat with Stafford at Google Geo 3D [[career/career]]
	Humility & wanting to learn; Have some of the best 3d engs; Need someone who doesn’t think they know it all; Hunger for 3d
	How do you collaborate & inspire the team; Collaborate with other teams on roadmaps
	Mostly partnering with other orgs within geo; Focussed on making 3d models
	Some impact cycles are longer 2-3 years
	City scale 3d models & meshes, some manual edits; Need to create atomic objects
	Point clouds are stereoscopic for lidar; Street view have lidar
	3 customers:
	1. Route preview for navigation
	2. Developer API for tiles (unreal tiles)
	3. GeoAI - analysis capabilities, provide semantically segmented datasets
	Have some core tech but that has been mostly unchanged for 10-15 years. Room for growth & experimentation
	Excited of digitizing the planet; have taken extended scope and working on getting better at delegation

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
