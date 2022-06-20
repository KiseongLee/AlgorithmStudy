# 문제를 분해함

# 1. 순열 -> 모든배열
# 2. 모든 차값(절대값)
# 3. 그 중에서 가장 큰 값(max) - 난이도
# 4. 담고 -> 그 중에서 min -> 가장 최소값
# first try : 메모리 초과

from itertools import permutations
import sys
input = sys.stdin.readline
t = int(input())

'''
for _ in range(t):
    
    n = int(input())
    
    woods = list(map(int, input().split()))
    
    woods_permu =list(permutations(woods, len(woods)))
    
    woods_hard_all = []
    for i in range(len(woods_permu)):
        woods_hard = []
        for j in range(len(woods_permu[i])):
            woods_hard.append(abs(woods_permu[i][j]-woods_permu[i][j-1]))
            # print(woods_hard)
        woods_hard_all.append(max(woods_hard))
        # print(woods_hard_all)
    
    print(min(woods_hard_all))
'''


# for _ in range(t):
    
#     n = int(input())
#     woods_hard = []
#     woods = list(map(int, input().split()))
   
#     woods.sort()
#     print(woods)
#     for i in range(n):
#         woods_hard.append(abs(woods[i]-woods[i-1]))
        
#     hard = max(woods_hard)
#     print(hard)
    
#     if n % 2 == 0:
#         x = n//2+1
#         value = abs(woods[n-1] - woods[x-2])
#         if hard > value:
#             hard = value
#     else:
#         x = n//2 + 1
#         value = abs(woods[n-1] - woods[x-2])
#         if hard > value:
#            hard = value
    
#     print(hard)
        
for _ in range(t):
    
    n = int(input())
    woods_hard = []
    woods = list(map(int, input().split()))
    woods.sort()
    result = 0
    for i in range(2, n):
        result = max(result, abs(woods[i]-woods[i-2]))
    
    print(result)    
    
    