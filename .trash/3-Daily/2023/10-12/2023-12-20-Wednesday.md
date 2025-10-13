---
aliases: [2023-12-20]
tags: 
---
**[DayOne](dayone://open?date=2023-12-20)**

# TOP-OF-MIND
- #j595/journal 
	- Character Meeting: 
		- Can we take a bunch of character examples and backstories and compress them using MS LLMLingua to see how it does? 
		- Are there benchmarks for character interactions that we can use or even build internally?
		- Shiraz shared: [Personality and Emotions | Inworld AI](https://docs.inworld.ai/docs/tutorial-basics/personality-emotion/#:~:text=Inworld%20characters%20can%20express%20a,specific%20emoji%20to%20each%20one)
		- Quip [agenda doc]([https://quip-apple.com/YgB6AXuKeQYH](https://quip-apple.com/YgB6AXuKeQYH))
	- Got the Llama swift app working on my iphone
		- Trying to get Xins model to get downloaded and run on device inference #j595/perf .
			- Worked on iPhone but had to manually copy the model because the download was only downloading 745M vs 746M for some reason. Used `dvdo` which is an equivalent of sudo for data vaults on iPhone.
				- When running it in an iOS simulator the model is stored here: /Users/ammarh/Library/Developer/CoreSimulator/Devices/60A0F1CB-E8DA-4C48-A0C2-7E5D8F0AD0E6/data/Containers/Data/Application/85EB155E-E4B0-4FE8-A68E-4B1364288E1E/Documents
				- scp  ammarh@169.254.93.42:~/j595/llama.cpp/models/xin-tinyllama1B/photo-1b-lora-v1_1-orca_data-single-5ep.Q5_K_M.gguf ~/.
				- dvdo mv ~/photo-1b-lora-v1_1-orca_data-single-5ep.Q5_K_M.gguf /var/mobile/Containers/Data/Application/BBD45E34-B0F7-4E20-A810-CD9753080C15/Documents/.
				- ![[2023-12-20-Wednesday-2023-12-21-1.jpeg]]
		- Got it build for J310 but TextEditor is not available on tvOS (need to find an alternative)
		- Experiment results that I presented in Work journal 2024/01/05 and as J595 demo #j595/perf 
			- * Got Xin’s TinyLlama 1B photographer model working and performance benchmarked on device:
			    * J310
			        * ~8.8 tokens / sec when started and goes upto ~29 tokens / sec once the caches are built up
				        * ![[2023-12-20-Wednesday-2024-06-05.png]]
			    * iPhone 15
			        * ~17.5 t/s when started and upto 41 t/s once caches are built up
			        * ![[2023-12-20-Wednesday-2024-06-05-1.png]]


	- SSO setup with Comet using Apple SAML IdMS

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
