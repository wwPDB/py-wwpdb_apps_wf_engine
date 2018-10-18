import sys
from wwpdb.apps.wf_engine.Tests.ServerCheck import ServerCheck


def main(argv):
    sm = ServerCheck()
    sm.check()

if __name__ == "__main__":
    main(sys.argv[1:])
