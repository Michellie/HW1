

def primeFactorisation (k):
    factorString = ""
    for i in range(2, k+1):
        if (k % 2) == 0:
            count = 0
            while (k % i) == 0:
                k = k / i
                count += 1
            factorString = (str(i) + "^" + str(count))
    primeCount = 0      #keep count of prime number
    if k != 1:
        primeCount += 1
        factorString += "*" + str(int(k))
    return (factorString)


def main():
    k = int(input("Please enter k: "))
    print("  k pfe(k) ")
    for i in range (k):
        factorString = primeFactorisation(i + 1)
        print(" " + str(i+ 1) + " " + factorString)




main()
