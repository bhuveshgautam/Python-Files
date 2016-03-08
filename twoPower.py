def square(x):
    return x * x

def twoPower(x, n):
    while n > 1:
        x = square(x)
        n /= 2
    return x
