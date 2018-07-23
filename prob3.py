
import sys


def main():
    inputList = (sys.stdin.readline()).split()  # problem
    baseDict = dict()
    if "0" in inputList:
        print("0")
    else:
        for i in inputList:
            if "^" not in i or "*" not in i:            # case for numbers only
                if i not in baseDict:             # if key doesn't exist, adds key
                    baseDict[i] = 1
                else:                                   # if base exist, adds power into string of values
                    baseDict[i] = baseDict[i] + 1
    # baseDict = sorted(baseDict.keys())
        for key in sorted(baseDict):                # sort base values into ascending order
            print("Key:", key, "Values:", baseDict[key])


main()