import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

def dfs(x,y):
        

       visited[x][y] = True
       
       for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= nx < m and 0 <= ny < n: 
        
            if graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx,ny)

t = int(input())

for _ in range(t):
    
    m, n, k = map(int, input().split())

    graph = [[0]*n for i in range(m)]

    visited = [[False]*n for i in range(m)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                if not visited[i][j]:
                    dfs(i,j)
                    count += 1
    
    
    
    print(count)