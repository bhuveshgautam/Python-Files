def abSubstring(s):
    longest = ''
    longestLength = 0
    st = s
    temp = abSubset(s)

    while temp != False and len(st) > longestLength:
        if len(temp) > longestLength:
            longest = temp
            longestLength = len(temp)
            index = longestLength
        else:
            index = 1
        st = st[index:]
        temp = abSubset(st)

    return longest

def abSubset(s):
    if len(s) == 0:
        return False

    st = s[0]

    for c in s[1:]:
        if c >= st[len(st) - 1]:
            st += c
        else:
            break

    return st
