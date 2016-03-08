def findDivisors(n1, n2):
    """
    Assumes n1 and n2 are positive ints
    returns tuple containing
    common divisors of n1 and n2
    """
    divisors = ()               # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisors += (i,)
    return divisors
