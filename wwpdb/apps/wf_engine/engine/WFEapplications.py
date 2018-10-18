##
# File: WFEapplications.py
# Date:
#
# jdw    WARNING loads of domain specific functions here called from all over wfm and depui.
# jdw -- grab bag of functions -- change date 'unknown' date today
# jdw -- replace missing workflow with placeholder workflow in initilliseInstance(DBstatusAPI, id)
#
# 4-Aug-2015 jdw -- add def runOutOfBandWorkflow(DBstatusAPI, depSetId, classId, classFileName)
# Aug-2015 lm -- add def getWfStatus
#
#  14-Jul-2016 jdw add validation_server flag to functions runWorkflowOnUpload() & runValidationUpload()
#  26-Sep-2017 ep  initilliseDepositDict() parameterize strings to ensure proper quoting
#
# #
import time
import sys
import os
import pickle
import datetime
import random

from wwpdb.apps.wf_engine.process.ProcessRunner import ProcessRunner
from wwpdb.utils.wf.WfDataObject import WfDataObject
from wwpdb.utils.wf.dbapi.WfDbApi import WfDbApi
from wwpdb.utils.wf.dbapi.dbAPI import dbAPI
from wwpdb.utils.config.ConfigInfo import ConfigInfo, getSiteId
from wwpdb.utils.wf.dbapi.WFEtime import *
from email.mime.text import MIMEText

try:
    from wwpdb.apps.deposit.settings import STORAGE_PICKLED_DEPOSITIONS
except Exception as e:
    STORAGE_PICKLED_DEPOSITIONS = None


def runOutOfBandWorkflow(DBstatusAPI, depSetId, classId, classFileName):
    '''    UPDATE status.communication SET  sender=%s, receiver=%s, wf_class_id=%s, wf_class_file=%s,
                                         command=%s, status=%s, actual_timestamp=%s, data_version=%s
                                         WHERE ( dep_set_id=%s);

           ['WFUTILS', 'WFE', 'PDBX2PDBX_DEP', 'wf_op_pdbx2pdbx_fs_deposit.xml',
            'runWF', 'PENDING', Decimal('492013055.527617'), 'latest',
            'D_1000208939']
    '''
    t = getTimeNow()
    sqlTemplate = "UPDATE status.communication SET  sender='%s', receiver='%s', wf_class_id='%s', wf_class_file='%s', command='%s', status='%s', actual_timestamp='%s', data_version='%s' WHERE ( dep_set_id='%s')"
    tdata = ('WFUTILS', 'WFE', classId, classFileName, 'RunWF', 'PENDING', str(t), 'latest', depSetId)
    sql = sqlTemplate % (tdata)
    ok = DBstatusAPI.runUpdateSQL(sql)
    return ok


def reRunWorkflow(depID):
    '''
      method to reRun the validation WF just by setting the communication status to pending
    '''

    status = 'OK'
    try:
        timestamp = getTimeNow()
        wfApi = WfDbApi(verbose=True)
        sql = "select wf_class_file,command from communication where dep_set_id = '" + str(depID) + "'"
        rows = wfApi.runSelectSQL(sql)
        for row in rows:
            if row[0] in ['ValidDeposit.xml', 'depRunOnUpload.xml', 'wf_op_validdeposit_fs_deposit.xml', 'wf_op_uploaddep_fs_deposit.xml'] and row[1] in ['runWF', 'restartGoWF']:
                sql = "update communication set status = 'PENDING',actual_timestamp = '" + str(timestamp) + "' where dep_set_id = '" + str(depID) + "'"
                ok = wfApi.runUpdateSQL(sql)
                if ok < 1:
                    status = "Failed to mark this for restart "
            else:
                status = "WF was not in deposition "
            break
    except Exception as e:
        status = "Kill WF error " + str(e)

    print "Restart WF request:  " + str(depID) + " : " + str(status)

    return status


def getValidationStatus(depID, wfApi=None):
    '''
     method to see if there is a valid row in the database for communication and that it is WORKING for deposition uploads
    '''

    if not wfApi:
        wfApi = WfDbApi(verbose=True)

    sql = "select status from communication where dep_set_id = '" + \
        str(depID) + "' and wf_class_file in ('ValidDeposit.xml','depRunOnUpload.xml','wf_op_validdeposit_fs_deposit.xml','wf_op_uploaddep_fs_deposit.xml')"
    rows = wfApi.runSelectSQL(sql)
    print sql
    print str(rows)

    if rows is not None and len(rows) > 0:
        for row in rows:
            return row[0].lower()
    else:
        return 'unknown'

    return 'unknown'


def getWfStatus(depID, wfApi=None):
    '''
     method to check the status of a current workflow; and to see if there is a valid row in the database for communication and that it is WORKING for deposition uploads
    '''

    if not wfApi:
        wfApi = WfDbApi(verbose=True)

    #sql = "select status from communication where dep_set_id = '" + str(depID) + "' and wf_class_file = '" + classFile +"'"
    sql = "select status, wf_class_file from communication where dep_set_id = '" + str(depID) + "'"
    rows = wfApi.runSelectSQL(sql)
    if rows is not None and len(rows) > 0:
        # if rows[0][0] != 'WORKING':
        if rows[0][0] == 'FINISHED':
            #logging.info("wf_engine.engine.WFEapplications.getWfStatus: " + sql)
            #logging.info("wf_engine.engine.WFEapplications.getWfStatus: " + str(rows))
            print "wf_engine.engine.WFEapplications.getWfStatus: " + sql
            print "wf_engine.engine.WFEapplications.getWfStatus: " + str(rows)
        for row in rows:
            return row
            # return row[0].lower()
    else:
        return 'unknown'

    return 'unknown'


def killAllWF(depID, who):

    status = 'OK'
    try:
        timestamp = getTimeNow()
        wfApi = WfDbApi(verbose=True)

        sql = "update communication set command = 'killWF', actual_timestamp = '" + \
            str(timestamp) + "', receiver = 'WFE', status = 'PENDING' where dep_set_id = '" + str(depID) + "'"
        ok = wfApi.runUpdateSQL(sql)
        if ok < 1:
            status = "Failed to mark this for process kill"
    except Exception as e:
        status = "Kill WF error " + str(e)

    print "Kill WF request:  " + str(depID) + " from " + str(who)

    return status


def waitTime(sec):

    time.sleep(sec)

# Updated jdw
#


def wfClassDir():
    # JDW -- deprecated -- directory containing the directory containing ---
    siteId = getSiteId(defaultSiteId="WWPDB_DEPLOY_TEST")
    cI = ConfigInfo(siteId)
    ret = cI.get('SITE_WF_PYTHON_PATH')
    #ret = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../')) + '/'
    return ret


def wfLogDirectory(self, depID):
    siteId = getSiteId(defaultSiteId="WWPDB_DEPLOY_TEST")
    cI = ConfigInfo(siteId)

    topSessionPath = cI.get('SITE_WEB_APPS_TOP_SESSIONS_PATH')
    logDir = os.path.join(topSessionPath, "wf-logs", depID)

    if not os.path.exists(logDir):
        os.makedirs(logDir)

    return logDir


def startWFonSubmit(depid):
    '''
     UPDATE communication as c  SET c.sender='WFM' ,c.receiver ='WFE', c.dep_set_id='D_1100201165', c.wf_class_id= Null, c.wf_inst_id = Null,c.wf_class_file='ValidModule.xml',c.command='restartGoWF', c.status ='pending',c.actual_timestamp= Null, c.parent_dep_set_id='D_1100201165', c.parent_wf_class_id='ValMod', c.parent_wf_inst_id='None', c.data_version='latest'  WHERE c.ordinal = '17686'

    try:
          sql = "update communication set sender='DEP', receiver = 'WFE', wf_class_id=Null, wf_inst_id = Null, wf_class_file='Annotation.bf.xml', command='restartGoWF', status='pending', actual_timestamp=Null, parent_dep_set_id = '" + str(depid) + "', parent_wf_class_id='Annotate', parent_wf_inst_id='None', data_version='latest' where dep_set_id = '" + str(depid) +"'"
          ok = DBstatusAPI.runUpdateSQL(sql)
          if int(ok) == 1:
            print "Updated 1 row to start the WFE annotation "
          else:
            print "DID NOT UPDATE status"
    except Exception,e:
       print "failed to start WF from deposition"
    '''

    pass


def getNextInstanceId(DBstatusAPI, depID, prt=sys.stderr):
    """
      Create new workflow instance from the statusDB
      Returns the ID
      The status API returns an ID as a number, result is padded with zeros on a field width of 3
    """
    sql = "select max(cast(substr(wf_inst_id,3) as decimal(5,0)))+1 from wf_instance where dep_set_id = '" + str(depID) + "'"

    ll = DBstatusAPI.runSelectSQL(sql)

    if ll is None:
        instID = 1
    else:
        for l in ll:
            if l is None:
                instID = 1
            else:
                if l[0] is None:
                    instID = 1
                else:
                    instID = l[0]

    ret = "W_" + str(instID).zfill(3)

    prt.write("+getNextInstanceId: Created new workflow instance ID = %s" % str(ret))

    return ret


def insertInitialStateDB(DBstatusAPI, depID, debug=0, prt=sys.stderr):
    '''  Method to insert or update the instance of the annotation workflow within the wf_instance/wf_instance_last table -

    '''
    # Check if this workflow already exists in the wf_instance table -
    #
    sql = "select ordinal from wf_instance where (wf_class_id = 'Annotate')  and (dep_set_id = '" + str(depID) + "')  order by status_timestamp desc limit 1"
    allList = DBstatusAPI.runSelectSQL(sql)

    if allList is not None and len(allList) > 0:
        return updateInitialStateDB(DBstatusAPI, depID, debug=debug, prt=prt)

    now = getTimeNow()
    instId = getNextInstanceId(DBstatusAPI, depID, prt=prt)

    sql = "insert into wf_instance (wf_inst_id, wf_class_id, dep_set_id, owner, inst_status, status_timestamp) values ('" + instId + "','Annotate','" + \
        depID + "','Annotation.bf.xml','init','" + str(now) + "')"
    ok = DBstatusAPI.runInsertSQL(sql)
    if int(ok) == 1:
        prt.write("+insertInitialStateDB - insert returns %r row into wf_instance for %r\n" % (ok, depID))
    #
    # Try update then insert -
    sql = "update wf_instance_last set owner = 'Annotation.bf.xml', wf_class_id = 'Annotate' , inst_status = 'init', " + \
        " wf_inst_id = '" + instId + "', status_timestamp = '" + str(now) + "'  where dep_set_id = '" + str(depID) + "'"
    prt.write("+insertInitialStateDB - SQL =  %s \n" % sql)
    ok = DBstatusAPI.runUpdateSQL(sql)
    prt.write("+insertInitialStateDB - return ok  =  %r \n" % ok)
    if int(ok) == 1:
        prt.write("+updateInitialStateDB - Updating Annotate class in wf_instance suceeded for %s\n" % depID)
    else:
        sql = "insert into wf_instance_last (wf_inst_id, wf_class_id, dep_set_id, owner, inst_status, status_timestamp) values ('" + instId + "','Annotate','" + \
            depID + "','Annotation.bf.xml','init','" + str(now) + "')"
        ok = DBstatusAPI.runInsertSQL(sql)
        if int(ok) == 1:
            prt.write("+insertInitialStateDB - Inserted 1 row into wf_instance_last for %s\n " % depID)
        else:
            prt.write("+insertInitialStateDB - Updating Annotate class in wf_instance failed for %s\n" % depID)


def resetInitialStateDB(DBstatusAPI, depID, debug=0, prt=sys.stderr):
    '''
      Method to reset (insert/update) a annotation workflow back to init state by setting the owner, status and class
    '''
    #
    sql = "select ordinal from wf_instance where (wf_class_id = 'Annotate')  and (dep_set_id = '" + str(depID) + "')  order by status_timestamp desc limit 1"
    allList = DBstatusAPI.runSelectSQL(sql)

    if ((allList is not None) and (len(allList) > 0)):
        return updateInitialStateDB(DBstatusAPI, depID, debug=debug, prt=prt)
    else:
        return insertInitialStateDB(DBstatusAPI, depID, debug=debug, prt=prt)


def updateInitialStateDB(DBstatusAPI, depID, debug=0, prt=sys.stderr):
    '''
      Method to reset the annoation workflow back to init state by setting the owner, status and class
    '''
    #
    sql = "select ordinal from wf_instance where (wf_class_id = 'Annotate')  and (dep_set_id = '" + str(depID) + "')  order by status_timestamp desc limit 1"
    allList = DBstatusAPI.runSelectSQL(sql)

    if allList is not None:
        for allRow in allList:
            now = getTimeNow()
            ordinal = allRow[0]
            prt.write("+updateInitialStateDB - Ordinal  %s found for depID %s \n" % (depID, ordinal))
            sql = "update wf_instance set owner = 'Annotation.bf.xml', wf_class_id = 'Annotate' , inst_status = 'init', status_timestamp = '" +\
                str(now) + "' where ordinal = " + str(ordinal)
            ok = DBstatusAPI.runUpdateSQL(sql)
            # update the wf_instance_last table
            sql = "update wf_instance_last set owner = 'Annotation.bf.xml', wf_class_id = 'Annotate' , inst_status = 'init', status_timestamp = '" +\
                str(now) + "' where dep_set_id = '" + str(depID) + "'"
            ok = DBstatusAPI.runUpdateSQL(sql)
            if int(ok) == 1:
                prt.write("+updateInitialStateDB - %s status=%r for updating Annotate class in wf_instance \n" % (depID, ok))
            else:
                prt.write("+updateInitialStateDB - %s status=%r for updating Annotate class in wf_instance \n" % (depID, ok))


def WFEsendEmail(email, frm, subject, message, bcc=None):

    import smtplib

    if email is None:
        print " Invalid email " + str(email)
        return

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = frm
    msg['To'] = email
    sendTo = [email]
    if bcc:
        sendTo = [email] + [bcc]
        print "send email (bcc) to " + str(bcc)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    print "send email from " + str(frm)
    print "send email to " + str(email)
    try:
        s = smtplib.SMTP('localhost')
        s.sendmail('noreply@wwpdb.org', sendTo, msg.as_string())
        s.quit()
    except Exception as e:
        print " Exception in WFE.WFEsendEmail " + str(e)


def WFEsendDepositorEmail(depID, data):

    data = data.replace("$DEPID", depID)
    data = data.replace("$LINEFEED", '\n')

    words = data.split('|')
    email = WFEgetDepositorEmail(depID)

    WFEsendEmail(email, words[0], words[1], words[2])


def WFEgetDepositorEmail(depID):
    '''
      go get the depositor email
    '''

    if STORAGE_PICKLED_DEPOSITIONS is None:
        print " The storage location of the pickle file is not known"
        return None

    fPath = os.path.join(STORAGE_PICKLED_DEPOSITIONS, str(depID))
    fName = os.path.join(fPath, "formdata.pkl")

    if os.path.isfile(fName):
        try:
            f = open(fName, 'rb')
            dat = pickle.load(f)
            f.close()
            if 'email' in dat:
                return dat['email']
            else:
                return None
        except Exception as e:
            print "Tried to get the formdata and return email  " + str(e)
            return None
    else:
        ss = dbAPI(depID)
        ret = ss.runSelectNQ(table='user_data', select=['email', 'role'], where={"dep_set_id": depID, "role": "valid"})
        for r in ret:
            return r[0]
        return None


def checkDB(DBstatusAPI, debug=0, prt=sys.stderr):
    '''
      Method to renew the DB connection if it is more than 1 hour old
    '''

    if DBstatusAPI is None:
        return False

    if (getTimeNow() - DBstatusAPI['when']) > 3600:
        # test      if time.time() - DBstatusAPI['when'] > 60:
        DBstatusAPI['api'].close()
        if debug > 2:
            DBstatusAPI['api'] = WfDbApi(log=prt, verbose=True)
        else:
            DBstatusAPI['api'] = WfDbApi(log=prt, verbose=False)
        DBstatusAPI['when'] = getTimeNow()
        DBstatusAPI['number'] = DBstatusAPI['number'] + 1
        prt.write("WFE.WFEapplications.checkDB : creating new DB connection : " + str(DBstatusAPI['number']) + "\n")

    return True


def resetComms(DBstatusAPI, id):

    t = getTimeNow()
    sql = "update communication set sender='INSERT',receiver='LOAD',command='INIT',status='INIT',actual_timestamp='" + \
        str(t) + "',parent_dep_set_id='" + str(id) + "',parent_wf_class_id='Annotate',wf_class_file = 'Annotation.bf.xml',parent_wf_inst_id='W_001' where dep_set_id = '" + id + "'"
    print sql
    DBstatusAPI.runUpdateSQL(sql)


def startAnnotation(DBstatusAPI, id):
    '''
      method to start Annotation

      set  restartWFGo foe depID
    '''

    print " ******** call to startAnnotation stub for " + str(id)

    return


def initialiseComms(DBstatusAPI, id):

    sql = "select dep_set_id from communication where dep_set_id = '" + str(id) + "'"

    allList = DBstatusAPI.runSelectSQL(sql)

    print "****************" + str(allList)

    if allList is None or len(allList) < 1:
        # The normal case - insert a new value
        t = getTimeNow()
        sql = "insert communication (sender,receiver,dep_set_id,command,status,actual_timestamp,parent_dep_set_id,parent_wf_class_id,parent_wf_inst_id,wf_class_file) values ('INSERT','LOAD','" + str(
            id) + "','INIT','INIT'," + str(t) + ", '" + str(id) + "','Annotate','W_001','Annotation.bf.xml')"
        print sql
        DBstatusAPI.runInsertSQL(sql)
    else:
        # we already have that dep_setID - so just reset the communication
        resetComms(DBstatusAPI, id)


def initilliseInstance(DBstatusAPI, id):
    """  If there is no existing wf_instance for the input id then add a placeholder instance -
    """
    sql = "select dep_set_id from wf_instance where dep_set_id = '" + str(id) + "'"

    allList = DBstatusAPI.runSelectSQL(sql)

    t = getTimeNow()
    if allList is None or len(allList) < 1:
        # The normal case - insert a new value
        sql = "insert wf_instance (wf_inst_id,wf_class_id,dep_set_id,owner,inst_status,status_timestamp) values ('W_001','PLACEHOLDER','" + \
            str(id) + "','wf_op_placeholder.xml','dep','" + str(t) + "')"
        DBstatusAPI.runInsertSQL(sql)
        sql = "insert wf_instance_last (wf_inst_id,wf_class_id,dep_set_id,owner,inst_status,status_timestamp) values ('W_001','PLACEHOLDER','" + \
            str(id) + "','wf_op_placeholder.xml','dep','" + str(t) + "')"
        DBstatusAPI.runInsertSQL(sql)
    else:
        # we already have that dep_setID - so just reset the communication
        pass


def __initilliseInstancePrev(DBstatusAPI, id):

    sql = "select dep_set_id from wf_instance where dep_set_id = '" + str(id) + "'"

    allList = DBstatusAPI.runSelectSQL(sql)

    t = getTimeNow()
    if allList is None or len(allList) < 1:
        # The normal case - insert a new value
        sql = "insert wf_instance (wf_inst_id,wf_class_id,dep_set_id,owner,inst_status,status_timestamp) values ('W_001','depUpload','" + \
            str(id) + "','DepositionUpload.xml','dep','" + str(t) + "')"
        DBstatusAPI.runInsertSQL(sql)
        sql = "insert wf_instance_last (wf_inst_id,wf_class_id,dep_set_id,owner,inst_status,status_timestamp) values ('W_001','depUpload','" + \
            str(id) + "','DepositionUpload.xml','dep','" + str(t) + "')"
        DBstatusAPI.runInsertSQL(sql)
    else:
        # we already have that dep_setID - so just reset the communication
        pass


def initilliseDepositDict(DBstatusAPI, id, pdb='?', data=None):
    '''
        raw deposition table inialisation
        nrow = updateDeposit(wfApi,depid, title = dep_title, site = THIS_SITE, auth = dep_authors)

    '''

    depDB = {}
    depDB["DEP_SET_ID"] = id

    if DBstatusAPI.exist(depDB):
        print "ID exists "
        sql = 'update deposition set '
        args = ()
        first = False
        for key, value in data.iteritems():
            if not first:
                first = True
            else:
                sql = sql + ','
            sql = sql + str(key) + ' = %s' 
            # comma important with single value tuples
            args += (str(value),)
        sql = sql + ' where dep_set_id = %s' 
        args += (str(id),)

        print sql, args
        DBstatusAPI.runUpdateSQL(sql, args)
    else:
        # I do not think this code path is used - missing
        # commas between keys and values - EP 2017-09-26
        print "ID is new"
        sql = 'insert deposition (dep_set_id,'
        for key, value in data.iteritems():
            sql = sql + str(key)
        sql = sql + ') values ("' + str(id) + '",'
        for key, value in data.iteritems():
            sql = sql + '"' + str(value) + '"'

        sql = sql + ')'
        print sql
        DBstatusAPI.runInsertSQL(sql)


def getdepUIPassword(DBstatusAPI, id):

    depDB = {}
    depDB["DEP_SET_ID"] = id

    try:
        if DBstatusAPI.exist(depDB):
            print "ID exists "
            sql = "select depPW from  deposition where dep_set_id = '" + str(id) + "'"
            print sql
            allList = DBstatusAPI.runSelectSQL(sql)

            if allList is not None:
                for allRow in allList:
                    pw = allRow[0]
                    if pw == 'unknown':
                        pw = getHardwiredPW(str(id))
                    return pw
    except Exception as e:
        print "Failed to get depUI PW in status DB"

    return None


def getHardwiredPW(id):
    '''
      these PW are too long for the DB
    '''

    pw = {'D_1100201846': 'thisisalongpasswordmorethan16char',
          'D_1000200215': 'AYx34NmKhcLQLtxMj64n',
          'D_1000200727': 'projectcomponent4',
          'D_1000200796': 'pdbdepositicshinsnu',
          'D_1000203715': 'Assamaou1234Assamaou1234',
          'D_1000203789': 'mzc1hAdDGW5JyJ7pvS87Ouu',
          'D_1000204348': 'mangustotslovamango',
          'D_1000204349': 'mangustotsolvamango'}

    if id in pw:
        return pw[id]
    else:
        print "Another unknown PW for ID = " + str(id)
        return 'unknown'


def setdepUIPassword(DBstatusAPI, id, pw):
    '''
      keep this separate so we never overwrite the PW
    '''

    depDB = {}
    depDB["DEP_SET_ID"] = id

    try:
        if DBstatusAPI.exist(depDB):
            #       print "ID exists "
            sql = "update deposition set depPW = '" + str(pw) + "' where dep_set_id = '" + str(id) + "'"
            DBstatusAPI.runUpdateSQL(sql)
        else:
            print " Cannot set depUI password - depID does not exist"
    except Exception as e:
        print "Failed to set depUI PW in status DB " + str(e)


def initilliseDepositV2(DBstatusAPI, id, pdb='?', date=None, initials='unknown', deposit_site='?', process_site='?', status_code='DEP',
                        author_code='?', title='?', author_list='?', expt='?',
                        status_code_exp='?', SG_center='?', ann='dep', email='',
                        requested_codes=[]):
    '''
      raw deposition table inialisation
        nrow = updateDeposit(wfApi,depid, title = dep_title, site = THIS_SITE, auth = dep_authors)

    '''

    depDB = {}
    depDB["DEP_SET_ID"] = id

    if DBstatusAPI.exist(depDB):
        print "ID exists "
        sql = "update deposition set process_site = '" + str(process_site) + "', exp_method = '" + str(expt) + "' where dep_set_id = '" + str(id) + "'"
        print sql
        DBstatusAPI.runUpdateSQL(sql)
    else:
        sql = "insert deposition (dep_set_id, pdb_id, emdb_id, bmrb_id, deposit_site, process_site, status_code, author_release_status_code, title, author_list, exp_method, status_code_exp, SG_center, annotator_initials,email) values ('" + str(id) + "','" + str(pdb) + "','" + str(pdb) + "','" + str(
            pdb) + "','" + str(deposit_site) + "','" + str(process_site) + "','" + str(status_code) + "','" + str(author_code) + "','" + str(title) + "','" + str(author_list) + "','" + str(expt) + "','" + str(status_code_exp) + "','" + str(SG_center) + "','" + str(ann) + "','" + str(email) + "')"

        DBstatusAPI.runInsertSQL(sql)
        if 'EMDB' in requested_codes:
            sql = "update deposition set status_code_emdb = %r where dep_set_id = %r" % (status_code, id)
            DBstatusAPI.runInsertSQL(sql)


def initilliseDeposit(DBstatusAPI, id, pdb='?', date=None, initials='unknown', deposit_site='?', process_site='?', status_code='DEP',
                      author_code='?', title='?', author_list='?', expt='?', status_code_exp='?', SG_center='?', ann='dep', email=''):
    '''
      raw deposition table inialisation
 nrow = updateDeposit(wfApi,depid, title = dep_title, site = THIS_SITE, auth = dep_authors)

    '''

    depDB = {}
    depDB["DEP_SET_ID"] = id

    if DBstatusAPI.exist(depDB):
        print "ID exists "
        sql = "update deposition set process_site = '" + str(process_site) + "', exp_method = '" + str(expt) + "' where dep_set_id = '" + str(id) + "'"
        print sql
        DBstatusAPI.runUpdateSQL(sql)
    else:
        sql = "insert deposition (dep_set_id, pdb_id, deposit_site, process_site, status_code, author_release_status_code, title, author_list, exp_method, status_code_exp, SG_center, annotator_initials,email) values ('" + str(id) + "','" + str(pdb) + "','" + str(
            deposit_site) + "','" + str(process_site) + "','" + str(status_code) + "','" + str(author_code) + "','" + str(title) + "','" + str(author_list) + "','" + str(expt) + "','" + str(status_code_exp) + "','" + str(SG_center) + "','" + str(ann) + "','" + str(email) + "')"
        print sql
        DBstatusAPI.runInsertSQL(sql)


def runWorkflowValidationServer(DBstatusAPI, id):
    '''
       Add request to run WF  : ValidDeposit .xml
    '''

    print " Engine.WFEapplications.ValidDeposit " + str(id)
    now = getTimeNow()

    print " Engine.WFEapplications.runWorkflowValidationServer " + str(now)

    sql = "update communication set sender = 'DEP', receiver = 'WFE', wf_class_file = 'ValidDeposit.xml', command = 'runWF', status = 'PENDING', actual_timestamp = '" + \
        str(now) + "', parent_dep_set_id = '" + str(id) + "', parent_wf_class_id = 'ValDep', parent_wf_inst_id = 'W_001' where dep_set_id = '" + id + "'"

    print " Engine.WFEapplications.runWorkflowValidationServer - "
    print " Engine.WFEapplications.runWorkflowValidationServer - " + str(sql)

    nrow = DBstatusAPI.runUpdateSQL(sql)
    print " WFE.runWorkflowValidationServer :  Rows affected: %i" % nrow


def runWorkflowOnSubmit(DBstatusAPI, id):
    '''
       Add request to run WF  : depRunOnUpload.xml
    '''

    print " Engine.WFEapplications.runWorkflowOnUpload " + str(id)
    now = getTimeNow()

    print " Engine.WFEapplications.runWorkflowOnUpload " + str(now)

    sql = "update communication set sender = 'DEP', receiver = 'WFE', wf_class_file = 'depRunOnSubmit.xml', command = 'runWF', status = 'PENDING', actual_timestamp = '" + \
        str(now) + "', parent_dep_set_id = '" + str(id) + "', parent_wf_class_id = 'DepUpload', parent_wf_inst_id = 'W_001' where dep_set_id = '" + id + "'"

    print " Engine.WFEapplications.runWorkflowOnUpload - " + str(sql)

    nrow = DBstatusAPI.runUpdateSQL(sql)
    print " WFE.runWorkflowOnUpload :  Rows affected: %i" % nrow


def runValidationUpload(DBstatusAPI, id, validation_server=False):
    '''
       (old: Add request to run WF  : DepValModule.xml)
       Add request to run WF  : wf_op_validdeposit_fs_deposit.xml

       Jul/2016 function is called by deposit/depui/upload.py
    '''

    status = getValidationStatus(id, wfApi=DBstatusAPI)
    now = getTimeNow()

    print " Engine.WFEapplications.runValidationUpload " + str(now)
    print " Engine.WFEapplications.runValidationUpload " + str(id)
    print " Engine.WFEapplications.runValidationUpload " + str(status)

    if validation_server:
        wfName = "wf_op_validserver_fs_deposit.xml"
    else:
        wfName = "wf_op_validdeposit_fs_deposit.xml"

    if status == 'working':
        # sql = "update communication set command = 'restartGoWF',  wf_class_file = 'DepValModule.xml', status = 'PENDING', actual_timestamp = '" + \
        #    str(now) + "' where dep_set_id = '" + id + "'"
        sql = "update communication set command = 'restartGoWF',  wf_class_file = '" + wfName + "', wf_class_id = 'DepVal', status = 'PENDING', actual_timestamp = '" + \
            str(now) + "' where dep_set_id = '" + id + "'"

    else:
        # sql = "update communication set sender = 'DEP', receiver = 'WFE', wf_class_file = 'DepValModule.xml', command = 'runWF', status = 'PENDING', actual_timestamp = '" + \
        #    str(now) + "', parent_dep_set_id = '" + str(id) + "', parent_wf_class_id = 'DepUpload', parent_wf_inst_id = 'W_001' where dep_set_id = '" + id + "'"
        sql = "update communication set sender = 'DEP', receiver = 'WFE', wf_class_file = '" + wfName + "', wf_class_id = 'DepVal', command = 'runWF', status = 'PENDING', actual_timestamp = '" + \
            str(now) + "', parent_dep_set_id = '" + str(id) + "', parent_wf_class_id = 'DepUpload', parent_wf_inst_id = 'W_001' where dep_set_id = '" + id + "'"

    print " Engine.WFEapplications.runValidationUpload - " + str(sql)

    nrow = DBstatusAPI.runUpdateSQL(sql)
    print " WFE.runValidationUpload :  Rows affected: %i" % nrow


def runWorkflowOnUpload(DBstatusAPI, id, validation_server=False):
    '''
       (old: Add request to run WF  : depRunOnUpload.xml)
       Add request to run WF  : wf_op_uploaddep_fs_deposit.xml

       Jul/2016 function is called by deposit/depui/upload.py
    '''

    try:
        status = getValidationStatus(id, wfApi=DBstatusAPI)
        now = getTimeNow()
        print " Engine.WFEapplications.runWorkflowOnUpload " + str(now)
        print " Engine.WFEapplications.runWorkflowOnUpload " + str(id)
        print " Engine.WFEapplications.runWorkflowOnUpload " + str(status)
        if validation_server:
            wfName = "wf_op_uploadvalsrv_fs_deposit.xml"
        else:
            wfName = "wf_op_uploaddep_fs_deposit.xml"
        if status == 'working':
            # sql = "update communication set command = 'restartGoWF',  wf_class_file = 'depRunOnUpload.xml', status = 'PENDING', actual_timestamp = '" + \
            #    str(now) + "' where dep_set_id = '" + id + "'"
            sql = "update communication set command = 'restartGoWF',  wf_class_file = '" + wfName + "', wf_class_id = 'uploadMod', status = 'PENDING', actual_timestamp = '" + \
                str(now) + "' where dep_set_id = '" + id + "'"

        else:

            # sql = "update communication set sender = 'DEP', receiver = 'WFE', wf_class_file = 'depRunOnUpload.xml', command = 'runWF', status = 'PENDING', actual_timestamp = '" + \
            #    str(now) + "', parent_dep_set_id = '" + str(id) + "', parent_wf_class_id = 'DepUpload', parent_wf_inst_id = 'W_001' where dep_set_id = '" + id + "'"
            sql = "update communication set sender = 'DEP', receiver = 'WFE', wf_class_file = '" + wfName + "', wf_class_id = 'uploadMod', command = 'runWF', status = 'PENDING', actual_timestamp = '" + \
                str(now) + "', parent_dep_set_id = '" + str(id) + "', parent_wf_class_id = 'DepUpload', parent_wf_inst_id = 'W_001' where dep_set_id = '" + id + "'"

        print " Engine.WFEapplications.runWorkflowOnUpload - " + str(sql)

        nrow = DBstatusAPI.runUpdateSQL(sql)
        print " WFE.runWorkflowOnUpload :  Rows affected: %i" % nrow
    except Exception as e:
        print "Exception Engine.WFEapplications.runWorkflowOnUpload " + str(e)


def populateDeposit(DBstatusAPI, id):
    '''
     Entry point added to the workflow system to create an object within
     the state system
    '''

    debug = 3
    log = sys.stderr

    # Get the data out of the mmCIF
    if debug > 0:
        process = ProcessRunner(True, log)
    else:
        process = ProcessRunner(False, log)

    process.setAction("status")

    wfoInp = WfDataObject()
    wfoInp.setDepositionDataSetId(id)
    wfoInp.setStorageType('archive')
    wfoInp.setContentTypeAndFormat('model', 'pdbx')
    wfoInp.setVersionId('latest')
    dP = wfoInp.getDirPathReference()
    fP = wfoInp.getFilePathReference()
    oVn = wfoInp.getFileVersionNumber()
    process.setInput("src", wfoInp)

    wfoOut = WfDataObject()
    wfoOut.setContainerTypeName('dict')
    wfoOut.setValueTypeName('string')
    process.setOutput("dst", wfoOut)

    if not process.preCheck():
        print "WFE.WFEapplications.initialliseDeposit  : failed to setup process\n"

    if not process.run():
        print "WFE.WFEapplications.initialliseDeposit : failed to run process\n"

    dataDict = wfoOut.getValue()

    if dataDict is not None:
        if 'recvd_initial_deposition_date' in dataDict:
            depDate = dataDict['recvd_initial_deposition_date']
        else:
            # JDW JDW
            today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
            #depDate = 'unknown'
            depDate = today

        if 'title' in dataDict:
            title = dataDict['title'].replace("'", " ")
        else:
            title = 'Unknown'

        if 'audit_author' in dataDict:
            auth = dataDict['audit_author']
            if isinstance(auth, list):
                author_list = ""
                author_list = " ".join(["%s," % a for a in auth])
            elif isinstance(auth, str):
                author_list = auth
            else:
                print " Unknown type of author list " + str(type(auth))
            author_list = author_list.replace("'", " ")
        else:
            author_list = "unknown"

        if 'exp_method' in dataDict:
            ex = dataDict['exp_method']
            expt = ""
            if 'status_code_nmr' in dataDict or ex.find('NMR') >= 0:
                expt += "NMR"
            if 'status_code_em' in dataDict or ex.find("EM") >= 0:
                if len(expt) > 0:
                    expt += ","
                expt += "EM"
            if 'status_code_sf' in dataDict or ex.find("XRAY") >= 0:
                if len(expt) > 0:
                    expt += ","
                expt += "xray"
        else:
            expt = 'Unknown'

        if 'full_name_of_center' in dataDict:
            sg_center = dataDict['full_name_of_center']
        else:
            sg_center = 'Unknown'

        now = datetime.datetime.utcnow().strftime("%Y-%m-%d")

        sql = "update deposition set initial_deposition_date = '" + str(now) + "',title = '" + str(title) + "', author_list = '" + str(
            author_list) + "', exp_method = '" + str(expt) + "',sg_center = '" + str(sg_center) + "' where dep_set_id = '" + str(id) + "' and status_code = 'DEP'"
        print sql
        nrow = DBstatusAPI.runUpdateSQL(sql)
        print "rows change " + str(nrow)


def updateDeposit(DBstatusAPI, id, site='pdbe', title='?', auth='?', method='?'):
    '''
      update deposition communications table
    '''

    depDB = {}
    depDB["DEP_SET_ID"] = id
    timeNow = getTimeNow()

    if DBstatusAPI.exist(depDB):

        print " -> Running SQL 1 : update deposition"
        if title is None:
            sql = "update deposition set annotator_initials = 'unknown',status_code = 'PROC'   where dep_set_id = '%s' and status_code = 'DEP'" % (id)
        else:
            sql = "update deposition set annotator_initials = 'unknown',status_code = 'PROC', deposit_site = '%s', title = '%s', author_list = '%s', exp_method = '%s' where dep_set_id = '%s' and status_code = 'DEP'" % (
                site, title, auth, method, id)
        print sql
        nrow = DBstatusAPI.runUpdateSQL(sql)
        print "Rows affected: %i" % nrow

        print " -> Running SQL 2 : insert wf_instance"
# make sure we only get the last in case processing was done with new instance data
        sql = "select ordinal from wf_instance where dep_set_id = '" + str(id) + "'  order by status_timestamp desc limit 1"
        allList = DBstatusAPI.runSelectSQL(sql)

        if allList is not None:
            for allRow in allList:
                ordinal = allRow[0]
                sql = "update wf_instance set wf_inst_id = 'W_001', wf_class_id = 'Annotate', owner = 'Annotation.bf.xml', inst_status = 'init', status_timestamp = '%s' where ordinal = '%s'" % (
                    timeNow, str(ordinal))
                print sql
                nrow = DBstatusAPI.runInsertSQL(sql)
                print "Rows affected: %i" % nrow
                break

        print " -> Running SQL 3 : insert wf_instance_last"
        sql = "update wf_instance_last set wf_inst_id = 'W_001', wf_class_id = 'Annotate', owner = 'Annotation.bf.xml', inst_status = 'init', status_timestamp = '%s' where dep_set_id = '%s'" % (
            timeNow, str(id))
        print sql
        nrow = DBstatusAPI.runInsertSQL(sql)
        print "Rows affected: %i" % nrow

        return nrow

    return 0


def initilliseDB(metaData, depositionID, WorkflowClassID, WorkflowInstanceID, DBstatusAPI, input, debug=0, prt=sys.stderr):
    '''
      method to extract information from the domain data
      using a depositionDB and put this into the statusDB
    '''

    prt.write("WFE.WFEapplications.initialliseDB : ============================================\n")
    prt.write("WFE.WFEapplications.initialliseDB :  Intiallising DB for depID = " + str(depositionID) + "\n")
    prt.write("WFE.WFEapplications.initialliseDB : ============================================\n")

    if (prt == sys.stderr):
        log = sys.stderr
    else:
        processLog = "log/status_" + str(depositionID) + "_" + WorkflwClassID + "_" + WorkflowInstanceID + ".log"
        log = open(processLog, "w")

    if debug > 0:
        process = ProcessRunner(True, log)
    else:
        process = ProcessRunner(False, log)

    process.setAction("status")

    if input is None:
        prt.write("WFE.WFEapplications.initialliseDB :  Requires input object \n")
        sys.exit(0)

    for key, value in input.iteritems():
        if debug > 0:
            prt.write("WFE.WFEapplications.initialliseDB :  setting input " + str(key) + str(value.getReferenceType()) + "\n")
            prt.write("WFE.WFEapplications.initialliseDB :  setting input " + str(key) + str(value) + "\n")
        process.setInput("src", value)

    wfoOut = WfDataObject()
    wfoOut.setContainerTypeName('dict')
    wfoOut.setValueTypeName('string')
    process.setOutput("dst", wfoOut)

    if not process.preCheck():
        prt.write("WFE.WFEapplications.initialliseDB  : failed to setup process\n")

    if not process.run():
        prt.write("WFE.WFEapplications.initialliseDB : failed to run process\n")

    dataDict = wfoOut.getValue()
    if dataDict is None:
        print " There is no dataDictionary "
        exit(0)

    depDB = {}
    depDB["DEP_SET_ID"] = depositionID
    depDB["PDB_ID"] = '????'
    if 'accessions' in dataDict:
        acc = dataDict['accessions']
        depDB["PDB_ID"] = '????'
        if acc is not None:
            accPDB = acc['PDB']
            if accPDB is not None:
                if len(accPDB) > 0:
                    depDB["PDB_ID"] = accPDB[0]

    if 'recvd_initial_deposition_date' in dataDict:
        depDB['INITIAL_DEPOSITION_DATE'] = dataDict['recvd_initial_deposition_date']
    else:
        # JDW JDW
        today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        #depDB['INITIAL_DEPOSITION_DATE'] = 'unknown'
        depDB['INITIAL_DEPOSITION_DATE'] = today
    if 'deposit_site' in dataDict:
        depDB['DEPOSIT_SITE'] = dataDict['deposit_site']
    else:
        depDB['DEPOSIT_SITE'] = 'unknown'
    if 'process_site' in dataDict:
        depDB['PROCESS_SITE'] = dataDict['process_site']
    else:
        depDB['PROCESS_SITE'] = 'unknown'
    if 'status_code' in dataDict:
        depDB['STATUS_CODE'] = dataDict['status_code']
    else:
        depDB['STATUS_CODE'] = "PROC"
    print "******* OVERWRITE OF STATUS CODE to PROC ***************"
    depDB['STATUS_CODE'] = "PROC"
    if 'annotator_initials' not in dataDict or dataDict['annotator_initials'] == 'UNASSIGNED':
        depDB["ANNOTATOR_INITIALS"] = 'unknown'
    else:
        depDB["ANNOTATOR_INITIALS"] = dataDict['annotator_initials']
        print "******* OVERWRITE OF ANNOTATOR INITIALS TO AN *******"
        depDB["ANNOTATOR_INITIALS"] = 'unknown'
    if 'author_release_status_code' not in dataDict:
        depDB["AUTHOR_RELEASE_STATUS_CODE"] = 'HPUB'
    else:
        depDB["AUTHOR_RELEASE_STATUS_CODE"] = dataDict['author_release_status_code']
    depDB["TITLE"] = dataDict['title'].replace("'", " ")

    if 'audit_author' in dataDict:
        auth = dataDict['audit_author']
    else:
        auth = "unknown"

    if auth is not None:
        if isinstance(auth, list):
            depDB["AUTHOR_LIST"] = ""
            depDB["AUTHOR_LIST"] = " ".join(["%s," % a for a in auth])
        elif isinstance(auth, str):
            depDB["AUTHOR_LIST"] = auth
        else:
            print " Unknown type of author list " + str(type(auth))
        depDB["AUTHOR_LIST"] = depDB["AUTHOR_LIST"].replace("'", " ")
        print depDB["AUTHOR_LIST"]
    else:
        depDB["AUTHOR_LIST"] = "unknown"
    #
    depDB["EXP_METHOD"] = dataDict['exp_method']
    if (depDB["EXP_METHOD"].find('NMR') >= 0):
        if 'status_code_nmr' in dataDict:
            depDB["STATUS_CODE_EXP"] = dataDict['status_code_nmr']
        else:
            depDB["STATUS_CODE_EXP"] = 'Unknown'
    elif (depDB["EXP_METHOD"].find('EM') >= 0):
        if 'status_code_em' in dataDict:
            depDB["STATUS_CODE_EXP"] = dataDict['status_code_em']
        else:
            depDB["STATUS_CODE_EXP"] = 'Unknown'
    else:
        if 'status_code_sf' in dataDict:
            depDB["STATUS_CODE_EXP"] = dataDict['status_code_sf']
        else:
            depDB["STATUS_CODE_EXP"] = 'Unknown'
    if 'full_name_of_center' in dataDict:
        depDB["SG_CENTER"] = dataDict['full_name_of_center']
    else:
        depDB["SG_CENTER"] = 'Unknown'

    if DBstatusAPI.exist(depDB):
        # then we do nothing - since this workflow does not modify the depostion
        constDict = {}
        constDict["DEP_SET_ID"] = depositionID
        DBstatusAPI.saveObject(depDB, 'update', constDict)
        pass
    else:
        DBstatusAPI.saveObject(depDB, 'insert')
        if debug > 0:
            prt.write("WFE.WFEapplications.initialliseDB : done insert data object in DB\n")
    #
    classDB = {}
    classDB["WF_CLASS_ID"] = WorkflowClassID
    classDB["WF_CLASS_FILE"] = metaData.getName()
    classDB["WF_CLASS_NAME"] = metaData.getName()
    classDB["TITLE"] = metaData.getDescription()
    classDB["AUTHOR"] = metaData.getAuthor()
    classDB["VERSION"] = metaData.getVersionMajor() + metaData.getVersionMinor()

    if DBstatusAPI.exist(classDB):
        if debug > 0:
            prt.write("WFE.WFEapplications.initialliseDB : updating the workflow class\n")
        # do nothing as we have run this workflow
        # We need to review the version to see if it is the same - how do we
        #   handle a new version of the workflow-class ?
        pass
        constDict = {}
        constDict['WF_CLASS_ID'] = WorkflowClassID
        DBstatusAPI.saveObject(classDB, 'update', constDict)
    else:
        if debug > 0:
            prt.write("WFE.WFEapplications.initialliseDB : creating the workflow class object\n")
        DBstatusAPI.saveObject(classDB, 'insert')

    instDB = {}
    instDB['WF_INST_ID'] = WorkflowInstanceID
    instDB['WF_CLASS_ID'] = WorkflowClassID
    instDB['DEP_SET_ID'] = depositionID
    instDB['STATUS_TIMESTAMP'] = datetime.datetime.utcnow()
    DBstatusAPI.updateStatus(instDB, "init")

    # and also initialise the wf_instance_last table
    sql = "update wf_instance_last set status_timestamp=" + str(getTimeNow()) + ", inst_status='init' where dep_set_id = '" + depositionID + "'"
    print sql
    ok = DBstatusAPI.runUpdateSQL(sql)
    if ok < 1:
        print " CRITICAL : failed to update wf_instance_last table"

    if log != sys.stderr:
        log.close()


def WFEisThereALigand(depID):

    wfoInp = WfDataObject()
    wfoInp.setDepositionDataSetId(self.__depDataSetId)
    wfoInp.setStorageType('archive')
    wfoInp.setContentTypeAndFormat('chem-comp-assign', 'pdbx')
    wfoInp.setVersionId('latest')
    #
    dP = wfoInp.getDirPathReference()
    fP = wfoInp.getFilePathReference()
    vN = wfoInp.getFileVersionNumber()
    self.__lfh.write("Input directory path: %s\n" % dP)
    self.__lfh.write("Input file      path: %s\n" % fP)
    self.__lfh.write("Input file   version: %d\n" % vN)
    #
    # Selection specification -
    wfoInp.setSelectCategoryName('pdbx_entry_info')
    wfoInp.addSelectAttributeName('status')

    wfoOut = WfDataObject()
    wfoOut.setContainerTypeName('list')
    wfoOut.setValueTypeName('string')
    #
    #
    pR = ProcessRunner()
    ok = pR.setAction('fetch')
    self.__lfh.write("setAction: %r\n" % ok)

    pR.setInput("src", wfoInp)
    pR.setOutput("dst", wfoOut)
    ok = pR.preCheck()
    self.__lfh.write("Precheck status: %r\n" % ok)
    print "Precheck status: %r\n" % ok
    ok = pR.run()
    self.__lfh.write("Run status: %r\n" % ok)
    print "Run status: %r\n" % ok
    statusList = wfoOut.getValue()
    self.__lfh.write("Assignment status list : %r\n" % statusList)
    print "Assignment status list : %r\n" % statusList


def WFEreleaseStatus(DBstatusAPI, depID, status):

    sql = "update deposition set author_release_status_code = '" + status + "' where dep_set_id = '" + depID + "'"
    ok = DBstatusAPI.runUpdateSQL(sql)


def WFEsetAnnotator(DBstatusAPI, depID, annotator):

    sql = "update deposition set annotator_initials = '" + annotator + "' where dep_set_id = '" + depID + "'"
    ok = DBstatusAPI.runUpdateSQL(sql)


def WFErandomAnnotator(DBstatusAPI, depID):

    sql = "select initials from da_users where length(user_name) = 2"
    allList = DBstatusAPI.runSelectSQL(sql)

    n = random.randrange(1, len(allList))

    annotator = allList[n][0]

    sql = "update deposition set annotator_initials = '" + annotator + "' where dep_set_id = '" + depID + "'"
    ok = DBstatusAPI.runUpdateSQL(sql)


def WFEexception(DBstatusAPI, depID):

    WFEsetCommunication(DBstatusAPI, "EXCEPTION", "EXCEPTION", depID)


def WFEfinished(DBstatusAPI, depID):

    WFEsetCommunication(DBstatusAPI, "FINISHED", "FINISHED", depID)


def WFEsetCommunication(DBstatusAPI, status, activity, depID):

    timeNow = getTimeNow()
    sql = "update communication set status = '" + str(status) + "', activity = '" + str(activity) + "', actual_timestamp = " + \
        str(timeNow) + " where dep_set_id  = '" + str(depID) + "'"

    ok = DBstatusAPI.runUpdateSQL(sql)

    if ok == 1:
        print "Set the communication to " + str(status) + " for dep_set_id = " + str(depID)
    else:
        print "Failed to set the communication table to " + str(status) + " for dep_set_id = " + str(depID)


def WFEtestFile(inputs, outputs, debug=2, prt=sys.stderr):

    input = None
    output = None
    if not inputs is None:
        for key, value in inputs.iteritems():
            if debug > 1:
                pass
                prt.write("WFE.WFEapplications.WFEtestFile :  setting input " + str(key) + " " + str(value.getReferenceType()) + "\n")
                prt.write("WFE.WFEapplications.WFEtestFile :  setting input " + str(key) + " " + str(value) + "\n")
            input = value
    if not outputs is None:
        for key, value in outputs.iteritems():
            if debug > 1:
                pass
                prt.write("WFE.WFEapplications.WFEtestFile :   setting output " + str(key) + " " + str(value) + "\n")
            output = value

    if input is None:
        prt.write("WFE.WFEapplications.WFEtestFile :  Catastrophic WF error missing input ")
    if output is None:
        prt.write("WFE.WFEapplications.WFEtestFile :  Catastrophic WF error missing output ")

    fp = input.getFilePathReference()
    if input.getFilePathExists(fp):
        output.data = "true"
    else:
        output.data = "false"


def getInitialDate(depid):

    ret = 'error'
    if depid is not None:
        wfApi = WfDbApi(verbose=True)
        sql = "select initial_deposition_date from deposition where dep_set_id = '" + depid + "'"
        dat = wfApi.runSelectSQL(sql)
        if dat is not None and len(dat) > 0:
            for r in dat:
                ret = r[0]

    return ret


def getAnnotatorInitials(depid):

    ret = 'error'
    if depid is not None:
        wfApi = WfDbApi(verbose=True)
        sql = "select annotator_initials from deposition where dep_set_id = '" + depid + "'"
        dat = wfApi.runSelectSQL(sql)
        if dat is not None and len(dat) > 0:
            for r in dat:
                ret = r[0]

    return ret


def getStatusCode(depid):

    ret = 'error'
    if depid is not None:
        wfApi = WfDbApi(verbose=True)
        sql = "select status_code from deposition where dep_set_id = '" + depid + "'"
        dat = wfApi.runSelectSQL(sql)
        if dat is not None and len(dat) > 0:
            for r in dat:
                ret = r[0]

    return ret


def getStatusCodeEMDB(depid):

    ret = 'error'
    if depid is not None:
        wfApi = WfDbApi(verbose=True)
        sql = "select status_code_emdb from deposition where dep_set_id = '" + depid + "'"
        dat = wfApi.runSelectSQL(sql)
        if dat is not None and len(dat) > 0:
            for r in dat:
                ret = r[0]

    return ret


def setStatusCode(depID, code):

    valid = ['PROC', 'AUTH', 'DEP', 'VAL', 'HPUB', 'REL', 'REPL', 'HOLD', 'OBS', 'WAIT', 'WDRN', 'REFI']

    if code not in valid:
        return False, "Invalid status code"

    try:
        wfApi = WfDbApi(verbose=True)
        sql = "update deposition set status_code = '" + str(code) + "' where dep_set_id = '" + depID + "'"
        n = wfApi.runUpdateSQL(sql)
        if n == 0:
            return False, "Update did not occur - possible invalid dep_set_id or no change to code "
        else:
            return True, "Status updated"
    except Exception as e:
        return False, "Exception : " + str(e)


def getLockingCode(depid):

    ret = 'error'
    try:
        if depid is not None:
            wfApi = WfDbApi(verbose=True)
            sql = "select locking from deposition where dep_set_id = '" + depid + "'"
            dat = wfApi.runSelectSQL(sql)
            if dat is not None and len(dat) > 0:
                for r in dat:
                    ret = r[0]
            else:
                return "badID"
    except Exception as e:
        return ret + str(e)

    return ret


def XinsertInitialStateDB(DBstatusAPI, depID, debug=0, prt=sys.stderr):
    '''
      Method to insert an initial state for the instance data
      This is not combined with the reset below as this is a critical
      failure except on load - never call this from the engine !
    '''

    sql = "select count(*) from wf_instance where dep_set_id = '" + depID + "'"
    list = DBstatusAPI.runSelectSQL(sql)

    if list is not None:
        for row in list:
            if row[0] > 0:
                print " WFEapplications.insertInitialStateDB : Tried to insert into the instance table that exists "
                sys.exit(0)

    now = getTimeNow()

    sql = "insert into wf_instance (wf_inst_id, wf_class_id, dep_set_id, owner, inst_status, status_timestamp) values ('W_001','Annotate','" + \
        depID + "','Annotation.bf.xml','init','" + str(now) + "')"
    ok = DBstatusAPI.runInsertSQL(sql)
    if int(ok) == 1:
        print "Inserted 1 row into wf_instance for " + str(depID)

    sql = "insert into wf_instance_last (wf_inst_id, wf_class_id, dep_set_id, owner, inst_status, status_timestamp) values ('W_001','Annotate','" + \
        depID + "','Annotation.bf.xml','init','" + str(now) + "')"
    ok = DBstatusAPI.runInsertSQL(sql)
    if int(ok) == 1:
        print "Inserted 1 row into wf_instance_last for " + str(depID)


def XresetInitialStateDB(DBstatusAPI, depID, debug=0, prt=sys.stderr):
    '''
      Method to reset a deposition back to init state by setting the owner, status and class
    '''

    # select ordinal from wf_instance where dep_set_id = 'D_057171'  order by status_timestamp desc limit 1;
    # get the last row in the instance table for this ID
    sql = "select ordinal from wf_instance where dep_set_id = '" + str(depID) + "'  order by status_timestamp desc limit 1"
    #sql = "select ordinal from wf_instance where (wf_class_id = 'Annotate')  and (dep_set_id = '" + str(depID) + "')  order by status_timestamp desc limit 1"
    allList = DBstatusAPI.runSelectSQL(sql)

    if allList is not None:
        for allRow in allList:
            ordinal = allRow[0]
            print "Ordinal found for ID " + str(depID) + " , ordinal = " + str(ordinal)
            sql = "update wf_instance set owner = 'Annotation.bf.xml', wf_class_id = 'Annotate' , inst_status = 'init' where ordinal = " + str(ordinal)
            ok = DBstatusAPI.runUpdateSQL(sql)
            # update the wf_instance_last table
            sql = "update wf_instance_last set owner = 'Annotation.bf.xml', wf_class_id = 'Annotate' , inst_status = 'init' where dep_set_id = '" + str(depID) + "'"
            ok = DBstatusAPI.runUpdateSQL(sql)
            if int(ok) == 1:
                print "Updated 1 row to initialise status DB"
            else:
                print "DID NOT UPDATE status"
