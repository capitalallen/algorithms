# weights: weight of items
# vals: value of items 
# capacity: c 
def knapscak(weights,vals,c):
    dp = [[0 for _ in range(c+1)] for _ in range(len(vals)+1)]
    print(dp)
    for i in range(len(vals)+1):
        dp[i][0] = 0
    # bottom up 
    for i in reversed(range(len(vals))):
        for j in range(c+1):
            print(i,j)
            if weights[i]<=j:
                print(i,j)
                dp[i][j]=max(dp[i+1][j],(vals[i]+dp[i+1][j-weights[i]]))
            else:
                dp[i][j] = dp[i+1][j]
    print(dp)
    print(dp[0][c])

weights,vals,c = [4,2,3],[10,4,7],5
knapscak(weights,vals,c)