---
alias: ["Wednesday, Jan 22, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Finished uploading docs for US Bank HELOC application. Need a 2024 P&L statement for Umri LLC. Used Clause to generate it
		- [[2024-P&L-Umri-USBank-HELOC.pdf]]
		- [[2024-statements-umri-chase.pdf]]
	- Booked flights to Vancouver & return from Anchorage after Alaska cruise
	- Met with SCORE mentors Virginia & Chuck at SFPL Civic Center. Productive session and interesting org to look into for guidance - mostly retired people volunteering
		- Be frugal & creative as small biz owner
		- Looking into shared kitchen spaces to make crackers - a bit like corworking space - can help get leads from other non competitor counterparts
		- Instead of buying a business outright try to come in as an investor into an existing business - make sure the owner stays on since they have expertise to run the show. Share your vision and what you can bring to the table as investor. Slowly guide the business direction to grow toward your vision
- #j595/journal 
	- Update on [rdar://141230692](rdar://141230692) (Audio is missing at the end of Casper utterances)After checking reddit threads and some more fiddling I think adding the following instruction to the system prompt seems to work (at face value) and does not repro even after 50-60 tries : `- It is very important that you add a silent pause at the end of your response WITHOUT ever vocalizing it. This is to ensure the user knows you are done speaking.`However in one instance it became a bit more verbose / chatty in its responses and then just endlessly kept repeating itself. My initial thought was that its the same bug as [rdar://143146702](rdar://143146702) (Bubbles JS Client sets output token limit to 4096) that Teddy and I fixed last Friday but that does not seem to be the case looking at the logs.
		- Next steps:  
			- Investigate the repeating behavior more
			- Try the updated pause prompt for another 100 or so tries to repro
				![[bubbles-endless-repeats-itself.mp4]]
				![[2025-01-22-Wednesday-2025-01-22.png]]
		- Tested about ~175 invocations with 100 consecutive ones for the tabby cat prompt and it did not repro the dropped audio like before 
			- Worth pushing this to QA for now: https://github.pie.apple.com/heavenly/ConversationAgent/pull/260
			- I have only tested with a couple of prompts that were reliably reproducible of the core issue however it is not representative of the wide gamut of other interactions.
			- As for the endless repeating audio - looking at the logs further it seems like that was an issue with the console web UI and nothing to do with Bubbles
			- ![[2025-01-22-Wednesday-2025-01-22-1.png]]
				
# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-01-22 00:00 %%
%% TCT_TEMPLATED_END 2025-01-22 23:59 %%



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
