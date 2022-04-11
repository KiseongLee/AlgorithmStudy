import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

queue = deque()
output = []

for i in range(1,n+1):
    queue.append(i)


idx = 1

while queue:   
    
    if idx == k:
        y = queue.popleft()
        output.append(y)
        idx = 1
    
    else:
        x = queue.popleft()
        queue.append(x)
        idx += 1

output =[str(a) for a in output]
output = (", ".join(output))


print(f"<{output}>")

