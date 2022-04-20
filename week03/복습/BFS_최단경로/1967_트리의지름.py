from collections import deque
n = int(input())


graph = [[] for i in range(n+1)]


for i in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))      # 양방향으로 graph를 넣어줌
    graph[b].append((a,c))
   

def bfs(start):
  
  q = deque()
  q.append([0, start])    
  visited =[0]*(n+1)                # 방문처리를 왜 해줘야하나?
  visited[start] = True             
  
  result = [0, 0]                   # result는 왜 있는 거지?
  while q:
    dist, now = q.popleft()
    
    for i in graph[now]: 
      cost = dist + i[1]            # cost = dist + i[1]
      if visited[i[0]] == 0:        # 방문 처리를 해줌과 동시에
        visited[i[0]] = 1
        q.append([cost, i[0]])      # 큐에 값을 넣어 주고
        if result[1] < cost:        # 최댓값을 result에 넣어 준다.
          result[0] = i[0]
          result[1] = cost          
  return result


a = bfs(1)
b = bfs(a[0])
print(b[1])

# 시작값에서 도착값까지 거리만 구하면되는데 길이 하나밖에 없어
# 다익스트라는 시작점을 거쳐서 어디 지점을 들려서 도착 지점 까지 가는데 최댓값을 구하는 거이므로 


