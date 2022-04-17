from collections import deque


n = int(input())


data = [list(map(int, input())) for i in range(n)]
distance = [[-1]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    
    queue = deque()
    queue.append([x,y])
    distance[0][0] =0
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if distance[nx][ny] == -1:                      # 핵심key : 이 코드가 없으면 무한반복
                                                            # 이미 바뀌었으면 들어가지 못하게 한다. 
                                                            # 생각을 해보면 data는 안바뀔거야 --> 계속해서 조건이 돈다. 그러면 queue에 계속들어가고 while 무한반복
                                                            # 그러면 distance가 어차피 가중치로 바뀌다 보니깐
                                                            # 한 번 갱신되면 최솟값으로 갱신되겠지
                                                            # 가중치가 작은 것들부터 계속해서 나오니까
                                                            # 그렇게 되면 또 바꿀필요가 없는거지.
                                                            
                if data[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y]+1
                    queue.append([nx,ny])                   # 가중치가 있는 것은 제일 마지막에 넣는다
            
                else:
                    distance[nx][ny] = distance[x][y]
                    queue.appendleft([nx,ny])               # 가중치가 없는 것은 제일 앞에 넣는다
                
    return distance[n-1][n-1]

    
print(bfs(0,0))

