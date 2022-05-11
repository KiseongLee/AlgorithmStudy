import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

max_value = max(map(max, graph))

count = 0
answer=[]

def dfs(x,y):
    if x>=n or y>=n or x <0 or y<0:
        return False
    
    if graph2[x][y] >= 1:
        
        graph2[x][y] = 0
        
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    
    return False

for k in range(max_value+1):
    graph2 = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            graph2[i][j] -= k

    for i in range(n):
        for j in range(n):
            if dfs(i,j) == True:
                count += 1
                
    answer.append(count)
    count = 0            


print(max(answer))