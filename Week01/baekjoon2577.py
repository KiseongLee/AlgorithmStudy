a = int(input())
b = int(input())
c = int(input())

total = a*b*c

total = str(total)

arr = [0] * 10

total_arr = []

for i in range(len(total)):
    total_arr.append(total[i])

total_arr = list(map(int, total_arr))

for i in range(len(total_arr)):
    arr[total_arr[i]] += 1

print(arr)
for i in range(len(arr)):
    print(arr[i])

