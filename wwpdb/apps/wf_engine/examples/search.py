from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

  normal = ['testAlign.py','-x','-t','entry-point','-s','D_000002','-d','0','-w','searchTest1.xml','-p','./wf-defs/','-g','console']
  
  engine = mainEngine()

  print("************ test of 1UIS : 14 errors , no GUI, full debug")
  engine.runNoThrow(normal)

