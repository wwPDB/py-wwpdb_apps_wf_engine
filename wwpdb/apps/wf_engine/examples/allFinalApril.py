from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine

if __name__ == "__main__":

  depDataSetIdList=['D_055430','D_055453','D_056215','D_057171','D_057525','D_057584',
                                 'D_057620','D_057630','D_057750','D_057776','D_058195','D_058198',
                                 'D_058417','D_1009416','D_101544','D_101653','D_1040975','D_1043050',
                                 'D_1043121','D_1043325','D_1043518','D_1043612','D_1043613']

  for dep_id in depDataSetIdList:

    normal = ['testAlign.py','-x','-t','entry-point','-s',dep_id,'-d','0','-w','SequenceModule.xml','-p','./wf-defs/','-g','console']
  
    engine = mainEngine()

    print"************ April API test - console interface"
    engine.runNoThrow(normal)

