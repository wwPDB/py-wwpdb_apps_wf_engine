
import sys

from wwpdb.apps.wf_engine.Maintenance.ServerTransfer import ServerTransfer


def main(argv):

    st = ServerTransfer(verbose=True)

    me = st.getHostMe()
    dbHosts = st.getValidHosts()
    allHosts = st.getAllHosts()

    print("Name of this host (new host name) : " + str(me))

    print("Existing Valid Hosts - active servers :")

    for i in range(0, len(dbHosts)):
        print(" %d :  %r" % (i, dbHosts[i]))

    print("Existing Hosts - in database : (number, name ,number of )")
    for i in range(0, len(allHosts)):
        row = allHosts[i]
        print(" %d) %r :  %d" % (i, row[1], row[0]))

    whichHost = input(" Which number host do you want (0-%d) > " % (len(allHosts) - 1))

    try:
        whichHost = int(whichHost)

        if whichHost >= 0 and whichHost < len(allHosts):
            newHost = allHosts[whichHost]
            newHost = newHost[1]
            print("Transfering from %r -to-> %r" % (newHost, me))
            st.changeAllHost(newHost, me)
        else:
            print("RFTM")

    except Exception as e:
        print("Number please ! ", e)

if __name__ == "__main__":

    main(sys.argv[1:])
