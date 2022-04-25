n = int(input())
data = [500, 100, 50, 10]

count = 0

for i in data:
    a = n // i
    count += a
    n  %= i

print(count)