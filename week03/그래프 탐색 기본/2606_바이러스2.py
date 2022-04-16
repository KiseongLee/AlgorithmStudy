from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start, visited):
     global result
     queue = deque([start])
    
     visited[start] = True
    
     while queue:
        
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1

n = int(input())
m = int(input())

visited = [False] * (n+1)

result = 0

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(graph, 1, visited)
print(result)