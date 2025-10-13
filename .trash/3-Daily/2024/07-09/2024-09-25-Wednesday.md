---
alias: ["Wednesday, Sep 25, 2024"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- [The Intelligence Age - Sam Altman](https://ia.samaltman.com/)
		- AI utopia article selling snake oil
	- [Founder Mode - paul graham](https://paulgraham.com/foundermode.html)
	- Hassle getting into work taking an Uber to shuttle which was both late & full. May be just drive next time since shuttle wifi is crap anyway
	- [Sort out your life! 100 tiny tricks to help with everything | Time management | The Guardian](https://www.theguardian.com/lifeandstyle/article/2024/sep/03/sort-out-your-life-100-tiny-tricks-to-help-with-everything-from-digital-overwhelm-to-lumpy-sugar-and-unpaid-bills)
- #j595/journal 
	- Messaged Saari directly about being included in AFM discussion after he mentioned AFM+ demo in the perception sync
	- Attention architecture review
	- Got device updated after a while - tested audio

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-09-25 00:00 %%
%% TCT_TEMPLATED_END 2024-09-25 23:59 %%


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
