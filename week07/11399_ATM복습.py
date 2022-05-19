n = int(input())

p = list(map(int, input().split()))

p.sort()

sum = 0

for i in range(n):
    for j in range(0, i+1):
        sum += p[j]

print(sum)