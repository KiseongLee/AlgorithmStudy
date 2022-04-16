from collections import deque

def dfs(graph, start, visited):
    
    visited[start] = True
    
    print(start, end=' ')
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    
     queue = deque([start])
    
     visited[start] = True
    
     while queue:
        
        v = queue.popleft()
        print(v, end = " ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

n, m, v = map(int, input().split())

visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)