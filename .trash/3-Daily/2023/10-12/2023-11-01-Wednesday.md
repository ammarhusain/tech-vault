---
aliases:
  - 2023-11-01
created: 2023-11-01-Wednesday 11:56
modified: 2023-11-01-Wednesday 12:03
tags: []
---
**[DayOne](dayone://open?date=2023-11-01)**
# TOP-OF-MIND
- #j595/journal 
	- Meeting on LLM & ML foundations. Ran the meeting pretty well
	- #j595/meditation need to be forceful and assertive in pushing back against the "build it all ourselves" attitude & comments mostly from Luke & Andreas
	- [ ] #j595/someday [MIT 6.5940 Fall 2023 TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2023-fall-65940) EfficientML course: seems like a lot of theory that I more or less already know. Would be interesting to get hands on with stuff.
	- Compiled and ran llama-cpp with the 13B llama-2 model [[ajax]]
		- `make -j` followed by `./main -m models/llama-2/llama-2-13b-chat.ggmlv3.q4_0.bin -p "Mao Zedong was: " -n 400 -e`

	 - In meeting with CometML: figure out
		 - on-prem hosting 
		 - license cost for a small 15-20 person team pilot
			 - low $2-3ks per year per seat.
		 - how do the features compare with w&b - more customizable
		 - support options? - can provide great dedicated support
		 - From Marshall on deployment guide - [Linux Install - Comet Docs](https://www.comet.com/docs/v2/deploying-comet/linux/linux-cometctl/)
	 - [x] #j595/todo find a paper to present in lit review on [[2023-11-16-Thursday]] [completed:: [[2024-01-09-Tuesday]]]
	 - W&B meeting:
		 - Yi: 3 instances at the moment - SPG, MLR & video eng
		 - Venky: Cant use SPG instance because MySQL database is shared. Prefered way is to have a docker container running on a kubernetes cluster
		 - Yi will sync with Cheng - how do we setup AWS@Apple account such that Venky or W&B ven. Key is AWS@Apple: info sec approved
		 - 4 components: domain name, kubernetes compute instance, mysql database, s3 bucket
		 - $100-300k for entire SPG : 50-100 seats: should be cheaper now

---
# TASKS
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has happens date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (happens on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
# CROSS-REFERENCED 
```dataviewjs
// Loop through pages 
for (let p of dv.pages()) {
	for (let ol of p.file.outlinks) {
		// find all the cross references of this file
		if (dv.current().file.path == ol.path) {
			// get all the lists in this file
			for (let ls of p.file.lists) {
				if (ls.text.includes(dv.current().file.name)) {
					dv.header(3, p.file.link + "  ...  " + ls.line)
					dv.paragraph(ls.text)
					dv.paragraph("---")
				}
			}
		}
	}
}
```

# VAULT UPDATES
## NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) AND file.ctime < date(substring(this.file.name,0,10))
SORT file.mtime ASCENDING
```

## NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
