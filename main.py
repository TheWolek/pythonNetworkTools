import json

from nics import getNics
from diagnoze import diagnoze


def main():
    nics = getNics()
    results = diagnoze()
    toDump = {
        "nics": nics,
        "testResults": results
    }

    with open("output.json", "w") as f:
        json.dump(toDump, f)


if __name__ == "__main__":
    main()
