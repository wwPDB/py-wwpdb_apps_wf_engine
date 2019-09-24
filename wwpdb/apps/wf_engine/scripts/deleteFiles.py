import getopt
import os,sys,shutil
#
'''
  delete all files based on ID
'''

def main(argv):

   try:
    opts, args = getopt.getopt(argv,"hi:a:d",["help","id="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(" use  -i <depID>")
      elif opt in ("-i", "--id"):
        id = arg

    if id is None or len(id) < 6:
      print(" No ID provided ")
      sys.exit(0)

    subs = ['archive','deposit','workflow','deposit/temp_files/deposition','deposit/temp_files/deposition_uploads']

    for sub in subs:
      dir = '/net/wwpdb_da/da_top/data/' + sub + '/' + id
      if os.path.isdir(dir):
        print("will remove this data " + str(dir))
        shutil.rmtree(dir)
      else:
        print("no directory called " + dir)


   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID>")


if __name__ == "__main__":

  main(sys.argv[1:])


