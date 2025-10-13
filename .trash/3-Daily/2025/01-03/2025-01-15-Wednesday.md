---
alias: ["Wednesday, Jan 15, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- 
- #j595/journal 
	- Got assigned rdar://141230692 (Audio is missing at the end of Casper utterances) - roadshow blocker
		- Was able to reproduce it using the openai-realtime-console (last commit before they moved it to WebRTC)
		- Known issue with OpenAI api - [\[Realtime API\] Audio is randomly cutting off at the end - API / Bugs - OpenAI Developer Forum](https://community.openai.com/t/realtime-api-audio-is-randomly-cutting-off-at-the-end/980587/71)

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-01-15 00:00 %%
%% TCT_TEMPLATED_END 2025-01-15 23:59 %%



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
