
import sys


def main():
    inputList = (sys.stdin.readline()).split()  # problem
    baseDict = dict()
    if "0" in inputList:
        print("0")
    else:
        one = 0
        for i in inputList:
            if "^" not in i or "*" not in i:            # case for numbers only
                key = int(i)
                if key == 1:
                    one = 1
                elif key not in baseDict and key != 1:             # if key doesn't exist, adds key
                    baseDict[key] = 1
                else:                                   # if base exist, adds power into string of values
                    baseDict[key] = baseDict[key] + 1
        output = ""
        if one == 1 and len(baseDict) < 1:
            print("1")
        else:
            for key in sorted(baseDict):                # sort base values into ascending order
                print("Key:", key, "Values:", baseDict[key])
                if baseDict[key] == 1:
                    output += (str(key) + "*")
                else:
                    output += (str(key) + "^" + str(baseDict[key]) + "*")
            print(output[:-1])      # to remove the last *


main()