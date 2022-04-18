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
graph_inv = [[] for i in range(n+1)]    # 거꾸로 bfs를 사용해야하기 때문에 graph_inv 생성

distance = [0]*(n+1)
edges = set()

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph_inv[b].append((a,c))
    
start, end = map(int, input().split())

def dijkstra(start):            # 도착지의 도시에 최대 경로를 받기위해 다익스트라 알고리즘사용
                                # 원래는 힙큐(logN)를 쓰는데 여기서는 그럴 필요가 없기 때문에
                                # 큐(1)을 사용한다. 계속 시간 초과가 떴었다. 
    
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


def bfs():                          # 거꾸로 bfs를 동작시켜준다.
    queue = deque()
    queue.append((end, 0))
    
    while queue:
        cur_node, cur_cost = queue.popleft()
        # 현재 노드, 현재 비용을 큐에서 빼낸다.
        for post_node, post_cost in graph_inv[cur_node]:
            # graph_inv는 graph의 도착지와 출발지를 거꾸로 만든 그래프
            # post_node = 다음에 갈 노드, post_code = 다음에 갈 노드까지의 비용
            if distance[cur_node] == post_cost + distance[post_node] and tuple((post_node, cur_node)) not in edges:
                # 현재 노드 거리 = 다음에 갈 노드 까지의 비용 + 거리 테이블에 있는 다음에 갈 노드 값   # 나중 노드, 현재 노드가 없다면(중복간선방지)
                # 12(node 7) =   5(node 7에서 node 6 까지) + 7 (거리 테이블 node 6)
                edges.add(tuple((post_node, cur_node)))
                queue.append((post_node, cur_cost+post_cost))
                        # 나중에 갈 노드, 큐에서 빼낸 현재 비용 + 나중 노드로 갈 비용

distance = dijkstra(start)
bfs()
print(distance[end])
print(len(edges))




# https://blog.naver.com/PostView.naver?blogId=gustn3964&logNo=222277117931&parentCategoryNo=&categoryNo=30&viewDate=&isShowPopularPosts=true&from=search
# https://intrepidgeeks.com/tutorial/1948-quasi-critical-path
