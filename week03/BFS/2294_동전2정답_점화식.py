import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

table = [10001] * (m+1)
table[0] = 0

for i in range(n):
    for j in range(data[i], m+1):
        table[j] = min(table[j], table[j-data[i]]+1)

if table[m] == 10001:
    print(-1)
else:
    print(table[m])