##
# File: WFEngineImportsTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
##
"""Test cases for WFengine imports
"""

__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "peisach@rcsb.rutgers.edu"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.01"

import unittest

from wwpdb.apps.wf_engine.engine.CommandLineArgs import CommandLineArgs  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.EngineUtils import EngineUtils  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.ExternalTask import ExternalTask  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.InterpretDataObject import *  # noqa: F401,F403 pylint: disable=unused-wildcard-import,unused-import,wildcard-import
from wwpdb.apps.wf_engine.engine.ProcessManager import ProcessManager  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.ServerMonitor import ServerMonitor  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.SwitchTask import SwitchTask  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.WFEapplications import *  # noqa: F401,F403 pylint: disable=unused-wildcard-import,unused-import,wildcard-import
from wwpdb.apps.wf_engine.engine.WorkflowManager import WorkflowManager  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.WorkflowSession import WorkflowSession  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.dbAPI import dbAPI  # noqa: F401 pylint: disable=unused-import
from wwpdb.apps.wf_engine.engine.mainEngine import mainEngine  # noqa: F401 pylint: disable=unused-import


class ImportTests(unittest.TestCase):
    def setUp(self):
        pass

    def testInstantiate(self):
        pass


if __name__ == '__main__':
    unittest.main()
