n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

x = set(coin)
coin = list(x)

dp = [0]*(k+1)

for i in range(len(dp)):
    if i % coin[0] == 0:
        dp[i] += 1

for i in range(1, len(coin)):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]

print(dp[k])