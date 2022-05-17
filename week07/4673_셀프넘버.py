
arr = []
visited = [0] * 10001
for i in range(1, 10001):
    
    n = str(i)
    a = [int(x) for x in n]
    dn = i + sum(a)
    if dn <= 10000:
       visited[dn] = 1
       arr.append(dn)
       

for i in range(1, len(visited)):
    if visited[i] == 0:
        print(i)

