n, k = map(int, input().split())

data =[]
for i in range(n):
    data.append(int(input()))
    
data.sort(reverse=True)

count = 0
for i in range(n):
    
    count += k // data[i]
    k %= data[i]
    
    
    if k == 0:
        break


print(count)
