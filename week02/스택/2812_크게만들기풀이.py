# import sys

# N,K = map(int, input().split())
# nums = list(map(int,input().strip()))

# result = []
# delNum = K

# for i in range(N):
#     while delNum>0 and result:
#         if result[len(result)-1] < nums[i]:
#             result.pop()
#             delNum-=1
#         else:
#             break
#     result.append(nums[i])
    
# for i in range(N-K):
#     print(result[i],end="")
    
    
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().strip()))

result = []
count = m

for i in range(n):
    while result and count > 0 :
     if  result[-1] < nums[i]:
        
            result.pop()
            count -= 1
     else:
         break
    
    result.append(nums[i])

for i in range(n-m):
    print(result[i], end="")
print()
    
    