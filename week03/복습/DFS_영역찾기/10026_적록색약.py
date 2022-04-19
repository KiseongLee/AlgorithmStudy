import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

graph = [list(map(str, input())) for _ in range(n)]

visited = [[False]*(n) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y,a):
    
    visited[x][y] = True
    
    for i in range(4):
       nx = x + dx[i]
       ny = y + dy[i]
     
       if 0<= nx <n and 0<= ny <n:
        
          if graph[nx][ny] == a:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, a) 
    

# 색약이 아닐 때
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == "R" or graph[i][j] =="G" or graph[i][j] == "B":
                dfs(i, j, graph[i][j])
                count += 1

print(count, end =' ')

# 색약일 때
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

count = 0
visited = [[False]*(n) for _ in range(n)]

for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        if graph[i][j] == "G" or graph[i][j]=="B":
            dfs(i, j, graph[i][j])
            count += 1
            
            
print(count)       

# 이 문제의 핵심 key는 1) 구분 해줘야할 기준이 3가지가 있을 때, 어떻게 받을 것인가? 2) 다시 색약일 떄, 구분 해줘야할 기준이 2가지 있을 때 어떻게 받을 것인가?

# 문제 자체는 구분 짓는 문제들과 다를게 없는데 0과 1이었던게 3개로 되니까 그걸 받는 방법을 알아야함

# 1)dfs에 문자 하나 더 넣어서 구별 해주면 된다.

# 2)R이랑 G를 똑같이 만들어서 한 번 더 구현해주면 된다.