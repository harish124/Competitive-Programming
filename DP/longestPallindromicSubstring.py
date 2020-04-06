from printDP import printdp2 as pdp

def lps(s:str):
    n=len(s)

    s=s.lower()

    dp=[[0 for i in range(n)] for j in range(n)]

    arr=list(s)
    
    pdp(dp,arr)

    max_len=0

    pallindromeBeginsAt=0

    # strings of len 1 are pallindrome
    for i in range(n):
        dp[i][i]=1
        pallindromeBeginsAt=i

    pdp(dp,arr)

    # strings of len 2 below
    # why this is a special case because:
    # conside 'll' start and end match so trim now s='' which is a pallindrome so this must
    # be treated as special case

    curr_len=2
    for i in range(2,n-curr_len+1):
        if(arr[i]==arr[i+1]):
            dp[i][i+1]=1
            max_len=2
            pallindromeBeginsAt=i

    #for lengths >2 below:
    for curr_len in range(3,n+1):        
        for i in range(n-curr_len+1):
            j=i+curr_len-1
            print('curr_len = ',curr_len,'i = ',i,' j = ',j)
            if(arr[i]==arr[j]):
                print('Reached')
                if(dp[i+1][j-1]==1):
                    print('i = ',i,' j = ',j)
                    dp[i][j]=1
                    max_len=curr_len
                    pallindromeBeginsAt=i
        pdp(dp,arr)
    
    print('Longest Pallindromic Substring Length in ',s,' = ',max_len)
    print('Pallindrome = ',s[pallindromeBeginsAt:max_len+pallindromeBeginsAt])

    
    
print('Enter any string: ')
lps(input())
