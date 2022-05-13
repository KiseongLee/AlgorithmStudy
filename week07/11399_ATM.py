n = int(input())
cost = list(map(int, input().split()))
cost.sort()
sum = 0
for i in range(n):
    sum += (n-i)*cost[i]

print(sum)