from collections import deque
import sys
input = sys.stdin.readline
INF=1e9

n = int(input())
m = int(input())
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
start, end = map(int, input().split())

distance[start]=0
def bfs(start, dist):
    
    queue = deque([(start, dist)])
    
    while queue:
        start, dist = queue.pop()
        
        if distance[start]<dist:
            continue
        
        for i in graph[start]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]]=cost
                queue.append([i[0], cost])
    

bfs(start, 0)
print(distance[end])