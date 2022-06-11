# 인구이동

# 처음 문제를 보았을 때, 간단하게 풀 수 있을 줄 알았음
# 문제점
# 1) 그래프 값들을 바꿔줘야하는데 이걸 어떻게???-> for문 2개 뽑아내는 것을 실수함 -> nation에서 걍 2개씩 뽑아내면 되는구나.. 바보
# 2) 이것이 없을 때까지 돌려야하는데 이걸 어떻게 ?? -> while과 flag 사용해서 풀면 되는 문제.. flag false일 때, break만 잘 걸어주면 된다

from collections import deque


n, L, R = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]



dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(x,y):
    global max, day
    nation = [(x,y)] # 연합된 국가 담기
    count = data[x][y] # 총 연합된 국가 수
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    
    while q:
        a,b = q.popleft()
        
        for i in range(4):
            na = a+dx[i]
            nb = b+dy[i]
            
            if 0<=na<=n-1 and 0<=nb<=n-1:
                
                if L<=abs(data[a][b]-data[na][nb])<=R and visited[na][nb] == 0:
                    visited[na][nb]=1
                    q.append([na,nb])
                    nation.append([na, nb])
                    count += data[na][nb] # count개수 더해주기
    
    for x, y in nation: # 이렇게 for문 사용하는 것
        # print(nation) 
        # print(x)
        # print(y)
        data[x][y] = int(count / len(nation))
    
    return len(nation)    
        
    # print(nation[0])
    # if count >= 1:
    #     day += 1
        
        # sum = 0
        # for i in range(len(nation)):
        #     for x, y in zip(nation[i]):
        #         sum += data[x][y]
        # sumdiv = int(sum / len(nation))
        # for i in range(len(nation)):
        #     for x,y in nation[i]:
        #         data[x][y] = sumdiv


day = 0 # 인구 이동이 발생하는 일수
while True : # 1. 인구 이동이 없을 때까지 반복
    flag = False # 인구 이동 존재 유무 플래그
    visited = [[0]*n for _ in range(n)]
    for i in range(n): # 2. 모든 곳을 bfs로 방문하여 연합 진행
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j) > 1:
                    flag = True  
    if not flag: #3. 지금까지 인구 이동이 없는 경우, 그만
        break
    day += 1
    
print(day)        