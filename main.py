import json
import sys

from nics import getNics
from diagnoze import diagnoze


def main():
    # main vars
    conductedTests = []
    toDump = {}

    ##########################

    # return flags passed to script or False if there is no flags
    def getFlags():
        args = sys.argv

        if len(args) - 1 > 0:
            args.pop(0)
            return args
        else:
            return False

    # adds test results to output log
    def addToDump(category: str, value):
        toDump[category] = value

    # creates output log file
    def createDump():
        with open("output.json", "w") as f:
            json.dump(toDump, f)
        return

    ######################################

    # always get NIC data and log them
    nics = getNics()
    addToDump("network interfaces", nics)

    # run functions when flag(s) is present
    flags = getFlags()
    if flags:
        if "-diag" in flags:
            conductedTests.append("diagnoze")
            results = diagnoze()
            addToDump("testResults", results)

        if "-ping" in flags:
            pass
    # if there is not flags ask user what kind of action do
    else:
        valid = False

        def choose():
            print("Please choose what do you want to do:",
                  "0) exit", "1) diagnoze network", "2) ping host", sep="\n")
            return input()

        select = choose()
        while not valid:
            if select == "0":  # exit
                break
            if select == "1":  # diagnoze
                results = diagnoze()
                addToDump("testResults", results)
                break
            elif select == "2":  # ping
                print("ping")
                break
            else:  # else -> ask again
                select = choose()
                continue

    # create output log file with all cached info about tests
    createDump()


if __name__ == "__main__":
    main()
