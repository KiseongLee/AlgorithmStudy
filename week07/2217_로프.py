n = int(input())

weight =[]
for _ in range(n):
    weight.append(int(input()))

weight.sort()

X = weight[0]*n

for i in range(1, n):
    if X < (n-i)*weight[i]:
        X = (n-i)*weight[i]

print(X)