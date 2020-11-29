import json
import sys
import concurrent.futures
import time

from nics import getNics
from diagnoze import diagnoze


def main():
    # main vars
    toDump = {}
    cfg = {}
    cfgPath = 'conf.json'
    dumpPath = 'output.json'

    ########################## UTILITY ##########################

    # read config file
    def getCfg():
        try:
            with open(cfgPath, "r") as cfgFile:
                content = json.load(cfgFile)

            if content != {}:
                print("config loaded")
                print("cfg: ", content)
                return content
            else:
                print("error: cfg file empty")
                quit()
        except:
            print("error: not cfg file found")

    # adds test results to output log
    def addToDump(category: str, value):
        toDump[category] = value

    # creates output log file
    def createDump():
        try:
            with open(dumpPath, "w") as f:
                json.dump(toDump, f)
            return True
        except:
            return False

    ############################ INIT ############################

    cfg = getCfg()  # fetch cfg data from file
    nics = getNics()  # fetch network interface data
    addToDump("network interfaces", nics)
    # print(nics)

    ###########################

    def TestHandler(targetName, target):
        results = {}
        # if type(target) is list and len(target) > 1:
        #     for i in range(0, len(target) - 1):
        #         results[target[i]] = diagnoze(target[i])
        # else:
        results[targetName] = diagnoze(target)

        print(results[targetName])
        return results

    if 'selfDiagnoze' in cfg:
        print("initializing self Diagnoze...")
        time.sleep(0.6)
        res = []
        for item in cfg['selfDiagnoze']:
            if item == "gateway":
                name = "gateway " + nics[0][item][0]
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    fnc = executor.submit(TestHandler, name, nics[0][item][0])
                    res.append(fnc.result())
            elif item == "dns":
                for nic in nics[0][item]:
                    name = "dns " + nic
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        fnc = executor.submit(TestHandler, name, nic)
                        res.append(fnc.result())

        addToDump("selfDiagnoze", res)

    if 'pingHosts' in cfg:
        print("initializing pinging hosts...")
        time.sleep(0.6)
        res = []
        for item in cfg['pingHosts']:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                fnc = executor.submit(TestHandler, item, item)
                res.append(fnc.result())

        addToDump("pingHosts", res)

    # create output log file with all cached info about tests
    line = "#"
    for i in range(0, 30):
        if i == 15:
            line = line + " END OF TESTS "
        line = line + "#"

    print(line)
    if createDump():
        print(f"log file {dumpPath} has been created")
    else:
        print("cannot create log file at current dir")


if __name__ == "__main__":
    main()
