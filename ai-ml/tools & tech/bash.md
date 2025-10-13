---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---
- [grep & sed](https://stackoverflow.com/questions/6178498/using-grep-and-sed-to-find-and-replace-a-string)
  - [Remove lines](https://askubuntu.com/questions/354993/how-to-remove-lines-from-the-text-file-containing-specific-words-through-termina) that contained `entry:` with sed: `sed -i '/entry:/d' *.md`

```
sed -i 's/original/new/g' file.txt
```
Explanation:
- `sed` = Stream EDitor
- `-i` = in-place (i.e. save back to the original file)
- The command string:    
	- `s` = the substitute command
	- `original` = a regular expression describing the word to replace (or just the word itself)
	- `new` = the text to replace it with
	- `g` = global (i.e. replace all and not just the first occurrence)
	- `file.txt` = the file name
---

`for loop` example: `for i in {10..31..1} ; do echo $i; done`

---

- [Video compression](https://unix.stackexchange.com/questions/28803/how-can-i-reduce-a-videos-size-with-ffmpeg) command:
`ffmpeg -i tst.mp4 -vcodec libx264 -crf 20 tst_out.mp4`
`ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4`
-i: This specifies the input file. In that case, it is (input.mp4).-ss: Used with -i, this seeks in the input file (input.mp4) to position.00:01:00: This is the time your trimmed video will start with.-to: This specifies duration from start (00:01:40) to end (00:02:12).00:02:00: This is the time your trimmed video will end with.-c copy: This is an option to trim via stream copy. (NB: Very fast)

[[ffmpeg_python.ipynb]], [colab](https://drive.google.com/open?id=1nPt2f_YoBwq8KBuOhk9B0-yCitP6Fbp9&authuser=mrahusain%40gmail.com&usp=drive_fs)

ffmpeg-python [docs](https://kkroening.github.io/ffmpeg-python/index.html?highlight=drawtext#ffmpeg.drawtext)

---

[Use gifski to create gif files from a sequence of images](https://gif.ski/). Could also use it to create gifs from videos. Works super well
`gifski -o file.gif frame*.png`

---
**find**
Moving a large set of files:
`find image_datasets/AnimeFaces/images/* -type f -prune -name "*" -exec mv {} /image_datasets/AnimeFaces/. \;`

Recursively remove files of a certain extension:

```
find . -name "*.bak" -type f -delete
```

---

Get size & other image details:
`$ identify color.jpg`

> color.jpg JPEG 1980x650 1980x650+0+0 8-bit DirectClass 231KB 0.000u 0:00.000`

---
**git**
Getting diff between 2 branches to create a third branch
```
- create and checkout branch tmp at branch_a
- reset --soft to branch_b
- commit
```

Adding patch hunks individually in git : `git add -p` 

Git flight rules - [cheatsheet](https://github.com/k88hudson/git-flight-rules)

**Remove large file from git commit history**
``` 
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH_TO_YOUR_FILE" \
  --prune-empty --tag-name-filter cat -- --all
```

**Search for installed apt packages**

`sudo apt list --installed`  
  
**CMake debug builds with compile commands:**  
`cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DCMAKE_BUILD_TYPE=Debug ..`

**Database Types:**

- Relational Databases: Vanilla SQL based ones; rows and columns; each row is unique; SQLLite is a lightweight local DB for sanity testing in Python.
- Object Relational Mapping: Relational database but adds a layer where it auto converts back and forth between Python objects
- NoSQL Databases: Best for large data storage where relations aren't as important; MongoDB (file based), Redis etc.