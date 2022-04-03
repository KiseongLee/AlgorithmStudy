a = []
for i in range(9):
    a.append(int(input()))


max = 0
index = 0
for i in range(9):
    if max < a[i]:
        max = a[i]
        index = i

print(max)
print(index+1)