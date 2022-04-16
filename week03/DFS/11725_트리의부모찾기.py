import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

graph = [[] for i in range(n+1)]
output = []

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


def dfs(graph, v, visited):
    
    visited[v] = True
    
    
    for i in graph[v]:
        if visited[i]:
            output.append((v, i))
        else:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
output.sort()

for i in range(len(output)):
    print(output[i][1])