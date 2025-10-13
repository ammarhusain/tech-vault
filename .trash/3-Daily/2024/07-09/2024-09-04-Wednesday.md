---
alias: ["Wednesday, Sep 4, 2024"]
tags: 
---


# TOP-OF-MIND
- #j595/journal 
	- Morning crossfit - fun communal workout
	- Setup the most recent builds and ran AttentionKit+LLM with it
	- From Sreeni when Everest was not working :
		- Install a new HomeDiagnostics to get Everest working with Mac Glow: sudo green-restore --install-tools SapphirePalazzo22V4390a 
	- Running into errors that WSC blocks on getting physicalObjects in the snapshot when running in Everest mode. Also encountered this on [[2024-08-15-Thursday]]
	- Kyle told me about the Enroll app to add a bunch of Enrollable users to suncore easily
		- Need to update it with newer team members and Everest agents - [Initiating SAML single sign-on](https://github.pie.apple.com/heavenly/SunGlue)
			- ![[2024-09-04-Wednesday-2024-09-04.png]]
- #crawlspace 
	- Got the Javascript code working with webflow where it writes the logged in user's name in html!
	- You can debug the auth0 tokens that get returned on [JSON Web Tokens - jwt.io](https://jwt.io/)
# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-09-04 00:00 %%
%% TCT_TEMPLATED_END 2024-09-04 23:59 %%


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
