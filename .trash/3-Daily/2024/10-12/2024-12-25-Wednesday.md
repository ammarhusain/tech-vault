---
alias: ["Wednesday, Dec 25, 2024"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Left wrapped gifts out for everyone for Christmas - slept quite late since we went out on a drive with Huzefa-Alifiya to Reshambag area.
	- Woke up groggy at 7am because of moms time anxiety 
	- Breakfast at Corridor Seven
	- Went home, packed for a bit and tried to nap - woke up in the afternoon because Sana's dad came over
	- Amazing massage at CP club - chilled and got cofffee with dad & Sana at the cafe outside after. Khurdi-khichdi for dinner
	- Reached the airport pretty early ~12.45am. Horrible experience at Nagpur airport while checking into Qatar flight back to SFO


# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-12-25 00:00 %%
%% TCT_TEMPLATED_END 2024-12-25 23:59 %%



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
