n, m = map(int, input().split())

M = list(map(int, input().split()))
C = list(map(int, input().split()))

C_max = sum(C)

d = [0] * (C_max+1)

for i in range(n):
    for j in range(C_max, C[i]-1, -1):
        d[j] = max(d[j], d[j-C[i]] + M[i])
        
        
        
for i in range(len(d)):
    if d[i] >= m:
        print(i)
        break