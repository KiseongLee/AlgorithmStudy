n, k = map(int, input().split())

coins =[]
for i in range(n):
    coins.append(int(input()))

dp = [0]*(k+1)

dp[0] = 1 # dp[0]을 1로 놓아야함. 그래야 정확히 값 빠질 때, 카운팅이 된다.

for i in range(len(coins)):
    for j in range(coins[i], k+1):
        dp[j] += dp[j-coins[i]]
        

print(dp[k])