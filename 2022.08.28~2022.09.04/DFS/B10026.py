import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x,y,str):
    
    
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx < n and 0<= ny < n:
            if graph[nx][ny]==str:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    dfs(nx,ny,str)
    return True
    
dx = [-1,1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

graph=[]
for i in range(n):
    graph.append(list(map(str, input())))

visited=[[0]*n for i in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            if dfs(i,j,graph[i][j]):
                result += 1
result_copy = 0
visited=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            if dfs(i,j,graph[i][j]):
                result_copy += 1

print(result, result_copy)