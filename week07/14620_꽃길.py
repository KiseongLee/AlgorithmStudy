from collections import deque
from copy import deepcopy

n = int(input())       

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*(n) for _ in range(n)]
flower_dir = [(0,0), (-1, 0),(1,0), (0,-1),(0,1)]
min_value = 1e9

def cal(y,x):
    # global min_value, ans
    # q = deque(ans)
    # sum=0
    global n
    result = 0
        
    for dy,dx in flower_dir:
        ny = y + dy
        nx = x + dx
        result += graph[ny][nx]
    return result
    #     sum += graph[x][y]
    
    # min_value = min(sum, min_value)

# def count(x,y):
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0<=nx<=n-1 and 0<=ny<=n-1:
            
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1

def check(y, x):
    global n
    for dy,dx in flower_dir:
        ny = y + dy
        nx = x + dx
        if visited[ny][nx] or nx<0 or ny <0 or nx > n-1 or ny > n-1:
            return False
    return True

def flower(x, cost, cnt):
      global min_value
      if cnt == 3:
          min_value = min(min_value, cost)
          return
    
      for i in range(x, n):
          for j in range(1, n):
              if check(i,j):
                 visited[i][j] = 1
                 for dy, dx in flower_dir:
                     visited[i+dy][j+dx] = True
                 flower(i, cost + cal(i, j), cnt+1)
                 visited[i][j] = 0
                 for dy, dx in flower_dir:
                     visited[i+dy][j+dx] = False
                     
flower(1,0,0)
print(min_value)         
#                   count(i,j)
#                   ans.append(i,j)
#                   flower(cnt+1)
#                   visited = visited_copy
#                   ans = []

# flower(0)
