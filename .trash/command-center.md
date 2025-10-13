---
aliases: []
created: 2022-08-07-Sunday 09:16
modified: 2023-03-10-Friday 23:15
tags: 
---
[[principles]]

# Stuff to Get Done

### Personal
```dataviewjs 
const today = new Date().toISOString().split('T')[0]; // Get today's date
dv.taskList(dv.pages().sort(p => p.file.mtime, 'descending').file.tasks
	.where(t => t.text.includes("#todo")
			&& t.fullyCompleted == false
			&& (t.scheduled ? t.scheduled.toISODate() <= today : true)
	))//.groupBy(t => t.tags))
```

## Goals
```dataviewjs 
dv.taskList(dv.pages().sort(p => p.file.mtime, 'desc').file.tasks
	.where(t => (t.tags.includes("#goal")) && t.fullyCompleted == false))//.groupBy(t => t.tags))
```

## Maybe / Long-term
```dataviewjs 
dv.taskList(dv.pages().file.tasks
	.where(t => (t.tags.includes("#goal_long_term")) && t.fullyCompleted == false))//.groupBy(t => t.tags))
```
---

