


# n, k = map(int, input().split())

# check = [0] * (k+1)

# def dfs(next, cur):
  
#   if next == k:
#     return check[k]
  
#   if next > k:
#      return
  
#   if next < k: 
     
#      check[next] = min(check[next], check[cur] +1)
    
#      dfs(next*2, next)
#      dfs(next+1, next)
#      dfs(next-1, next)
    
# dfs(n, n)     


# from collections import deque
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# max_value = 100000

# def bfs(n, sec):
  
#   q = deque()
#   q.append([n,sec])
  
#   while q:
    
    
#     n, sec = q.popleft()
    
#     if n == k:
#        break
     
#     if n < k:
#        if not n*2 in q:
#         q.append([n*2,sec+1])
#        if not n+1 in q:
#         q.append([n+1,sec+1])
#        if not n-1 in q:
#         q.append([n-1,sec+1])

#   return sec

# print(bfs(n, 0))





from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
max_value = 100000
check = [0]*(max_value+1)

def bfs():
  
  q = deque()
  q.append(n)
  
  while q:
    
    x = q.popleft()
    
    if x == k:
      print(check[x])
      break
    
    for i in (x-1, x+1, x*2):
       if  0 <= i <= max_value and not check[i]:    # max 값 중요
          check[i] = check[x] + 1
          q.append(i)
          

bfs()