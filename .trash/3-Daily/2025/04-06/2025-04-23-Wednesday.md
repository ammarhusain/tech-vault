---
alias: ["Wednesday, Apr 23, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- #travel/egypt
		- Coffee & breakfast at Mr Mousa - then got picked up for the pyramids tour
		- Went into the pyramid of Khufu which was a really tight space and tested my claustrophobia. Was proud to have been able to get through it. Even though I was nervious in the start I was enjoying the experience inside.
		- Guide Fayrouz was not that great - she did not know too much and the tour kept taking us to tourist trap shops. We bought stuff half out of politeness and half because they seemed cool in the moment. Overall it was a bad idea though since we could have just bought it local boutique shops instead. We were also held hostage by the guide where she ended up taking us to a tourist trap restaurant at the end where the meal would cost $20 per person and probably not even authentic. Glad I walked out of there and asked to be dropped back to the Airbnb. Got chai & paratha wrap at Karak boy instead for a late lunch.
		- Some meetings and then got a wrap from Griix - ate at home watching the Ancient Egypt documentary

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-04-23 00:00 %%
%% TCT_TEMPLATED_END 2025-04-23 23:59 %%



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
