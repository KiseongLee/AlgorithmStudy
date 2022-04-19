import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)

def dfs(x):
    
    visited[x] = True

    
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            
count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)

            
    