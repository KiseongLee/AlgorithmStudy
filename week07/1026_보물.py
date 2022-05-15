# import itertools
# n = int(input())
# INF = 1e9

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# per = list(itertools.permutations(A, len(A)))

# print(per)

# min_value = INF
# sum = 0
# for i in range(len(per)):
#     for j in range(n):
#         sum += per[i][j]*B[j]
#     if min_value > sum:
#         min_value = sum
#     sum = 0

# print(min_value)

import itertools
n = int(input())
INF = 1e9

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

sum = 0

for i in range(n):
    sum += A[i]*B[i]

print(sum)
