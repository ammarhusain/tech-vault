---
alias: ["Wednesday, Jan 1, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Beautiful New Year's Day in. Chilled in the cabin as it was snowing like crazy outside.
	- Met Stephan the Airbnb host when we asked them for a shovel chatted with him for a while about owning an Airbnb near crater Lake while shoveling snow
- #j595/journal 
	- 

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-01-01 00:00 %%
%% TCT_TEMPLATED_END 2025-01-01 23:59 %%



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
