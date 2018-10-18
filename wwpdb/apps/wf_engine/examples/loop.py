from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

  normal = ['testAlign.py','-x','-t','entry-point','-s','D_000001','-d','3','-w','loopTest.xml','-p','./wf-defs/','-g','console']
  
  engine = mainEngine()

  print"************ Loop test"
  engine.runNoThrow(normal)

