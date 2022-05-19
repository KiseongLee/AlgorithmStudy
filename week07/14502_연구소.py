from collections import deque
import copy
import sys
n, m = map(int, input().split())
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(n)]

max_result = 0      # max값 갱신을 위해서

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]

def wall(cnt):      # 벽 3개를 놓는 함수
    
    if cnt == 3:    # 벽 3개 (cnt=3) 재귀 종료 조건
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1     # 벽을 1개 놓고
                wall(cnt+1)         # cnt 값을 증가시키면서 다시 탐색하여 놓을 곳을 찾는다 -> 3번이 되면 알아서 나가고 
                                    #                                          -> 2번이 된 것에서 for문이 계속 탐색하므로 모든 경우의 수 검색 가능
                graph[i][j] = 0     # 다시 0으로 바꿔줘서 초기화를 시킨다
                
def bfs():      # 3개의 벽을 놓은 후, 1. 바이러스 상하좌우 퍼짐 + 2. 안전 영역 크기 구하기
    
    global max_result
    q = deque()                     # 1. 바이러스 상하좌우 퍼짐 구하기 
    graph_cp = copy.deepcopy(graph) # 바이러스가 퍼지므로 graph를 복사해놓는다.
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:    # 바이러스 포인트를 찾아서
                q.append([i,j])     # q에 넣어준다. -> 상하좌우로 움직여서 graph값을 바꿀 것이다.
    while q:
        x,y = q.popleft()           # 바이러스 포인트를 하나씩 빼고
        for i in range(4):          # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]    
        
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:   # 예외 처리 부분
            
             if graph_cp[nx][ny] == 0:  # 상하좌우가 0이면
                graph_cp[nx][ny] = 2    # 2로 전염시킨다
                q.append([nx, ny])      # 그리고 그 값들을 다시 큐에 넣는다
    
    result = 0                          # 1. 과정이 다 끝나면 2. 안전 영역의 크기 구하고 최대값 갱신하기 
    for i in range(n):
        for j in range(m):              # 2중 포문을 돌려서
            if graph_cp[i][j] == 0:     # 0의 값이면
                result += 1             # 결과값에 1을 더해줘서 안전영역의 크기를 구한다.
    
    max_result = max(result, max_result)    # 최댓값을 갱신해준다.
    
wall(0)
print(max_result)



