# Work
- Be aware of out of scope workstreams popping up
- Design docs & agreed upon documentation does not matter - they might just change scope anyway
- Dont need to take charge if it is not appreciated - just provide technical leadership
- FC1:
	- Be very very very clear of the deliverable.
	- Make sure you understand exactly how this system you are building fits into the larger system.
	- Be assertive about dependencies that others need to deliver - be trigger happy filing radars.
	- Learned a lot about open-set vision detectors DETR style, SAM and vision to text adapters (Video-Llama lit review)
```dataviewjs
let pages_foo = dv.pages().sort(p => p.file.mtime, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#j595/meditation"))))
}
```

# Personal
```dataviewjs
let pages_foo = dv.pages().sort(p => p.file.mtime, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#journal/meditations"))))
}
```

## Travel
```dataviewjs
let pages_foo = dv.pages().sort(p => p.file.mtime, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#travel/meditation"))))
}
```