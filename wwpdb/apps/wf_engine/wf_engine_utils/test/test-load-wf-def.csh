#!/bin/tcsh
#
# File:  test-load-wf-def.csh
# Date:  27-Jul-2015 jdw
#
#        Load a workflow definition into the status.wf_class_dict table.
#
../tasks/WFTaskRequestExec.py  --report=wf_defs
../tasks/WFTaskRequestExec.py --load_wf_def_file=wf_op_placeholder.xml
../tasks/WFTaskRequestExec.py --load_wf_def_file=wf_op_annot-main_fs_archive.xml
../tasks/WFTaskRequestExec.py  --report=wf_defs

