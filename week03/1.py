import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

result = 0
def dfs(start):
  global result
  visited[start] = True
  
  for i in graph[start]:
    if not visited[i]:
        dfs(i)
        result +=1

dfs(1)
   
print(result)