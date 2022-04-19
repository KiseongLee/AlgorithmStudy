from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [False]*(n+1)
check = [0] * (n+1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):

    q = deque()
    q.append((x,y))
    
  
            
    while q:
       x,y = q.popleft()
       
       for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:   
          if graph[nx][ny] == 1:
              graph[nx][ny] = graph[x][y] +1
              q.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])