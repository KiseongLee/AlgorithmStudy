import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    
    a = input().strip()
    
    if " " in a:
        b = a.split(" ")
        queue.append(b[1])
        
    if a == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    if a == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)   
    
    if a == "size":
        if queue:
            print(len(queue))
        else:
            print(0)
    
    if a == "empty":
        if queue:
            print(0)
        else:
            print(1)
    
    if a == "pop":
        if queue:
            x = queue.popleft()
            print(x)
            
        else:
            print(-1)
    
