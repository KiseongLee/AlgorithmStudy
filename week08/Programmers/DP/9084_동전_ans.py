
t = int(input())

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    
    d = [0]*(m+1)
    d[0] = 1 # dp[2] = dp[2] + dp[0]
             # 동전 한 개만 썼을 때를 위한 것을 계산하기 위해 선언
    
    for coin in coins:
        for j in range(coin, m+1):
               d[j] += d[j-coin]
    
    print(d[m])
    