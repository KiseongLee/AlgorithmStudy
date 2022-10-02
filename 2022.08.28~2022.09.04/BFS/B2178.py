from collections import deque
import sys
input = sys.stdin.readline

n,m= map(int, input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

visited =[[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    
    queue = deque([(x,y)])
    visited[x][y]=1
    
    while queue:
        x,y = queue.popleft() #popleft를 통해서 먼저들어온놈이 먼저 나가게 해줘야함
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        visited[nx][ny]=1
                        graph[nx][ny]=graph[x][y]+1
                        queue.append((nx,ny))
                    
bfs(0,0)
print(graph[n-1][m-1])