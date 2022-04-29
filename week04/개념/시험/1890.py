from collections import deque
n = int(input())

data = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
# visited = [[False]*n for i in range(n)]

def bfs(a,b):
    
    q = deque()
    q.append((a,b))
    
    while q:
        
        x,y = q.popleft()
        value = data[x][y]
        
        if value == 0:
            continue
        
        nx1 = x+value
        ny1 = y
        
        if 0<=nx1<=n-1:    
            if nx1 == n-1 and ny1 == n-1:
                dp[nx1][ny1] +=1 
                continue
                
            if not dp[nx1][ny1]:
                dp[nx1][ny1] += 1
                q.append((nx1,ny1))
                
        nx2 = x
        ny2 = y+value
        
        if 0<=ny2<=n-1: 
             
            if nx2 == n-1 and ny2 == n-1:
                dp[nx2][ny2] +=1
                continue 
                
            if not dp[nx2][ny2]:
                dp[nx2][ny2] += 1
                q.append((nx2,ny2))
            
bfs(0,0)

print(dp[n-1][n-1])

'''
9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0
6
'''



N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)] 
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1: 
            print(dp[i][j])
            break
        cur_cnt = field[i][j]
 
        if j + cur_cnt < N:
            dp[i][j + cur_cnt] += dp[i][j]
        if i + cur_cnt < N:
            dp[i + cur_cnt][j] += dp[i][j]