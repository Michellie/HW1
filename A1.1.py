
import sys


def primeFactorisation (k):
    outputList = []
    primeList = [2]
    for i in range(2,k + 1):
        factorString = ""
        firstDigit = 1;
        for j in range(2, i+1):
            if (i % j) == 0:
                if i == j and i not in primeList:
                    primeList += [i]
                count = 0
                while (i % j) == 0:
                    i = i / j
                    count += 1
                if j in primeList:
                    stringValue = str(primeList.index(j) + 2)
                else:
                    stringValue = str(j)
                if count > 1:
                    factorString = (stringValue + "^" + str(count))   # only prints power that is greater than 1
                    firstDigit = 0      # indicates the next digit will not be the first digit
                else:
                    if firstDigit == 1:
                        factorString += stringValue
                    else:
                        factorString += "*" + stringValue
                    firstDigit = 0      # indicates the next digit will not be the first digit

        outputList.append(factorString)
    return outputList


def main():
    k = int(sys.stdin.readline())   # problem
    if k > 1:
        print("  1 1")
        factorList = primeFactorisation(k)  # returns a list of prime factorisation strings
        for i in range (len(factorList)):
            if int(i) < 8:
                print("  " + str(i + 2) + " " + factorList[i])
            elif int(i) < 98:
                print(" " + str(i + 2) + " " + factorList[i])
            else:
                print(str(i + 2) + "" + factorList[i])
main()