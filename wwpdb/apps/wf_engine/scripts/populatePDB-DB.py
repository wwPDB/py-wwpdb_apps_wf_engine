import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.utils.rcsb.FormatOut     import FormatOut
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi

from wwpdb.apps.wf_engine.engine.WFEapplications import initialiseComms
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import WFEsetAnnotator


def main(argv):

   path = wfClassDir() + 'wf-defs/'

   wfApi= WfDbApi(verbose=True)

# query to get the highest deposition number
# select dep_set_id, pdb_id from deposition where substring(dep_set_id,1,3) = 'D_3' order by dep_set_id desc limit 1;

   try:
    opts, args = getopt.getopt(argv,"hi:a:d",["help","id="])
    for opt, arg in opts:
      print opt,  ", ", arg
      if opt in ("-h", "--help"):
        print " use  -i <depID>"
      elif opt in ("-i", "--id"):
        accession = arg
        sql = "select max(idnum) from (select substr(dep_set_id,3,7) idnum from deposition where substr(dep_set_id,1,3) = 'D_3') as junk"
        ret = wfApi.runSelectSQL(sql);
        idnum = 300000
        for rett in ret:
          idnum = rett[0]
        try:
          num = int(idnum)
          depID = "D_" + str(int(idnum) + 1)
        except:
          depID = "D_300000"
        print "---------------<" + depID + ">"
        depDB = {}
        depDB["DEP_SET_ID"]=depID
# make sure the entry does not exist
        if not wfApi.exist(depDB):
#        if 1 <> 1:
          print "Converting deposition " + accession + " to  " + depID
          engine = mainEngine()
          normal = ['testAlign.py','-t','entry-point','-s',depID,'-a',accession,'-d','1','-w','PopulatePDBeDB.xml','-p',path]
          engine.run(normal)
          initialiseComms(wfApi,depID)
          resetInitialStateDB(wfApi,depID)
          WFEsetAnnotator(wfApi,depID,'an')
          break;

        else:
          print " skipping ", depID, " as it is already loaded"
   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID>"


if __name__ == "__main__":

  main(sys.argv[1:])


