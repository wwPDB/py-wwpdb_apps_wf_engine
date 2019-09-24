import getopt
import sys
import datetime
import time
from time import gmtime, strftime,sleep
import socket
from wwpdb.apps.wf_engine.engine.ServerMonitor import ServerMonitor

def main(argv):

    sm = ServerMonitor(None,None,None);
# paramter is the number of loops to review the data
# 0 : don't stop, 1 - summary and exit, 2 - review once....

    while True:
      list = sm.staleServer(report = 2)

      print("-------" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "---------------")
      for item in list:
        print(str(item))
 
      print(time.sleep(10))

if __name__ == "__main__":

  main(sys.argv[1:])

