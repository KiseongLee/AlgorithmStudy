n = int(input())

data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort(key=lambda x:(x[1], x[0]))


X = data[0][1]
count = 1
for i in range(1, n):
    if X <= data[i][0]:
        X = data[i][1]
        count += 1
        
print(count)