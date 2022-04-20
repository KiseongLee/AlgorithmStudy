import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(graph, start, visited):
    
    visited[start] = True
    
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
    
            

n, m = map(int, input().split())

visited = [False] * (n+1)

result = 0

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n+1):
    if not visited[i]:                  # 핵심 key : 생각해보면 한 번돌고 다시 돌때, 방문처리 되있으면 안하는거네 그러면 연결요소 개수 셀 수 있다
       dfs(graph, i, visited)
       result += 1

print(result)