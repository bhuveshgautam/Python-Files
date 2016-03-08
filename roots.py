def findRoot1(x, power, epsilon):
    low = 0
    high = x
    ans = (high + low) / 2.0
    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def findRoot2(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    
    low = min(0, x)
    high = max(0, x)
    ans = (high + low) / 2.0

    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def findRoot3(x, power, epsilon):
    """
    x: int or float
    power: int >= 1
    epsilon: int or float > 0

    Returns a float y s t. y ** power is within epsilon of x.
    If such a float does not exist, it returns None.
    """
    if x < 0 and power % 2 == 0:
        return None

    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2.0

    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans
