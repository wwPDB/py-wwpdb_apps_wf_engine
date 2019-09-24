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

   try:
    opts, args = getopt.getopt(argv,"hi:a:d",["help","id="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(" use  -i <depID>")
      elif opt in ("-i", "--id"):
        id = arg
        depID =  id
        depDB = {}
        depDB["DEP_SET_ID"]=depID
# make sure the entry does not exist
        if not wfApi.exist(depDB):
           print(" That entry is not loaded ")
        else:
          print(" that entry is already loaded")
          sql = "select dep_set_id, annotator_initials, pdb_id,deposit_site from deposition where dep_set_id = '" +id +"'"
          ret = wfApi.runSelectSQL(sql);
          if ret is not None:
            for row in ret:
              print(" dep_set_id = " + row[0])
              print(" pdbID      = " + row[2])
              print(" annotator  = " + row[1])
              print(" dep site   = " + row[3])


   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID>")


if __name__ == "__main__":

  main(sys.argv[1:])


