from collections import deque


n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))
INF = 1e9
visited = [[-1]*n for _ in range(n)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    queue = deque([[x,y]])
    
    while queue:
        
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==-1:
                    if graph[nx][ny]==1:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft([nx,ny])
                    else:
                        visited[nx][ny] = visited[x][y]+1
                        queue.append([nx,ny])

bfs(0,0)
print(visited[n-1][n-1])
    