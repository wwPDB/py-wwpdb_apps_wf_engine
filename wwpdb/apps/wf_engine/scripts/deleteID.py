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
delete from deposition where dep_set_id = 'D_013067';
delete from communication where dep_set_id = 'D_013067';
delete from wf_task where dep_set_id = 'D_013067';
delete from wf_instance where dep_set_id = 'D_013067';
delete from wf_instance_last where dep_set_id = 'D_013067';

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
        if True:
          sql = "delete from deposition where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows delete from deposition = " + str(row))
          sql = "delete from communication where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows communication from deposition = " + str(row))
          sql = "delete from wf_task where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows wf_task from deposition = " + str(row))
          sql = "delete from wf_instance where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows wf_instance from deposition = " + str(row))
          sql = "delete from wf_instance_last where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows wf_instance_last from deposition = " + str(row))
          sql = "delete from user_data where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows user_data from deposition = " + str(row))
          sql = "delete from timestamp where dep_set_id = '" +id +"'"
          row = wfApi.runUpdateSQL(sql);
          print("Number of rows timestamp from deposition = " + str(row))

   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID>")


if __name__ == "__main__":

  main(sys.argv[1:])


