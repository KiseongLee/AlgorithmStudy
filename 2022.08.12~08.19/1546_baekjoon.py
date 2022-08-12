n = int(input())

X = list(map(int, input().split()))

X_max = max(X)

sum = 0
for a in X:
    sum += (a / X_max) * 100

print(sum/n)