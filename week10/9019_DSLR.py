

# t = int(input())

# def bfs(a,b):
    
  
#     global count_d, count_s, count_l, count_r
#     D=a
#     S=a
#     L=a
#     R=a
#     while True:
        
#         if 2*D > 9999:
#             D = 2*D % 10000
#         D = 2*D
#         count_d += 1
        
#         if D == b:
#             return print("D"*count_d)
        
#         if S == 0:
#             S = 9999
#         S = S-1
#         count_s += 1
        
#         if S == b:
#             return print("S"*count_s)
        
        
#         x1 = deque(str(L))
#         x1.rotate(-1)
#         L1=[]
#         for i in range(len(x1)):
#             L1.append(x1.popleft())
#         L = int("".join(L1))
#         count_l += 1
        
#         if L == b:
#             return print("L"*count_l)
            
        
#         x2 = deque(str(R))
#         x2.rotate(1)
#         R1=[]
#         for i in range(len(x2)):
#             R1.append(x2.popleft())
#         R = int("".join(R1))
#         count_r += 1
        
#         if R == b:
#             return print("R"*count_r)
    
    
# for i in range(t):
    
#     a, b = map(int, input().split())
#     count_d = 0
#     count_s = 0
#     count_l = 0
#     count_r = 0
    
#     bfs(a,b)
   
from collections import deque
import sys
input = sys.stdin.readline




def bfs(start, end):
    
    visited = [False]*10000 #주의!!
    q = deque()
    q.append([start, ""])
    visited[start] = True
    
    while q:
        
        num, operation = q.popleft()
        
        if num == end:
            return print(operation)
        
        if not visited[2*num%10000]:
            visited[2*num%10000] = True
            q.append([2*num%10000, operation+"D"])
        
        if not visited[(num-1)%10000]:
            visited[(num-1)%10000] = True
            q.append([(num-1)%10000, operation+"S"])
        
        if not visited[num%1000*10+num//1000]:
            visited[num%1000*10+num//1000] = True
            q.append([num%1000*10+num//1000, operation+"L"])
            
        if not visited[num%10*1000+num//10]:
            visited[num%10*1000+num//10]=True
            q.append([num%10*1000+num//10, operation+"R"])
            
t = int(input())

for i in range(t):
    
    a, b = map(int, input().split())
    bfs(a,b)