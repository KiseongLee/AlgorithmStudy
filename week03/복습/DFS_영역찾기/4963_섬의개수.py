import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x,y):
    
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    
    if data[x][y] == 1:
        
        data[x][y] = 0
        
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y+1) # 오른쪽 위 대각선
        dfs(x+1, y+1) # 오른쪽 아래 대각선
        dfs(x-1, y-1) # 왼쪽 위 대각선
        dfs(x+1, y-1) # 왼쪽 아래 대각선

        return True
    return False


while True:
    

    m, n = map(int, input().split())
    
    if n == 0 and m == 0:
        break

    data = [ list(map(int, input().split())) for i in range(n)]


    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    
    print(result)


