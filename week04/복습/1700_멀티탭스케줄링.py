import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = list(map(int, input().split()))
pluged = []

count = 0
for index, num in enumerate(data):
    
    if len(pluged) < n :
        pluged.append(num)
        continue
    
    if num in pluged: # 2랑 바로 2가 못들어오니까 이게 밑에 있어도됨
        continue
    
    temp = (0,0)
    for num_p in pluged:
        
        if num_p not in data[index:]:
            temp = (num_p,)
            break
        
        idx = data[index:].index(num_p)
        
        
        if temp[1] < idx:
            temp = (num_p, idx)
            
    pluged.remove(temp[0])
    pluged.append(num)
    count += 1

print(count)

# set은 찾을 때, 시간복잡도 (1)
# list는 찾을 때, 시간복잡도 (N)

