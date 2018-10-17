#!/bin/tcsh
#
#
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --report=summary
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --reload_status --file_source=archive
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --add
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --task=ANNOTATION_WF
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --report=deposition
../tasks/WFTaskRequestExec.py --dataset=D_1001200002  --report=summary
#
