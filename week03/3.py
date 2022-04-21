import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distance = [0]*(n+1)
X,Y = map(int, input().split())


def bfs(b, start):
    
    q = []
    heapq.heappush(q, [b, start])
    
    
    while q:
        
        cost, index = heapq.heappop(q)
    
        
        for x,y in graph[index]:
            
            if cost == 0:
                distance[x] = y
                heapq.heappush(q, [-distance[x], x])
                continue
            
            if -cost > y :
              if distance[x] < y:
                  distance[x] =y
                  heapq.heappush(q, [-distance[x], x])
            else:
              if distance[x] < -cost:
                 distance[x] = -cost
                 heapq.heappush(q, [-distance[x], x])
                    
bfs(0, X)               
print(distance[Y])