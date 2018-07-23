
import sys


def main():
    inputList = (sys.stdin.readline()).split()  # problem
    baseDict = dict()
    if "0" in inputList:
        print("0")
    else:
        for i in inputList:
            if "^" not in i or "*" not in i:            # case for numbers only
                key = int(i)
                if key not in baseDict:             # if key doesn't exist, adds key
                    baseDict[key] = 1
                else:                                   # if base exist, adds power into string of values
                    baseDict[key] = baseDict[key] + 1
    # baseDict = sorted(baseDict.keys())
        output = ""
        for key in sorted(baseDict):                # sort base values into ascending order
            print("Key:", key, "Values:", baseDict[key])
            output += (str(key) + "^" + str(baseDict[key]) + "*")
    print(output[:-1])      # to remove the last *


main()