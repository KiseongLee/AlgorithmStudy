# 2022/04/06

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

data = []
for i in range(n):
    data.append(input().rstrip())
    
visited = [False]*n

arr = set()

def recursive(idx, value, visited):
    
    if idx == k :
        
        arr.add("".join(value))
        return
    
    else:
        
        for i in range(n):
            if not visited[i]:
                
                visited[i] = True
                recursive(idx+1, value + [data[i]], visited)
                visited[i] = False
                print(value)


recursive(0, [], visited)
print(len(arr))
