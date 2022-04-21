import copy
import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(m)] #list에 괄호 치지 말것!!

graph_copy = copy.deepcopy(graph)       # graph를 복사하는 이유는?
                                        
max_result = 0                          # 안전영역의 최댓값을 구해야하므로

dx = [-1,1,0,0]                         # 상하좌우 이동
dy = [0,0,-1,1]


def wall(cnt):                          # 벽놓기

    if cnt == 3:                        # 3개가 됨과 동시에 BFS 진행
        bfs()
        return
    
    for i in range(m):
        for j in range(n):              # for문으로 전체를 다돌려서
            if graph[i][j] == 0:        # 0인 부분에
                graph[i][j] = 1         # 1을 놓고
                wall(cnt+1)             # wall 재귀함수를 다시 돌려서 3개가 되면 나가겠지?
                graph[i][j] = 0         # 그리고 끝나면 0으로 다시 돌려놓는다.
                
def bfs():
    global max_result                   
    
    queue = deque()                     # BFS 사용하여 탐색할 것이므로
    final_graph = copy.deepcopy(graph)  # graph를 copy해서 사용
    
    for i in range(m):                  # for문을 이용한다 // 가로가 m인거 조심
        for j in range(n):              
            if graph[i][j] == 2:        # 2인 부분을 체크하고
                queue.append((i,j))     # 큐에 그 좌표를 넣어준다
        
    while queue:                        # 큐가 빌 때까지
        x,y = queue.popleft()           # pop 해주고
        for i in range(4):              # 상하 좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:     # 범위안에 들면
                if final_graph[nx][ny] == 0:    # 그래프 복사한 것들이 0이면
                    final_graph[nx][ny] = 2     # 2로 바꿔준다 --> 그래서 복사한 것을 사용한다. 왜냐하면 graph 자체를 건들면 bfs 한 번 할 때마다 계속 graph가 바뀌면 안되니까
                    queue.append((nx, ny))      # 다시 큐로 넣어준다
    
    result = 0                          # 개수 세기
    for i in range(m):                  
        for j in range(n):
            if final_graph[i][j]==0:    # 0이면
                result += 1             # 개수를 세준다
                
    max_result = max(result, max_result)    # 지금까지 세왔던 것과 비교해서 max값을 구한다

wall(0)                                 # wall을 0 돌리면 끝까지 반복할 수 있어서 이거 하나만 동작시키면 된다.
print(max_result)


#https://velog.io/@jungmiin/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%ACBFSDFS18%EC%A3%BC%EC%B0%A8-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-18352-14502-18405-14888
