n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
INF = 1e9
result = INF
for color in range(3):
    
    for i in range(3):
        # 현재 색깔을 정하면, 다른 것은 다 무한대로 처리하는 구문
        if i == color:
            dp[0][i] = data[0][i]
        else:
            dp[0][i] = INF
    
    
    for i in range(1, n):
        # dp테이블 채우기
        dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])

    for i in range(3):
        # 마지막 색깔이랑 처음 색깔이랑 비교하는 구문
        if i != color:
            result = min(result, dp[n-1][i])

print(result)

# 색깔을 정하고 들어간다. 비교만해주면된다.