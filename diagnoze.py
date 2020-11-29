from pythonping import ping


def diagnoze(Int):
    # nics = nics[0]
    print("diagnozing ", Int, "...", sep="")

    def runTest(target):
        return ping(target)

    try:
        results = runTest(Int)
        if results.success(3):
            return "OK (5/5)"
        elif results.success(2):
            return "OK (3/5)"
        else:
            return "Not responding (0/0)"
    except:
        print("error in ping")
        return "ERROR"
