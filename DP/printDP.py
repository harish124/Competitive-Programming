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

def printdp3(dp,arr1,arr2):
    print('######################################################')
    i=0
    print('     ',end='')
    for j in range(len(arr2)):
        print(arr2[j],end='  ')
    print()
    for x in dp:
        print(arr1[i],' ',x)
        i+=1
    print('######################################################')
