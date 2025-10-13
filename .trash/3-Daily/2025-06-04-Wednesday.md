---
alias: ["Wednesday, Jun 4, 2025"]
tags: 
---
##### TOP-OF-MIND
- #journal/daily 
	- Woke up, showered and packed up.
	- Got breakfast at Bordeaux
	- It was pouring outside - we walked out to the cruise terminal - Alifiya and I waited while Ammar and bhai got the rented car.
	- It was a small sedan but we managed to all squeeze in with the luggage.
	- We were blocked by the open times of the tunnel out of Whittier - it was only open for 15 min every hour - and we had 40 min to go so we waited at a cafe.
	- Finally drove out - we stopped by portage glacier visitor center but the weather was horrible and the palce was closed.
	- We drove to the airport - Ammar and I checked in the bags and we went to the 5th ave mall to pick up bhai's laptop from the apple store
	- The guy at the apple store recommended Moose's Tooth pizza place for lunch - we drove over and it was packed - we waited for 15 min for a table.
	- Finally we sat on two separate tables and shared pizzas.
	- We got to the airport on time - the flight was slightly delayed so we got a coffee and caught up with work.
	- Landed at 920 - Took an uber home - had pizza leftover and falafels with kebabs for dinner.

##### TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-06-04 00:00 %%
%% TCT_TEMPLATED_END 2025-06-04 23:59 %%



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
