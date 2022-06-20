# from copy import deepcopy


# n, m = map(int, input().split())

# data = [0]+list(map(int, input().split()))
# for i in range(m):
    
#     a, b = map(int, input().split())
    
#     if a>b:
#         tmp = a
#         a = b
#         b = tmp
    
#     data_sum = 0
#     for i in range(b-a+1):
#         data_sum += data[a+i]
    
#     print(data_sum)

from copy import deepcopy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [0]+list(map(int, input().split()))
S = deepcopy(data)
for i in range(2, n+1):
    S[i] += S[i-1]
for i in range(m):
    ans = 0
    a, b = map(int, input().split())
    if a>b:
        tmp = a
        a=b
        b=tmp
    ans = S[b] - S[a-1]
    print(ans)