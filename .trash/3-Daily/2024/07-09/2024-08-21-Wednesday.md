---
alias: ["Wednesday, Aug 21, 2024"]
tags: 
---


# TOP-OF-MIND
- #journal/daily 
	- Cool project that simply does : whisper STT/ASR -> llama3 -> openAI/Piper TTS
		- Hooks up with the macbooks clipboard for example - fun simple app to build around this for a local Obsidian voice assistant
		- I should build something like this on a raspberry pi - [[tinkering]] #tinker 
		- [GitHub - ILikeAI/AlwaysReddy: AlwaysReddy is a LLM voice assistant that is always just a hotkey away.](https://github.com/ILikeAI/AlwaysReddy)
		- [Voice chatting with llama 3 8B : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1ca510h/voice_chatting_with_llama_3_8b/)
		- [Using Whipser+GPT for automatic note taking and tagging : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1ewi9m2/using_whipsergpt_for_automatic_note_taking_and/)
		- Popular TTS library[Deep learning toolkit for Text-to-Speech, battle-tested in research and production](https://github.com/coqui-ai/TTS)
	- Interesting way to run LLMs [llamafile: Distribute and run LLMs with a single file.](https://github.com/Mozilla-Ocho/llamafile) [[llama]]
		- [llamafile/whisper.cpp/doc/getting-started.md](https://github.com/Mozilla-Ocho/llamafile/blob/main/whisper.cpp/doc/getting-started.md) [[tinkering#Raspberry Pi-5]]
- #j595/journal  

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-08-21 00:00 %%
%% TCT_TEMPLATED_END 2024-08-21 23:59 %%


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
