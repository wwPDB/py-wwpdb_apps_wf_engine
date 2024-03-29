import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.utils.rcsb.FormatOut     import FormatOut
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi

from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir
from wwpdb.apps.wf_engine.engine.WFEapplications import initialiseComms
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import WFEsetAnnotator

def main(argv):

   path = wfClassDir() + 'wf-defs/'

   wfApi= WfDbApi(verbose=True)

   try:
    opts, args = getopt.getopt(argv,"hi:a:d",["help","id="])
    for opt, arg in opts:
      print(opt,  ", ", arg)
      if opt in ("-h", "--help"):
        print(" use  -i <depID>")
      elif opt in ("-i", "--id"):
        id = arg
        depID = id
        depDB = {}
        depDB["DEP_SET_ID"]=depID
# make sure the entry does not exist
        if not wfApi.exist(depDB):
          print("Converting deposition " + id + " to  " + depID)
          engine = mainEngine()
          normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','1','-w','PopulateDB.xml','-p',path]
          engine.run(normal)
          resetInitialStateDB(wfApi,depID)
          initialiseComms(wfApi,depID)
          WFEsetAnnotator(wfApi,depID,'an')
          break;

        else:
          print(" skipping ", depID, " as it is already loaded")
   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID>")


if __name__ == "__main__":

  main(sys.argv[1:])


