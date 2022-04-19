import sys
input = sys.stdin.readline

def find(parent, x):
    
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    
    a = find(parent, a)
    b = find(parent, b)
    
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

edges = []
result = 0

parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
       union(parent, a, b)
       result += cost

print(result)