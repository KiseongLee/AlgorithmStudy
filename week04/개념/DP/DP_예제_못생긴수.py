n = int(input())

data = [2, 3, 5]

result =[1]

idx = 0
while True:
    
    for i in range(len(data)):
        result.append(result[idx]* data[i])
        x = set(result)
        result = list(x)
        result.sort()
        
    idx += 1
    
    if len(result) >= n:
        break
        

print(result[n-1])

# 뇌피셜로 문제품



n = int(input())

ugly =[0]* n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    
    ugly[l] = min(next2, next3, next5)
    
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5]* 50