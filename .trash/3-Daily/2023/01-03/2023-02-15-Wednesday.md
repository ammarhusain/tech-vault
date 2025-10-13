---
aliases: [2023-02-15]
created: 2023-02-15-Wednesday 14:04
modified: 2023-03-10-Friday 23:15
tags: 
---

---

# Top-of-mind
- Barrys in the morning + smoothie + drive to Mt View
- Opened Citi checking & wealth accounts over the phone
- Call with Kristi at Geo:
	- You mentioned inflection points in 3D - what are they?
		- hardware & 3d reconstruction on device
		- proliferation of lidar & other data
		- metaverse of the real, build a digital twin of the world
		- increasing user expectations from AR & VR
		- mix of both applied research & user - not the org that directly faces users. Google maps does a lot of the user research.
		- visual positioning service
		- seemed a safe & interesting bet if I wanna stay a PM
	- Drinks with Ana Mirtabtabei in the evening.

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
