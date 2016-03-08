def McNuggets(n):
    if n < 0:
        return False
    elif n % 6 == 0:
        return True
    elif n % 9 == 0:
        return True
    elif n % 20 == 0:
        return True
    else:
        return McNuggets(n - 6) and McNuggets(n - 9) and McNuggets(n - 20)

    
print(McNuggets(0))
print(McNuggets(1))
print(McNuggets(3))
print(McNuggets(6))
print(McNuggets(9))
print(McNuggets(20))
print(McNuggets(16))
