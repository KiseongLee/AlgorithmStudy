import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().rstrip())))


def dfs(x,y):
    global count
    if x<= -1 or y <= -1 or x >= n or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x-1,y), dfs(x,y-1), dfs(x+1,y), dfs(x,y+1)
        return True
    return False

result = 0
count = 0
result_array = []
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            result += 1
            result_array.append(count)
            count = 0


result_array.sort()
print(result)
for i in range(len(result_array)):
    print(result_array[i]) 
            