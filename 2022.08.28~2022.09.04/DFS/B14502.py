from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
safe_region = 0
graph_copy = deepcopy(graph)
    
def dfs(x,y,graph):
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    dfs(nx,ny, graph)
                    


def wall(start, cnt):
    global safe_region
    if cnt == 3:
        final_graph = deepcopy(graph_copy)
        
        for i in range(n):
            for j in range(m):
                if final_graph[i][j] == 2:
                    dfs(i, j, final_graph)
        safe_count = sum(_.count(0) for _ in final_graph)
        safe_region = max(safe_region, safe_count)
        return
    
    else:
        for i in range(start, n*m):
            r = i%n
            c = i//n 
            if graph_copy[r][c] == 0:
                graph_copy[r][c]=1
                wall(i, cnt+1)
                graph_copy[r][c]=0

wall(0,0)
print(safe_region)