from collections import deque
import sys
input = sys.stdin.readline

n = int(input())


graph =[list(map(int, input().rstrip())) for i in range(n)]

distance = [[-1]*n for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
  
  q = deque()
  q.append([x,y])
  distance[0][0]=0
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0<= nx < n and 0<= ny < n:
        
        if distance[nx][ny] == -1:
          
          if graph[nx][ny] == 1:
             
             distance[nx][ny] = distance[x][y]
             q.appendleft([nx,ny])
          
          else:
             distance[nx][ny] = distance[x][y]+1
             q.append([nx,ny])
             
  return distance[n-1][n-1]


print(bfs(0,0))
for i in range(len(distance)):
  print(distance[i])