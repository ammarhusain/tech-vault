
```dataviewjs 
let pages = dv.pages().sort(p => p.file.name, "desc");
// Loop through pages 
for (let p of pages) {
	let noteText = p.file.text //await dv.io.load(p.file.path); 
	dv.paragraph(dv.fileLink(note))
	let regexPattern = /#{1,6}\s(TOP-OF-MIND)\n(.+?)(?:\n#{1,6}|$)/sg; 
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


