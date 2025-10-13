---
aliases: []
tags: 
---
**[DayOne](dayone://open?date=2024-06-26)**
[photos](photos://library?search=june10)
# TOP-OF-MIND
-  #j595/journal 
	-  Evaluated the fp32 models: 5epoch & 3epoch and they are both much better than the results I was getting before.
	- Generated a bigger corpus of sentences to sample from. Kicked off 2 training runs of 3 epochs (one with and other without punctuation).
- #journal/daily
	- Met with Giel & Jorrit from Jurimesh along with Jakub for [[Crawlspace]] #crawlspace 
	- #travel/brazil  
		- Morning meeting about Crawlspace with the Belgian AI startup - debriefed with Jakub after
		- Went over to the beach after thinking ll take a bit. Water was not super inviting however.
		- Came back and I went over to Crossainteria Portuguese to work for a bit. The wifi there was crap though - mostly checked emails and chatted with Kevin Peterson after
		- Back at the Airbnb, worked for a bit
		- Head over to Copacabana around 4 to take a dip and chill for a while. Waves were still pretty large so did not go super deep. Had corn on the beach
		- Showered and then went to Zona sul to pick up some coconut water, veggie juice etc. Picked up some popcorn on the way back.
		- Worked for another couple of hours while hogging popcorn and chocolate.
		- Masala rice for dinner.
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
