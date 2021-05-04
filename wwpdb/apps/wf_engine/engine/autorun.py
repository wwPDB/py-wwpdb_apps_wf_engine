from wwpdb.utils.wf.dbapi.DbApiUtil import DbApiUtil
from wwpdb.utils.config.ConfigInfo import ConfigInfo
import sys


class AutoRun(object):
    __queries = {
        "LAST_STATUS_AND_ORDINAL": f'''
                                select status, ordinal from communication where parent_dep_set_id = '{dep_id}' order by actual_timestamp desc limit 1
                                ''',
        "START_ANNOTATION_WORKFLOW": f'''
                                UPDATE communication set sender='WFM' receiver='WFE' dep_set_id='{dep_id}' wf_class_file= 'Annotation.bf.xml', 
                                command='runWF', status='pending', parent_dep_set_id='{dep_id}', parent_wf_class_id='Annotate' 
                                WHERE ordinal = f{ordinal}'''
    }

    def __init__(self, dep_id, site_id=None, verbose=False, log=sys.stderr):
        """

        """
        self.__lfh = log
        self.__verbose = verbose
        self.__siteId = site_id
        self.dep_id = dep_id
        self.__cI = ConfigInfo(self.__siteId)
        self.db_api = self.make_db_connection()
        self.current_status = None
        self.ordinal = None

    def make_db_connection(self):
        config_info = ConfigInfo(self.__siteId)

        db_server = config_info.get("SITE_DB_SERVER")
        db_host = config_info.get("SITE_DB_HOST_NAME")
        db_name = config_info.get("SITE_DB_DATABASE_NAME")
        db_user = config_info.get("SITE_DB_USER_NAME")
        db_pw = config_info.get("SITE_DB_PASSWORD")
        db_socket = config_info.get("SITE_DB_SOCKET")
        db_port = int(config_info.get("SITE_DB_PORT_NUMBER"))

        return DbApiUtil(dbServer=db_server, dbHost=db_host, dbName=db_name,
                         dbUser=db_user, dbPw=db_pw, dbSocket=db_socket, dbPort=db_port,
                         verbose=self.__verbose, log=self.__lfh)

    def update_status_and_ordinal(self):
        sql = self.__queries['SELECT_COMMUNICATION'].format(dep_id=self.dep_id)
        rows = self.db_api.runSelectSQL(sql)
        if rows:
            self.current_status = rows.get('status', None)
            self.current_ordinal = rows.get('ordinal', None)
        else:
            self.__lfh("Couldn't get Status of current workflow")

    def run_annotation(self):
        sql = self.__queries['START_ANNOTATION_WORKFLOW'].format(dep_id=self.dep_id, ordinal=self.ordinal)
        ret = self.db_api.runUpdateSQL(sql)
        if ret != 'OK':
            self.__lfh('Annotation Workflow Started.')
        else:
            self.__lfh('Start Annotate workflow failed.')
