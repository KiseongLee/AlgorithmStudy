import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

graph = [[] for i in range(n+1)]
output = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


def dfs(graph, v, visited):
    
    visited[v] = True
    
    
    for i in graph[v]:
        if not visited[i]:
            output[i] = v
        
            dfs(graph, i, visited)

dfs(graph, 1, visited)


for i in range(2,n+1):
    print(output[i])


# 방문하지 않은 것을 기준으로 봐서
# graph의 인덱스를 기준으로 얘는 방문 안한거네 --> 그럼 내가 부모지
# 바로 output값을 넣어줄 수 있다. 즉, else구문이 필요 없어짐
