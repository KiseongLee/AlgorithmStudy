import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for i in range(n+1)]
graph_inv = [[] for i in range(n+1)]
indegree = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
edges = set()

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph_inv[b].append((a,c))
    indegree[b] += 1
    
start, end = map(int, input().split())

def topology():
    
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i,0))
            
    while q:
        cur_node, cur_cost = q.popleft()
        
        
        for post_node, post_cost in graph[cur_node]:
            indegree[post_node] -= 1
            distance[post_node] = max(distance[post_node], distance[cur_node]+post_cost)
            if indegree[post_node] == 0:
                  q.append((post_node, cur_cost+post_cost))
                  
    return distance


def bfs():
    queue = deque()
    queue.append((end, 0))
    
    while queue:
        cur_node, cur_cost = queue.popleft()
        
        for post_node, post_cost in graph_inv[cur_node]:
            if distance[cur_node] == post_cost + distance[post_node] and tuple((post_node, cur_node)) not in edges:
                edges.add(tuple((post_node, cur_node)))
                queue.append((post_node, cur_cost+post_cost))


distance = topology()
bfs()
print(distance[end])
print(len(edges))