from collections import deque
import sys
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
distance[x] = 0


def bfs(graph, start, dist, distance):

    queue = deque([(start, dist)])
    
    while queue:
        
        v, dist = queue.popleft()
        
        if distance[v] < dist:
            continue
        
        for i in graph[v]:
            cost = distance[v]+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                queue.append((i[0], cost))
               

bfs(graph, x, distance[x], distance)

min_value = INF
idx = -1

print(distance[y])