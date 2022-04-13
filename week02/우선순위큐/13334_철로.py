import heapq
import copy

n = int(input())

heap =[]
start =[]
count = 0
max_count = 0
for i in range(n):
    h, o = map(int, input().split())
    if h < o:
        heapq.heappush(heap, (h, o))
    else:
        heapq.heappush(heap, (o, h))

heap2 = copy.deepcopy(heap)

l = int(input())



for _ in range(n) :
    x = heapq.heappop(heap)
    start.append(x[0])
    
    

for i in start:
    for j in heap2:
      if i <= j[0] and i+l >= j[1]:
           count += 1
        
    if max_count < count:
       max_count = count
       count = 0
         
    else:
       count = 0

print(max_count)  