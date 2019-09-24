import getopt
import os
import sys
import socket
import time
import shutil
import signal
from wwpdb.apps.wf_engine.engine.ServerMonitor import ServerMonitor


def main(argv):

    sm = ServerMonitor(None, None, None)
    proc = sm.myProcessID()
    print("My process ID : " + str(proc))

    if proc:
        try:
            pid = int(proc)
            os.kill(pid, signal.SIGKILL)
            print("Workflow Server killed ")
        except Exception as e:
            print("Failed to kill WF daemon" + str(id) + " because " + str(e))

    host = socket.gethostname()
    logName = '/wwpdb_da/da_top/sessions/wfm-logs/monitor-' + str(host) + '.log'
    print("Log will be written to " + str(logName))

    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())

    if os.path.exists(logName):
        shutil.move(logName, logName + '_' + now)

    os.system('. /wwpdb_da/da_top/scripts/env/runtime-environment.sh; python monitor.py > ' + logName + ' 2>&1 &')


if __name__ == "__main__":

    main(sys.argv[1:])
