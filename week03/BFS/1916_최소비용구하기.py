import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]    
for i in range(m):
    a,b,c = map(int,input().split())            # 비용까지 넣어서 graph를 만들어준다!
    graph[a].append((b,c))

x, y = map(int, input().split())                

distance = [INF] * (n+1)


def dijkstra(start):                            # 다익스트라 알고리즘 시작
    
    q = []                                      # q를 리스트로 만들고
    heapq.heappush(q, (0, start))               # 힙큐를 사용한다.
    distance[start] = True
    while q:
        
        dist, now = heapq.heappop(q)            # dist, now값을 뽑아낸다
        
        if distance[now] < dist:                # distance[now]가 dist보다 크다면 끝
            continue
        
        for i in graph[now]:                    # 그래프 now안에 i값 즉 다음 값들을 뽑아낸다음
            cost = i[1] + dist                  # 거리를 계산해본다. cost = i[1] + dist = distance[now]
            
            if distance[i[0]] > cost:           # distance[i[0]] 값 갱신해줄 필요가 있나? 보는 것이다
               distance[i[0]] = cost
               heapq.heappush(q, (cost ,i[0]))
               
dijkstra(x)


print(distance[y])