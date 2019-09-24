import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.utils.rcsb.FormatOut     import FormatOut
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.api.status.dbapi.WFEtime import getTimeNow
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir
from wwpdb.apps.wf_engine.engine.WFEapplications import initialiseComms
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import WFEsetAnnotator


'''
  assumes the archive data is present - it loads the data into the workflow system
'''


def main(argv):

   path = wfClassDir() + 'wf-defs/'

   wfApi= WfDbApi(verbose=False)

   ann = None
   depID = None
   site = None
   try:
    opts, args = getopt.getopt(argv,"hi:a:s:d",["help","id=","an=","site="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(" use  -i <depID> -a <initials>")
      elif opt in ("-i", "--id"):
        depID =  arg
      elif opt in ("-a", "--an"):
        ann = arg
      elif opt in ("-s", "--site"):
        site = arg


    if ann is None or depID is None:
        print(" use  -i <depID> -a <annotator_initials>")
    else:
        depDB = {}
        depDB["DEP_SET_ID"]=depID
        if wfApi.exist(depDB):
          WFEsetAnnotator(wfApi,depID,ann)
          print("Done")
        else:
          print(" That ID is not loaded ")
   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID> -a <initials>")


if __name__ == "__main__":

  main(sys.argv[1:])


