n = int(input())

T = []
P = []
dp = [0]*(n+1)
max_value = 0
for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

for i in range(n-1, -1, -1):
    if T[i]+i <= n:
        dp[i] = max(P[i]+dp[T[i]+i], max_value)
        max_value = dp[i]
    
    else:
        dp[i] = max_value

print(max(dp))