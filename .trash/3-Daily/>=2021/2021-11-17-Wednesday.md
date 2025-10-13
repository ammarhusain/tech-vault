---
aliases: [2021-11-17]
created: 2023-01-10-Tuesday 14:34
modified: 2023-03-10-Friday 23:15
tags: 
---


---

# Quote
> People don't notice whether it's winter or summer when they're happy.
> — <cite>Anton Chekhov</cite>

# Top-of-mind

## Abhinav
 - Jasmine has already been working on this so pair up with her in creating this PRD
- Josh is good at visual PRDs that illustrates the vision
- goal - work on creating a visual PRD that not only describes the vision in words but work with the designer/illustrator to visually represent it.
- Everyone has their own vision of human in the loop in their own heads. By the end of it, the vision should be shared and everyone should be talking about the same thing.
- Set a 3 year horizon.
	 - What should HITL look like in 2025?
	 - What services do we expect to run in 2025? : Talk to Sara about this
- First step: requirements, detailed specs, what to build (visual in PRD); second step: build a roadmap, do we build buy or acquire (for ex Reach) this?
- Project has great visibility - has struggled to gain clarity thus far.
- Show evolution of HITL: next year it will do this, then after it will do that, and finally will do XYZ
- Next12-18 months detailes; can leave it vague after that
- Jasmine has been working to concretely spec out: onsite help vs remote reasoning vs remote demonstration ... how many incidents today and where we need to get to.
- Split the visual PRD with Jasmine - she tackles certain sections and I do others.
- Success: in Q1 implementation strategy defined; in Q2 begin implementation
- Get more imaginative: how is the robot interacting with the environment, how is it getting situational awareness?
- Will be invited to weekly staff meeting, regular 1:1s etc. Can make it general on how to become a PM, skillsets etc.

# Tasks
```dataviewjs
const date = `${dv.current().file.name}`
const query1 = `(has start date) OR (has due date) OR (has scheduled date) OR (has done date)`
const query2 = `(done on ` + date + `) OR (due on ` + date + `) OR (scheduled on ` + date + `) OR (starts on ` + date + `)`
dv.paragraph('```tasks\n ' + query1 + '\n' + query2 + '\n```');
```
---

## Vault Updates

**Notes created in the last week:**

``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) AND file.ctime < date(substring(this.file.name,0,10))
SORT file.mtime ASCENDING
```

**Notes modified in the last week:**

``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
