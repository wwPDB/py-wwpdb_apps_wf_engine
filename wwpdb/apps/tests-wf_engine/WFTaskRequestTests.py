##
# File:    WFTaskRequestTests.py
# Author:  J. Westbrook
# Date:    11-Apr-2014
# Version: 0.001
#
# Updates:
#
# 13-Apr-2014 jdw  verify the transactions database maintainance operations using test database 'status_test'.
#
##
"""
Test cases for the processing workflow management task requests.

These test database connections deferring to authentication details defined
in the environment.   See class MyDbConnect() for the environment requirements.

"""

__docformat__ = "restructuredtext en"
__author__ = "John Westbrook"
__email__ = "jwest@rcsb.rutgers.edu"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.01"

import sys
import os
import time
import unittest
import traceback
#from wwpdb.apps.wf_engine.wf_engine_utils.tasks.WFTaskRequest import WFTaskRequest


@unittest.skip("Until wf_engine code imported")
class WFTaskRequestTests(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(WFTaskRequestTests, self).__init__(methodName)
        self.__lfh = sys.stderr
        self.__verbose = True

    def setUp(self):
        self.__lfh = sys.stderr
        self.__verbose = True
        self.__databaseName = 'status_test'

    def tearDown(self):
        pass

    def testSchemaCreate(self):
        """Test case -  create table schema ---
        """
        startTime = time.clock()
        self.__lfh.write("\nStarting %s %s at %s\n" % (self.__class__.__name__,
                                                       sys._getframe().f_code.co_name,
                                                       time.strftime("%Y %m %d %H:%M:%S", time.localtime())))
        try:
            wftr = WFTaskRequest(verbose=self.__verbose, log=self.__lfh)
            wftr.setDataStore(dataStoreName=self.__databaseName)
            wftr.createDataStore()
        except:
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.clock()
        self.__lfh.write("\nCompleted %s %s at %s (%.3f seconds)\n" % (self.__class__.__name__,
                                                                       sys._getframe().f_code.co_name,
                                                                       time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                                                                       endTime - startTime))

    def testDeleteTransactions(self):
        """Test case -  request transactions
        """
        startTime = time.clock()
        self.__lfh.write("\nStarting %s %s at %s\n" % (self.__class__.__name__,
                                                       sys._getframe().f_code.co_name,
                                                       time.strftime("%Y %m %d %H:%M:%S", time.localtime())))
        try:
            wftr = WFTaskRequest(verbose=self.__verbose, log=self.__lfh)
            wftr.setDataStore(dataStoreName=self.__databaseName)
            #
            for depId in ['D_0000000000', 'D_0000000001', 'D_0000000002', 'D_0000000003', 'D_0000000004', 'D_0000000005']:
                ok = wftr.deleteDataSet(depId=depId)
            #
            rdList = wftr.getStatus()
            for rd in rdList:
                self.__lfh.write(" +++ full status = %r\n" % rd.items())

        except:
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.clock()
        self.__lfh.write("\nCompleted %s %s at %s (%.3f seconds)\n" % (self.__class__.__name__,
                                                                       sys._getframe().f_code.co_name,
                                                                       time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                                                                       endTime - startTime))

    def testTransactions(self):
        """Test case -  request transactions
        """
        startTime = time.clock()
        self.__lfh.write("\nStarting %s %s at %s\n" % (self.__class__.__name__,
                                                       sys._getframe().f_code.co_name,
                                                       time.strftime("%Y %m %d %H:%M:%S", time.localtime())))
        try:
            wftr = WFTaskRequest(verbose=self.__verbose, log=self.__lfh)
            wftr.setDataStore(dataStoreName=self.__databaseName)
            #
            for depId in ['D_0000000001', 'D_0000000002', 'D_0000000003', 'D_0000000004', 'D_0000000005']:
                wftr.addDataSet(depId=depId, hostName='localhost', wfInstId='W_001', wfClassId='Annotate', wfClassFileName='annotate.xml')
                if False:
                    continue
                for ii in range(1, 5):
                    rdL = wftr.getTaskStatus(depId=depId)
                    for rd in rdL:
                        self.__lfh.write(" +++ row (%s):  %r\n" % (depId, rd.items()))
                    #
                    ok = wftr.assignTask(depId=depId, hostName='localhost', wfInstId='W_002', wfClassId='Sequence', wfClassFileName='sequence.xml')
                    rdL = wftr.getTaskStatus(depId=depId)
                    for rd in rdL:
                        self.__lfh.write(" +++ row (%s):  %r\n" % (depId, rd.items()))

                    ok = wftr.assignTask(depId=depId, hostName='localhost', wfInstId='W_003', wfClassId='Entity', wfClassFileName='entity.xml')
                    rdL = wftr.getTaskStatus(depId=depId)
                    for rd in rdL:
                        self.__lfh.write(" +++ row (%s):  %r\n" % (depId, rd.items()))
            #
            rdL = wftr.getStatus()
            for rd in rdL:
                self.__lfh.write(" +++ row:  %r\n" % (rd.items()))

        except:
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.clock()
        self.__lfh.write("\nCompleted %s %s at %s (%.3f seconds)\n" % (self.__class__.__name__,
                                                                       sys._getframe().f_code.co_name,
                                                                       time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                                                                       endTime - startTime))


def createSuite():
    suiteSelect = unittest.TestSuite()
    suiteSelect.addTest(WFTaskRequestTests("testSchemaCreate"))
    return suiteSelect


def transactionsSuite():
    suiteSelect = unittest.TestSuite()
    suiteSelect.addTest(WFTaskRequestTests("testTransactions"))
    return suiteSelect


def deleteTransactionsSuite():
    suiteSelect = unittest.TestSuite()
    suiteSelect.addTest(WFTaskRequestTests("testDeleteTransactions"))
    return suiteSelect


if __name__ == '__main__':
    #
    if True:
        mySuite = createSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)
        #
        mySuite = transactionsSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)

        mySuite = deleteTransactionsSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)
