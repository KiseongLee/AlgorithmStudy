from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0
check = False
queue = deque()

def bfs(x, y):
    queue.append((x,y))                 # 처음 들어 올 때, queue 값 넣어줘야 한다!!
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True            # 처음 것 방문처리 해줘야함    #아래 부터는 밑에서 해줌
        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                   
                
                    if data[nx][ny] != 0 and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        
                    elif data[nx][ny] == 0:
                        count[x][y] += 1
                    
    return 1




while True:
    visited = [[False]*m for _ in range(n)]     # 이것들도 while문 안에서 계속 초기화 해줘야한다
    count = [[0]*m for _ in range(n)]           # 그래야 빙하가 아예 0이 되었을 때도 체크 가능
    result = []
   
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))

    for i in range(n):
        for j in range(m):
            data[i][j] -= count[i][j]
            if data[i][j] < 0:
                data[i][j] = 0
    
    if len(result) == 0:            # 빙산이 다 없어질때까지 분리가 되지 않으면 break
       break                            # 어떻게 가능하지?
    if len(result) >= 2:
        check = True
        break
    year += 1
        
            
# 방문처리 --> bfs 한 번 돌 떄, 방문처리를 함으로써 아래 for문 돌 때, 엄청난 시간적 이득을 볼듯
# count --> 한 번에 깎아줘야 하기 때문에 count를 받아서 아래에서 처리 -->미쳤다
# result --> 둘로 나뉘는 순간의 값을 받아와야 하기 때문에 사용 // visited가 안되있을 때는 위에 queue.append for문이 도니까 
#            bfs가 한번 더 돌꺼아니야 그래서 그러면 result값은 2개가 될거고 --> 생각 절대 못함
            
if check:
    print(year)
else:
    print(0)