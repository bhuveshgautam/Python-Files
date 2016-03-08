def myLog(x, b):
    test = 0
    ans = 0
    temp = b ** test

    while temp <= x:
        test += 1
        temp = b ** test
        ans = test - 1

    return ans
