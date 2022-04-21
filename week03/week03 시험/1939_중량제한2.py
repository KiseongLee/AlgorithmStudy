import sys
from collections import deque

def bfs(d, e, mm):              # BFS 시작
    q = deque()                 # 큐를 만든다
    visited = [0]*(n+1)         # visited를 만든다
    q.append(d)                 # 사작값(d)을 넣어준다.
    visited[d] = 1              # 방문처리를 해준다.

    while q:                    
        v = q.popleft()         # 시작값을 빼내면서 거기에 next들을 하나씩 뽑아낸다.
        if v == e:              # 시작값과 끝값이 같아지면 (append가 끝값까지 된다는 것은 이진 탐색한 mid값을 다 통과한다는 것을 의미한다)                                
            return True         # 그래서 True로 return이 가능하다
        for i in graph[v]:      # 시작값부터 next들을 하나씩 뽑아낸다.
            if visited[i[0]]==0 and i[1] >= mm: # 시작값의 인덱스가 visited가 되어 있지 않고, 거리가 이진 탐색한 것 보다 크거나 같다면
                visited[i[0]] =1                # 방문 처리를 해주고
                q.append(i[0])                  # 인덱스 값을 다시 append 해준다.
    return False                                # 이외의 경우에 False를 출력한다.

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

d, e = map(int, input().split())
left, right = 1, int(1e9)           # 전체 범위를 left, right 값으로 바꾼다. // 현재 300ms // c값만 받고 최댓값으로 구간을 정해봤지만 오히려 시간이 더 높게나옴(312ms)//크게 차이 없는듯하다

while left <= right:                # 이진 탐색 시작
    
    mid = (left + right)//2         # mid 값을 구해준다. 

    if bfs(d, e, mid):              # mid 값을 넣고 BFS 를 시작한다.
        answer = mid                # answer값으로 mid를 넣어준다
        left = mid + 1              # 더 맞는 값을 갖기 위해서 mid값을 조금 더 올려본다
    else:
        right = mid -1              # 조건에 부합하지 않는다는 것(False)이므로 right값을 내리면서 mid 값을 내려본다
        
print(answer)

'''
6 12
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
3 6 7
1 3 11
5 6 12
6 3
9

7

'''