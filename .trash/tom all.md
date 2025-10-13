---
aliases:
  - daily
created: 2022-08-29-Monday 06:44
modified: 2023-03-10-Friday 23:15
tags: []
---
# Last week
```dataviewjs
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

// Get the date 7 days ago
let sevenDaysAgo = new Date(today);
sevenDaysAgo.setDate(today.getDate() - 8);

let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate >= sevenDaysAgo && pageDate <= today;
    })
    .sort(p => p.file.name, "desc");

// Loop through pages 
for (let p of pages) {
    // Skip the Templates directory
    if (p.file.path.includes("Templates")) {
        continue;
    }
    let noteText = await dv.io.load(p.file.path); 
    let regexPattern = /#{1,6}\s(TOP-OF-MIND)\n(.+?)(?:\n#{1,6}|$)/sgi; 
    let matches = regexPattern.exec(noteText); 
    let fileName = p.file.name;
    
    if (matches != null) {
        let sectionName = matches[1]; 
        let sectionText = matches[2]; 
        // Insert into document however you like 
        dv.paragraph(dv.fileLink(fileName));
        dv.el("article", sectionText);
    }
}
```

# Last Month
```dataviewjs
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

// Get the date 7 days ago
let sevenDaysAgo = new Date(today);
sevenDaysAgo.setDate(today.getDate() - 8);
// Get the date a month ago
let oneMonthAgo = new Date(today);
oneMonthAgo.setDate(today.getDate() - 32);

let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate >= oneMonthAgo && pageDate <= sevenDaysAgo;
    })
    .sort(p => p.file.name, "desc");

// Loop through pages 
for (let p of pages) {
    // Skip the Templates directory
    if (p.file.path.includes("Templates")) {
        continue;
    }
    let noteText = await dv.io.load(p.file.path); 
    let regexPattern = /#{1,6}\s(TOP-OF-MIND)\n(.+?)(?:\n#{1,6}|$)/sgi; 
    let matches = regexPattern.exec(noteText); 
    let fileName = p.file.name;
    
    if (matches != null) {
        let sectionName = matches[1]; 
        let sectionText = matches[2]; 
        // Insert into document however you like 
        dv.paragraph(dv.fileLink(fileName));
        dv.el("article", sectionText);
    }
}
```

# Last Quarter
```dataviewjs
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

// Get the date a month ago
let oneMonthAgo = new Date(today);
oneMonthAgo.setDate(today.getDate() - 32);
// Get the date 7 days ago
let threeMonthsAgo = new Date(today);
threeMonthsAgo.setDate(today.getDate() - 92);

let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate >= threeMonthsAgo && pageDate <= oneMonthAgo;
    })
    .sort(p => p.file.name, "desc");

// Loop through pages 
for (let p of pages) {
    // Skip the Templates directory
    if (p.file.path.includes("Templates")) {
        continue;
    }
    let noteText = await dv.io.load(p.file.path); 
    let regexPattern = /#{1,6}\s(TOP-OF-MIND)\n(.+?)(?:\n#{1,6}|$)/sgi; 
    let matches = regexPattern.exec(noteText); 
    let fileName = p.file.name;
    
    if (matches != null) {
        let sectionName = matches[1]; 
        let sectionText = matches[2]; 
        // Insert into document however you like 
        dv.paragraph(dv.fileLink(fileName));
        dv.el("article", sectionText);
    }
}
```


# History
```dataviewjs 
// Get today's date
let today = new Date();
today.setHours(0, 0, 0, 0);

let threeMonthsAgo = new Date(today);
threeMonthsAgo.setDate(today.getDate() - 92);

let pages = dv.pages('"Daily"')
    .filter(p => {
        let pageDate = new Date(p.file.name.substring(0, 10));
        return pageDate <= threeMonthsAgo;
    })
    .sort(p => p.file.name, "desc");


// Loop through pages 
for (let p of pages) {
	// Skip the Templates directory
	if (p.file.path.includes("Templates")) {
		continue
	}
	let noteText = await dv.io.load(p.file.path); 
	let regexPattern = /#{1,6}\s(TOP-OF-MIND)\n(.+?)(?:\n#{1,6}|$)/sgi; 
	let matches = regexPattern.exec(noteText); 
	let fileName = p.file.name;
	
	if (matches != null) {
		let sectionName = matches[1]; 
		let sectionText = matches[2]; 
		// Insert into document however you like 
		dv.paragraph(dv.fileLink(fileName));
		dv.el("article", sectionText);
	}
}
```
