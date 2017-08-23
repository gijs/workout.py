workout.py
==========

A super simple bodyweight workout notification system.

Obviously needs Python. 
Also needs [terminal-notifier](https://github.com/julienXX/terminal-notifier). 

Made for MacOS.


Why?
====

[Sitting is bad](https://www.bloomberg.com/quicktake/dangers-of-sitting) and standing desks suck.

workout.py is a perfect middle ground for me.


Installation
============

Copy `workout.py` anywhere you like.

Then run:
```
$ brew install terminal-notifier
$ crontab -e
```

Add this to your crontab:

```
1,31 8-18 * * * /path/to/workout.py
```

