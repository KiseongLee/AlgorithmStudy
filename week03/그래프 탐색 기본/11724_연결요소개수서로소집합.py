from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

result = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    start, end = map(int, input().split())
    union(start, end)

for i in range(1,n+1):  
    find(i)
    
result = len(set(parent))-1
print(result)