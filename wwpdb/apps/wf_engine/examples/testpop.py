import getopt
import sys

from wwpdb.api.status.dbapi.WfDbApi import WfDbApi
from wwpdb.apps.wf_engine.engine.WFEapplications import resetInitialStateDB
from wwpdb.apps.wf_engine.engine.WFEapplications import resetComms
from wwpdb.apps.wf_engine.engine.WFEapplications import populateDeposit


def main(argv):

  wfApi = WfDbApi(verbose = True)
#  populateDeposit(DBstatusAPI = wfApi,id  = 'D_300001')

  for i in range(300016,300045):
    try :
      populateDeposit(DBstatusAPI = wfApi,id  = 'D_' + str(i))
    except:
      pass

        

if __name__ == "__main__":

  main(sys.argv[1:])

