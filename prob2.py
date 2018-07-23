
import sys


def primeFactorisation (k):
    outputList = []
    for i in range(11, k + 1, 2):
        count = 0
        for j in range(2, i+1):
            if (i % j) == 0 and i != j:
                count += 1
        if count == 0:
            outputList.append(i)
    return outputList


def main():
    k = int(sys.stdin.readline())
    print("  k pfe(k) ")
    if k == 1:
        print("  1 1")
    if k > 1:
        factorList = primeFactorisation(k)  # returns a list of prime factorisation strings
        count = 6
        for i in factorList:
            if len(str(count)) < len(str(i)):       # only prints strings with pfe string shorter than length of d(k) string representation
                if len(str(i)) == 2:
                    print(" " + str(i), count)
                else:
                    print(str(i), count)
            count += 1


main()