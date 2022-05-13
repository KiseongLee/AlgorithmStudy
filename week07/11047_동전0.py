'''

입력 : n[1,10] k[1, 1억] // N개의 동전 가치 
출력 : k원을 만드는데 필요한 동전 개수 최솟값

'''

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0

for coin in coins:
    if k == 0:
        break
    
    if k // coin != 0:  
       cnt += (k//coin)
       k = (k%coin)         

print(cnt)