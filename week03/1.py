
import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for i in range(n+1)]
graph_inv = [[] for i in range(n+1)]

distance = [0]*(n+1)
edges = set()

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph_inv[b].append([a,c])
    
start, end = map(int, input().split())

def dijkstra(start):
    
    q =[]
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = -heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    

dijkstra(start)
print(distance)