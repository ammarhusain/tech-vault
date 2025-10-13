---
alias: ["Wednesday, Mar 5, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Met [Ben Handel \| UC Berkeley Economics](https://econ.berkeley.edu/profile/ben-handel) at Neighbors Coffee - chatted with him about the Oliver Burkeman book
- #j595/journal 
	- Did analysis for extracting server errors from logs: rdar://146066202 (22W4074: Baking Experiment: Multiuser: "Pellegrino" was added to the list but casper did not utter verbiage around its addition), [saari slack](https://a1350286.slack.com/archives/D05PX8MQMRV/p1741197678284999)
	- 

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-03-05 00:00 %%
%% TCT_TEMPLATED_END 2025-03-05 23:59 %%



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
