
import sys


def primeFactorisation (k):
    outputList = []
    primeList = [2]
    for i in range(2,k + 1):
        factorString = ""
        for j in range(2, i+1):
            if (i % j) == 0:                        # i = 50, j = 2
                if i == j and i not in primeList:
                    primeList += [i]
                count = 0
                while (i % j) == 0:     # 50%2 = 0
                    i = i / j           #i = 25 j = 2
                    count += 1
                stringValue = str(j)
                factorString += stringValue
                if count > 1:
                    factorString += "^" + str(count)  # only prints power that is greater than 1
                if i > 1:
                    factorString += "*"

        outputList.append(factorString)
    print("PrimeList:", primeList)
    return outputList


def main():
    k = int(sys.stdin.readline())   # problem
    print("  k pfe(k) ")
    if k > 1:
        print("  1 1")
        factorList = primeFactorisation(k)  # returns a list of prime factorisation strings
        for i in range (len(factorList)):
            if int(i) < 8:
                print("  " + str(i + 2) + " " + factorList[i])
            elif int(i) < 98:
                print(" " + str(i + 2) + " " + factorList[i])
            else:
                print(str(i + 2) + " " + factorList[i])


main()