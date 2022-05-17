import itertools


n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr2 = []

arrc = list(itertools.combinations(arr, 3))

for i in range(len(arrc)):
    if sum(arrc[i]) <= m:
        arr2.append(sum(arrc[i]))

print(max(arr2))