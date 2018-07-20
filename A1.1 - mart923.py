def primeFactorisation (k):
    outputList = []
    primeList = [2]
    for i in range(2,k + 1):
        factorString = ""
        firstDigit = 1;
        for j in range(2, i+1):
            if (i % j) == 0:
                count = 0
                while (i % j) == 0:
                    i = i / j
                    count += 1
                if count > 1:
                    factorString = (str(j) + "^" + str(count))   # only prints power that is greater than 1
                    firstDigit = 0
                else:
                    if firstDigit == 1:
                        factorString +=  (str(j))
                    else:
                        factorString += "*" + (str(j))
                    firstDigit = 0

        outputList.append(factorString)
    return outputList


def main():
    k = int(input("Please enter k: "))
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
                print(str(i + 2) + "" + factorList[i])
main()