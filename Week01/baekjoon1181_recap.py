
n = int(input())

data = []
data_len = []
for i in range(n):
    data.append(input())
    data_len.append(len(data[i]))

data_total = []
for i in range(n):
 data_total.append((data[i], data_len[i]))

result = set(data_total)
data_total = list(result)

data_total_sort = sorted(data_total, key=lambda x : (x[1], x[0]))

for i in range(len(data_total_sort)):
    print(data_total_sort[i][0])

