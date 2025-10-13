---
aliases: 
created: 2023-01-11-Wednesday 10:12
modified: 2023-10-29-Sunday 17:48
tags: []
---

[Home - Obsidian Help](https://help.obsidian.md/Home)

# Code Snippets

## Jupyter Notebook

[[vault-manage.ipynb]]
## Tasks

[Filters | Obsidian Tasks](https://obsidian-tasks-group.github.io/obsidian-tasks/queries/filters/#tag-query-examples)

```obs
	```tasks
	not done
	(tags include #todo) AND (path includes apple)
	```
```

By dates:

````
```tasks
(done date is 2023-01-19) OR (due date is 2023-01-19) OR (scheduled date is 2023-01-19) OR (happens date is 2023-01-19)
```
````

By current file

````
```tasks
not done
filename includes home remodel
```
```tasks
done
filename includes home remodel
```
````

## Dataview

[Dataview](https://blacksmithgu.github.io/obsidian-dataview/)

``` obs
	```dataviewjs 
	dv.taskList(dv.pages().file.tasks
		.where(t => (t.text.includes("#todo") || t.tags.includes("#goal")) && t.fullyCompleted == false))//.groupBy(t => t.tags))
	```
```

More involved query from [[tom all]]

```obs
```dataviewjs 
let pages = dv.pages('"Daily"').sort(p => p.file.name, "desc");
// Loop through pages 
for (let p of pages) {
	// Skip the Templates directory
	if (p.file.path.includes("Templates")) {
		continue
	}
	let noteText = await dv.io.load(p.file.path); 
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

Added this to [[daily-template]] for cross-referencing notes with this particular note
```dataviewjs
// Loop through pages 
for (let p of dv.pages('"vault-management"')) {
	for (let ol of p.file.outlinks) {
		// find all the cross references of this file
		if (dv.current().file.path == ol.path) {
			// get all the lists in this file
			for (let ls of p.file.lists) {
				if (ls.text.includes(dv.current().file.name)) {
					dv.header(3, p.file.link)
					dv.paragraph(ls.text)
					dv.paragraph("---")
				}
			}
		}
	}
}
```
### Simple Dql Based Query
```obs
```dataview
LIST 
FROM #meditations 
SORT file.mtime DESC
```

```obs
```dataview
task
where !completed
group by file.name
```
## Minimal Theme

[Checklists - Minimal Documentation](https://minimal.guide/Block+types/Checklists)

## Launchctl Cron Job

Set up a launchd agent in `~/Library/LaunchAgents` for periodically backing up obsidian vault with git every morning at 8am - .plist specified job config
[Creating Launch Daemons and Agents](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html#//apple_ref/doc/uid/10000172i-SW7-BCIEDDBJ) , [Scheduling Timed Jobs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html#//apple_ref/doc/uid/10000172i-CH1-SW2), [How to Use launchd to Run Services in macOS | Medium](https://medium.com/swlh/how-to-use-launchd-to-run-services-in-macos-b972ed1e352)

Steps to enable launchctl job for [[git-backup.sh]] script

- Copy plist file to `~/Library/LaunchAgents/.` then run `launchctl load ~/Library/LaunchAgents/<>`
- Use the LaunchControl SW GUI utility to help debug - [soma-zone:](https://www.soma-zone.com/download/)
- Need to grant full disk access to LaunchControl, fdutil etc
- By default macOS marks the Documents directory as private so you need to grant `sh` full disk access from System > Privacy & Security
	1. Open Preferences
	2. Go to Security & Preferences
	3. Select Full Disk Access in the list on the left
	4. Click the lock to make changes
	5. Click the + button on the list on the right
	6. Navigate to the root of your HD
	7. Press CMD+Shift+. to show all the hidden items
	8. Select /bin/bash
	9. Quit Preferences
[[com.obsidian.vault-git-backup.plist]]

---

Had a cron job before:

``` 
0 8 * * * sh ~/Documents/second-brain/vault-management/git-backup.sh >> ~/Documents/second-brain/vault-management/git-backup-log.md 2>&1
```

This was set with `crontab -e` but does not automatically run if the computer is asleep at the time of the job (vs launchd that auto runs once the computer wakes up).

## Linter

[obsidian-linter/README.md at master · platers/obsidian-linter · GitHub](https://github.com/platers/obsidian-linter/blob/master/README.md)

```
---
---
```

## Custom Plugin

[Create your first plugin | Obsidian Plugin Developer Docs](https://marcus.se.net/obsidian-plugin-docs/getting-started/create-your-first-plugin)
[[2023-02-08-Wednesday]]- Trying it out in a test vault on my personal macbook-m1

## Weaviate

[[weaviate-sandbox.py]]

## iPad & iPhone
[[2023-12-03-Sunday]]
This was a useful post to get the vault working on the iPad again. Turn off & on the iCloud access to Obsidian app. Omnisearch plugin seems to cause it to crash - the constant reindex might be costly and since I have iCloud sync it is not possible to keep it only on the Mac while disabling on iPad.

## Obsidian Features
### Callouts
[Callouts - Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Callouts)

## Logs
Dataview query to pull tags from daily logs
```
```dataviewjs 
let pages_foo = dv.pages('"Daily"').sort(p => p.file.name, "desc");
for (let p of pages_foo) {
dv.taskList(p.file.lists.where(t => (t.text.includes("#aiml"))))
}
```
```

