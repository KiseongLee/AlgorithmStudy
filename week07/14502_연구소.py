from collections import deque
import copy
import sys
n, m = map(int, input().split())
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(n)]

max_result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def wall(cnt):
    
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0    #다시 0으로 바꿔줘서 초기화를 시킨다
                
def bfs():
    
    global max_result
    q = deque()
    graph_cp = copy.deepcopy(graph)
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]    
        
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            
             if graph_cp[nx][ny] == 0:
                graph_cp[nx][ny] = 2
                q.append([nx, ny])
    
    result = 0
    for i in range(n):
        for j in range(m):
            if graph_cp[i][j] == 0:
                result += 1
    
    max_result = max(result, max_result)

wall(0)
print(max_result)



