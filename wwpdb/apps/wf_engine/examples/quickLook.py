import getopt
import sys
import socket
from wwpdb.apps.wf_engine.engine.ServerMonitor import ServerMonitor

def main(argv):

    sm = ServerMonitor(None,None,None);
# paramter is the number of loops to review the data
# 0 : don't stop, 1 - summary and exit, 2 - review once....
    sm.watchOnly(1)

if __name__ == "__main__":

  main(sys.argv[1:])

