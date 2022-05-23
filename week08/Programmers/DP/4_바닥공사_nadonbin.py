n = int(input())

d = [0] * (n+1)

d[1] = 1

if n>=2 :
    d[2] = 3

for i in range(3,n+1):
    d[i] = (2*d[i-2] + d[i-1]) % 796796

print(d[n])