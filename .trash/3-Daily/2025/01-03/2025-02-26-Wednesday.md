---
alias: ["Wednesday, Feb 26, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Went home early and worked on [[karpathy#[Deep Dive into LLMs like ChatGPT - YouTube](https //www.youtube.com/watch?v=7xTGNNLPyMI)|Deep Dive into LLMs like ChatGPT]]

- #j595/journal 
	- #j595/perf Bubbles latency work acknowledged in the Eng Sync this morning
		- [Created latency plots from demo run](https://a1350286.slack.com/archives/C07T7PQJJMP/p1740607246009279?thread_ts=1740596823.871299&cid=C07T7PQJJMP)
		- Added new feature to stitch audio together on BRAD dashboard - [slack](https://a1350286.slack.com/archives/C07RYK1B13R/p1740612404485759)
			- ![[2025-02-26-Wednesday-2025-02-26.png]]

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-02-26 00:00 %%
%% TCT_TEMPLATED_END 2025-02-26 23:59 %%



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
