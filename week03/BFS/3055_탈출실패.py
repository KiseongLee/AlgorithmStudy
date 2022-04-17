from collections import deque
import sys
input = sys.stdin.readline


r, c = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(r)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            queue.appendleft((i,j,1))
            graph[i][j] = 0
        
        elif graph[i][j] == '*':
             queue.append((i,j,0))
             graph[i][j] = -1
        elif graph[i][j] == 'D':
            target_x = i
            target_y = j
            graph[i][j] = 9
        elif graph[i][j] == '.':
            graph[i][j] = 0
        else:
            graph[i][j] = -2

def bfs():
    
    while queue:
        
        x,y,check = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx>=r or ny >= c:
                continue
            
            if check == 1:
                if graph[nx][ny] != -1:
                    graph[nx][ny]= graph[x][y]+1
                    queue.append((nx, ny, 1))
            
            if check == 0:
               if graph[nx][ny] != -2 and graph[nx][ny] != 9:
                    graph[nx][ny] = -1
                    queue.append((nx, ny, 0))
        
            
bfs()
print(graph)
if graph[target_x][target_y]==-1:
    print("KAKTUS")
else:
    print(graph[target_x][target_y])
        