import getopt
import sys
import socket
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir

def main(argv):

    path = wfClassDir() + 'wf-defs/'
    hostname = socket.gethostname()
    log = open("log/ServerEngine." + str(hostname)+".log","w");
    engine = mainEngine(1,log)
    normal = ['testAlign.py','-x','-k','WF','-t','entry-point','-s','watch','-w','WatchDB.xml','-p',path]
    engine.runNoThrow(normal)
    log.close()
        

if __name__ == "__main__":

  main(sys.argv[1:])

