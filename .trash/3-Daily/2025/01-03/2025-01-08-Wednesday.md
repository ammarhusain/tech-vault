---
alias: ["Wednesday, Jan 8, 2025"]
tags: 
---
# TOP-OF-MIND
- #journal/daily 
	- Chatted with Adam BofA agent for HELOC. Their terms are not that great and would only afford me a $160k as it stands today with rates 10.2%, ie Prime Rate + 2.625% margin which sucks.
		- No annual fee or closing fee though - only early termination of $425 if closed in < 3 years
	- Chat with Gwendolyn Wright - SBDC advisor (very very helpful) [Services - The Wright Consultants - San Francisco Small Business Consulting](https://www.thewrightconsultants.com/services/)
		- Business with absentee owners will absolutely go to die eventually - SBA will not give a loan for that
			- One way could be to give equity to management (make them partners) so they dont leave
			- Need to know the ins & outs of business and have a plan on how to grow it
		- SBA section of a bank is the lender. This is standard across all banks. Average rate is 2 to 4% of prime rate 
		- you need to know what you're buying is it an asset sale or is it a cash flow off of business? It could be one or the other but not both.
		- factors that are going into underwriting an SBA loan
			- Deb service coverage. This is similar to DTI for getting a home mortgage.
				- net earnings divided by the principal plus interest on the business
			- 3 years of tax returns and other financial statements
				- it is important that the business is set up for sale in that they do not have a tax strategy in place where profit margins are minimized
				- a common way companies minimize profit is by channeling income to inventory. For example, this reduces their tax liability.
				- have a business plan on how you can grow that business
					- liveplan.com offers a monthly subscription template for $20 a month with questions to fill out and generate a basic business plan
		- all owners with at least 20% will have to have personal liability in the business
			- personal credit score DTI factored in - it might make sense for one of the spouses to jump on this full-time and show that they can substitute their income through the business
		- three common ways to value a business
			-  sellers net discretionary earnings method
				- EBITDA + discretionary expenses, like travel, car, etc get added back to the  income statement
				- 2X net earnings is a good value for the business could go up to 3X in certain cases
			- asset sale where you buy the equipment in the business
				- look up the serial number of all the equipment. See what they're valued at online.
			- market value - for example NFT's or tech companies it is pretty much whatever the market is willing to pay for this type of business.
				- not applicable here
		- steps in acquiring a business
			- expressed interest and get basic details from the owners like earnings, etc.
			- put out a letter of intent LOI. This would have a broad clause for you to back out of. for example: ability to acquire financing.
			- get access to tax returns income statements, all the accounting books for this particular business
			- create a business plan on how you would like to grow this business and how you can screen line it operations and make it more efficient
			- apply for an SBA loan or get us SAFE from friends family or put up your own money
		- be cautious of sellers financing - if the owners know that the books are not right, the buyer will not be able to secure a loan so they might offer it. Getting sellers financing also may cause the buyer not to do property diligence.
			- make sure the sellers involved for the first due to three years after acquiring the business and one form of the other by having skin in the game
			
- #j595/journal 
	- Turned in a bunch of referrals from LinkedIn messages for job posting
	- Interviewed Yang Gao
	- Chat with Selina about NotificationsLM
		- in facetime - do we want to notify the user at all - its a shared device - privacy concerns whether the call should be announced at all
		- if the phone is ringing already or you are already looking at your phone - why notify on device
		- Vera wants a generic notification system to think through the use cases
		- Dont pull HI in too early - they might started pressuring people with more requirements
		- Need to create a quick Notifications 1 pager that lists out the proposed ML model architecture and some simple use cases that we can go through with Selina, Abhi, Luke & Martin
- called Apple HR about perf during mental health leave
	- I can complete my self assessment and submitted and after I go to leave, the ratings are finalized I will just not know what my ratings are until I return, but it seems like the pay adjustments RSU grants and bonus should get deposited. I'll probably have access to pay and finances through AppleConnect. It looks like so I don't think competition is adjusted very much. I just need to make sure I can submit a self assessment. If I don't submit a self assessment then it is it is what it Is.
	- 

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2025-01-08 00:00 %%
* Inbox
    - [x] Look up data view in craft 
    - [x] Change Amex airline fee credit 
    - [x] remove pblish: tag from obsidian notes 
    - [x] call apple HR for perf during sabbatical 
%% TCT_TEMPLATED_END 2025-01-08 23:59 %%


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
