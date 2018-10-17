#!/bin/tcsh
#
#source /wwpdb_da/da_top/scripts/env/runtime-environment.csh
#
##
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --delete_deposition
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --delete_workflow
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --reload_status --file_source=deposit
#
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --add --verbose --debug
../tasks/WFTaskRequestExec.py --dataset=D_1000000001  --task=PDBX2PDBX_DEP
../tasks/WFTaskRequestExec.py --report=summary
#

