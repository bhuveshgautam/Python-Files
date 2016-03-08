def factorial(n):
    result = n
    count = n - 1

    if n == 0:
        return 1

    while count > 0:
        result *= count
        count -= 1

    return result

def zeros(n):
    result = 0
    temp = n

    if n > 0:
        while temp % 10 == 0:
            result += 1
            temp = int(temp / 10)

    return result
