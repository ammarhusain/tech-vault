---
alias: ["Wednesday, Nov 13, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595/journal 
	- Chatted with Marisa & Greg for [scene understanding use cases](https://quip-apple.com/XfypA4r86HBm)
		- Marisa is excited about "informed autonomy" where the device is aware of the scene to make decisions such as notification delivery or proactive behaviors like "play music if someone is dancing"
			- Some video examples in this [box link](https://apple.ent.box.com/folder/286211017777?s=m79mr556de7wddrdf94ksgcv5gcsx07e)
			- #j595/idea - Would be neat to prototype a SmallLM on device that works on activity, enrolled persons, notification type & content to decide whether to notify or not. She mentioned these rule sets need to be semantic & situational so cannot be hand crafted.
				- An interesting addition to this would be manual overrides or teachable behavior - "let me know when mom calls" (may be this could be shoved in the context)
		- Teachable behaviors is the most vaguely defined one and it does not have anyone on HI assigned to it yet.
		- Need to follow up with Gui & Agatha on other scene understanding use cases.
- #journal/daily 
	- Met with psychiatrist Dr Jean-Pierre. He prescribed 5mg of Lexapro again - minimal dose to start with. Asked me to continue therapy; walk outside in the sun for at least 5 mins a day; get 7-8 hours of sleep.

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-11-13 00:00 %%
%% TCT_TEMPLATED_END 2024-11-13 23:59 %%


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
