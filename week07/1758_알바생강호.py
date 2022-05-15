n = int(input())

tip = []
for _ in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

sum = 0
for i in range(n):
    X = tip[i] - i
    if X > 0:
        sum += X

print(sum) 

