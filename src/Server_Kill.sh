#! /bin/sh
# ends the server by looking up the process id
kill "$(ps -aux | grep "python3 app.py" | grep -v grep | awk '{print $2}')"
