# t = int(input())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def dfs(x, y):
    
#     global sum_value
    
#     if 
    
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if not visited[nx][ny]:
#             visited[nx][ny] = 1
    
#     for i in range(2):
#         for j in range(n):
#             if not visited[i][j]:
#                 visited[i][j]=1
#                 sum_value += sticker[i][j]
#                 dfs(i,j)
#                 visited[i][j]=0
        
# for i in range(t):
#     n = int(input())
#     sticker = [list(map(int,input().split())) for _ in range(2)]
#     visited = [[0]*n for _ in range(2)]
    
#     for i in range(2):
#         for j in range(n):
#             sum_value = sticker[i][j]
#             dfs(i,j)
            
t = int(input())

for i in range(t):
    n = int(input())
    
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n>=2:
        dp[0][1] = dp[1][0]+sticker[0][1]
        dp[1][1] = dp[0][0]+sticker[1][1]
    if n>=3:
        for i in range(n):
            dp[0][i] = max(dp[1][i-1]+sticker[0][i], dp[1][i-2]+sticker[0][i])
            dp[1][i] = max(dp[0][i-1]+sticker[1][i], dp[0][i-2]+sticker[1][i])
    
    print(max(dp[0][n-1], dp[1][n-1]))
    
    
    