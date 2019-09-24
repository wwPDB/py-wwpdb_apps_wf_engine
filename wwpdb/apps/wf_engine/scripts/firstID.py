import getopt
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.api.status.dbapi.WFEtime import getTimeNow


'''
  Script to get the first available depID in the requested "series".  A series
   is D_N : where N is the root series 
'''


def main(argv):

   wfApi= WfDbApi(verbose=False)

   try:
    opts, args = getopt.getopt(argv,"hi:d",["help","id="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(" use  -i <depID-series-root>")
        print(" example     -i D_3")
      elif opt in ("-i", "--id"):
        id = arg[:3]
        sql = "select idnum from (select substr(dep_set_id,3,7) idnum from deposition where substr(dep_set_id,1,3) = '" + id + "' order by substr(dep_set_id,3,7)) as junk"
        ret = wfApi.runSelectSQL(sql);
# test the first one 
        test = int(arg[2:3] + '00000')
        found = False
        if ret is None or len(ret) < 1:
          print(" First ID available in series " + str(arg)  + " is " + arg[:3] + '00000')
          found = True

        try:
          for rett in ret:
            id = int(rett[0])
#            print str(id) + " : " + str(test)
            if id != test:
              print(" First ID available in series " + str(arg)  + " is " + arg[:2] + str(test))
              found = True
              break
            elif test >= int(arg[2:3] + '99999'):
              print("There are no more ID left in that series")
            else:
              test = test + 1
          if not found:
            print(" First ID available in series " + str(arg)  + " is " + arg[:2] + str(test))
            
        except:
          print(" There was no return from that query : the next depID is unknonw ")

   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID-series-root>")
        print(" example     -i D_3")


if __name__ == "__main__":

  main(sys.argv[1:])


