import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
sum = 0
for i in range(n):
    
 a = int(input())
    
 heapq.heappush(heap, a)

while len(heap) != 1 :
    
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)

    sum += x+y
    heapq.heappush(heap, x+y)
       

print(sum)
