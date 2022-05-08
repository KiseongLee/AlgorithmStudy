import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x,y):
    
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    
    if graph[x][y] == 1:
     
       graph[x][y] = 0
     
       dfs(x+1, y)
       dfs(x-1, y)
       dfs(x, y+1)
       dfs(x, y-1)
       dfs(x-1, y-1) # 왼쪽위 대각선
       dfs(x-1, y+1) # 오른쪽 위 대각선
       dfs(x+1, y-1) # 왼쪽아래 대각선
       dfs(x+1, y+1) #오른쪽아래 대각선
       return True    
    return False


while True:
    m, n = map(int, input().split())
    
    if (m == 0 and n == 0):
        break
    graph = [list(map(int, input().split())) for i in range(n)]
    count = 0
    
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                count += 1   
    print(count)


    
    

