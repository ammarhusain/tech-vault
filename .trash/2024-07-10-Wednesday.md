---
alias: ["Wednesday, Jul 10, 2024"]
tags: 
---


# TOP-OF-MIND
- [x] foo bag [link](https://todoist.com/app/task/8193890921) #todoist %%[todoist_id:: 8193890921]%%
- [x] try this now [link](https://todoist.com/app/task/8193924502) #todoist %%[todoist_id:: 8193924502]%% 
- [x] do this again [link](https://todoist.com/app/task/8193931349) #todoist %%[todoist_id:: 8193931349]%% 
[Todoist](todoist://task/8193890921)
[Task 8193890921](todoist://task/?id=8193890921)

- [x] foo bat man [link](https://todoist.com/app/task/8193948413) #todoist %%[todoist_id:: 8193948413]%%
- [x] tststst [link](todoist://task?id=8193971729) #todoist %%[todoist_id:: 8193971729]%%
- [x] tst again [link](todoist://task?id=8193993315) [link](todoist://task?id=8193993600) [link](todoist://task?id=8193993679) [link](todoist://task?id=8193993758) [link](todoist://task?id=8193993812) [link](todoist://task?id=8193993837) [link](todoist://task?id=8193993872) [link](todoist://task?id=8193993947) [link](todoist://task?id=8193994018) [link](todoist://task?id=8193994086) [link](todoist://task?id=8193994164) [link](todoist://task?id=8193994281) [link](todoist://task?id=8193994388) [link](todoist://task?id=8193994468) [link](todoist://task?id=8193994572) [link](todoist://task?id=8193994616) [link](todoist://task?id=8194294362) #todoist                  %%[todoist_id:: 8194294362]%%
- [x] no id i mean [link](todoist://task?id=8194018836) [link](todoist://task?id=8194294465) #todoist  %%[todoist_id:: 8194294465]%%
- [ ] 
#### TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-07-10 00:00 %%
%% TCT_TEMPLATED_END 2024-07-10 23:59 %%

#### NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

#### NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
