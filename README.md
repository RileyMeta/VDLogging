# VDLogging
Python Module for Version and Delta Error Logging

## Description
A fairly simple Python Error Logging module that will:
- Create a log file in a specific directory
- Automatically incriment the version IF a previous log exists
- Automatically start a timer at the start of the program
- Automatically calculate a delta (time from start) for each log
- All Errors are logged (appended) to the same file

It will **NOT** exit the application at any point, unless the log cannot be created.
> [!NOTE]
> New log files are only created when the program / module is initalized.

### Default Setup:
```python
#!/usr/bin/env python3

import vdlogging

L = Logging("my_program")
L.log_event(error_number, descriptions)
# or
L.error(errno, prompt, exit=True)
```
The name passed in the Class declaration is what the logs will be named, along with a version number.<br>
Optionally you can pass a specific location, instead of using the default `/tmp/`
```sh
L = Logging("my_program", "/var/logs/")
```

---
### Example Output:
```sh
$ cat /tmp/my_program_1.log
...
[ERROR 404 @ 00:00:02]: File not Found
[ERROR 500 @ 00:00:12]: Databse connection failed
...
```
