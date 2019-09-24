import getopt
import sys

from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import insertInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import resetComms
from wwpdb.apps.wf_engine.engine.WFEapplications import initialiseComms
from wwpdb.apps.wf_engine.engine.WFEapplications import initilliseDB
from wwpdb.apps.wf_engine.engine.metaDataObject import metaDataObject
from wwpdb.api.facade.WfDataObject  import WfDataObject
from wwpdb.apps.wf_engine.engine.WFEapplications import WFEsetAnnotator


def main(argv):

   id = None
   ann = None

   try:
    opts, args = getopt.getopt(argv,"hi:a:",["help","id=","an="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(" use  -i <depID>  (optional  -a <annotator_initials>)")
      elif opt in ("-i", "--id"):
        id = arg
      elif opt in ("-a", "--an"):
        ann = arg

    if id is not None:
        DBstatusAPI = WfDbApi(verbose=False)
        depDB = {}
        depDB["DEP_SET_ID"]=id
        if not DBstatusAPI.exist(depDB):
# Do a read of the CIF data - and populate the data
# This metaData is a dictionary requirement - copy for now
           metaData = metaDataObject()
           metaData.ID = id
           metaData.versionMajor = '00.01'
           metaData.versionMinor = ''
           metaData.name = 'RawCommand'
           metaData.description = 'Direct command'
           metaData.author = 'T.J.Oldfield'
# Create a WF-system file handle
           wfoInp = WfDataObject()
           wfoInp.setDepositionDataSetId(id)
           wfoInp.setStorageType('archive')
           wfoInp.setContentTypeAndFormat('model','pdbx')
           wfoInp.setVersionId('latest')
           input = {'D0': wfoInp }
# this is differt - do this first so as to not throw warnings
           insertInitialStateDB(DBstatusAPI,id)
           initilliseDB(metaData,id,'RawCommand','W_001',DBstatusAPI,input,2,sys.stderr)
        else:
           resetInitialStateDB(DBstatusAPI,id)

        resetComms(DBstatusAPI,id)
        initialiseComms(DBstatusAPI,id)
        if ann is not None:
           WFEsetAnnotator(DBstatusAPI,id,ann)

# This is the class file reference - necessary but neutral
    else:
      print(" use  -i <depID> (optional  -a <annotator_initials>)")
   except getopt.GetoptError:
        # print help information and exit:
        print(" use  -i <depID> (optional  -a <annotator_initials>)")
        

if __name__ == "__main__":

  main(sys.argv[1:])

