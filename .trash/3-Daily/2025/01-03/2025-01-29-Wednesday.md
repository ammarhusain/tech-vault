---
alias: ["Wednesday, Jan 29, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- 
- #j595/journal 
	- Been working closely with Marios & Teddy over the last couple of weeks - could add them as reviewer for feedback in #j595/perf 
	- Command to get rsync and dashboard DB update working every 5 mins:
		- `watch -n 600 'rsync -cavz --dry-run local@superserver.corp.apple.com:/Users/local/deploy/staging/openai-realtime-console/logs/. /Users/local/roadshow/superserver-logs/logs/. && python transcript_db.py --logs-dir /Users/local/roadshow/superserver-logs/logs/.'`


# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-01-29 00:00 %%
%% TCT_TEMPLATED_END 2025-01-29 23:59 %%



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
