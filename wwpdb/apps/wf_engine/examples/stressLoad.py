import getopt
import os,sys
import shutil
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.utils.rcsb.FormatOut     import FormatOut
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi

from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir
from wwpdb.apps.wf_engine.engine.WFEapplications import initialiseComms


def main(argv):

   path = wfClassDir() + 'wf-defs/'

   wfApi= WfDbApi(verbose=True)

   try:
    opts, args = getopt.getopt(argv,"hs:n:a:d",["help","start=","num="])
    start = 900010
    loop = 1
    for opt, arg in opts:
        print opt,  ", ", arg
        if opt in ("-h", "--help"):
          print " use  -n <size-of-stress>"
          exit(0)
        if opt in ("-n", "--num"):
          loop = int(arg)
        if opt in ("-s", "--start"):
          start = int(arg)
          if start < 900010: 
            print " Invalid start value 900010 < start < 999999 " + str(start)
            exit(0)
    print " ************** starting at " + str(start) + "  finish at " + str(start+loop)
    if loop > 0 and start > 900000:
        for i in range(start,start+loop):
          depID = "D_" + str(i)
          if not os.path.exists("/ebi/msd/services/data/archive/" + depID):
            os.mkdir("/ebi/msd/services/data/archive/" + depID)
            shutil.copy("/ebi/msd/services/data/archive/D_900000/D_900000_model_P1.cif.V1","/ebi/msd/services/data/archive/" + depID + "/" + depID + "_model_P1.cif.V1")
#          os.system("copy  %s %s" , "(/ebi/msd/services/data/archive/D_900000/D_900000_model_P1.cif.V1","/ebi/msd/services/data/archive/" + depID + "/" + depID + "_model_P1.cif.V1))"

          depDB = {}
          depDB["DEP_SET_ID"]=depID
# make sure the entry does not exist
          if not wfApi.exist(depDB):
            engine = mainEngine()
            normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','1','-w','PopulateStress.xml','-p',path]
            engine.runNoThrow(normal)
            initialiseComms(wfApi,depID)
          else:
            print " skipping ", depID, " as it is already loaded"
          engine = mainEngine()
          normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','1','-w','Stress.xml','-p',path]
          engine.runNoThrow(normal)
   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID>"


if __name__ == "__main__":

  main(sys.argv[1:])


