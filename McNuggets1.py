def mcNuggets(n):
    p=False
    for i in range(n//6+1):
        for j in range(n//9+1):
            for k in range(n//20+1):
                if(6*i+9*j+20*k==n):
                    p=True
                    print("No. of 6 , 9 , 20 pack of nuggets",i,j,k)
                   
    if(p==False):
        print("Combination not possible")
