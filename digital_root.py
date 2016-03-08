def digital_root(num):
    temp = num
    count = 0

    while temp > 1:
        temp /= 10
        count += 1

    answer = int(temp)

    if num <= 1:
        return 0

    print("count: " + str(count))
    print("temp: " + str(temp))
    print("answer: " + str(answer))
    #return answer + digital_root(num - (answer * 10 ** count))
