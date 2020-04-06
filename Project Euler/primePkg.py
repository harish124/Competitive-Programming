import time

start=time.time()
def isPrime(n):
    if(n<2):
        return 0
    if(n<4):
        return 1
    if(n%2==0 or n%3==0):
        return 0
    if(n<8):
        return 1

    r=int(n**.5)
    f=5
    if(r**2 == n):
        return 0

    while(f<=r):
        if(n%f==0):
            return 0
        if(n%(f+2)==0):
            return 0
        f=f+6

    return 1

primeSet=set()
def calcPrimeSet():
    for i in range(999983,10000000):
        if(isPrime(i)):
            #print(i)
            primeSet.add(i)
    #print("Set : ",primeSet)
    print("Time Elapsed: ",time.time()-start)


    
        
    
