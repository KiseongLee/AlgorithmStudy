from collections import deque
import sys
input = sys.stdin.readline

s = int(input())

visited = [[0]*(2002) for _ in range(2002)]

def bfs(x, y, second):
    
    q = deque([[x, y, second]])
    
    while q:
        
        a, b, sec = q.popleft()
        
        if a == s:
            return print(sec)
        
        if 0<=a<=s and 0<=b<=s:
            if visited[a][a] == 0:
                visited[a][a] = 1
                nb = a
                sec1 = sec
                sec1 += 1
                q.append([a, nb, sec1])
            
            if visited[a+b][b] == 0 and b>0:
                visited[a+b][b] = 1
                na = a+b
                sec2 = sec
                sec2 += 1
                q.append([na, b, sec2])
            
            if visited[a-1][b] ==0:
                visited[a-1][b] = 1
                na = a-1
                sec3 = sec
                sec3 += 1
                q.append([na, b, sec3])


bfs(1,0,0)

