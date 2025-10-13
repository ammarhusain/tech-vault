# Recommendations
From lady on flight
- Abba show
- Back to the future show
- Vicoria and Albert museum
- Imperial museum
- Timeout website
- Hampton hall
# Logs
```dataviewjs 
let pages_foo = dv.pages('"Daily"').sort(p => p.file.name, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#travel/london"))))
}
```
