import os
import sys

file = os.path.expanduser("~/.cache/is-active")
if os.access(file, os.F_OK):
    #if the lockfile is already there then check the PID number
    #in the lock file
    pidfile = open(file, "r")
    pidfile.seek(0)
    old_pid = pidfile.readline()
    # Now we check the PID from lock file matches to the current
    # process PID
    if os.path.exists("/proc/%s" % old_pid):
        # Killing the process if it is already started
        os.system(f'kill {old_pid}')
        sys.exit(1)
    else:
        # Removing the pid file if the file is present but the program is not running
        os.remove(file)

pidfile = open(file, "w")
pidfile.write("%s" % os.getpid())
pidfile.close()
