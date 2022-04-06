# 외판원 순회 2 / 2022.04.06


import sys
input = sys.stdin.readline

n = int(input())

cities = []
for i in range(n):
    cities.append(list(map(int, input().split())))

min_value = sys.maxsize

def dfs(start, next, value, visited):
    
    global min_value
    if len(visited) == n:
        if cities[next][start] != 0:
            
           min_value = min(min_value, value + cities[next][start])
        
           return min_value
    
    else:
        
        for i in range(n):
            if cities[next][i] != 0 and not i in visited and value < min_value:
                
                visited.append(i)
                dfs(start, i, value+cities[next][i], visited)
                visited.pop()
    

for i in range(n):
    dfs(i, i, 0, [i])

print(min_value)

