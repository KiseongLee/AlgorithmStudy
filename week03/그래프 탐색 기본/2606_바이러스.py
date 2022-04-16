import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(graph, start, visited):
    global result
    visited[start] = True
    
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
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



dfs(graph, 1, visited)
print(result)


