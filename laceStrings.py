def laceStrings(s1, s2):
    ans = ''
    s1Temp = s1
    s2Temp = s2

    while s1Temp != '' and s2Temp != '':
        ans += s1Temp[0] + s2Temp[0]
        s1Temp = s1Temp[1:]
        s2Temp = s2Temp[1:]

    if s1Temp == '':
        return ans + s2Temp
    else:
        return ans + s1Temp
