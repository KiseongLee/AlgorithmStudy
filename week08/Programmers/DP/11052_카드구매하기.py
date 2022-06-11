n = int(input())


data = [0] + list(map(int, input().split()))

d = [0]*(n+1)

d[1] = data[1]

for i in range(1, n+1):
    for j in range(i, n+1):
        d[j] = max(d[j], d[j-i]+data[i])

print(d[n]) 