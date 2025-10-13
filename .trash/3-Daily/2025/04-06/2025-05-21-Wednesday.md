---
alias: ["Wednesday, May 21, 2025"]
tags: 
---
##### TOP-OF-MIND
- #journal/daily 
	- Chat Patti - Main street launch [[business acquisition#Parkers Crazy Cookies]]
		- non profit mission driven lender - loans up to $350k
		- SF downtown vibrancy fund - opening a new business in a designated area for ground floor street facing store front
		- would need at least one person to be working full time
		- Require last 3 years financials + personal guarantee: would need current year P&L 
		- will connect with a realtor who can look for places to rent in SF
			- will need 5 year lease in downtown and also SF permits & plans approved
		- fixed rate at 4% with 5 year term; no application fee or prepayment penalty
			- 2% loan fee, blanket lien on all equipment
			- need business plan with projections of how you would recover this business
			- get projections in order; figure out your true costs of running the business - lease etc
- #j595/journal 


##### TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-05-21 00:00 %%
%% TCT_TEMPLATED_END 2025-05-21 23:59 %%



##### NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

##### NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
