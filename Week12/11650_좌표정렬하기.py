n = int(input())

data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

data.sort(key=lambda x:(x[0], x[1]))

for i in range(len(data)):
    print(*data[i])