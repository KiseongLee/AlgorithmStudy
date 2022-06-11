n = int(input())

wine = []
for i in range(n):
    wine.append(int(input()))

d = [0]*(n)

d[0] = wine[0]

if n>=2 :
    d[1] = wine[0]+wine[1]

if n>=3:
    d[2] = max(wine[0]+wine[1], wine[1]+wine[2], wine[0]+wine[2])

for i in range(3, n):
    d[i] = max(wine[i]+d[i-2], wine[i]+wine[i-1]+d[i-3], d[i-1])

print(max(d))