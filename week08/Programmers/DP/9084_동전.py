t = int(input())
INF = 1e9

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    d = [0]*(m+1)
   

    for i in range(m+1):
        if i%coins[0] ==0:
            d[i] += 1

    for i in range(1, n):
        for j in range(coins[i], m+1):
            d[j] += d[j-coins[i]]
    
    print(d[m])
