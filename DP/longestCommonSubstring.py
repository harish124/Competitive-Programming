from printDP import printdp3 as pdp

def lcs(s1,s2):
    m=len(s1)
    n=len(s2)

    dp=[[0 for j in range(n)] for i in range(m)]

    arr1=list(s1)
    arr2=list(s2)
    
    pdp(dp,arr1,arr2)

    mmax=0

    sub_strings=[]
    
    for i in range(m):
        for j in range(n):
            if(arr1[i]==arr2[j]):
                if(j==0):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+1

                if(dp[i][j]>mmax):
                    mmax=dp[i][j]
                    sub_strings=[]
                    sub_strings.append(arr1[i-mmax+1:i+1])
                elif(dp[i][j]==mmax):
                    sub_strings.append(arr1[i-mmax+1:i+1])

        pdp(dp,arr1,arr2)

    print('Length of LongestCSubstring btw \n',s1,' and \n',s2,' = \t',mmax)
    print('The substrings are: ')
    for x in sub_strings:
        print(''.join(x))

    

print('Enter String 1: ')
s1=input()
print('Enter String 2: ')
s2=input()

lcs(s1,s2)

