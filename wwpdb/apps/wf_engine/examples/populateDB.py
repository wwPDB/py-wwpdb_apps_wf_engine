import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.utils.rcsb.FormatOut     import FormatOut
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi

from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir


def main(argv):

    path = wfClassDir() + 'wf-defs/'
    cApi=LocalDbApi(verbose=True)
    rd=[]
    rd= cApi.getNewDepositedIds(1)

    wfApi= WfDbApi(verbose=True)

    for k in rd:
      depID = "D_" + k[4:]
      depDB = {}
      depDB["DEP_SET_ID"]=depID
# make sure the entry does not exist
      if not wfApi.exist(depDB):
        print "Converting deposition " + k + " to  " + depID
        engine = mainEngine()
        normal = ['testAlign.py','-t','entry-point','-s',depID,'-d','2','-w','PopulateDB.xml','-p',path]
        engine.runNoThrow(normal)
        now =   getTimeNow()
        sql = "insert communication (sender,receiver,dep_set_id,command,status,actual_timestamp,parent_dep_set_id,parent_wf_class_id,paraent_wf_inst_id,data_version) values ('INSERT','LOAD','" + id + "','INIT','INIT'," + now + ")"
        wfApi.runInsertSQL(sql);
      else:
        print " skipping ", depID, " as it is already loaded"


if __name__ == "__main__":

  main(sys.argv[1:])

