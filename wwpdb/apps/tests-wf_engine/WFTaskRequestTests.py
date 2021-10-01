# pylint: disable=no-value-for-parameter
# XXXXXXX Needs to be redone due to code changes

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
import time
import unittest
import traceback
import logging
from wwpdb.apps.wf_engine.wf_engine_utils.tasks.WFTaskRequest import WFTaskRequest
from wwpdb.utils.config.ConfigInfo import getSiteId

logger = logging.getLogger(__name__)


@unittest.skip("Until test code adapted to code base")
class WFTaskRequestTests(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(WFTaskRequestTests, self).__init__(methodName)
        self.__lfh = sys.stderr
        self.__verbose = True

    def setUp(self):
        self.__lfh = sys.stderr
        self.__verbose = True
        self.__databaseName = 'status_test'
        self.__siteId = getSiteId()

    def tearDown(self):
        pass

    def testSchemaCreate(self):
        """Test case -  create table schema ---
        """
        startTime = time.time()
        logger.debug("Starting at %s", time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        try:
            wftr = WFTaskRequest(siteId=self.__siteId, verbose=self.__verbose, log=self.__lfh)
            wftr.setDataStore(dataStoreName=self.__databaseName)
            wftr.createDataStore()
        except Exception as _e:  # noqa: F841
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.time()
        logger.debug("Completed at %s (%.3f seconds)",
                     time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                     endTime - startTime)

    def testDeleteTransactions(self):
        """Test case -  request transactions
        """
        startTime = time.time()
        logger.debug("Starting at %s",
                     time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        try:
            wftr = WFTaskRequest(siteId=self.__siteId, verbose=self.__verbose, log=self.__lfh)
            wftr.setDataStore(dataStoreName=self.__databaseName)
            #
            for depId in ['D_0000000000', 'D_0000000001', 'D_0000000002', 'D_0000000003', 'D_0000000004', 'D_0000000005']:
                _ok = wftr.deleteDataSet(depSetId=depId)  # noqa: F841
            #
            # rdList = wftr.getStatus()
            # for rd in rdList:
            #     logger.debug(" +++ full status = %r", rd.items())

        except Exception as _e:  # noqa: F841
            logger.exception("Failure")
            self.fail()

        endTime = time.time()
        logger.debug("Completed at %s (%.3f seconds)\n",
                     time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                     endTime - startTime)

    def testTransactions(self):
        """Test case -  request transactions
        """
        startTime = time.time()
        logger.debug("Starting %s",
                     time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        try:
            wftr = WFTaskRequest(siteId=self.__siteId, verbose=self.__verbose, log=self.__lfh)
            wftr.setDataStore(dataStoreName=self.__databaseName)
            #
            for depId in ['D_0000000001', 'D_0000000002', 'D_0000000003', 'D_0000000004', 'D_0000000005']:
                wftr.addDataSet(depSetId=depId, hostName='localhost', wfInstId='W_001', wfClassId='Annotate', wfClassFileName='annotate.xml')
                if False:  # pylint: disable=using-constant-test
                    continue
                for _ii in range(1, 5):
                    # rdL = wftr.getTaskStatus(depId=depId)
                    # for rd in rdL:
                    #     logger.debug(" +++ row (%s):  %r", depId, rd.items())
                    #
                    _ok = wftr.assignTask(depSetId=depId, hostName='localhost', wfInstId='W_002', wfClassId='Sequence', wfClassFileName='sequence.xml')  # noqa: F841
                    # rdL = wftr.getTaskStatus(depId=depId)
                    # for rd in rdL:
                    #     logger.debug(" +++ row (%s):  %r", depId, rd.items())

                    _ok = wftr.assignTask(depSetId=depId, hostName='localhost', wfInstId='W_003', wfClassId='Entity', wfClassFileName='entity.xml')  # noqa: F841
                    # rdL = wftr.getTaskStatus(depId=depId)
                    # for rd in rdL:
                    #     logger.debug(" +++ row (%s):  %r", depId, rd.items())
            #
            # rdL = wftr.getStatus()
            # for rd in rdL:
            #     logger.debug(" +++ row:  %r", rd.items())

        except Exception as _e:  # noqa: F841
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.time()
        logger.debug("Completed at %s (%.3f seconds)",
                     time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                     endTime - startTime)


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
    if True:  # pylint: disable=using-constant-test
        mySuite = createSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)
        #
        mySuite = transactionsSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)

        mySuite = deleteTransactionsSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)
