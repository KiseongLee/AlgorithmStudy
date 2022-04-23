T = int(input())


d_0 = [0] * 41
d_1 = [0] * 41

d_0[0] = 1
d_1[1] = 1

for x in range(2, 41):
    
    d_0[x] = d_0[x-1] + d_0[x-2]
    d_1[x] = d_1[x-1] + d_1[x-2]


for i in range(T):
    x = int(input())
    
    print(d_0[x], d_1[x])