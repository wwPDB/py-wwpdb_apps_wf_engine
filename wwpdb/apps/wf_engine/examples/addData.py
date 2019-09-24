import getopt,shutil
import os,sys
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine
#
from wwpdb.api.status.dbapi.LocalDbApi import LocalDbApi
from wwpdb.utils.rcsb.FormatOut     import FormatOut
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.api.facade.ProcessRunner import ProcessRunner
from wwpdb.api.facade.WfDataObject  import WfDataObject

from wwpdb.apps.wf_engine.engine.WFEapplications import initialiseComms
from wwpdb.apps.wf_engine.engine.WFEapplications import populateDeposit
from wwpdb.apps.wf_engine.engine.WFEapplications import initilliseDeposit
from wwpdb.apps.wf_engine.engine.WFEapplications import initilliseDepositDict
from wwpdb.apps.wf_engine.engine.WFEapplications import initilliseInstance
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import resetComms
from wwpdb.apps.wf_engine.engine.WFEapplications import updateDeposit


def getDepID(wfApi):

        sql = "select max(idnum) from (select substr(dep_set_id,3,7) idnum from deposition where substr(dep_set_id,1,3) = 'D_3') as junk"
        ret = wfApi.runSelectSQL(sql);
        idnum = 300000
        for rett in ret:
          idnum = rett[0]
        try:
          num = int(idnum)
          depID = "D_" + str(int(idnum) + 1)
        except:
          depID = "D_300000"

	return depID

def main(argv):

# query to get the highest deposition number
# select dep_set_id, pdb_id from deposition where substring(dep_set_id,1,3) = 'D_3' order by dep_set_id desc limit 1;

  try:
    sf = None
    opts, args = getopt.getopt(argv,"hp:c:s:d",["help","pdb=","cif=","sf="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(" use  -p <PDB>")
        print(" use  -c <CIF>")
      elif opt in ("-p", "--pdb"):
        file = arg
        op = 'pdb2pdbx'
        format = 'pdb'
      elif opt in ("-c", "--cif"):
        op = 'rcsb-cifeps2pdbx'
        file = arg
        format = 'cif'
      elif opt in ("-s", "--sf"):
        sf = arg

    wfApi = WfDbApi(verbose = True)
    id = getDepID(wfApi)
    print("**********************************")
    print("        New ID  = %s" % id)
    print("**********************************")

#  make the folder
    wfo=WfDataObject()
    wfo.setDepositionDataSetId(id)
    wfo.setWorkflowInstanceId('W_001')
    wfo.setStorageType('archive')
    if op == 'pdb2pdbx':
      wfo.setContentTypeAndFormat( 'model' , 'pdb' )
    else:
      wfo.setContentTypeAndFormat( 'model' , 'pdbx' )
    wfo.setVersionId('next')
    pR=ProcessRunner(verbose=False) ;  
    pR.setInput("src",wfo) ;  
    ok=pR.setAction('mkdir');
    if not ok: print("setAction() for mkdir returns status %r" % (ok))
    ok=pR.preCheck()
    if not ok: print("preCheck() for mkdir returns status %r" % (ok))
    ok=pR.run()
    if not ok: 
	print("OpRun() for mkdir return status %r" % (ok))
        return

# copy file to folder

    fInp=WfDataObject()
    fInp.setExternalFilePath(file)
    fInp.setContentTypeAndFormat( 'model', format )
    fP=fInp.getFilePathReference();
    print("Input file is %s" % fP)

    fP=wfo.getFilePathReference();
    print("Output file is %s" % fP)

    pR=ProcessRunner(verbose=False);  
    pR.setInput("src",fInp);  
    pR.setOutput("dst",wfo);
    ok=pR.setAction('copy')
    if not ok: print("setAction() for copy returns status %r" % (ok))
    ok=pR.preCheck()
    if not ok: print("preCheck() for copy returns status %r" % (ok))
    ok=pR.run()
    if not ok: 
	print("OpRun() for copy return status %r" % (ok))
        return

    if op == 'pdb2pdbx':
      wfi=WfDataObject()
      wfi.setDepositionDataSetId(id)
      wfi.setWorkflowInstanceId('W_001')
      wfi.setStorageType('archive')
      wfi.setContentTypeAndFormat( 'model' , 'pdb' )
      wfi.setVersionId('latest')

      wfo.setContentTypeAndFormat( 'model' , 'pdbx' )

      pR=ProcessRunner(verbose=False);  
      pR.setInput("src",wfi);  
      pR.setOutput("dst",wfo);
      ok=pR.setAction(op)
      if not ok: print("setAction() for %s returns status %r" % (op,ok))
      ok=pR.preCheck()
      if not ok: print("preCheck() for %s returns status %r" % (op,ok))
      ok=pR.run()
      if not ok: 
	print("OpRun() for %s return status %r" % (op,ok))
        return

# fill in the deposition detail as much as possible
# creates a row with initial values
    initilliseDeposit(DBstatusAPI = wfApi, id = id)
    populateDeposit(wfApi,id)
# overwrite the inserted blanks :
    data = {"deposit_site" : "PDBe", "exp_method" : "X-RAY" }
    initilliseDepositDict(DBstatusAPI = wfApi, id = id , data = data)

# now prepare the tables for annotation
    initialiseComms(wfApi,id)
    initilliseInstance(DBstatusAPI = wfApi, id = id)

    resetInitialStateDB(wfApi,id)
    resetComms(wfApi,id)
    nrow = updateDeposit(wfApi,id, title = None)

    if sf != None:
      if os.path.exists(sf):
        shutil.copyfile(sf,'/ebi/msd/services/DandA/data/archive/' + id + '/' + id + '_sf_P1.cif.V1')
        print("copied SF file")


    print("finished")
  except getopt.GetoptError:
     # print help information and exit:
    print(" use  -i <depID>")


if __name__ == "__main__":

  main(sys.argv[1:])


