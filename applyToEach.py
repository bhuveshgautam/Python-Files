def fact(n):
    assert n >= 0
    
    ans = 1

    while n > 0:
        ans *= n
        n -= 1

    return ans

def fib(n):
    assert n >= 0

    a = 0
    b = 1

    count = 0

    while count <= n:
        temp = a + b
        b = a
        a = temp
        count += 1

    return a

def applyToEach(L, f):
    """
    Assumes L is a list, f a functions
    Mutates L by replacing each element,
    e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.4]

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)

def applyFuns(L, x):
    for f in L:
        print(f(x))
