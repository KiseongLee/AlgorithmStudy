import heapq
import sys
input = sys.stdin.readline

# 우선순위 큐는 heapq에 push했다고 바로 오름차순 정렬되는것이 아니라, heappop을 할 때, 오름 차순으로 나오게되는 것을 의미한다.

n = int(input())

small = []
big =[]

for i in range(n):
    
    x = int(input())
    
    if i == 0:
        center = x
        print(center)
        continue
        
    
    if small:
       a = heapq.heappop(small)[1]
       heapq.heappush(small, (-a, a))
    if big:
       b = heapq.heappop(big)
       heapq.heappush(big, b)
       
    if center > x :
        
        if small:
          if x >= a:
            heapq.heappush(big, center)
            center = x
          else:
             heapq.heappush(small, (-x,x))
            
            
        else:
            heapq.heappush(small, (-x,x))

        
    else:
        
       if big: 
         if x <= b:
            heapq.heappush(small, (-center, center))
            center = x
         else:
             heapq.heappush(big, x)
        
       else:
           heapq.heappush(big, x)
    
    print(center)
    
    
