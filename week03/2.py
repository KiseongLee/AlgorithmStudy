'''
문제 : 모든 도로는 일방통행, 싸이클 없음, 많은 사람들이 시작 도시로부터 도착 도시까지 출발하여 가능한 모든 경로 탐색
      출발한 후 최소 몇시간 후 (마지막에 도착하는 사람까지 도착하는 시간) 만날 수 있는가
      어떤 사람들은 이 시간에 만나기 위해 1분도 쉬지 않고 달려야함. 이런 사람들이 지나는 도로의 수를 카운트
    
입력 : 도시의 개수 n [1,10000] // 도로의 개수 m [1, 100,000] // 셋째줄부터 m+2줄까지 도로의 정보 주어짐 // 출발 도시, 도착 도시
      도로의 출발 도시 번호, 그다음에는 도착 도시 번호, 도로를 지나는데 걸리는 시간 [1,10000]
      모든 도시는 출발 도시로부터 도달이 가능, 모든 도시로부터 도착 도시에 도달이 가능

출력 :  첫째줄에는 이들이 만나는 시간 // 둘째줄에는 1분도 쉬지 않고 달려야하는 도로의 수가 몇개?
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for i in range(n+1)]
graph_inv = [[] for i in range(n+1)]

distance = [0]*(n+1)
edges = set()

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph_inv[b].append((a,c))
    
start, end = map(int, input().split())

def dijkstra(start):
    
    q = deque()
    
    q.append((0,start))
    distance[start] = 0
    
    while q:      
        dist, now = q.popleft()
        
        for i in graph[now]:
            cost = dist + i[1]
            if distance[now] > dist:
                continue
            if cost > distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost, i[0]))
    return distance


def bfs():
    queue = deque()
    queue.append((end, 0))
    
    while queue:
        cur_node, cur_cost = queue.popleft()
        
        for post_node, post_cost in graph_inv[cur_node]:
            if distance[cur_node] == post_cost + distance[post_node] and tuple((post_node, cur_node)) not in edges:
                edges.add(tuple((post_node, cur_node)))
                queue.append((post_node, cur_cost+post_cost))


distance = dijkstra(start)
bfs()
print(distance[end])
print(len(edges))

'''
5
7
1 2 1
1 3 3
2 3 2
2 4 1
4 5 1
3 5 1
2 5 3
1 5
'''