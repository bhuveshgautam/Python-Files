def genPrimes():
    primes = []
    current = 2
    while True:
        flag = True
        for p in primes:
            if (current % p) == 0:
                flag = False
                break

        if flag == True:
            primes.append(current)
            yield current

        current += 1
