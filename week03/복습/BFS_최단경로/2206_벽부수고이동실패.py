from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
cost = [[-1] * (M) for _ in range(N)]
matrix = [list(map(int, input().strip())) for _ in range(N)]
wall = [[0]*(M) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([[0,0]])
cost[0][0] = 1


while q : 
    x,y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 : continue
        
        if cost[nx][ny] == -1:    
            if matrix[nx][ny] == 0 : 
               cost[nx][ny] = cost[x][y] +1 
               q.appendleft([nx,ny])
           
        
            if matrix[nx][ny] == 1:
    
                cost[nx][ny] = cost[x][y] +1
                wall[nx][ny] = wall[x][y] +1
            
                if wall[nx][ny] < 2:
                     q.append([nx,ny])
                else:
                  continue

print(cost[N-1][M-1])
for i in range(len(cost)):
    print(cost[i])
for i in range(len(wall)):
    print(wall[i])   

'''
4 4
0101
0101
0001
1110
'''