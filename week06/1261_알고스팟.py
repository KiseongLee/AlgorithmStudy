import heapq
import sys
input = sys.stdin.readline
INF = 1e9
m, n = map(int, input().split())

graph = [list(map(int, input().rstrip())) for i in range(n)]

distance = [[INF]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
q = []
heapq.heappush(q, (0,0,0))
distance[0][0] = 0

def daijkstra():
   while q:

      cost, x, y = heapq.heappop(q)
    
      if x == n-1 and y == m-1:
        return print(distance[n-1][m-1])
    
      for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          
          if nx < 0 or ny < 0 or nx >= n or ny >= m:
              continue
      
          new_cost = cost + graph[nx][ny]
      
          if new_cost < distance[nx][ny]:
                distance[nx][ny] = new_cost
                heapq.heappush(q, (new_cost, nx, ny))

daijkstra()


        
    
    
    
        
        