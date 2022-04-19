from collections import deque

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = True
check = []

def bfs():
    global flag,check
    
    while flag:
        for i in range(len(data)):
            check.append(any(data[i]))
    
        if any(check) == False:
            flag = False
            return data
        else:
            check = []
        
        
        queue = deque()
        
        for i in range(n):
            for j in range(m):
                if data[i][j] != 0:
                    queue.append((i, j))
            
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                
                if data[nx][ny] == 0:
                    
                    data[x][y] = data[x][y] -1
                    if data[x][y] <= 0:
                        data[x][y] = -1
                        
        for i in range(n):
            for j in range(m):
                if data[i][j] == -1:
                    data[i][j] = 0
        print(data)
                    
    return data

           

bfs()

# 1. 빙산을 깎는 과정에서 0이 되버리면 안되니까 한번에 바꿔주는 것을 처리함 --> -1 로 변경

# 2. while문을 어떻게 하면 정지할 수 있을까? --> list 내 모든 값이 0이 될 때까지로 반복
#  --> 그런데 문제에서 원하는 건 2개로 분리되었을 때, 개수를 구하는 것이므로 어떻게?
