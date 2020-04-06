def printdp(dp):
    print('######################################################')
    for x in dp:
        print(x)
    print()
    print('######################################################')
    
def printdp2(dp,arr):
    print('######################################################')
    i=0
    print('     ',end='')
    for j in range(len(arr)):
        print(arr[j],end='  ')
    print()
    for x in dp:
        print(arr[i],' ',x)
        i+=1
    print('######################################################')
