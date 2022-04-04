import itertools
import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

data_c = list(itertools.permutations(data, n))


data_final = []
sum=0
max = 0
for i in data_c:
    
    for j in range(n-1):
        sum += abs(i[j]-i[j+1])

    if max < sum:
        max = sum

    sum = 0
    
    

print(max)