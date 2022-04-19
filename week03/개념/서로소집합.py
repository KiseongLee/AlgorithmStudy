# 특정한 원소가 속한 집합을 찾기

def find(parent, x):
    
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기

def union(parent, a, b):
    
    a = find(parent, a)
    b = find(parent, b)
        
    if b > a:
        parent[b] = a
    else:
        parent[a] = b
        

# 노드의 개수와 간선(union 연산)의 개수 입력 받기

v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화

for i in range(e):
    parent[i] = i

# union 연산을 각각 수행

for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)


# 각 원소가 속한 집합 출력

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find(parent, i), end=' ')

# 부모 테이블 출력
print('부모 테이블 출력: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
