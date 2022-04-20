from collections import deque
n, k = map(int, input().split())

graph =[list(map(int, input().split())) for i in range(n)]
virus= []
s, x, y = map(int, input().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*n for i in range(n)]

def bfs():
    q = deque(virus)
    while q:
        
        
        a,x,y,sec = q.popleft()
        
        if sec == s:
            break
        
        visited[x][y] = True
        sec += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0<= ny < n:
                
                if graph[nx][ny] == 0  and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    graph[nx][ny] = a
                    q.append([graph[nx][ny],nx,ny,sec])
        

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append([graph[i][j], i, j, 0])

virus.sort()
bfs()

print(graph[x-1][y-1])