---
alias: ["Wednesday, May 28, 2025"]
tags: 
---
##### TOP-OF-MIND
- #journal/daily 
	- Co-incidentally we saw the cruiseship pull up outside the window lol.
	- We got breakfast at Purebread - picked up a couple things from London drugs. Showered and packed up to leave.
	- We walked over to the cruise terminal. We stopped at dollorama and tim hortons on the way. I got an Iced-cap but found it incredibly sweet since stopping sugar so couldn't drink it.
	- We boarded the cruise ship and got lunch at the buffet on deck 14.
	- We checked into our rooms and went to deck 14 for the sail away party.
	- Then we went to the hot tub for a bit.
	- Showered and got dinner at the bordeaux dining room - turned out we had the same table every night for the week with our servers Dinesh and Ramil.
	- We turned in soon after.

##### TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-05-28 00:00 %%
%% TCT_TEMPLATED_END 2025-05-28 23:59 %%



##### NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

##### NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
