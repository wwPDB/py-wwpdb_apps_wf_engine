#!/bin/tcsh
#
#source /wwpdb_da/da_top/scripts/env/runtime-environment.csh
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --add
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --report=summary
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --add
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000002  --report=summary
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --add
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000003  --report=summary
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --add
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000004  --report=summary
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --add
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000005  --report=summary
#
