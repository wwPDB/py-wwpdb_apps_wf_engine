##
# File: WebServiceImportTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
##
"""Test cases for webservice - simply import everything to ensure imports work"""

__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "peisach@rcsb.rutgers.edu"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.01"

import unittest

from wwpdb.apps.wf_engine.wf_engine_utils.process.ProcessUtils import ProcessUtils
from wwpdb.apps.wf_engine.wf_engine_utils.run.MyLogger import MyLogger
from wwpdb.apps.wf_engine.wf_engine_utils.run.WFEngineRunner import WFEngineRunner
from wwpdb.apps.wf_engine.wf_engine_utils.tasks.WFTaskRequest import WFTaskRequest
from wwpdb.apps.wf_engine.wf_engine_utils.time.TimeStamp import TimeStamp


class ImportTests(unittest.TestCase):
    def setUp(self):
        pass

    def testInstantiate(self):
#        vc = ProcessUtils()
        vc = MyLogger()
        vc = WFEngineRunner()
        #vc = WFTaskRequest()
        vc = TimeStamp()

if __name__ == '__main__':
    unittest.main()


    
