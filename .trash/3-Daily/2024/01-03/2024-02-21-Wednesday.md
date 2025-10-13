---
aliases: [2024-02-21]
tags: 
---
**[DayOne](dayone://open?date=2024-02-21)**

# TOP-OF-MIND
- #j595/journal 
	- Narrowed most of my AttentionLLM update to AK-10 misery to this [PR](https://github.pie.apple.com/heavenly/AttentionKit/pull/33/files). It changes the proto generation script to FastProtobuffable. Also the xcode project & workspace files are a nightmare to manage with git. They seemed to have gotten fucked up making the targets all funky. Fuck XCode.
	- Turns out XCode was installing roots on my device without my knowledge which was fucking up binaries from running properly. Had to do `darwinup list` to see and then uninstall everything.
	- Lots of pain in bringing AttentionLLM and the corresponding MotifTools visualize code up to date.
	- Got AttentionLLM working again!!
	- Created streamlit app to edit text prompt. Added ability to serve the prompt and fetch it from within the swift app at load time.
	- Trying to get prompt written to a separate txt file into the AttentionLLM app bundle and read it from there when remote fetching fails
	- 

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
