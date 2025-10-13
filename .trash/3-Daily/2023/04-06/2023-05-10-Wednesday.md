---
aliases: [2023-05-10]
tags: 
---

---
# TOP-OF-MIND
Checked out Shinjuku and Shibuya neighborhood.

Had a heavy traditional Japanese breakfast at the resting across the hotel. Walked to government office building observatory. Tried a standing sushi bar for the first time, amazing sushi! Went into a beautiful tea house in the shinjuku park where I tried a matcha red bean paste mochi for the first time. Came back to rest up in the hotel for a bit before heading to Shibuya. Checked out the famous Meiji shrine then walked from that neighborhood to Shibuya crossing. Was trying to get into this sushi no Midori at Shibuya station but it was packed. Ended up getting very ok yakitori at a neighborhood restaurant. In the way back tried our luck at the sushi place and were able to get in. The sushi unfortunately wasn’t as good as we expected it to be. Headed back to Shinjuku and ended up in an unsuccessful attempt to find toasteees. Finally settled for some cake at Smokist coffee house next to hotel. 

—-

From Sana:

Had coffee across the intersection at Smokist Coffee with sweet butter bun and soft white chocolate croissant. 

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
