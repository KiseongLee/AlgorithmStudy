from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n*h)]

dx = [-1,1,0,0,-n,n]
dy = [0,0,-1,1,0,0]

queue = deque()

def bfs(x,y):
     
      
      queue.append((x,y))
      
      while queue:
            x,y = queue.popleft()
            
            for i in range(6):
                  nx = x + dx[i]
                  ny = y + dy[i]
            
                  if nx<0 or ny < 0 or nx >= n*h or ny >= m:
                     continue
            
                  if graph[nx][ny] == -1:
                         continue
            
                  if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx,ny))
            

state = True
for i in range(n*h):
      for j in range(m):
            if graph[i][j] == 1:
                  queue.append((i, j))

          
x,y = queue.popleft()                    
bfs(x, y)




for i in graph:
      if 0 in i:
         state = False
         break
   
if state:
      print(max(map(max, graph))-1)
else:
      print(-1)