
import sys


def primeFactorisation (k):
    outputList = []
    primeList = [2]
    primeCounter = 2
    for i in range(2,k + 1):
        factorString = ""
        for j in range(2, i+1):
            if (i % j) == 0:
                if i == j:
                    if i not in primeList:       # identifies prime numbers
                        primeList += [i]
                        primeCounter += 1       # increase the number of prime number
                        factorString += str(primeCounter)
                        #factorString += str(i) + "     p: " + str(primeCounter) + " a "
                    else:
                        factorString += str(primeList.index(i)+ 2)      # 1: number 2 is already found, 2: index + 1 = number found
                        #factorString += "   " + str(int(i)) + "     p: " + str(primeList.index(i)+ 2) + " b "
                else:
                    count = 0
                    while (i % j) == 0:
                        i = i / j
                        count += 1
                    if j not in primeList:
                        stringValue = str(j)
                    else:
                        stringValue = str(primeList.index(j)+ 2)
                    factorString += stringValue
                    if count > 1:
                        factorString += "^" + str(count)  # only prints power that is greater than 1
                    if i > 1:
                        factorString += "*"
        outputList.append(factorString)
    return outputList


def main():
    k = int(sys.stdin.readline())   # problem
    print("  k pfe(k) ")
    if k == 1:
        print("  1 1")
    if k > 1:
        factorList = primeFactorisation(k)  # returns a list of prime factorisation strings
        for i in range (len(factorList)):
            if int(i) < 8:
                print("  " + str(i + 2) + " " + factorList[i])
            elif int(i) < 98:
                print(" " + str(i + 2) + " " + factorList[i])
            else:
                print(str(i + 2) + " " + factorList[i])


main()