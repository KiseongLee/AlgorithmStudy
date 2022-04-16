import heapq

k, n = map(int, input().split())

data = list(map(int, input().split()))

heap = []
for i in range(k):
    heapq.heappush(heap, data[i])

count = 0

while count < n:
    
   x = heapq.heappop(heap)
   count += 1
   
   if count == n:
       print(x)
       break
        
   for i in range(k):
       y = data[i]*x 
       heapq.heappush(heap,y)
           
       if x % data[i] == 0:
           break

    