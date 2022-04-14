'''
1. 맨 처음에(1,1)의 위치에서 시작하며, (1,1)의 값은 항상 1이라고 문제에서 언급

2. (1,1)좌표에서 상,하,좌,우로 탐색을 진행하면 바로 옆 노드인(1,2) 위치의 노드를
방문하게 되고 새롭게 방문하는 (1,2) 노드의 값을 2로 바꾸게 된다.

3. 마찬가지로 BFS를 계속 수행하면 결과적으로 다음과 같이 최단 경로의 값들이 
1씩 증가하는 형태로 변경된다.


'''



from collections import deque

n, m = map(int, input().split())


data = [list(map(int, input())) for i in range(n)]



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if data[nx][ny] == 0:
                continue
            
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))
                
    return data[n-1][m-1]

print(bfs(0,0))