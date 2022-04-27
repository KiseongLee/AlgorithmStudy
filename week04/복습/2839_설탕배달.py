
n = int(input())

dp = [5001] * (n+1)

dp[0] = 0
dp[3] = 1

for i in range(5, n+1):
    dp[i] = min(dp[i-5]+1, dp[i-3]+1)


if dp[-1] >= 5001:
    print(-1)
else:
    print(dp[-1])