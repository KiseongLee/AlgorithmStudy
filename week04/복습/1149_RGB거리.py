n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dp = [[0]*3 for i in range(n)]

for i in range(3):
    dp[0][i] = data[0][i]


for i in range(1, n):
    
    dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])


print(min(dp[n-1]))