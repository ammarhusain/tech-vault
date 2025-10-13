---
alias: ["Wednesday, Nov 27, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595/journal 
	- [Release v0.28.0 · roboflow/inference · GitHub](https://github.com/roboflow/inference/releases/tag/v0.28.0) - interesting for some of the fitness usecases. Uses posture tracking and feeds into GPT4o for form correction
- #journal/daily 
	- Crossfit at 10am for a pretty decent deadlift focused workout
	- Showered and head over to Fremont to help Saman-Mehlam move #social 
	- We forgot to charge the car so had to stop over at an Electrify America for a topup - its such a pain given the lines at these stations usually. 
	- Drive to Mountain House was painful with crazy traffic along the way.
	- Briefly hung out there, checked out the place and drove back to SF with a pit stop to pick up some halal chicken. Drive back was not too bad - 1hr20mins

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-11-27 00:00 %%
%% TCT_TEMPLATED_END 2024-11-27 23:59 %%


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
