import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(start, group):
    global error
    
    if error:                   
        return
    
    visited[start] = group
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)
        elif visited[start] == visited[i]:  # 인접한 노드가 같은 group을 가지고 있다면
            error = True                    # error = True --> 이분 그래프가될 수 없음
            return                          # return 해줌


T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)         # 방문한 정점 체크
    error = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:  # 만약 아직 방문하지 않았다면
            dfs(i, 1)       # dfs를 돈다.
            if error:       # 만약 에러가 참이라면
                break       # 탈출

    if error:
        print('NO')
    else:
        print('YES')