---
aliases:
  - 2024-05-27-Monday
  - 2024-05-28-Tuesday
  - 2024-05-29-Wednesday
  - 2024-05-30-Thursday
  - 2024-05-31-Friday
  - 2024-06-01-Saturday
  - 2024-06-02-Sunday
tags: 
---
**[DayOne](dayone://open?date=2024-05-29)**

# TOP-OF-MIND
- #journal/meditations 
	- I feel like I am not opposed to work or putting in hardwork. I just hate doing it and am unmotivated when:
		- my deliverables are not crisp & clear
		- not feeling included - i hate the feeling that what i build will amount to nothing or if no one depends/needs it
		- i get a lot of opposition on it or its for my own amusement
		- requires me to consistently be in the zone to make progress
	- Ran Manuels tool - he really like to blabber but so far he hasnt generated too much data. Just has the tool
	- Got started setting up finetuning workflow with synthetic data & TinyLlama with [[hugging face]]
		- Mostly spent time formatting dataset.
		- I have done this finetuning before. Some mental block in my head seems to really derail me from focusing.
- #journal/daily 
	- Marla lesson - I am still struggling to keep my pitches in line. She mentioned that I need to get a keyboard and practice the scales first.
		- Xpro minus 1 is apparently some app that can help or find some app that teaches how to play the keyboard.
		- Feeling a bit overwhelmed about the learning curve here - I need to learn how to read music and play the piano even before I can sing anything.
	- Attended the Art & Tech luma event in Studio 55. Cool to see some of the demos. This vent it out one was interesting: Letitallout.vercel.demo
		- #tinker_short 
			- Vercel could be an interesting tool to tinker something with potentially.
			- [[2024-08-25-Sunday]] Also came across [Docs • SvelteKit](https://kit.svelte.dev/docs/adapter-vercel) for building UIs
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
