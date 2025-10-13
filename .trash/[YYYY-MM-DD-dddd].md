---
aliases:
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 0, tp.file.title, "YYYY-MM-DD") %>
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 1, tp.file.title, "YYYY-MM-DD") %>
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 2, tp.file.title, "YYYY-MM-DD") %>
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 3, tp.file.title, "YYYY-MM-DD") %>
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 4, tp.file.title, "YYYY-MM-DD") %>
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 5, tp.file.title, "YYYY-MM-DD") %>
  - <% tp.date.weekday("YYYY-MM-DD-dddd", 6, tp.file.title, "YYYY-MM-DD") %>
tags: 
---
**[DayOne](dayone://open?date=<% tp.file.title.substring(0,10) %>)**

# TOP-OF-MIND
- <%tp.file.cursor()%> 
#### NOTES CREATED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.ctime As Created
WHERE file.ctime >= date(substring(this.file.name,0,10)) - dur(1 week) 
AND file.ctime < date(substring(this.file.name,0,10)) 
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```

#### NOTES MODIFIED IN THE LAST WEEK
``` dataview
TABLE file.folder AS Folder, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= date(substring(this.file.name,0,10)) - dur(1 week)
AND file.mtime < date(substring(this.file.name,0,10))
AND file.ctime < date(substring(this.file.name,0,10)) - dur(1 week)
AND file.folder != "Daily"
SORT file.mtime ASCENDING
```
---
