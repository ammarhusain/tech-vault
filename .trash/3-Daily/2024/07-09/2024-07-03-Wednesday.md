---
alias: ["Wednesday, Jul 3, 2024"]
tags: 
---


# TOP-OF-MIND
- #journal/daily #travel/brazil 
	- Flight to Manaus from Rio at 10am with a stopover in Campinas. Reached the airport around 9am - guy at Azul counter was pretty friendly and took our second bag to check in as well. I guess they are not as sticklers about luggage in Brazilian airlines.
	- Most of the day was on the flight - there was wifi which was nice to get a bit of random work done
	- Checked into Novotel and took a short nap / rested for a bit. The wifi at the hotel was really crap which was frustrating because I was hoping to download photos to sort on the flight back to SF
	- Went over to Centro in Manaus - had an amazing charcoal grilled half Tambaqui fish at Tambaqui da Banda across from the Opera House / Amazon theater
	- We walked around for a little bit after but the town was super run down - took an early Uber back since we were both pretty exhausted.
	- Watched a little more of Elite Squad 2 and hit the bed

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-07-03 00:00 %%
%% TCT_TEMPLATED_END 2024-07-03 23:59 %%


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
