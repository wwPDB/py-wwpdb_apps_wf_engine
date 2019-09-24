from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

  normal = ['testAlign.py','-t','entry-point','-s','D_057750','-d','0','-w','SequenceModule.xml','-p','./wf-defs/']
#  normal = ['testAlign.py','-x','-t','entry-point','-s','D_1043612','-d','0','-w','SequenceModule.xml','-p','./wf-defs/']
  
  engine = mainEngine()

  print("************ April API test")
  engine.runNoThrow(normal)

