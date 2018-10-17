#!/bin/tcsh
#
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=monitor       --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --add
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --task=TEST_MODULE_ACCESSOR_DECISION
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --report=summary
