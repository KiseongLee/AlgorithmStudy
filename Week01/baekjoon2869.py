# import sys

# a,b,v = map(int, sys.stdin.readline().split())

# sum = a
# day = 1

# while sum >= 0 and sum < v :
#     sum -= b
#     sum += a
#     day += 1

# print(day)

# 시간초과 반복문으로 절대 풀 수 없음

import math
a,b,v = map(int, input().split())

d = (v-a)/(a-b) + 1

print(math.ceil(d))

