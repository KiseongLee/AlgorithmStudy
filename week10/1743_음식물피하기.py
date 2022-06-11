# 음식물피하기

# count 개수만 max로 쳐주면 된다. 
# bfs로 구현 -> 소요시간 20분


from collections import deque

n, m, k = map(int, input().split())

data = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(k):
    x, y = map(int, input().split())
    data[x-1][y-1] = 1
    
max = 0
def bfs(x,y):
    global max
    count = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    
    while q:
        a,b = q.popleft()
        
        for i in range(4):
            na = a+dx[i]
            nb = b+dy[i]
            
            if 0<=na<=n-1 and 0<=nb<=m-1:
                
                if data[na][nb] == 1 and visited[na][nb] == 0:
                    visited[na][nb]=1
                    count += 1
                    q.append([na,nb])
    
    if max < count:
        max = count



for i in range(n):
    for j in range(m):
       if data[i][j] == 1:
           bfs(i,j)
        
print(max)        