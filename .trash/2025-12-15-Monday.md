---
<%*
// Get the file name
let fileName = tp.file.title;

// Extract date components from the file name
let [year, month, day] = fileName.split('-');

// Create a Date object
let date = new Date(year, month - 1, day); // month is 0-indexed in JavaScript

// Format the date
let formattedDate = date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', weekday: 'long' });

// Add the alias to the frontmatter, enclosed in quotes
tR += `alias: ["${formattedDate}"]`;
%>
tags: 
---
