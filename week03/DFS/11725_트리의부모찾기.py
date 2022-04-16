import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

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
            output[v] = i
        else:
            dfs(graph, i, visited)
        
dfs(graph, 1, visited)


for i in range(2,n+1):
    print(output[i])
    
# 이 방법으로 하면 약간 빠르다. 정렬할 필요가 없기 때문에


'''
    
for i in graph[v]:
        if visited[i]:
            output.append((v, i))
        else:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
output.sort()

for i in range(len(output)):
    print(output[i][1])
    


# 방문을 한 것에 값을 받아 와서 output에 넣어준다음
# 정렬을 하는 방식인데
# 조금 느릴 것 같다.
'''