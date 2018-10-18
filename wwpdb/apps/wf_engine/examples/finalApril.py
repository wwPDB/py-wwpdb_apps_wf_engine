from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

  normal = ['testAlign.py','-x','-t','entry-point','-s','D_057750','-w','SequenceModule.xml','-p','./wf-defs/','-g','console']
#  normal = ['testAlign.py','-x','-t','entry-point','-s','D_1043612','-w','SequenceModule.xml','-p','./wf-defs/','-g','console']
  
  log = open("log/WFE_D_057750_SequenceModule.log","w");
  engine = mainEngine(debug = 0,prt = log)

  print"************ April API test"
  engine.runNoThrow(normal)
  log.close();

