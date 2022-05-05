n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
connect = [[] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for i in range(n):
    x,y,d,g = data[i]
    connect[i].append(d)
    for _ in range(g):
        reverse = list(reversed(connect[i]))
        for j in reverse:
            if j + 1 == 4:
                connect[i].append(0)
            else:
                connect[i].append(j+1)

visited = [[False]*101 for i in range(101)]

for i in range(n):
    x,y,d,g = data[i]
    visited[y][x] = True
    for j in connect[i]:
        x,y = x+dx[j], y+dy[j]
        if 0<=x<=100 and 0<=y<=100:
            visited[y][x] = True
            
answer = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
           answer += 1
           
print(answer)  