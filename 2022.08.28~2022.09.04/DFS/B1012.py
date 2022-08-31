import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

t = int(input())

def dfs(x,y):
    
    if x<= -1 or y <= -1 or x >= m or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y), dfs(x,y-1), dfs(x+1,y), dfs(x,y+1)
        return True
    return False

for _ in range(t):
    m,n,k= map(int, input().split())

    graph=[]
    for i in range(m):
        graph.append([0]*n)

    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j):
                result += 1
    print(result)