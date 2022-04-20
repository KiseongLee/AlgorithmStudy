from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0] * (n+1)

def bfs(start):

    q = deque([start])
    
    while q:
        
        v = q.popleft()
        
        for i in graph[v]:
            if check[i] == 0:               # 핵심 check를 만드는 것이고
                q.append(i)
                check[i] = check[v] + 1     # 거기에 전에 거의 check값에 1씩을 더해주는 것이 가장 key point이다.

bfs(start)
if check[end] == 0:
    print(-1)
    
else:
    print(check[end])