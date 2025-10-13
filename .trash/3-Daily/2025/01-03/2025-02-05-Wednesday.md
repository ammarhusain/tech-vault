---
alias: ["Wednesday, Feb 5, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Sana got 3 of her wisdom teeth removed at DIOS center - Dr Francis Chung
	- Hung out at Grand coffee nearby for an hour waiting for her procedure to get some
- #j595/journal 
	- Wrote some visualization code to plot timestamp deltas in bubbles response events
		- [RoadshowBubblesDiagnostics/blob/main/latency_visualizer.ipynb](https://github.pie.apple.com/heavenly/RoadshowBubblesDiagnostics/blob/main/latency_visualizer.ipynb)
		- ![[2025-02-05-Wednesday-2025-02-05.png]]
		- ![[2025-02-05-Wednesday-2025-02-05-1.png]]
		- ![[2025-02-05-Wednesday-2025-02-05-2.png]]

# 
TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-02-05 00:00 %%
%% TCT_TEMPLATED_END 2025-02-05 23:59 %%



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
