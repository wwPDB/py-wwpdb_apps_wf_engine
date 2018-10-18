import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.api.status.dbapi.WFEtime import getTimeNow


'''
  Script to get the next depID in the requested "series".  A series
   is D_N : where N is the root series 
'''


def main(argv):

   wfApi= WfDbApi(verbose=False)

   try:
    opts, args = getopt.getopt(argv,"hi:d",["help","id="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print " use  -i <depID-series-root>"
        print " example     -i D_3"
      elif opt in ("-i", "--id"):
        id = arg[:3]
        sql = "select max(idnum) from (select substr(dep_set_id,3,7) idnum from deposition where substr(dep_set_id,1,3) = '" + id + "') as junk"
        ret = wfApi.runSelectSQL(sql);
        for rett in ret:
          idnum = rett[0]
        try:
          num = int(idnum)
          if num >= int(arg[2:3] + '99999'):
            print "There are no more ID left in that series"
          else:
            depID = "D_" + str(int(idnum) + 1)
            print " Next ID available in series " + str(id)  + " is " + depID
        except:
          print " There was no return from that query : the next depID is " + id + "00000"

   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID-series-root>"
        print " example     -i D_3"


if __name__ == "__main__":

  main(sys.argv[1:])


