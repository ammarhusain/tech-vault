---
alias: ["Wednesday, Aug 14, 2024"]
tags: 
---


# TOP-OF-MIND
- #journal/daily 
	- [x] Came across: [Transformer Explainer](https://poloclub.github.io/transformer-explainer/)  and its corresponding [paper](https://arxiv.org/pdf/2408.04619). Would be interesting to play around with it for an hour or two sometime  [completion:: 2025-02-28]
	- Text chatted with Alberto about Apple shuttles from SF. HE accepted an offer at VPG. May be I ll get an intro bonus?
- #j595/journal 
	- Found [AppleBot](https://pages.github.pie.apple.com/applebot/applebot-sdk/datasets/README.html) documentation from slack. Would be interested to go through it for [[Crawlspace]]

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-08-14 00:00 %%
%% TCT_TEMPLATED_END 2024-08-14 23:59 %%


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
