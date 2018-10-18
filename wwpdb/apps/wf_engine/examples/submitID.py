import getopt
import sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
from wwpdb.apps.wf_engine.engine.WFEapplications import wfLogDirectory
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir

def main(argv):

   id = "D_000000"
   acc = "1abc"
   path = wfClassDir() + 'wf-defs/'

   try:
    opts, args = getopt.getopt(argv,"hi:a:d",["help","id="])
    for opt, arg in opts:
      print opt,  ", ", arg
      if opt in ("-h", "--help"):
        print " use  -i <depID>"
      elif opt in ("-i", "--id"):
        id = arg
      elif opt in ("-a", "--accession"):
        acc = arg

    logDir = wfLogDirectory(id)
    log = open(logDir + "/WFE_" + id + "__SequenceModule.log","w");
    log = sys.stderr
    engine = mainEngine(debug=1,prt=log)
    normal = ['testAlign.py','-t','entry-point','-s',id,'-a',acc,'-d','1','-w','Annotation.xml','-p',path]
    engine.runNoThrow(normal)
    log.close()
   except getopt.GetoptError:
        # print help information and exit:
        print " use  -i <depID>"
        

if __name__ == "__main__":

  main(sys.argv[1:])

