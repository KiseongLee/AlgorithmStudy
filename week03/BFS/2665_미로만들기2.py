import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  


n = int(input())
graph = [list(map(int, input().rstrip())) for i in range(n)]
distance = [[INF]*(n) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    
    q =[]
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    
    while q:
        cost, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(distance[n-1][n-1])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[nx][ny] == 0:
                a = 1
                new_cost = cost + a
            else:
                new_cost = cost

            if new_cost < distance[nx][ny]:             # 이 코드 때문에 무한 반복이 안되겠네
                distance[nx][ny] = new_cost             # heappush 자체를 new_cost가 작아질 때만 하는 거니깐
                heapq.heappush(q, (new_cost, nx, ny))
            


dijkstra()

