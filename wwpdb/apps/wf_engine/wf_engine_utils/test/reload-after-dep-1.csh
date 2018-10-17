#!/bin/tcsh
#
#
#
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --report=summary
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --add
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1100200001  --report=summary
#
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --report=summary
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --add
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1100200002  --report=summary
#
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --report=summary
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --reload_status --file_source=deposit
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --add
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1100200003  --report=summary
#
