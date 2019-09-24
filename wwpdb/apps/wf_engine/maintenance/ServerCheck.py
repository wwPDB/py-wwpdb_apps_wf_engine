import time
from wwpdb.api.facade.ConfigInfo import ConfigInfo
from wwpdb.api.status.dbapi.DbConnection import DbConnection
from wwpdb.api.status.dbapi.DbCommand import DbCommand
from wwpdb.api.status.dbapi.WFEtime import getTimeNow
from email.MIMEText import MIMEText


class ServerCheck():

    '''
      Check all the active DB for activity and email errors
    '''

    def __init__(self):

        self.emails = ['jwest@rcsb.rutgers.edu']
        self.siteIDs = ['WWPDB_DEPLOY_INTERNAL_RU', 'WWPDB_DEPLOY_VALSRV_RU', 'WWPDB_DEPLOY', 'WWPDB_DEPLOY_TEST', 'WWPDB_DEPLOY_PRODUCTION_RU']

    def check(self):

        while True:
            for siteID in self.siteIDs:
                print(" Checking " + siteID)
                config = ConfigInfo(siteId=siteID)

                con = self.getConnection(config)

                self.getHosts(siteID)

                print(" ")
                self.closeConnection()
            time.sleep(600)

    def getConnection(self, cI):
        '''
          manual connection
        '''

        dbServer = cI.get("SITE_DB_SERVER")
        dbHost = cI.get("SITE_DB_HOST_NAME")
        dbName = cI.get("SITE_DB_DATABASE_NAME")
        dbUser = cI.get("SITE_DB_USER_NAME")
        dbPw = cI.get("SITE_DB_PASSWORD")
        dbPort = int("%s" % cI.get("SITE_DB_PORT_NUMBER"))

        self.myDb = DbConnection(dbServer=dbServer, dbHost=dbHost, dbName=dbName, dbUser=dbUser, dbPw=dbPw, dbPort=dbPort)

        self.dbcon = self.myDb.connect()
        self.db = DbCommand(self.dbcon)

    def closeConnection(self):

        self.myDb.close(self.dbcon)

    def getHosts(self, siteID):

        sql = 'select hostname,status_timestamp,total_physical_mem,physical_mem_usage,cached,buffers,cpu_number,cpu_usage from engine_monitoring'

        list = self.db.runSelectSQL(sql)
        if list is None:
            return None

        timeNow = getTimeNow()
        for row in list:
            if timeNow - row[1] > 60:
                print(" ERROR : very timestamp from host %s , delay = %8.2f" % (row[0], timeNow - row[1]))
                self.sendHelpEmails('WFdaemon response error ' + str(row[0]), 'WFdaemon on ' + str(row[0]) + ' has a response time > 60 seconds for SITE-ID = ' + str(siteID))
            else:
                if timeNow - row[1] > 10:
                    print(" Warning : stale timestamp from host %s , delay = %8.2f" % (row[0], timeNow - row[1]))
            if row[2] > 0:
                # available physical memory is that used - buffers and cache which are available to use
                # print " test : host = %s,  total =  %s , used = %s,  buffers = %s,
                # cached = %s , fraction = %8.2f" % (row[0] , row[2] , row[3] , row[4] ,
                # row[5], (row[3] - row[4] - row[5]) / row[2])
                if (row[3] - row[4] - row[5]) / row[2] > 0.9:
                    print(" ERROR : Physical memory usage very large on host %s , fraction = %8.2f" % (row[0], row[3] / (row[2] - row[4] - row[5])))
                    self.sendHelpEmails('High memory usage on ' +
                                        str(row[0]), 'High physical memory usage on ' +
                                        str(row[0]) +
                                        ' for SITE-ID = ' +
                                        str(siteID) +
                                        ' has a fraction of %8.2f memory usage' %
                                        (row[3] /
                                            (row[2] -
                                             row[4] -
                                             row[5])))
                else:
                    if (row[3] - row[4] - row[5]) / row[2] > 0.5:
                        print(" Warning : Physical memory usage large on host %s , fraction = %8.2f" % (row[0], row[3] / (row[2] - row[4] - row[5])))
            if row[7] / row[6] > 0.8:
                print(" ERROR : CPU usage very large on host %s , nCPU = %d, Usage  = %8.2f" % (row[0], row[4], row[5]))
                self.sendHelpEmails('CPU usage on ' +
                                    str(row[0]), 'CPU usage on ' +
                                    str(row[0]) +
                                    ' for SITE-ID = ' +
                                    str(siteID) +
                                    ' has usage %8.2f out of %d' %
                                    (row[4], row[5]))
            else:
                if row[7] / row[6] > 0.5:
                    print(" Warngin : CPU usage large on host %s , nCPU = %d, Usage  = %8.2f" % (row[0], row[4], row[5]))

    def sendHelpEmails(self, subject, message):

        for email in self.emails:
            self.sendHelpEmail(email, subject, message)

    def sendHelpEmail(self, email, subject, message):

        import smtplib

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'noreply@wwpdb.org'
        msg['To'] = email

         # Send the message via our own SMTP server, but don't include the
         # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail('noreply@wwpdb.org', [email], msg.as_string())
        s.quit()
