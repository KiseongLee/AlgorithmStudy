t = int(input())


for i in range(t):
    
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    
    dp = [0] * (m+1)
    
    for i in range(m+1):
        if i % coin[0] == 0:
            dp[i] += 1
    
    for i in range(1, len(coin)):
        for j in range(coin[i], m+1):
            dp[j] += dp[j-coin[i]]
    
    print(dp[m])