def countBobs(s):
    index = s.find('bob')
    count = 0
    st = s
    
    while index != -1:
        count += 1
        st = st[(index + 2):]
        index = st.find('bob')

    print("Number of times bob occurs is : " + str(count))
