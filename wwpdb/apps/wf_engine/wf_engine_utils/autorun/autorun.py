from wwpdb.apps.workmanager.db_access.StatusDbApi import StatusDbApi


def get_status(depid, this_site):
    sdb = StatusDbApi(this_site, verbose=False)
    com_status = sdb.getCommandStatus(depositionid=depid)
    return com_status


def run_annotation(depid, this_site):
    sdb = StatusDbApi(this_site, verbose=False)
    msg = sdb.insertCommunicationCommand(depositionid=depid, instid="W_001", classid="Annotate", command="runWF",
                                         classname="Annotation.bf.xml", dataversion='')
    return msg
