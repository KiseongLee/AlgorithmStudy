'''
문제 : 특정한 도시 X로 부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램

입력 : 도시의 개수 N[2, 300000], 도로의 개수 M[1, 백만], 거리 정보 K[1, 30만], 출발 도시 번호 X[1, N]
      M개의 줄에 거쳐서 두개의 자연수 A,B가 공백을 기준으로 구분되어짐 (A->B / [1,N]) 자기자신 못감

'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited, distance):

    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        
        v = queue.popleft()
        for i in graph[v]:
            
            if not visited[i]:
                
                distance[i] = distance[v]+1         # distance 놓고 전에 거에 1 더하는 것이 핵심
                queue.append(i)
                visited[i] = True
                

n, m, k, x = map(int, input().split())


graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)

distance = [-1]*(n+1)
distance[x] = 0


bfs(graph, x, visited, distance)

for i in range(1, n+1):
    if distance[i] == k:
        print(i)

if not k in distance:
    print(-1)