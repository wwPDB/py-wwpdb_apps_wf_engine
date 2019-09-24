import getopt
import sys
import socket
import shlex
import subprocess

from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir

def main(argv):

    runningSE = myProcessID()

    if runningSE != None:
#  panic - already running
      print("This server is running a Workflow Daemon of process ID = " + str(runningSE))
      exit(0)

    path = wfClassDir() + 'wf-defs/'
    hostname = socket.gethostname()
    log = open("log/ServerEngine." + str(hostname)+".log","w");
    engine = mainEngine(1,log)
    normal = ['testAlign.py','-x','-k','WF','-t','entry-point','-s','monitor','-w','MonitorDB.xml','-p',path]
    engine.runNoThrow(normal)
    log.close()
        
def myProcessID():

        '''
          Method to return the process ID of this process
        '''


        try:
          str1 = "ps -C python -o pid,ppid,cmd"
          str2 = "grep 'monitor.py'"
          args = shlex.split(str1)
          ps = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          args = shlex.split(str2)
          grep1 = subprocess.Popen(args,stdin=ps.stdout,stdout=subprocess.PIPE)

        except OSError:
          pass

        monitor = None
        if grep1 is None:
          print("No process running")

        if grep1 is None:
#          print "monitor.py is not running"
           pass
        else:
          line = grep1.stdout.readline()
          line = grep1.stdout.readline()
          if line is None or len(line) < 2: return None
          words = line.split()
          monitor = words[0]

        return monitor


if __name__ == "__main__":

  main(sys.argv[1:])

