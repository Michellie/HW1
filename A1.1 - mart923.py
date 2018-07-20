

def primeFactorisation (k):
    i = k
    factorString = ""
    for j in range(2, i+1):
        if (i % 2) == 0:
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

    return (factorString)


def main():
    k = int(input("Please enter k: "))
    print("  k pfe(k) ")
    if k > 1:
        print(" 1 1")
        for i in range(1,k):
            factorString = primeFactorisation(i + 1)
            print(" " + str(i+ 1) + " " + factorString)




main()
