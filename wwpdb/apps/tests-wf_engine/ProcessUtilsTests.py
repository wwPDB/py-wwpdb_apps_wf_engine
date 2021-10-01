##
# File:    ProcessUtilsTests.py
# Author:  J. Westbrook
# Date:    12-Mar-2015
# Version: 0.001
#
# Updates:
#
# 12-Mar-2015 jdw  add process search methods
# 12-Mar-2015 jdw  add parent process id -
#
##
"""
Test cases for the process information utilities.

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

from wwpdb.apps.wf_engine.wf_engine_utils.process.ProcessUtils import ProcessUtils

logger = logging.getLogger(__name__)


class ProcessUtilsTests(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(ProcessUtilsTests, self).__init__(methodName)
        self.__lfh = sys.stderr
        self.__verbose = True

    def setUp(self):
        self.__lfh = sys.stderr
        self.__verbose = True

    def tearDown(self):
        pass

    def testProcessList(self):
        """Test case -  for listing process details and finding processes by feature
        """
        startTime = time.time()
        logger.info("Starting at %s",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        try:
            pU = ProcessUtils(verbose=self.__verbose, log=self.__lfh)
            pU.setDebug(flag=False)
            tL = [("username", "jwest", 'str_in'),
                  ("cmdline", "python", 'str_in'),
                  ("cmdline", "Frameworks", 'str_in'),
                  ("cpu_percent", 1, 'numb_gt'),
                  ("num_fds", 1, 'numb_gt')
                  ]
            for t in tL:
                pidL = pU.findProcesses(key=t[0], value=t[1], op=t[2])
                self.__lfh.write("ProcessUtilsTests.testProcessList() for  %r  process list length is %d\n" % (t, len(pidL)))
        except Exception as _e:  # noqa: F841
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.time()
        logger.info("Completed at %s (%.3f seconds)",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                    endTime - startTime)

    def testProcessChildren(self):
        """Test case -  for listing process details and finding processes by feature
        """
        startTime = time.time()
        logger.info("Starting at %s",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        try:
            pU = ProcessUtils(verbose=self.__verbose, log=self.__lfh)
            pidL = pU.findProcesses(key="username", value="jwest")
            self.__lfh.write("ProcessUtilsTests.testProcessChildren()  process list length is %d\n" % len(pidL))
            for pidTup in pidL:
                cL = pU.getChildren(pidTup[0])
                if len(cL) > 0:
                    self.__lfh.write("ProcessUtilsTests.testProcessChildren()) process %d has %d children\n" % (pidTup[0], len(cL)))
        except Exception as _e:  # noqa: F841
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.time()
        logger.info("Completed at %s (%.3f seconds)",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                    endTime - startTime)

    def testProcessWfeChildren(self):
        """Test case -  for listing wfe
        """
        startTime = time.time()
        logger.info("Starting at %s",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        myName = "WFEngineRunnerExec"
        try:
            pU = ProcessUtils(verbose=self.__verbose, log=self.__lfh)
            pidL = pU.findProcesses(key='cmdline', value=myName, op='str_in')
            self.__lfh.write("ProcessUtilsTests.testProcessChildren()  process list length is %d\n" % len(pidL))
            for pidTup in pidL:
                cL = pU.getChildren(pidTup[0])
                if len(cL) > 0:
                    self.__lfh.write("ProcessUtilsTests.testProcessChildren()) process %d has %d children\n" % (pidTup[0], len(cL)))
        except Exception as _e:  # noqa: F841
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.time()
        logger.info("Completed at %s (%.3f seconds)",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                    endTime - startTime)

    def testSystemInfo(self):
        """Test case -  system details --
        """
        startTime = time.time()
        logger.info("Starting at %s",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()))
        try:
            pU = ProcessUtils(verbose=self.__verbose, log=self.__lfh)
            dM = pU.getMemoryInfo()
            dC = pU.getCpuInfo()
            self.__lfh.write("+ProcessUtilsTests - cpuInfo    = %r\n" % dC.items())
            self.__lfh.write("+ProcessUtilsTests - memoryInfo = %r\n" % dM.items())
        except Exception as _e:  # noqa: F841
            traceback.print_exc(file=self.__lfh)
            self.fail()

        endTime = time.time()
        logger.info("Completed at %s (%.3f seconds)\n",
                    time.strftime("%Y %m %d %H:%M:%S", time.localtime()),
                    endTime - startTime)


def processInfoSuite():
    suiteSelect = unittest.TestSuite()
    suiteSelect.addTest(ProcessUtilsTests("testProcessList"))
    suiteSelect.addTest(ProcessUtilsTests("testProcessChildren"))
    suiteSelect.addTest(ProcessUtilsTests("testSystemInfo"))
    return suiteSelect


def processWfeSuite():
    suiteSelect = unittest.TestSuite()
    suiteSelect.addTest(ProcessUtilsTests("testProcessWfeChildren"))
    return suiteSelect


if __name__ == '__main__':
    #
    if False:  # pylint: disable=using-constant-test
        mySuite = processInfoSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)
        #
        mySuite = processWfeSuite()
        unittest.TextTestRunner(verbosity=2).run(mySuite)
        #
    mySuite = processWfeSuite()
    unittest.TextTestRunner(verbosity=2).run(mySuite)
