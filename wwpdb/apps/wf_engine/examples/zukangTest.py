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
    opts, args = getopt.getopt(argv,"hi:d",["help","id="])
    for opt, arg in opts:
        print opt,  ", ", arg
        if opt in ("-h", "--help"):
          print " use  -i <depID>"
          exit(0)
        if opt in ("-i", "--id"):
          depID = arg
# make sure the entry does not exist
          depDB = {}
          depDB["DEP_SET_ID"]=depID
          if not wfApi.exist(depDB):
            print " ID NOT FOUND " + str(depID)
          else:
            engine = mainEngine()
#            normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','4','-w','ReportsModuleUI.xml','-p',path]
#            normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','4','-w','AnnotateModule.xml','-p',path]
#            normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','4','-w','TransformerModule.xml','-p',path]
            normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','4','-w','LigandModule.xml','-p',path]
#            normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','4','-w','SequenceModule.xml','-p',path]
            engine.runNoThrow(normal)
          print "Finished "
   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID>"


if __name__ == "__main__":

  main(sys.argv[1:])


