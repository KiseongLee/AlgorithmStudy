import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

x, y = map(int, input().split())

distance = [INF] * (n+1)


def dijkstra(start):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = True
    while q:
        
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = i[1] + dist
            
            if distance[i[0]] > cost:
               distance[i[0]] = cost
               heapq.heappush(q, (cost ,i[0]))
               
dijkstra(x)


print(distance[y])