import getopt
import sys

from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import resetComms

def main(argv):

   try:
    opts, args = getopt.getopt(argv,"hi:",["help","id="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print " use  -i <depID>"
      elif opt in ("-i", "--id"):
        id = arg
        DBstatusAPI = WfDbApi(verbose=False)
        resetInitialStateDB(DBstatusAPI,id)
        resetComms(DBstatusAPI,id)
   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID>"
        

if __name__ == "__main__":

  main(sys.argv[1:])

