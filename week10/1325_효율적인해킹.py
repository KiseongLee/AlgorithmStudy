from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = []
for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)
    


# def dfs(x):
    
#     global count
#     if not visited[x]:
#         visited[x] = True
        
#     for i in graph[x]:
#         if visited[i] == False:
#             visited[i] = True
#             count += 1
#             dfs(i)

# for i in range(1, n+1):
#     count = 0
#     visited = [False]*(n+1)
#     dfs(i)
#     ans.append(count)


def bfs(x):
    
    global count
    q = deque()
    q.append(x)
    visited[x] = True
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                count += 1
                q.append(i)


for i in range(1, n+1):
    count = 0
    visited = [False]*(n+1)
    bfs(i)
    ans.append(count)
    
for i in range(n):
    if ans[i] == max(ans):
        print(i+1, end=" ")