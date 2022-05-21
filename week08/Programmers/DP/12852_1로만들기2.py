n = int(input())
INF = 1e9
d = [INF] * (n+1)
d_list = [0] * (n+1)
d[1] = 0

for i in range(2, n+1):
    
    d[i] = min(d[i], d[i-1]+1)
    d_list[i] = i-1

    if i % 3 == 0 and d[i] > d[i//3]+1:
        d[i] = d[i//3]+1
        d_list[i] = i//3
        
    if i % 2 == 0 and d[i] > d[i//2]+1:
        d[i] = d[i//2]+1
        d_list[i] = i//2


result = [n]
while True:
    if n == 1:
        break    
    result.append(d_list[n])
    n = d_list[n]
        

print(d[len(d)-1])
print(*result, sep=' ')