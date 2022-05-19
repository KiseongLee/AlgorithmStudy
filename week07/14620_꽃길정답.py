import sys
input = sys.stdin.readline

n = int(input())       

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*(n) for _ in range(n)]   # 꽃을 심을 장소를 체크하기 위해서 사용
flower_dir = [(0,0), (-1, 0),(1,0), (0,-1),(0,1)]   # 상 하 좌 우 중간까지 모두 고려해서 사용
min_value = 1e9

def cal(x,y):       #계산 해주는 함수

    global n
    result = 0
        
    for dx,dy in flower_dir:    # 상하좌우중간값을 싹다 더해서 result값을 구해낸다
        nx = x + dx
        ny = y + dy
        result += graph[nx][ny]
    return result

def check(x, y):        # 예외처리를 해주는 함수
    global n
    for dx,dy in flower_dir:
        nx = x + dx
        ny = y + dy
        if nx<0 or ny <0 or nx > n-1 or ny > n-1 or visited[nx][ny]:    # visited가 무조건 마지막에 나와야한다
                                                                        # 아니면 nx,ny값들이 먼저 visited에 들어가버리면 out of range 떠버림
            return False
    return True

def flower(x, cost, cnt):               # flower함수에 x(가로 좌표 선택하여 for문 줄여주기 가능), cost(비용 모두 계산), cnt(재귀 종료 조건) 
      global min_value
      if cnt == 3:                      # 재귀 종료 조건
          min_value = min(min_value, cost)  #최솟값 갱신
          return
    
      for i in range(1, n):             # x좌표를 먼저 선택 
                                        # (방문처리를 해줬기 때문에 1부터 돌려도 되지만 for문을 돌 때, 앞에 것은 이미 처리하면서 왔기 때문에 )
                                        # (x부터라고 해주면 시간이 훨씬 빠르다.)
          for j in range(1, n):         # y좌표 선택
              if check(i,j):            # check함수가 True면 (예외가 없으면)
                 visited[i][j] = 1      # 그 좌표에 꽃을 심겠다
                 for dy, dx in flower_dir:  # 각 방향(상하좌우중간)에 방문 처리를 해준다 
                     visited[i+dx][j+dy] = True
                 flower(i, cost + cal(i, j), cnt+1) 
                    # 1) x값에는 선택한 좌표의 x좌표가 들어간다
                    # 2) cost에는 cal(i,j)를 넣어줘서 선택한 좌표의 값을 더해주면된다 -> 누적
                    # 3) cnt는 재귀 종료 조건이므로 1을 더해주면 된다. -> 누적
                 visited[i][j] = 0  # 방문 처리를 풀어준다
                 for dy, dx in flower_dir:  # 각 방향(상하좌우중간)에 방문 처리를 풀어준다.
                     visited[i+dx][j+dy] = False
                     
flower(1,0,0)
print(min_value)