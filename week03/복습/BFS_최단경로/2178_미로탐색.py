from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [False]*(n+1)
check = [0] * (n+1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):

    q = deque()
    q.append((x,y))             # 무조건 append로 넣어줘야함 // 이유는 잘 모르겠다 deque에 바로 넣으니까 left할 때, 오류난다.
                                # cannot unpack non-iterable int object
                                # queue = deque([(0,0)])이 맞는 것이다. 그 외에는 위에 오류가 남
                                # 아니면 append를 써서 대괄호를 없앨 수도 있다.
            
    while q:            
       x,y = q.popleft()        # q에서 x,y 뽑고

       for i in range(4):       # 상 하 좌 우 바로 돌려준다.
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:   
          if graph[nx][ny] == 1:
              graph[nx][ny] = graph[x][y] +1        # key point !! 값을 더해주면서 간다
              q.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])