---
created: 2023-06-26-Monday 16:28
modified: 2023-10-05-Thursday 11:11
---

# Top of Mind Log
## Last Week
```dataviewjs 
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

// Get the date a month ago
let sevenDaysAgo = new Date(today);
sevenDaysAgo.setDate(today.getDate() - 8);
let oneMonthAgo = new Date(today);
oneMonthAgo.setDate(today.getDate() - 32);
// Get the date 7 days ago
let threeMonthsAgo = new Date(today);
threeMonthsAgo.setDate(today.getDate() - 92);
let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate >= sevenDaysAgo && pageDate <= today;
    })
    .sort(p => p.file.name, "desc");

for (let p of pages) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#journal"))))
}
```

## Last Month
```dataviewjs 
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

// Get the date a month ago
let sevenDaysAgo = new Date(today);
sevenDaysAgo.setDate(today.getDate() - 8);
let oneMonthAgo = new Date(today);
oneMonthAgo.setDate(today.getDate() - 32);
// Get the date 7 days ago
let threeMonthsAgo = new Date(today);
threeMonthsAgo.setDate(today.getDate() - 92);
let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate >= oneMonthAgo && pageDate <= sevenDaysAgo;
    })
    .sort(p => p.file.name, "desc");

for (let p of pages) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#journal"))))
}
```


## History
```dataviewjs 
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

// Get the date a month ago
let sevenDaysAgo = new Date(today);
sevenDaysAgo.setDate(today.getDate() - 8);
let oneMonthAgo = new Date(today);
oneMonthAgo.setDate(today.getDate() - 32);
// Get the date 7 days ago
let threeMonthsAgo = new Date(today);
threeMonthsAgo.setDate(today.getDate() - 92);
let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate <= oneMonthAgo;
    })
    .sort(p => p.file.name, "desc");

for (let p of pages) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#journal"))))
}

```
