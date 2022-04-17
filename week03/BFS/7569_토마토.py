'''
문제 : 토마토 창고에 보관하는 격자 모양의 상자들의 크기와 익은 토마토들과 익지않은 토마토들이 주어졌을 때,
      며칠이 지나면 토마토들이 모두 익는지, 최소 일수를 구해라
      
입력 : 상자의 크기 m[2, 100],n[2, 100] 상자의 수 h[1,100]
      가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토 정보
      가로줄에 들어있는 토마토들의 상태가 M개
      1 = 익은토마토, 0 = 익지 않은 토마노, -1 = 토마토 X
      N개의 줄이 H번 반복하여 주어짐.
      토마토가 하나 이상 있는 경우만 입력으로 주어진다.
      
출력 : 토마토가 모두 익을 때까지 최소 며칠이 걸리는지 계산
      모든 토마토가 익어있는 상태 0
      토마토가 모두 익지는 못하는 상황 -1
      

'''
from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for i in range(n)] for _ in range(h)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()

def bfs():
     
      
      
      while queue:
            z,x,y = queue.popleft()
            
            for i in range(6):
                  nx = x + dx[i]
                  ny = y + dy[i]
                  nz = z + dz[i]
            
                  if nx<0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                     continue
            
                  if graph[nz][nx][ny] == -1:
                     continue
            
                  if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = graph[z][x][y] + 1
                        queue.append((nz,nx,ny))
            

state = True
for i in range(h):
      for j in range(n):
            for k in range(m):
                  if graph[i][j][k] == 1:
                        queue.append((i, j, k))

          
                
bfs()



result = -2

for i in range(h):
      for j in range(n):
            for k in range(m):
                  if graph[i][j][k] == 0:
                        state = False
                  
                  result = max(result, graph[i][j][k])

if not state:
      print(-1)
else:
      print(result-1)