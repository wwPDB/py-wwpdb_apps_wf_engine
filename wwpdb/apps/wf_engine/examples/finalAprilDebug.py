from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
from wwpdb.apps.wf_engine.engine.WFEapplications import wfLogDirectory

import sys,os

if __name__ == "__main__":

  normal = ['testAlign.py','-x','-t','entry-point','-s','D_057750','-w','SequenceModule.xml','-p','./wf-defs/','-g','console']
#  normal = ['testAlign.py','-x','-t','entry-point','-s','D_1043612','-w','SequenceModule.xml','-p','./wf-defs/','-g','console']

  
  log = sys.stderr
  engine = mainEngine(debug=1,prt=log)

  engine.runNoThrow(normal)

