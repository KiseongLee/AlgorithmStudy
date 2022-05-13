n = int(input())

k = 1000-n

coins = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coins:
    if k // coin != 0:
        count += k//coin
        k = k % coin

print(count)