from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
def bfs():

  
  while q:
    
    x,y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      
    
      if 0<=nx<n and 0<=ny<m:
        
        
        if graph[nx][ny] == 0:
           graph[nx][ny] = graph[x][y]+1
           q.append((nx,ny))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
       q.append((i,j))


bfs()


state = True
for i in graph:
      if 0 in i:
        state = False
        break

if state:
  print(max(map(max, graph))-1)
else:
  print(-1)
        


'''
마지막 출력

state = True
result=-1
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
       state = False
    result = max(result, graph[i][j])      

if state:
  print(result-1)
else:
  print(-1)
        
'''

# 무한루프가 도는 이유는?
# 토마토 문제에서 핵심 key는 동시에 1이 돌아야 한다는 것이다
# 그래서 밑에 for문에서 bfs를 돌리는 것이 아니라 1이 되는 것을 이미 큐에 다 넣고 돌려야한다.

# 출력할 떄, max값에서 1을 뺴는 이유는??
# 처음에 1부터 시작하니까 당연히 끝에가면 1이 더해져있겠지 -> 그래서 1을 빼줘야함

# 런타임에러가 계속나온다(indexerror)
# bfs할 때, queue 넣는 거에서 문제가 발생하는 거 같다. 
# bfs 파라미터 해결하니까 정답 나옴!!


