import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
m = int(input())

visited = [0]*(n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0

def dfs(x):
    global count
    visited[x] = 1
    
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            count += 1
            dfs(i)
             

dfs(1)


print(count)