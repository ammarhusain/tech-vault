---
aliases: [2022-08-31]
created: 2022-08-31-Wednesday 17:59
modified: 2024-07-10-Wednesday 10:58
tags: 
---

---

# Top-of-mind
- Worked on the xcs234 [[xcs234 - assignment-3]] today. Remember whenever using the pytorch optimizer, you need to zero_grad to zero out the gradients before any forward passes and then doing a .backward() followed by a optimizer.step()

---

# Vault Updates

**Notes created in the last week:**

``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
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
