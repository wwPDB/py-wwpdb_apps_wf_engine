import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.api.status.dbapi.WFEtime import getTimeNow

'''
Reassign server engines

'''


def main(argv):

   hostin = None
   hostout = None

   wfApi= WfDbApi(verbose=False)

   try:
    opts, args = getopt.getopt(argv,"hi:o:",["help","in","out"])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print " use  -i <depID>"
      elif opt in ("-i", "--in"):
        hostin = arg
      elif opt in ("-o", "--out"):
        hostout = arg
# make sure the entry does not exist


    if hostin and hostout:
          print "Transfering host from %s to %s " % (hostin,hostout)
          sql = "delete from engine_monitoring where hostname = '" +hostin +"'"
#          sql = "select hostname from engine_monitoring where hostname = '" +hostin +"'"
          row = wfApi.runUpdateSQL(sql);
#	  row = wfApi.runSelectSQL(sql);
          print "Number of rows delete from engine_monitoring = " + str(row)

          sql = "update communication set host = '" + str(hostout) + "' where host = '" + str(hostin) + "'"
#          sql = "select count(1) from communication where host = '" + str(hostin) + "'"
          row = wfApi.runUpdateSQL(sql);
#          row = wfApi.runSelectSQL(sql);
          print "Number of rows communication changed in communication = " + str(row)

   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID>"


if __name__ == "__main__":

  main(sys.argv[1:])


