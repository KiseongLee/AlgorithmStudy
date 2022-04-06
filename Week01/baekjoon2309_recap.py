
def permu(idx, value, visited):
    
    if idx == 7:
        arr.append(value)
        return
    
    
    for i in range(9):
       if not visited[i]:
           visited[i] = True
           permu(idx+1, value + [data[i]], visited)
           visited[i] = False

arr=[]

data=[]
for i in range(9):
    data.append(int(input()))




permu(0, [], [False]*9)

for i in range(len(arr)):
    arr[i].sort()


tuple_arr = [tuple(l) for l in arr]
result = set(tuple_arr)
arr = list(result)

idx = 0
for i in range(len(arr)):
    if sum(arr[i]) == 100:
        idx = i

for i in arr[idx]:
    print(i)





# h = list(itertools.combinations(data, 7))

# idx = 0
# for i in range(len(h)):
 
#     if sum(h[i]) == 100:
#         idx = i

# x = sorted(h[idx])

# for i in x:
#     print(i)
    
'''
20
7
23
19
10
15
25
8
13
'''