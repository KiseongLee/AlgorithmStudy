import copy
import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(m)]

graph_copy = copy.deepcopy(graph)

max_result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def wall(cnt):
    
    if cnt == 3:
        bfs()
        return
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0
                
def bfs():
    global max_result
    
    queue = deque()
    final_graph = copy.deepcopy(graph)
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 2:
                queue.append((i,j))
        
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if final_graph[nx][ny] == 0:
                    final_graph[nx][ny] = 2
                    queue.append((nx, ny))
    
    result = 0
    for i in range(m):
        for j in range(n):
            if final_graph[i][j]==0:
                result += 1
                
    max_result = max(result, max_result)

wall(0)
print(max_result)


#https://velog.io/@jungmiin/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%ACBFSDFS18%EC%A3%BC%EC%B0%A8-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-18352-14502-18405-14888
