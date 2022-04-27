n, k = map(int, input().split())

coins = [0]
for i in range(n):
    coins.append(int(input()))

coins.sort()

dp = [0] * (k+1)
dp[0] = 1

for i in range(1, n+1):
     for j in range(coins[i], k+1):
         dp[j] = dp[j] + dp[j-coins[i]]

print(dp[-1])

# 마찬가지로 초기화 해줄 필요가 없다!!
# dp[0]을 잘 주면 된다.