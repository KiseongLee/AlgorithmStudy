from collections import deque

n, m = map(int, input().split())
INF = 1e9

map = [list(map(int,input())) for _ in range(n)]
distance = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a,b,c):
    
    q = deque()
    q.append([a,b,c])
    distance[a][b][c] = 1
    
    while q:
        
        x,y,z = q.popleft()
        
        if x == n-1 and y == m-1:
            return print(distance[x][y][z])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx<=n-1 and 0<=ny<=m-1:
            
                if map[nx][ny] == 1 and z == 0:
                    distance[nx][ny][1] = distance[x][y][0]+ 1
                    q.append([nx,ny, 1])
                
                elif map[nx][ny] == 0 and distance[nx][ny][z] == 0:
                    distance[nx][ny][z] = distance[x][y][z]+ 1
                    q.append([nx,ny,z])

    return print(-1)

bfs(0,0,0)
# for i in range(len(distance)):
#     print(distance[i])
             
    
