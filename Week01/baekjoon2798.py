
from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))

data_a =[]
for i in combinations(data, 3):
    data_a.append(i)
# data_a.sort()
# print(data_a)

data_sum = []
for i in range(len(data_a)):
    data_sum.append(sum(data_a[i]))
data_sum.sort()

# print(data_sum)
# print(len(data_sum))

for i in range(len(data_sum)):

    if data_sum[i] > m:
       print(data_sum[i-1])
       break
     
    if i == len(data_sum)-1:
        print(data_sum[len(data_sum)-1])
        
