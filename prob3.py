
import sys


def main():
    input = (sys.stdin.readline()).replace("*", " ")  # replace * with space in order to split numbers from mulplication
    inputList = input.split()
    baseDict = dict()
    if "0" in inputList:
        print("0")
    else:
        one = 0
        power = 0
        key = 0
        for i in inputList:
            if "^" not in i and "*" not in i:            # case for numbers only
                key = int(i)
                if key == 1:
                    one = 1
                power = 1
            else:
                basePos = i.find("^")
                key = int(i[:basePos])
                power = int(i[(basePos+1):])
            output = ""
            if key not in baseDict:             # if key doesn't exist, adds key
                baseDict[key] = power
            else:
                baseDict[key] += power
        if one == 1 and len(baseDict) < 1:
            print("1")
        else:
            baseDict.pop(1)
            for key in sorted(baseDict):                # sort base values into ascending order
                if baseDict[key] > 1:
                    output += (str(key) + "^" + str(baseDict[key]) + "*")
                else:
                    output += (str(key) + "*")
            print(output[:-1])     # to remove the last *


main()