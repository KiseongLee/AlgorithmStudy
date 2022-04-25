n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)



ans = 0
count = 0
total = 0
while True:
        
    ans += data[0]
    count += 1
    total += 1

    if count == k:
        ans += data[1]
        total += 1
        count = 0
    
    if total == m:
        break
 
print(ans)   


