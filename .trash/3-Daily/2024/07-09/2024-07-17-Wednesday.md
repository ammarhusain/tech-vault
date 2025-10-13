---
alias: ["Wednesday, Jul 17, 2024"]
tags: 
---


# TOP-OF-MIND
- #j595/journal 
	- Morning of meetings: Tanya Arana for [[taxes]], perception sync, j595 eng sync, chat with manuel
		- saari seems interested in the finetuned model - wants me to profile mem usage for on device
	- refactored the streamlit eval & data collection ui to make it more stable for the team to contribute
		- streamlit seems to rerun execution flow of the script everytime some state in the app changes. need to be more thoughtful in the app ui design next time around and make more use of the session_state variables
- #journal/daily 
	- Crossfit after a long break - back squats and thrusters which felt good.
	- Helped alifiya get access to her robinhood account and sold all the holdings
		- #journal/meditations I should not be arrogant, stubborn in managing people's money. Do the safe investment rather than risky lottery ticket bets

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-07-17 00:00 %%
* Inbox
    - [x] send link to streamlit ui for quick data capturing 
    - [x] file radar for manuel that the worldstatecollator is not returning with a prompt 
* J595
    - [x] track down how conversational context is set from the attention llm output 
%% TCT_TEMPLATED_END 2024-07-17 23:59 %%


#### PHOTOS
```photos
notedate
```

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
