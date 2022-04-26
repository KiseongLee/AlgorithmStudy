n, k = map(int, input().split())

data =[]
for i in range(n):
    a, b = map(int, input().split())
    data.append((a,b))
    
data.sort()

dp = [0] * (k+1)

for i in range(len(dp)):
    if i >= data[0][0]:
        dp[i] = data[0][1]

for j in range(1, len(data)):
    for i in range(k, data[j][0]-1, -1):
        dp[i] = max(dp[i], dp[i-data[j][0]]+data[j][1])
        
print(dp)