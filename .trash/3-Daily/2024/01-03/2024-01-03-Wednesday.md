---
aliases: [2024-01-03]
tags: 
---
**[DayOne](dayone://open?date=2024-01-03)**

# TOP-OF-MIND

- #j595/journal 
	- Attention meeting with Jakub and Marisa [[attentionkit-fc]]
	- ====Got Xins model working on J310====:
		- [Slack thread](https://a1391192.slack.com/archives/C04VBGWNT52/p1704331370785519) with results:  
		- ![[2024-01-03-Wednesday-2024-01-03.png]]
		- Caveats: Had to download the model in the Caches directory on tvOS - instead of Documents; UI all messed up; for some reason the Comet download link only downloads 745M of the model rather than the full 746M so I had to manually scp it in from my machine by trying to find where it lives on device: `dvdo find /var/mobile/Containers/Data/Application/. -name "*gguf"`

# NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

# NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
