from heapq import heappop, heappush
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
P1, P2 = map(int, input().split()) # P1에서 P2로 가는 최댓값을 구함
dist = [0] * (N+1)                 # 거리테이블 만듬
que = []                           # heapq 사용
heappush(que, (0, P1))             # 거리 : 0, 출발 : P1
while que:                         
    ds, s = heappop(que)           # 거리(ds), 인덱스(s) 뽑아냄
    if s == P2:                    # 인덱스가 P2이면 브레이크
        break
    for e, w in graph[s]:          # 인덱스(e), 거리(w) 뽑아냄
        d = w if not -ds else min(-ds, w) # d라는 값은 현재 거리(ds)와 다음 거리(w)와 비교한 값 중에 작은 것 // 0처리는 따로 해줘야함
        if dist[e] < d:                   # 거리테이블에 있는 다음 인덱스의 값과 d값을 비교해서 큰 값을   
            dist[e] = d                   # 거리테이블에 초기화 해준다.
            heappush(que, (-d, e))        # heappush해준다.
print(dist[P2])                           