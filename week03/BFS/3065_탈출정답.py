from collections import deque
import sys
input = sys.stdin.readline


r, c = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(r)]
distance = [[0]*c for _ in range(r)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            queue.appendleft((i,j))
           
        
        elif graph[i][j] == '*':
             queue.append((i,j))
             
        elif graph[i][j] == 'D':
            target_x = i
            target_y = j
            
            
      

def bfs(target_x, target_y):
    
    while queue:
        
        x,y= queue.popleft()
        
        if graph[target_x][target_y] =='S':
            return distance[target_x][target_y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx>=r or ny >= c:
                continue
            
            if graph[x][y] == 'S' and (graph[nx][ny] =='.' or graph[nx][ny] =='D'):
                graph[nx][ny] = 'S'
                distance[nx][ny] = distance[x][y]+1
                queue.append((nx, ny))
            
            if graph[x][y] == '*' and (graph[nx][ny] =='.' or graph[nx][ny]=='S'):
                graph[nx][ny] = '*'
                queue.append((nx, ny))
                
    return "KAKTUS"
        
            
print(bfs(target_x, target_y))
        