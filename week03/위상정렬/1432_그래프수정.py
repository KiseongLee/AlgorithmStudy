import heapq

v = int(input())

indegree = [0] * (v)

graph = [list(map(int, input())) for i in range(v)]
graph_ = [[] for i in range(v)]
anw = [0]*(v)

for i in range(v):
    for j in range(v):
       if graph[i][j] == 1:
          graph_[j].append(i)
          indegree[i] += 1

q = []
n = v
def topology():
    global n,anw
    
    for i in range(v):
        if indegree[i] == 0:
            heapq.heappush(q, -i)
            
    while q:
        now = -heapq.heappop(q)
        anw[now] = n
        
        for k in graph_[now]:
            indegree[k] -= 1
            if indegree[k] == 0:
                heapq.heappush(q, -k)
        n -= 1

topology()


if anw.count(0) >= 1:
        print(-1)
else:
        print(*anw[0:], end = ' ')