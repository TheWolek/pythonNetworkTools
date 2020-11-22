import json
import sys

from nics import getNics
from diagnoze import diagnoze


def main():
    conductedTests = []

    def getFlags():
        args = sys.argv

        if len(args) - 1 > 0:
            args.pop(0)
            return args
        else:
            return False

    def createDump():
        toDump = {
            "nics": nics
        }
        if "diagnoze" in conductedTests:
            toDump["testResults"] = results

        with open("output.json", "w") as f:
            json.dump(toDump, f)

        return

    flags = getFlags()
    if flags:
        if "-diag" in flags:
            conductedTests.append("diagnoze")
            results = diagnoze()

    nics = getNics()
    createDump()


if __name__ == "__main__":
    main()
