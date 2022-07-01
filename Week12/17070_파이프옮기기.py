n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)] # [0, 0, 0] 가로, 대각선, 세로 순

for i in range(1, n):
        
    if board[0][i] == 1:
        break
    
    dp[0][i][0] = 1     # 가로 첫줄(0행) 초기화 해주는데, board[0][i]==1일 때 부턴 0으로 초기화

# 조건
# 1. 파이프 설치할 공간 확인
# 벽 or (가로, 세로, 대각선) 파이프 설치할 공간 있는지 확인

# board[i][j] = 0  # 가로, 세로
# board[i-1][j] and board[i][j-1] # 대각선


for i in range(1, n):
    for j in range(1, n):
        if board[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

        if board[i][j] == 0 and board[i-1][j] ==0 and board[i][j-1] == 0:
            dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

# for i in range(n):
#     print(dp[i])
print(sum(dp[n-1][n-1]))

