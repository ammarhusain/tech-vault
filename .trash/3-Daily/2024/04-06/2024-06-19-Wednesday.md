---
aliases: []
tags: 
---
**[DayOne](dayone://open?date=2024-06-19)**

# TOP-OF-MIND
- #j595/journal 
	- Juneteenth holiday today
	- Found this internal home [brew repo](https://github.pie.apple.com/homebrew/brew) apple packages
		- To get AWS certificates had to run: brew install apple/crypto-services/trust-apple-corp-root-cas; sudo bash trust_apple_corp_root_cas.sh
	- Finetuned model with 30k examples of isRejected, isEngaged & isReferenced: it performs like crap!
		- Discovered that I am json converting the synthetic training data twice. this is introducing some weird characters that might cause the training inference to differ from the runtime inference - need to consolidate and fix.
- #journal/daily #travel/brazil 
	- Worked for a bit when I woke up because my trained model was performing pretty shit. Discovered some bugs in json formatting that I need to fix.
	- Packed up all our stuff
	- Went to Jurere Internacional to explore and get lunch - the place was nice but extremely dead. I suspect it would be more popping over the weekend or during summer
	- ⁠Walked around and got juice at a kiosk called (Something Natura) inside this fitness center (kinda like CP club) 
	- Took an über back to Campeche and got lunch at Paradiso as I was in a mood for a Prato 
	- Walked back - said bye to Floripa and took an Uber to the airport 
	- Checked in and chilled at the lounge for a while
	- Flight was pretty smooth - some more crossword 
	- Landed in Rio around 810 - Took an Uber over to Copacabana. The driver gave us some good recommendations like Assador, Boteco Belmonte, Fogo de Chao etc.
	- Rio is a lot more popping and lively - feels a lot like Bombay - Our airbnb is in this old building but the apt is clean and comfy except for a couple stains on the couch which I’m hoping are harmless 
	- Walked along the main beach avenue for a while and walked back but were a bit scared since the streets were starting to get empty
	- Got Tapas under the Airbnb at El Born Tapas
	- Picked up some dessert, and coffee and breakfast stuff from Zona Sul supermarket
	- Got back - crossword puzzle with dessert before bed
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
