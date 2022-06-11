# visited를 count로 쓸 생각을 어떻게 했을까?
# 처음에 count를 변수 1개로 썼었는데 왜 안될까?
# 나는 +를 하고 나서 -를 하면 된다고 생각했고, 그리고 예외처리를 하면 된다고 생각했는데
# 0층에 왔을 때를 처리하는 것이나 아니면 D=0이될 때, 수많은 예외를 만났고 결국 83%에서 오류가 남
# 0층 처리를 하면 또 틀렸다고 나오고 이 것의 원인은 무엇일까 생각을 해보았는데
# count를 일단 변수 1개로 받으면 안되는 것 같음
# -> 간단하게 하려면 두개로 받으면 되긴 하겠다.

# 분기를 하는 문제는 -> count를 들고다니는 것이 풀이방법!!!

from collections import deque
import sys
input = sys.stdin.readline


F, S, G, U, D = map(int, input().split())


def bfs(x):
    
    global G, U, D
    q = deque()
    q.append(x)
    visited = [0] * (F+1)
    visited[x] = 1
    
    while q:
        
        a = q.popleft()

        if a == G:
            return print(visited[G]-1)
        
        up = a + U
        down = a - D
        
        if up <= F and not visited[up]:
            q.append(up) 
            visited[up] = visited[a]+1
            
        if down > 0 and not visited[down]:
            q.append(down)
            visited[down] = visited[a]+1
            
    else:
        return print("use the stairs")
    

        
  
        
    
bfs(S)