---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

[python_sandbox.ipynb](https://drive.google.com/open?id=1fUbzOqndjx7dcFZUVp9sekYNNF5T23Iy&authuser=mrahusain%40gmail.com&usp=drive_fs)
[[sandbox.ipynb]]

UC Berkeley course - [[xcs433-002 - mastering python]]

**[[Pandas]]** has two main types [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) (equivalent to a table) and [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) (equivalent to a column). Lots of nifty functions to query in and apply transformations.

`requests` module to work on web related stuff. `requests.get(url)` to download something for example.

`threading` module for thread programming. `ThreadPoolExecutor` creates a pool that threads can be submitted to and are started and joined together rather than handling them individually. `Lock()` is a semaphore provided by the library to lock around resource usages.

`BeautifulSoup` module for HTML & other parsing.
`strptime()` converts strings to date time format. `trim` removed extraneous characters like trailing or leading whitespaces.

`datetime`: To handle anything to do with dates & time.
`re` module for regular expressions.

"`re`" module for [[regular expressions]].

**Database Types:**

- Relational Databases: Vanilla SQL based ones; rows and columns; each row is unique; SQLLite is a lightweight local DB for sanity testing in Python.
- Object Relational Mapping: Relational database but adds a layer where it auto converts back and forth between Python objects
- NoSQL Databases: Best for large data storage where relations aren't as important; MongoDB (file based), Redis etc.
