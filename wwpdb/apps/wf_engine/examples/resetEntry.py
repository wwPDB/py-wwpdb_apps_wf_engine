
import getopt
import os,sys
from wwpdb.api.status.dbapi.WFEtime import getTimeNow
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi

from wwpdb.apps.wf_engine.engine.WFEapplications import wfClassDir

'''
| ordinal | sender | receiver | dep_set_id   | wf_class_id | wf_inst_id | wf_class_file     | command | status | actual_timestamp   | parent_dep_set_id | parent_wf_class_id | parent_wf_inst_id | data_version | host                            | activity |
+---------+--------+----------+--------------+-------------+------------+-------------------+---------+--------+--------------------+-------------------+--------------------+-------------------+--------------+---------------------------------+----------+
|   17878 | INSERT | LOAD     | D_1100201302 | NULL        | NULL       | Annotation.bf.xml | INIT    | INIT   | 445441380.65467400 | D_1100201302      | Annotate           | W_001             | NULL         | pdb-hp-linux-1.rcsb.rutgers.edu | FINISHED |

'''

def main(argv):

    wfApi= WfDbApi(verbose=True)

    id = argv[0]

    if id is None:
      print("Please provide a depsetid ")
      sys.exit(0)
   
    host = None
    try:
      sql = " select hostname from engine_monitoring where cpu_usage = (select min(cpu_usage) from engine_monitoring)"
      ret = wfApi.runSelectSQL(sql);
      for r in ret:
        host = r[0]

      if not host:
        print(" Could not get hostname ?? " + host)
        sys.exit(0)
      else:
        print("Will assign " + str(id) + " to this host " + str(host))

      now =   getTimeNow()
    except Exception as e:
      print("failed to get host " + str(e))
      sys.exit(0)

    try:
      sql = "update communication set sender='INSERT',receiver='LOAD',wf_class_id=NULL,wf_inst_id=NULL,wf_class_file='Annotation.bf.xml',command='INIT',status='INIT',actual_timestamp='" + str(now) + "',parent_dep_set_id='" + str(id) + "',parent_wf_class_id='Annotate',parent_wf_inst_id='W_001',data_version=NULL,host='" + str(host) + "',activity='FINISHED' where dep_set_id = '" + str(id) + "'"
      print(sql)
      ok = wfApi.runUpdateSQL(sql);
      if ok < 1:
        print(" Please check that you have run this script on the right server - ID was not found for this host " + str(host))
    except Exception as e:
      print("Failed to update the database " + str(e))


if __name__ == "__main__":

  main(sys.argv[1:])
