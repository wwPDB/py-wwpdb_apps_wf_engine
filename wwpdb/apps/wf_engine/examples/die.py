import getopt
import sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
from wwpdb.apps.wf_engine.engine.WFEapplications import wfLogDirectory
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir

def main(argv):

#   id = "D_1100200005"
   id = "D_900009"
   acc = "1abc"
   path = wfClassDir() + 'wf-defs/'

   log = sys.stderr
   engine = mainEngine(debug=1,prt=log)
   normal = ['engine.py','-t','entry-point','-s',id,'-a',acc,'-d','2','-w','testException.xml','-p',path]
   engine.runNoThrow(normal)
   print "finished"
        

if __name__ == "__main__":

  main(sys.argv[1:])

