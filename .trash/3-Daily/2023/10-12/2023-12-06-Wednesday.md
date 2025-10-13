---
aliases: [2023-12-06]
tags: 
---
**[DayOne](dayone://open?date=2023-12-06)**

# TOP-OF-MIND
- #j595/journal 
	- Demo'ed comet to the llm working group. They liked it
	- Code to run palazzo-llm-ws locally : `python client/ws_client.py --host localhost --port 8000 --prompt 'Tell me a story about when jack and jill go up the hill' --temp 0.5 --backend llama.cpp --top-p 0.5 --n_predict 100 --interactive`
	- Code to run palazzo-llm-ws on superserver: 
	- `python client/ws_client.py --host superserver.corp.apple.com --port 1337 --prompt 'how many planets are there' --temp 0.5 --backend llama.cpp --top-p 0.5`

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
