# 동전 문제 --> 책 순서로 복습
# 금광, 등등
# 문제까지 풀어보기
# 그리디 알고리즘 --> 복습


n, k = map(int, input().split())

coins = [0]
for i in range(n):
    coins.append(int(input()))
    
coins.sort()

INF = 1e9
dp = [INF]*(k+1)
dp[0] = 0


# for i in range(1, k+1):
#     if i % coins[1] == 0:
#         dp[i] = i // coins[1]

# for j in range(2, n+1):
#     for i in range(coins[j], k+1):
#         dp[i] = min(dp[i], dp[i-coins[j]]+1)

for j in range(1, n+1):
    for i in range(coins[j], k+1):
        dp[i] = min(dp[i], dp[i-coins[j]]+1)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
    

# 0이 있으므로 for문을 나눌 필요가 없다
# dp[0]이 0이므로 점화식에 넣어보면 무조건 갱신될 수 밖에 없다.