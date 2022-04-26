n, t = map(int, input().split())

data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

data.sort()

dp = [0] * (t+1)


for time, score in data:
    for total_time in range(t, time-1, -1):
        dp[total_time] = max(dp[total_time], dp[total_time-time]+score)

print(dp[-1])


