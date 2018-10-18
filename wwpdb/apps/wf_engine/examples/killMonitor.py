import getopt,os
import sys,socket,time,shutil,signal
from wwpdb.apps.wf_engine.engine.ServerMonitor import ServerMonitor

def main(argv):

  sm = ServerMonitor(None,None,None)
  proc = sm.myProcessID()
  print "Process ID : " + str(proc)

  if proc:
    try:
      pid = int(proc)
      os.kill(pid,signal.SIGKILL)
      print "Workflow Server killed "
    except Exception,e:
      print "Failed to kill WF daemon" + str(id) + " because " + str(e)


if __name__ == "__main__":

  main(sys.argv[1:])


