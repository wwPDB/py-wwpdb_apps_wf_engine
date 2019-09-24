from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

  normal = ['testAlign.py','-x','-t','entry-point','-s','D_000002','-d','2','-w','fetchTest.xml','-p','./wf-defs/','-g','console']
  
  engine = mainEngine()

  print("************ select test 1")
  engine.runNoThrow(normal)

