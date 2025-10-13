---
aliases: [2022-09-21]
created: 2022-09-21-Wednesday 10:38
modified: 2023-03-10-Friday 23:15
tags: 
---


---

# Quote
> If you set out to be liked, you would be prepared to compromise on anything at any time, and you would achieve nothing.
> — <cite>Margaret Thatcher</cite>

# Top-of-mind
- Chat with Brain HitL:
	- Mostly interested in data collection
	- Looking to RoboticsUI (web based) as primary tool for data collection - formerly ReachUI
	- Prioritizing data collection
	- Shifting strategy away from VR controllers to RoboticsUI
	- Mostly doing local teleop and remote teleop is possible
	- Possible to do asynchronous teleop - where robots are doing everything autonomously and can call for help when needed.
	- Browser can connect to multiple robots
	- Need help from EDR:
		- Need to upgrade GPU to A2000 - need eng help there
		- Availability of robots is not very high - need someone on site to start it up. Make it easy to operate for the data collection operator.
		- Logs get filled up very quickly
		- Make the fleet stable & reliable
		- Need the robot to be mobile with the manipulation

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
