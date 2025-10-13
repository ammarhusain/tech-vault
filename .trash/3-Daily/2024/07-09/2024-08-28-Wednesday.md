---
alias: ["Wednesday, Aug 28, 2024"]
tags: 
---


# TOP-OF-MIND
- #journal/daily #travel/london  
	- Setup [aider](https://aider.chat/docs/install.html) - really cool chat LLM interface for coding
		- I could just use it in the repo to make changes rather than copy pasting code to the claude browser window
	- [Speculative Decoding: When Two LLMs are Faster than One - YouTube](https://www.youtube.com/watch?v =S-8yr_RibJ4) [[ai-ml|aiml]]
		- Like Medusa
		- You need a big target model and a corresponding small draft model (preferably distilled from the big target one) so that their token probability distributions align.
		- Sample K tokens from the smaller model then run these tokens as prefix through the larger big model. By feeding in the K generated tokens to the big model in order to get the K+1 next token we automatically end up generating the token probability distribution for the K tokens as well. This is the nature of the transformer where we can take the final_embedding at the N-1 position (where N is between 1 through K) from the last transformer block and run the feedforward projection layer on it <embed_dim_size x vocab_size> . Remember we usually take the final_embedding at index K to generate the token sampling distribution for the K+1 token. 
		- ![[2024-08-28-Wednesday-2024-08-28.png]]
		- In the worst case if we reject all tokens from the draft distribution we still do not waste the target distribution forward pass as it gives us 1 new token (only the K forward passes on the draft model are thrown away - which should be cheap anyway)
		- Use rejection sampling techniques to figure out whether to accept or reject a draft token - continue until first draft token is rejected
		- Interesting Karpathy tweets about it:
			  - [speculative execution](https://x.com/karpathy/status/1697318534555336961), [how is llama.cpp possible?](https://x.com/karpathy/status/1691571869051445433)
			  - **TLDR**: this weird trick works because LLMs are memory bound at inference time, in the "batch size 1" setting of sampling a single sequence of interest, that a large fraction of "local LLM" use cases fall into. And because most tokens are "easy".
	- Afternoon walking tour of Old City London - Embankment, Temple, big church inside Temple where all the crusaders departed for Jerusalem, oldest pub in London, house of the guy who wrote the Oxford dictionary, St Pauls Cathedral, Bank of England (where a lot of gold is stored), finally a viewpoint in the courtyard of a building overlooking Tower Bridge
	- Went to Barbican Center today to meet Jakub - Got dinner at the Cafe and worked until 8ish pm
	- #crawlspace 
		- prod_onboarding_request is the lambda to send the SQS request to start crawling the URL
			- Use zapier-test event which is of template SQS -> basically the "body" needs to be strigified:
				-       `"body": "{\n        \"domain\": \"ammarh.io\",\n        \"paywall\": false,\n        \"email\": \"self@ammarh.io\",\n        \"start_url\": \"ammarh.io\"\n      }",`
		- To check what got written to the DynamoDB table go [here](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#item-explorer?maximize=true&operation=SCAN&table=prod_storage): DynamoDB->Explore Items on prod_storage
		- Go to S3 -> prod_web_crawl to see the crawled pages

# TASKS COMPLETED TODAY
%% TCT_TEMPLATED_START 2024-08-28 00:00 %%
%% TCT_TEMPLATED_END 2024-08-28 23:59 %%


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
