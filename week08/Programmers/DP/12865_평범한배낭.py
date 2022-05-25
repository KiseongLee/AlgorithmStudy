n, k = map(int, input().split())

cap = []
for i in range(n):
    w, v = map(int, input().split())
    cap.append([w,v])

cap.sort()
d = [0] * (k+1)

for i in range(n):
    for j in range(k, cap[i][0]-1, -1):
    
        d[j] = max(d[j], d[j-cap[i][0]] + cap[i][1])
        
print(d[k])