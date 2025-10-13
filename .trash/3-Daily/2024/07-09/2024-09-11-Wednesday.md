---
alias: ["Wednesday, Sep 11, 2024"]
tags: 
---

# TOP-OF-MIND
- #j595/journal 
	- Setup Beyond Compare diff tool for git to easily create PRs
	- Tested ConversationReference intrinsic and renamed everything accordingly - readied for [PR](https://github.pie.apple.com/heavenly/AttentionKit/pull/103)
	- Tried getting the TestApp behavior to play animation when no entities are tracked
	- Chatted with Paul & Anton to possibly work on Perception [Memories in FC4](https://quip-apple.com/Bu3BALxbM0D3)

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-09-11 00:00 %%
%% TCT_TEMPLATED_END 2024-09-11 23:59 %%


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
