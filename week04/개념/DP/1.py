
n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))
    
    
dp = [10001]*(m+1)
dp[0] = 0


for i in range(n):
    for j in range(data[i], m+1):
        if dp[j-data[i]] != 10001:
            dp[j] = min(dp[j], dp[j-data[i]]+1)


if dp[n] == 10001:
    print(-1)
else:
    print(dp[m])