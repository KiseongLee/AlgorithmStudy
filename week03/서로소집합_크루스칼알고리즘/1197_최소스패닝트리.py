'''
크루스칼 알고리즘

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.

2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    - 사이클이 발생하지 않는 경우 최소 스패닝 트리에 포함 시킨다.
    - 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 거친다.

'''
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0]*(v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):            #부모가 같으면 사이클이 발생하므로 이 식을 써줘야함
        union_parent(parent, a, b)              # 부모 값이 바뀌는 거다, 그 노드가 바뀌는게 아니야
                                                # 즉, parent[b]=a로 바뀌는 것이기 때문에
                                                # 그 노드가 바뀌는 것이라고 착각하지 말기
                                                # 어? 같은 집합 아닌거 아니야? 하지말기 
        result += cost

print(result)
print(parent)

    


