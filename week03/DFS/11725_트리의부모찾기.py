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

# 방문 처리를 한 것이 이미 부모이다.
# 왜냐하면 1에 물려있는 애가 4,6이라고 하자
# 1먼저 방문처리하고 4로 들어가서 1이 나오겠지 그건 부모겠지 그리고 방문처리 안된 것은 자식 노드겠지
# 그러면 다시 dfs가 돌 것이고 반대편에 4가 다시 방문처리가 된 거니까 얘가 부모가 되는 거다

# if visited[i]:
#   output[v] = i  
#         자식   부모