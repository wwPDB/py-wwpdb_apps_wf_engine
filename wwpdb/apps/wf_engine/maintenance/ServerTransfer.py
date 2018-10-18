##
# File:  ServerTransfer.py
# Date:
#
#        Old untested example to reassign hosts --   jdw
# #

import sys
import socket
import time

from wwpdb.api.status.dbapi.WFEtime import getTimeNow
from wwpdb.api.status.dbapi.WfDbApi import WfDbApi


class ServerTransfer(object):

    def __init__(self, connection=None, shortResponse=100, longResponse=600, sleepTime=5, verbose=False):

        if not connection:
            connection = WfDbApi(verbose=True)

        self.wfCon = connection
        self.hostname = socket.gethostname()
        self.shortResponse = shortResponse
        self.longResponse = longResponse
        self.sleepTime = sleepTime
        self.verbose = verbose

    def changeAllHost(self, fromHost, toHost):

        sql = "update communication set host = '" + str(toHost) + "' where host = '" + str(fromHost) + "'"
        ok = self.wfCon.runUpdateSQL(sql)
        if ok > 0:
            print "Number of hostname changes : " + str(ok)
        else:
            print "No hosts transfered"

        return ok

    def getHostMe(self):

        return self.hostname

    def getValidHosts(self):

        ret = []
        sql = "select hostname from engine_monitoring"
        rows = self.wfCon.runSelectSQL(sql)

        for row in rows:
            ret.append(row[0])

        return ret

    def getAllHosts(self):

        sql = "select count(1),host from communication group by host order by host"
        rows = self.wfCon.runSelectSQL(sql)
        if self.verbose:
            print "getAllHosts : " + str(rows)

        return rows

    def getContention(self, host):

        sql = "select total_physical_mem,physical_mem_usage,cached,buffers from engine_monitoring where hostname = '" + str(host) + "'"

        rows = self.wfCon.runSelectSQL(sql)
        if rows is not None and len(rows) > 0:
            for row in rows:
                totalPhysical = row[0]
                physical = row[1]
                cache = row[2]
                buffers = row[3]
                break
        else:
            return 0.0

        try:
            ret = 100.0 * float(physical - buffers - cache) / float(totalPhysical)
            if self.verbose:
                print "Contention = " + str(ret)
            return ret
        except:
            return 0.0

    def StealControl(self, ordinal):
        '''
           method to update the communication table with a host name of this server
           this then redefines the working host to this machine
        '''

        try:
            timeNow = getTimeNow()
            # set the time now so we don't get this stolen by another server and get bouncing
            sql = "update communication set host = '" + str(self.hostname) + "' , actual_timestamp = " + str(timeNow) + " where ordinal = " + str(ordinal)
            if self.verbose:
                print "StealControl " + str(sql)
            ok = self.wfCon.runUpdateSQL(sql)
            if ok > 0:
                print " Servertransfer : Updated ordinal = " + str(ordinal)
        except Exception as e:
            print "Exception : StealControl " + str(e)

    def pingDBforStale(self):
        '''
          Get any dep_set_id that have a stale pending status
          Test for memory contention to see if the computer might be paging
          return the row ordinal or zero
        '''

        try:
            timeNow = getTimeNow()

            # Has any server engine that is not the one on this host failed to respond ?
            stat = "PENDING"
            # test       stat = "EXCEPTION"
            sql = "select ordinal,host,actual_timestamp from communication where UPPER(status) = '" + str(stat) + "' and host <> '" + str(
                self.hostname) + "' and (" + str(timeNow) + " - actual_timestamp)  > " + str(self.shortResponse) + " order by actual_timestamp desc limit 1"

            if self.verbose:
                print "pingDBSQL " + str(sql)

            rows = self.wfCon.runSelectSQL(sql)
            if self.verbose:
                print "Query Return  " + str(rows)

            if rows is not None and len(rows) > 0:
                # yes there is one at least
                for row in rows:
                    if self.verbose:
                        self.printHowOld(timeNow - row[2])
                    contention = self.getContention(row[1])
                    if contention > 80:
                        # maybe the computer is paging and heart beat has stopped
                        if timeNow - row[2] > self.longResponse:
                            # now we are worried
                            return row[0]
                    else:
                        return row[0]
        except Exception as e:
            print "Exception : pingDBforStayle " + str(e)

        return 0

    def printHowOld(self, seconds):

        min = int(seconds) / 60
        if min == 0:
            print " Stale = " + str(seconds) + " sec"
        else:
            sec = int(seconds) % min
            hour = min / 60
            if hour == 0:
                print " Stale = " + str(min) + ":" + str(sec) + " m:s"
            else:
                min = min % hour
                print " Stale = " + str(hour) + ":" + str(min) + ":" + str(sec) + " h:m:s"


def main(argv):

    st = ServerTransfer(verbose=False)

    while True:
        ordinal = st.pingDBforStale()
        print " Ping " + str(ordinal)
        if ordinal > 0:
            st.StealControl(ordinal)

        time.sleep(5)


if __name__ == "__main__":

    main(sys.argv[1:])
