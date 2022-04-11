from collections import deque

queue = deque([])

n = int(input())
for i in range(1, n+1):
    queue.append(i)


for _ in range(n-1):
    
    queue.popleft()
    x = queue.popleft()
    queue.append(x)
    
    
  
    
print(queue[0])
    


    

