---
alias: ["Wednesday, Oct 16, 2024"]
tags: 
---
# TOP-OF-MIND
- #j595/journal 
	- Walked through a step by step example of creating an OpenAI realtime API app in Node.js - [OpenAI Realtime API: A Guide With Examples | DataCamp](https://www.datacamp.com/tutorial/realtime-api-openai)
		- My demo app here: [openai-api-node-demo](file:///Users/ammarh/j595/openai-api-node-demo)
		- Very helpful in understanding the inner workings of the raw api ([OpenAI Platform](https://platform.openai.com/docs/api-reference/realtime-server-events/response/audio/delta)) as well as the beta client that they provide ([openai-realtime-api-beta/lib/client.js at main](https://github.com/openai/openai-realtime-api-beta/blob/main/lib/client.js)).
		- There is also a realtime console that comes with a frontend + relay server that uses the client to talk with the OpenAI backend ([openai/openai-realtime-console](https://github.com/openai/openai-realtime-console/tree/6ea4dba795fee868c60ea9e8e7eba7469974b3e9)   - meat of the console here [ConsolePage.tsx](https://github.com/openai/openai-realtime-console/blob/6ea4dba795fee868c60ea9e8e7eba7469974b3e9/src/pages/ConsolePage.tsx#L385))
	- Added the setMemory function to the demo app I built and it seems to work seamlessly - could be a nice proving ground for experimenting with these ideas for Bubbles
	- Figured out how to add links to local files in Obsidian! Opt+drag the file in 
	- [OpenAI Evals](https://platform.openai.com/docs/guides/evals) - seems like they have built a pipeline for their beefy GPT4o models to be used as evaluators along multiple criteria
# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-10-16 00:00 %%
%% TCT_TEMPLATED_END 2024-10-16 23:59 %%


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
