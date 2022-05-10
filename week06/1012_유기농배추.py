import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x,y):
    
    if x >= m or y >= n or x < 0 or y < 0:
        return False
    
    if graph[x][y] == 1:
     
       graph[x][y] = 0
     
       dfs(x+1, y)
       dfs(x-1, y)
       dfs(x, y+1)
       dfs(x, y-1)
       return True    
    return False

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    
    graph = [[0]*n for i in range(m)]
    count = 0
    
    for i in range(k):
       x,y = map(int, input().split())
       graph[x][y] = 1
    
    
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                count += 1   
    print(count)


    
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)    


def dfs(x, y):
    global count
    if 0<= x < m or 0 <= y < n:
        
    
        if graph[x][y] == 1:
            
            graph[x][y] = 0
            
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
            return True
        
        return False

    return False
        

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0]*n for i in range(m)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                count += 1

print(count) 
            
        
        
            
        
    