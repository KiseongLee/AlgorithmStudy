n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*i for i in range(1, n+1)]

dp[0][0] = data[0][0]


for i in  range(1, len(dp)):
    for j in range(len(dp[i])):
        
        if j == 0:
            dp[i][j] = data[i][j] + dp[i-1][j]
            continue
            
        if j == len(dp[i])-1:
            dp[i][j] = data[i][j] + dp[i-1][j-1]
            continue
        
        dp[i][j] = data[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        # else쓸 때 조심하자!!

print(max(dp[n-1])) 


