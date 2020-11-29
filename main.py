import json
import sys

from nics import getNics
from diagnoze import diagnoze


def main():
    # main vars
    toDump = {}
    cfg = {}
    cfgPath = 'conf.json'

    ##########################
    # read config file

    def getCfg():
        try:
            with open("conf.json", "r") as cfgFile:
                cfg = json.load(cfgFile)

            if cfg != {}:
                print("config loaded")
            else:
                print("error: cfg file empty")
                quit()
        except:
            print("error: not cfg file found")

    ##########################

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
    getCfg()
    nics = getNics()
    addToDump("network interfaces", nics)

    # create output log file with all cached info about tests
    createDump()


if __name__ == "__main__":
    main()
