'''
핵심 : 벽의개수 3개를 어떻게 세워야는가?

2로 변하게 하고 개수 세는 건 쉬운데
벽의 개수 3개를 어떤 기준을 가지고 세워야하는지는 모르겠다.

2의 상하좌우 봐서 0인 것을 1로 바꾸려고 했는데 그게 안되는 경우가 너무 많아서
1로 둘러쌓여 있는 곳을 봐야 하는 건가?라는 생각이 들음
근데 또 아닌 것도 있어서
'''
import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(m)]

graph_copy = copy.deepcopy(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_region = 0

def dfs(x,y,map):
    
    map[x][y] = 2
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<m and 0<=ny<n:
            if map[nx][ny] == 0:
                dfs(nx, ny, map)

def wall(start, cnt):
    global safe_region
    if cnt == 3:
        final_graph = copy.deepcopy(graph_copy)
        
        for i in range(m):
            for j in range(n):
                if final_graph[i][j] == 2:
                   dfs(i, j, final_graph)
        safe_count = sum(_.count(0) for _ in final_graph)
        safe_region = max(safe_region, safe_count)
        return
    
    else: # 벽이 3개 선택되지 않은 경우
        for i in range(start, n*m): # 브루트-포스로 벽 선택
            r = i // n # n으로 나눈 몫는 행
            c = i % n # n으로 나눈 나머지는 열
            if graph_copy[r][c] == 0: # 해당 구역이 0인 경우에
                graph_copy[r][c] = 1 # 벽으로 선택
                wall(i,cnt+1) # 다음 벽 선택
                graph_copy[r][c] = 0 # 되돌리기
            

wall(0, 0)
print(safe_region)

#https://deep-learning-study.tistory.com/619