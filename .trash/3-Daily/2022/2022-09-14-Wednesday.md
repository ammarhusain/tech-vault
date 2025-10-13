---
aliases: [2022-09-14]
created: 2022-09-14-Wednesday 09:23
modified: 2023-03-10-Friday 23:15
tags: 
---


---

# Quote
> Doing what you love is the cornerstone of having abundance in your life.
> — <cite>Wayne Dyer</cite>

# Top-of-mind
- [The Information Lifecycle: How Three Filters Shape the Mind](https://moretothat.com/information-lifecycle/)
	This whole process of previously unknown facts eventually shaping one’s perspective is what I call the **information lifecycle**:
	![[lawrence-yeo-information-lifecycle-filters.png|400]]
		**Identities organize the familiar, but divide the unfamiliar. The more we love the idea of “us,” the more we hate the idea of “them.”**
		Without cultivating curiosity, the awareness filter remains closed to any facts in the first place.
		Without updating our capabilities, we can’t react to whatever data we discover.
		And without letting go of identity, no amount of information will ever shift our perspective.

---

# Vault Updates

**Notes created in the last week:**

``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

**Notes modified in the last week:**

``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
SORT file.mtime ASCENDING
```
---
