import sys
input = sys.stdin.readline
import copy
sys.setrecursionlimit(10 ** 9)

def dfs(x,y):
        

       visited[x][y] = True                 #x,y 받자마자 방문처리를 해준다.
       
       for i in range(4):                   # 상하좌우 
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= nx < n and 0 <= ny < n:      # 범위 안에들고
        
            if graph[nx][ny] == 1:          # 그래프 값이 1이고
                if not visited[nx][ny]:     # 방문하지 않았으면
                    visited[nx][ny] = True  # 방문처리 해주고
                    dfs(nx,ny)              # dfs 진행


    
n = int(input())

graph = [list(map(int, input().rstrip())) for i in range(n)]

visited = [[False]*n for i in range(n)]
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
result = []
count = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            if not visited[i][j]:               # 방문 처리 안된 것만
                dfs(i,j)                        # dfs 처리
                cnt += 1                        # 전체 단지 개수
                for a in range(n):
                    for b in range(n):
                        if visited[a][b] == 1:  # visited[a][b]가 1이면
                            count += 1          # 카운트를 해준다
                result.append(count)            # result 값에 넣어준다.
                count = 0                       # count를 0을 해줘야 다음 것이 중복되어지지 않는다

result2 = copy.deepcopy(result)                 # result[1]값은 1,2단지를 포함하므로 조치를 취해줘야함

for i in range(1, len(result)):
    result2[i] = result[i] - result[i-1]        # result2값을 받은 후, 값들을 하나씩 빼주면 정답의 리스트가 나옴

result2.sort()
    
    
print(cnt)
for i in range(len(result2)):
    print(result2[i])