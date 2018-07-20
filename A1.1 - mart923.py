

def primeFactorisation (k):
    outputList = []
    primeList = [2]
    for i in range(2,k + 1):
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
        if i != 1:
            if i not in primeList:
                primeList += [i]
                factorString += str(int(i))
            else:
                prime = primeList.index(int(i))
                factorString += "*" + str(prime + 2 ) # 1: counting from 1, 2: number 2 is already in the list
        outputList.append(factorString)
    print("a", primeList)
    return outputList


def main():
    k = int(input("Please enter k: "))
    print("  k pfe(k) ")
    if k > 1:
        print(" 1 1")
        factorList = primeFactorisation(k)  # returns a list of prime factorisation strings
        for i in range (len(factorList)):
            print(" " + str(i + 2) + " " + factorList[i])




main()
