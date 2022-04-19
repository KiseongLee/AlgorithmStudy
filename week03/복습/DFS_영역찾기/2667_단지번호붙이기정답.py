import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)



n = int(input())    
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def dfs(x,y):
    if x<0 or x>= n or y<0 or y>= n:        # dfs 시작 시, 범위 넘어가면 바로 False
        return False
    
    if graph[x][y] == 1:                    # graph값이 1이면
        global count
        count += 1                          # 바로 count 한다
        graph[x][y] = 0                     # 그리고 0으로 바꿔준다 --> 나중에 셀 때, 편해짐
        for i in range(4):                  # 상하좌우 dfs를 돌려준다
            nx = x + dx[i]                  # 크게 부담 없는게 저 위에 조건이 있기 때문에
            ny = y + dy[i]                  # 범위 넘어가는 거랑, graph[x][y] == 1
            dfs(nx, ny)                     # count는 되면서 밑에 포문의 dfs는 끝이 안난다. 그리고 마지막에 끝내줄 때, result를 +1해주면 된다
        return True                         # return True
    return False
        

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:               # return True를 받으면 최초에 for문에서 돌던게 끝이 났다는 거고 result +1을 해준다
            num.append(count)               # count는 1의 개수이고, 이것은 세면서 다 0으로 바꿔줬다. 그래서 다음 것도 세주기 위해
            result += 1
            count = 0                       # 초기화를 해준다

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])