
n = int(input())

data=[]
for i in range(n):
    data.append(int(input()))

d = [0]*(n)

d[0] = data[0]

if n>=2:
    d[1] = data[0]+data[1]

if n>=3:
    d[2] = max(data[1]+data[2], data[0]+data[2])

for i in range(3, n): 
    d[i] = max(data[i]+data[i-1]+d[i-3], data[i]+d[i-2])

print(d[n-1])