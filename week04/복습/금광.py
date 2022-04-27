t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result =[]
    for i in range(n):
        result.append(data[m*i:m*i+4])
    dp = [[0]*m for i in range(n)]
    for i in range(n):
        dp[i][0] = result[i][0]
    for j in range(1, m):
     for i in range(n):
        
           if i == 0:
           
            dp[i][j] = result[i][j] + max(dp[i][j-1], dp[i+1][j-1])
            
           elif i == n-1:
            dp[i][j] = result[i][j] + max(dp[i][j-1], dp[i-1][j-1])
           
           else:
            dp[i][j] = result[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
    
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][-1])
    
    print(ans)