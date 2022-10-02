# 구하고 싶은 것 : X로부터 출발하여 도달할 수 있는 도시 중, 최단 거리가 K인 모든 도시

# 조건 : 도시 개수 : N[2,300,000], 도로 : M[1, 백만], 최단 거리 : K[1, 30만], 출발 도시 번호 :X[1, N]

# 최단 거리를 구해야하므로 BFS로 구하자

from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [False]*(n+1)
result = [] 
def bfs(start, distance):
    queue = deque([(start, distance)]) # distance를 들고 다닌다
    
    visited[start] = True
    
    while queue:
        start, distance = queue.popleft()
        
        if distance == k:   # 출력 조건과 일치하면 result에 값을 넣어준다
            result.append(start)    
        
        for i in graph[start]:
            if not visited[i]:
                distance +=1    # distance 갱신
                queue.append((i,distance))
                distance -=1 # for문이 돌기 때문에(dfs가 아님, bfs가 다시 시작되는게 아니기 떄문에) 원상복귀를 해줘야함
                visited[i]=True
bfs(x,0)
if result:
    result.sort()
    for i in range(len(result)):
        print(result[i])
else:
    print(-1)
    