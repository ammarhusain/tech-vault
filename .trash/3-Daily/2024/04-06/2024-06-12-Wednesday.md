---
aliases: []
tags: 
---
**[DayOne](dayone://open?date=2024-06-12)**

# TOP-OF-MIND
- #j595/journal 
	- Continued evolving the streamlit finetuned model eval UI to make it cleaner & easier to use
		- Added functionality in there to use llama-cpp-python instead of the llama-cpp server reducing one extra step and encapsulating the full eval inference within one script - gives ability to operate with a grammar and the results seem to be the same as the server version
	- Finetuned a model with the synth-sentences-casper-generic-fc3.json dataset that has j595 specific demo phrases
		- Initial eval of the model shows it to perform like crap
		- Modified the dataset to create a v2 with 595 names and more samples from casper-sentences rather than the generic sentences (9000:1000 mix) - kicked off a second finetuning run
	- Doing peer feedback: Sylvain, Martin
	- Chat with attention team about FC3- sprint 2 tasks & activities. Follow up call with Manuel where he vented his frustration with Jakub calling his work on WorldState Manager not necessary0
- #journal/daily 
	- Chat with Dennis - Meta recruiter:
		- IC6 - MLE: 5 interviews
		- 2 x45min standard coding - communication + efficiency + testing
		- 2 x45min ML design - whiteboard (in-person onsite or virtual), expected to drive convo
			- 3-5 min problem exploration - motivation & requirements
			- design approach, start designing your components and how they work together
			- proactively call trade-offs
			- design requirements: # of server, latency etc: ask your interviewer or state your assumptions
			- deep dive on one aspect of the system : security, efficiency, scale, performance (depth reflects IC6)
		- 1 x behavioral interview - tell me about a time ... - keep highlighting on these 5 signals
			- driving results: overcoming obstacles
			- growing continuously - learn from making mistakes
			- working in an unstructured environment & embracing ambiguity 
			- conflict resolution - disagreements in the workplace
			- collaboration & communicating effectively - overcome complex obstacles while working cross functionally
	- #travel/brazil 
		- Nice long walk on the beach near the Airbnb in the morning. Walked for almost 2 hours headed north of the island. Sana had a 12pm meeting so rushed back. Heard from the Airbnb host who said they ll fix the drain situation very soon. Showered and rushed to get some Vibe Poke before my 1.30pm Perception sync where I’d have to give an update. Worked at Cafe Cultura next door for several hours. Walked back to Hiper to pick up groceries for dinner - nice stir fry of vegetables and chicken. I did a nice home core workout while Sana was in meetings. Jumped on an attention quick sync with Paul and stuck around for some Manuel blabbering after. Dinner at home and then got a glass of wine at Galleria after. It was Brazilian Valentines Day!

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
