##
# File:    MainEngineExceptionNodeTests.py
#
##
"""
Test cases for the instance status written when a workflow reaches an exception node.

"""

__docformat__ = "restructuredtext en"
__license__ = "Creative Commons Attribution 3.0 Unported"

import re
import unittest
from unittest import mock

from wwpdb.apps.wf_engine.engine import mainEngine as mainEngineModule


class MainEngineExceptionNodeTests(unittest.TestCase):
    def setUp(self):
        patchers = [
            mock.patch.object(mainEngineModule, "EngineUtils"),
            mock.patch.object(mainEngineModule, "TimeStamp"),
            mock.patch.object(mainEngineModule.sys, "exit", side_effect=SystemExit),
        ]
        self.engineUtils = patchers[0].start()
        for patcher in patchers[1:]:
            patcher.start()
        for patcher in patchers:
            self.addCleanup(patcher.stop)

        self.eUtil = self.engineUtils.return_value
        self.eUtil.exist.return_value = True
        self.eUtil.runUpdateSQL.return_value = 1

        self.engine = mainEngineModule.mainEngine()
        self.engine._mainEngine__depositionId = "D_1000000001"
        self.engine._mainEngine__wfClassId = "DepVal"
        self.engine._mainEngine__wfInstId = "W_002"

        self.task = mock.MagicMock()
        self.task.type = "Exception"
        self.task.name = "EX1"
        self.task.getDataReference.return_value = None

    def instanceStatuses(self):
        """Instance statuses written so far, in order."""
        sqls = [call.args[0] for call in self.eUtil.runUpdateSQL.call_args_list]
        return [re.search(r"inst_status='([^']*)'", sql).group(1) for sql in sqls]

    def reachExceptionNode(self):
        with self.assertRaises(SystemExit):
            self.engine._mainEngine__handleTask(self.task, [], 0)

    def testNodeAfterFailureKeepsException(self):
        """A run that already failed (e.g. a timeout) must stay 'exception' so the Workflow Manager shows it."""
        self.engine._mainEngine__setDBInstStatus("process", "exception", self.task)
        self.reachExceptionNode()
        self.assertEqual(self.instanceStatuses(), ["exception"])

    def testNodeWithoutEarlierFailureIsAborted(self):
        """A run that reaches the node with no earlier failure is still recorded as 'aborted'."""
        self.engine._mainEngine__setDBInstStatus("workflow", "running", self.task)
        self.reachExceptionNode()
        self.assertEqual(self.instanceStatuses(), ["running", "aborted"])

    def testNodeAfterRecoveryIsAborted(self):
        """An earlier failure that was later replaced by another status does not hold the node back."""
        self.engine._mainEngine__setDBInstStatus("process", "exception", self.task)
        self.engine._mainEngine__setDBInstStatus("workflow", "running", self.task)
        self.reachExceptionNode()
        self.assertEqual(self.instanceStatuses(), ["exception", "running", "aborted"])

    def testNodeTaskStatusIsAborted(self):
        """The node's own task row is 'aborted' whether or not the run had failed."""
        self.engine._mainEngine__setDBInstStatus("process", "exception", self.task)
        self.reachExceptionNode()
        taskModes = [call.args[1] for call in self.eUtil.updateStatus.call_args_list if "TASK_NAME" in call.args[0]]
        self.assertEqual(taskModes[-1], "aborted")


if __name__ == "__main__":
    unittest.main()
