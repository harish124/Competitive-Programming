from printDP import printdp2 as pdp

def lps(s:str):
    n=len(s)

    arr=list(s)

    
    dp=[[0 for i in range(n)] for j in range(n)]

    max_len=0

    # strings of len 1 are pallindrome
    for i in range(n):
        dp[i][i]=1
        max_len=1

    pdp(dp,arr)

    
    for curr_len in range(2,n+1):
        for i in range(n-curr_len+1):
            j=i+curr_len-1

            if(arr[i]==arr[j]):
                dp[i][j]=2+dp[i+1][j-1]                
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        pdp(dp,arr)

    max_len=dp[0][n-1]
    print('Length of Longest Pallindromic Subsequence in ',s,' = ',max_len)
    
print('Enter any string: ')
lps(input())
