from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

# args = ["python",  self.path +"engine/mainEngine.py","-0","-s",self.depID,"-i",self.instID,"-t",self.taskID,"-d","2","-l",logFile,"-w",self.file,"-p",self.path+"wf-defs/"]

  normal = ['engine/mainEngine.py','-i','recover','-t','recover','-s','D_900000','-d','2','-w','Annotation.xml','-p','./wf-defs/']
  
  engine = mainEngine()

  print("************ April API test")
  engine.runNoThrow(normal)

