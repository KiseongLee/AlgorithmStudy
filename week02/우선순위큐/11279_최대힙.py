import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())



for i in range(n):
    
    x = int(input())
    
    if x == 0:
       if not heap:
            print(0)
        
       else:
           a = heapq.heappop(heap)[1]
           print(a)
       
       
       
    else:
       heapq.heappush(heap, (-x, x))
       
    
    