import itertools


arr = []
for _ in range(9):
    arr.append(int(input()))

arrc = list(itertools.combinations(arr, 7))

for i in range(len(arrc)):
    if sum(arrc[i]) == 100:
       x = list(arrc[i])
       x.sort()
       break 
    
for i in range(len(x)):
    print(x[i])