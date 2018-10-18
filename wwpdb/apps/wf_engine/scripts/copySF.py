import shutil
import getopt
import os,sys

def main(argv):

   id = None
   sf = None
   root = '/net/wwpdb_da/da_top/data/archive'

   try:
    opts, args = getopt.getopt(argv,"hi:s:d",["help","id=", "sf="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print " use  -i <depID> -s  <sf-file>"
      elif opt in ("-i", "--id"):
        id = arg
      elif opt in ("-s", "--sf"):
        sf = arg

    if id is not None and sf is not None:
        if os.path.exists(sf):
              shutil.copyfile(sf,root + '/' + id + '/' + id + '_sf_P1.cif.V1')
              print "file copied - finished"
        else:
              print "that file does not exist - nothing done"
    else:
        print " use  -i <depID> -s  <sf-file>"
   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID> -s  <sf-file>"


if __name__ == "__main__":

  main(sys.argv[1:])


