

def primeFactorisation (k):
    outputList = []
    for i in range(2,k):
        factorString = ""
        for j in range(2, i+1):
            if (i % 2) == 0: # i is an even number
                count = 0
                while (i % j) == 0:
                    i = i / j
                    count += 1
                if count > 1:
                    factorString = (str(j) + "^" + str(count))   # only prints power that is greater than 1
                else:
                    factorString = (str(j))
        primeList = []
        if i != 1:
            if i not in primeList:
                primeList.append(i)
                factorString += str(int(i))
            else:
                prime = primeList.index(str(int(i)))
                factorString += "*" + str(prime + 1)

        outputList.append(factorString)
    return outputList


def main():
    k = int(input("Please enter k: "))
    print("  k pfe(k) ")
    if k > 1:
        print(" 1 1")
        # for i in range(1,k):
        factorList = primeFactorisation(k)
        for i in range (len(factorList)):
            print(" " + str(i + 2) + " " + factorList[i])




main()
