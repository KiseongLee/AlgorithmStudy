from collections import deque

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

s, a, b = map(int, input().split())

visited = [[0]*n for _ in range(n)]

virus = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    
    q = deque(virus)
    
    while q:
        
        value, x, y, sec = q.popleft()
        
        if sec == s:
            break
        
        sec += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<= nx < n and 0<= ny <n:
                
                if graph[nx][ny] == 0 and visited[nx][ny]==0:
                    graph[nx][ny] = value
                    visited[nx][ny] = 1
                    q.append([graph[nx][ny], nx, ny, sec])        


for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append([graph[i][j], i, j, 0])

virus.sort()
bfs()

print(graph[a-1][b-1])
        
        
        