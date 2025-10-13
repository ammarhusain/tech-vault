---
alias: ["Wednesday, Aug 7, 2024"]
tags: 
---


# TOP-OF-MIND
- #j595/journal 
	- Tried finetuning the SmolLM 600M param model - ran into issues with converting it to GGUF
	- Tried running sunscreen with live device - does not seem to work
- #crawlspace 
	- Built the Join Waitlist form
	- Experimented with the Memberstack integration for Webflow - seems a bit overkill since we would just want to use AWS for our backend
	- Tinkered with AWS Cognito to build a user sign up / sign in workflow following a youtube video. Works well - now I just need to figure out how to get the member specific info from the AWS backend into the Webflow frontend.

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-08-07 00:00 %%
%% TCT_TEMPLATED_END 2024-08-07 23:59 %%


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
