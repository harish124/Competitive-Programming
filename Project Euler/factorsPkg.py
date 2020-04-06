def my_factors(n):    
    l=set()
    r=int(n**.5)
    i=2
    l.add(1)
    l.add(n)
    while(i<=r):
        if(n%i==0):
            l.add(int(i))        
            l.add(int(n/i))
            #print("i = ",i," n = ",n/i)
        i=i+1
    #print(l)
    return l












