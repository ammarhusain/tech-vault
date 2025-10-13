---
aliases: [2023-05-17]
tags: 
---

---
# TOP-OF-MIND
-     

Went down to get coffee in the hotel lobby and check emails. Spoke to Kevin from Apple for a bit. Walked over to higashi hoganji temple near the hotel. There seemed to be a bit of construction going on so we didn’t really go in much. Walked back to hotel, got dressed and head over to catch  the train to Nara. I left a bit early to find breakfast. Found a really really good bakery in Porta B1F floor. Their breads were delicious which we picked to carry with us on the train. Took the bus to Nara park once we reached. There were friendly and hungry deer everywhere. Fed a few packs of crackers to them before we head into Todaijee temple. The Buddha statue inside was huuuuge indeed. Walked around to one of the stupas on the right of the temple. Stopped to get some tea and juice at a small little cafe. Walked around to another little temple in there and then walked by out to get some soba right outside the temple. It turned out to be really good. We then walked to isuien garden which had closed by the time we arrived so we went to the neighboring yoshikien garden.garden was great but couldn’t find a tea house in there unfortunately. Walked out and head over to check out kofukuji temple also in Nara park.  It was closed but also beautiful. There were school kids everywhere in Nara and we kept getting stuck in lines behind them. We fed several more packs of crackers to the deer and then took the bus back to the station. The rapid train was like 45 mins later so we got a pancake at Mos and coffee. Then picked up a bunch of snacks and Starbucks lattes at 7-11. 7-11 are popping in Japan. There was an Italian woman who didn’t shut up for the entire train ride, it seemed like her companions also were tired of her yammering away. Once we reached back to the hotel both of ended up in the bath for an hour.  It was hard but we dragged ourselves out to dinner. We were searching for Yakiniku but ended up getting some Xiao Long baos at a place across the hotel. The chef was nice,  gave us some stickers and waved long good byes as we left. Back to hotel and passed out. 

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
