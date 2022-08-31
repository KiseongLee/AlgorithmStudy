import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x,y):
    if x<= -1 or y <= -1 or x>=h or y>=w:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
        
    return False


while True:
    w, h = map(int, input().split())

    dx = [-1,1,0,0,-1,1,-1,1]
    dy = [0, 0,-1,1,-1,-1,1,1]
 
    if w == 0 and h == 0:
        break
    
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                result += 1
    
    print(result)
