
```dataviewjs
let pages = dv.pages('"vault-management"').sort(p => p.file.name, "desc");
// Loop through pages 
for (let p of pages) {
	let outlinks = p.file.outlinks
	for (let ol of outlinks) {
		// find all the cross references of this file
		if (dv.current().file.path == ol.path) {
			// get all the lists in this file
			let lists = p.file.lists
			for (let ls of lists) {
				//if (ls.outlinks.indexOf("fooyah")) 
				let currFileName = dv.current().file.name
				if (ls.text.includes(currFileName)) {
				dv.paragraph(ls.text)
				}
				dv.paragraph(currFileName)			
			}
	

		}
	}
	
}
```



- [[2023-10-29-Sunday]] this is what happened