import pythonping


def diagnoze(Int):
    # nics = nics[0]
    print("diagnozing ", Int, "...", sep="")

    def runTest(target):
        return "OK"

    try:
        results = runTest(Int)
        return results
    except:
        print("error in ping")
        return "ERROR"
