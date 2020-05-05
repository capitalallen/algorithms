# Dynamic Programming implementation of LCS problem
def lcs(s1,s2):
    m,n = len(s1),len(s2)
    dp = [[None]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j ==0:
                dp[i][j] = 0
            elif s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp

def print_lcs(dp, s1, s2, i, j):
    if dp[i][j] == 0:
        return
    if s1[i-1] == s2[j-1]:
        print_lcs(dp, s1, s2, i - 1, j - 1)
        print (s1[i-1])
    elif dp[i - 1][j] > dp[i][j - 1]:
        print_lcs(dp, s1, s2, i - 1, j)
    else:
        print_lcs(dp, s1, s2, i, j - 1)

s1 = "AGGTAB"
s2 = "GXTXAYB"
print_lcs(lcs(s1,s2),s1,s2,len(s1),len(s2))